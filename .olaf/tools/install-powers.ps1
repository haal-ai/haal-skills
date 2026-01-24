# Haal AI Powers Installation Script for Kiro
# Copies powers to ~/.kiro/powers/installed/
# Registry update is done separately by Update-KiroPowersRegistry

param(
    [string]$SourcePath = ".",
    [string[]]$Competency = @(),
    [string]$Collection = "",
    [switch]$Force,
    [switch]$UpdateRegistry  # If set, update registry after copying (for standalone use)
)

$ErrorActionPreference = 'Continue'

$SourcePath = (Resolve-Path $SourcePath).Path
$PowersSourceDir = Join-Path $SourcePath "powers"
$CompetenciesDir = Join-Path $SourcePath "competencies"
$CollectionManifest = Join-Path $SourcePath "collection-manifest.json"
$KiroInstalledDir = Join-Path $env:USERPROFILE ".kiro\powers\installed"
$KiroRegistryFile = Join-Path $env:USERPROFILE ".kiro\powers\registry.json"

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

function Get-InstalledPowers {
    if (!(Test-Path $KiroInstalledDir)) { return @() }
    Get-ChildItem $KiroInstalledDir -Directory | 
        Where-Object { Test-Path (Join-Path $_.FullName "POWER.md") } |
        ForEach-Object { $_.Name }
}

function Parse-PowerMd([string]$PowerPath) {
    $powerMdPath = Join-Path $PowerPath "POWER.md"
    if (!(Test-Path $powerMdPath)) { return $null }
    
    $content = Get-Content $powerMdPath -Raw
    $result = @{
        name = ""
        displayName = ""
        description = ""
        author = ""
        keywords = @()
    }
    
    # Extract YAML frontmatter
    if ($content -match '(?s)^---\r?\n(.+?)\r?\n---') {
        $yaml = $Matches[1]
        
        if ($yaml -match 'name:\s*"?([^"\r\n]+)"?') { $result.name = $Matches[1].Trim() }
        if ($yaml -match 'displayName:\s*"?([^"\r\n]+)"?') { $result.displayName = $Matches[1].Trim() }
        if ($yaml -match 'description:\s*"?([^"\r\n]+)"?') { $result.description = $Matches[1].Trim() }
        if ($yaml -match 'author:\s*"?([^"\r\n]+)"?') { $result.author = $Matches[1].Trim() }
        
        # Parse keywords array
        if ($yaml -match 'keywords:\s*\[([^\]]*)\]') {
            $kwString = $Matches[1]
            $result.keywords = @($kwString -split ',' | ForEach-Object { $_.Trim().Trim('"').Trim("'") } | Where-Object { $_ })
        }
    }
    
    return $result
}

# Update registry with ALL installed powers (scans the installed directory)
function Update-KiroPowersRegistry {
    $installedPowers = @(Get-InstalledPowers)
    
    if ($installedPowers.Count -eq 0) {
        Write-Host "    No powers to register" -ForegroundColor Gray
        return
    }
    
    if (!(Test-Path $KiroRegistryFile)) {
        Write-Host "    WARN: No Kiro registry found. Open Kiro Powers panel first." -ForegroundColor Yellow
        return
    }
    
    $registryContent = Get-Content $KiroRegistryFile -Raw
    $registry = $registryContent | ConvertFrom-Json
    
    if ($null -eq $registry) {
        Write-Host "    WARN: Invalid Kiro registry." -ForegroundColor Yellow
        return
    }
    
    $timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
    $repoId = "haal-ai-powers"
    
    # Ensure repoSources exists
    if ($null -eq $registry.repoSources) {
        $registry | Add-Member -NotePropertyName "repoSources" -NotePropertyValue ([PSCustomObject]@{}) -Force
    }
    
    # Add repo source
    $repoSource = [PSCustomObject]@{
        name = "Haal AI Powers"
        type = "local"
        enabled = $true
        addedAt = $timestamp
        path = $KiroInstalledDir
        lastSync = $timestamp
        powerCount = $installedPowers.Count
    }
    
    if ($registry.repoSources.PSObject.Properties.Name -contains $repoId) {
        $registry.repoSources.$repoId = $repoSource
    } else {
        $registry.repoSources | Add-Member -NotePropertyName $repoId -NotePropertyValue $repoSource
    }
    
    # Add/update each installed power
    foreach ($powerName in $installedPowers) {
        $powerPath = Join-Path $KiroInstalledDir $powerName
        $metadata = Parse-PowerMd $powerPath
        
        if ($null -eq $metadata) { continue }
        
        $powerEntry = [PSCustomObject]@{
            name = if ($metadata.name) { $metadata.name } else { $powerName }
            description = if ($metadata.description) { $metadata.description } else { "" }
            displayName = if ($metadata.displayName) { $metadata.displayName } else { $powerName }
            author = if ($metadata.author) { $metadata.author } else { "Haal AI" }
            keywords = $metadata.keywords
            installed = $true
            installedAt = $timestamp
            installPath = $powerPath
            source = [PSCustomObject]@{
                type = "repo"
                repoId = $repoId
                repoName = "Haal AI Powers"
            }
            sourcePath = $powerPath
        }
        
        if ($registry.powers.PSObject.Properties.Name -contains $powerName) {
            $registry.powers.$powerName = $powerEntry
        } else {
            $registry.powers | Add-Member -NotePropertyName $powerName -NotePropertyValue $powerEntry
        }
    }
    
    $registry.lastUpdated = $timestamp
    
    # Convert to compact JSON then pretty-print with 2-space indent
    $compactJson = $registry | ConvertTo-Json -Depth 10 -Compress
    $prettyJson = Format-Json $compactJson
    
    [System.IO.File]::WriteAllText($KiroRegistryFile, $prettyJson)
    
    Write-Host "    Registry updated: $($installedPowers.Count) powers" -ForegroundColor Green
}

