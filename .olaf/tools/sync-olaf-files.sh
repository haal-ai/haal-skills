#!/usr/bin/env bash
set -uo pipefail

# OLAF File Synchronization Script
# Syncs .olaf/ config files from source to target repo

SOURCE_PATH="${1:-}"
DEST_PATH="${2:-}"

# Determine source (from env var or default to global ~/.olaf)
if [[ -z "$SOURCE_PATH" ]]; then
    SOURCE_PATH="${HAAL_SKILLS_SOURCE:-}"
fi
if [[ -z "$SOURCE_PATH" ]]; then
    SOURCE_PATH="$HOME/.olaf"
fi

# Determine destination (current directory or param)
if [[ -z "$DEST_PATH" ]]; then
    DEST_PATH="$(pwd)"
fi

# Default folders to sync (relative paths from ~/.olaf)
DEFAULT_FOLDERS=(
    "data"
    "work"
    "tools"
)

# Git exclusions to add
GIT_EXCLUSIONS=(
    "olaf-*/"
    "my-skills-*/"
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
    local src_rel_folder="$2"
    local dest_base="$3"
    local dest_rel_folder="$4"
    shift 4
    local prune_files=("$@")
    
    local source_path="$source_base/$src_rel_folder"
    
    if [[ ! -d "$source_path" ]]; then
        echo "  SKIP: $src_rel_folder (not found)"
        return
    fi
    
    local copied=0
    local skipped=0
    
    while IFS= read -r -d '' file; do
        local rel_path="${file#$source_path/}"
        local dest_file="$dest_base/$dest_rel_folder/$rel_path"
        
        # Check prune list
        local should_prune=false
        for prune in "${prune_files[@]}"; do
            if [[ "$rel_path" == "$prune" ]]; then
                should_prune=true
                break
            fi
        done
        [[ "$should_prune" == "true" ]] && continue
        
        # Check if exists (skip if exists)
        if [[ -f "$dest_file" ]]; then
            ((skipped++)) || true
            continue
        fi
        
        # Create parent directory
        mkdir -p "$(dirname "$dest_file")" 2>/dev/null || true
        
        # Copy file
        cp "$file" "$dest_file"
        ((copied++)) || true
        
    done < <(find "$source_path" -type f -print0 2>/dev/null)
    
    echo "  $dest_rel_folder: $copied copied, $skipped skipped"
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
    local git_dir="$dest_base/.git"
    
    if [[ ! -d "$git_dir" ]]; then
        echo "  SKIP: Not a git repo"
        return
    fi
    
    local exclude_file="$git_dir/info/exclude"
    
    # Ensure .git/info exists
    mkdir -p "$git_dir/info" 2>/dev/null || true
    
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

# Resolve source path to absolute
if [[ ! "$SOURCE_PATH" = /* ]]; then
    SOURCE_PATH="$(cd "$SOURCE_PATH" 2>/dev/null && pwd)" || {
        echo "ERROR: Cannot resolve source path" >&2
        exit 1
    }
fi

echo "Source: $SOURCE_PATH"
echo "Destination: $DEST_PATH"
echo ""

if [[ ! -d "$SOURCE_PATH" ]]; then
    echo "ERROR: Source path not found" >&2
    exit 1
fi

# Load config
CONFIG_PATH="$SOURCE_PATH/local-file.json"
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

echo "Folders to sync: ${folders[*]}"

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
    rel_folder="$folder"
    
    # Handle absolute paths - convert to relative
    if [[ "$folder" = /* ]]; then
        # Try to extract just the relative part
        if [[ "$folder" == *".olaf"* ]]; then
            rel_folder="${folder##*.olaf/}"
        else
            echo "  SKIP: Cannot parse path $folder"
            continue
        fi
    fi
    
    # Source is directly under ~/.olaf, dest goes to .olaf/ in repo
    dest_rel_folder=".olaf/$rel_folder"
    sync_folder "$SOURCE_PATH" "$rel_folder" "$DEST_PATH" "$dest_rel_folder" "${prune_files_list[@]}"
done
echo ""

# Step 3: Update git exclude
echo "Step 3: Updating git exclude..."
update_git_exclude "$DEST_PATH"
echo ""

echo "=== Sync Complete ==="
