# Carry On Session: Step-by-Step Tutorial

**How to Execute the "Carry On Session"**

This tutorial shows exactly how to resume work using the most recent carry-over note.

## Prerequisites

- A carry-over note exists in `.olaf/work/carry-over/`
- The carry-over note follows the expected format and contains `## NEXT PROMPT`

## Step-by-Step Instructions

### Step 1: Run the carry-on skill
This step triggers the assistant to locate and parse the latest carry-over note.

**User Action:**
1. Open your assistant/chat.
2. Ask to run: `carry-on-session`

**Assistant Response:**
The assistant starts searching for the latest carry-over file in `.olaf/work/carry-over/`.

### Step 2: The assistant selects the latest carry-over note

**What the assistant does:**
- Finds files matching `carry-over-YYYYMMDD-HHmm.txt`
- Selects the newest one based on its timestamp

**You should see:**
The assistant referencing the selected carry-over filename.

### Step 3: The assistant parses the carry-over note

**What the assistant does:**
- Extracts `## NEXT PROMPT` (required)
- Extracts `## FILES NEEDED` (optional)
- Extracts `## OPTIONAL - Brief Context` (optional)

**You should see:**
A proposed plan and (optionally) a list of files to open.

### Step 4: Review the proposal and confirm

**Assistant Response:**
```text
## Resuming from Carry-Over
- Carry-Over File: carry-over-20260116-1045.txt
- Session Date: 2026-01-16 10:45

### Proposed Plan (from NEXT PROMPT)
[Paste NEXT PROMPT verbatim]

### Files To Open
[List each absolute path from FILES NEEDED]

Confirm: Proceed with the proposed plan? (Yes/No)
If No, please specify adjustments.
```

**User Action:**
Reply with one of:
- `Yes`
- `No, please do X instead`

## Verification Checklist

✅ Latest carry-over file selected from `.olaf/work/carry-over/`
✅ `NEXT PROMPT` is shown verbatim
✅ Confirmation requested before any action

## Troubleshooting

**If no carry-over files are found:**
- Create one first (for example using `carry-over-session`), then rerun `carry-on-session`.

**If `NEXT PROMPT` is missing:**
- Edit the carry-over note to include a `## NEXT PROMPT` section.

**If file paths in `FILES NEEDED` are invalid:**
- Update the paths in the carry-over note to match the current workspace layout.

## Key Learning Points

1. **Safety first:** this skill always asks before doing anything.
2. **Most recent wins:** the newest timestamped carry-over file is selected.
3. **Carry-over notes drive execution:** `NEXT PROMPT` becomes the next working instruction after you approve.

## Next Steps to Try

- Create a new carry-over note, then run `carry-on-session` to resume it.
- Test the “No” flow by requesting a smaller first step before proceeding.

## Expected Timeline

- **Total time:** typically under a minute (depends on the carry-over contents)
- **User input required:** confirmation (Yes/No) before any action
