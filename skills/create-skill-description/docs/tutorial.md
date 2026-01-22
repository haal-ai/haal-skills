# Tutorial: Creating Skill Documentation with create-skill-description

This tutorial walks you through using the `create-skill-description` skill to generate documentation for your skills.

## Prerequisites
- An existing skill in `skills/` that needs documentation
- Basic familiarity with OLAF framework skills

## Step-by-Step Guide

### Step 1: Invoke the Skill

Start by calling the skill with any of its aliases:

```
olaf create-skill-description
```

Or use alternative commands:
```
olaf document skill
olaf generate skill docs
```

### Step 2: Select the Skill

If you didn't specify a skill name, the skill will ask:

```
Which skill would you like to document?
```

You can either:
- **Provide the skill name directly**: `review-code-quality`
- **Select from the list** if the skill displays available skills

**Example:**
```
Available skills:
1. create-skill
2. review-code-quality  
3. generate-test-cases
4. format-email-response

Which skill would you like to document? 2
```

### Step 3: Review Generated Documentation

The skill will:
1. Read your skill file
2. Analyze its structure and content
3. Extract parameters, process flow, and features
4. Generate a comprehensive description.md

You'll see the generated content displayed for review:

```markdown
# Review Code Quality

## Overview
Analyzes code files for quality issues and suggests improvements...

## Purpose
This skill helps developers identify code quality issues...

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
skills/[your-skill-name]/docs/description.md

```

**Check the file:**
- Open it in your editor
- Verify all sections are populated
- Make any manual refinements if needed

## Advanced Usage

### Documenting Multiple Skills

To document several skills efficiently:

```bash
# Document first skill
olaf document skill
> create-user-story

# Document second skill  
olaf document skill
> format-commit-message

# Document third skill
olaf document skill
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

### Providing Custom Skill Path

For skills in non-standard locations:

```
olaf create-skill-description

Skill name: my-custom-skill
Skill path: /custom/location/my-custom-skill
```

## Common Scenarios

### Scenario 1: New Skill Without Documentation

**Situation:** You just created a skill using `create-skill` but want better documentation.

**Solution:**
```
olaf document skill
> [your-new-skill-name]
> yes
```

### Scenario 2: Updating Outdated Documentation

**Situation:** Your skill changed significantly and documentation is outdated.

**Solution:**
1. Delete or backup existing `description.md`
2. Run `olaf create-skill-description`
3. Review and save the regenerated documentation

### Scenario 3: Documenting Legacy Skills

**Situation:** Old skills lack proper documentation.

**Solution:**
```
# List all skills needing documentation
ls skills/*/docs/

# Document each one
olaf document skill
> [legacy-skill-name]
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

### Tip 3: Keep Skills Up-to-Date
When you modify a skill significantly, regenerate its documentation:
```
olaf document skill
> [modified-skill]
```

### Tip 4: Standardize Documentation
Use this skill for all skills to maintain consistent documentation structure.

## Troubleshooting

### Issue: "Skill not found"
**Cause:** Skill name doesn't match any existing skill  
**Solution:** Check available skills in `skills/` or let the skill list them

### Issue: "Cannot read skill file"
**Cause:** Skill structure is incomplete or corrupted  
**Solution:** Verify the skill has a valid file at `skill.md`

### Issue: "File save failed"
**Cause:** Permission issues or disk full  
**Solution:** Check file permissions on the `/docs/` directory

### Issue: Documentation is incomplete
**Cause:** Skill file has minimal content  
**Solution:** Enhance your skill file first, then regenerate documentation

## Next Steps

After creating documentation:
1. **Review and refine** the generated description.md
2. **Create tutorial.md** for step-by-step usage guides (can be done manually or with another skill)
3. **Update skill metadata** if you added new features to the skill
4. **Share your documented skill** with team members

## Summary

You've learned how to:
- ✅ Invoke the create-skill-description skill
- ✅ Select skills for documentation
- ✅ Review and approve generated content
- ✅ Handle existing documentation
- ✅ Troubleshoot common issues

**Remember:** Good documentation makes your skills more discoverable and easier to use!
