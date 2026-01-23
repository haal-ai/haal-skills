param(
    [Parameter(Mandatory=$true)]
    [string]$ClonePath,
    [string]$RepoPath = "",
    [string[]]$Competency = @(),
    [string]$Collection = ""
)

Set-StrictMode -Version Latest
# Continue on errors - don't block on missing items
$ErrorActionPreference = 'Continue'

# Fixed temp folder for staging
$TempStagingFolder = Join-Path $env:TEMP "haal-skills-staging"

# Destination folders
$Destinations = @(
    (Join-Path $env:USERPROFILE ".codeium\windsurf\skills"),
    (Join-Path $env:USERPROFILE ".claude\skills"),
    (Join-Path $env:USERPROFILE ".github\skills"),
    (Join-Path $env:USERPROFILE ".kiro\skills")
)

function Test-Command([string]$Name) {
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    return $null -ne $cmd
}

function Resolve-RepoRoot([string]$Path) {
    if (![string]::IsNullOrWhiteSpace($Path)) {
        try {
            return (Resolve-Path -LiteralPath $Path -ErrorAction Stop).Path
        } catch {
            return $Path
        }
    }
    try {
        $root = (& git rev-parse --show-toplevel 2>$null)
        if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace($root)) {
            return $root.Trim()
        }
    } catch { }
    return (Get-Location).Path
}

function Clean-Folder([string]$Path) {
    if (Test-Path -LiteralPath $Path) {
        Remove-Item -LiteralPath $Path -Recurse -Force -ErrorAction SilentlyContinue
    }
    New-Item -ItemType Directory -Path $Path -Force -ErrorAction SilentlyContinue | Out-Null
}

function Read-JsonFile([string]$Path) {
    if (!(Test-Path -LiteralPath $Path)) {
        return $null
    }
    try {
        return Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json
    } catch {
        Write-Host "  WARN: Failed to parse $Path" -ForegroundColor Yellow
        return $null
    }
}

function Get-SkillsFromCompetencies([string[]]$CompetencyNames, [string]$ClonePath) {
    $competenciesPath = Join-Path $ClonePath "competencies"
    
    $skills = @()
    foreach ($comp in $CompetencyNames) {
        $manifestPath = Join-Path $competenciesPath "$comp.json"
        $manifest = Read-JsonFile $manifestPath
        if ($null -eq $manifest) {
            Write-Host "  SKIP: Competency '$comp' not found" -ForegroundColor Yellow
            continue
        }
        
        if ($manifest.skills) {
            $skills += $manifest.skills
            Write-Host "  OK: Competency '$comp' ($($manifest.skills.Count) skills)" -ForegroundColor Green
        }
    }
    return $skills | Select-Object -Unique
}

function Get-CompetenciesFromCollection([string]$CollectionName, [string]$ClonePath) {
    $manifestPath = Join-Path $ClonePath "collection-manifest.json"
    $manifest = Read-JsonFile $manifestPath
    if ($null -eq $manifest) {
        Write-Host "  SKIP: collection-manifest.json not found" -ForegroundColor Yellow
        return @()
    }
    
    if ($manifest.PSObject.Properties.Name -contains $CollectionName) {
        $competencies = $manifest.$CollectionName
        Write-Host "  OK: Collection '$CollectionName' ($($competencies.Count) competencies)" -ForegroundColor Green
        return $competencies
    } else {
        Write-Host "  SKIP: Collection '$CollectionName' not found" -ForegroundColor Yellow
        return @()
    }
}

function Get-PruneList([string]$ClonePath) {
    $prunePath = Join-Path $ClonePath ".olaf\prune-skills.txt"
    if (!(Test-Path -LiteralPath $prunePath)) {
        return @()
    }
    
    $lines = Get-Content -LiteralPath $prunePath -ErrorAction SilentlyContinue
    $skills = @()
    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        if ($trimmed -and !$trimmed.StartsWith('#')) {
            $skills += $trimmed
        }
    }
    return $skills
}

function Get-SkillsPath([string]$ClonePath) {
    # Check for skills/ subfolder first, then root
    $skillsSubfolder = Join-Path $ClonePath "skills"
    if (Test-Path -LiteralPath $skillsSubfolder) {
        return $skillsSubfolder
    }
    return $ClonePath
}

function Get-AllSkills([string]$ClonePath) {
    $skillsPath = Get-SkillsPath $ClonePath
    if (!(Test-Path -LiteralPath $skillsPath)) {
        Write-Host "  WARN: Skills folder not found" -ForegroundColor Yellow
        return @()
    }
    
    $folders = Get-ChildItem -LiteralPath $skillsPath -Directory -ErrorAction SilentlyContinue | 
        Where-Object { Test-Path (Join-Path $_.FullName "skill.md") }
    return $folders | ForEach-Object { $_.Name }
}

function Prune-Skills([string[]]$SkillNames, [string[]]$Destinations) {
    foreach ($dest in $Destinations) {
        foreach ($skill in $SkillNames) {
            $skillPath = Join-Path $dest $skill
            if (Test-Path -LiteralPath $skillPath) {
                Remove-Item -LiteralPath $skillPath -Recurse -Force -ErrorAction SilentlyContinue
                Write-Host "  Pruned: $skill" -ForegroundColor Gray
            }
        }
    }
}

