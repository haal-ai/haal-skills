# Review-Diff Skill Description

## Overview

The **review-diff** skill provides comprehensive code review capabilities for git diffs using language-specific review standards and practices. It automatically detects programming languages, applies appropriate review criteria, and generates structured severity-based feedback reports.

## Purpose

This skill automates the code review process by:
- Analyzing git diff output for changed files
- Detecting programming languages from file extensions
- Applying language-specific review standards from the knowledge base
- Generating structured review reports with actionable feedback
- Providing file and line number references for all findings

## Key Features

### Language Detection
- Automatically identifies programming languages (.py, .cpp, .h, .java, .go, .js, etc.)
- Routes each file to appropriate review standards
- Supports Python, C++, Java, and Go specific review criteria
- Fallback to general review principles for other languages

### Severity Classification
- **HIGH**: Security vulnerabilities, memory safety, runtime errors
- **MEDIUM**: Code quality, best practices, testing gaps
- **LOW**: Minor style issues, optimization opportunities

### Actionable Commands
- Generates specific fix commands for each finding
- Provides verification commands to confirm fixes
- Categorizes actions by immediate vs manual fixes
- Language-specific tooling recommendations

### Report Persistence
- Optional saving to `[staging_dir]/diff-reviews/`
- Timestamped report files for tracking over time
- Separate actionable commands file for easy execution
- Organized directory structure for review history

### Comprehensive Coverage
- Security vulnerability scanning (hardcoded secrets, credentials)
- Code quality assessment (duplication, complexity, organization)
- Best practices validation (type hints, documentation, testing)
- Formatting and style compliance checking
- Naming convention consistency verification

### Structured Output
- Mandatory file and line number references for every finding
- Markdown-formatted reports with clickable file links
- Organized by severity levels for prioritized action
- Summary statistics and next steps guidance

## Integration

This skill integrates with:
- **Git**: Requires git repository in workspace
- **OLAF Framework**: Follows established protocols and templates
- **Shared Practices**: References central language-specific review standards in `data/practices/code-reviews/`
- **Templates**: Uses structured report formats
- **Language Router**: Uses `helpers/review-diff-router.md` for language detection and routing
- **Other Review Skills**: Shares review standards with `review-github-pr`, `review-commit`, and other review tools

## Use Cases

1. **Pre-commit Review**: Review changes before committing to repository
2. **Pull Request Preparation**: Generate comprehensive feedback for PR descriptions  
3. **External Integration**: Accept diff from other tools (GitHub PRs, external systems)
4. **Code Quality Assurance**: Systematic evaluation of code changes
5. **Team Standards Enforcement**: Consistent application of coding standards
6. **Security Scanning**: Identification of potential security vulnerabilities

## Input Parameters

- **diff_content**: Pre-collected diff content for external integrations (OPTIONAL)
- **review_scope**: Scope of review - workspace, folder, or file (default: workspace)
- **target_path**: Specific folder or file path when scope is targeted
- **save_report**: Save report to staging directory (default: false)  
- **include_actions**: Include actionable fix commands (default: true)

## Workflow Integration

The skill follows the OLAF **Act** protocol for standard reviews:
1. Validates git repository availability
2. Discovers and verifies target paths
3. Executes appropriate git diff commands
4. Applies language-specific review standards
5. Generates structured severity-based reports
6. Provides actionable recommendations and next steps