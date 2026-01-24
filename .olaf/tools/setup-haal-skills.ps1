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


Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Default RepoPath to current directory if not specified
if ([string]::IsNullOrWhiteSpace($RepoPath)) {
    $RepoPath = (Get-Location).Path
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
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
    
    Write-Host "Cloning $RepoSpec..." -ForegroundColor Cyan
    Write-Host "  URL: $repoUrl"
    Write-Host "  Branch: $branch"
    
    # Remove existing clone path if it exists
    if (Test-Path -LiteralPath $clonePath) {
        Remove-Item -LiteralPath $clonePath -Recurse -Force -ErrorAction SilentlyContinue
    }
    
    # Use Start-Process to avoid stderr issues
    $process = Start-Process -FilePath "git" -ArgumentList "clone", "--depth", "1", "--branch", $branch, $repoUrl, $clonePath -Wait -PassThru -NoNewWindow
    
    if ($process.ExitCode -eq 0 -and (Test-Path -LiteralPath $clonePath)) {
        Write-Host "  OK: ${repoName}:${branch}" -ForegroundColor Green
        return $clonePath
    }
    
    # Try master if main failed
    if ($branch -eq "main") {
        Write-Host "  Trying master branch..." -ForegroundColor Yellow
        $clonePath = Join-Path $DestFolder "${repoName}_master"
        $process = Start-Process -FilePath "git" -ArgumentList "clone", "--depth", "1", "--branch", "master", $repoUrl, $clonePath -Wait -PassThru -NoNewWindow
        
        if ($process.ExitCode -eq 0 -and (Test-Path -LiteralPath $clonePath)) {
            Write-Host "  OK: ${repoName}:master" -ForegroundColor Green
            return $clonePath
        }
    }
    
    Write-Host "  SKIP: $RepoSpec (not available)" -ForegroundColor Yellow
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

Write-Host "=== HAAL Skills Multi-Repo Setup ===" -ForegroundColor Cyan
Write-Host ""

# Determine seed
# If not specified, always use the canonical haal-ai/haal-skills repo.
# Note: Try-CloneRepo automatically falls back to master when main is unavailable.
if ([string]::IsNullOrWhiteSpace($Seed)) {
    $Seed = "haal-ai/haal-skills:main"
}

Write-Host "Seed: $Seed"
Write-Host ""

# Clean temp folder
Clean-Folder $TempBaseFolder

# Step 1: Clone seed repo
Write-Host "Step 1: Cloning seed repo..." -ForegroundColor Cyan
$seedPath = Try-CloneRepo $Seed $TempBaseFolder

if ($null -eq $seedPath) {
    throw "Failed to clone seed repo: $Seed"
}
Write-Host ""

# Step 2: Read repos manifest from seed
Write-Host "Step 2: Reading repos manifest..." -ForegroundColor Cyan
$additionalRepos = @(Read-ReposManifest $seedPath)
$repoCount = $additionalRepos.Count
Write-Host "  Found $repoCount additional repo(s)"
Write-Host ""

# Step 3: Clone additional repos
$clonedPaths = @()
if ($repoCount -gt 0) {
    Write-Host "Step 3: Cloning additional repos..." -ForegroundColor Cyan
    foreach ($repo in $additionalRepos) {
        $path = Try-CloneRepo $repo $TempBaseFolder
        if ($null -ne $path) {
            $clonedPaths += $path
        }
    }
    Write-Host ""
}

# Add seed path last (so it installs last and wins conflicts)
$clonedPaths += $seedPath

# Step 4: Install from bottom to top
Write-Host "Step 4: Installing skills (bottom to top)..." -ForegroundColor Cyan
Write-Host "  Order: $($clonedPaths -join ' -> ')"
Write-Host ""

$installArgs = @{}
$installArgs['RepoPath'] = $RepoPath
if (![string]::IsNullOrWhiteSpace($Collection)) { $installArgs['Collection'] = $Collection }
if ($Competency.Count -gt 0) { $installArgs['Competency'] = $Competency }

foreach ($clonePath in $clonedPaths) {
    $repoName = Split-Path -Leaf $clonePath
    Write-Host "Installing from: $repoName" -ForegroundColor Cyan
    # Only first install can clean (if --Clean), subsequent ones never clean
    $cleanThis = $Clean -and ($clonePath -eq $clonedPaths[0])
    Install-FromClone $clonePath $installArgs $cleanThis $Platform
    Write-Host ""
}

# Step 5: Final registry update for all installed powers
Write-Host "Step 5: Updating Kiro Powers registry..." -ForegroundColor Cyan
$powersScript = Join-Path $seedPath ".olaf\tools\install-powers.ps1"
if (Test-Path -LiteralPath $powersScript) {
    try {
        & $powersScript -SourcePath $seedPath -UpdateRegistry
    } catch {
        Write-Host "  WARN: Registry update failed: $_" -ForegroundColor Yellow
    }
} else {
    Write-Host "  No powers script found" -ForegroundColor Gray
}
Write-Host ""

Write-Host "=== Done ===" -ForegroundColor Green
