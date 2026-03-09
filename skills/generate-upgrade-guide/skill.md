---
name: generate-upgrade-guide
description: Generate a step-by-step upgrade guide between two git tags by gathering git data, Jira issue details, and producing a human-and-LLM-readable upgrade document.
license: Apache-2.0
metadata:
  olaf_tags: [upgrade, migration, git, jira, documentation, release-management]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

if you are in need to get the date and time, use time tools, fallback to shell command if needed

# Generate Upgrade Guide

Generate a comprehensive, step-by-step upgrade guide from one version (git tag) to another. The guide is designed to be readable and actionable by both humans and LLMs.

## Input Parameters

You MUST request these parameters if not provided by the user:

**REQUIRED**:
- `start_tag`: string — The starting git tag (e.g., `v1.0.0`). This is the version you are upgrading FROM.
- `end_tag`: string — The ending git tag (e.g., `v1.1.0`). This is the version you are upgrading TO.

**OPTIONAL**:
- `branch`: string — The git branch to use. Default: current branch.
- `project_name`: string — Name of the project. Default: derived from repository name.
- `repo_path`: string — Path to the git repository. Default: current working directory.

## User Interaction

- Parameter collection: Ask the user, present defaults clearly.
- Script execution: Run without approval (non-destructive, read-only git operations).
- Jira fetching: Run without approval (read-only API calls).
- Final upgrade guide generation: Present to user for review.

## Process

### Phase 1: Collect Parameters and Validate

1. Ask the user for `start_tag` and `end_tag`. These are mandatory.
2. Ask for `branch`. If not provided, default to the current branch.
3. Ask for `project_name`. If not provided, derive from the repository folder name.
4. Validate that both tags exist in the repository:
   ```bash
   git rev-parse --verify {start_tag}
   git rev-parse --verify {end_tag}
   ```
5. If a branch is specified, confirm the current branch:
   ```bash
   git rev-parse --abbrev-ref HEAD
   ```
6. Determine a timestamp for output file naming: `YYYYMMDD-HHmm` format.

### Phase 2: Gather Git Data

Run the git data gathering script:

```bash
python skills/generate-upgrade-guide/tools/gather_git_data.py \
  "{start_tag}" "{end_tag}" \
  -o ".olaf/work/staging/upgrade-guide/git-data-{timestamp}.md" \
  --branch "{branch}" \
  --repo "{repo_path}"
```

This script produces:
- `.olaf/work/staging/upgrade-guide/git-data-{timestamp}.md` — Structured git data (commits, diffs, contributors)
- `.olaf/work/staging/upgrade-guide/jira-tickets.txt` — Extracted Jira ticket IDs

**Read the git data file** to confirm it was generated correctly and note the number of commits and Jira tickets found.

### Phase 3: Gather Jira Data

Run the Jira data gathering script:

```bash
python skills/generate-upgrade-guide/tools/gather_jira_data.py \
  -f ".olaf/work/staging/upgrade-guide/jira-tickets.txt" \
  -o ".olaf/work/staging/upgrade-guide/jira-data-{timestamp}.md"
```

**Prerequisites for Jira integration** (inform user if not configured):
- `JIRA_BASE_URL` environment variable must be set (e.g., `https://yourcompany.atlassian.net`)
- Authentication via one of:
  - `JIRA_PAT` — Personal access token
  - `JIRA_USER` + `JIRA_API_TOKEN` — User email + API token

If Jira is not configured, the script will still produce a report listing the ticket IDs found. The upgrade guide will be generated without Jira details.

**Read the Jira data file** to confirm it was generated correctly.

### Phase 4: Build Combined Context

Read the two generated files:
1. `.olaf/work/staging/upgrade-guide/git-data-{timestamp}.md`
2. `.olaf/work/staging/upgrade-guide/jira-data-{timestamp}.md`

These files together form the **complete context** for generating the upgrade guide.

### Phase 5: Generate Upgrade Guide

Using the combined context from Phase 4, generate a comprehensive upgrade guide following the structure below.

**Writing principles:**
- Write for both **humans** and **LLMs** — clear, structured, unambiguous
- Every step must be **actionable** — include exact commands, file paths, configuration changes
- Group changes by **impact area** (breaking changes first, then features, then fixes)
- Include **verification steps** after each major action
- Use numbered steps for sequential actions
- Use checklists for parallel/independent actions
- Include rollback guidance for risky steps

**Output file**: `.olaf/work/staging/upgrade-guide/upgrade-guide-{start_tag}-to-{end_tag}-{timestamp}.md`

## Output Format

The generated upgrade guide MUST follow this structure:

