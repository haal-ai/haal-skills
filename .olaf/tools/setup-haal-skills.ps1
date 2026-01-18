
param(
    [string]$RepoPath = "",
    [string]$SkillsRepoUrl = "https://github.com/haal-ai/haal-skills",
    [string]$SkillsBranch = "main",
    [int]$CloneDepth = 1
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Require-Command([string]$Name) {
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($null -eq $cmd) {
        throw "Required command '$Name' was not found on PATH. Please install it and restart your terminal."
    }
    return $cmd
}

 function Normalize-GitRemoteUrl([string]$Url) {
     if ([string]::IsNullOrWhiteSpace($Url)) { return "" }
     $u = $Url.Trim()
     while ($u.EndsWith('/')) { $u = $u.Substring(0, $u.Length - 1) }
     return $u
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
    } catch {
        # ignore
    }

    return (Get-Location).Path
}

$null = Require-Command 'git'
$null = Require-Command 'python'

$repoRoot = Resolve-RepoRoot $RepoPath
$windsurfSkillsPath = Join-Path $env:USERPROFILE ".codeium\windsurf\skills"
$syncScript = Join-Path $windsurfSkillsPath ".olaf\tools\sync_olaf_files.py"

Write-Output "=== HAAL Skills Setup ==="
Write-Output "Repo:   $repoRoot"
Write-Output "Skills: $windsurfSkillsPath"
Write-Output "Depth:  $CloneDepth"

if (!(Test-Path -LiteralPath (Join-Path $repoRoot '.git'))) {
    throw "Target path is not a git repository: $repoRoot"
}

# Step 1: Ensure skills directory parent exists
$skillsParent = Split-Path -Parent $windsurfSkillsPath
if (!(Test-Path -LiteralPath $skillsParent)) {
    New-Item -ItemType Directory -Path $skillsParent -Force | Out-Null
}

# Step 2: Clone/update haal-skills repo into windsurf skills directory
if (Test-Path -LiteralPath (Join-Path $windsurfSkillsPath '.git')) {
    Push-Location $windsurfSkillsPath
    try {
        $remote = (& git remote get-url origin 2>$null)
        if ($LASTEXITCODE -ne 0) { $remote = "" }
        $remoteNorm = Normalize-GitRemoteUrl $remote
        $expectedNorm = Normalize-GitRemoteUrl $SkillsRepoUrl
        if ($remoteNorm -ne $expectedNorm) {
            throw "Existing skills folder has unexpected git remote: '$remote' (expected '$SkillsRepoUrl')."
        }

        Write-Output "Updating existing haal-skills checkout..."
        if ($CloneDepth -gt 0) {
            & git fetch --depth $CloneDepth origin $SkillsBranch
        } else {
            & git fetch origin
        }
        & git checkout $SkillsBranch | Out-Null
        & git reset --hard "origin/$SkillsBranch" | Out-Null
    }
    finally {
        Pop-Location
    }
} else {
    if (!(Test-Path -LiteralPath $windsurfSkillsPath)) {
        Write-Output "Creating skills folder: $windsurfSkillsPath"
        New-Item -ItemType Directory -Path $windsurfSkillsPath -Force | Out-Null
    } else {
        # Folder exists but is not a git repo
        $itemCount = (Get-ChildItem -LiteralPath $windsurfSkillsPath -Force -ErrorAction SilentlyContinue | Measure-Object).Count
        if ($itemCount -gt 0) {
            throw "Cannot install into '$windsurfSkillsPath' because it exists, is not a git repo, and is not empty (contains $itemCount items)."
        }
    }

    Write-Output "Cloning haal-skills into $windsurfSkillsPath ..."
    if ($CloneDepth -gt 0) {
        & git clone --depth $CloneDepth --branch $SkillsBranch --single-branch $SkillsRepoUrl $windsurfSkillsPath
    } else {
        & git clone --branch $SkillsBranch $SkillsRepoUrl $windsurfSkillsPath
    }
}

# Step 3: Run OLAF sync script (copies into current repo)
if (!(Test-Path -LiteralPath $syncScript)) {
    throw "Sync script not found: $syncScript"
}

Write-Output "Running OLAF sync script..."
Push-Location $repoRoot
try {
    & python $syncScript
}
finally {
    Pop-Location
}

# Step 4: Basic verification
$envValidationFile = Join-Path $repoRoot ".windsurf\workflows\environment-validation.md"
$olafDataDir = Join-Path $repoRoot ".olaf\data"

Write-Output "Verification:"
Write-Output ("- environment-validation.md: " + (Test-Path -LiteralPath $envValidationFile))
Write-Output ("- .olaf/data exists: " + (Test-Path -LiteralPath $olafDataDir))

if (Test-Path -LiteralPath $olafDataDir) {
    $fileCount = (Get-ChildItem -Path $olafDataDir -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
    Write-Output "- .olaf/data file count: $fileCount"
}

Write-Output "=== Done ==="
