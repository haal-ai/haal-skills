# Tutorial: carry-over-session

## Introduction

This tutorial guides you through using the `carry-over-session` skill to create carry-over notes that enable seamless session continuation.

## Prerequisites

- Active workspace with ongoing work
- Conversation context with the AI assistant
- Write access to `.olaf/work/carry-over/` directory

## Step-by-Step Instructions

### Step 1: Identify the Right Moment

Before ending your work session, ensure you have:
- A clear stopping point in your current task
- Understanding of what needs to happen next

**Expected Outcome**: You know the logical next step in your workflow.

### Step 2: Invoke the Skill

Call the carry-over-session skill:
```
@carry-over-session
```

**Expected Outcome**: The skill begins analyzing your conversation context.

### Step 3: Review the Generated Note

The skill will produce a carry-over note with:
- A specific, actionable prompt for your next session
- List of files with absolute paths

**Example Output**:
```text
CARRY-OVER - 2025-11-14 14:30
========================

## NEXT PROMPT
Add JWT validation to AuthService, update login to return token.

## FILES NEEDED (Absolute Paths)
c:\Users\user\project\src\services\AuthService.ts
c:\Users\user\project\src\middleware\auth.ts
```

### Step 4: Verify File Location

Confirm the note was saved to:
```
.olaf/work/carry-over/carry-over-YYYYMMDD-HHmm.txt
```

**Expected Outcome**: File exists with current timestamp.

### Step 5: Resume Later with carry-on-session

When starting your next session, use the companion skill:
```
@carry-on-session
```

This will read your carry-over note and restore context.

## Verification Checklist

- [ ] Carry-over note created in `.olaf/work/carry-over/`
- [ ] Next prompt is clear and actionable
- [ ] All relevant files are listed with absolute paths
- [ ] Timestamp matches current date/time

## Troubleshooting

### Issue: No clear next prompt generated

**Cause**: Insufficient context in the conversation.

**Solution**: Provide more details about your current task and intended next steps before invoking the skill.

### Issue: Missing files in the list

**Cause**: Files weren't explicitly mentioned in the conversation.

**Solution**: Mention the files you're working with before creating the carry-over note.

### Issue: Directory doesn't exist

**Cause**: First time using carry-over functionality.

**Solution**: The skill will create the directory automatically. If it fails, manually create `.olaf/work/carry-over/`.

## Tips for Best Results

1. **Be explicit** about your current task before invoking
2. **Mention files** you're actively working with
3. **State your next goal** clearly in the conversation
4. **Use regularly** at natural stopping points

## Next Steps

- Learn about `carry-on-session` to resume work
- Explore `stash-restart-session` for alternative session management
