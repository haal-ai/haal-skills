---
name: sync-github-discussions-incrementally
description: Incrementally sync GitHub Discussions (posts + comments) into a stable source markdown file marked NEW/UPDATED/UNCHANGED, then guide an agent to create or update a stable analytical summary file. Use when you need recurring, delta-based discussion summaries for a repository.
license: Proprietary
compatibility: Requires GitHub CLI (gh) authenticated, network access to github.com, and Python 3.
metadata:
  author: Amadeus-xDLC
  version: "1.0"
---

## Goal

Maintain two stable, repo-named markdown files:

- `discussion-summaries/<repo>-discussions-source.md`
- `discussion-summaries/<repo>-discussions-summary.md`

The **source** file is produced by GitHub extraction and marks each discussion section as:

- `NEW`
- `UPDATED`
- `UNCHANGED`

The **summary** file is maintained by an agent using the prompt in `references/`:

- For `NEW` discussions: create a new analytical summary.
- For `UPDATED` discussions: update the existing analytical summary.
- For `UNCHANGED` discussions: keep existing summary content intact.

## Inputs

- Repository owner (e.g. `Amadeus-xDLC`)
- Repository name (e.g. `genai.claude-code-evaluation`)

## Outputs

- Updated source file:
  - `discussion-summaries/<repo>-discussions-source.md`
- Updated or created summary file:
  - `discussion-summaries/<repo>-discussions-summary.md`

Both documents must have an `**Updated:** <timestamp>` line near the top.

## Steps

### 1) Sync the stable source file from GitHub

Run:

```powershell
python .windsurf/skills/sync-github-discussions-incrementally/scripts/sync_discussions_source.py --owner <owner> --repo <repo>
```

This will:

- Create or update `discussion-summaries/<repo>-discussions-source.md`
- Mark each discussion section as `NEW`, `UPDATED`, or `UNCHANGED`
- Preserve unchanged discussion blocks without rewriting their contents

### 2) Update the stable summary file (agent step)

Use the prompt:

- `.windsurf/skills/sync-github-discussions-incrementally/references/analyze-discussions-and-update-summary.md`

The agent must:

- Read the source file
- Read (or create) the summary file
- Apply updates only for discussions marked `NEW` or `UPDATED`
- Update the `**Updated:**` timestamp at the top of the summary file

## Notes

If you want strict compliance with your repo naming convention, delete `SKILL.md` manually and keep this file as the canonical skill definition.
