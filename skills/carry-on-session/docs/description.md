# carry-on-session

## Overview
Loads the latest carry-over note and proposes the immediate next action for seamless session continuation.

## Purpose
Resume work from where you left off by loading a previously saved carry-over note and presenting a clear action plan for approval.

## Key Features
- Automatically finds the most recent carry-over file
- Parses next prompt, files needed, and optional context
- Presents a proposal for user approval before taking action
- Safe operation - no auto-execution without consent

## Usage
```
@carry-on-session
```

## Parameters
| Parameter | Required | Description |
|-----------|----------|-------------|
| None | - | Automatically loads the latest carry-over note |

## Process Flow
1. Searches `.olaf/work/carry-over/` for latest `carry-over-YYYYMMDD-HHmm.txt`
2. Parses NEXT PROMPT, FILES NEEDED, and optional context sections
3. Presents proposal with file paths and recommended action
4. Waits for user confirmation before proceeding

## Output
A formatted proposal showing:
- Carry-over file name and session date
- Proposed plan from NEXT PROMPT
- List of files to open
- Confirmation prompt

## Error Handling
| Scenario | Resolution |
|----------|------------|
| No carry-over files found | Suggests running carry-over-session first |
| Malformed carry-over file | Reports parsing error with file location |

## Related Skills
- `carry-over-session` - Create carry-over notes for later resumption
- `stash-restart-session` - Alternative session management
