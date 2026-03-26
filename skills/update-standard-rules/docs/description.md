# update-standard-rules

## Overview
Update, add, or deprecate standards and rules based on conversation context. Detects patterns, conventions, and workflow changes proactively.

## Purpose
Maintain existing coding standards by updating rules when conventions evolve, adding new rules from observed patterns, or deprecating outdated ones. Triggers both explicitly ("update standard") and proactively ("we always do X").

## Key Features
- Three actions: update, add, deprecate
- Proactive detection from conversation patterns
- Language-aware using reference files
- Evidence-based changes (conversation context or code)
- Backup before modifications
- User approval required for all changes
- Local-only mode (no cloud dependency)

## Usage
Invoke this skill by saying:
- "Update the error handling standard"
- "Add a rule about async error boundaries"
- "Deprecate the old naming convention rule"
- "We always wrap errors with context" (proactive trigger)

## Parameters

### Required
- **intent**: What to update/add/deprecate (from conversation context)

### Optional
- **standard_name**: Specific standard to modify
- **scope**: Files the change applies to

## Process Flow
1. **Understand Request** — Evaluate user intent (STOP gate — no analysis before this)
2. **Detect Stack** — Identify project languages and architecture
3. **Analyze Existing Practices** — Read current standards against reference files
4. **Produce Change Report** — Numbered list of proposed changes
5. **User Approval** — Get confirmation for each change
6. **Apply Changes** — Update files with backup
7. **Summary** — Report what was changed

## Output
- Updated standard files in `.olaf/data/practices/standards/`
- Backup of previous versions
- Change summary report

## Related Skills
- **create-standard**: Create new standards from scratch
- **init-standard-rules**: Initialize standards from codebase
- **onboard-local**: Generate standards from project analysis
