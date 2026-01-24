#!/usr/bin/env bash
# Haal AI Powers Installation Script for Kiro
# Installs powers from haal-skills repo to ~/.kiro/powers/
# Powers are read from competency manifests (powers array)

set -uo pipefail

SOURCE_PATH="${1:-}"
COMPETENCIES=()
COLLECTION=""
FORCE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --competency) COMPETENCIES+=("${2:-}"); shift 2;;
        --collection) COLLECTION="${2:-}"; shift 2;;
        --force) FORCE="--force"; shift;;
        *) 
            if [[ -z "$SOURCE_PATH" ]]; then
                SOURCE_PATH="$1"
            fi
            shift;;
    esac
done

# Determine source path
if [[ -z "$SOURCE_PATH" ]]; then
    SOURCE_PATH="${HAAL_SKILLS_SOURCE:-$(pwd)}"
fi

# Kiro powers directory
KIRO_POWERS_DIR="$HOME/.kiro/powers"
KIRO_INSTALLED_DIR="$KIRO_POWERS_DIR/installed"
REGISTRY_FILE="$KIRO_POWERS_DIR/registry.json"

# Paths in source repo
POWERS_SOURCE_DIR="$SOURCE_PATH/powers"
COMPETENCIES_DIR="$SOURCE_PATH/competencies"
CONFIG_FILE="$COMPETENCIES_DIR/powers.json"
COLLECTION_MANIFEST="$SOURCE_PATH/collection-manifest.json"

# Colors
info() { echo -e "  \033[0;36m$1\033[0m"; }
success() { echo -e "  \033[0;32m✓ $1\033[0m"; }
warn() { echo -e "  \033[0;33m⚠ $1\033[0m"; }
err() { echo -e "  \033[0;31m✗ $1\033[0m"; }

echo -e "\033[0;36m=== Haal AI Powers Installation ===\033[0m"
echo ""

# Validate paths
if [[ ! -d "$POWERS_SOURCE_DIR" ]]; then
    err "Powers source directory not found: $POWERS_SOURCE_DIR"
    exit 1
fi

if [[ ! -d "$KIRO_POWERS_DIR" ]]; then
    err "Kiro powers directory not found. Please run Kiro at least once."
    exit 1
fi

# Check for jq
if ! command -v jq &> /dev/null; then
    err "jq is required but not installed."
    exit 1
fi

# Load config for registry powers to keep
KEEP_FROM_REGISTRY=()
if [[ -f "$CONFIG_FILE" ]]; then
    while IFS= read -r line; do
        [[ -n "$line" ]] && KEEP_FROM_REGISTRY+=("$line")
    done < <(jq -r '.keep_from_registry[]? // empty' "$CONFIG_FILE" 2>/dev/null)
fi

echo "Keep from registry: ${KEEP_FROM_REGISTRY[*]:-none}"
echo ""

# Get competencies from collection
get_competencies_from_collection() {
    local collection="$1"
    if [[ -f "$COLLECTION_MANIFEST" ]]; then
        jq -r --arg c "$collection" '.[$c][]? // empty' "$COLLECTION_MANIFEST" 2>/dev/null
    fi
}

# Get powers from competency
get_powers_from_competency() {
    local comp="$1"
    local manifest="$COMPETENCIES_DIR/$comp.json"
    if [[ -f "$manifest" ]]; then
        jq -r '.powers[]? // empty' "$manifest" 2>/dev/null
    fi
}

