#!/usr/bin/env bash
set -euo pipefail

REPO_PATH=""
CLONE_PATH=""
COMPETENCIES=()
COLLECTION=""

# Fixed temp folder for staging
TEMP_STAGING_FOLDER="${TMPDIR:-/tmp}/haal-skills-staging"

# Destination folders
DESTINATIONS=(
    "$HOME/.codeium/windsurf/skills"
    "$HOME/.claude/skills"
    "$HOME/.github/skills"
    "$HOME/.kiro/skills"
)

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
    echo "  --competency NAME,NAME   Competency names (comma-separated)"
    echo "  -h, --help               Show this help message"
    echo ""
    echo "If no collection or competency is specified, all skills are installed."
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --clone-path)
            CLONE_PATH="${2:-}"; shift 2;;
        --repo-path)
            REPO_PATH="${2:-}"; shift 2;;
        --competency)
            IFS=',' read -ra COMP_ARRAY <<< "${2:-}"
            COMPETENCIES+=("${COMP_ARRAY[@]}")
            shift 2;;
        --collection)
            COLLECTION="${2:-}"; shift 2;;
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

resolve_repo_root() {
    if [[ -n "$REPO_PATH" ]]; then
        (cd "$REPO_PATH" && pwd -P)
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
    if [[ -d "$path" ]]; then
        rm -rf "$path"
        echo "Cleaned: $path"
    fi
    mkdir -p "$path"
}

read_json_array() {
    local file="$1"
    local key="$2"
    if [[ ! -f "$file" ]]; then
        return
    fi
    python3 -c "
import json, sys
with open('$file') as f:
    data = json.load(f)
if '$key' in data:
    for item in data['$key']:
        print(item)
" 2>/dev/null || true
}

get_all_skills() {
    local clone_path="$1"
    local skills_path="$clone_path/skills"
    if [[ -d "$skills_path" ]]; then
        ls -1 "$skills_path" 2>/dev/null || true
    fi
}

get_prune_list() {
    local clone_path="$1"
    local prune_file="$clone_path/.olaf/prune-skills.txt"
    if [[ -f "$prune_file" ]]; then
        grep -v '^#' "$prune_file" | grep -v '^$' | tr -d '\r' || true
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
    else
        echo "Warning: Competency '$competency' manifest not found" >&2
    fi
}

prune_skills() {
    local skill="$1"
    for dest in "${DESTINATIONS[@]}"; do
        local skill_path="$dest/$skill"
        if [[ -d "$skill_path" ]]; then
            rm -rf "$skill_path"
            echo "Pruned: $skill_path"
        fi
    done
}

copy_skill_to_staging() {
    local skill="$1"
    local clone_path="$2"
    local staging_path="$3"
    local source_path="$clone_path/skills/$skill"
    local dest_path="$staging_path/$skill"
    
    if [[ -d "$source_path" ]]; then
        rm -rf "$dest_path" 2>/dev/null || true
        cp -r "$source_path" "$dest_path"
        echo "Staged: $skill"
    else
        echo "Warning: Skill '$skill' not found in source"
    fi
}

deploy_staging_to_destinations() {
    local staging_path="$1"
    
    for dest in "${DESTINATIONS[@]}"; do
        mkdir -p "$dest"
        
        local count=0
        for skill_dir in "$staging_path"/*/; do
            if [[ -d "$skill_dir" ]]; then
                local skill_name=$(basename "$skill_dir")
                local dest_skill_path="$dest/$skill_name"
                
                rm -rf "$dest_skill_path" 2>/dev/null || true
                cp -r "$skill_dir" "$dest_skill_path"
                ((count++)) || true
            fi
        done
        
        echo "Deployed $count skills to: $dest"
    done
}

# Main execution
PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "Required command 'python' or 'python3' not found."; exit 1
fi

REPO_ROOT="$(resolve_repo_root)"

echo "=== HAAL Skills Install ==="
echo "Clone path: $CLONE_PATH"
echo "Repo: $REPO_ROOT"
echo "Collection: ${COLLECTION:-(none)}"
echo "Competencies: ${COMPETENCIES[*]:-(none)}"
echo ""

# Step 1: Read prune list and prune skills
echo "Step 1: Pruning deprecated skills..."
prune_list=$(get_prune_list "$CLONE_PATH")
if [[ -n "$prune_list" ]]; then
    echo "Skills to prune: $prune_list"
    while IFS= read -r skill; do
        [[ -n "$skill" ]] && prune_skills "$skill"
    done <<< "$prune_list"
else
    echo "No skills to prune"
fi
echo ""

# Step 2: Resolve skills to install
echo "Step 2: Resolving skills..."
all_competencies=()

if [[ -n "$COLLECTION" ]]; then
    echo "Collection '$COLLECTION':"
    while IFS= read -r comp; do
        [[ -n "$comp" ]] && all_competencies+=("$comp")
    done < <(get_competencies_from_collection "$COLLECTION" "$CLONE_PATH")
    echo "  Competencies: ${all_competencies[*]}"
fi

for comp in "${COMPETENCIES[@]}"; do
    all_competencies+=("$comp")
done

all_competencies=($(printf '%s\n' "${all_competencies[@]}" | sort -u))

skills_to_install=()
if [[ ${#all_competencies[@]} -gt 0 ]]; then
    for comp in "${all_competencies[@]}"; do
        echo "Competency '$comp':"
        while IFS= read -r skill; do
            if [[ -n "$skill" ]]; then
                skills_to_install+=("$skill")
                echo "  - $skill"
            fi
        done < <(get_skills_from_competency "$comp" "$CLONE_PATH")
    done
else
    echo "No collection/competency specified, installing all skills"
    while IFS= read -r skill; do
        [[ -n "$skill" ]] && skills_to_install+=("$skill")
    done < <(get_all_skills "$CLONE_PATH")
fi

skills_to_install=($(printf '%s\n' "${skills_to_install[@]}" | sort -u))
echo "Skills to install: ${#skills_to_install[@]}"
echo ""

# Step 3: Clean staging and copy selected skills
echo "Step 3: Staging skills..."
clean_folder "$TEMP_STAGING_FOLDER"
for skill in "${skills_to_install[@]}"; do
    copy_skill_to_staging "$skill" "$CLONE_PATH" "$TEMP_STAGING_FOLDER"
done
echo ""

# Step 4: Deploy to all destinations
echo "Step 4: Deploying to destinations..."
deploy_staging_to_destinations "$TEMP_STAGING_FOLDER"
echo ""

# Step 5: Run sync script for .olaf files
echo "Step 5: Syncing .olaf files..."
sync_script="$CLONE_PATH/.olaf/tools/sync_olaf_files.py"
if [[ -f "$sync_script" ]]; then
    (
        cd "$REPO_ROOT"
        export HAAL_SKILLS_SOURCE="$CLONE_PATH"
        "$PYTHON_BIN" "$sync_script"
    )
else
    echo "Warning: sync script not found"
fi
echo ""

echo "=== Done ==="
