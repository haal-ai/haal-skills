---
name: archive-changelog-entries
description: Archive changelog entries older than a specified number of days to maintain a clean and organized changelog register.
license: Apache-2.0
metadata:
  olaf_tags: [changelog, archive, maintenance, automation]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.
This process is fully automated using the Python script at `tools/archive_changelog_entries.py`. The script will:
1. Archive entries older than the specified number of days
2. Maintain chronological order and formatting
3. Add a maintenance entry to the changelog
4. Provide execution summary

## Output/Result Format

The script will produce:
- Updated changelog with recent entries
- Archive file containing older entries
- Maintenance entry in the changelog
- Execution summary in the terminal

## Output to USER
1. **Execution Summary**:
   - Number of entries archived
   - Number of entries remaining
   - Archive file location
   - Any warnings or errors
2. **Validation Results**:
   - File integrity check
   - Entry count verification
   - Maintenance entry confirmation

## Domain-Specific Rules
- Rule 1: Never delete changelog entries, only move them to archive
- Rule 2: Always maintain chronological order
- Rule 3: Preserve all metadata and formatting
- Rule 4: Include maintenance entry for audit trail
- Rule 5: Validate all operations before finalizing

## Required Actions
1. Verify file paths and permissions
2. Execute archival process
3. Add maintenance entry
4. Validate results
5. Report outcomes

## Python Execution

```python

import subprocess

changelog_path = ".olaf/data/projects/changelog-register.md"

archive_path = ".olaf/data/projects/changelog-archive.md"

days_to_keep = 7  # Default value, can be overridden

subprocess.run([

    "python", "tools/archive_changelog_entries.py",

    changelog_path,

    archive_path,

    "--days-to-keep", str(days_to_keep)

], check=True)

```

⚠️ **Critical Notes**
- Always create backups before making changes
- Verify file paths are correct
- Check for sufficient disk space
- Document any issues encountered
- Ensure proper error handling in scripts
