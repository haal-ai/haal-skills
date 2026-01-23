param(
    [Parameter(Mandatory=$true)]
    [string]$ClonePath,
    [string]$RepoPath = "",
    [string[]]$Competency = @(),
    [string]$Collection = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Fixed temp folder for staging
$TempStagingFolder = Join-Path $env:TEMP "haal-skills-staging"

# Destination folders
$Destinations = @(
    (Join-Path $env:USERPROFILE ".codeium\windsurf\skills"),
    (Join-Path $env:USERPROFILE ".claude\skills"),
    (Join-Path $env:USERPROFILE ".github\skills"),
    (Join-Path $env:USERPROFILE ".kiro\skills")
)

function Require-Command([string]$Name) {
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($null -eq $cmd) {
        throw "Required command '$Name' was not found on PATH."
    }
    return $cmd
}

function Resolve-RepoRoot([string]$Path) {
    if (![string]::IsNullOrWhiteSpace($Path)) {
        return (Resolve-Path -LiteralPath $Path).Path
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
        Remove-Item -LiteralPath $Path -Recurse -Force
        Write-Output "Cleaned: $Path"
    }
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
}

function Read-JsonFile([string]$Path) {
    if (!(Test-Path -LiteralPath $Path)) {
        return $null
    }
    return Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json
}

function Get-SkillsFromCompetencies([string[]]$CompetencyNames, [string]$ClonePath) {
    $competenciesPath = Join-Path $ClonePath "competencies"
    
    $skills = @()
    foreach ($comp in $CompetencyNames) {
        $manifestPath = Join-Path $competenciesPath "$comp.json"
        $manifest = Read-JsonFile $manifestPath
        if ($null -eq $manifest) {
            Write-Output "Warning: Competency '$comp' manifest not found, skipping"
            continue
        }
        
        if ($manifest.skills) {
            $skills += $manifest.skills
            Write-Output "Competency '$comp': $($manifest.skills.Count) skills"
        }
    }
    return $skills | Select-Object -Unique
}

function Get-CompetenciesFromCollection([string]$CollectionName, [string]$ClonePath) {
    $manifestPath = Join-Path $ClonePath "collection-manifest.json"
    $manifest = Read-JsonFile $manifestPath
    if ($null -eq $manifest) {
        Write-Output "Warning: collection-manifest.json not found, skipping collection resolution"
        return @()
    }
    
    if ($manifest.PSObject.Properties.Name -contains $CollectionName) {
        $competencies = $manifest.$CollectionName
        Write-Output "Collection '$CollectionName': $($competencies.Count) competencies"
        return $competencies
    } else {
        Write-Output "Warning: Collection '$CollectionName' not found in manifest"
        return @()
    }
}

function Get-PruneList([string]$ClonePath) {
    $prunePath = Join-Path $ClonePath ".olaf\prune-skills.txt"
    if (!(Test-Path -LiteralPath $prunePath)) {
        return @()
    }
    
    $lines = Get-Content -LiteralPath $prunePath
    $skills = @()
    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        if ($trimmed -and !$trimmed.StartsWith('#')) {
            $skills += $trimmed
        }
    }
    return $skills
}

function Get-AllSkills([string]$ClonePath) {
    $skillsPath = Join-Path $ClonePath "skills"
    if (!(Test-Path -LiteralPath $skillsPath)) {
        Write-Output "Warning: skills folder not found"
        return @()
    }
    
    $folders = Get-ChildItem -LiteralPath $skillsPath -Directory
    return $folders | ForEach-Object { $_.Name }
}

function Prune-Skills([string[]]$SkillNames, [string[]]$Destinations) {
    foreach ($dest in $Destinations) {
        foreach ($skill in $SkillNames) {
            $skillPath = Join-Path $dest $skill
            if (Test-Path -LiteralPath $skillPath) {
                Remove-Item -LiteralPath $skillPath -Recurse -Force
                Write-Output "Pruned: $skillPath"
            }
        }
    }
}

