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

# Default to current directory if not specified
REPO_PATH="$(pwd)"

# If we're inside .olaf/tools, go up to repo root
if [[ "$REPO_PATH" == */.olaf/tools ]] || [[ "$REPO_PATH" == *\.olaf\tools ]]; then
    REPO_PATH="$(cd "$REPO_PATH/../.." && pwd)"
fi

# Try to find git root
if git_root=$(git -C "$REPO_PATH" rev-parse --show-toplevel 2>/dev/null); then
    REPO_PATH="$git_root"
fi

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
    
    printf "  Fetching %s..." "$repo_spec"
    
    # Remove existing if present
    rm -rf "$clone_path" 2>/dev/null || true
    
    if git clone --depth 1 --branch "$branch" "$repo_url" "$clone_path" >/dev/null 2>&1; then
        echo " OK"
        echo "$clone_path" > "$result_file"
        return 0
    fi
    
    # Try master if main failed
    if [[ "$branch" == "main" ]]; then
        printf " trying master..."
        clone_path="$dest_folder/${repo_name}_master"
        if git clone --depth 1 --branch "master" "$repo_url" "$clone_path" >/dev/null 2>&1; then
            echo " OK"
            echo "$clone_path" > "$result_file"
            return 0
        fi
    fi
    
    echo " SKIP (not available)"
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

echo "=== HAAL Setup ==="
echo "  Installing skills, powers, and tools to your environment"
echo ""

# Determine seed
if [[ -z "$SEED" ]]; then
    SEED="haal-ai/haal-skills:main"
fi

# Clean temp folder
clean_folder "$TEMP_BASE_FOLDER"

# Download packages
echo "Downloading skill packages..."
CLONE_RESULT_FILE=$(mktemp)
seed_path=""
if try_clone_repo "$SEED" "$TEMP_BASE_FOLDER" "$CLONE_RESULT_FILE"; then
    seed_path=$(cat "$CLONE_RESULT_FILE")
fi
rm -f "$CLONE_RESULT_FILE"

if [[ -z "$seed_path" || ! -d "$seed_path" ]]; then
    echo "ERROR: Failed to download: $SEED" >&2
    exit 1
fi

# Read repos manifest from seed
mapfile -t additional_repos < <(read_repos_manifest "$seed_path")

# Clone additional repos
cloned_paths=()
if [[ ${#additional_repos[@]} -gt 0 ]]; then
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
fi

# Add seed path last (so it installs last and wins conflicts)
cloned_paths+=("$seed_path")
echo ""

# Install
echo "Installing..."

install_args=()
install_args+=(--repo-path "$REPO_PATH")
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
done

# Final registry update for all installed powers
powers_script="$seed_path/.olaf/tools/install-powers.sh"
if [[ -f "$powers_script" ]]; then
    chmod +x "$powers_script" 2>/dev/null || true
    "$powers_script" --update-registry || echo "  WARN: Registry update failed"
fi
echo ""

echo "=== Setup Complete ==="
