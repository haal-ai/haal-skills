# Carry-Over Session - Description

## Overview
Carry-Over creates a simple note file to resume work in a future session with minimal context and maximum clarity.

## What It Does
- Creates a carry-over note file in `.olaf/carry-over/`
- Captures the exact next prompt to use
- Lists absolute file paths needed
- Optionally includes brief context (1-2 lines)
- Names file with timestamp: `carry-over-YYYYMMDD-HHmm.txt`

## How It Works
1. **User requests carry-over** with command like "carry over"
2. **Copilot analyzes current session** to determine next action
3. **Generates carry-over file** with:
   - **NEXT PROMPT**: Exact prompt to continue work
   - **FILES NEEDED**: Absolute paths to files
   - **OPTIONAL context**: Brief 1-2 line summary if critical
4. **Saves file** to `.olaf/carry-over/` directory

## File Structure
```
CARRY-OVER - 2025-11-14 14:30
========================

## NEXT PROMPT
<Exact prompt for next session>

## FILES NEEDED (Absolute Paths)
<Full paths to files>

## OPTIONAL - Brief Context
<1-2 lines if needed>
```

## Key Files
- **Carry-Over Directory**: `.olaf/carry-over/`
- **File Pattern**: `carry-over-YYYYMMDD-HHmm.txt`
- **Skill Prompt**: `skills/carry-over-session/carry-over-session.md`
- **Companion Skill**: `carry-on-session.md` (to resume)

## Commands
- `carry over` - Create carry-over note for current session
- `create carry over` - Same as above
- `carry over note` - Same as above

## When to Use
- Ending work session but want to resume later
- Switching to different task temporarily
- Need to remember exact next action
- Want to preserve file context between sessions

## Companion Feature
Use `carry on` in next session to load and resume from the carry-over note.
