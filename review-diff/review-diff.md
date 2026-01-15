---
name: review-diff
description: Comprehensive code review for git diffs using language-specific standards
tags: [code-review, git, diff, quality, standards, workflow]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **review_scope**: string|"workspace"|"folder"|"file" - Scope of review (OPTIONAL - default: workspace)
- **target_path**: string - Specific folder or file path to review (OPTIONAL - only if review_scope is folder/file)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Use **Act** protocol for standard code reviews

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm git repository is available in workspace
- Validate target path exists (if specified)
- Check access to review standards and templates

### 2. Execution Phase
You WILL execute these operations:

**Path Discovery** (when target_path provided):
- Search all workspace folders to find exact filesystem location
- Verify path exists before proceeding
- Document discovered path

**Git Operations**:
- Change directory to target location
- Execute command: `git diff` (workspace) OR `git diff .` (folder) OR `git diff filename` (file)
- Validate git diff output exists

**Language Detection**:
- Analyze file extensions in git diff output
- Categorize files by language (.py, .cpp, .h, .js, etc.)
- Route each file to appropriate review standards

**Core Review Logic**: Apply comprehensive review workflow

- Follow helper instructions: `/helpers/review-commit.md`
- Apply language-specific standards from knowledge base:
  - Python files: `/kb/review-commit-python.md`
  - C++ files: `/kb/review-commit-cplusplus.md`
- Exclude regression test files (.play, .gsv, /regression/ directories)
- Scan for security vulnerabilities (hardcoded secrets, credentials)
- Check code quality, formatting, naming conventions
- Validate test coverage and documentation

### 3. Report Generation Phase
You WILL generate structured output:
- Follow template: `templates/review-report-format.md`
- Apply severity guidelines: `templates/severity-guidelines.md`
- Include mandatory file and line number references
- Organize findings by HIGH/MEDIUM/LOW severity

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Structured review report with severity levels
- File references: Markdown links with line numbers for every finding
- Summary: Count of issues by severity level

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation of git diff analysis completion
- Language detection results
- Review scope and file count

### Completion Summary
- Review findings organized by severity
- Total issue counts (HIGH/MEDIUM/LOW)
- Recommendations for addressing findings
- Next steps based on severity levels

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ONLY use `git diff` commands - no other git operations for review
- Rule 2: Every finding MUST include file path and line number references
- Rule 3: Apply language-specific standards individually to each changed file
- Rule 4: Exclude regression test files and directories from review scope
- Rule 5: Scan for security vulnerabilities in all file types

**IMPORTANT**: Focus only on changes shown by `git diff`. Do NOT run any other git commands for review purposes.

