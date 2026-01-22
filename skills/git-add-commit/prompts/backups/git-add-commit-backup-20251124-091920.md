---
name: git-add-commit
description: Enhanced P1 skill migrated from git-assistant competency pack with comprehensive reference detection
tags: [developer-workflow, git-operations, version-control, commit-automation, staging-analysis]
aliases: [git add commit, git-add-commit skill]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

# Git Add and Commit - Git Assistant Competency

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read the full ~/reference/.condensed/olaf-framework-condensed.md.

## Purpose

Intelligently handle git add and commit operations with proper staging analysis, meaningful commit messages, and staged file conflict resolution.

## Input Parameters

### Commit Message Mode
- **message**: string - (Optional) Pre-defined commit message. If provided, skip message generation
- **message_template**: enum[conventional|descriptive|minimal] - (Optional) Commit message style (default: descriptive)

### Staging Control
- **files**: array[string] - (Optional) Specific files to stage. If omitted, stages all changes
- **skill_name**: string - (Optional) Stage all files belonging to a specific skill (e.g., "git-add-commit", "review-code")
- **pattern**: string - (Optional) Glob pattern to match files (e.g., "*.md", "src/**/*.ts")
- **include_untracked**: boolean - (Optional) Whether to include untracked files (default: true)
- **staged_action**: enum[commit|add-all|cancel] - (Optional) Action when files already staged (default: ask user)

### Safety & Validation
- **skip_safety_checks**: boolean - (Optional) Skip large file and sensitive data warnings (default: false)
- **auto_confirm**: boolean - (Optional) Skip confirmation prompts (default: false)
- **dry_run**: boolean - (Optional) Show what would be done without executing (default: false)

### Message Generation Options
- **context**: string - (Optional) Additional context for commit message generation
- **commit_type**: enum[feature|fix|docs|config|refactor|test] - (Optional) Type hint for message generation

**DEFAULT BEHAVIOR**: If no parameters provided, analyze git status and interactively guide user through staging and commit.

## Context
- User wants to add and commit changes
- Need to check for already staged files
- Generate meaningful commit messages based on changes
- Handle mixed staging scenarios properly

## Instructions

### 1. Analyze Current Git State

Check git status to understand the current situation:

```bash
git status --porcelain
```

Parse the output to identify staged files, unstaged files, and untracked files.

**If skill_name is provided:**
1. Determine skill location pattern: `skills/{skill_name}/`
2. Filter changed files to only those matching the skill directory
3. Include all files under that skill's directory structure

**If pattern is provided:**
1. Use git status to get all changed files
2. Filter files matching the glob pattern
3. Present filtered list to user for confirmation

### 2. Handle Mixed Staging Scenarios

**Scenario A: Only unstaged/untracked files**
- Proceed with git add and commit

**Scenario B: Only staged files**
- Generate commit message for staged files
- Ask user about committing staged files first

**Scenario C: Both staged and unstaged files**
- Present options to user:
  1. Commit staged files first, then handle unstaged
  2. Add unstaged to staging and commit everything together
  3. Cancel to review changes

### 3. Generate Meaningful Commit Messages

Analyze changes and create context-aware commit messages:
- Single file: "Update [filename]: [description]"
- Multiple files: "Update [area]: [description]"
- New features: "Add [functionality]"
- Bug fixes: "Fix [issue]"
- Documentation: "Update documentation"
- Configuration: "Update configuration"

### 4. Interactive Workflow
- Generate initial commit message
- Show proposed message to user
- Allow user to approve, modify, or provide their own
- Execute with confirmation

### 5. Safety Checks
- Warn about large files (>10MB)
- Check for sensitive data patterns
- Validate commit message quality
- Show summary of changes

## Protocol

**Propose-Act**: Present staging analysis and commit plan, get user approval before executing.

## Success Criteria
- Proper staging conflict resolution
- Meaningful commit messages
- User control over the process
- Safety warnings when needed
- Clear feedback on results
