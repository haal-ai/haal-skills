# Haal AI Powers Installation Script for Kiro
# Copies powers to ~/.kiro/powers/installed/ without modifying registry

param(
    [string]$SourcePath = ".",
    [string[]]$Competency = @(),
    [string]$Collection = "",
    [switch]$Force
)

$ErrorActionPreference = 'Continue'

$SourcePath = (Resolve-Path $SourcePath).Path
$PowersSourceDir = Join-Path $SourcePath "powers"
$CompetenciesDir = Join-Path $SourcePath "competencies"
$CollectionManifest = Join-Path $SourcePath "collection-manifest.json"
$KiroInstalledDir = Join-Path $env:USERPROFILE ".kiro\powers\installed"

function Read-JsonFile([string]$Path) {
    if (!(Test-Path $Path)) { return $null }
    try { return Get-Content $Path -Raw | ConvertFrom-Json }
    catch { return $null }
}

function Get-PowersFromCompetencies([string[]]$Names) {
    $powers = @()
    foreach ($comp in $Names) {
        $manifest = Read-JsonFile (Join-Path $CompetenciesDir "$comp.json")
        if ($manifest -and $manifest.powers) {
            $powers += $manifest.powers
            Write-Host "  Competency '$comp': $($manifest.powers.Count) powers" -ForegroundColor Cyan
        }
    }
    return $powers | Select-Object -Unique
}

function Get-AllPowers {
    Get-ChildItem $PowersSourceDir -Directory | 
        Where-Object { Test-Path (Join-Path $_.FullName "POWER.md") } |
        ForEach-Object { $_.Name }
}

Write-Host "=== Haal AI Powers Installation ===" -ForegroundColor Cyan
Write-Host ""

if (!(Test-Path $PowersSourceDir)) {
    Write-Host "ERROR: Powers source not found: $PowersSourceDir" -ForegroundColor Red
    exit 1
}

# Resolve powers
Write-Host "Step 1: Resolving powers..." -ForegroundColor Cyan
$allCompetencies = @()
if ($Collection) {
    $manifest = Read-JsonFile $CollectionManifest
    if ($manifest -and $manifest.$Collection) {
        $allCompetencies += $manifest.$Collection
        Write-Host "  Collection '$Collection': $($manifest.$Collection.Count) competencies" -ForegroundColor Cyan
    }
}
$allCompetencies += $Competency
$allCompetencies = @($allCompetencies | Select-Object -Unique)

$powersToInstall = @()
if ($allCompetencies.Count -gt 0) {
    $powersToInstall = @(Get-PowersFromCompetencies $allCompetencies)
} else {
    Write-Host "  No collection/competency specified, installing all powers" -ForegroundColor Cyan
    $powersToInstall = @(Get-AllPowers)
}
$powersToInstall = @($powersToInstall | Select-Object -Unique)

Write-Host "  Powers: $($powersToInstall -join ', ')" -ForegroundColor Gray
Write-Host ""

if ($powersToInstall.Count -eq 0) {
    Write-Host "WARN: No powers found" -ForegroundColor Yellow
    exit 0
}

# Copy powers
Write-Host "Step 2: Copying powers..." -ForegroundColor Cyan
if (!(Test-Path $KiroInstalledDir)) { New-Item -ItemType Directory -Path $KiroInstalledDir -Force | Out-Null }

$copied = 0
foreach ($power in $powersToInstall) {
    $src = Join-Path $PowersSourceDir $power
    $dst = Join-Path $KiroInstalledDir $power
    
    if (!(Test-Path (Join-Path $src "POWER.md"))) {
        Write-Host "  SKIP: $power (no POWER.md)" -ForegroundColor Yellow
        continue
    }
    
    if ((Test-Path $dst) -and !$Force) {
        Write-Host "  EXISTS: $power (use -Force)" -ForegroundColor Gray
    } else {
        if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
        Copy-Item $src $dst -Recurse
        Write-Host "  OK: $power" -ForegroundColor Green
        $copied++
    }
}

Write-Host ""
Write-Host "=== Done ===" -ForegroundColor Green
Write-Host "Copied $copied powers to: $KiroInstalledDir"
Write-Host ""
Write-Host "To activate in Kiro:" -ForegroundColor Yellow
Write-Host "  1. Powers panel > Add Local Repository"
Write-Host "  2. Select: $PowersSourceDir"
