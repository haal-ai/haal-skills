# Tutorial: convert-skill-to-chain

## Introduction

This tutorial guides you through converting an existing OLAF skill into the master-chain pattern using the `convert-skill-to-chain` skill. The master-chain pattern breaks monolithic skills into modular, reusable task files with a coordinator prompt.

## Prerequisites

Before starting, ensure you have:

- [ ] An existing skill that you want to convert
- [ ] The skill has a valid `skill.md` file
- [ ] Understanding of the skill's current workflow
- [ ] Write access to the skill's directory

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Start the conversion process by invoking the skill:

```
@convert-skill-to-chain
```

The skill will begin the 11-task conversion workflow.

### Step 2: Select Skill to Convert

When prompted, select the skill you want to convert:

```
Available skills for conversion:
1. my-complex-skill
2. another-skill
3. workflow-skill

Please select a skill to convert: my-complex-skill
```

### Step 3: Review Backup Creation

The skill automatically backs up your original skill.md:

```
✓ Backup created: my-complex-skill/skill.md.backup
```

Verify the backup exists before proceeding.

### Step 4: Review Structure Analysis

The skill analyzes your skill's current structure:

```
Skill Structure Analysis:
- Entry points: 1
- Workflow steps: 7
- Conditional branches: 2
- External dependencies: 3
```

### Step 5: Review Pattern Detection

The skill identifies the workflow pattern:

```
Detected Pattern: sequential
Confidence: high
Pattern Details:
- Linear task flow
- No loops detected
- Clear input/output boundaries
```

### Step 6: Review Conversion Decision

The skill evaluates if conversion is beneficial:

**If conversion is recommended:**
```
Conversion Recommended
Complexity Score: 7/10
Reason: Skill has multiple distinct phases suitable for task extraction
```

**If conversion is not needed:**
```
Analysis Complete - No Conversion Needed
Skill: simple-skill
Complexity: 2/10
This skill remains as a single-prompt implementation.
```

If conversion is not needed, the workflow stops here gracefully.

### Step 7: Review Common Tasks Found

The skill searches for reusable common tasks:

```
Common Tasks Found:
- common/tasks/validate-input.md (reusable)
- common/tasks/format-output.md (reusable)

These will be referenced instead of duplicated.
```

### Step 8: Review Task Boundaries

The skill identifies where to split the skill:

```
Task Boundaries Identified:
1. Initialize and validate inputs
2. Fetch required data
3. Process business logic
4. Format results
5. Generate output
```

### Step 9: Verify Task Extraction

The skill creates individual task files:

```
Tasks Extracted:
✓ tasks/initialize-inputs.md
✓ tasks/fetch-data.md
✓ tasks/process-logic.md
✓ tasks/format-results.md
✓ tasks/generate-output.md
```

### Step 10: Review Master Coordinator

The skill creates the new master coordinator:

```
Master Coordinator Created:
- File: my-complex-skill/skill.md
- Tasks: 5
- Dependencies: Properly linked
- Context passing: Configured
```

### Step 11: Verify Registry Update

The skill updates the task registry:

```
Registry Updated:
- Added 5 new tasks
- Updated task dependencies
- Registry location: common/tasks/registry.md
```

### Step 12: Review Conversion Summary

Review the final summary:

```
Conversion Complete!
==================
Skill: my-complex-skill
Pattern: sequential
Tasks Created: 5
Common Tasks Reused: 2
Backup: my-complex-skill/skill.md.backup

New Structure:
my-complex-skill/
├── skill.md (master coordinator)
├── skill.md.backup (original)
└── tasks/
    ├── initialize-inputs.md
    ├── fetch-data.md
    ├── process-logic.md
    ├── format-results.md
    └── generate-output.md
```

## Verification Checklist

After conversion, verify:

- [ ] Original skill.md is backed up
- [ ] New skill.md contains master coordinator structure
- [ ] All task files exist in tasks/ directory
- [ ] Task dependencies are correctly defined
- [ ] Context variables are properly passed between tasks
- [ ] Registry is updated with new tasks
- [ ] Skill executes correctly with new structure

## Troubleshooting

### Conversion Stops at Task 5

**Symptom**: Workflow ends after evaluation phase

**Cause**: Skill complexity is too low for conversion

**Solution**: This is expected behavior. Simple skills don't benefit from the master-chain pattern.

### Missing Task Files

**Symptom**: Some task files not created

**Cause**: Task extraction encountered an error

**Solution**: Check the error message, restore from backup, and retry with manual task boundary hints.

### Broken Dependencies

**Symptom**: Converted skill fails during execution

**Cause**: Context variables not properly passed

**Solution**: Review the task chain definition in skill.md and ensure all `depends_on` entries are correct.

### Registry Update Failed

**Symptom**: Tasks not appearing in registry

**Cause**: Registry file access issue

**Solution**: Manually add task entries to the registry following the existing format.

## Next Steps

After successful conversion:

1. **Test the converted skill** - Run the skill to verify it works correctly
2. **Review task reusability** - Identify tasks that could be shared with other skills
3. **Document the new structure** - Update any skill documentation
4. **Consider further optimization** - Look for additional common task opportunities
