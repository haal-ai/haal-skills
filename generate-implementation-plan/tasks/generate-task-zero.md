---
name: generate-task-zero
description: "Task 1 - Generate Task 0.0 following onboarding 0.3 pattern"
task_id: 1
protocol: Propose-Act
---

# Task 1: Generate Task 0.0 (Context Extraction)

## Objective

Create Task 0.0 specification following the **current onboarding Task 0.3 pattern** for extracting condensed task contexts.

## Context Variables

**Required**:
- `design_layers`: Output from Task 0 (JSON structure)
- `skill_path`: Target path for skill implementation
- `output_file`: Path to IMPLEMENTATION-TASK-PLAN.md

**Outputs**:
- `task_zero_spec`: Complete Task 0.0 specification (markdown)

## Execution Steps

### Step 1: Calculate Task Count

```
total_tasks = 3 (Phase 0) + sum of all layer estimated_tasks

Example:
  Phase 0: 3 tasks (0.0, 0.1, 0.2)
  Phase 1: 4 tasks (1.1, 1.2, 1.3, 1.4)
  Phase 2: 3 tasks (2.1, 2.2, 2.3)
  ...
  Total: 3 + 4 + 3 + ... = 47 tasks
```

### Step 2: Generate Task 0.0 Specification

**Template** (following onboarding 0.3):

```markdown
## Task 0.0: Extract Task Contexts

**CRITICAL**: This task MUST be executed FIRST before any other tasks

**Artifact**: Condensed context files for universal prompt generator  
**Execution Time**: 10-15 min  
**STRAF Command**:
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md" `
  --context "bootstrap_doc=${output_file},skill_path=${skill_path}" `
  --tool-mode standard `
  --aws-profile bedrock
```

**Task Details**:
- **Input**: ${output_file} (this implementation plan)
- **Process**:
  1. Read implementation plan
  2. Extract task definitions (Task 0.1 through {total_tasks})
  3. For each task, create condensed context file:
     - Task description
     - Inputs/outputs
     - Reuse references
     - Success criteria
  4. Save to ${skill_path}/tasks/contexts/task-{N}-context.md
  5. Compress ~50KB → ~500 tokens (97% reduction)

**Reuse**:
- **Existing tool**: `extract-task-contexts.md` from onboarding competency
- **Pattern**: Context extraction pattern (proven in onboarding)

**Outputs**:
- ${skill_path}/tasks/contexts/task-0.1-context.md
- ${skill_path}/tasks/contexts/task-0.2-context.md
- ${skill_path}/tasks/contexts/task-1.1-context.md
- ... (one file per task, {total_tasks} total)

**Dependencies**: None (FIRST task)

**Success Criteria**:
- ✅ All {total_tasks} context files generated
- ✅ Each file ~500 tokens (compressed)
- ✅ contexts/ directory created in ${skill_path}/tasks/
- ✅ Ready for universal-task-prompt-generator.md

**Impact**:
- 🚀 3x faster prompt generation (600s vs 1800s)
- 💾 97% smaller context files
- ✅ Enables universal prompt generator pattern

---
```

### Step 3: Add Explanation Section

```markdown
### Why Task 0.0 Exists

The universal-task-prompt-generator.md requires condensed context for each task to:
1. Avoid token limit issues (50KB → 500 tokens)
2. Speed up prompt generation (3x faster)
3. Enable consistent prompt structure across all tasks

This pattern was proven in onboarding competency bootstrap and is now standard for all ESDI-generated implementations.

**Original Pattern**: Each task had full implementation plan embedded (50KB)
**Current Pattern**: Each task has condensed context file (500 tokens)
**Result**: Faster, more reliable prompt generation
```

### Step 4: Propose to User

**CRITICAL**: Use Propose-Act protocol

```
Present to user:

📝 Task 0.0 Specification Generated

Pattern: Onboarding 0.3 (proven context extraction)
Total Tasks: {total_tasks}
Context Files: {total_tasks} files in ${skill_path}/tasks/contexts/

Task 0.0 will:
  ✅ Extract {total_tasks} task definitions from implementation plan
  ✅ Generate condensed context files (~500 tokens each)
  ✅ Save to ${skill_path}/tasks/contexts/
  ✅ Enable universal prompt generator for all tasks

Size Reduction: ~50KB → ~500 tokens (97% smaller)
Time Savings: ~1200 seconds per task (20 minutes)

STRAF Command:
  python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
    --prompt "olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md" \
    --context "bootstrap_doc=${output_file},skill_path=${skill_path}" \
    --tool-mode standard \
    --aws-profile bedrock

APPROVE to include Task 0.0 in implementation plan
ADJUST if modifications needed
```

## Success Criteria

✅ Task 0.0 specification follows onboarding 0.3 pattern exactly
✅ STRAF command uses extract-task-contexts.md
✅ Context variables correctly reference ${output_file} and ${skill_path}
✅ Total task count calculated correctly
✅ Explanation of why Task 0.0 exists included
✅ User approved via Propose-Act gate

## Error Handling

**If task count calculation fails**:
```
Error: Cannot determine total task count

Check design_layers structure has estimated_tasks for each layer.
Provide default: 3 (Phase 0) + 4 per layer
```

**If skill_path not provided**:
```
Error: skill_path required for Task 0.0

Default to: skills/${skill_name}
Confirm with user.
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "task_zero_spec": "## Task 0.0: Extract Task Contexts\n\n**CRITICAL**: ...",
  "total_tasks": 47,
  "context_file_count": 47,
  "straf_command": "python .\\...",
  "dependencies": []
}
```

## Next Task

→ Task 2: create-task-breakdown.md (uses task_zero_spec + design_layers)
