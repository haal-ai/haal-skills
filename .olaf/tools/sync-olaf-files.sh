#!/usr/bin/env bash
# OLAF File Synchronization Script
# Syncs .olaf/ config files from source to target repo

set -uo pipefail

SOURCE_PATH="${1:-}"
DEST_PATH="${2:-}"

# Determine source (from env var or default)
if [[ -z "$SOURCE_PATH" ]]; then
    SOURCE_PATH="${HAAL_SKILLS_SOURCE:-}"
fi
if [[ -z "$SOURCE_PATH" ]]; then
    SOURCE_PATH="$HOME/.codeium/windsurf/skills"
fi

# Determine destination (current directory or param)
if [[ -z "$DEST_PATH" ]]; then
    DEST_PATH="$(pwd)"
fi

# Config file location
CONFIG_PATH="$SOURCE_PATH/.olaf/local-file.json"

# Default folders to sync
DEFAULT_FOLDERS=(
    ".olaf/data"
    ".olaf/work"
    ".olaf/tools"
    ".windsurf/rules"
    ".windsurf/workflows"
)

# Git exclusions to add
GIT_EXCLUSIONS=(
    "olaf-*"
    "my-skills-*"
    ".olaf/work/"
    ".olaf/data/context/"
)

read_json_array() {
    local file="$1"
    local key="$2"
    if [[ ! -f "$file" ]]; then
        return
    fi
    python3 -c "
import json
try:
    with open('$file') as f:
        data = json.load(f)
    for item in data.get('$key', []):
        print(item)
except:
    pass
" 2>/dev/null || true
}

sync_folder() {
    local source_base="$1"
    local rel_folder="$2"
    local dest_base="$3"
    shift 3
    local prune_files=("$@")
    
    local source_path="$source_base/$rel_folder"
    
    if [[ ! -d "$source_path" ]]; then
        echo "  SKIP: $rel_folder (not found)"
        return
    fi
    
    local copied=0
    local skipped=0
    
    while IFS= read -r -d '' file; do
        local rel_path="${file#$source_base/}"
        local dest_file="$dest_base/$rel_path"
        
        # Check prune list
        local should_prune=false
        for prune in "${prune_files[@]}"; do
            if [[ "$rel_path" == "$prune" ]]; then
                should_prune=true
                break
            fi
        done
        [[ "$should_prune" == "true" ]] && continue
        
        # Check if exists (skip if exists, unless force)
        if [[ -f "$dest_file" ]]; then
            ((skipped++)) || true
            continue
        fi
        
        # Create parent directory
        mkdir -p "$(dirname "$dest_file")"
        
        # Copy file
        cp "$file" "$dest_file"
        ((copied++)) || true
        
    done < <(find "$source_path" -type f -print0 2>/dev/null)
    
    echo "  $rel_folder: $copied copied, $skipped skipped"
}

prune_files() {
    local dest_base="$1"
    shift
    local files=("$@")
    
    for file in "${files[@]}"; do
        local path="$dest_base/$file"
        if [[ -e "$path" ]]; then
            rm -rf "$path"
            echo "  Pruned: $file"
        fi
    done
}

update_git_exclude() {
    local dest_base="$1"
    local exclude_file="$dest_base/.git/info/exclude"
    
    if [[ ! -d "$dest_base/.git" ]]; then
        echo "  SKIP: Not a git repo"
        return
    fi
    
    # Ensure .git/info exists
    mkdir -p "$dest_base/.git/info"
    
    # Read existing exclusions
    local existing=()
    if [[ -f "$exclude_file" ]]; then
        while IFS= read -r line; do
            [[ -n "$line" && ! "$line" =~ ^# ]] && existing+=("$line")
        done < "$exclude_file"
    fi
    
    # Add new exclusions
    local added=0
    for ex in "${GIT_EXCLUSIONS[@]}"; do
        local found=false
        for e in "${existing[@]}"; do
            [[ "$e" == "$ex" ]] && found=true && break
        done
        if [[ "$found" == "false" ]]; then
            [[ $added -eq 0 ]] && echo "" >> "$exclude_file" && echo "# OLAF sync exclusions" >> "$exclude_file"
            echo "$ex" >> "$exclude_file"
            ((added++)) || true
        fi
    done
    
    if [[ $added -gt 0 ]]; then
        echo "  Added $added git exclusions"
    else
        echo "  Git exclusions already set"
    fi
}

# === Main ===

echo "=== OLAF File Sync ==="
echo "Source: $SOURCE_PATH"
echo "Destination: $DEST_PATH"
echo ""

if [[ ! -d "$SOURCE_PATH" ]]; then
    echo "ERROR: Source path not found" >&2
    exit 1
fi

# Load config
prune_files_list=()
while IFS= read -r line; do
    [[ -n "$line" ]] && prune_files_list+=("$line")
done < <(read_json_array "$CONFIG_PATH" "files_to_prune")

folders=()
while IFS= read -r line; do
    [[ -n "$line" ]] && folders+=("$line")
done < <(read_json_array "$CONFIG_PATH" "folders_to_copy_from")

if [[ ${#folders[@]} -eq 0 ]]; then
    folders=("${DEFAULT_FOLDERS[@]}")
fi

# Step 1: Prune files
echo "Step 1: Pruning files..."
if [[ ${#prune_files_list[@]} -gt 0 ]]; then
    prune_files "$DEST_PATH" "${prune_files_list[@]}"
else
    echo "  No files to prune"
fi
echo ""

# Step 2: Sync folders
echo "Step 2: Syncing folders..."
for folder in "${folders[@]}"; do
    # Handle both absolute and relative paths
    if [[ "$folder" = /* ]]; then
        # Absolute path - extract relative part
        if [[ "$folder" == "$SOURCE_PATH"* ]]; then
            rel_folder="${folder#$SOURCE_PATH/}"
        else
            continue
        fi
    else
        rel_folder="$folder"
    fi
    sync_folder "$SOURCE_PATH" "$rel_folder" "$DEST_PATH" "${prune_files_list[@]}"
done
echo ""

# Step 3: Update git exclude
echo "Step 3: Updating git exclude..."
update_git_exclude "$DEST_PATH"
echo ""

echo "=== Done ==="
