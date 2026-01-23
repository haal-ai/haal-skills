---
task_id: "update-task-registry"
task_name: "Update Task Registry"
dependencies: ["context.extracted_tasks", "context.task_boundaries"]
conditions: []
---

# Update Task Registry with New Tasks

## Input Context
**Required Context Variables**: 
- `context.skill_name`: Name of skill
- `context.task_boundaries`: Task definitions
- `context.extracted_tasks`: Created task file paths
- `context.reuse_count`: Number of common tasks reused
**Required Files**: 
- `skills/common/kb/task-registry.json`
**Required Tools**: JSON editing

## Task Instructions

### Add New Tasks to Registry

1. **Read Current Registry**:
   - Load `skills/common/kb/task-registry.json`
   - Parse JSON structure

2. **For Each New Task** (skip common tasks):
   
   Create registry entry:
   ```json
   {
     "id": "task-id",
     "name": "Task Name",
     "description": "What this task does (from task definition)",
     "category": "environment|github|analysis|cleanup|user-interaction",
     "tags": ["tag1", "tag2"],
     "current_location": "skills/[skill-name]/tasks/[task-id].md",
     "used_in_skills": ["[skill-name]"],
     "dependencies": {
       "tools": [],
       "templates": [],
       "state_variables": ["context.input_var"]
     },
     "outputs": {
       "state_variables": ["context.output_var"],
       "files_created": []
     },
     "reusability_score": 5,
     "notes": "Created from [skill-name] conversion"
   }
   ```

3. **Determine Reusability Score**:
   - **10**: Universal (no skill-specific logic)
   - **8-9**: Broadly applicable (generic patterns)
   - **6-7**: Domain-specific but reusable
   - **4-5**: Somewhat specialized
   - **1-3**: Highly skill-specific

4. **Assign Appropriate Category**:
   - `environment`: System/env detection
   - `github`: GitHub API operations
   - `analysis`: Data analysis/parsing
   - `cleanup`: Resource cleanup
   - `user-interaction`: User prompts/input

5. **Update Registry File**:
   - Add new task entries to `tasks` array
   - Update `last_updated` field to current date
   - Validate JSON syntax

6. **Update Usage for Reused Common Tasks**:
   - Find common tasks in registry
   - Add current skill to `used_in_skills` array

## Output Requirements

**State Updates**:
- `context.registry_updated`: true
- `context.tasks_registered`: Count of tasks added to registry
- `context.common_tasks_usage_updated`: Count of common task usages updated
- `task_status.update-task-registry`: "completed"

**Files Created**: None (existing file modified)

**Files Modified**:
- `skills/common/kb/task-registry.json`

**Context Passed to Next Tasks**:
- Registry status for final summary
