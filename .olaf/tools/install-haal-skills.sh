#!/usr/bin/env bash
set -uo pipefail

REPO_PATH=""
CLONE_PATH=""
COMPETENCIES=()
COLLECTION=""
CLEAN=false
PLATFORM="all"

# Fixed temp folder for staging
# Use Windows-compatible temp path if on Windows (Git Bash)
if [[ -n "${USERPROFILE:-}" ]]; then
    TEMP_STAGING_FOLDER="$(cygpath -u "$LOCALAPPDATA")/Temp/haal-skills-staging"
else
    TEMP_STAGING_FOLDER="${TMPDIR:-/tmp}/haal-skills-staging"
fi

# Destination folders for skills
declare -A ALL_SKILL_DESTINATIONS=(
    ["windsurf"]="$HOME/.codeium/windsurf/skills"
    ["claude"]="$HOME/.claude/skills"
    ["github"]="$HOME/.github/skills"
    ["kiro"]="$HOME/.kiro/skills"
)

# Global OLAF folder
OLAF_DESTINATION="$HOME/.olaf"

show_help() {
    echo "Usage: $0 --clone-path PATH [options]"
    echo ""
    echo "Install HAAL skills from a cloned repository."
    echo ""
    echo "Required:"
    echo "  --clone-path PATH        Path to the cloned skills repository"
    echo ""
    echo "Options:"
    echo "  --repo-path PATH         Target repository path (for sync script)"
    echo "  --collection NAME        Collection name to install"
    echo "  --competency NAME        Competency name (can be repeated)"
    echo "  --clean                  Delete existing skills first (default: update only)"
    echo "  --platform PLATFORM      Platform: all, kiro, claude, windsurf, github"
    echo "  -h, --help               Show this help message"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --clone-path)
            CLONE_PATH="${2:-}"; shift 2;;
        --repo-path)
            REPO_PATH="${2:-}"; shift 2;;
        --competency)
            COMPETENCIES+=("${2:-}"); shift 2;;
        --collection)
            COLLECTION="${2:-}"; shift 2;;
        --clean)
            CLEAN=true; shift;;
        --platform)
            PLATFORM="${2:-all}"; shift 2;;
        -h|--help)
            show_help
            exit 0;;
        *)
            echo "Unknown argument: $1" >&2
            show_help >&2
            exit 2;;
    esac
done

# Validate required argument
if [[ -z "$CLONE_PATH" ]]; then
    echo "Error: --clone-path is required" >&2
    show_help >&2
    exit 1
fi

if [[ ! -d "$CLONE_PATH" ]]; then
    echo "Error: Clone path does not exist: $CLONE_PATH" >&2
    exit 1
fi

# Select destinations based on platform
SKILL_DESTINATIONS=()
if [[ "$PLATFORM" == "all" ]]; then
    for dest in "${ALL_SKILL_DESTINATIONS[@]}"; do
        SKILL_DESTINATIONS+=("$dest")
    done
else
    SKILL_DESTINATIONS+=("${ALL_SKILL_DESTINATIONS[$PLATFORM]}")
fi

resolve_repo_root() {
    if [[ -n "$REPO_PATH" ]]; then
        (cd "$REPO_PATH" 2>/dev/null && pwd -P) || echo "$REPO_PATH"
        return
    fi
    if git_root=$(git rev-parse --show-toplevel 2>/dev/null) && [[ -n "$git_root" ]]; then
        echo "$git_root"
        return
    fi
    pwd -P
}

clean_folder() {
    local path="$1"
    rm -rf "$path" 2>/dev/null || true
    mkdir -p "$path"
}

clean_skill_destinations() {
    for dest in "${SKILL_DESTINATIONS[@]}"; do
        if [[ -d "$dest" ]]; then
            local count=0
            for folder in "$dest"/*/; do
                if [[ -d "$folder" ]]; then
                    rm -rf "$folder"
                    ((count++)) || true
                fi
            done
            echo "  Cleaned $count skills from: $dest"
        fi
    done
}

read_json_array() {
    local file="$1"
    local key="$2"
    if [[ ! -f "$file" ]]; then
        return
    fi
    if command -v jq &>/dev/null; then
        jq -r --arg key "$key" '.[$key][]? // empty' "$file" 2>/dev/null | tr -d '\r' || true
        return
    fi

    # Bash-only fallback (supports our simple top-level: {"key": ["a","b", ...]})
    # Works for both pretty-printed and minified JSON.
    local key_escaped
    key_escaped=$(printf '%s' "$key" | sed 's/[][\\.^$*]/\\&/g')

    local compact
    compact=$(tr -d '\n\r\t ' < "$file" 2>/dev/null || true)
    [[ -z "$compact" ]] && return

    local array_contents
    array_contents=$(printf '%s' "$compact" | sed -n "s/.*\"$key_escaped\":\\[\\([^]]*\\)\\].*/\\1/p" | head -n 1)
    [[ -z "$array_contents" ]] && return

    # Extract quoted string elements.
    # Example input: "a","b","c"  -> outputs a\nb\nc
    printf '%s\n' "$array_contents" | tr ',' '\n' | sed -n 's/^"\(.*\)"$/\1/p' | tr -d '\r' || true
}