```markdown
# Upgrade Guide: {project_name} {start_tag} → {end_tag}

**Generated**: {date}
**Branch**: {branch}
**Commits**: {count}
**Jira Tickets**: {count}

## Executive Summary

[2-3 sentence summary of what changed and the overall upgrade complexity:
SIMPLE (no breaking changes, drop-in replacement),
MODERATE (some configuration or code changes needed),
COMPLEX (significant refactoring, data migration, or breaking API changes)]

## Applicability Check

Before applying this guide, verify your target is at the expected starting version.

**Automated check** (recommended):
```bash
python skills/execute-upgrade-guide/tools/check_version_applicability.py "{start_tag}" "{end_tag}" --repo .
```

**Manual check** — confirm your version matches `{start_tag}` using one of:
```bash
git describe --tags --abbrev=0 HEAD
# or check package.json / pom.xml / pyproject.toml / VERSION file
```

| Current Version | Result |
|----------------|--------|
| Matches `{start_tag}` | ✅ Proceed with this guide |
| Before `{start_tag}` | ❌ Upgrade to `{start_tag}` first |
| Between `{start_tag}` and `{end_tag}` | ⚠️ Partial upgrade — review carefully |
| Matches `{end_tag}` or later | ❌ Already upgraded — this guide does not apply |

## Prerequisites

Before starting the upgrade:
- [ ] Read this guide completely
- [ ] Run the applicability check above and confirm it passes
- [ ] Back up your current deployment
- [ ] Ensure you are on version {start_tag}
- [ ] [Any additional prerequisites discovered from the changes]

## Breaking Changes

[List each breaking change with:]
1. **What changed**: [description]
   - **Jira**: [ticket reference if available]
   - **Impact**: [what breaks if you don't act]
   - **Action required**:
     ```bash
     [exact command or code change]
     ```
   - **Verify**:
     ```bash
     [verification command]
     ```

## Step-by-Step Upgrade Procedure

### Step 1: [First action group]
[Numbered sub-steps with exact commands]

### Step 2: [Second action group]
[Numbered sub-steps with exact commands]

[... continue for all steps ...]

## New Features

[Features introduced in this version, grouped by Jira ticket if available]

| Feature | Ticket | Description |
|---------|--------|-------------|
| ... | ... | ... |

## Bug Fixes

[Bug fixes included in this version]

| Fix | Ticket | Description |
|-----|--------|-------------|
| ... | ... | ... |

## Configuration Changes

[Any new, changed, or removed configuration options]

| Parameter | Change | Old Value | New Value | Notes |
|-----------|--------|-----------|-----------|-------|
| ... | ... | ... | ... | ... |

## Post-Upgrade Verification

After completing the upgrade:
- [ ] [Verification step 1]
- [ ] [Verification step 2]
- [ ] [... ]

## Rollback Procedure

If the upgrade fails:
1. [Rollback step 1]
2. [Rollback step 2]

## Appendix: Full Change Log

[Summary of all commits grouped by category]

### Features
- [commit] [description] ([ticket])

### Fixes
- [commit] [description] ([ticket])

### Technical / Chores
- [commit] [description] ([ticket])

### Documentation
- [commit] [description] ([ticket])
```

## Quality Standards

### Content Requirements
- Every breaking change MUST have an explicit action and verification step
- Commands must be copy-pastable (no placeholders unless clearly marked)
- Steps must be ordered by dependency (do X before Y if Y depends on X)
- Include time estimates where possible (e.g., "this step takes ~5 minutes")

### LLM-Readability Requirements
- Use consistent heading hierarchy (H1 → H2 → H3)
- Use fenced code blocks with language identifiers for all commands
- Use tables for structured data
- Use checklists (- [ ]) for verification items
- Avoid ambiguous pronouns — be explicit about what each step refers to

### Validation
- All commits between the two tags must be accounted for
- All Jira tickets must be referenced
- Breaking changes must have migration steps
- Verification steps must be provided for critical changes

## Error Handling

- **Tag not found**: Inform user, list available tags with `git tag -l`
- **No commits between tags**: Inform user, suggest checking tag order
- **Jira not configured**: Continue without Jira details, note limitation in output
- **Jira fetch failures**: List failed tickets, continue with available data
- **Empty diff**: Inform user, confirm tags are different

## Success Criteria

You WILL consider the task complete when:
- [ ] Both tags validated in the repository
- [ ] Git data gathered (commits, diffs, contributors)
- [ ] Jira tickets extracted and details fetched (or noted as unavailable)
- [ ] Upgrade guide generated following the output format
- [ ] Guide saved to `.olaf/work/staging/upgrade-guide/`
- [ ] User presented with the guide for review
