---
name: create-practice-from-evidence
description: Create a standardized good/bad practice document from user-provided evidence (file/commit) and intent.
license: Apache-2.0
metadata:
  olaf_tags: [practices, documentation, git, merge, review, good-bad]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Inputs to request from the user
- evidence_type: one of [file, commit, comment]
- evidence_path_or_sha: if file → absolute/relative path; if commit → SHA or range; if comment → free text
- practice_focus: short description of what to document as a practice
- domain: e.g., code-fix, PR-review, merge, architecture
- use_case: e.g., hotfix, feature PR, refactor
- language: e.g., go, ts, md (used for code fencing)
- practice_kind: one of [good, bad, both] (default: both)
- title_hint: 2–5 words that summarize the practice (e.g., "fast-forward-only")

# Naming and storage rules
- Output folder: `.olaf/data/practices/good-bad`
- File id (and filename without extension): `{domain}-{language}-{title_hint}` kebab-case
- Output path: `.olaf/data/practices/good-bad/{id}.md`
- Template: `templates/practice-template.md` from this skill
- YAML preamble must include: id, name(title), shortDescription, domain, use_case, language, status, created/updated

# Process
1) Validate inputs are present; if missing, ask for them.
2) Collect and summarize evidence depending on `evidence_type`:
   - file: read file and extract the minimal relevant snippet(s)
   - commit: show `git show <sha>` summary and diff snippets relevant to the practice
   - comment: treat as rationale/context
3) Draft content blocks:
   - long_description: derive from `practice_focus` + evidence summary
   - why_important: link to reliability, clarity, safety, performance, etc.
   - good_explanation / good_example_code (if `good` or `both`)
   - bad_explanation / bad_example_code (if `bad` or `both`)
   - sources_files / sources_commits / user_comment
4) Build variables for template:
   - id: `{domain}-{language}-{title_hint}` (kebab-case)
   - title: capitalize words of `title_hint`
   - short_description: one-line summary of the practice
   - created_timestamp: ISO-like `yyyy-MM-dd HH:mm`
5) Render `practice-template.md` by replacing variables with values.
6) Propose the final filename and a preview of the document. Ask for confirmation.
7) On confirmation, write the file to `.olaf/data/practice/good-bad/{id}.md`.
8) Output the saved path.

# Output
- On preview: show the rendered markdown (collapsed if UI supports) and the target path.
- On save: show the final saved path.

# Guardrails
- Never overwrite an existing practice without explicit consent; if exists, propose `{id}-v2.md`.
- Keep examples minimal and self-contained.
- Do not hardcode credentials or secrets from diffs.
