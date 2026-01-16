---
name: create-bootstrap-integration
description: "Task 6 - Generate bootstrap orchestrator configuration"
task_id: 6
protocol: Propose-Act
---

# Task 6: Create Bootstrap Integration

## Objective

Generate the bootstrap orchestrator execution command and integration instructions for autonomous task execution.

## Context Variables

**Required**:
- `output_file`: Path to IMPLEMENTATION-TASK-PLAN.md

**Optional**:
- `execution_mode`: `manual|bootstrap` (default: `manual`)
- `include_bootstrap`: `true|false` (default: `false`)
- `bootstrap_orchestrator_prompt`: Prompt path to the bootstrap/orchestrator tool (required only if `include_bootstrap=true`)
- `skill_path`: Target skill path (only needed when using bootstrap + prompt trees)

- `checklist_path`: Task tracking file (default: `.olaf/work/project-tasks/task-checklist.md`)

**Outputs**:
- `bootstrap_command`: Bootstrap execution command
- `bootstrap_instructions`: Integration documentation

## Execution Steps

If `execution_mode` is not `bootstrap` OR `include_bootstrap=false`, set:
- `bootstrap_command`: empty string
- `bootstrap_instructions`: "Bootstrap execution omitted (manual execution mode)."

Only generate the bootstrap command and instructions when `execution_mode=bootstrap` AND `include_bootstrap=true`.

### Step 1: Define Runner Inputs

When `execution_mode=bootstrap` AND `include_bootstrap=true`, produce runner-oriented inputs (not tied to any specific framework/tool):

- `plan_file`: `${output_file}`
- `checklist_path`: `${checklist_path}`
- `start_from_task`: optional resume marker (example: `2.1`)
- `stop_on_failure`: default `true`

### Step 2: Create Integration Instructions

```markdown
## Bootstrap Execution

### Full Autonomous Execution

Execute ALL tasks sequentially via a plan runner.

Runner configuration (conceptual):
- `plan_file`: `${output_file}`
- `checklist_path`: `${checklist_path}`
- `mode`: `auto` (runner proceeds task-by-task without additional human intervention)

**What Happens**:
1. Bootstrap orchestrator reads this implementation plan
2. For each task (0.0 → {total_tasks}):
  - Loads task context (from plan, and optional condensed per-task context if you generated it)
  - Executes the task steps
   - Verifies outputs against success criteria
   - Updates checklist with completion status
   - If task fails → STOPS and reports error
3. Displays final summary of completed implementation

**Execution Time**: {estimated_total_time} minutes
**Autonomous**: YES (tool-mode=auto, no human intervention)

### Resume from Specific Task

If execution fails or is interrupted:

Runner configuration (conceptual):
- `plan_file`: `${output_file}`
- `checklist_path`: `${checklist_path}`
- `start_from_task`: `{example_task_id}`

Replace `{example_task_id}` with task ID from checklist (e.g., "2.1", "3.4")

### Monitor Progress

Track execution via checklist:

- Open `${checklist_path}` and update statuses as tasks complete.

---

## How Bootstrap Orchestrator Works

The runner follows this pattern:

```
FOR each phase (0 through {total_phases}):
  FOR each task in phase:
    
    STEP 0: Load task definition
      From: ${output_file}
    
    STEP 1: (Optional) Load condensed task context
      Only if you generated per-task context files
    
    STEP 2: Execute task steps
      Output: Task deliverables
    
    STEP 3: Verify success
      Check outputs match success criteria
      IF failed → STOP execution, report error
      IF success → Update checklist, proceed
  
  NEXT task
NEXT phase

Display final summary
```

**Key Features**:
- ✅ **Sequential execution**: Each task completes before next starts
- ✅ **Error handling**: Stops on failure, allows resume
- ✅ **Progress tracking**: Updates checklist in real-time
- ✅ **Autonomous**: No human intervention required

---

## Prerequisites

Before running bootstrap:

1. ✅ **Implementation plan validated** (this file)
  - All tasks documented
  - Dependencies logical

2. ✅ **Runner configured** (if using a runner)
  - Knows `plan_file`, `checklist_path`, and optional resume marker

---
```

### Step 4: Calculate Estimated Time

```
estimated_time_per_task = 10 minutes (average)
total_tasks = {from task_breakdown}
estimated_total_time = total_tasks * 10 minutes

Example:
  47 tasks × 10 min = 470 minutes (~8 hours)
  
Adjust for:
  - Task 0.0: 15 minutes (longer for context extraction)
  - Complex layer tasks: 15-20 minutes
  - Simple migration tasks: 5 minutes
```

### Step 5: Propose to User

**CRITICAL**: Use Propose-Act protocol

```
Present to user:

🚀 Bootstrap Integration Complete

Runner Inputs:
  - plan_file=${output_file}
  - checklist_path=${checklist_path}
  - mode=auto

Orchestration Pattern:
  ✅ Sequential execution (Phase 0 → Phase {last_phase})
  ✅ Autonomous (tool-mode=auto, no human intervention)
  ✅ Resumable (from any task ID)
  ✅ Progress tracking (via task-checklist.md)

Estimated Execution:
  Total Tasks: {total_tasks}
  Estimated Time: {estimated_total_time} minutes (~{hours} hours)

Prerequisites:
  ⚠️ Run Task 0.0 manually FIRST only if your plan includes Task 0.0
  ✅ Runner available (manual or automated)

Resume Command (if needed):
Resume Hint:
  Re-run your runner with `start_from_task=X.Y`

APPROVE to include bootstrap integration in plan
ADJUST if modifications needed
```

## Success Criteria

✅ Runner configuration references ${output_file} and ${checklist_path}
✅ Resume pattern documented
✅ Integration instructions complete
✅ Prerequisites listed
✅ Estimated execution time calculated
✅ User approved via Propose-Act gate

## Error Handling

**If checklist_path not provided**:
```
Default to: .olaf/work/project-tasks/task-checklist.md
Inform user of default location
```

**If estimated time calculation fails**:
```
Use conservative estimate:
  total_tasks × 15 minutes = {result}
  
Note: Actual time may vary based on task complexity
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "runner_inputs": {
    "plan_file": "${output_file}",
    "checklist_path": "${checklist_path}",
    "start_from_task": "(optional)"
  },
  "estimated_time_minutes": 470,
  "estimated_time_hours": 7.8,
  "prerequisites": [
    "Task 0.0 executed manually",
    "Runner available (manual or automated)"
  ]
}
```

## Next Task

→ Task 5: generate-plan-document.md (assembles final IMPLEMENTATION-TASK-PLAN.md)
