# OLAF File Synchronization Script
# Syncs .olaf/ config files from source to target repo

param(
    [string]$SourcePath = "",
    [string]$DestPath = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

# Determine source (from env var or default)
if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    $SourcePath = $env:HAAL_SKILLS_SOURCE
}
if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    $SourcePath = Join-Path $env:USERPROFILE ".codeium\windsurf\skills"
}

# Determine destination (current directory or param)
if ([string]::IsNullOrWhiteSpace($DestPath)) {
    $DestPath = (Get-Location).Path
}

# Config file location
$ConfigPath = Join-Path $SourcePath ".olaf\local-file.json"

# Default folders to sync
$DefaultFolders = @(
    ".olaf\data",
    ".olaf\work", 
    ".olaf\tools",
    ".windsurf\rules",
    ".windsurf\workflows"
)

# Git exclusions to add
$GitExclusions = @(
    "olaf-*",
    "my-skills-*",
    ".olaf/work/",
    ".olaf/data/context/"
)

function Read-Config([string]$Path) {
    if (!(Test-Path -LiteralPath $Path)) {
        return @{
            files_to_prune = @()
            files_to_force_replace = @()
            folders_to_copy_from = $DefaultFolders
        }
    }
    try {
        return Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json
    } catch {
        Write-Host "  WARN: Failed to parse config" -ForegroundColor Yellow
        return @{
            files_to_prune = @()
            files_to_force_replace = @()
            folders_to_copy_from = $DefaultFolders
        }
    }
}

function Sync-Folder([string]$SourceBase, [string]$RelFolder, [string]$DestBase, [string[]]$PruneFiles, [string[]]$ForceFiles) {
    $sourcePath = Join-Path $SourceBase $RelFolder
    
    if (!(Test-Path -LiteralPath $sourcePath)) {
        Write-Host "  SKIP: $RelFolder (not found)" -ForegroundColor Yellow
        return
    }
    
    $files = Get-ChildItem -LiteralPath $sourcePath -Recurse -File -ErrorAction SilentlyContinue
    $copied = 0
    $skipped = 0
    
    foreach ($file in $files) {
        $relPath = $file.FullName.Substring($SourceBase.Length + 1)
        $destFile = Join-Path $DestBase $relPath
        
        # Check prune list
        if ($PruneFiles -contains $relPath) {
            continue
        }
        
        # Check if exists and not force replace
        if ((Test-Path -LiteralPath $destFile) -and ($ForceFiles -notcontains $relPath)) {
            $skipped++
            continue
        }
        
        # Create parent directory
        $destDir = Split-Path -Parent $destFile
        if (!(Test-Path -LiteralPath $destDir)) {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
        }
        
        # Copy file
        Copy-Item -LiteralPath $file.FullName -Destination $destFile -Force
        $copied++
    }
    
    Write-Host "  $RelFolder : $copied copied, $skipped skipped" -ForegroundColor Green
}

function Prune-Files([string[]]$Files, [string]$DestBase) {
    foreach ($file in $Files) {
        $path = Join-Path $DestBase $file
        if (Test-Path -LiteralPath $path) {
            Remove-Item -LiteralPath $path -Recurse -Force -ErrorAction SilentlyContinue
            Write-Host "  Pruned: $file" -ForegroundColor Gray
        }
    }
}

function Update-GitExclude([string]$DestBase) {
    $gitDir = Join-Path $DestBase ".git"
    if (!(Test-Path -LiteralPath $gitDir)) {
        Write-Host "  SKIP: Not a git repo" -ForegroundColor Yellow
        return
    }
    
    $excludeFile = Join-Path $DestBase ".git\info\exclude"
    $infoDir = Split-Path -Parent $excludeFile
    
    # Ensure .git/info exists
    if (!(Test-Path -LiteralPath $infoDir)) {
        New-Item -ItemType Directory -Path $infoDir -Force -ErrorAction SilentlyContinue | Out-Null
    }
    
    # Read existing exclusions
    $existing = @()
    if (Test-Path -LiteralPath $excludeFile) {
        $existing = @(Get-Content -LiteralPath $excludeFile -ErrorAction SilentlyContinue | 
            Where-Object { $_ -and !$_.StartsWith('#') })
    }
    
    # Add new exclusions
    $toAdd = @($GitExclusions | Where-Object { $existing -notcontains $_ })
    
    if ($toAdd.Count -gt 0) {
        Add-Content -LiteralPath $excludeFile -Value "`n# OLAF sync exclusions" -ErrorAction SilentlyContinue
        foreach ($ex in $toAdd) {
            Add-Content -LiteralPath $excludeFile -Value $ex -ErrorAction SilentlyContinue
        }
        Write-Host "  Added $($toAdd.Count) git exclusions" -ForegroundColor Green
    } else {
        Write-Host "  Git exclusions already set" -ForegroundColor Gray
    }
}

# === Main ===

Write-Host "=== OLAF File Sync ===" -ForegroundColor Cyan
Write-Host "Source: $SourcePath"
Write-Host "Destination: $DestPath"
Write-Host ""

if (!(Test-Path -LiteralPath $SourcePath)) {
    Write-Host "ERROR: Source path not found" -ForegroundColor Red
    exit 1
}

# Load config
$config = Read-Config $ConfigPath
$pruneFiles = @($config.files_to_prune)
$forceFiles = @($config.files_to_force_replace)
$folders = @($config.folders_to_copy_from)

if ($folders.Count -eq 0) {
    $folders = $DefaultFolders
}

# Step 1: Prune files
Write-Host "Step 1: Pruning files..." -ForegroundColor Cyan
if ($pruneFiles.Count -gt 0) {
    Prune-Files $pruneFiles $DestPath
} else {
    Write-Host "  No files to prune"
}
Write-Host ""

# Step 2: Sync folders
Write-Host "Step 2: Syncing folders..." -ForegroundColor Cyan
foreach ($folder in $folders) {
    # Handle both absolute and relative paths
    if ([System.IO.Path]::IsPathRooted($folder)) {
        # Absolute path - extract relative part
        if ($folder.StartsWith($SourcePath)) {
            $relFolder = $folder.Substring($SourcePath.Length + 1)
        } else {
            continue
        }
    } else {
        $relFolder = $folder
    }
    Sync-Folder $SourcePath $relFolder $DestPath $pruneFiles $forceFiles
}
Write-Host ""

# Step 3: Update git exclude
Write-Host "Step 3: Updating git exclude..." -ForegroundColor Cyan
Update-GitExclude $DestPath
Write-Host ""

Write-Host "=== Done ===" -ForegroundColor Green
