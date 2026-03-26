# create-discussion

## Overview
Create a GitHub Discussion (Q&A or Proposal) in the current repository. Verifies gh CLI auth, searches for duplicates, and creates the discussion with auto-detected type.

## Purpose
This skill exists to streamline creating well-structured GitHub Discussions. Use it when you want to ask a question, report a problem, or propose a solution via GitHub Discussions instead of issues.

## Key Features
- Verifies gh CLI installation and GitHub authentication
- Auto-detects discussion type (Q&A vs Proposal) from keywords
- Searches for duplicate discussions before creation
- Checks if Discussions are enabled in the repository
- Auto-generates discussion title and body from user request

## Usage
Invoke this skill by saying:
- "create a discussion"
- "open a GitHub discussion"
- "ask a question on discussions"

## Parameters

### Required
- **user_request**: Description of what to discuss

### Optional
- **type**: Override auto-detected type (Q&A or Proposal)
- **title**: Custom title (auto-generated if not provided)

## Process Flow
1. **Verify gh CLI** — Confirms gh is installed
2. **Verify authentication** — Checks gh auth status
3. **Check Discussions enabled** — Verifies the repo supports Discussions
4. **Auto-detect type** — Infers Q&A or Proposal from keywords
5. **Duplicate check** — Searches existing discussions for similar topics
6. **Create discussion** — Posts via gh API
7. **Return URL** — Provides link to created discussion

## Output
- Created GitHub Discussion with title, body, and URL

## Related Skills
- **generate-documented-issue**: Alternative when Discussions are disabled
