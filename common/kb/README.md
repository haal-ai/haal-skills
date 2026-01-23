# Task Registry Knowledge Base

## Purpose

Centralized registry tracking all reusable tasks across OLAF skills to:
- **Avoid duplication** - identify existing tasks before creating new ones
- **Enable reuse** - find common tasks that can be shared across skills
- **Track dependencies** - understand tool and template requirements
- **Maintain consistency** - standardize task patterns

## Files

### `task-registry.json`
Main registry containing:
- **Task metadata** - ID, name, description, category
- **Location tracking** - where task prompt files live
- **Dependency mapping** - tools, templates, state variables needed
- **Output specification** - what each task produces
- **Usage tracking** - which skills use each task
- **Reusability scoring** - how generally applicable each task is

### Schema: `../../schemas/task-registry.schema.json`
JSON Schema for validation and IDE support when editing registry (located in `~/.olaf/core/schemas/`).

## How to Use

### Before Creating a New Task

1. **Search the registry** for similar functionality:
   ```bash
   # Using the search tool
   python skills/common/tools/search-tasks.py category github
   
   # Or with jq directly
   jq '.tasks[] | select(.category=="github")' task-registry.json
   
   # Search by tags
   jq '.tasks[] | select(.tags[] | contains("timestamp"))' task-registry.json
   
   # Find high-reusability tasks
   jq '.tasks[] | select(.reusability_score >= 8)' task-registry.json
   ```

2. **Check if task exists** - if found, reuse it!
3. **If creating new task** - register it here after creation

### When Creating a New Skill

1. **Review common tasks** in `skills/common/tasks/`
2. **Check registry** for tasks matching your needs
3. **Reuse existing tasks** instead of duplicating
4. **Update registry** if you create skill-specific tasks that could be generalized

### Registering a New Task

Add entry to `tasks` array with:

```json
{
  "id": "your-task-id",
  "name": "Human Readable Name",
  "description": "What this task does in detail",
  "category": "environment|github|analysis|cleanup|user-interaction",
  "tags": ["relevant", "searchable", "tags"],
  "current_location": "skills/[skill-name]/tasks/[task-file].md",
  "used_in_skills": ["skill-name-1"],
  "dependencies": {
    "tools": [
      {
        "name": "script.py",
        "location": "skills/[skill]/tools/script.py",
        "description": "What it does"
      }
    ],
    "templates": [],
    "state_variables": ["context.some_var"]
  },
  "outputs": {
    "state_variables": ["context.output_var"],
    "files_created": [".olaf/work/staging/file-{placeholder}.txt"]
  },
  "reusability_score": 7,
  "notes": "Additional context"
}
```

### Reusability Scoring Guide

- **10** - Universal (timestamp, cleanup, generic file operations)
- **8-9** - Broadly applicable (GitHub API calls, common parsing)
- **6-7** - Domain-specific but reusable (PR selection, metadata analysis)
- **4-5** - Somewhat specialized (specific analyzers)
- **1-3** - Highly specialized (one-off tasks)

## Categories

- **environment** - System info, timestamps, environment detection
- **github** - GitHub API, PR/issue operations, repository interactions
- **analysis** - Data analysis, parsing, report generation
- **cleanup** - File cleanup, resource management
- **user-interaction** - Prompts, selections, confirmations

## Workflow Integration

When designing a new master skill:

1. Load `task-registry.json`
2. Search for tasks by category/tags
3. Identify reusable tasks for your chain
4. Reference existing task locations in your master prompt
5. Update registry if you create new reusable tasks

## Maintenance

- Update `last_updated` when making changes
- Increment `version` for significant updates (semver)
- Keep `used_in_skills` current when skills are added/removed
- Periodically review low-usage tasks for archival
