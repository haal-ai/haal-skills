# OLAF File Synchronization Script
# Syncs .olaf/ config files from source to target repo

param(
    [string]$SourcePath = "",
    [string]$DestPath = "",
    [string]$ConfigFile = ""  # Optional: path to config file (defaults to source/.olaf/local-file.json)
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

# Determine source (from env var or default to global ~/.olaf)
if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    $SourcePath = $env:HAAL_SKILLS_SOURCE
}
if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    $SourcePath = Join-Path $env:USERPROFILE ".olaf"
}

# Determine destination (current directory or param)
if ([string]::IsNullOrWhiteSpace($DestPath)) {
    $DestPath = (Get-Location).Path
}

# Config file location (use param if provided, otherwise default)
if ([string]::IsNullOrWhiteSpace($ConfigFile)) {
    $ConfigPath = Join-Path $SourcePath ".olaf\local-file.json"
} else {
    $ConfigPath = $ConfigFile
}

# Default folders to sync (relative paths from ~/.olaf)
$DefaultFolders = @(
    "data",
    "work", 
    "tools"
)

# Git exclusions to add
$GitExclusions = @(
    "olaf-*/",
    "my-skills-*/",
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

function Sync-Folder([string]$SourceBase, [string]$SrcRelFolder, [string]$DestBase, [string]$DestRelFolder, [string[]]$PruneFiles, [string[]]$ForceFiles) {
    $sourcePath = Join-Path $SourceBase $SrcRelFolder
    
    if (!(Test-Path -LiteralPath $sourcePath)) {
        return
    }
    
    $files = Get-ChildItem -LiteralPath $sourcePath -Recurse -File -ErrorAction SilentlyContinue
    $copied = 0
    $skipped = 0
    
    foreach ($file in $files) {
        $relPath = $file.FullName.Substring($sourcePath.Length + 1)
        $destFile = Join-Path $DestBase (Join-Path $DestRelFolder $relPath)
        
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
    
    Write-Host "      $DestRelFolder : $copied copied, $skipped skipped" -ForegroundColor Gray
}

function Prune-Files([string[]]$Files, [string]$DestBase) {
    $pruned = 0
    foreach ($file in $Files) {
        $path = Join-Path $DestBase $file
        if (Test-Path -LiteralPath $path) {
            Remove-Item -LiteralPath $path -Recurse -Force -ErrorAction SilentlyContinue
            $pruned++
        }
    }
    return $pruned
}

function Update-GitExclude([string]$DestBase) {
    $gitDir = Join-Path $DestBase ".git"
    if (!(Test-Path -LiteralPath $gitDir)) {
        return 0
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
    }
    return $toAdd.Count
}

# === Main ===

# Resolve paths to absolute
if (![System.IO.Path]::IsPathRooted($SourcePath)) {
    $SourcePath = (Resolve-Path -LiteralPath $SourcePath -ErrorAction SilentlyContinue).Path
    if (!$SourcePath) {
        Write-Host "      ERROR: Cannot resolve source path" -ForegroundColor Red
        exit 1
    }
}

if (!(Test-Path -LiteralPath $SourcePath)) {
    Write-Host "      ERROR: Source path not found" -ForegroundColor Red
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

# Prune files from both destination AND source (to prevent re-copying)
$pruneCount = $pruneFiles.Count
if ($pruneCount -gt 0) {
    $prunedDest = Prune-Files $pruneFiles $DestPath
    $prunedSrc = Prune-Files $pruneFiles $SourcePath
    $totalPruned = $prunedDest + $prunedSrc
    if ($totalPruned -gt 0) {
        Write-Host "      Pruned $totalPruned files" -ForegroundColor Gray
    }
}

# Sync folders
foreach ($folder in $folders) {
    $relFolder = $folder
    
    # Handle absolute paths - convert to relative
    if ([System.IO.Path]::IsPathRooted($folder)) {
        # Try to extract just the relative part
        $parts = $folder -split '[/\\]'
        $olafIdx = [Array]::IndexOf($parts, '.olaf')
        
        if ($olafIdx -ge 0) {
            # Skip the .olaf part, get subfolders
            $relFolder = ($parts[($olafIdx+1)..($parts.Length-1)]) -join '\'
        } else {
            continue
        }
    }
    
    # Source is directly under ~/.olaf, dest goes to .olaf/ in repo
    $destRelFolder = ".olaf\$relFolder"
    Sync-Folder $SourcePath $relFolder $DestPath $destRelFolder $pruneFiles $forceFiles
}

# Update git exclude
$gitAdded = Update-GitExclude $DestPath
if ($gitAdded -gt 0) {
    Write-Host "      Git exclusions: $gitAdded added" -ForegroundColor Gray
}
