# Git Add Commit

## Overview

The **git-add-commit** skill provides an intelligent, LLM-driven approach to git commits by automatically discovering related files through dependency analysis and generating meaningful semantic commit messages.

## Purpose

Traditional git workflows require manually tracking which files are related to a change. This skill automates that process by:

1. **Dependency Chasing**: Starting from a scope (folder/file), it reads files to extract imports, references, and links
2. **Smart Discovery**: Loops through git status to find all referenced files that have been modified
3. **Semantic Analysis**: Deeply analyzes diffs to understand what actually changed and why
4. **Meaningful Commits**: Generates conventional commit messages that explain the real intent

## Key Features

- **Universal Language Support**: Works with Python imports, TypeScript/JavaScript imports, markdown links, JSON paths
- **Dependency-Aware**: Finds connected files even if they're in different directories
- **Semantic Understanding**: Analyzes what changed (features, fixes, refactors) not just which files
- **Safety Validation**: Checks for large files, sensitive data, and common mistakes
- **Conventional Commits**: Follows standardized format with type, scope, subject, and body

## When to Use

Use this skill when you:
- Want to commit logically related changes together
- Need help understanding what files are connected
- Want meaningful commit messages without manual writing
- Have changes spanning multiple files/directories
- Want to ensure nothing related is missed

## How It Works

### 1. Scope-Based Discovery
You provide a scope (e.g., "create-prompt", "vscode-extension/src"), and the skill finds all matching files in git status.

### 2. Reference Chasing
For each matched file, it:
- Reads the content
- Extracts imports (`import X from './Y'`, `from X import Y`)
- Extracts links (`[link](../path)`, `[id:dir]path`)
- Extracts JSON paths (`"manifest": "path/to/file"`)
- Checks if those referenced files are in git status
- Loops until no new references found

### 3. Semantic Analysis
Analyzes all diffs to identify:
- Structural changes (new sections, reorganization)
- Functional changes (features, fixes, behavior)
- Knowledge base changes (KB files, schemas, validation)
- Terminology/UX changes (user messages, help text)
- Dependencies (new imports, schema updates)

### 4. Commit Message Generation
Creates conventional commit with:
- **Type**: feat/fix/refactor/docs/chore/test
- **Scope**: Affected area (from user's input)
- **Subject**: One-line summary
- **Body**: Detailed explanation of what, why, and major changes

### 5. Safe Execution
- Validates for large files (>10MB)
- Checks for sensitive data patterns
- Requires user confirmation
- Stages files with `git add`
- Commits with generated message

## Example

**User**: "commit create-prompt"

**Skill discovers**:
```
Initial: create-prompt.md (modified)
References found: kb/prompt-structure-schema.md (new)
References found: kb/file-modification-rules.md (new)
No more references → Stop

Result: 3 connected files
```

**Generated commit**:
```
refactor(create-prompt): enforce KB-driven structure validation

Added mandatory KB loading:
- prompt-structure-schema.md: minimal BOM requirements  
- file-modification-rules.md: read-only file rules

Ensures prompts follow canonical structure.
```

## Integration

This skill integrates with:
- **Git**: All standard git operations
- **File System**: Reads files to extract references
- **LLM Context**: Uses semantic understanding for analysis

## Limitations

- Requires files to be in git status (modified/new/staged)
- Reference extraction is pattern-based (may miss dynamic imports)
- Best for projects with clear dependency structures
- Cannot handle very large codebases (>1000 changed files) efficiently

## Version History

- **2.0.0** (2025-11-25): Complete refactor to dependency-aware LLM approach
- **1.0.0** (2025-11-15): Initial version with task-based workflow
