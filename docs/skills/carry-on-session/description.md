# Carry-On Session - Description

## Overview
Carry-On loads the latest carry-over note file and proposes resuming work from where you left off.

## What It Does
- Finds the most recent carry-over file in `.olaf/carry-over/`
- Parses the file sections (NEXT PROMPT, FILES NEEDED, OPTIONAL context)
- Proposes the plan from the carry-over note
- Waits for user approval before taking action
- Opens/reads required files upon approval

## How It Works
1. **User requests carry-on** with command like "carry on"
2. **Copilot searches** for latest `carry-over-YYYYMMDD-HHmm.txt` file by timestamp
3. **Parses carry-over file**:
   - Extracts NEXT PROMPT section
   - Extracts FILES NEEDED (absolute paths)
   - Extracts OPTIONAL context if present
4. **Proposes plan** to user showing:
   - Carry-over file name and date
   - Proposed plan (from NEXT PROMPT)
   - Files to open (from FILES NEEDED)
5. **Waits for approval** - Does NOT auto-execute
6. **On approval**, proceeds with proposed plan

## Key Files
- **Carry-Over Directory**: `.olaf/carry-over/`
- **File Pattern**: `carry-over-YYYYMMDD-HHmm.txt` (finds most recent)
- **Skill Prompt**: `skills/carry-on-session/prompts/carry-on-session.md`
- **Companion Skill**: `carry-over-session.md` (creates the note)

## Commands
- `carry on` - Load and resume from latest carry-over
- `resume work` - Same as above
- `continue work` - Same as above

## When to Use
- Starting a new session and want to resume previous work
- Need to load context from where you left off
- Have a carry-over note from previous session

## Companion Feature
Use `carry over` to create the carry-over note that this skill loads.

## Protocol
**Act** - Loads carry-over and proposes plan, but waits for approval before executing.
