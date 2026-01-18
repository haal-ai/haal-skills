# Tutorial: carry-on-session

## Introduction
Resume your previous work session by loading a carry-over note and reviewing the proposed next steps.

## Prerequisites
- Existing carry-over note in `.olaf/work/carry-over/`
- Created using `carry-over-session` skill

## Step-by-Step Instructions

### Step 1: Invoke the Skill
```
@carry-on-session
```

### Step 2: Review the Proposal
The skill displays:
- Session date from the carry-over file
- The exact next prompt to execute
- Files that need to be opened

### Step 3: Confirm or Adjust
- Type **Yes** to proceed with the proposed plan
- Type **No** and specify adjustments if needed

### Step 4: Execute the Plan
Once confirmed, the assistant will:
- Open the listed files
- Execute the proposed prompt

## Verification Checklist
- [ ] Latest carry-over file was found
- [ ] Proposal displays correct session date
- [ ] Next prompt matches your expectations
- [ ] File paths are valid

## Troubleshooting

### No carry-over files found
Run `@carry-over-session` first to create a carry-over note.

### Wrong carry-over loaded
Check `.olaf/work/carry-over/` for multiple files and manually specify which one to use.

## Next Steps
- Use `carry-over-session` at the end of each work session
- Review and clean up old carry-over files periodically
