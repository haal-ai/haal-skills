# create-changelog-entry

## Overview
Adds entries to functional or technical product changelogs with linked detail files.

## Purpose
Maintain organized changelogs with proper date sections and linked detail files for comprehensive change documentation.

## Key Features
- Supports Functional and Technical changelog types
- Auto-generates date sections (YYYY-MM, YYYY-MM-DD)
- Creates linked detail files for additional context
- Maintains reverse chronological order
- Preserves existing changelog structure

## Usage
```
@create-changelog-entry
```

## Parameters
| Parameter | Required | Description |
|-----------|----------|-------------|
| changelog_type | Yes | Functional or Technical |
| entry_type | Yes | Feature, Enhancement, Fix, etc. |
| entry_description | Yes | Concise change description |
| additional_context | Yes | Detailed info for linked file |
| subject_name | No | Kebab-case name (auto-generated) |

## Process Flow
1. Validates changelog type and entry type
2. Retrieves current date
3. Shows proposed file paths for confirmation
4. Inserts entry at top of date section
5. Creates detail file with context
6. Generates clickable markdown link

## Output
- Entry in: `.olaf/data/product/changelog-[type].md`
- Detail file: `.olaf/data/product/[type]/[subject].md`
- Format: `- [entry_type]: [description] [Details](link)`

## Error Handling
| Scenario | Resolution |
|----------|------------|
| Invalid changelog type | Re-requests with valid options |
| Date command failure | Provides fallback method |
| Malformed changelog | Attempts repair or requests intervention |

## Related Skills
- `analyze-changelog-and-report` - Analyze changelog content
- `archive-changelog-entries` - Archive old entries
