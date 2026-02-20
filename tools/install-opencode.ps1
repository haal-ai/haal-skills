# =============================================================================
# OpenCode Installer Wrapper (Windows PowerShell)
# Installs OpenCode and configures GitHub Copilot as the default provider
# =============================================================================

$ErrorActionPreference = "Stop"

$ConfigDir = "$env:USERPROFILE\.config\opencode"
$ConfigFile = "$ConfigDir\opencode.json"

Write-Host "=== OpenCode Corporate Installer ===" -ForegroundColor Cyan
Write-Host ""

# Step 1: Install or update OpenCode
Write-Host "[1/3] Installing/updating OpenCode..." -ForegroundColor Yellow
$opencodeCmd = Get-Command opencode -ErrorAction SilentlyContinue
if ($opencodeCmd) {
    $current = opencode --version 2>$null
    if (-not $current) { $current = "0.0.0" }
    try {
        $latest = (Invoke-RestMethod -Uri "https://registry.npmjs.org/opencode-ai/latest" -ErrorAction Stop).version
    } catch {
        $latest = $null
    }

    if ($latest -and ($current -ne $latest)) {
        Write-Host "  Update available: $current -> $latest"
        Write-Host "  Updating..."
    } else {
        Write-Host "  OpenCode $current is up to date."
        $skipInstall = $true
    }
} 

if (-not $skipInstall) {
    # Try scoop first, fall back to npm
    $scoopCmd = Get-Command scoop -ErrorAction SilentlyContinue
    $npmCmd = Get-Command npm -ErrorAction SilentlyContinue

    if ($scoopCmd) {
        Write-Host "  Installing via Scoop..."
        scoop install opencode
    } elseif ($npmCmd) {
        Write-Host "  Installing via npm..."
        npm i -g opencode-ai@latest
        # Ensure npm global bin is in PATH for this session
        $npmGlobalDir = "$env:APPDATA\npm"
        if ($env:Path -notlike "*$npmGlobalDir*") {
            $env:Path += ";$npmGlobalDir"
            Write-Host "  Added $npmGlobalDir to PATH for this session."
            Write-Host "  To make permanent, add it to your system PATH."
        }
    } else {
        Write-Host "  ERROR: No supported package manager found (scoop or npm)." -ForegroundColor Red
        Write-Host "  Please install one of: scoop, npm, chocolatey"
        exit 1
    }
}

Write-Host ""

# Step 2: Create user-level config
Write-Host "[2/3] Configuring GitHub Copilot provider..." -ForegroundColor Yellow

if (-not (Test-Path $ConfigDir)) {
    New-Item -ItemType Directory -Path $ConfigDir -Force | Out-Null
}

$newConfig = @{
    '$schema'          = "https://opencode.ai/config.json"
    enabled_providers  = @("github-copilot")
    model              = "github-copilot/claude-sonnet-4"
}

if (Test-Path $ConfigFile) {
    Write-Host "  Existing config found at $ConfigFile"
    Write-Host "  Backing up to ${ConfigFile}.bak"
    Copy-Item $ConfigFile "${ConfigFile}.bak"

    try {
        $existing = Get-Content $ConfigFile -Raw | ConvertFrom-Json
        $existing | Add-Member -NotePropertyName "enabled_providers" -NotePropertyValue @("github-copilot") -Force
        $existing | Add-Member -NotePropertyName "model" -NotePropertyValue "github-copilot/claude-sonnet-4" -Force
        $json = $existing | ConvertTo-Json -Depth 10
        [System.IO.File]::WriteAllText($ConfigFile, $json, [System.Text.UTF8Encoding]::new($false))
        Write-Host "  GitHub Copilot configured as provider."
    } catch {
        Write-Host "  WARNING: Could not parse existing config. Creating new one." -ForegroundColor Yellow
        $json = $newConfig | ConvertTo-Json -Depth 10
        [System.IO.File]::WriteAllText($ConfigFile, $json, [System.Text.UTF8Encoding]::new($false))
    }
} else {
    $json = $newConfig | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($ConfigFile, $json, [System.Text.UTF8Encoding]::new($false))
    Write-Host "  Config created at $ConfigFile"
}

Write-Host ""

# Step 3: Create convenience alias
Write-Host "[3/4] Creating 'occ' shortcut..." -ForegroundColor Yellow
$profileDir = Split-Path $PROFILE -Parent
$profileFile = $PROFILE

if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}
if (-not (Test-Path $profileFile)) {
    New-Item -ItemType File -Path $profileFile -Force | Out-Null
}

$aliasLine = @"
function occ {
    if (-not (Get-Command opencode -ErrorAction SilentlyContinue)) {
        `$npmDir = "`$env:APPDATA\npm"
        if (Test-Path "`$npmDir\opencode.cmd") { `$env:Path += ";`$npmDir" }
    }
    opencode auth login
}
"@
$profileContent = Get-Content $profileFile -Raw -ErrorAction SilentlyContinue
if ($profileContent -and $profileContent.Contains("function occ")) {
    Write-Host "  Alias already exists in $profileFile"
} else {
    Add-Content -Path $profileFile -Value "`n# OpenCode - quick connect to GitHub Copilot"
    Add-Content -Path $profileFile -Value $aliasLine
    Write-Host "  Added 'occ' to $profileFile"
}

# Define occ in the GLOBAL scope so it works immediately after irm | iex
Set-Item -Path function:global:occ -Value {
    if (-not (Get-Command opencode -ErrorAction SilentlyContinue)) {
        $npmDir = "$env:APPDATA\npm"
        if (Test-Path "$npmDir\opencode.cmd") { $env:Path += ";$npmDir" }
    }
    opencode auth login
}
Write-Host "  'occ' is ready to use now."

Write-Host ""

# Step 4: Verify installation
Write-Host "[4/4] Verifying installation..." -ForegroundColor Yellow
$opencodeCmd = Get-Command opencode -ErrorAction SilentlyContinue
if ($opencodeCmd) {
    Write-Host "  OpenCode installed successfully." -ForegroundColor Green
} else {
    Write-Host "  WARNING: 'opencode' not found in PATH." -ForegroundColor Yellow
    Write-Host "  Restart your terminal or check your PATH."
}

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "One last step - connect to GitHub Copilot:"
Write-Host "  Run: occ  (or 'opencode auth login')"
Write-Host "  Select 'GitHub Copilot' -> authenticate in browser -> done."
Write-Host ""
Write-Host "After that, just run 'opencode' in any project. You're set."
