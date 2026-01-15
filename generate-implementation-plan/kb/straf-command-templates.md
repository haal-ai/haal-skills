# STRAF Command Templates

## Overview

Standard templates for generating STRAF agent commands in implementation plans.

---

## Basic Command Structure

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "{prompt_path}" `
  --context "{context_variables}" `
  --tool-mode {mode} `
  --aws-profile bedrock
```

**Parameters**:
- `prompt`: Path to prompt file (relative or absolute)
- `context`: Comma-separated key=value pairs
- `tool-mode`: `standard` | `auto` | `minimal`
- `aws-profile`: AWS profile name (usually `bedrock`)

---

## Tool Modes

### Standard Mode
**Usage**: Most tasks (default)
**Behavior**: Propose-Act protocol, requires user approval for tool calls
```powershell
--tool-mode standard
```

### Auto Mode
**Usage**: Bootstrap orchestrator, autonomous agents
**Behavior**: Auto-approves all tool calls, fully autonomous
```powershell
--tool-mode auto
```

### Minimal Mode
**Usage**: Simple analysis tasks, read-only operations
**Behavior**: Limited tool access, fast execution
```powershell
--tool-mode minimal
```

---

## Template 1: Phase 0 Setup Tasks

### Task 0.0: Extract Task Contexts
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md" `
  --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md,skill_path=${skill_path}" `
  --tool-mode standard `
  --aws-profile bedrock
```

### Task 0.1: Create Skill Structure
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${skill_path}/tasks/setup/create-skill-structure.md" `
  --context "skill_name=${skill_name},target_path=${skill_path}" `
  --tool-mode standard `
  --aws-profile bedrock
```

### Task 0.2: Create Master Coordinator
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${skill_path}/tasks/setup/create-master-coordinator.md" `
  --context "skill_name=${skill_name},layers=${layer_count},pattern=sequential,output_base=${output_dir}" `
  --tool-mode standard `
  --aws-profile bedrock
```

---

## Template 2: Layer Implementation Tasks

### General Layer Task Pattern
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${skill_path}/tasks/layer-${layer_num}/${task_name}.md" `
  --context "skill_path=${skill_path},layer_number=${layer_num},input_file=${input_artifact}" `
  --tool-mode standard `
  --aws-profile bedrock
```

### With Context File (Post Task 0.0)
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${skill_path}/tasks/layer-${layer_num}/${task_name}.md" `
  --context "task_id=${task_id},context_file=${skill_path}/tasks/contexts/task-${task_id}-context.md,skill_path=${skill_path}" `
  --tool-mode auto `
  --aws-profile bedrock
```

---

## Template 3: Bootstrap Orchestrator Execution

### Full Execution
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md,checklist_path=.olaf/work/project-tasks/task-checklist.md" `
  --tool-mode auto `
  --aws-profile bedrock
```

### Resume from Specific Task
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md,checklist_path=.olaf/work/project-tasks/task-checklist.md,start_from_task=2.1" `
  --tool-mode auto `
  --aws-profile bedrock
```

---

## Template 4: Universal Prompt Generator

**Usage**: Generate task prompts dynamically during bootstrap

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/universal-task-prompt-generator.md" `
  --context "task_id=${task_id},context_file=${skill_path}/tasks/contexts/task-${task_id}-context.md,skill_path=${skill_path}" `
  --tool-mode auto `
  --aws-profile bedrock
```

---

## Context Variable Patterns

### Common Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `skill_path` | Path to skill being built | `competencies/onboard-me` |
| `skill_name` | Name of skill | `onboard-me` |
| `output_dir` | Output directory | `.olaf/work/staging/esdi/20251122-repo-scanner` |
| `task_id` | Task identifier | `1.1`, `2.3` |
| `layer_num` | Layer number | `1`, `2`, `3` |
| `input_file` | Input artifact path | `${output_dir}/design.md` |
| `bootstrap_doc` | Implementation plan path | `${output_dir}/IMPLEMENTATION-TASK-PLAN.md` |
| `checklist_path` | Task tracking file | `.olaf/work/project-tasks/task-checklist.md` |

### Phase-Specific Variables

#### Phase 0 (Setup)
```
skill_name=onboard-me
target_path=competencies/onboard-me
layers=5
pattern=sequential
```

#### Phase 1+ (Layer Implementation)
```
skill_path=competencies/onboard-me
layer_number=1
input_file=.olaf/data/product/repo-name/design.md
```

#### Bootstrap Orchestrator
```
bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md
checklist_path=.olaf/work/project-tasks/task-checklist.md
start_from_task=1.1  # Optional
```

---

## Variable Interpolation Rules

### Windows PowerShell
```powershell
# Use ${var} syntax
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --context "skill_path=${skill_path},output=${output_dir}/design.md"
```

### Unix/Linux Bash
```bash
# Use $var or ${var} syntax
python ./.olaf/core/agentic/straf/olaf_strands_agent.py \
  --context "skill_path=$skill_path,output=$output_dir/design.md"
```

### Literal Values (No Interpolation)
```powershell
# Use actual values when variables not set
--context "skill_path=competencies/onboard-me,layer_number=1"
```

---

## Multi-Line Commands

### PowerShell (Backtick)
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "path/to/prompt.md" `
  --context "var1=value1,var2=value2,var3=value3" `
  --tool-mode standard `
  --aws-profile bedrock
```

### Bash (Backslash)
```bash
python ./.olaf/core/agentic/straf/olaf_strands_agent.py \
  --prompt "path/to/prompt.md" \
  --context "var1=value1,var2=value2,var3=value3" \
  --tool-mode standard \
  --aws-profile bedrock
```

---

## Timeout Configuration

```powershell
# Default timeout: 1800 seconds (30 minutes)
# For Task 0.0 with condensed contexts: 600 seconds (10 minutes)

python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md" `
  --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md" `
  --tool-mode standard `
  --aws-profile bedrock `
  --timeout 600  # Optional: Override default
```

---

## Error Handling

### Retry Pattern
```powershell
# Retry failed task with same command
# Check logs in: .olaf/logs/straf_agent_*.log

python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${failed_task_prompt}" `
  --context "${failed_task_context}" `
  --tool-mode standard `
  --aws-profile bedrock
```

### Debug Mode
```powershell
# Add verbose logging
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "path/to/prompt.md" `
  --context "debug=true,${other_context}" `
  --tool-mode standard `
  --aws-profile bedrock `
  --verbose  # Optional: Enable verbose output
```

---

## Quick Reference

### Minimal Command
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py --prompt "path/to/prompt.md" --context "key=value" --tool-mode standard --aws-profile bedrock
```

### Full Command with All Options
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "path/to/prompt.md" `
  --context "var1=value1,var2=value2" `
  --tool-mode auto `
  --aws-profile bedrock `
  --timeout 600 `
  --verbose
```