get_skills_path() {
    local clone_path="$1"
    local skills_subfolder="$clone_path/skills"
    if [[ -d "$skills_subfolder" ]]; then
        echo "$skills_subfolder"
    else
        echo "$clone_path"
    fi
}

get_all_skills() {
    local clone_path="$1"
    local skills_path
    skills_path=$(get_skills_path "$clone_path")
    
    if [[ -d "$skills_path" ]]; then
        for dir in "$skills_path"/*/; do
            if [[ -f "${dir}skill.md" ]]; then
                basename "$dir"
            fi
        done
    fi
}

get_prune_list() {
    local clone_path="$1"
    local prune_file="$clone_path/.olaf/prune-skills.txt"
    if [[ -f "$prune_file" ]]; then
        grep -v '^#' "$prune_file" 2>/dev/null | grep -v '^$' | tr -d '\r' || true
    fi
}

get_competencies_from_collection() {
    local collection="$1"
    local clone_path="$2"
    read_json_array "$clone_path/collection-manifest.json" "$collection"
}

get_skills_from_competency() {
    local competency="$1"
    local clone_path="$2"
    local manifest_file="$clone_path/competencies/$competency.json"
    if [[ -f "$manifest_file" ]]; then
        read_json_array "$manifest_file" "skills"
    fi
}

prune_skills() {
    local skill="$1"
    for dest in "${SKILL_DESTINATIONS[@]}"; do
        local skill_path="$dest/$skill"
        if [[ -d "$skill_path" ]]; then
            rm -rf "$skill_path" 2>/dev/null || true
            echo "  Pruned: $skill"
        fi
    done
}

copy_skill_to_staging() {
    local skill="$1"
    local clone_path="$2"
    local staging_path="$3"
    local skills_path
    skills_path=$(get_skills_path "$clone_path")
    local source_path="$skills_path/$skill"
    local dest_path="$staging_path/$skill"
    
    if [[ -d "$source_path" ]]; then
        rm -rf "$dest_path" 2>/dev/null || true
        cp -r "$source_path" "$dest_path"
        return 0
    else
        echo "  SKIP: Skill '$skill' not found"
        return 1
    fi
}

deploy_staging_to_destinations() {
    local staging_path="$1"
    
    for dest in "${SKILL_DESTINATIONS[@]}"; do
        mkdir -p "$dest" 2>/dev/null || true
        
        local count=0
        for skill_dir in "$staging_path"/*/; do
            if [[ -d "$skill_dir" ]]; then
                local skill_name
                skill_name=$(basename "$skill_dir")
                local dest_skill_path="$dest/$skill_name"
                
                rm -rf "$dest_skill_path" 2>/dev/null || true
                cp -r "$skill_dir" "$dest_skill_path" 2>/dev/null || true
                ((count++)) || true
            fi
        done
        
        echo "  Deployed $count skills to: $dest"
    done
}


copy_olaf_folder() {
    local clone_path="$1"
    local source_olaf="$clone_path/.olaf"
    
    if [[ ! -d "$source_olaf" ]]; then
        echo "  SKIP: No .olaf folder in source"
        return
    fi
    
    mkdir -p "$OLAF_DESTINATION" 2>/dev/null || true
    
    local olaf_folders=("data" "work" "tools")
    for folder in "${olaf_folders[@]}"; do
        local src_folder="$source_olaf/$folder"
        local dest_folder="$OLAF_DESTINATION/$folder"
        
        if [[ -d "$src_folder" ]]; then
            local copied=0
            while IFS= read -r -d '' file; do
                local rel_path="${file#$src_folder/}"
                local dest_file="$dest_folder/$rel_path"
                
                if [[ ! -f "$dest_file" ]]; then
                    mkdir -p "$(dirname "$dest_file")" 2>/dev/null || true
                    cp "$file" "$dest_file"
                    ((copied++)) || true
                fi
            done < <(find "$src_folder" -type f -print0 2>/dev/null)
            echo "  .olaf/$folder: $copied new files"
        fi
    done
}

# === Main execution ===

echo "=== HAAL Skills Install ==="

REPO_ROOT="$(resolve_repo_root)"

echo "Clone path: $CLONE_PATH"
echo "Repo: $REPO_ROOT"
echo "Collection: ${COLLECTION:-(none)}"
echo "Competencies: ${COMPETENCIES[*]:-(none)}"
echo "Mode: $(if [[ "$CLEAN" == "true" ]]; then echo 'Clean install'; else echo 'Update only'; fi)"
echo "Platform: $PLATFORM"
echo ""

# Step 0: Clean skill destinations (only if --clean)
if [[ "$CLEAN" == "true" ]]; then
    echo "Step 0: Cleaning skill destinations..."
    clean_skill_destinations
    echo ""
fi

# Step 1: Read prune list and prune skills
echo "Step 1: Pruning deprecated skills..."
prune_list=$(get_prune_list "$CLONE_PATH")
if [[ -n "$prune_list" ]]; then
    while IFS= read -r skill; do
        [[ -n "$skill" ]] && prune_skills "$skill"
    done <<< "$prune_list"
