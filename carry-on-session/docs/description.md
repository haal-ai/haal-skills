# Carry On Session

## Overview
The `carry-on-session` skill resumes work by loading the most recent carry-over note and proposing the immediate next action. It always waits for user approval before doing anything.

## Purpose
Use this skill to continue a prior session safely and quickly by:
- locating the latest carry-over file
- extracting the intended “NEXT PROMPT”
- showing which files should be opened
- asking you to confirm before any work begins

## Key Features
- **Safe by design**: never modifies files until you approve
- **Automatic carry-over selection**: picks the most recent `carry-over-YYYYMMDD-HHmm.txt`
- **Structured parsing**: reads `NEXT PROMPT`, optional `FILES NEEDED`, optional context
- **Clear proposal**: outputs a consistent “Resuming from Carry-Over” block you can accept or adjust

## Usage

### Invocation
Invoke the skill by asking for `carry-on-session` in your chat/assistant environment.

### Expected Input
You typically provide no parameters. The skill finds the latest carry-over note automatically.

## Parameters

### Required Parameters
None.

### Optional Parameters
None.

## Process Flow

1. **Read required team protocol**: reads `.olaf/team-delegation.md`.
2. **Locate latest carry-over note**: searches `.olaf/work/carry-over/` for `carry-over-YYYYMMDD-HHmm.txt` and selects the newest by timestamp.
3. **Parse the note**:
   - `## NEXT PROMPT` (required)
   - `## FILES NEEDED` (optional)
   - `## OPTIONAL - Brief Context` (optional)
4. **Propose next action**: prints the proposal and asks for confirmation.
5. **Wait**: takes no action unless you approve.

## Output
The skill responds with a proposal that follows this structure:

```text
## Resuming from Carry-Over
- Carry-Over File: [filename]
- Session Date: [YYYY-MM-DD HH:mm]

### Proposed Plan (from NEXT PROMPT)
[Paste NEXT PROMPT verbatim]

### Files To Open
[List each absolute path from FILES NEEDED]

Confirm: Proceed with the proposed plan? (Yes/No)
If No, please specify adjustments.
```

## Examples

### Example: Resume the latest work
1. Ask the assistant to run `carry-on-session`.
2. Review the proposed plan and file list.
3. Reply **Yes** to proceed or reply **No** with adjustments.

## Error Handling

### No carry-over found
- **Cause**: `.olaf/work/carry-over/` has no matching files.
- **Fix**: run `carry-over-session` (or otherwise create a carry-over note) and try again.

### Missing `NEXT PROMPT`
- **Cause**: the carry-over note is missing the required section.
- **Fix**: add a `## NEXT PROMPT` section and re-run.

## Related Skills
- **carry-over-session**: creates carry-over notes that this skill can resume