function Copy-SkillsToStaging([string[]]$SkillNames, [string]$ClonePath, [string]$StagingPath) {
    $skillsSource = Join-Path $ClonePath "skills"
    
    foreach ($skill in $SkillNames) {
        $sourcePath = Join-Path $skillsSource $skill
        $destPath = Join-Path $StagingPath $skill
        
        if (Test-Path -LiteralPath $sourcePath) {
            if (Test-Path -LiteralPath $destPath) {
                Remove-Item -LiteralPath $destPath -Recurse -Force
            }
            Copy-Item -LiteralPath $sourcePath -Destination $destPath -Recurse
            Write-Output "Staged: $skill"
        } else {
            Write-Output "Warning: Skill '$skill' not found in source"
        }
    }
}

function Deploy-StagingToDestinations([string]$StagingPath, [string[]]$Destinations) {
    $stagedSkills = Get-ChildItem -LiteralPath $StagingPath -Directory -ErrorAction SilentlyContinue
    
    foreach ($dest in $Destinations) {
        # Ensure destination exists
        if (!(Test-Path -LiteralPath $dest)) {
            New-Item -ItemType Directory -Path $dest -Force | Out-Null
        }
        
        foreach ($skill in $stagedSkills) {
            $destSkillPath = Join-Path $dest $skill.Name
            
            # Delete existing skill folder first
            if (Test-Path -LiteralPath $destSkillPath) {
                Remove-Item -LiteralPath $destSkillPath -Recurse -Force
            }
            
            # Copy new version
            Copy-Item -LiteralPath $skill.FullName -Destination $destSkillPath -Recurse
        }
        
        Write-Output "Deployed $($stagedSkills.Count) skills to: $dest"
    }
}

# Main execution
$null = Require-Command 'python'

# Validate clone path
if (!(Test-Path -LiteralPath $ClonePath)) {
    throw "Clone path does not exist: $ClonePath"
}

$repoRoot = Resolve-RepoRoot $RepoPath

Write-Output "=== HAAL Skills Install ==="
Write-Output "Clone path: $ClonePath"
Write-Output "Repo: $repoRoot"
Write-Output "Collection: $(if ($Collection) { $Collection } else { '(none)' })"
Write-Output "Competencies: $(if ($Competency.Count -gt 0) { $Competency -join ', ' } else { '(none)' })"
Write-Output ""

# Step 1: Read prune list and prune skills from destinations
Write-Output "Step 1: Pruning deprecated skills..."
$pruneList = Get-PruneList $ClonePath
if ($pruneList.Count -gt 0) {
    Write-Output "Skills to prune: $($pruneList -join ', ')"
    Prune-Skills $pruneList $Destinations
} else {
    Write-Output "No skills to prune"
}
Write-Output ""

# Step 2: Resolve skills to install
Write-Output "Step 2: Resolving skills..."
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
    Write-Output "No collection/competency specified, installing all skills"
    $skillsToInstall = Get-AllSkills $ClonePath
}

Write-Output "Skills to install: $($skillsToInstall.Count)"
Write-Output ""

# Step 3: Clean staging and copy selected skills
Write-Output "Step 3: Staging skills..."
Clean-Folder $TempStagingFolder
Copy-SkillsToStaging $skillsToInstall $ClonePath $TempStagingFolder
Write-Output ""

# Step 4: Deploy to all destinations
Write-Output "Step 4: Deploying to destinations..."
Deploy-StagingToDestinations $TempStagingFolder $Destinations
Write-Output ""

# Step 5: Run sync script for .olaf files
Write-Output "Step 5: Syncing .olaf files..."
$syncScript = Join-Path $ClonePath ".olaf\tools\sync_olaf_files.py"
if (Test-Path -LiteralPath $syncScript) {
    Push-Location $repoRoot
    try {
        $env:HAAL_SKILLS_SOURCE = $ClonePath
        & python $syncScript
    }
    finally {
        Remove-Item Env:\HAAL_SKILLS_SOURCE -ErrorAction SilentlyContinue
        Pop-Location
    }
} else {
    Write-Output "Warning: sync script not found"
}
Write-Output ""

Write-Output "=== Done ==="
