# Tutorial: run-implementation-plan

## Introduction

This tutorial guides you through using the `run-implementation-plan` skill to execute implementation plans systematically. You'll learn how to run plans, track progress, handle failures, and resume interrupted work.

## Prerequisites

Before starting, ensure you have:
- An implementation plan file (typically `IMPLEMENTATION-TASK-PLAN.md`)
- Tasks formatted with headings like `### Task 1.1: Task Title`
- Each task should include artifact, outputs, and success criteria

## Step-by-Step Instructions

### Step 1: Prepare Your Implementation Plan

Ensure your plan file follows the expected format:

```markdown
# Implementation Plan

Target: ./src/my-feature

## PHASE 1: Setup

### Task 1.1: Initialize Project Structure
**Artifact**: Project directory structure
**Outputs**: 
- src/index.ts
- src/types.ts
**Success Criteria**: All files created and compile without errors

### Task 1.2: Configure Dependencies
**Artifact**: Package configuration
**Outputs**:
- package.json updated
**Success Criteria**: npm install succeeds
```

### Step 2: Start Execution

Invoke the skill with your plan file:

```
Execute run-implementation-plan with:
  plan_file: ./IMPLEMENTATION-TASK-PLAN.md
```

The skill will:
1. Parse your plan and identify all tasks
2. Create a progress checklist
3. Present the first task for confirmation
4. Begin sequential execution

### Step 3: Confirm and Execute Tasks

For each task, the skill:

1. **Summarize**: The skill summarizes the task objective, expected outputs, and success criteria
2. **Confirm**: You review and approve the task execution
3. **Execute**: The skill performs the task (code changes, file edits, tests)

### Step 4: Monitor Progress

The skill maintains a checklist file (default: `.olaf/work/project-tasks/implementation-plan-checklist.md`) with:

```markdown
# Implementation Plan Checklist

## PHASE 1: Setup
- [x] Task 1.1: Initialize Project Structure (completed: 2026-01-16 10:30)
- [x] Task 1.2: Configure Dependencies (completed: 2026-01-16 10:45)
- [ ] Task 1.3: Create Base Components

## PHASE 2: Implementation
- [ ] Task 2.1: Implement Core Logic
```

### Step 5: Handle Failures

When a task fails:

**With `stop_on_failure: true` (default)**:
- Execution stops immediately
- The skill provides recovery instructions
- You can fix the issue and resume

**With `stop_on_failure: false`**:
- Failure is logged
- The skill asks whether to continue
- Execution can proceed to remaining tasks

### Step 6: Resume Interrupted Work

To continue from a specific task:

```
Execute run-implementation-plan with:
  plan_file: ./IMPLEMENTATION-TASK-PLAN.md
  start_from_task: 2.3
```

Or let the skill auto-detect the next pending task:

```
Execute run-implementation-plan with:
  plan_file: ./IMPLEMENTATION-TASK-PLAN.md
```

The skill reads the checklist and continues from the first unchecked task.

### Step 7: Enable Carry-Over (Optional)

For long-running plans or team handoffs, enable carry-over files:

```
Execute run-implementation-plan with:
  plan_file: ./IMPLEMENTATION-TASK-PLAN.md
  carry_over: true
  carry_over_dir: ./handoffs/
```

Each completed task generates a carry-over file containing:
- Task completed
- Files changed
- Next task ID
- Context and gotchas

## Verification Checklist

After execution, verify:

- [ ] Checklist file exists and shows correct task status
- [ ] Completed tasks are marked with timestamps
- [ ] Output artifacts exist as specified in tasks
- [ ] Success criteria are met for each completed task
- [ ] Any carry-over files are generated (if enabled)

## Troubleshooting

### Plan Format Not Recognized

**Symptom**: Skill cannot identify tasks in your plan

**Solution**: Ensure tasks use the expected heading format:
```markdown
### Task X.Y: Task Title
```

If your plan uses a different format, the skill will propose a normalization patch.

### Checklist Not Updating

**Symptom**: Progress not being saved

**Solution**: 
1. Check write permissions on the checklist directory
2. Verify the `checklist_path` parameter is correct
3. Ensure the directory exists or can be created

### Task Execution Fails Repeatedly

**Symptom**: Same task keeps failing

**Solution**:
1. Review the error message for specific issues
2. Check if prerequisites from earlier tasks are complete
3. Manually verify the task's success criteria
4. Consider breaking the task into smaller steps

### Resume Not Working

**Symptom**: Skill starts from beginning instead of resuming

**Solution**:
1. Verify the checklist file exists and is readable
2. Check that task IDs in `start_from_task` match the plan format
3. Ensure the checklist format matches expected structure

## Next Steps

After completing this tutorial, explore:

- **generate-implementation-plan**: Create new implementation plans
- **carry-over-session**: Manage session handoffs between team members
- **generate-design**: Create design documents that inform implementation plans

## Tips for Success

1. **Review tasks before execution**: Use the Propose phase to catch issues early
2. **Keep tasks atomic**: Each task should have clear, verifiable outputs
3. **Use carry-over for long plans**: Preserve context across sessions
4. **Check the checklist regularly**: Monitor progress and identify blockers
5. **Handle failures promptly**: Don't let failed tasks accumulate
