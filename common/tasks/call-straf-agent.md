---
task_id: "call-straf-agent"
task_name: "Execute STRAF Agent" 
dependencies: []
conditions: []
---

# Call STRAF Agent

## Input Context
**Required State Variables**: 
- `context.straf_prompt_full_path`: Absolute path to prompt file
- `context.straf_context_file_path`: Path to file containing code content
- `context.project_root`: Absolute path to project root directory  
- `context.timestamp`: Session timestamp for output file naming

**Required Files**: Prompt file and context file
**Required Tools**: STRAF wrapper (`olaf_strands_wrapper.py`)

## Task Instructions

### Step 1: Prepare Output Location

Set output path: `.olaf/work/staging/straf-output-{context.timestamp}.txt`

### Step 2: Execute STRAF (Interactive Mode with Polling)

NOTE: Wrapper always spawns background. "Interactive" = poll until done.

1. **Execute wrapper**:
   ```bash
   python .olaf/core/agentic/straf/olaf_strands_wrapper.py \
     --prompt "{context.straf_prompt_full_path}" \
     --context-file "{context.straf_context_file_path}" \
     --output "{output_path}" \
     --project-root "{context.project_root}" \
     --aws-profile bedrock
   ```

2. **Parse task ID**: Extract from output line "Task ID: [id]"

3. **Poll for completion** (10s intervals, max 180s):
   ```bash
   python .olaf/core/agentic/straf/olaf_strands_wrapper.py --status --task-id {task_id}
   ```
   Continue until status == "completed"

4. **Read results**: From stdout log file `{task_id}_stdout.log`

## Output Requirements
- `context.straf_result`: Agent output
- `context.straf_task_id`: Task ID
- `context.straf_output_file`: Output file path
- `task_status.call-straf-agent`: "completed"
