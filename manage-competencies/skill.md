---
name: manage-competencies
description: Comprehensive competency management skill that handles the full lifecycle of OLAF competencies including creation of new competencies from scratch or existing files, editing existing competencies (structure, files, manifest), safe deletion with dependency checking, and validation of competency structure and integrity.
license: Apache-2.0
metadata:
  olaf_tags: [lifecycle-management, interactive-workflow, competency-operations, crud-operations, framework-administration]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

# Manage Competencies

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read the full ~/reference/.condensed/olaf-framework-condensed.md.

## Context
You are helping manage OLAF competencies through an interactive Python script. This skill provides four core operations: **create**, **edit**, **delete**, and **validate**.

## Input Parameters
- **operation**: string - Operation to perform: "create", "edit", "delete", "validate" (OPTIONAL - will prompt if not provided)
- **competency_name**: string - Target competency name in kebab-case (OPTIONAL - will prompt if needed)
- **pack**: string - Competency pack name (OPTIONAL for create - will prompt)

## User Interaction Protocol
Follow **Propose-Confirm-Act**:
1. **Propose**: Show operation plan before execution2. **Confirm**: Get explicit user approval
3. **Act**: Execute with progress updates

## Process

### 1. Determine Operation

If not provided, ask user:
```
What would you like to do with competencies?
1. Create a new competency2. Edit an existing competency  
3. Delete a competency4. Validate a competency structure

Please specify (1-4):
```

### 2. Run Python Script

Execute the management script based on operation:

```bash
python skills/manage-competencies/scripts/manage_competencies.py --operation {operation} [--name {competency_name}] [--pack {pack}]
```

**Script handles all interactions:**
- Interactive prompts for missing parameters
- File structure creation/modification
- Manifest generation/validation
- Dependency checking
- User confirmations at each step

### 3. Review Output

The script will:
- Display proposed changes before execution
- Request confirmation for destructive operations
- Show progress during execution
- Report completion status and next steps
- Validate all changes

## Operations Overview

### Create
- Interactive structure setup
- File organization from existing files or new
- Manifest generation with proper entry_points
- Documentation template creation
- Dependencies setup (optional)

### Edit
- Select competency to edit
- Choose what to modify (files, manifest, dependencies)
- Update with validation
- Backup before changes

### Delete
- Dependency check (prevent breaking other competencies)
- Confirmation with impact analysis
- Safe removal with optional backup

### Validate
- Structure verification
- Manifest validation (JSON, required fields, entry_points)
- File reference checking
- Dependency validation
- Standards compliance

## Quick Commands

Support direct invocation:
- "create competency [name]"
- "edit competency [name]"
- "delete competency [name]"
- "validate competency [name]"

## Error Handling

The Python script handles:
- Invalid competency names → suggestions
- Missing files → offer to create
- Dependency conflicts → show conflicts
- Permission issues → clear error messages
- Validation failures → specific fix recommendations

## Output

Script provides:
- ✅ Success confirmations
- 📋 Structure summaries
- ⚠️  Warnings and recommendations
- 🔍 Validation reports
- 📝 Next steps guidance
