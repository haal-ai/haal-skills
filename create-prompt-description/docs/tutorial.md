# Tutorial: Creating Prompt Documentation with create-prompt-description

This tutorial walks you through using the `create-prompt-description` skill to generate documentation for your prompts.

## Prerequisites
- An existing prompt in `skills/` that needs documentation
- Basic familiarity with OLAF framework prompts

## Step-by-Step Guide

### Step 1: Invoke the Skill

Start by calling the skill with any of its aliases:

```
olaf create-prompt-description
```

Or use alternative commands:
```
olaf document prompt
olaf generate prompt docs
```

### Step 2: Select the Prompt

If you didn't specify a prompt name, the skill will ask:

```
Which prompt would you like to document?
```

You can either:
- **Provide the prompt name directly**: `review-code-quality`
- **Select from the list** if the skill displays available prompts

**Example:**
```
Available prompts:
1. create-prompt
2. review-code-quality  
3. generate-test-cases
4. format-email-response

Which prompt would you like to document? 2
```

### Step 3: Review Generated Documentation

The skill will:
1. Read your prompt file
2. Analyze its structure and content
3. Extract parameters, process flow, and features
4. Generate a comprehensive description.md

You'll see the generated content displayed for review:

```markdown
# Review Code Quality

## Overview
Analyzes code files for quality issues and suggests improvements...

## Purpose
This prompt helps developers identify code quality issues...

[... full generated content ...]
```

### Step 4: Approve or Request Changes

After reviewing, you have three options:

**Option A: Approve and Save**
```
Ready to save this documentation? (yes/no/edit)
> yes
✅ Documentation saved to skills/review-code-quality/docs/description.md
```

**Option B: Request Edits**
```
Ready to save this documentation? (yes/no/edit)
> edit

What changes would you like?
> Add more examples in the Examples section

[Skill regenerates with requested changes]
Ready to save this documentation? (yes/no/edit)
> yes
```

**Option C: Cancel**
```
Ready to save this documentation? (yes/no/edit)
> no

Would you like to cancel or provide different requirements?
> cancel
Operation cancelled.
```

### Step 5: Verify the Documentation

After saving, verify the file was created:

**Location:**
```
skills/[your-prompt-name]/docs/description.md
```

**Check the file:**
- Open it in your editor
- Verify all sections are populated
- Make any manual refinements if needed

## Advanced Usage

### Documenting Multiple Prompts

To document several prompts efficiently:

```bash
# Document first prompt
olaf document prompt
> create-user-story

# Document second prompt  
olaf document prompt
> format-commit-message

# Document third prompt
olaf document prompt
> analyze-dependencies
```

### Handling Existing Documentation

If `description.md` already exists, the skill will warn you:

```
⚠️  description.md already exists at:
skills/review-code-quality/docs/description.md

Do you want to overwrite it? (yes/no)
> yes
```

**Best Practice:** Review the existing file first to preserve any manual customizations.

### Providing Custom Prompt Path

For prompts in non-standard locations:

```
olaf create-prompt-description

Prompt name: my-custom-prompt
Prompt path: /custom/location/my-custom-prompt
```

## Common Scenarios

### Scenario 1: New Prompt Without Documentation

**Situation:** You just created a prompt using `create-prompt` but want better documentation.

**Solution:**
```
olaf document prompt
> [your-new-prompt-name]
> yes
```

### Scenario 2: Updating Outdated Documentation

**Situation:** Your prompt changed significantly and documentation is outdated.

**Solution:**
1. Delete or backup existing `description.md`
2. Run `olaf create-prompt-description`
3. Review and save the regenerated documentation

### Scenario 3: Documenting Legacy Prompts

**Situation:** Old prompts lack proper documentation.

**Solution:**
```
# List all prompts needing documentation
ls skills/*/docs/

# Document each one
olaf document prompt
> [legacy-prompt-name]
```

## Tips and Best Practices

### Tip 1: Review Before Saving
Always review the generated documentation. The skill is smart, but manual review ensures accuracy.

### Tip 2: Edit After Generation
The generated `description.md` is a starting point. Feel free to enhance it with:
- Additional examples
- Screenshots or diagrams
- Advanced usage patterns
- Known limitations

### Tip 3: Keep Prompts Up-to-Date
When you modify a prompt significantly, regenerate its documentation:
```
olaf document prompt
> [modified-prompt]
```

### Tip 4: Standardize Documentation
Use this skill for all prompts to maintain consistent documentation structure across your skills.

## Troubleshooting

### Issue: "Prompt not found"
**Cause:** Prompt name doesn't match any existing prompt  
**Solution:** Check available prompts in `skills/` or let the skill list them

### Issue: "Cannot read prompt file"
**Cause:** Prompt structure is incomplete or corrupted  
**Solution:** Verify the prompt has a valid file at `prompts/[prompt-name].md`

### Issue: "File save failed"
**Cause:** Permission issues or disk full  
**Solution:** Check file permissions on the `/docs/` directory

### Issue: Documentation is incomplete
**Cause:** Prompt file has minimal content  
**Solution:** Enhance your prompt file first, then regenerate documentation

## Next Steps

After creating documentation:
1. **Review and refine** the generated description.md
2. **Create tutorial.md** for step-by-step usage guides (can be done manually or with another skill)
3. **Update skill manifest** if you added new features to the prompt
4. **Share your documented prompt** with team members

## Summary

You've learned how to:
- ✅ Invoke the create-prompt-description skill
- ✅ Select prompts for documentation
- ✅ Review and approve generated content
- ✅ Handle existing documentation
- ✅ Troubleshoot common issues

**Remember:** Good documentation makes your prompts more discoverable and easier to use!
