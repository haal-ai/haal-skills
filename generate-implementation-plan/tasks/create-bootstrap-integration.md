---
name: create-bootstrap-integration
description: "Task 4 - Generate bootstrap orchestrator configuration"
task_id: 4
protocol: Propose-Act
---

# Task 4: Create Bootstrap Integration

## Objective

Generate the bootstrap orchestrator execution command and integration instructions for autonomous task execution.

## Context Variables

**Required**:
- `output_file`: Path to IMPLEMENTATION-TASK-PLAN.md
- `skill_path`: Target skill path

**Optional**:
- `checklist_path`: Task tracking file (default: `.olaf/work/project-tasks/task-checklist.md`)

**Outputs**:
- `bootstrap_command`: Bootstrap execution command
- `bootstrap_instructions`: Integration documentation

## Execution Steps

### Step 1: Generate Bootstrap Command

**Template**:
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_file},checklist_path=${checklist_path}" `
  --tool-mode auto `
  --aws-profile bedrock
```

**Variables**:
- `bootstrap_doc`: Path to IMPLEMENTATION-TASK-PLAN.md (this file)
- `checklist_path`: Task progress tracker
- `tool-mode`: `auto` (fully autonomous multi-agent orchestration)

### Step 2: Generate Resume Command

**Template** (for resuming from specific task):
```powershell
# Resume from Task 2.1 (example)
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_file},checklist_path=${checklist_path},start_from_task=2.1" `
  --tool-mode auto `
  --aws-profile bedrock
```

### Step 3: Create Integration Instructions

```markdown
## Bootstrap Execution

### Full Autonomous Execution

Execute ALL tasks sequentially via bootstrap orchestrator:

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_file},checklist_path=.olaf/work/project-tasks/task-checklist.md" `
  --tool-mode auto `
  --aws-profile bedrock
```

**What Happens**:
1. Bootstrap orchestrator reads this implementation plan
2. For each task (0.0 → {total_tasks}):
   - Checks if task prompt exists
   - If NO → Spawns Agent A (universal-task-prompt-generator.md)
   - Spawns Agent B (executes generated/existing prompt)
   - Verifies outputs against success criteria
   - Updates checklist with completion status
   - If task fails → STOPS and reports error
3. Displays final summary of completed implementation

**Execution Time**: {estimated_total_time} minutes
**Autonomous**: YES (tool-mode=auto, no human intervention)

### Resume from Specific Task

If execution fails or is interrupted:

```powershell
# Resume from Task {example_task_id}
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_file},checklist_path=.olaf/work/project-tasks/task-checklist.md,start_from_task={example_task_id}" `
  --tool-mode auto `
  --aws-profile bedrock
```

Replace `{example_task_id}` with task ID from checklist (e.g., "2.1", "3.4")

### Monitor Progress

Track execution via checklist:

```powershell
# View task checklist
cat .olaf/work/project-tasks/task-checklist.md

# Watch logs (real-time)
Get-Content .olaf/logs/straf_agent_*.log -Wait
```

---

## How Bootstrap Orchestrator Works

The bootstrap-orchestrator.md follows this pattern:

```
FOR each phase (0 through {total_phases}):
  FOR each task in phase:
    
    STEP 0: Check if prompt exists
      Path: ${skill_path}/tasks/layer-{N}/{task-name}.md
      IF exists → Skip Agent A, use existing
      IF NOT exists → Proceed to Agent A
    
    STEP 1: Spawn Agent A (Conditional)
      ONLY IF prompt doesn't exist
      Prompt: universal-task-prompt-generator.md
      Context: task_id={task_id},context_file=${skill_path}/tasks/contexts/task-{task_id}-context.md
      Output: Generated task prompt
      WAIT for completion
    
    STEP 2: Spawn Agent B (Execute Task)
      Prompt: ${skill_path}/tasks/layer-{N}/{task-name}.md (from Agent A or existing)
      Context: {task_specific_context}
      Output: Task deliverables
      WAIT for completion
    
    STEP 3: Verify Success
      Check outputs match success criteria
      IF failed → STOP execution, report error
      IF success → Update checklist, proceed
  
  NEXT task
NEXT phase

Display final summary
```

**Key Features**:
- ✅ **Sequential execution**: Each task completes before next starts
- ✅ **Automatic prompt generation**: Creates prompts if missing
- ✅ **Error handling**: Stops on failure, allows resume
- ✅ **Progress tracking**: Updates checklist in real-time
- ✅ **Autonomous**: No human intervention required

---

## Prerequisites

Before running bootstrap:

1. ✅ **Task 0.0 completed manually** (extract task contexts)
   - Generates ${skill_path}/tasks/contexts/*.md files
   - Enables universal prompt generator
   
2. ✅ **Implementation plan validated** (this file)
   - All tasks documented
   - STRAF commands correct
   - Dependencies logical

3. ✅ **AWS credentials configured**
   - Profile: bedrock
   - Region: us-east-1 (or configured)

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

Execution Command:
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_file},checklist_path=.olaf/work/project-tasks/task-checklist.md" `
  --tool-mode auto `
  --aws-profile bedrock

Orchestration Pattern:
  ✅ Sequential execution (Phase 0 → Phase {last_phase})
  ✅ Multi-agent (Agent A: generate prompts, Agent B: execute)
  ✅ Autonomous (tool-mode=auto, no human intervention)
  ✅ Resumable (from any task ID)
  ✅ Progress tracking (via task-checklist.md)

Estimated Execution:
  Total Tasks: {total_tasks}
  Estimated Time: {estimated_total_time} minutes (~{hours} hours)

Prerequisites:
  ⚠️ Run Task 0.0 manually FIRST (extract task contexts)
  ✅ AWS profile 'bedrock' configured
  ✅ STRAF agent operational

Resume Command (if needed):
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --context "...,start_from_task=X.Y" `
  --tool-mode auto

APPROVE to include bootstrap integration in plan
ADJUST if modifications needed
```

## Success Criteria

✅ Bootstrap command uses bootstrap-orchestrator.md
✅ Context variables reference ${output_file} and ${checklist_path}
✅ Tool mode set to `auto` (autonomous execution)
✅ Resume command pattern documented
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
  "bootstrap_command": "python .\\.olaf\\core\\agentic\\straf\\olaf_strands_agent.py ...",
  "resume_command": "python .\\.olaf\\core\\agentic\\straf\\olaf_strands_agent.py ... --context \"...,start_from_task=X.Y\"",
  "estimated_time_minutes": 470,
  "estimated_time_hours": 7.8,
  "prerequisites": [
    "Task 0.0 executed manually",
    "AWS bedrock profile configured",
    "STRAF agent operational"
  ]
}
```

## Next Task

→ Task 5: generate-plan-document.md (assembles final IMPLEMENTATION-TASK-PLAN.md)
