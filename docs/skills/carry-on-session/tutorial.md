# Carry-On Session: Step-by-Step Tutorial

**How to Execute the "Carry-On Session" Workflow**

This tutorial shows exactly how to resume work from a carry-over note.

## Prerequisites

- OLAF framework installed and active
- At least one carry-over file in `.olaf/carry-over/`
- Previous session where you created a carry-over note
- Access to GitHub Copilot Chat or compatible IDE

## Step-by-Step Instructions

### Step 1: Start New Session and Request Carry-On
Brief: Load the latest carry-over note

**User Action:**
1. Open GitHub Copilot Chat (new session)
2. Type: `carry on`
3. Press Enter

**Alternative commands:**
```
resume work
continue work
```

### Step 2: Copilot Finds Latest Carry-Over
**What Copilot Does:**
- Scans `.olaf/carry-over/` directory
- Finds most recent file matching pattern `carry-over-YYYYMMDD-HHmm.txt`
- Reads and parses the file

**You Should See:** Copilot processing the carry-over file

### Step 3: Carry-Over File Parsed
**What Copilot Does:**
- Extracts **NEXT PROMPT** section (the exact prompt to continue)
- Extracts **FILES NEEDED** section (absolute file paths)
- Extracts **OPTIONAL context** if present

### Step 4: Proposal Presented
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
If No, please specify adjustments.
```

**User Action:** Review the proposed plan

### Step 5: User Approves or Adjusts
**User Action:**
Type your response:
```
Yes
```
or
```
No, let's focus only on AuthService first
```

**Provide Confirmation:**
- `Yes` - Proceed as proposed
- `No` - Specify adjustments needed

### Step 6: Copilot Proceeds (if approved)
**What Copilot Does:**
- Opens/reads the specified files
- Executes the NEXT PROMPT as the working instruction
- Continues with the work described in the carry-over

**You Should See:** Work resuming from where previous session ended

## Verification Checklist

✅ **Latest carry-over loaded** - Correct file by timestamp
✅ **Plan presented** - NEXT PROMPT shown clearly
✅ **Files listed** - All absolute paths displayed
✅ **Approval requested** - Copilot waits before acting
✅ **Work resumed** - Continues from previous session context

## Troubleshooting

**If no carry-over found:**
```
Error: No carry-over files found in .olaf/carry-over/
Create a carry-over note first using "carry over"
```

**If carry-over file corrupted:**
- Check file exists in `.olaf/carry-over/`
- Verify file format matches template
- Ensure NEXT PROMPT section exists

**If wrong carry-over loaded:**
- Carry-on loads MOST RECENT by timestamp
- Check file timestamps in `.olaf/carry-over/`
- Rename or delete unwanted carry-over files

**If files not found:**
- Verify absolute paths in carry-over file are correct
- Update paths if workspace location changed
- Edit carry-over file manually if needed

## Key Learning Points

1. **Proposal first, action second:** Carry-on always proposes the plan and waits for approval. It never auto-executes.

2. **Most recent by timestamp:** The file with the latest YYYYMMDD-HHmm timestamp is selected automatically.

3. **NEXT PROMPT becomes instruction:** The exact prompt from the carry-over becomes the working instruction once approved.

4. **Session continuity:** Carry-over + carry-on workflow enables seamless work across sessions without losing context.

5. **User control:** You can adjust the plan before proceeding - it's not all-or-nothing.

## Next Steps to Try

- Create a carry-over with `carry over`, then resume it with `carry on`
- Try adjusting the proposed plan instead of accepting it as-is
- Create multiple carry-overs and see which one loads (most recent)
- Edit a carry-over file manually before using `carry on`

## Expected Timeline

- **Total carry-on execution time:** 10-30 seconds
- **User input required:** Approval/adjustment of proposed plan
- **Copilot execution time:** Instant for loading, variable for work execution
