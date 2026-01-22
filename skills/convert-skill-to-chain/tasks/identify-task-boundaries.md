---
task_id: "identify-task-boundaries"
task_name: "Identify Task Boundaries"
dependencies: ["context.skill_structure", "context.common_tasks_found"]
conditions: []
---

# Identify Task Boundaries

## Input Context
**Required Context Variables**: 
- `context.skill_content`: Full skill prompt content
- `context.skill_structure`: Structure analysis
- `context.common_tasks_found`: Available common tasks
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Analyze and Define Task Boundaries

1. **Review Skill Workflow**:
   - Read through skill content line by line
   - Identify distinct logical units
   - Look for natural separation points

2. **Apply Task Boundary Principles**:
   Each task should:
   - **Do ONE thing** (single responsibility)
   - **Have clear inputs** (context variables or files)
   - **Produce clear outputs** (new context or files)
   - **Be independently testable**
   - **Not reference future tasks**

3. **Common Task Patterns to Extract**:
   - **Initialization**: Environment setup, timestamp
   - **User Input**: Selections, confirmations
   - **Data Retrieval**: API calls, file reads
   - **Data Processing**: Parsing, transformation
   - **Analysis**: Code review, validation
   - **Output Generation**: Reports, summaries
   - **Cleanup**: Temporary file removal

4. **Create Task Chain Design**:
```yaml
Proposed Task Chain:
  Task 0: retrieve-timestamp [COMMON]
  Task 1: [user-selection-task]
  Task 2: [data-extraction-task]
  Task 3: [data-processing-task]
  Task 4: [analysis-task]
  Task 5: [report-generation-task]
  Task 6: cleanup-extraction-files [COMMON]
```

5. **Define Task Metadata for Each**:
   For each identified task:
   ```markdown
   - **Task ID**: kebab-case-name
   - **Task Name**: Human readable
   - **Purpose**: Single sentence
   - **Inputs**: Required context variables
   - **Outputs**: Created context variables
   - **Dependencies**: Which tasks must run first
   - **Type**: common-reuse / new-skill-specific
   ```

## Output Requirements

**State Updates**:
- `context.task_boundaries`: Array of task definitions
  ```json
  [
    {
      "task_id": "retrieve-timestamp",
      "task_name": "Environment Info",
      "type": "common-reuse",
      "location": "../common/tasks/retrieve-timestamp.md",
      "inputs": [],
      "outputs": ["context.timestamp"]
    },
    {
      "task_id": "select-target",
      "task_name": "Select Target",
      "type": "new",
      "inputs": ["context.timestamp"],
      "outputs": ["context.target_name"]
    }
  ]
  ```
- `context.task_count`: Total number of tasks in chain
- `context.reuse_count`: Number of common tasks reused
- `context.new_count`: Number of new tasks to create
- `task_status.identify-task-boundaries`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- `context.task_boundaries` will drive task extraction
