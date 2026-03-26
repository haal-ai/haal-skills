# sync-github-discussions-incrementally

## Overview
Incrementally sync GitHub Discussions (posts and comments) into a stable source markdown file with NEW/UPDATED/UNCHANGED markers, then guide creation of an analytical summary.

## Purpose
Maintain recurring, delta-based summaries of GitHub Discussions for a repository. Tracks changes across syncs so you only process what's new or updated.

## Key Features
- Incremental sync (only fetches changes since last run)
- Delta markers: NEW, UPDATED, UNCHANGED for each discussion
- Two stable output files: source and summary
- Python sync script for automated extraction
- Agent-guided analytical summaries
- Repository-named output files

## Usage
Invoke this skill by saying:
- "Sync GitHub discussions for this repo"
- "Update discussion summaries"
- "Pull new discussions from GitHub"

## Parameters

### Required
- **repo**: GitHub repository to sync (default: current)

### Optional
- **output_dir**: Directory for output files (default: `discussion-summaries/`)

## Process Flow
1. **Extract Discussions** — Run Python script to fetch via `gh` CLI
2. **Mark Deltas** — Tag each discussion as NEW, UPDATED, or UNCHANGED
3. **Write Source File** — Save `<repo>-discussions-source.md`
4. **Generate Summary** — Agent creates analytical summary for NEW/UPDATED items
5. **Write Summary File** — Save `<repo>-discussions-summary.md`

## Output
- `discussion-summaries/<repo>-discussions-source.md` — Raw extracted data with delta markers
- `discussion-summaries/<repo>-discussions-summary.md` — Analytical summary maintained across syncs

## Related Skills
- **generate-documented-issue**: Creates documented GitHub Issues
- **create-discussion**: Creates GitHub Discussions
