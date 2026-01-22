---
task_id: "search-common-tasks"
task_name: "Search for Reusable Common Tasks"
dependencies: ["context.skill_structure"]
conditions: []
---

# Search for Reusable Common Tasks

## Input Context
**Required Context Variables**: 
- `context.skill_structure`: Structure analysis from previous task
- `context.skill_content`: Full skill prompt content
**Required Files**: 
- `.olaf/work/staging/temporary/task-search-results.json` (created by search-tasks.py)
**Required Tools**: 
- `search-tasks.py` script at `skills/common/tools/search-tasks.py`

## Task Instructions

### Execute Common Task Search

1. **Identify Potential Common Patterns**:
   From skill content, look for these patterns:
   - Environment/timestamp retrieval
   - GitHub API calls (PR, issues, repos)
   - File cleanup operations
   - User input/selection prompts
   - Data extraction/parsing
   - Report generation

2. **Search Task Registry by Category**:
   ```bash
   # Search for highly reusable tasks
   python skills/common/tools/search-tasks.py reusable 8
   
   # Search specific categories based on skill needs
   python skills/common/tools/search-tasks.py category environment
   python skills/common/tools/search-tasks.py category github
   python skills/common/tools/search-tasks.py category cleanup
   ```
   
   **Note**: Script outputs to terminal AND saves results to:
   `.olaf/work/staging/temporary/task-search-results.json`

3. **Read Search Results from File**:
   - Read `.olaf/work/staging/temporary/task-search-results.json`
   - Parse JSON to extract task list
   - Extract relevant fields: id, name, location, reusability_score, description

4. **Match Common Tasks to Skill Needs**:
   - Compare skill workflow steps with available common tasks
   - Identify which common tasks can be reused
   - Note any tasks that need to be created

5. **Create Reusability Map**:
```markdown
**Common Tasks Available for Reuse**:
- ✓ retrieve-timestamp (environment)
- ✓ cleanup-extraction-files (cleanup)
- ✓ [other matching tasks]

**Tasks Needed (not in common)**:
- [skill-specific task 1]
- [skill-specific task 2]
```

## Output Requirements

**State Updates**:
- `context.common_tasks_found`: Array of common task objects
  ```json
  [
    {
      "id": "retrieve-timestamp",
      "location": "skills/common/tasks/retrieve-timestamp.md",
      "match_reason": "Skill needs environment info"
    }
  ]
  ```
- `context.common_tasks_count`: Number of reusable tasks found
- `context.new_tasks_needed`: Estimated count of new tasks to create
- `task_status.search-common-tasks`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- `context.common_tasks_found` will guide task boundary identification
- Will help determine which tasks to extract vs. reuse
