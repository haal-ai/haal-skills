# Prompt: Analyze Discussions and Update Summary

## Inputs

You have two files:

- **Source:** `discussion-summaries/<repo>-discussions-source.md`
- **Summary:** `discussion-summaries/<repo>-discussions-summary.md`

The source file contains multiple discussion sections. Each section has:

- `**Status:** NEW|UPDATED|UNCHANGED`
- Original post content
- Comments content

## Task

Update the summary file incrementally.

### Rules

- Update `**Updated:** <timestamp>` near the top of the summary file.
- Do **not** rewrite or reword sections for `UNCHANGED` discussions.
- For `NEW` discussions:
  - Create a new summary section in the summary file.
- For `UPDATED` discussions:
  - Locate the existing section in the summary file and update it.
- If a discussion exists in the source but not in the summary, treat it as `NEW`.

### Required Summary Structure (per discussion)

For each discussion, write:

- **Intent:** What the author is trying to achieve (1-2 sentences)
- **Core question/problem:** The main question or decision being asked (1-2 sentences)
- **Proposed solutions / responses:**
  - Bullet list of distinct solution directions (not copied sentences)
  - Attribute to authors only when it clarifies differences
- **Outcome / current status:**
  - Resolved / in progress / blocked / needs clarification
- **Follow-up ideas (optional):**
  - If helpful, propose 1-3 additional ideas
  - You may use web search to find best practices or known solutions

### Writing style

- Concise.
- Synthesize: do not copy/paste long text from GitHub.
- Prefer actionable content.

## Output

Update `discussion-summaries/<repo>-discussions-summary.md` in place.
