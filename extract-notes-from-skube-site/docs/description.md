# skube-doc-synthesis

Creates chapter-by-chapter synthesis notes that clearly separate:
- **SKube-specific** content (what SKube adds/changes)
- **Quarkus-baseline** content (what is standard Quarkus)

It is designed for:
- Large documentation that must be processed across multiple sessions.
- Multi-agent execution via a shared `TODO/WIP/DONE` tracker.

## Inputs
- `input_url` (required)
- `chapter_selection` (`next` / `all` / list)
- `agent_name` (recommended)

## Outputs
- Progress tracker: `.olaf/work/skube/progress.md`
- Notes folder: `.olaf/work/skube/syntheise-YYYYMMDD-HHmm/`
  - `00-global-synthesis.md`
  - One file per chapter completed

## Usage
Invoke the skill and provide the URL.
Then run with `chapter_selection=next` repeatedly to process one chapter at a time.
