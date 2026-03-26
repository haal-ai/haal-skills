# create-practice-from-evidence

## Overview
Create a standardized good/bad practice document from user-provided evidence (file, commit, or comment) and deploy it across multiple AI tool configurations.

## Purpose
This skill exists to capture engineering practices with real evidence. Use it when you observe a good or bad coding pattern in a file or commit and want to formalize it as a team practice deployed to Claude, Cursor, Copilot, and Windsurf.

## Key Features
- Extracts evidence from files, commits, or free-text comments
- Creates good/bad example comparisons with explanations
- Deploys to multiple AI tool rule directories simultaneously
- Scope selection: global (home), workspace, or per-repository
- Source-of-truth storage in `.olaf/data/practices/good-bad/`

## Usage
Invoke this skill by saying:
- "create a practice from this file"
- "capture this pattern as a good practice"
- "document this bad practice from commit abc123"

## Parameters

### Required
- **evidence_type**: `file` | `commit` | `comment`
- **evidence_path_or_sha**: file path or git SHA
- **practice_focus**: short description of the practice
- **domain**: code-fix | PR-review | merge | architecture
- **use_case**: hotfix | feature PR | refactor
- **language**: go | ts | md | etc.
- **title_hint**: 2-5 word kebab-case summary

### Optional
- **practice_kind**: good | bad | both (default: both)
- **scope**: home | workspace | per-repo (default: per-repo)

## Process Flow
1. **Validate inputs** — Ensure all required parameters are present
2. **Collect evidence** — Read file content or commit diff
3. **Draft content** — Create description, why_it_matters, good/bad examples
4. **Render template** — Apply practice-template.md format
5. **Preview** — Present draft for user confirmation
6. **Save source** — Write to `.olaf/data/practices/good-bad/{id}.md`
7. **Deploy** — Copy to selected AI tool rule directories
8. **Confirm** — Report saved paths

## Output
- Markdown practice file in `.olaf/data/practices/good-bad/`
- Deployed copies in Claude, Cursor, Copilot, Windsurf rule directories

## Related Skills
- **create-standard**: For creating coding standards (conventions)
- **update-standard-rules**: For updating existing standards