function Format-Json([string]$Json) {
    # Pretty print JSON with 2-space indentation
    $indent = 0
    $result = New-Object System.Text.StringBuilder
    $inString = $false
    $escaped = $false
    
    for ($i = 0; $i -lt $Json.Length; $i++) {
        $char = $Json[$i]
        
        if ($escaped) {
            [void]$result.Append($char)
            $escaped = $false
            continue
        }
        
        if ($char -eq '\') {
            [void]$result.Append($char)
            $escaped = $true
            continue
        }
        
        if ($char -eq '"') {
            $inString = -not $inString
            [void]$result.Append($char)
            continue
        }
        
        if ($inString) {
            [void]$result.Append($char)
            continue
        }
        
        switch ($char) {
            '{' {
                [void]$result.Append("{`n")
                $indent++
                [void]$result.Append("  " * $indent)
            }
            '}' {
                $indent--
                [void]$result.Append("`n")
                [void]$result.Append("  " * $indent)
                [void]$result.Append("}")
            }
            '[' {
                [void]$result.Append($char)
                # Check if empty array
                if ($i + 1 -lt $Json.Length -and $Json[$i + 1] -eq ']') {
                    # Empty array, don't add newline
                } else {
                    [void]$result.Append("`n")
                    $indent++
                    [void]$result.Append("  " * $indent)
                }
            }
            ']' {
                if ($i -gt 0 -and $Json[$i - 1] -ne '[') {
                    $indent--
                    [void]$result.Append("`n")
                    [void]$result.Append("  " * $indent)
                }
                [void]$result.Append("]")
            }
            ',' {
                [void]$result.Append(",`n")
                [void]$result.Append("  " * $indent)
            }
            ':' {
                [void]$result.Append(": ")
            }
            default {
                if ($char -notmatch '\s') {
                    [void]$result.Append($char)
                }
            }
        }
    }
    
    return $result.ToString()
}

function Update-KiroRegistry([string[]]$InstalledPowers, [string]$InstallDir) {
    # DEPRECATED: Use Update-KiroPowersRegistry instead
    # This function is kept for backward compatibility
    Update-KiroPowersRegistry
}

# === Main ===

if (!(Test-Path $PowersSourceDir)) {
    Write-Host "    ERROR: Powers source not found: $PowersSourceDir" -ForegroundColor Red
    exit 1
}

# Resolve powers to install
$allCompetencies = @()
if ($Collection) {
    $manifest = Read-JsonFile $CollectionManifest
    if ($manifest -and $manifest.$Collection) {
        $allCompetencies += $manifest.$Collection
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

# Copy powers to install directory
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

# Update registry if requested (for standalone use)
if ($UpdateRegistry) {
    Update-KiroPowersRegistry
}
