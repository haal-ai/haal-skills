# Review-Diff Skill Tutorial

## Step-by-Step Guide

This tutorial walks you through using the **review-diff** skill to perform comprehensive code reviews on git diffs.

## Prerequisites

Before using this skill:
- Ensure you have a git repository in your workspace
- Make some code changes (but don't commit them yet)
- Have the OLAF framework loaded

## Basic Usage

### Step 1: Review All Changes in Workspace

```markdown
/review-diff
```

This will:
- Analyze all unstaged changes in the workspace
- Apply appropriate language-specific standards
- Generate a comprehensive review report

### Step 2: Review Specific Folder

```markdown
/review-diff folder /path/to/specific/folder
```

This will:
- Limit review to changes within the specified folder
- Verify the folder path exists
- Focus review scope on targeted changes

### Step 3: Review Specific File

```markdown
/review-diff file /path/to/specific/file.py
```

This will:
- Review changes only in the specified file
- Apply language-specific standards for that file type
- Provide focused feedback on single file changes

## Understanding the Output

### Report Structure

The skill generates reports with this structure:

```markdown
# Code Review Report - 20251120-1445

**Files Reviewed:** 3 files
**Languages Detected:** Python, C++
**Review Scope:** Full workspace

#### HIGH
- [src/auth.py](src/auth.py), line 42 — Hardcoded API key detected. Use environment variable instead.

#### MEDIUM  
- [src/utils.cpp](src/utils.cpp), lines 15-20 — Missing type hints for function parameters. Add type annotations.

#### LOW
- [src/main.py](src/main.py), line 8 — Import organization could be improved for readability.

---
**Review Summary:**
- HIGH: 1 issues
- MEDIUM: 1 issues
- LOW: 1 issues

**Next Steps:**
- Address HIGH severity issues before push
- Consider MEDIUM issues for code quality  
- Apply LOW suggestions when convenient
```

### Severity Levels

**HIGH Priority** - Address before committing:
- Security vulnerabilities
- Memory safety issues
- Runtime errors
- Critical performance problems

**MEDIUM Priority** - Consider for code quality:
- Best practices violations
- Missing documentation
- Test coverage gaps
- Formatting inconsistencies

**LOW Priority** - Apply when convenient:
- Minor style improvements
- Optimization opportunities
- Code organization suggestions

## Language-Specific Reviews

### Python Files (.py)

The skill automatically applies Python-specific standards from the central practices:
- **Source**: `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-python.md`
- **Standards**: Type hints validation, PEP compliance checking, import organization
- **Tools**: Docstring requirements, memory management patterns

### C++ Files (.cpp, .h, .hpp)

For C++ files, it applies standards from:
- **Source**: `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-cplusplus.md`  
- **Standards**: Memory safety checks, modern C++ standards, smart pointer usage
- **Tools**: Thread safety validation, performance considerations

### Java Files (.java)

For Java files, it applies enterprise-grade standards:
- **Source**: `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-java.md`
- **Standards**: Modern Java features, Spring framework patterns, exception handling
- **Tools**: JVM performance, security practices, testing patterns

### Go Files (.go)

For Go files, it applies Go-specific idioms and practices:
- **Source**: `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-go.md`
- **Standards**: Go idioms, error handling, concurrency patterns
- **Tools**: Goroutine management, channel usage, memory efficiency

### Mixed Language Projects

When your changes include multiple languages:
- Each file is reviewed with its appropriate standards
- Findings are organized by language in the report
- Cross-language interface concerns are noted

## Advanced Usage

### Working with Large Diffs

For projects with many changes:
1. Start with a full workspace review to get overview
2. Address HIGH severity issues first
3. Use folder-specific reviews to focus on areas
4. Use file-specific reviews for detailed analysis

### Integration with Git Workflow

**Before Committing:**
```markdown
/review-diff
```
Review all changes and address HIGH/MEDIUM issues

**Before Push:**
```markdown  
/review-diff
```
Final check to ensure quality standards

**Pull Request Preparation:**
Use the generated report to write comprehensive PR descriptions

## Troubleshooting

### No Changes Detected

If the skill reports no changes:
- Verify you have unstaged changes: `git status`
- Ensure you're in the correct directory
- Check that files are tracked by git

### Path Not Found

If specified paths aren't found:
- Verify the path exists in your workspace
- Use absolute paths or workspace-relative paths
- Check for typos in the path specification

### Missing Language Standards

If a language isn't specifically supported:
- The skill applies general code review principles
- Consider adding language-specific standards to the knowledge base
- Focus on universal quality aspects (security, organization, documentation)

## Best Practices

1. **Regular Reviews**: Run reviews frequently during development
2. **Incremental Fixes**: Address issues as they're identified
3. **Team Standards**: Use consistent review criteria across team
4. **Documentation**: Keep review findings for future reference
5. **Continuous Improvement**: Update review standards based on findings

## Next Steps

After completing your review:
- Address HIGH severity findings before committing
- Consider MEDIUM severity improvements
- Apply LOW severity suggestions incrementally
- Update your commit message based on review findings
- Share review insights with your team