#!/usr/bin/env bash
set -euo pipefail

# Wrapper script for backward compatibility
# Calls clone-haal-skills.sh and install-haal-skills.sh in sequence

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

REPO_PATH=""
SEED=""
COMPETENCIES=()
COLLECTION=""

# Legacy parameters (converted to new format)
SKILLS_REPO_URL=""
SKILLS_BRANCH=""

show_help() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Setup HAAL skills (wrapper for clone + install)."
    echo ""
    echo "Options:"
    echo "  --repo-path PATH         Target repository path"
    echo "  --seed OWNER/REPO:BRANCH Override source repo (e.g., 'haal-ai/haal-skills:main')"
    echo "  --skills-repo-url URL    Skills repository URL (legacy, prefer --seed)"
    echo "  --skills-branch BRANCH   Branch to clone (legacy, prefer --seed)"
    echo "  --collection NAME        Collection name to install"
    echo "  --competency NAME,NAME   Competency names (comma-separated)"
    echo "  -h, --help               Show this help message"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --repo-path)
            REPO_PATH="${2:-}"; shift 2;;
        --seed)
            SEED="${2:-}"; shift 2;;
        --skills-repo-url)
            SKILLS_REPO_URL="${2:-}"; shift 2;;
        --skills-branch)
            SKILLS_BRANCH="${2:-}"; shift 2;;
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

# Build seed from legacy parameters if not provided
if [[ -z "$SEED" && -n "$SKILLS_REPO_URL" ]]; then
    # Extract owner/repo from URL
    repo_part=$(echo "$SKILLS_REPO_URL" | sed -E 's|https?://github\.com/||' | sed 's|\.git$||')
    if [[ -n "$SKILLS_BRANCH" ]]; then
        SEED="$repo_part:$SKILLS_BRANCH"
    else
        SEED="$repo_part"
    fi
fi

# Build clone arguments
CLONE_ARGS=()
if [[ -n "$SEED" ]]; then
    CLONE_ARGS+=(--seed "$SEED")
fi

# Build install arguments
INSTALL_ARGS=()
if [[ -n "$REPO_PATH" ]]; then
    INSTALL_ARGS+=(--repo-path "$REPO_PATH")
fi
if [[ -n "$COLLECTION" ]]; then
    INSTALL_ARGS+=(--collection "$COLLECTION")
fi
for comp in "${COMPETENCIES[@]}"; do
    INSTALL_ARGS+=(--competency "$comp")
done

# Step 1: Clone
echo "=== Running clone-haal-skills.sh ===" 
CLONE_PATH=$("$SCRIPT_DIR/clone-haal-skills.sh" "${CLONE_ARGS[@]}")

# Step 2: Install
echo ""
echo "=== Running install-haal-skills.sh ==="
"$SCRIPT_DIR/install-haal-skills.sh" --clone-path "$CLONE_PATH" "${INSTALL_ARGS[@]}"
