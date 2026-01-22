# carry-over-session

## Overview

Creates a simple carry-over note with the next prompt and files needed for seamless session continuation.

## Purpose

When you need to pause work and resume later, this skill captures the essential context: what to do next and which files to reference. It eliminates the friction of remembering where you left off.

## Key Features

- Generates actionable next-session prompts
- Lists all relevant files with absolute paths
- Saves timestamped carry-over notes for easy retrieval
- Minimal format focused on immediate resumption

## Usage

Invoke the skill when ending a work session:
```
@carry-over-session
```

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| None | - | The skill analyzes the current conversation context automatically |

## Process Flow

1. Analyzes the current conversation and work state
2. Formulates a clear, actionable prompt for the next session
3. Identifies all files relevant to continuing the work
4. Saves the carry-over note to `.olaf/work/carry-over/carry-over-YYYYMMDD-HHmm.txt`

## Output

A timestamped text file containing:
- **Next Prompt**: Exact prompt to resume work
- **Files Needed**: Absolute paths to all relevant files
- **Optional Context**: Brief state summary if critical

## Examples

**Use Case**: Ending a session while implementing authentication
```text
CARRY-OVER - 2025-11-14 14:30
========================

## NEXT PROMPT
Add JWT validation to AuthService, update login to return token, and add middleware to protect routes.

## FILES NEEDED (Absolute Paths)
c:\Users\user\project\src\services\AuthService.ts
c:\Users\user\project\src\middleware\auth.ts
c:\Users\user\project\src\routes\api.ts
```

## Error Handling

| Scenario | Resolution |
|----------|------------|
| No clear next steps | Skill prompts for clarification on work direction |
| Missing file context | Reviews conversation history for file references |

## Related Skills

- `carry-on-session` - Resume work using a carry-over note
- `stash-restart-session` - Alternative session management approach
