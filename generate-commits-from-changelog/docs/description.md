# Generate Commits from Changelog

**Source**: generate-commits-from-changelog/skill.md

## Overview

Generate Commits from Changelog creates meaningful Git commits from changelog entries and repository changes, ensuring consistency between documentation and version control history.

## Purpose

Maintaining alignment between changelog documentation and Git commit history is essential for project traceability and release management. This skill automates the process of analyzing changelog entries and repository changes to generate properly formatted, atomic commits that follow conventional commit standards.

## Usage

**Command**: `generate commits from changelog`

**Protocol**: Interactive (with approval gates)

**When to Use**: Use this skill when you have changelog entries that need to be reflected in Git commits, or when you want to ensure your commit history aligns with documented changes. It's particularly valuable during release preparation or when catching up on commit documentation.

## Parameters

### Required Inputs
None - the skill will prompt for entries if not provided

### Optional Inputs
- **changelog_path**: Path to the changelog file (default: `.olaf/data/projects/changelog-register.md`)
- **repository_root**: Path to the Git repository root (default: current directory)
- **commit_strategy**: How to handle commit creation - `auto` or `interactive` (default: `interactive`)
- **sign_commits**: Whether to sign commits (default: `false`)

### Context Requirements
- Access to Git repository
- Read access to changelog file
- Write access to repository for commits

## Output

**Deliverables**:
- Markdown report with proposed commit messages
- Files to be included in each commit
- Changelog references
- Validation results

**Format**: Interactive commit plan with approval workflow

## Process Flow

1. **Initial Analysis**: Check for staged changes, scan for modified/added/deleted files, identify untracked files
2. **Changelog Processing**: Parse recent changelog entries, group related changes, map changes to affected files
3. **Change Analysis**: Analyze file modifications, group related files by feature/fix, identify unassociated changes
4. **Commit Planning**: Create commit plan with messages, organize commits logically, validate against branch policies
5. **Review & Execution**: Present commit plan for approval, execute commits after user confirmation

## Examples

### Example 1: Interactive Commit Generation

**Input**:
- changelog_path: `.olaf/data/projects/changelog-register.md`
- commit_strategy: `interactive`

**Output**: 
- Proposed commits grouped by feature/fix
- User reviews and approves each commit
- Commits created with proper messages and references

### Example 2: Auto Commit Generation

**Input**:
- commit_strategy: `auto`
- sign_commits: `true`

**Output**:
- Commits automatically created based on changelog analysis
- All commits signed with GPG key

## Commit Message Format

```
type(scope): concise description

Detailed explanation if needed
- List of changes
- Related to #issue
- BREAKING CHANGE: if applicable
```

## Supported Commit Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes
- **refactor**: Code refactoring
- **perf**: Performance improvements
- **test**: Test additions/modifications
- **chore**: Maintenance tasks

## Related Skills

- **create-changelog-entry**: Create new changelog entries
- **analyze-changelog-and-report**: Analyze changelog for patterns
- **git-add-commit**: Simple git commit operations

## Tips

1. **Review before committing**: Always use interactive mode for important changes
2. **Keep commits atomic**: Let the skill group related changes together
3. **Use conventional commits**: Follow the commit type conventions for consistency
4. **Reference issues**: Include issue references in commit messages when applicable
5. **Respect .gitignore**: The skill automatically respects gitignore rules

## Limitations

- Requires valid Git repository
- Cannot commit sensitive information (blocked by design)
- Merge conflicts must be resolved manually before running
- Branch protection rules may prevent direct commits
