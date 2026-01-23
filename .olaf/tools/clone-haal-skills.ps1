param(
    [string]$Seed = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Fixed temp folder for clone
$TempCloneFolder = Join-Path $env:TEMP "haal-skills-clone"

function Show-Help {
    Write-Output "Usage: clone-haal-skills.ps1 [options]"
    Write-Output ""
    Write-Output "Clone the HAAL skills repository to a temp folder."
    Write-Output ""
    Write-Output "Options:"
    Write-Output "  -Seed OWNER/REPO:BRANCH   Override source repo (e.g., 'haal-ai/haal-skills:main')"
    Write-Output "                            Branch is optional; if omitted, tries 'main' then 'master'"
    Write-Output ""
    Write-Output "Output:"
    Write-Output "  Prints the path to the cloned folder on success"
    Write-Output ""
    Write-Output "Default behavior:"
    Write-Output "  - Clones from the origin remote of the local repo"
    Write-Output "  - Uses 'main' branch by default"
}

function Require-Command([string]$Name) {
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($null -eq $cmd) {
        throw "Required command '$Name' was not found on PATH."
    }
    return $cmd
}

function Parse-Seed([string]$SeedValue) {
    $repoPart = ""
    $branchPart = ""
    
    if ($SeedValue -match '^([^:]+):(.+)$') {
        $repoPart = $Matches[1]
        $branchPart = $Matches[2]
    } else {
        $repoPart = $SeedValue
        $branchPart = ""
    }
    
    return @{
        Url = "https://github.com/$repoPart"
        Branch = $branchPart
    }
}

function Get-DefaultRepoUrl {
    try {
        $url = & git remote get-url origin 2>$null
        if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace($url)) {
            return $url.Trim()
        }
    } catch { }
    return "https://github.com/haal-ai/haal-skills"
}

function Try-CloneBranch([string]$Url, [string]$Branch, [string]$Dest) {
    try {
        & git clone --depth 1 --branch $Branch $Url $Dest 2>$null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Clean-Folder([string]$Path) {
    if (Test-Path -LiteralPath $Path) {
        Remove-Item -LiteralPath $Path -Recurse -Force
    }
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
}

# Main execution
$null = Require-Command 'git'

# Resolve repo URL and branch
if (![string]::IsNullOrWhiteSpace($Seed)) {
    $parsed = Parse-Seed $Seed
    $RepoUrl = $parsed.Url
    $Branch = $parsed.Branch
} else {
    $RepoUrl = Get-DefaultRepoUrl
    $Branch = "main"
}

Write-Host "=== HAAL Skills Clone ===" -ForegroundColor Cyan
Write-Host "Source: $RepoUrl"
Write-Host "Branch: $(if ($Branch) { $Branch } else { 'auto (main/master)' })"
Write-Host ""

# Clean and prepare temp folder
Clean-Folder $TempCloneFolder

# Clone the repository
if (![string]::IsNullOrWhiteSpace($Branch)) {
    # Specific branch requested
    Write-Host "Cloning branch '$Branch'..."
    & git clone --depth 1 --branch $Branch $RepoUrl $TempCloneFolder
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to clone branch '$Branch' from $RepoUrl"
    }
} else {
    # Try main first, then master
    Write-Host "Trying branch 'main'..."
    if (Try-CloneBranch $RepoUrl "main" $TempCloneFolder) {
        Write-Host "Cloned 'main' branch"
    } else {
        Write-Host "Branch 'main' not found, trying 'master'..."
        if (Try-CloneBranch $RepoUrl "master" $TempCloneFolder) {
            Write-Host "Cloned 'master' branch"
        } else {
            throw "Could not clone 'main' or 'master' branch from $RepoUrl"
        }
    }
}

Write-Host ""
Write-Host "Clone complete: $TempCloneFolder"

# Output the path (for capturing in variable)
Write-Output $TempCloneFolder
