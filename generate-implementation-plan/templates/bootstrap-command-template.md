# Plan Runner Execution Template

## Full Autonomous Execution

```powershell
# This is a placeholder template.
# Replace with whatever runner mechanism you use in your environment.

# Required runner inputs:
# - plan_file={output_file}
# - checklist_path={checklist_path}
# - mode=auto
```

**Variables**:
- `{output_file}`: Path to IMPLEMENTATION-TASK-PLAN.md
- `{checklist_path}`: Task progress tracker (default: `.olaf/work/project-tasks/task-checklist.md`)

**Behavior**:
- Sequential execution of ALL tasks
- Autonomous (no human intervention)
- Error handling (stops on failure)
- Progress tracking (updates checklist)

---

## Resume from Specific Task

```powershell
# Runner inputs (conceptual):
# - plan_file={output_file}
# - checklist_path={checklist_path}
# - start_from_task={task_id}
```

**Additional Variable**:
- `{task_id}`: Task to resume from (e.g., "2.1", "3.4")

**Use Case**: Resume after failure or interruption

---

## Monitor Progress

### View Checklist
```powershell
cat .olaf/work/project-tasks/task-checklist.md
```

### Watch Logs (Real-time)
```powershell
# Runner-specific logging goes here
```

---

## Prerequisites

Before executing (only if your plan requires it):

1. ✅ **Any required pre-steps completed** (e.g., Task 0.0 context extraction)
   
2. ✅ **AWS credentials configured**
   - Profile: bedrock
   - Region: us-east-1 (or your region)
   
3. ✅ **Runner available**
   - Your runner can accept `plan_file`, `checklist_path`, and optional resume markers

---

## Execution Flow

```
1. Bootstrap reads implementation plan ({output_file})
2. For each task (0.0 → N.M):
   a. Check if task prompt exists
   b. If NO → Spawn Agent A (generate prompt)
   c. Spawn Agent B (execute task)
   d. Verify outputs
   e. Update checklist
   f. If failed → STOP
3. Display completion summary
```

---

## Example

```powershell
# Example runner configuration
# plan_file=.olaf/work/staging/esdi/20251122-repo-scanner/IMPLEMENTATION-TASK-PLAN.md
# checklist_path=.olaf/work/project-tasks/task-checklist.md
# mode=auto
```

**Result**: Executes the plan described in `{output_file}`
