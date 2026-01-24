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
        if ($manifest) {
            # Check if powers property exists using PSObject.Properties
            $hasPowers = $manifest.PSObject.Properties.Name -contains 'powers'
            if ($hasPowers -and $manifest.powers) {
                $powers += $manifest.powers
            }
        }
    }
    return $powers | Select-Object -Unique
}

function Get-AllPowers {
    Get-ChildItem $PowersSourceDir -Directory | 
        Where-Object { Test-Path (Join-Path $_.FullName "POWER.md") } |
        ForEach-Object { $_.Name }
}

if (!(Test-Path $PowersSourceDir)) {
    Write-Host "    ERROR: Powers source not found: $PowersSourceDir" -ForegroundColor Red
    exit 1
}

# Resolve powers
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
    $powersToInstall = @(Get-AllPowers)
}
$powersToInstall = @($powersToInstall | Select-Object -Unique)

if ($powersToInstall.Count -eq 0) {
    Write-Host "    No powers to install" -ForegroundColor Gray
    exit 0
}

# Copy powers
if (!(Test-Path $KiroInstalledDir)) { New-Item -ItemType Directory -Path $KiroInstalledDir -Force | Out-Null }

$copied = 0
$skipped = 0
foreach ($power in $powersToInstall) {
    $src = Join-Path $PowersSourceDir $power
    $dst = Join-Path $KiroInstalledDir $power
    
    if (!(Test-Path (Join-Path $src "POWER.md"))) {
        continue
    }
    
    if ((Test-Path $dst) -and !$Force) {
        $skipped++
    } else {
        if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
        Copy-Item $src $dst -Recurse
        $copied++
    }
}

Write-Host "    Powers: $copied copied, $skipped existing" -ForegroundColor Green
