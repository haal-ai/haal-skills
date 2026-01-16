# Git Add Commit - Tutorial

## Getting Started

This tutorial walks you through using the git-add-commit skill to intelligently commit related changes.

## Prerequisites

- Git repository initialized
- Files modified/added in your working directory
- Understanding of what you changed (general scope)

## Step-by-Step Guide

### Step 1: Make Your Changes

Edit files in your project. For this example, let's say you updated a skill:

```bash
# Modified files
skills/create-prompt/prompts/create-prompt.md
skills/create-prompt/skill-manifest.json

# New files
skills/create-prompt/kb/prompt-structure-schema.md
skills/create-prompt/kb/file-modification-rules.md
```

### Step 2: Invoke the Skill

Tell the LLM you want to commit with a scope:

```
commit create-prompt
```

Or more explicitly:

```
Use git-add-commit skill to commit changes to create-prompt
```

### Step 3: Skill Discovers Related Files

The skill will:

1. **Run git status** to see all changes
2. **Filter by scope** "create-prompt"
3. **Read matched files** to find references
4. **Check git status** for referenced files
5. **Loop** until no new references found

**Output**:
```
📦 Dependency Analysis for 'create-prompt':

Initial matches (2):
  M create-prompt.md
  M skill-manifest.json

Referenced files found (2):
  ?? kb/prompt-structure-schema.md ← create-prompt.md:34
  ?? kb/file-modification-rules.md ← create-prompt.md:37

Total: 4 connected files
```

### Step 4: Review Dependency Graph

The skill shows you WHY files are related:

```
create-prompt.md
├─ References: kb/prompt-structure-schema.md
└─ References: kb/file-modification-rules.md

skill-manifest.json
└─ (no references)
```

### Step 5: Semantic Analysis

The skill reads all diffs and identifies:

```
🔍 Analysis Results:

Structural changes:
- Added KB loading section in create-prompt.md

Functional changes:
- Enforce structure validation before generation
- Add file safety rules

Knowledge base changes:
- New file: prompt-structure-schema.md (BOM requirements)
- New file: file-modification-rules.md (read-only rules)
```

### Step 6: Review Generated Commit Message

```
📝 Proposed Commit Message:
────────────────────────────────────────
refactor(create-prompt): enforce KB-driven structure validation

Added mandatory KB loading for canonical structure enforcement:
- prompt-structure-schema.md: minimal BOM requirements
- file-modification-rules.md: read-only vs editable file rules
- JSON schema validation enforcement

Strengthened validation:
- Enforce minimal BOM (prompts + docs only)
- Directory structure restrictions
- Schema compliance checks

Ensures prompts follow canonical structure and prevents
corruption of auto-generated files.
────────────────────────────────────────

Files (4):
  M skills/create-prompt/prompts/create-prompt.md
  M skills/create-prompt/skill-manifest.json
  ?? skills/create-prompt/kb/prompt-structure-schema.md
  ?? skills/create-prompt/kb/file-modification-rules.md
```

### Step 7: Approve or Modify

You have three options:

**Option 1: Approve (y)**
```
Proceed? (y/n/edit): y
```

**Option 2: Cancel (n)**
```
Proceed? (y/n/edit): n
❌ Commit cancelled
```

**Option 3: Edit (edit)**
```
Proceed? (y/n/edit): edit
Provide your commit message: [type your own]
```

### Step 8: Execution

If approved, the skill:

```bash
# Stages all files
git add skills/create-prompt/prompts/create-prompt.md \
        skills/create-prompt/skill-manifest.json \
        skills/create-prompt/kb/

# Commits with message
git commit -m "refactor(create-prompt): enforce KB-driven structure validation
..."
```

**Result**:
```
✅ Commit successful

Commit: abc1234
Branch: main
Files: 4 changed (120 insertions, 10 deletions)
```

## Advanced Usage

### Commit Specific File

```
commit vscode-extension/src/services/installationManager.ts
```

### Commit Entire Directory

```
commit vscode-extension/src/commands
```

### Include Untracked Files

```
commit create-prompt with new files
```

### Provide Custom Message

```
commit create-prompt with message "Add validation rules"
```

## Tips

1. **Use descriptive scopes**: "create-prompt" better than "core"
2. **Trust dependency chasing**: It finds connections you might miss
3. **Review the graph**: Understand why files are grouped
4. **Check the analysis**: Make sure it understood your changes
5. **Edit if needed**: The generated message is a starting point

## Troubleshooting

**Problem**: No files found
```
❌ No files match scope 'xyz'

Solution: Check spelling, try broader scope, or run git status manually
```

**Problem**: Too many files included
```
⚠️  Found 50 files - seems too broad

Solution: Use more specific scope like "folder/subfolder" instead of "folder"
```

**Problem**: Reference not resolved
```
⚠️  Could not resolve: ../missing/file.md

Solution: This is OK - reference might be to uncommitted file or incorrect path
```

## Next Steps

- Explore dependency graphs for your codebase
- Create conventional commits consistently
- Use for complex multi-file changes
- Integrate into your git workflow
