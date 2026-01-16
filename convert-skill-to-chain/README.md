# Convert Skill to Master Chain Pattern

## Overview

This skill automates the conversion of existing OLAF skills to the **master-chain pattern** - a structured approach where complex skills are broken down into isolated, reusable task prompts coordinated by a master prompt.

## What It Does

Converts a monolithic skill prompt into:
- **Master coordinator** - Orchestrates task execution
- **Individual task prompts** - Isolated, single-responsibility units
- **Task registry entries** - Tracks reusable tasks
- **Conversion summary** - Documents the transformation

## Key Features

- **Discovers reusable tasks** using the task registry
- **Reuses common tasks** (like `retrieve-timestamp`, cleanup)
- **Creates skill-specific tasks** for unique functionality
- **Updates task registry** automatically
- **Follows master-chain protocol** exactly

## Task Chain

```
Task 0: Retrieve environment info (common task)
Task 1: Select skill to convert
Task 2: Backup original skill prompt
Task 3: Analyze existing skill structure
Task 4: Search for reusable common tasks
Task 5: Identify task boundaries
Task 6: Extract individual tasks
Task 7: Create master coordinator prompt
Task 8: Update task registry
Task 9: Generate conversion summary
```

## Usage

```
Convert skill [skill-name] to master chain pattern
```

### Examples

```
Convert skill review-code to master chain pattern
Use convert-skill-to-chain for analyze-business-requirements
Help me refactor the create-feature-for-pr skill
```

## Benefits of Master Chain Pattern

### Before (Monolithic)
```markdown
# review-code.md (500+ lines)
- All instructions in one file
- Hard to reuse components
- Difficult to test individual steps
- Complex to maintain
```

### After (Master Chain)
```markdown
# review-code.md (master coordinator ~200 lines)
- Task chain definition
- Execution protocol
- Context management

# tasks/task-1.md (~50 lines each)
# tasks/task-2.md
# tasks/task-3.md
- Focused, single-purpose
- Reusable across skills
- Easy to test
- Clear boundaries
```

## What Gets Created

### Directory Structure
```
skills/[skill-name]/
├── prompts/
│   └── [skill-name].md          # Master coordinator (created/updated)
├── tasks/
│   ├── task-1.md                # New task files
│   ├── task-2.md
│   └── task-3.md
└── skill-manifest.json           # Updated
```

### Task Registry Updates
```json
{
  "tasks": [
    {
      "id": "new-task-from-conversion",
      "name": "Task Name",
      "current_location": "skills/[skill-name]/tasks/new-task.md",
      "used_in_skills": ["[skill-name]"],
      "reusability_score": 7,
      ...
    }
  ]
}
```

## Task Isolation Principles

Each extracted task must:
1. **Do ONE thing** - Single responsibility
2. **Clear inputs** - Defined context variables
3. **Clear outputs** - What it produces
4. **No forward references** - Doesn't mention future tasks
5. **Independently testable** - Can run in isolation

## Example: review-github-pr

This skill itself was converted using the master-chain pattern and serves as the reference example.

**Before**: One large prompt (~800 lines)

**After**:
- Master coordinator: `review-github-pr.md`
- 11 task prompts in `tasks/` and `common/tasks/`
- Task registry entries for reusable components
- Clear task chain with dependencies

## Dependencies

### Tools
- `search-tasks.py` - Discover reusable tasks
- `get-env.py` - Environment information

### Knowledge Bases
- `task-registry.json` - Central task registry

## Output

- **Creates**: Task markdown files, master coordinator
- **Modifies**: Task registry JSON
- **Reports**: Conversion summary with statistics

## Quality Checklist

After conversion, verify:
- [ ] Original skill backed up in backups/ directory
- [ ] Tasks have clear input/output definitions
- [ ] No forward references between tasks
- [ ] Common tasks properly referenced
- [ ] Registry updated with new tasks
- [ ] All task files have proper frontmatter
- [ ] Context variables flow correctly

## Related Skills

- `review-github-pr` - Reference implementation
- `use-skill` - Execute converted skills
- Task registry tools in `common/kb/`

## Notes

- This skill is **self-demonstrating** - it uses the pattern it creates
- Encourages **task reusability** across skills
- Makes skills **easier to maintain** and test
- Promotes **consistent structure** across OLAF framework
