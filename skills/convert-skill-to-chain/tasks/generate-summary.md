---
task_id: "generate-summary"
task_name: "Generate Conversion Summary"
dependencies: ["context.master_created", "context.registry_updated"]
conditions: []
---

# Generate Conversion Summary

## Input Context
**Required Context Variables**: 
- `context.skill_name`: Converted skill name
- `context.task_count`: Total tasks in chain
- `context.reuse_count`: Common tasks reused
- `context.new_count`: New tasks created
- `context.extracted_tasks`: List of created files
- `context.master_file`: Path to master coordinator
- `context.tasks_registered`: Tasks added to registry
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Create Conversion Report

1. **Generate Summary Report**:

```markdown
# Skill Conversion Summary

## Conversion Complete

**Skill**: [skill_name]
**Date**: [current date]
**Pattern**: Master Chain Coordinator

---

## Conversion Statistics

- **Total Tasks**: [task_count]
- **Common Tasks Reused**: [reuse_count]
- **New Tasks Created**: [new_count]
- **Tasks Registered**: [tasks_registered]

---

## Files Created

### Master Coordinator
- `[master_file]`

### Task Files ([new_count] new tasks)
[for each in extracted_tasks:]
- `[task_file]`

---

## Task Chain Overview

```yaml
[display task chain from task_boundaries]
```

---

## Reusable Common Tasks

[for each common task reused:]
- ✓ **[task_id]**: [task_name]
  - Location: [location]
  - Purpose: [description]

---

## Registry Updates

- **Tasks Added**: [tasks_registered]
- **Common Task Usages Updated**: [common_tasks_usage_updated]
- **Registry**: `skills/common/kb/task-registry.json`

---

## Next Steps

1. **Test the converted skill**:
   ```
   Use skill: [skill_name]
   ```

2. **Review task files** for accuracy:
   - Check task boundaries make sense
   - Verify input/output context variables
   - Ensure single responsibility per task

3. **Consider generalizing tasks**:
   - Review reusability scores in registry
   - Identify tasks that could be moved to common/
   - Update registry if tasks become more general

4. **Update documentation**:
   - Add skill to list of master-chain pattern skills
   - Document any unique patterns or learnings

---

## Quality Checklist

- [ ] Tasks have clear input/output definitions
- [ ] No forward references between tasks
- [ ] Common tasks properly referenced
- [ ] Registry updated with new tasks
- [ ] All task files have proper frontmatter
- [ ] Context variables flow correctly through chain

```

2. **Display Summary to User**:
   - Show the complete summary
   - Highlight key metrics
   - Note any warnings or recommendations

## Output Requirements

**State Updates**:
- `context.conversion_summary`: Full summary text
- `task_status.generate-summary`: "completed"

**Files Created**: None (summary displayed, not saved)

**Context Passed**: 
- Final task - no subsequent tasks
