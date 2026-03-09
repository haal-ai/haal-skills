# generate-upgrade-guide

## What It Does

Generates a comprehensive, step-by-step upgrade guide between two git tags. The skill gathers git commit data and Jira issue details, then uses the LLM to produce a structured upgrade document that is readable and actionable by both humans and LLMs.

## When To Use

- When preparing a release and you need upgrade instructions for consumers
- When documenting migration steps between two versions of a product
- When you need to understand what changed between two tags and how to apply those changes
- When onboarding teams to a new version and they need a clear action plan

## Key Features

- **Git-based analysis**: Extracts commits, diffs, file changes, and contributors between two tags
- **Jira integration**: Automatically detects Jira ticket references in commit messages and fetches issue details (summary, type, status, priority, description)
- **Human + LLM readable output**: Structured Markdown with numbered steps, checklists, tables, and fenced code blocks
- **Breaking change detection**: Highlights breaking changes with explicit migration steps and verification commands
- **Rollback guidance**: Includes rollback procedures for risky upgrades
- **Graceful degradation**: Works without Jira configuration (lists ticket IDs without details)

## Components

| Component | Purpose |
|-----------|---------|
| `skill.md` | Main skill definition and LLM instructions |
| `tools/gather_git_data.py` | Python script to extract git commits, diffs, and Jira ticket references |
| `tools/gather_jira_data.py` | Python script to fetch Jira issue details via REST API |

## Prerequisites

- `git` installed and repository accessible
- Python 3.9+ for the data gathering scripts
- (Optional) Jira API access via environment variables: `JIRA_BASE_URL`, and either `JIRA_PAT` or `JIRA_USER` + `JIRA_API_TOKEN`
