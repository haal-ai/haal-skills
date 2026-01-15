# Structural Folder Reorganization & Kernel Skills Renaming

## Overview
Major architectural reorganization to improve clarity and consistency in the OLAF framework structure.

## Changes Made

### 1. Directory Structure Reorganization
```
OLD: .olaf/olaf-core/
NEW: .olaf/core/
```

**Rationale**: Eliminates redundant "olaf-" prefix in the path structure, improving readability and reducing cognitive load.

### 2. Kernel Skills Terminology Update ✅ COMPLETED
- **use-competency** → **use-skill**: Intelligent skill discovery and execution router (MIGRATED)
- **list-competencies** → **list-skills**: Display available skills and protocols (MIGRATED)
- **olaf-help-me**: Updated to use skills-based architecture (`[id:skills_dir]` instead of `[id:competencies_dir]`) (UPDATED)

**Rationale**: Aligns naming with the new skills-based architecture being adopted framework-wide.

## Breaking Changes

### Installer Compatibility
The structural changes break existing installer functionality that relies on hardcoded paths:
- Old paths: `.olaf/olaf-core/skills/`, `.olaf/olaf-core/competencies/`
- New paths: `.olaf/core/skills/`, `.olaf/core/competencies/`

### Required Installer Updates
1. Update path resolution logic to use new `.olaf/core/` structure
2. Update skill discovery to look for renamed kernel skills
3. Update framework file references in installation scripts
4. Test installer with both fresh installs and upgrades

## Migration Impact

### Framework Files Updated
- `.olaf/core/competencies/common/competency-manifest.json`: Updated skill references
- `.olaf/core/reference/query-competency-index.md`: Updated aliases and paths
- `.olaf/core/reference/memory-map.md`: Updated directory structure mapping
- `.olaf/core/reference/.condensed/olaf-framework-condensed.md`: Updated with skills terminology

### User Impact
- Existing users will need to reinstall or update their OLAF installation
- Custom scripts referencing old paths will need updates
- No functional changes to end-user workflows once updated

## Implementation Status
- ✅ Directory structure reorganized
- ✅ Kernel skills renamed and updated
- ✅ Framework files updated
- ✅ Git commits completed
- ⏳ Installer updates required (pending)

## Next Steps
1. Update installer to support new directory structure
2. Create migration script for existing installations
3. Update documentation to reflect new paths
4. Test installation process end-to-end