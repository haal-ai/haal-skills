#!/usr/bin/env bash
set -uo pipefail

# Multi-repo setup script
# 1. Clone seed repo
# 2. Read repos-manifest.json from seed
# 3. Clone additional repos (skip unavailable)
# 4. Install from bottom to top (seed wins on conflicts)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use Windows-compatible temp path if on Windows (Git Bash)
if [[ -n "${USERPROFILE:-}" ]]; then
    # Windows - use AppData\Local\Temp
    TEMP_BASE_FOLDER="$(cygpath -u "$LOCALAPPDATA")/Temp/haal-skills-repos"
else
    TEMP_BASE_FOLDER="${TMPDIR:-/tmp}/haal-skills-repos"
fi

REPO_PATH=""
SEED=""
COMPETENCIES=()
COLLECTION=""
CLEAN=false
PLATFORM="all"

show_help() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Setup HAAL skills from multiple repos."
    echo ""
    echo "Options:"
    echo "  --repo-path PATH         Target repository path"
    echo "  --seed OWNER/REPO:BRANCH Seed repo (e.g., 'haal-ai/haal-skills:main')"
    echo "  --collection NAME        Collection name to install"
    echo "  --competency NAME        Competency name (can be repeated)"
    echo "  --clean                  Delete existing skills first (default: update only)"
    echo "  --platform PLATFORM      Platform to install to: all, kiro, claude, windsurf, github"
    echo "  -h, --help               Show this help message"
}

clean_folder() {
    local path="$1"
    rm -rf "$path" 2>/dev/null || true
    mkdir -p "$path"
}

try_clone_repo() {
    local repo_spec="$1"
    local dest_folder="$2"
    local result_file="$3"
    
    local repo_url=""
    local branch=""
    
    if [[ "$repo_spec" == *:* ]]; then
        repo_url="https://github.com/${repo_spec%%:*}"
        branch="${repo_spec##*:}"
    else
        repo_url="https://github.com/$repo_spec"
        branch="main"
    fi
    
    local repo_name="${repo_spec%%:*}"
    repo_name="${repo_name//\//_}"
    local branch_safe="${branch//\//_}"
    local clone_path="$dest_folder/${repo_name}_${branch_safe}"
    
    echo "Cloning $repo_spec..."
    echo "  URL: $repo_url"
    echo "  Branch: $branch"
    
    # Remove existing if present
    rm -rf "$clone_path" 2>/dev/null || true
    
    if git clone --depth 1 --branch "$branch" "$repo_url" "$clone_path" >/dev/null 2>&1; then
        echo "  OK: ${repo_name}:${branch}"
        echo "$clone_path" > "$result_file"
        return 0
    fi
    
    # Try master if main failed
    if [[ "$branch" == "main" ]]; then
        echo "  Trying master branch..."
        clone_path="$dest_folder/${repo_name}_master"
        if git clone --depth 1 --branch "master" "$repo_url" "$clone_path" >/dev/null 2>&1; then
            echo "  OK: ${repo_name}:master"
            echo "$clone_path" > "$result_file"
            return 0
        fi
    fi
    
    echo "  SKIP: $repo_spec (not available)"
    return 1
}

read_repos_manifest() {
    local clone_path="$1"
    local manifest_path="$clone_path/repos-manifest.json"
    
    if [[ ! -f "$manifest_path" ]]; then
        return
    fi
    
    if command -v jq &>/dev/null; then
        jq -r '.repos[]?' "$manifest_path" 2>/dev/null | tr -d '\r' || true
        return
    fi

    # Bash-only fallback for simple JSON: {"repos": ["a","b", ...]}
    local compact
    compact=$(tr -d '\n\r\t ' < "$manifest_path" 2>/dev/null || true)
    [[ -z "$compact" ]] && return

    local array_contents
    array_contents=$(printf '%s' "$compact" | sed -n 's/.*"repos":\[\([^]]*\)\].*/\1/p' | head -n 1)
    [[ -z "$array_contents" ]] && return

    printf '%s\n' "$array_contents" | tr ',' '\n' | sed -n 's/^"\(.*\)"$/\1/p' | tr -d '\r' || true
}