# Get all powers
get_all_powers() {
    for dir in "$POWERS_SOURCE_DIR"/*/; do
        if [[ -f "${dir}POWER.md" ]]; then
            basename "$dir"
        fi
    done
}

# Step 1: Resolve powers from competencies
echo -e "\033[0;36mStep 1: Resolving powers from competencies...\033[0m"
ALL_COMPETENCIES=()

if [[ -n "$COLLECTION" ]]; then
    while IFS= read -r comp; do
        [[ -n "$comp" ]] && ALL_COMPETENCIES+=("$comp")
    done < <(get_competencies_from_collection "$COLLECTION")
    if [[ ${#ALL_COMPETENCIES[@]} -gt 0 ]]; then
        info "Collection '$COLLECTION': ${#ALL_COMPETENCIES[@]} competencies"
    fi
fi

for comp in "${COMPETENCIES[@]}"; do
    ALL_COMPETENCIES+=("$comp")
done

# Dedupe
if [[ ${#ALL_COMPETENCIES[@]} -gt 0 ]]; then
    mapfile -t ALL_COMPETENCIES < <(printf '%s\n' "${ALL_COMPETENCIES[@]}" | sort -u)
fi

POWERS_TO_INSTALL=()
if [[ ${#ALL_COMPETENCIES[@]} -gt 0 ]]; then
    for comp in "${ALL_COMPETENCIES[@]}"; do
        comp_powers=()
        while IFS= read -r power; do
            [[ -n "$power" ]] && comp_powers+=("$power") && POWERS_TO_INSTALL+=("$power")
        done < <(get_powers_from_competency "$comp")
        if [[ ${#comp_powers[@]} -gt 0 ]]; then
            info "Competency '$comp': ${#comp_powers[@]} powers"
        fi
    done
else
    info "No collection/competency specified, installing all powers"
    while IFS= read -r power; do
        [[ -n "$power" ]] && POWERS_TO_INSTALL+=("$power")
    done < <(get_all_powers)
fi

# Dedupe
if [[ ${#POWERS_TO_INSTALL[@]} -gt 0 ]]; then
    mapfile -t POWERS_TO_INSTALL < <(printf '%s\n' "${POWERS_TO_INSTALL[@]}" | sort -u)
fi

echo "  Powers to install: ${#POWERS_TO_INSTALL[@]}"
[[ ${#POWERS_TO_INSTALL[@]} -gt 0 ]] && echo "  ${POWERS_TO_INSTALL[*]}"
echo ""

if [[ ${#POWERS_TO_INSTALL[@]} -eq 0 ]]; then
    warn "No powers found to install"
    exit 0
fi

mkdir -p "$KIRO_INSTALLED_DIR"

# Step 2: Clean registry - remove unwanted registry powers
echo -e "\033[0;36mStep 2: Cleaning registry...\033[0m"

# Build jq filter for powers to keep
KEEP_FILTER=$(printf '"%s",' "${KEEP_FROM_REGISTRY[@]}" | sed 's/,$//')
[[ -z "$KEEP_FILTER" ]] && KEEP_FILTER='""'

jq --argjson keep "[$KEEP_FILTER]" '
  .powers = (.powers | to_entries | map(
    select(
      (.key as $k | $keep | index($k)) or
      (.value.author == "Haal AI") or
      (.value.source.type != "registry")
    )
  ) | from_entries)
' "$REGISTRY_FILE" > "$REGISTRY_FILE.tmp" && mv "$REGISTRY_FILE.tmp" "$REGISTRY_FILE"
echo ""

# Step 3: Install powers
echo -e "\033[0;36mStep 3: Installing Haal AI powers...\033[0m"

for POWER_NAME in "${POWERS_TO_INSTALL[@]}"; do
    POWER_SOURCE_PATH="$POWERS_SOURCE_DIR/$POWER_NAME"
    POWER_MD_FILE="$POWER_SOURCE_PATH/POWER.md"
    
    if [[ ! -f "$POWER_MD_FILE" ]]; then
        warn "Skipping $POWER_NAME - POWER.md not found"
        continue
    fi
    
    # Parse frontmatter
    DESCRIPTION=$(sed -n '/^---$/,/^---$/p' "$POWER_MD_FILE" | grep '^description:' | sed 's/description: *"\?\([^"]*\)"\?/\1/' | head -1)
    DISPLAY_NAME=$(sed -n '/^---$/,/^---$/p' "$POWER_MD_FILE" | grep '^displayName:' | sed 's/displayName: *"\?\([^"]*\)"\?/\1/' | head -1)
    AUTHOR=$(sed -n '/^---$/,/^---$/p' "$POWER_MD_FILE" | grep '^author:' | sed 's/author: *"\?\([^"]*\)"\?/\1/' | head -1)
    KEYWORDS=$(sed -n '/^---$/,/^---$/p' "$POWER_MD_FILE" | grep '^keywords:' | sed 's/keywords: *\[\(.*\)\]/\1/' | tr -d '"' | tr ',' '\n' | sed 's/^ *//' | jq -R . 2>/dev/null | jq -s . 2>/dev/null || echo "[]")
    
    [[ -z "$DISPLAY_NAME" ]] && DISPLAY_NAME="$POWER_NAME"
    [[ -z "$AUTHOR" ]] && AUTHOR="Haal AI"
    [[ -z "$KEYWORDS" || "$KEYWORDS" == "null" ]] && KEYWORDS="[]"
    
    # Copy power
    INSTALL_PATH="$KIRO_INSTALLED_DIR/$POWER_NAME"
    if [[ -d "$INSTALL_PATH" && "$FORCE" != "--force" ]]; then
        info "Already installed: $POWER_NAME (use --force to reinstall)"
    else
        rm -rf "$INSTALL_PATH"
        cp -r "$POWER_SOURCE_PATH" "$INSTALL_PATH"
        success "Installed: $POWER_NAME"
    fi
    
    # Update registry
    REPO_ID="haal-$POWER_NAME"
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%S.000Z")
    
    jq --arg name "$POWER_NAME" \
       --arg desc "$DESCRIPTION" \
       --arg display "$DISPLAY_NAME" \
       --arg author "$AUTHOR" \
       --argjson keywords "$KEYWORDS" \
       --arg installPath "$INSTALL_PATH" \
       --arg sourcePath "$POWER_SOURCE_PATH" \
       --arg repoId "$REPO_ID" \
       --arg timestamp "$TIMESTAMP" '
      .powers[$name] = {
        name: $name, description: $desc, displayName: $display, author: $author,
        keywords: $keywords, installed: true, installedAt: $timestamp,
        installPath: $installPath,
        source: { type: "local", repoId: $repoId, repoName: $sourcePath },
        sourcePath: $sourcePath
      } |
      .repoSources[$repoId] = {
        name: $sourcePath, type: "local", enabled: true,
        addedAt: $timestamp, path: $sourcePath, lastSync: $timestamp, powerCount: 1
      }
    ' "$REGISTRY_FILE" > "$REGISTRY_FILE.tmp" && mv "$REGISTRY_FILE.tmp" "$REGISTRY_FILE"
done
echo ""

# Step 4: Clean orphaned repo sources
echo -e "\033[0;36mStep 4: Cleaning orphaned repo sources...\033[0m"
jq '
  .repoSources = (.repoSources | to_entries | map(
    select(
      (.key | startswith("haal-")) or
      (.key | startswith("clone-")) or
      ((.key | startswith("local-")) | not)
    )
  ) | from_entries)
' "$REGISTRY_FILE" > "$REGISTRY_FILE.tmp" && mv "$REGISTRY_FILE.tmp" "$REGISTRY_FILE"
echo ""

# Step 5: Update timestamp
echo -e "\033[0;36mStep 5: Saving registry...\033[0m"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%S.000Z")
jq --arg ts "$TIMESTAMP" '.lastUpdated = $ts' "$REGISTRY_FILE" > "$REGISTRY_FILE.tmp" && mv "$REGISTRY_FILE.tmp" "$REGISTRY_FILE"
success "Registry updated"
echo ""

# Summary
echo -e "\033[0;32m=== Installation Complete ===\033[0m"
echo -e "\033[0;36mInstalled powers: ${POWERS_TO_INSTALL[*]}\033[0m"
echo -e "\033[0;33mRestart Kiro to see the powers in your registry.\033[0m"
