# sync-github-discussions-incrementally

> Step-by-step tutorial for syncing GitHub Discussions incrementally

## Prerequisites
- GitHub CLI (`gh`) installed and authenticated
- Python 3 installed
- Network access to github.com

## Estimated Time
5–10 minutes per sync

## Step-by-Step Instructions

### Step 1: First Sync
> "Sync GitHub discussions for this repo"

On first run, all discussions are marked as NEW.

### Step 2: Review Source File
The extracted data is saved in `discussion-summaries/<repo>-discussions-source.md` with markers:
- **NEW** — First time seeing this discussion
- **UPDATED** — Discussion has new comments since last sync
- **UNCHANGED** — No changes since last sync

### Step 3: Review Summary
An analytical summary is generated for NEW and UPDATED discussions. UNCHANGED discussions keep their existing summary.

### Step 4: Subsequent Syncs
Run the skill again to pull incremental changes. Only NEW and UPDATED items are re-processed — UNCHANGED items are left intact.

### Step 5: Verify Output
Check both files in the `discussion-summaries/` directory.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `gh: command not found` | Install GitHub CLI from https://cli.github.com/ |
| No discussions found | Verify the repository has GitHub Discussions enabled |
| Python errors | Ensure Python 3 is installed and on PATH |
| Stale data | Delete source file and re-run for a full sync |

## Verification Checklist
- [ ] gh CLI authenticated
- [ ] Source file created with delta markers
- [ ] Summary file created with analytical content
- [ ] Subsequent syncs correctly identify NEW/UPDATED/UNCHANGED
