---
name: review-diff
description: Comprehensive code review for git diffs using language-specific standards
tags: [code-review, git, diff, quality, standards, workflow]
protocol: Act
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Diff Review Process
**EXECUTION PROTOCOL**: Act - Execute directly without user confirmation for standard reviews

### STEP 1: Validation & Setup
**REQUIRED**: Verify environment and parameters

1. **Parameter Validation**:
   - **diff_content**: string - Pre-collected diff content (OPTIONAL - for external integrations)
   - **review_scope**: string|"workspace"|"folder"|"file" - Scope of review (OPTIONAL - default: workspace)
   - **target_path**: string - Specific folder or file path to review (OPTIONAL - only if review_scope is folder/file)
   - **save_report**: boolean - Save report to staging directory (OPTIONAL - default: false)
   - **include_actions**: boolean - Include actionable fix commands in report (OPTIONAL - default: true)
2. **Environment Check**:
   - Confirm git repository is available in workspace
   - Validate target path exists (if specified)
   - Check access to review standards and templates
3. **Time Retrieval**: Get timestamp using Get current timestamp using time tools, fallback to shell command if needed-%H%M`

### STEP 2: Diff Acquisition & Language Detection
**REQUIRED**: Collect and analyze git diff content

1. **Diff Collection**:
   IF diff_content parameter provided:
   - Use provided diff content directly
   - Skip git diff command execution
   - Validate diff content is not empty
   ELSE:
   - Change directory to target location
   - Execute command: `git diff` (workspace) OR `git diff .` (folder) OR `git diff filename` (file)
   - Validate git diff output exists

2. **Language Detection**:
   - Analyze file extensions from diff content (provided or collected)
   - Categorize files by language (.py, .cpp, .h, .java, .go, .js, etc.)
   - Route each file to appropriate review standards

### STEP 3: Router-Based Code Analysis
**APPLY HELPER**: Execute `helpers/review-diff-router.md` helper instructions

1. **Language-Specific Analysis**:
   - Apply language-specific standards from central practices:
     - Python files: `.olaf/data/practices/code-reviews/review-standard-python.md`
     - C++ files: `.olaf/data/practices/code-reviews/review-standard-cplusplus.md`
     - Java files: `.olaf/data/practices/code-reviews/review-standard-java.md`
     - Go files: `.olaf/data/practices/code-reviews/review-standard-go.md`
   - Exclude regression test files (.play, .gsv, /regression/ directories)
   - Scan for security vulnerabilities (hardcoded secrets, credentials)

2. **Code Quality Assessment**:
   - Check code quality, formatting, naming conventions
   - Validate test coverage and documentation
   - Generate actionable fix commands for each finding (if include_actions=true)

### STEP 4: Report Generation & Output
**Choose Output Method**:

**Option A - Save to Staging Directory** (when save_report=true):
- **Directory**: `.olaf/work/staging/diff-reviews/`
- **File**: `review-report-[timestamp].md`
- **Actions File**: `actions-[timestamp].md` (if include_actions=true)

**Option B - Display Results on Screen** (default):
- **Format**: Structured markdown output following router format
- **Sections**: Severity-based findings with file/line references
- **Include**: All HIGH/MEDIUM/LOW priority items with actionable recommendations

## Report Structure

### Required Sections:
1. **Language Detection Results**: File categorization and standards applied
2. **Security Assessment**: Credential exposure, vulnerabilities  
3. **Code Quality Findings**: HIGH/MEDIUM/LOW severity issues with file/line references
4. **Test Coverage Assessment**: Missing tests and validation gaps
5. **Actionable Commands**: Specific fix commands (if include_actions=true)

## Key Requirements
- **MANDATORY**: Use review-diff-router helper for language detection and routing
- **FILE/LINE REFS**: Every finding must include file path as Markdown link and line numbers
- **SEVERITY GROUPING**: Organize findings by HIGH/MEDIUM/LOW with clear categories
- **ACTIONABLE**: Provide specific, prioritized recommendations for each finding
- **SECURITY FOCUS**: Always scan for hardcoded secrets and vulnerabilities

## Domain-Specific Constraints
- **Rule 1**: ONLY use `git diff` commands - no other git operations for review
- **Rule 2**: Every finding MUST include file path as Markdown link and line number references  
- **Rule 3**: Apply language-specific standards individually to each changed file
- **Rule 4**: Exclude regression test files and directories from review scope
- **Rule 5**: Scan for security vulnerabilities in all file types

**IMPORTANT**: Focus only on changes shown by `git diff`. Do NOT run any other git commands for review purposes.