install_from_clone() {
    local clone_path="$1"
    local clean_mode="$2"
    local platform_mode="$3"
    shift 3
    local install_args=("$@")
    
    local install_script="$clone_path/.olaf/tools/install-haal-skills.sh"
    
    if [[ ! -f "$install_script" ]]; then
        echo "  SKIP: No install script in $clone_path"
        return
    fi
    
    chmod +x "$install_script" 2>/dev/null || true
    
    local args=(--clone-path "$clone_path")
    [[ "$clean_mode" == "true" ]] && args+=(--clean)
    [[ -n "$platform_mode" ]] && args+=(--platform "$platform_mode")
    args+=("${install_args[@]}")
    
    "$install_script" "${args[@]}" || {
        echo "  WARN: Install had errors for $clone_path - continuing"
    }
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --repo-path)
            REPO_PATH="${2:-}"; shift 2;;
        --seed)
            SEED="${2:-}"; shift 2;;
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

# === Main ===

echo "=== HAAL Skills Multi-Repo Setup ==="
echo ""

# Determine seed
# If not specified, always use the canonical haal-ai/haal-skills repo.
# Note: try_clone_repo automatically falls back to master when main is unavailable.
if [[ -z "$SEED" ]]; then
    SEED="haal-ai/haal-skills:main"
fi

echo "Seed: $SEED"
echo ""

# Clean temp folder
clean_folder "$TEMP_BASE_FOLDER"

# Step 1: Clone seed repo
echo "Step 1: Cloning seed repo..."
CLONE_RESULT_FILE=$(mktemp)
seed_path=""
if try_clone_repo "$SEED" "$TEMP_BASE_FOLDER" "$CLONE_RESULT_FILE"; then
    seed_path=$(cat "$CLONE_RESULT_FILE")
fi
rm -f "$CLONE_RESULT_FILE"

if [[ -z "$seed_path" || ! -d "$seed_path" ]]; then
    echo "ERROR: Failed to clone seed repo: $SEED" >&2
    exit 1
fi
echo ""

# Step 2: Read repos manifest from seed
echo "Step 2: Reading repos manifest..."
mapfile -t additional_repos < <(read_repos_manifest "$seed_path")
echo "  Found ${#additional_repos[@]} additional repo(s)"
echo ""

# Step 3: Clone additional repos
cloned_paths=()
if [[ ${#additional_repos[@]} -gt 0 ]]; then
    echo "Step 3: Cloning additional repos..."
    for repo in "${additional_repos[@]}"; do
        if [[ -n "$repo" ]]; then
            CLONE_RESULT_FILE=$(mktemp)
            if try_clone_repo "$repo" "$TEMP_BASE_FOLDER" "$CLONE_RESULT_FILE"; then
                path=$(cat "$CLONE_RESULT_FILE")
                if [[ -n "$path" && -d "$path" ]]; then
                    cloned_paths+=("$path")
                fi
            fi
            rm -f "$CLONE_RESULT_FILE"
        fi
    done
    echo ""
fi

# Add seed path last (so it installs last and wins conflicts)
cloned_paths+=("$seed_path")

# Step 4: Install from bottom to top
echo "Step 4: Installing skills (bottom to top)..."
echo "  Order: ${cloned_paths[*]}"
echo ""

install_args=()
if [[ -n "$REPO_PATH" ]]; then
    install_args+=(--repo-path "$REPO_PATH")
fi
if [[ -n "$COLLECTION" ]]; then
    install_args+=(--collection "$COLLECTION")
fi
for comp in "${COMPETENCIES[@]}"; do
    install_args+=(--competency "$comp")
done

first_clone=true
for clone_path in "${cloned_paths[@]}"; do
    repo_name=$(basename "$clone_path")
    echo "Installing from: $repo_name"
    # Only first install can clean (if --clean), subsequent ones never clean
    if [[ "$first_clone" == "true" && "$CLEAN" == "true" ]]; then
        install_from_clone "$clone_path" "true" "$PLATFORM" "${install_args[@]}"
    else
        install_from_clone "$clone_path" "false" "$PLATFORM" "${install_args[@]}"
    fi
    first_clone=false
    echo ""
done

echo "=== Done ==="
