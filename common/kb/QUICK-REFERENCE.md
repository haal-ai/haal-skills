# Task Registry Quick Reference

## Quick Search Commands

```bash
# List all tasks
python skills/common/tools/search-tasks.py list

# Search by category
python skills/common/tools/search-tasks.py category github
python skills/common/tools/search-tasks.py category environment

# Search by tag
python skills/common/tools/search-tasks.py tag timestamp
python skills/common/tools/search-tasks.py tag api

# Search by keyword
python skills/common/tools/search-tasks.py keyword "pull request"
python skills/common/tools/search-tasks.py keyword cleanup

# Find highly reusable tasks (score >= 8)
python skills/common/tools/search-tasks.py reusable
python skills/common/tools/search-tasks.py reusable 10
```

## PowerShell Aliases (Optional Setup)

Add to your PowerShell profile for convenience:

```powershell
# Add to $PROFILE
function Search-OlafTasks {
    param([string]$Type, [string]$Query)
    python skills/common/tools/search-tasks.py $Type $Query
}

Set-Alias -Name olaf-tasks -Value Search-OlafTasks

# Usage:
# olaf-tasks category github
# olaf-tasks tag timestamp
```

## Manual JSON Queries

Using `jq` (if installed):

```bash
# Get all GitHub tasks
jq '.tasks[] | select(.category=="github")' task-registry.json

# Get tasks by tag
jq '.tasks[] | select(.tags[] | contains("pull-request"))' task-registry.json

# Get highly reusable tasks
jq '.tasks[] | select(.reusability_score >= 8)' task-registry.json

# Get task by ID
jq '.tasks[] | select(.id=="retrieve-timestamp")' task-registry.json

# List all categories
jq '.categories | keys' task-registry.json

# Count tasks per category
jq '[.tasks[].category] | group_by(.) | map({category: .[0], count: length})' task-registry.json
```

## Adding New Tasks - Template

```json
{
  "id": "your-new-task",
  "name": "Your Task Name",
  "description": "Detailed description of what this task does",
  "category": "environment|github|analysis|cleanup|user-interaction",
  "tags": ["tag1", "tag2"],
  "current_location": "skills/[skill-name]/tasks/your-task.md",
  "used_in_skills": ["skill-name"],
  "dependencies": {
    "tools": [],
    "templates": [],
    "state_variables": []
  },
  "outputs": {
    "state_variables": [],
    "files_created": []
  },
  "reusability_score": 7,
  "notes": "Additional notes"
}
```

## Task Discovery Workflow

1. **Before creating a task**: Search for similar functionality
2. **Check common tasks**: Look in `skills/common/tasks/`
3. **Search registry**: Use search tools above
4. **Reuse if found**: Reference existing task in your skill
5. **Create if needed**: Add new task and register it

## Categories Explained

- **environment** - System detection, timestamps, env vars
- **github** - API calls, PR/issues, repo operations  
- **analysis** - Data parsing, report generation
- **cleanup** - File/resource cleanup operations
- **user-interaction** - Prompts, confirmations, selections
