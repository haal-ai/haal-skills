# Multi-repo setup script
# 1. Clone seed repo
# 2. Read repos-manifest.json from seed
# 3. Clone additional repos (skip unavailable)
# 4. Install from bottom to top (seed wins on conflicts)

param(
    [string]$RepoPath = "",
    [string]$Seed = "",
    [string[]]$Competency = @(),
    [string]$Collection = "",
    [switch]$Clean,  # If set, delete existing skills first (default: update only)
    [ValidateSet("all", "kiro", "claude", "windsurf", "github")]
    [string]$Platform = "all"  # Which platform(s) to install to
)

$ErrorActionPreference = 'Stop'

# Default RepoPath to current directory if not specified
if ([string]::IsNullOrWhiteSpace($RepoPath)) {
    $RepoPath = (Get-Location).Path
}

$TempBaseFolder = Join-Path $env:TEMP "haal-skills-repos"

function Clean-Folder([string]$Path) {
    if (Test-Path -LiteralPath $Path) {
        Remove-Item -LiteralPath $Path -Recurse -Force
    }
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
}

function Try-CloneRepo([string]$RepoSpec, [string]$DestFolder) {
    # Parse repo spec: owner/repo:branch
    $repoUrl = ""
    $branch = ""
    
    if ($RepoSpec -match '^([^:]+):(.+)$') {
        $repoUrl = "https://github.com/$($Matches[1])"
        $branch = $Matches[2]
    } else {
        $repoUrl = "https://github.com/$RepoSpec"
        $branch = "main"
    }
    
    # Create unique folder name: owner_repo_branch
    $repoName = ($RepoSpec -split ':')[0] -replace '/', '_'
    $branchSafe = $branch -replace '[/\\]', '_'
    $clonePath = Join-Path $DestFolder "${repoName}_${branchSafe}"
    
    Write-Host "  Fetching $RepoSpec..." -ForegroundColor Gray -NoNewline
    
    # Remove existing clone path if it exists
    if (Test-Path -LiteralPath $clonePath) {
        Remove-Item -LiteralPath $clonePath -Recurse -Force -ErrorAction SilentlyContinue
    }
    
    # Clone silently (redirect all output to null)
    $process = Start-Process -FilePath "git" -ArgumentList "clone", "--depth", "1", "--branch", $branch, $repoUrl, $clonePath -Wait -PassThru -NoNewWindow -RedirectStandardOutput "NUL" -RedirectStandardError "NUL"
    
    if ($process.ExitCode -eq 0 -and (Test-Path -LiteralPath $clonePath)) {
        Write-Host " OK" -ForegroundColor Green
        return $clonePath
    }
    
    # Try master if main failed
    if ($branch -eq "main") {
        Write-Host " trying master..." -ForegroundColor Yellow -NoNewline
        $clonePath = Join-Path $DestFolder "${repoName}_master"
        $process = Start-Process -FilePath "git" -ArgumentList "clone", "--depth", "1", "--branch", "master", $repoUrl, $clonePath -Wait -PassThru -NoNewWindow -RedirectStandardOutput "NUL" -RedirectStandardError "NUL"
        
        if ($process.ExitCode -eq 0 -and (Test-Path -LiteralPath $clonePath)) {
            Write-Host " OK" -ForegroundColor Green
            return $clonePath
        }
    }
    
    Write-Host " SKIP (not available)" -ForegroundColor Yellow
    return $null
}

function Read-ReposManifest([string]$ClonePath) {
    $manifestPath = Join-Path $ClonePath "repos-manifest.json"
    if (!(Test-Path -LiteralPath $manifestPath)) {
        return @()
    }
    
    try {
        $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
        if ($manifest.repos) {
            return @($manifest.repos)
        }
    } catch {
        Write-Host "  WARN: Failed to parse repos-manifest.json" -ForegroundColor Yellow
    }
    return @()
}

