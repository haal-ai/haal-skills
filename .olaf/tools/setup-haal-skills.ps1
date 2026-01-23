# Wrapper script for backward compatibility
# Calls clone-haal-skills.ps1 and install-haal-skills.ps1 in sequence

param(
    [string]$RepoPath = "",
    [string]$Seed = "",
    [string]$SkillsRepoUrl = "",
    [string]$SkillsBranch = "",
    [string[]]$Competency = @(),
    [string]$Collection = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Build seed from legacy parameters if not provided
if ([string]::IsNullOrWhiteSpace($Seed) -and ![string]::IsNullOrWhiteSpace($SkillsRepoUrl)) {
    # Extract owner/repo from URL
    $repoPart = $SkillsRepoUrl -replace '^https?://github\.com/', '' -replace '\.git$', ''
    if (![string]::IsNullOrWhiteSpace($SkillsBranch)) {
        $Seed = "$repoPart`:$SkillsBranch"
    } else {
        $Seed = $repoPart
    }
}

# Build clone arguments
$cloneArgs = @{}
if (![string]::IsNullOrWhiteSpace($Seed)) {
    $cloneArgs['Seed'] = $Seed
}

# Build install arguments
$installArgs = @{}
if (![string]::IsNullOrWhiteSpace($RepoPath)) {
    $installArgs['RepoPath'] = $RepoPath
}
if (![string]::IsNullOrWhiteSpace($Collection)) {
    $installArgs['Collection'] = $Collection
}
if ($Competency.Count -gt 0) {
    $installArgs['Competency'] = $Competency
}

# Step 1: Clone
Write-Output "=== Running clone-haal-skills.ps1 ==="
$cloneScript = Join-Path $ScriptDir "clone-haal-skills.ps1"
$clonePath = & $cloneScript @cloneArgs | Select-Object -Last 1

# Step 2: Install
Write-Output ""
Write-Output "=== Running install-haal-skills.ps1 ==="
$installScript = Join-Path $ScriptDir "install-haal-skills.ps1"
& $installScript -ClonePath $clonePath @installArgs
