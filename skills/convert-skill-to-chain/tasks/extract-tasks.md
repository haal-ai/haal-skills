---
task_id: "extract-tasks"
task_name: "Extract Individual Tasks"
dependencies: ["context.task_boundaries"]
conditions: []
---

# Extract Individual Tasks

## Input Context
**Required Context Variables**: 
- `context.skill_name`: Name of skill being converted
- `context.skill_path`: Path to skill directory
- `context.skill_content`: Full original skill content
- `context.task_boundaries`: Defined task breakdown
**Required Files**: Original skill prompt
**Required Tools**: File creation capabilities

## Task Instructions

### Create Task Files

1. **Create Tasks Directory** (if needed):
   ```
   skills/[skill-name]/tasks/
   ```

2. **For Each New Task** (skip common tasks):
   
   **a) Extract Relevant Content**:
   - Find the section(s) in original skill that match this task
   - Extract instructions, context, and requirements
   - Identify input/output specifications

   **b) Create Task File**:
   - File name: `[task-id].md`
   - Location: `skills/[skill-name]/tasks/[task-id].md`

   **c) Use Task Template**:
   ```markdown
   ---
   task_id: "[task-id]"
   task_name: "[Task Name]"
   dependencies: ["context.var1", "context.var2"]
   conditions: []
   ---

   # [Task Name]

   ## Input Context
   **Required Context Variables**: 
   - `context.var1`: Description
   **Required Files**: [list or "None"]
   **Required Tools**: [list or "None"]

   ## Task Instructions

   ### [Main Instruction Section]

   1. **Step 1**: Description
   2. **Step 2**: Description
   
   [Detailed instructions extracted from original skill]

   ## Output Requirements

   **State Updates**:
   - `context.output_var`: Description
   - `task_status.[task-id]`: "completed"

   **Files Created**: 
   - [path] or "None"

   **Context Passed to Next Tasks**:
   - [What subsequent tasks need]
   ```

   **d) Ensure Task Isolation**:
   - Remove references to other tasks
   - Focus only on single responsibility
   - Clear input/output boundaries
   - No forward-looking statements

3. **Track Created Files**:
   Keep list of all created task files

## Output Requirements

**State Updates**:
- `context.extracted_tasks`: Array of created task file paths
  ```json
  [
    "skills/skill-name/tasks/task-1.md",
    "skills/skill-name/tasks/task-2.md"
  ]
  ```
- `context.extraction_count`: Number of files created
- `task_status.extract-tasks`: "completed"

**Files Created**: 
- Multiple task markdown files in `skills/[skill-name]/tasks/`

**Context Passed to Next Tasks**:
- `context.extracted_tasks` will be listed in master coordinator
- Will be registered in task registry
