---
name: generate-task-zero
description: "Task 2 - Optionally generate Task 0.0 (condensed task context extraction)"
task_id: 2
protocol: Propose-Act
---

# Task 2: Generate Task 0.0 (Context Extraction)

## Objective

Create an OPTIONAL Task 0.0 specification for extracting condensed per-task context files.

## Context Variables

**Required**:
- `design_layers`: Output from Task 1 (JSON structure)
- `output_file`: Path to IMPLEMENTATION-TASK-PLAN.md

**Optional**:
- `execution_mode`: `manual|bootstrap` (default: `manual`)
- `include_task_context_extraction`: `true|false` (default: `false`)
- `task_context_extractor_prompt`: Prompt path to the context-extraction tool (required only if `include_task_context_extraction=true`)
- `deliverable_root`: Root path for deliverables
- `skill_path`: Back-compat alias used only when generating an OLAF-skill plan

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

ONLY generate Task 0.0 when `execution_mode=bootstrap` AND `include_task_context_extraction=true`.

If NOT enabled, set `task_zero_spec` to an empty string and explicitly state: "Task 0.0 omitted (manual execution mode)."

**Template** (following onboarding 0.3):

```markdown
## Task 0.0: Extract Task Contexts

**CRITICAL**: This task MUST be executed FIRST before any other tasks

**Artifact**: Condensed context files for universal prompt generator  
**Execution Time**: 10-15 min  
**Execution Notes**:
- Use `${task_context_extractor_prompt}` (or an equivalent mechanism) to generate condensed per-task context files.
- Inputs should include `bootstrap_doc=${output_file}` and the target root (`deliverable_root` or `skill_path`).

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
  4. Save to ${deliverable_root}/tasks/contexts/task-{N}-context.md (or an equivalent location)
  5. Compress ~50KB → ~500 tokens (97% reduction)

**Reuse**:
- **Existing tool**: A task-context extraction prompt (provided via `task_context_extractor_prompt`)
- **Pattern**: Condensed context extraction to keep per-task execution small

**Outputs**:
- ${deliverable_root}/tasks/contexts/task-0.1-context.md
- ${deliverable_root}/tasks/contexts/task-0.2-context.md
- ${deliverable_root}/tasks/contexts/task-1.1-context.md
- ... (one file per task, {total_tasks} total)

**Dependencies**: None (FIRST task)

**Success Criteria**:
- ✅ All {total_tasks} context files generated
- ✅ Each file is condensed (target: ~500 tokens)
- ✅ `contexts/` directory created under the chosen root
- ✅ Runner/manual execution can load per-task context instead of full plan

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

This is an optional optimization for large plans.

**Original Pattern**: Each task had full implementation plan embedded (50KB)
**Current Pattern**: Each task has condensed context file (500 tokens)
**Result**: Faster, more reliable prompt generation
```

### Step 4: Propose to User

**CRITICAL**: Use Propose-Act protocol

```
Present to user:

📝 Task 0.0 Specification Generated

Pattern: condensed per-task context extraction
Total Tasks: {total_tasks}
Context Files: {total_tasks} files in ${deliverable_root}/tasks/contexts/

Task 0.0 will:
  ✅ Extract {total_tasks} task definitions from implementation plan
  ✅ Generate condensed context files (~500 tokens each)
  ✅ Save to ${skill_path}/tasks/contexts/
  ✅ Enable universal prompt generator for all tasks

Size Reduction: ~50KB → ~500 tokens (97% smaller)
Time Savings: ~1200 seconds per task (20 minutes)

Execution Notes:
  Use `${task_context_extractor_prompt}` with context like:
  - `bootstrap_doc=${output_file}`
  - `deliverable_root=${deliverable_root}` (or `skill_path` if applicable)

APPROVE to include Task 0.0 in implementation plan
ADJUST if modifications needed
```

## Success Criteria

✅ Task 0.0 specification is optional and clearly scoped
✅ Execution notes reference `task_context_extractor_prompt`
✅ Context variables correctly reference ${output_file} and a target root
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
Error: skill_path/deliverable_root required for Task 0.0

If generating an OLAF skill plan, default to: skills/${skill_name}
Otherwise, use deliverable_root.
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
  "runner_hint": "Invoke your context-extractor with bootstrap_doc + deliverable_root",
  "dependencies": []
}
```

## Next Task

→ Task 3: create-task-breakdown.md (uses task_zero_spec + design_layers)