else
    echo "  No skills to prune"
fi
echo ""

# Step 2: Resolve skills to install
echo "Step 2: Resolving skills..."
all_competencies=()

if [[ -n "$COLLECTION" ]]; then
    while IFS= read -r comp; do
        if [[ -n "$comp" ]]; then
            all_competencies+=("$comp")
        fi
    done < <(get_competencies_from_collection "$COLLECTION" "$CLONE_PATH")
    
    if [[ ${#all_competencies[@]} -gt 0 ]]; then
        echo "  OK: Collection '$COLLECTION' (${#all_competencies[@]} competencies)"
    else
        echo "  SKIP: Collection '$COLLECTION' not found"
    fi
fi

for comp in "${COMPETENCIES[@]}"; do
    all_competencies+=("$comp")
done

# Dedupe
if [[ ${#all_competencies[@]} -gt 0 ]]; then
    mapfile -t all_competencies < <(printf '%s\n' "${all_competencies[@]}" | sort -u)
fi

skills_to_install=()
if [[ ${#all_competencies[@]} -gt 0 ]]; then
    for comp in "${all_competencies[@]}"; do
        comp_skills=()
        while IFS= read -r skill; do
            if [[ -n "$skill" ]]; then
                comp_skills+=("$skill")
                skills_to_install+=("$skill")
            fi
        done < <(get_skills_from_competency "$comp" "$CLONE_PATH")
        
        if [[ ${#comp_skills[@]} -gt 0 ]]; then
            echo "  OK: Competency '$comp' (${#comp_skills[@]} skills)"
        else
            echo "  SKIP: Competency '$comp' not found"
        fi
    done
else
    echo "  No collection/competency specified, installing all skills"
    while IFS= read -r skill; do
        [[ -n "$skill" ]] && skills_to_install+=("$skill")
    done < <(get_all_skills "$CLONE_PATH")
fi

# Dedupe
if [[ ${#skills_to_install[@]} -gt 0 ]]; then
    mapfile -t skills_to_install < <(printf '%s\n' "${skills_to_install[@]}" | sort -u)
fi

echo "  Skills to install: ${#skills_to_install[@]}"
echo ""

if [[ ${#skills_to_install[@]} -eq 0 ]]; then
    echo "WARN: No skills found to install"
    exit 0
fi

# Step 3: Clean staging and copy selected skills
echo "Step 3: Staging skills..."
clean_folder "$TEMP_STAGING_FOLDER"
staged=0
for skill in "${skills_to_install[@]}"; do
    if copy_skill_to_staging "$skill" "$CLONE_PATH" "$TEMP_STAGING_FOLDER"; then
        ((staged++)) || true
    fi
done
echo "  Staged $staged skills"
echo ""

# Step 4: Deploy to all destinations
echo "Step 4: Deploying skills to destinations..."
deploy_staging_to_destinations "$TEMP_STAGING_FOLDER"
echo ""

# Step 5: Copy .olaf folder to global location
echo "Step 5: Syncing .olaf to global location..."
copy_olaf_folder "$CLONE_PATH"
echo ""

# Step 6: Install Kiro Powers
echo "Step 6: Installing Kiro Powers..."
powers_script="$CLONE_PATH/.olaf/tools/install-powers.sh"
if [[ -f "$powers_script" ]]; then
    chmod +x "$powers_script" 2>/dev/null || true
    powers_args=("$CLONE_PATH")
    if [[ -n "$COLLECTION" ]]; then
        powers_args+=("--collection" "$COLLECTION")
    fi
    for comp in "${COMPETENCIES[@]}"; do
        powers_args+=("--competency" "$comp")
    done
    "$powers_script" "${powers_args[@]}" && echo "  OK: Kiro Powers installed" || echo "  WARN: Powers install failed"
else
    echo "  SKIP: Powers install script not found"
fi
echo ""

# Step 7: Sync to repo if RepoPath specified
if [[ -n "$REPO_PATH" ]]; then
    echo "Step 7: Syncing to repo..."
    sync_script="$CLONE_PATH/.olaf/tools/sync-olaf-files.sh"
    if [[ -f "$sync_script" ]]; then
        chmod +x "$sync_script" 2>/dev/null || true
        "$sync_script" "$OLAF_DESTINATION" "$REPO_ROOT" && echo "  OK: .olaf files synced to repo" || echo "  WARN: Sync script failed"
    else
        echo "  SKIP: Sync script not found"
    fi
    
    # Copy AGENTS.md to repo root if it doesn't exist
    agents_md_src="$OLAF_DESTINATION/data/AGENTS.md"
    agents_md_dst="$REPO_ROOT/AGENTS.md"
    if [[ -f "$agents_md_src" && ! -f "$agents_md_dst" ]]; then
        cp "$agents_md_src" "$agents_md_dst"
        echo "  AGENTS.md copied to repo root"
    fi
    echo ""
fi

echo "=== Install Complete ==="
