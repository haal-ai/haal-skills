# Bootstrap Execution Command Template

## Full Autonomous Execution

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc={output_file},checklist_path=.olaf/work/project-tasks/task-checklist.md" `
  --tool-mode auto `
  --aws-profile bedrock
```

**Variables**:
- `{output_file}`: Path to IMPLEMENTATION-TASK-PLAN.md
- `{checklist_path}`: Task progress tracker (default: `.olaf/work/project-tasks/task-checklist.md`)

**Behavior**:
- Sequential execution of ALL tasks
- Multi-agent orchestration (Agent A: generate prompts, Agent B: execute)
- Autonomous (no human intervention)
- Error handling (stops on failure)
- Progress tracking (updates checklist)

---

## Resume from Specific Task

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc={output_file},checklist_path=.olaf/work/project-tasks/task-checklist.md,start_from_task={task_id}" `
  --tool-mode auto `
  --aws-profile bedrock
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
Get-Content .olaf/logs/straf_agent_*.log -Wait
```

---

## Prerequisites

Before executing:

1. ✅ **Task 0.0 completed manually**
   - Generates context files in `{skill_path}/tasks/contexts/`
   - Required for universal prompt generator
   
2. ✅ **AWS credentials configured**
   - Profile: bedrock
   - Region: us-east-1 (or your region)
   
3. ✅ **STRAF agent operational**
   - Path: `.olaf/core/agentic/straf/olaf_strands_agent.py`
   - Tested and working

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
# Full execution for repo-scanner skill
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=.olaf/work/staging/esdi/20251122-repo-scanner/IMPLEMENTATION-TASK-PLAN.md,checklist_path=.olaf/work/project-tasks/task-checklist.md" `
  --tool-mode auto `
  --aws-profile bedrock
```

**Result**: Fully implemented repo-scanner skill in `skills/repo-scanner/`
