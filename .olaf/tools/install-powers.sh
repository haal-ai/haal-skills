#!/usr/bin/env bash
# Haal AI Powers Installation Script for Kiro
# Copies powers to ~/.kiro/powers/installed/ and updates registry.json

set -uo pipefail

SOURCE_PATH=""
COMPETENCIES=()
COLLECTION=""
FORCE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --competency) COMPETENCIES+=("${2:-}"); shift 2;;
        --collection) COLLECTION="${2:-}"; shift 2;;
        --force) FORCE="true"; shift;;
        *) 
            if [[ -z "$SOURCE_PATH" ]]; then
                SOURCE_PATH="$1"
            fi
            shift;;
    esac
done

# Determine source path
if [[ -z "$SOURCE_PATH" ]]; then
    SOURCE_PATH="$(pwd)"
fi
SOURCE_PATH="$(cd "$SOURCE_PATH" && pwd)"

# Kiro powers directory
KIRO_POWERS_DIR="$HOME/.kiro/powers"
KIRO_INSTALLED_DIR="$KIRO_POWERS_DIR/installed"
REGISTRY_FILE="$KIRO_POWERS_DIR/registry.json"

# Paths in source repo
POWERS_SOURCE_DIR="$SOURCE_PATH/powers"
COMPETENCIES_DIR="$SOURCE_PATH/competencies"
COLLECTION_MANIFEST="$SOURCE_PATH/collection-manifest.json"

# Check for jq
if ! command -v jq &> /dev/null; then
    echo "    ERROR: jq is required but not installed."
    exit 1
fi

# Validate paths
if [[ ! -d "$POWERS_SOURCE_DIR" ]]; then
    echo "    ERROR: Powers source not found: $POWERS_SOURCE_DIR"
    exit 1
fi

# Get powers from competency
get_powers_from_competency() {
    local comp="$1"
    local manifest="$COMPETENCIES_DIR/$comp.json"
    if [[ -f "$manifest" ]]; then
        jq -r '.powers[]? // empty' "$manifest" 2>/dev/null
    fi
}

