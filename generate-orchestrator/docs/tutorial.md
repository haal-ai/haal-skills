# Tutorial: generate-orchestrator

## Introduction

This tutorial guides you through using the `generate-orchestrator` skill to create workflow orchestrators that chain multiple skills together. By the end, you'll have a complete orchestrator skill package ready for use.

## Prerequisites

Before starting, ensure you have:

- [ ] Identified the skills you want to orchestrate
- [ ] Verified the skills exist in the skills directory
- [ ] Determined the execution order for your workflow
- [ ] Decided on any review gates needed

## Step-by-Step Instructions

### Step 1: Plan Your Orchestrator

Before generating, plan your workflow:

1. **List the skills**: What skills need to run in sequence?
2. **Define the order**: What's the correct execution sequence?
3. **Identify gates**: Where should the workflow pause for review?
4. **Consider failures**: Should the workflow stop on failure?

Example planning:
```
Workflow: Code Quality Pipeline
Skills: review-code → augment-code-unit-test → review-diff
Gates: After review-code (to address issues before testing)
Stop on failure: Yes
```

### Step 2: Invoke the Skill

Start the orchestrator generation:

```
Generate an orchestrator called "code-quality-pipeline"
```

Or with full parameters:

```
Generate an orchestrator:
- Name: code-quality-pipeline
- Description: Automated code quality checks with testing
- Skills: review-code, augment-code-unit-test, review-diff
- Review gates: after-review
- Stop on failure: yes
```

### Step 3: Provide Required Parameters

If using interactive mode, answer the prompts:

**Orchestrator name**:
```
code-quality-pipeline
```

**Description**:
```
Automated code quality pipeline that reviews code, generates tests, and validates changes
```

**Skills to orchestrate** (in order):
```
1. review-code
2. augment-code-unit-test
3. review-diff
```

**Review gates** (optional):
```
after-code-review
```

**Stop on failure**:
```
yes
```

### Step 4: Review the Proposal

The skill presents the orchestrator structure:

```
## Proposed Orchestrator: code-quality-pipeline

Execution Flow:
1. review-code
   ↓ (output: code review findings)
2. [GATE: after-code-review] - User confirmation required
   ↓
3. augment-code-unit-test
   ↓ (output: generated tests)
4. review-diff
   ↓ (output: diff analysis)

Stop on Failure: Yes
Recovery: Manual intervention required

Files to generate:
- skills/code-quality-pipeline/skill.md
- skills/code-quality-pipeline/docs/description.md
- skills/code-quality-pipeline/docs/tutorial.md

Proceed with generation? (yes/no)
```

### Step 5: Confirm Generation

Type `yes` to proceed. The skill will:

1. Create the orchestrator directory
2. Generate skill.md with full workflow definition
3. Create description.md documentation
4. Create tutorial.md for users

### Step 6: Review Generated Files

Check the generated orchestrator:

```bash
# View the structure
ls -la skills/code-quality-pipeline/

# Review the main skill file
cat skills/code-quality-pipeline/skill.md
```

Verify the skill.md includes:
- All skills listed in correct order
- Review gates properly defined
- Context passing between steps
- Error handling configuration

### Step 7: Test the Orchestrator

Run your new orchestrator:

```
Run the code-quality-pipeline orchestrator
```

Verify:
- Skills execute in the correct order
- Review gates pause for confirmation
- Failures are handled as configured
- Context passes correctly between steps

## Verification Checklist

After generation, verify:

- [ ] Orchestrator directory exists under skills/
- [ ] skill.md contains all required sections
- [ ] All skills to orchestrate are listed
- [ ] Execution order is correct
- [ ] Review gates are properly defined
- [ ] Stop-on-failure behavior is configured
- [ ] description.md provides clear overview
- [ ] tutorial.md has step-by-step instructions

## Troubleshooting

### "Skill not found in skills_to_orchestrate"

**Cause**: One of the specified skills doesn't exist.

**Solution**: Verify all skill names are correct and exist in the skills directory:
```bash
ls skills/
```

### "Orchestrator already exists"

**Cause**: A skill with that name already exists.

**Solution**: Choose a different name or confirm overwrite when prompted.

### "Invalid orchestrator name"

**Cause**: Name doesn't follow kebab-case or exceeds 4 words.

**Solution**: Use lowercase with hyphens, max 4 words:
- ✅ `code-review-pipeline`
- ✅ `release-workflow`
- ❌ `My Code Review Pipeline Workflow` (too long, wrong case)

### "Review gate not recognized"

**Cause**: Gate name doesn't match expected format.

**Solution**: Use descriptive kebab-case names:
- ✅ `after-review`
- ✅ `pre-deployment`
- ❌ `Gate 1` (spaces, not kebab-case)

### "Context not passing between steps"

**Cause**: Output/input mapping not properly defined.

**Solution**: Review the generated skill.md and ensure each step defines:
- What output it produces
- What input it expects from previous steps

## Next Steps

After creating your orchestrator:

1. **Test Thoroughly**: Run the orchestrator with various inputs
2. **Refine Gates**: Adjust review gates based on actual usage
3. **Document Edge Cases**: Add troubleshooting for common issues
4. **Share with Team**: Make the orchestrator available to others
5. **Iterate**: Improve based on feedback and usage patterns