function Copy-SkillsToStaging([string[]]$SkillNames, [string]$ClonePath, [string]$StagingPath) {
    $skillsSource = Get-SkillsPath $ClonePath
    $copied = 0
    
    foreach ($skill in $SkillNames) {
        $sourcePath = Join-Path $skillsSource $skill
        $destPath = Join-Path $StagingPath $skill
        
        if (Test-Path -LiteralPath $sourcePath) {
            if (Test-Path -LiteralPath $destPath) {
                Remove-Item -LiteralPath $destPath -Recurse -Force -ErrorAction SilentlyContinue
            }
            Copy-Item -LiteralPath $sourcePath -Destination $destPath -Recurse -ErrorAction SilentlyContinue
            $copied++
        } else {
            Write-Host "  SKIP: Skill '$skill' not found" -ForegroundColor Yellow
        }
    }
    Write-Host "  Staged $copied skills" -ForegroundColor Green
}

function Deploy-StagingToDestinations([string]$StagingPath, [string[]]$Destinations) {
    $stagedSkills = Get-ChildItem -LiteralPath $StagingPath -Directory -ErrorAction SilentlyContinue
    
    if ($null -eq $stagedSkills -or $stagedSkills.Count -eq 0) {
        Write-Host "  WARN: No skills to deploy" -ForegroundColor Yellow
        return
    }
    
    foreach ($dest in $Destinations) {
        # Ensure destination exists
        if (!(Test-Path -LiteralPath $dest)) {
            New-Item -ItemType Directory -Path $dest -Force -ErrorAction SilentlyContinue | Out-Null
        }
        
        foreach ($skill in $stagedSkills) {
            $destSkillPath = Join-Path $dest $skill.Name
            
            # Delete existing skill folder first
            if (Test-Path -LiteralPath $destSkillPath) {
                Remove-Item -LiteralPath $destSkillPath -Recurse -Force -ErrorAction SilentlyContinue
            }
            
            # Copy new version
            Copy-Item -LiteralPath $skill.FullName -Destination $destSkillPath -Recurse -ErrorAction SilentlyContinue
        }
        
        Write-Host "  Deployed $($stagedSkills.Count) skills to: $dest" -ForegroundColor Green
    }
}

# === Main execution ===

Write-Host "=== HAAL Skills Install ===" -ForegroundColor Cyan

# Validate clone path
if (!(Test-Path -LiteralPath $ClonePath)) {
    Write-Host "ERROR: Clone path does not exist: $ClonePath" -ForegroundColor Red
    exit 1
}

$repoRoot = Resolve-RepoRoot $RepoPath

Write-Host "Clone path: $ClonePath"
Write-Host "Repo: $repoRoot"
Write-Host "Collection: $(if ($Collection) { $Collection } else { '(none)' })"
Write-Host "Competencies: $(if ($Competency.Count -gt 0) { $Competency -join ', ' } else { '(none)' })"
Write-Host ""

# Step 1: Read prune list and prune skills from destinations
Write-Host "Step 1: Pruning deprecated skills..." -ForegroundColor Cyan
$pruneList = Get-PruneList $ClonePath
if ($pruneList.Count -gt 0) {
    Prune-Skills $pruneList $Destinations
} else {
    Write-Host "  No skills to prune"
}
Write-Host ""

# Step 2: Resolve skills to install
Write-Host "Step 2: Resolving skills..." -ForegroundColor Cyan
$allCompetencies = @()

# From collection
if ($Collection) {
    $collectionCompetencies = Get-CompetenciesFromCollection $Collection $ClonePath
    $allCompetencies += $collectionCompetencies
}

# From explicit competencies
if ($Competency.Count -gt 0) {
    $allCompetencies += $Competency
}

$allCompetencies = $allCompetencies | Select-Object -Unique

# Get skills from competencies
$skillsToInstall = @()
if ($allCompetencies.Count -gt 0) {
    $skillsToInstall = Get-SkillsFromCompetencies $allCompetencies $ClonePath
} else {
    # No selection = all skills
    Write-Host "  No collection/competency specified, installing all skills"
    $skillsToInstall = Get-AllSkills $ClonePath
}

Write-Host "  Skills to install: $($skillsToInstall.Count)"
Write-Host ""

if ($skillsToInstall.Count -eq 0) {
    Write-Host "WARN: No skills found to install" -ForegroundColor Yellow
    exit 0
}

# Step 3: Clean staging and copy selected skills
Write-Host "Step 3: Staging skills..." -ForegroundColor Cyan
Clean-Folder $TempStagingFolder
Copy-SkillsToStaging $skillsToInstall $ClonePath $TempStagingFolder
Write-Host ""

# Step 4: Deploy to all destinations
Write-Host "Step 4: Deploying to destinations..." -ForegroundColor Cyan
Deploy-StagingToDestinations $TempStagingFolder $Destinations
Write-Host ""

# Step 5: Run sync script for .olaf files (optional)
Write-Host "Step 5: Syncing .olaf files..." -ForegroundColor Cyan
$syncScript = Join-Path $ClonePath ".olaf\tools\sync-olaf-files.ps1"
if (Test-Path -LiteralPath $syncScript) {
    try {
        & $syncScript -SourcePath $ClonePath -DestPath $repoRoot
        Write-Host "  OK: .olaf files synced" -ForegroundColor Green
    } catch {
        Write-Host "  WARN: Sync script failed" -ForegroundColor Yellow
    }
} else {
    Write-Host "  SKIP: Sync script not found" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "=== Done ===" -ForegroundColor Green
