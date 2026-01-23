we have # Multi-repo setup script
# 1. Clone seed repo
# 2. Read repos-manifest.json from seed
# 3. Clone additional repos (skip unavailable)
# 4. Install from bottom to top (seed wins on conflicts)

param(
    [string]$RepoPath = "",
    [string]$Seed = "",
    [string[]]$Competency = @(),
    [string]$Collection = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

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
    
    $repoName = ($RepoSpec -split ':')[0] -replace '/', '_'
    $clonePath = Join-Path $DestFolder $repoName
    
    Write-Host "Cloning $RepoSpec..." -ForegroundColor Cyan
    
    try {
        & git clone --depth 1 --branch $branch $repoUrl $clonePath 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  OK: $repoName" -ForegroundColor Green
            return $clonePath
        }
    } catch { }
    
    # Try master if main failed
    if ($branch -eq "main") {
        try {
            & git clone --depth 1 --branch "master" $repoUrl $clonePath 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  OK: $repoName (master)" -ForegroundColor Green
                return $clonePath
            }
        } catch { }
    }
    
    Write-Host "  SKIP: $RepoSpec (not available)" -ForegroundColor Yellow
    return $null
}

function Read-ReposManifest([string]$ClonePath) {
    $manifestPath = Join-Path $ClonePath "repos-manifest.json"
    if (!(Test-Path -LiteralPath $manifestPath)) {
        return @()
    }
    
    $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    if ($manifest.repos) {
        return $manifest.repos
    }
    return @()
}

function Install-FromClone([string]$ClonePath, [hashtable]$InstallArgs) {
    $installScript = Join-Path $ClonePath ".olaf\tools\install-haal-skills.ps1"
    
    if (!(Test-Path -LiteralPath $installScript)) {
        Write-Host "  SKIP: No install script in $ClonePath" -ForegroundColor Yellow
        return
    }
    
    # Run install from the cloned repo's script
    $args = @{ ClonePath = $ClonePath }
    if ($InstallArgs.RepoPath) { $args['RepoPath'] = $InstallArgs.RepoPath }
    if ($InstallArgs.Collection) { $args['Collection'] = $InstallArgs.Collection }
    if ($InstallArgs.Competency -and $InstallArgs.Competency.Count -gt 0) { 
        $args['Competency'] = $InstallArgs.Competency 
    }
    
    try {
        & $installScript @args
    } catch {
        Write-Host "  WARN: Install had errors for $ClonePath - continuing" -ForegroundColor Yellow
    }
}

# === Main ===

Write-Host "=== HAAL Skills Multi-Repo Setup ===" -ForegroundColor Cyan
Write-Host ""

# Determine seed
if ([string]::IsNullOrWhiteSpace($Seed)) {
    # Try to get from current repo's origin
    try {
        $originUrl = & git remote get-url origin 2>$null
        if ($LASTEXITCODE -eq 0 -and $originUrl) {
            $Seed = $originUrl -replace '^https://github\.com/', '' -replace '\.git$', ''
            $Seed = "$Seed`:main"
        }
    } catch { }
}

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
$additionalRepos = Read-ReposManifest $seedPath
Write-Host "  Found $($additionalRepos.Count) additional repo(s)"
Write-Host ""

# Step 3: Clone additional repos
$clonedPaths = @()
if ($additionalRepos.Count -gt 0) {
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
if (![string]::IsNullOrWhiteSpace($RepoPath)) { $installArgs['RepoPath'] = $RepoPath }
if (![string]::IsNullOrWhiteSpace($Collection)) { $installArgs['Collection'] = $Collection }
if ($Competency.Count -gt 0) { $installArgs['Competency'] = $Competency }

foreach ($clonePath in $clonedPaths) {
    $repoName = Split-Path -Leaf $clonePath
    Write-Host "Installing from: $repoName" -ForegroundColor Cyan
    Install-FromClone $clonePath $installArgs
    Write-Host ""
}

Write-Host "=== Done ===" -ForegroundColor Green
