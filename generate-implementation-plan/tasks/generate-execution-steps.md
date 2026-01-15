---
name: generate-execution-steps
description: "Task 3 - Create execution steps for each task"
task_id: 3
protocol: Propose-Act
---

# Task 3: Generate Execution Steps

## Objective

Generate execution information for every task in the breakdown, including task prompts, context variables, and dependencies.

## Context Variables

**Required**:
- `task_breakdown`: Output from Task 2
- `skill_path`: Target skill path
- `output_file`: Path to IMPLEMENTATION-TASK-PLAN.md

**Outputs**:
- `task_execution_info`: Map of task_id → execution details (prompt path, context, dependencies)

## Execution Steps

### Step 1: Define Task Structure Templates

For each task type:
- Phase 0 tasks: Setup and initialization
- Layer tasks: Implementation tasks organized by layer
- Each task needs: prompt path, context variables, dependencies

### Step 2: Define Phase 0 Task Information

**Task 0.0** (already defined in task_zero_spec):
- **Prompt**: `olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md`
- **Context**: `bootstrap_doc=${output_file},skill_path=${skill_path}`
- **Dependencies**: None

**Task 0.1**:
- **Prompt**: `${skill_path}/tasks/setup/create-skill-structure.md`
- **Context**: `skill_name=${skill_name},target_path=${skill_path}`
- **Dependencies**: Task 0.0

**Task 0.2**:
- **Prompt**: `${skill_path}/tasks/setup/create-master-coordinator.md`
- **Context**: `skill_name=${skill_name},layers=${layer_count},pattern=sequential,output_base=${output_dir}`
- **Dependencies**: Task 0.1

### Step 3: Define Layer Task Information

For each layer task (1.1, 1.2, ..., N.M):

- **Prompt**: `${skill_path}/tasks/layer-${layer_num}/${task_slug}.md`
- **Context Variables**: 
  - `skill_path`: From context
  - `component`: Component name from task_breakdown
  - `layer_number`: Layer ID from task_breakdown
  - `input_file`: Previous layer output or design artifact
  - `task_id`: Task ID (e.g., "1.2")
  - `context_file`: `${skill_path}/tasks/contexts/task-${task_id}-context.md`
- **Dependencies**: Previous tasks in sequence

### Step 4: Format Task Information

For each task, document:
- **Task Prompt**: Path to the task prompt file
- **Context**: Key-value pairs of context variables
- **Dependencies**: List of prerequisite tasks
- **Expected Outputs**: Artifacts produced
- **Execution Time**: Estimated duration

### Step 5: Propose Task Structure

**CRITICAL**: Use Propose-Act protocol

```
Present to user:

⚙️ Execution Information Generated for All {total_tasks} Tasks

Sample Task Information:

📌 Task 0.0 (Extract Contexts):
- **Prompt**: olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md
- **Context**: bootstrap_doc=${output_file},skill_path=${skill_path}
- **Dependencies**: None
- **Outputs**: Context files for all tasks

📌 Task 1.1 (First Layer Task):
- **Prompt**: ${skill_path}/tasks/layer-1/implement-component-1.md
- **Context**: skill_path=${skill_path},component=Component1,layer_number=1,context_file=${skill_path}/tasks/contexts/task-1.1-context.md
- **Dependencies**: Task 0.0, 0.1, 0.2
- **Outputs**: Component implementation

📌 Task 2.1 (Second Layer Task):
- **Prompt**: ${skill_path}/tasks/layer-2/implement-component-x.md
- **Context**: skill_path=${skill_path},component=ComponentX,layer_number=2,context_file=${skill_path}/tasks/contexts/task-2.1-context.md
- **Dependencies**: All Phase 1 tasks
- **Outputs**: Layer 2 component

Context Variables:
  ${output_file} = {actual_path}
  ${skill_path} = {actual_skill_path}
  ${skill_name} = {actual_name}
  ${layer_count} = {actual_count}

Execution Approach:
  ✅ Tasks can be executed sequentially
  ✅ Each task has clear prompt and context
  ✅ Dependencies explicitly defined

APPROVE to proceed to Task 4 (Bootstrap Integration)
ADJUST if task structure needs refinement
```

## Success Criteria

✅ Execution information generated for every task
✅ Context variables properly defined
✅ Dependencies clearly specified
✅ Task prompts paths correctly formatted
✅ Task 0.0 uses existing extract-task-contexts.md
✅ Layer tasks reference context files from Task 0.0
✅ User approved via Propose-Act gate

## Error Handling

**If context variable missing**:
```
Warning: Task {task_id} missing required variable: {var_name}
Default: Use placeholder ${var_name}
User will provide actual value during execution
```

**If prompt path ambiguous**:
```
Error: Cannot determine prompt path for Task {task_id}

Expected pattern:
  Phase 0: ${skill_path}/tasks/setup/{task-name}.md
  Layer N: ${skill_path}/tasks/layer-{N}/{task-name}.md

Suggest: Create prompt paths based on task breakdown
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "task_execution_info": {
    "0.0": {
      "prompt": "olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md",
      "context": "bootstrap_doc=...,skill_path=...",
      "dependencies": []
    },
    "0.1": {
      "prompt": "${skill_path}/tasks/setup/create-skill-structure.md",
      "context": "skill_name=...,target_path=...",
      "dependencies": ["0.0"]
    },
    ...
  },
  "total_tasks": 47
}
```

## Next Task

→ Task 4: create-bootstrap-integration.md (uses task_commands)
