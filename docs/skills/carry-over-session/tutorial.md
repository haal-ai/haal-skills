# Carry-Over Session: Step-by-Step Tutorial

**How to Execute the "Carry-Over Session" Workflow**

This tutorial shows exactly how to create a carry-over note to resume work in a future session.

## Prerequisites

- OLAF framework installed and active
- `.olaf/carry-over/` directory exists (created automatically if needed)
- Active work session with tasks in progress
- Access to GitHub Copilot Chat or compatible IDE

## Step-by-Step Instructions

### Step 1: Request Carry-Over
Brief: Signal that you want to create a carry-over note

**User Action:**
1. Open GitHub Copilot Chat
2. Type: `carry over`
3. Press Enter

**Alternative commands:**
```
create carry over
carry over note
```

### Step 2: Copilot Analyzes Current Session
**What Copilot Does:**
- Reviews the current conversation and work context
- Identifies the logical next action/prompt
- Determines which files are relevant
- Extracts absolute file paths

**You Should See:** Copilot processing your request

### Step 3: Carry-Over File Generation
**What Copilot Does:**
- Creates timestamp: `YYYYMMDD-HHmm` format
- Generates carry-over file content:
  - Section 1: NEXT PROMPT (exact prompt for next session)
  - Section 2: FILES NEEDED (absolute paths)
  - Section 3: OPTIONAL context (brief summary if critical)
- Saves to `.olaf/carry-over/carry-over-YYYYMMDD-HHmm.txt`

**Example Generated File:**
```text
CARRY-OVER - 2025-11-14 14:30
========================

## NEXT PROMPT
Add JWT validation to AuthService, update login to return token, and add middleware to protect routes.

## FILES NEEDED (Absolute Paths)
c:\users\<user-name>\coderepos\project\src\services\AuthService.ts
c:\users\<user-name>\coderepos\project\src\middleware\auth.ts
c:\users\<user-name>\coderepos\project\src\routes\api.ts
c:\users\<user-name>\coderepos\project\config\jwt.config.ts
c:\users\<user-name>\coderepos\project\tests\auth.test.ts

## OPTIONAL - Brief Context
Working on authentication feature. Login endpoint exists but needs JWT implementation.
```

### Step 4: Confirmation
**Copilot Response:**
```
✓ Carry-over note created: .olaf/carry-over/carry-over-20251114-1430.txt
  Use "carry on" in next session to resume
```

**User Action:** Note the confirmation, end your session

### Step 5: Resume in Future Session (Using Carry-On)
**User Action:**
1. Start new Copilot Chat session
2. Type: `carry on`
3. Press Enter

**What Copilot Does:**
- Finds latest carry-over file
- Loads NEXT PROMPT and FILES NEEDED
- Proposes plan and asks for approval

**Copilot Response:**
```
## Resuming from Carry-Over
- Carry-Over File: carry-over-20251114-1430.txt
- Session Date: 2025-11-14 14:30

### Proposed Plan (from NEXT PROMPT)
Add JWT validation to AuthService, update login to return token, and add middleware to protect routes.

### Files To Open
c:\users\<user-name>\coderepos\project\src\services\AuthService.ts
c:\users\<user-name>\coderepos\project\src\middleware\auth.ts
c:\users\<user-name>\coderepos\project\src\routes\api.ts
c:\users\<user-name>\coderepos\project\config\jwt.config.ts
c:\users\<user-name>\coderepos\project\tests\auth.test.ts

Confirm: Proceed with the proposed plan? (Yes/No)
```

**User Action:** Respond `Yes` to proceed

## Verification Checklist

✅ **Carry-over file created** - Check `.olaf/carry-over/` directory
✅ **Timestamp format correct** - File named `carry-over-YYYYMMDD-HHmm.txt`
✅ **NEXT PROMPT included** - Clear actionable prompt present
✅ **FILES NEEDED listed** - Absolute paths to relevant files
✅ **Resumable in next session** - Can use `carry on` to load

## Troubleshooting

**If carry-over file not created:**
```
Check .olaf/carry-over/ directory exists
Copilot may need write permissions
```

**If files have relative paths instead of absolute:**
- Manually edit the carry-over file
- Convert to absolute paths using workspace root
- Format: `c:\Users\<user>\coderepos\<project>\<path>`

**If NEXT PROMPT is unclear:**
- Manually edit the carry-over file
- Make the prompt more specific and actionable
- Add any critical context

**If resuming doesn't work:**
- Check carry-over file exists and isn't corrupted
- Verify file follows correct template format
- Try `carry on` command again

## Key Learning Points

1. **Minimal but sufficient:** Carry-over notes are intentionally brief. Include only what's needed to resume work immediately.

2. **Absolute paths critical:** File paths must be absolute (full workspace path) so they work across sessions without ambiguity.

3. **NEXT PROMPT is key:** This is the exact prompt you or Copilot will use to continue work. Make it clear and actionable.

4. **Companion workflow:** Carry-over creates the note, `carry on` loads it. They work together as a pair.

5. **Personal workspace:** `.olaf/` directory is typically in `.gitignore`, keeping carry-over notes private.

## Next Steps to Try

- Create a carry-over note and resume it in next session using `carry on`
- Edit a carry-over file manually to refine the NEXT PROMPT
- Create multiple carry-over notes for different tasks (use descriptive timestamps)
- Compare carry-over with stash workflow (stash is for pausing, carry-over is for session continuity)

## Expected Timeline

- **Total carry-over creation time:** 10-30 seconds
- **User input required:** Request carry-over command
- **Copilot execution time:** Instant (file generation)
- **Resume time:** 10-20 seconds in next session with `carry on`
