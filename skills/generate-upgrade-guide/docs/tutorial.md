# Generate Upgrade Guide: Step-by-Step Tutorial

## Overview

This skill generates a comprehensive upgrade guide between two git tags. It gathers git data (commits, diffs, contributors), extracts Jira ticket references, fetches Jira issue details, and then uses the LLM to produce a structured, actionable upgrade document.

## Prerequisites

- Git repository with tags
- Python 3.9+
- (Optional) Jira API credentials configured as environment variables

## Step 1: Configure Jira (Optional)

If your commits reference Jira tickets and you want full issue details:

**For Jira Cloud:**
```bash
export JIRA_BASE_URL="https://yourcompany.atlassian.net"
export JIRA_USER="your.email@company.com"
export JIRA_API_TOKEN="your-api-token"
```

**For Jira Server (PAT):**
```bash
export JIRA_BASE_URL="https://jira.yourcompany.com"
export JIRA_PAT="your-personal-access-token"
```

If not configured, the skill still works — it lists Jira ticket IDs found in commits but cannot fetch details.

## Step 2: Run the Skill

Invoke the skill in your AI assistant:

```
Generate an upgrade guide from v1.0.0 to v1.1.0
```

Or with more detail:

```
Generate an upgrade guide from v1.0.0 to v1.1.0 on branch main for project MyApp
```

## Step 3: Provide Parameters

The skill will ask for:

1. **start_tag** (required): The version you are upgrading FROM (e.g., `v1.0.0`)
2. **end_tag** (required): The version you are upgrading TO (e.g., `v1.1.0`)
3. **branch** (optional): Defaults to current branch
4. **project_name** (optional): Defaults to repository folder name

## Step 4: Automated Data Gathering

The skill runs two Python scripts automatically:

1. **gather_git_data.py** — Extracts:
   - All commits between the two tags
   - Commit messages and bodies
   - File changes (additions, modifications, deletions)
   - Contributor summary
   - Jira ticket references from commit messages

2. **gather_jira_data.py** — Fetches:
   - Issue summary, type, status, priority
   - Assignee, reporter, components, labels
   - Fix versions and descriptions

## Step 5: Review the Upgrade Guide

The LLM generates a structured upgrade guide including:

- **Executive Summary** — Overall upgrade complexity (Simple/Moderate/Complex)
- **Prerequisites** — What to do before starting
- **Breaking Changes** — With explicit migration steps and verification commands
- **Step-by-Step Procedure** — Numbered, actionable steps
- **New Features & Bug Fixes** — Linked to Jira tickets
- **Configuration Changes** — New, changed, or removed settings
- **Post-Upgrade Verification** — Checklist to confirm success
- **Rollback Procedure** — How to revert if needed
- **Full Change Log** — All commits categorized

## Output Files

All files are saved to `.olaf/work/staging/upgrade-guide/`:

| File | Contents |
|------|----------|
| `git-data-{timestamp}.md` | Raw git data (commits, diffs, contributors) |
| `jira-tickets.txt` | Extracted Jira ticket IDs |
| `jira-data-{timestamp}.md` | Jira issue details |
| `upgrade-guide-{start}-to-{end}-{timestamp}.md` | Final upgrade guide |

## Example Output

```markdown
# Upgrade Guide: MyApp v1.0.0 → v1.1.0

**Generated**: 2026-03-09
**Branch**: main
**Commits**: 47
**Jira Tickets**: 12

## Executive Summary

This upgrade introduces 3 new features, 8 bug fixes, and 1 breaking change
affecting the authentication module. Complexity: MODERATE — requires updating
the auth configuration file before deploying.

## Breaking Changes

1. **Auth configuration format changed** (PROJ-234)
   - **Impact**: Application will fail to start with old auth.yaml format
   - **Action required**:
     ```bash
     cp config/auth.yaml config/auth.yaml.bak
     python scripts/migrate-auth-config.py config/auth.yaml
     ```
   - **Verify**:
     ```bash
     python scripts/validate-config.py config/auth.yaml
     ```

## Step-by-Step Upgrade Procedure

### Step 1: Update dependencies
...
```

## Tips

- **Large releases**: For releases with many commits, the guide will be comprehensive. Review the breaking changes section first.
- **No Jira**: If your team doesn't use Jira, the guide still works based on git data alone.
- **Custom ticket patterns**: The script detects standard Jira patterns (`PROJ-123`). If your project uses a different format, you may need to adjust the regex in `gather_git_data.py`.