function Install-FromClone([string]$ClonePath, [hashtable]$InstallArgs, [bool]$CleanMode, [string]$PlatformMode) {
    $installScript = Join-Path $ClonePath ".olaf\tools\install-haal-skills.ps1"
    
    if (!(Test-Path -LiteralPath $installScript)) {
        Write-Host "  SKIP: No install script in $ClonePath" -ForegroundColor Yellow
        return
    }
    
    # Build args for install script
    $args = @{ ClonePath = $ClonePath }
    if ($InstallArgs.ContainsKey('RepoPath') -and ![string]::IsNullOrWhiteSpace($InstallArgs['RepoPath'])) { 
        $args['RepoPath'] = $InstallArgs['RepoPath'] 
    }
    if ($InstallArgs.ContainsKey('Collection') -and ![string]::IsNullOrWhiteSpace($InstallArgs['Collection'])) { 
        $args['Collection'] = $InstallArgs['Collection'] 
    }
    if ($InstallArgs.ContainsKey('Competency') -and $InstallArgs['Competency'] -and $InstallArgs['Competency'].Count -gt 0) { 
        $args['Competency'] = $InstallArgs['Competency'] 
    }
    if ($CleanMode) {
        $args['Clean'] = $true
    }
    if ($PlatformMode) {
        $args['Platform'] = $PlatformMode
    }
    
    try {
        & $installScript @args
    } catch {
        Write-Host "  WARN: Install had errors for $ClonePath - continuing" -ForegroundColor Yellow
        Write-Host "  Error: $_" -ForegroundColor Yellow
    }
}

# === Main ===

Write-Host "=== HAAL Setup ===" -ForegroundColor Cyan
Write-Host "  Installing skills, powers, and tools to your environment"
Write-Host ""

# Determine seed
if ([string]::IsNullOrWhiteSpace($Seed)) {
    $Seed = "haal-ai/haal-skills:main"
}

# Clean temp folder
Clean-Folder $TempBaseFolder

# Step 1: Clone seed repo
Write-Host "Downloading skill packages..." -ForegroundColor Cyan
$seedPath = Try-CloneRepo $Seed $TempBaseFolder

if ($null -eq $seedPath) {
    throw "Failed to download: $Seed"
}

# Step 2: Read repos manifest from seed
$additionalRepos = @(Read-ReposManifest $seedPath)
$repoCount = $additionalRepos.Count

# Step 3: Clone additional repos
$clonedPaths = @()
if ($repoCount -gt 0) {
    foreach ($repo in $additionalRepos) {
        $path = Try-CloneRepo $repo $TempBaseFolder
        if ($null -ne $path) {
            $clonedPaths += $path
        }
    }
}

# Add seed path last (so it installs last and wins conflicts)
$clonedPaths += $seedPath
Write-Host ""

# Step 4: Install from bottom to top
Write-Host "Installing..." -ForegroundColor Cyan

$installArgs = @{}
$installArgs['RepoPath'] = $RepoPath
if (![string]::IsNullOrWhiteSpace($Collection)) { $installArgs['Collection'] = $Collection }
if ($Competency.Count -gt 0) { $installArgs['Competency'] = $Competency }

foreach ($clonePath in $clonedPaths) {
    $repoName = Split-Path -Leaf $clonePath
    # Only first install can clean (if --Clean), subsequent ones never clean
    $cleanThis = $Clean -and ($clonePath -eq $clonedPaths[0])
    Install-FromClone $clonePath $installArgs $cleanThis $Platform
}

# Step 5: Final registry update for all installed powers
$powersScript = Join-Path $seedPath ".olaf\tools\install-powers.ps1"
if (Test-Path -LiteralPath $powersScript) {
    try {
        & $powersScript -SourcePath $seedPath -UpdateRegistry
    } catch {
        Write-Host "  WARN: Registry update failed: $_" -ForegroundColor Yellow
    }
}
Write-Host ""

Write-Host "=== Setup Complete ===" -ForegroundColor Green