# Get competencies from collection
get_competencies_from_collection() {
    local collection="$1"
    if [[ -f "$COLLECTION_MANIFEST" ]]; then
        jq -r --arg c "$collection" '.[$c][]? // empty' "$COLLECTION_MANIFEST" 2>/dev/null
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

# Parse POWER.md frontmatter
parse_power_md() {
    local power_path="$1"
    local power_md="$power_path/POWER.md"
    
    if [[ ! -f "$power_md" ]]; then
        return 1
    fi
    
    # Extract frontmatter values
    local content
    content=$(sed -n '/^---$/,/^---$/p' "$power_md" | tail -n +2 | head -n -1)
    
    NAME=$(echo "$content" | grep '^name:' | sed 's/name: *"\?\([^"]*\)"\?/\1/' | head -1)
    DISPLAY_NAME=$(echo "$content" | grep '^displayName:' | sed 's/displayName: *"\?\([^"]*\)"\?/\1/' | head -1)
    DESCRIPTION=$(echo "$content" | grep '^description:' | sed 's/description: *"\?\([^"]*\)"\?/\1/' | head -1)
    AUTHOR=$(echo "$content" | grep '^author:' | sed 's/author: *"\?\([^"]*\)"\?/\1/' | head -1)
    
    # Parse keywords array
    KEYWORDS=$(echo "$content" | grep '^keywords:' | sed 's/keywords: *\[\(.*\)\]/\1/' | tr -d '"' | tr -d "'" | tr ',' '\n' | sed 's/^ *//' | sed 's/ *$//' | grep -v '^$' | jq -R . 2>/dev/null | jq -s . 2>/dev/null || echo "[]")
    
    [[ -z "$KEYWORDS" || "$KEYWORDS" == "null" ]] && KEYWORDS="[]"
}

# Resolve powers to install
ALL_COMPETENCIES=()

if [[ -n "$COLLECTION" ]]; then
    while IFS= read -r comp; do
        [[ -n "$comp" ]] && ALL_COMPETENCIES+=("$comp")
    done < <(get_competencies_from_collection "$COLLECTION")
fi

for comp in "${COMPETENCIES[@]}"; do
    ALL_COMPETENCIES+=("$comp")
done

# Dedupe competencies
if [[ ${#ALL_COMPETENCIES[@]} -gt 0 ]]; then
    mapfile -t ALL_COMPETENCIES < <(printf '%s\n' "${ALL_COMPETENCIES[@]}" | sort -u)
fi

POWERS_TO_INSTALL=()
if [[ ${#ALL_COMPETENCIES[@]} -gt 0 ]]; then
    for comp in "${ALL_COMPETENCIES[@]}"; do
        while IFS= read -r power; do
            [[ -n "$power" ]] && POWERS_TO_INSTALL+=("$power")
        done < <(get_powers_from_competency "$comp")
    done
else
    while IFS= read -r power; do
        [[ -n "$power" ]] && POWERS_TO_INSTALL+=("$power")
    done < <(get_all_powers)
fi

# Dedupe powers
if [[ ${#POWERS_TO_INSTALL[@]} -gt 0 ]]; then
    mapfile -t POWERS_TO_INSTALL < <(printf '%s\n' "${POWERS_TO_INSTALL[@]}" | sort -u)
fi

if [[ ${#POWERS_TO_INSTALL[@]} -eq 0 ]]; then
    echo "    No powers to install"
    exit 0
fi

# Check registry exists
if [[ ! -f "$REGISTRY_FILE" ]]; then
    echo "    WARN: No Kiro registry found. Open Kiro Powers panel first."
    exit 0
fi

# Create installed directory
mkdir -p "$KIRO_INSTALLED_DIR"

# Copy powers and collect metadata
COPIED=0
SKIPPED=0
INSTALLED_POWERS=()
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%S.%3NZ")
REPO_ID="haal-ai-powers"

for POWER_NAME in "${POWERS_TO_INSTALL[@]}"; do
    POWER_SOURCE="$POWERS_SOURCE_DIR/$POWER_NAME"
    POWER_DEST="$KIRO_INSTALLED_DIR/$POWER_NAME"
    
    if [[ ! -f "$POWER_SOURCE/POWER.md" ]]; then
        continue
    fi
    
    if [[ -d "$POWER_DEST" && "$FORCE" != "true" ]]; then
        ((SKIPPED++))
        INSTALLED_POWERS+=("$POWER_NAME")
    else
        rm -rf "$POWER_DEST"
        cp -r "$POWER_SOURCE" "$POWER_DEST"
        ((COPIED++))
        INSTALLED_POWERS+=("$POWER_NAME")
    fi
done

# Update registry with all powers at once
if [[ ${#INSTALLED_POWERS[@]} -gt 0 ]]; then
    # Build powers JSON
    POWERS_JSON="{"
    FIRST=true
    
    for POWER_NAME in "${INSTALLED_POWERS[@]}"; do
        POWER_PATH="$KIRO_INSTALLED_DIR/$POWER_NAME"
        
        # Parse metadata
        NAME=""
        DISPLAY_NAME=""
        DESCRIPTION=""
        AUTHOR=""
        KEYWORDS="[]"
        parse_power_md "$POWER_PATH"
        
        [[ -z "$NAME" ]] && NAME="$POWER_NAME"
        [[ -z "$DISPLAY_NAME" ]] && DISPLAY_NAME="$POWER_NAME"
        [[ -z "$AUTHOR" ]] && AUTHOR="Haal AI"
        
        if [[ "$FIRST" != "true" ]]; then
            POWERS_JSON+=","
        fi
        FIRST=false
        
        # Escape strings for JSON
        DESCRIPTION_ESC=$(echo "$DESCRIPTION" | jq -Rs . | sed 's/^"//;s/"$//')
        
        POWERS_JSON+="\"$POWER_NAME\":{\"name\":\"$NAME\",\"description\":\"$DESCRIPTION_ESC\",\"displayName\":\"$DISPLAY_NAME\",\"author\":\"$AUTHOR\",\"keywords\":$KEYWORDS,\"installed\":true,\"installedAt\":\"$TIMESTAMP\",\"installPath\":\"$POWER_PATH\",\"source\":{\"type\":\"repo\",\"repoId\":\"$REPO_ID\",\"repoName\":\"Haal AI Powers\"},\"sourcePath\":\"$POWER_PATH\"}"
    done
    
    POWERS_JSON+="}"
    
    # Update registry using jq
    jq --argjson newPowers "$POWERS_JSON" \
       --arg repoId "$REPO_ID" \
       --arg installDir "$KIRO_INSTALLED_DIR" \
       --arg timestamp "$TIMESTAMP" \
       --arg powerCount "${#INSTALLED_POWERS[@]}" '
      # Merge new powers into existing
      .powers = (.powers + $newPowers) |
      # Add/update repo source
      .repoSources[$repoId] = {
        name: "Haal AI Powers",
        type: "local",
        enabled: true,
        addedAt: $timestamp,
        path: $installDir,
        lastSync: $timestamp,
        powerCount: ($powerCount | tonumber)
      } |
      .lastUpdated = $timestamp
    ' "$REGISTRY_FILE" > "$REGISTRY_FILE.tmp" && mv "$REGISTRY_FILE.tmp" "$REGISTRY_FILE"
fi

echo "    Powers: $COPIED copied, $SKIPPED existing (registry updated)"
