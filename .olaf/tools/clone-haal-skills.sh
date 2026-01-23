#!/usr/bin/env bash
set -euo pipefail

# Default values - will be resolved from local git repo
DEFAULT_REPO_URL=""
DEFAULT_BRANCH=""
SEED=""

# Fixed temp folder for clone
TEMP_CLONE_FOLDER="${TMPDIR:-/tmp}/haal-skills-clone"

show_help() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Clone the HAAL skills repository to a temp folder."
    echo ""
    echo "Options:"
    echo "  --seed OWNER/REPO:BRANCH   Override source repo (e.g., 'haal-ai/haal-skills:main')"
    echo "                             Branch is optional; if omitted, tries 'main' then 'master'"
    echo "  -h, --help                 Show this help message"
    echo ""
    echo "Output:"
    echo "  Prints the path to the cloned folder on success"
    echo ""
    echo "Default behavior:"
    echo "  - Clones from the origin remote of the local repo"
    echo "  - Uses 'main' branch by default"
}

parse_seed() {
    local seed="$1"
    local repo_part=""
    local branch_part=""
    
    # Check if seed contains a colon (branch separator)
    if [[ "$seed" == *":"* ]]; then
        repo_part="${seed%%:*}"
        branch_part="${seed#*:}"
    else
        repo_part="$seed"
        branch_part=""
    fi
    
    # Convert owner/repo to full URL
    echo "https://github.com/$repo_part"
    echo "$branch_part"
}

get_default_repo_url() {
    # Try to get origin URL from local git repo
    if git remote get-url origin >/dev/null 2>&1; then
        git remote get-url origin
    else
        echo "https://github.com/haal-ai/haal-skills"
    fi
}

try_clone_branch() {
    local url="$1"
    local branch="$2"
    local dest="$3"
    
    if git clone --depth 1 --branch "$branch" "$url" "$dest" 2>/dev/null; then
        return 0
    fi
    return 1
}

clean_folder() {
    local path="$1"
    if [[ -d "$path" ]]; then
        rm -rf "$path"
    fi
    mkdir -p "$path"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --seed)
            SEED="${2:-}"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo "Unknown argument: $1" >&2
            show_help >&2
            exit 2
            ;;
    esac
done

# Require git
command -v git >/dev/null 2>&1 || { echo "Required command 'git' not found." >&2; exit 1; }

# Resolve repo URL and branch
if [[ -n "$SEED" ]]; then
    # Parse seed format: owner/repo:branch
    read -r REPO_URL BRANCH <<< "$(parse_seed "$SEED" | tr '\n' ' ')"
else
    REPO_URL="$(get_default_repo_url)"
    BRANCH="main"
fi

echo "=== HAAL Skills Clone ===" >&2
echo "Source: $REPO_URL" >&2
echo "Branch: ${BRANCH:-auto (main/master)}" >&2
echo "" >&2

# Clean and prepare temp folder
clean_folder "$TEMP_CLONE_FOLDER"

# Clone the repository
if [[ -n "$BRANCH" ]]; then
    # Specific branch requested
    echo "Cloning branch '$BRANCH'..." >&2
    if ! git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TEMP_CLONE_FOLDER" 2>&2; then
        echo "Error: Failed to clone branch '$BRANCH' from $REPO_URL" >&2
        exit 1
    fi
else
    # Try main first, then master
    echo "Trying branch 'main'..." >&2
    if try_clone_branch "$REPO_URL" "main" "$TEMP_CLONE_FOLDER"; then
        echo "Cloned 'main' branch" >&2
    else
        echo "Branch 'main' not found, trying 'master'..." >&2
        if try_clone_branch "$REPO_URL" "master" "$TEMP_CLONE_FOLDER"; then
            echo "Cloned 'master' branch" >&2
        else
            echo "Error: Could not clone 'main' or 'master' branch from $REPO_URL" >&2
            exit 1
        fi
    fi
fi

echo "" >&2
echo "Clone complete: $TEMP_CLONE_FOLDER" >&2

# Output the path (this is the only stdout output for piping)
echo "$TEMP_CLONE_FOLDER"
