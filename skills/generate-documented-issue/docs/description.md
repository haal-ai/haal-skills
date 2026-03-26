# generate-documented-issue

## Overview
Create a highly documented GitHub Issue with duplicate detection across issues, PRs, and discussions, codebase impact analysis, and clear acceptance criteria.

## Purpose
Produce well-structured GitHub Issues that include context, evidence, and acceptance criteria. Prevents duplicates by checking existing issues, pull requests, and discussions before creation.

## Key Features
- Duplicate detection across issues, PRs, and discussions
- Codebase impact analysis (identifies likely affected files)
- Structured issue template with acceptance criteria
- Preview and confirmation before creation
- Automatic gh CLI authentication verification
- Solution-agnostic (describes the "what", not the "how")

## Usage
Invoke this skill by saying:
- "Create an issue for the flaky login test"
- "Generate a documented issue about the API rate limiting bug"
- "Open a GitHub issue for the missing validation"

## Parameters

### Required
- **issue_intent**: Description of the problem or feature request (provided in conversation)

### Optional
- **repo**: Target repository (default: current repository)
- **labels**: Issue labels to apply

## Process Flow
1. **Verify gh CLI** — Check `gh --version`
2. **Verify Authentication** — Check `gh auth status`
3. **Identify Repository** — Detect from git remote or ask user
4. **Collect Intent** — Gather problem description and context
5. **Duplicate Detection** — Search existing issues, PRs, and discussions
6. **Codebase Impact Analysis** — Identify likely affected files
7. **Draft Issue** — Create structured issue with acceptance criteria
8. **Preview & Confirm** — Show draft for user approval
9. **Create Issue** — Submit via `gh issue create`

## Output
- A GitHub Issue created in the target repository with:
  - Clear title and description
  - Impact analysis (affected files/components)
  - Acceptance criteria
  - Related issues/PRs references

## Related Skills
- **generate-documented-issue**: Self (this skill)
- **sync-github-discussions-incrementally**: For tracking discussions
