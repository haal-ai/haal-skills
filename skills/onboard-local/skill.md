---
name: onboard-local
description: Local-only onboarding: analyzes codebase and generates draft standards & commands without cloud service dependency
license: Apache-2.0
metadata:
  olaf_tags: [onboarding, analysis, standards, commands, local, offline]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

# Onboard-Local: Offline Codebase Onboarding

Local-only onboarding that analyzes codebase patterns and generates draft standards and commands without requiring any cloud service or authentication.

## Guarantees

- **No cloud dependency.** Runs entirely locally without authentication or network access.
- **Read-only analysis.** Analysis phase does not modify any project files.
- **Drafts before final.** All items are written as drafts first, allowing review.
- **Evidence required.** Every reported insight must include file-path evidence.
- **Focused output.** Max **5 Standards** and **5 Commands** generated per run.

---

## Step 0 — Introduction

Print exactly:

```
Starting local onboarding analysis. This will analyze your codebase for patterns and generate draft standards and commands. No cloud connection required.
```

---

## Step 1 — Get Repository Name

Get the repository name:

```bash
basename "$(git rev-parse --show-toplevel)"
```

Remember this as the repository name.

---

## Step 2 — Detect Existing Configuration

Before analyzing, detect and preserve any existing agent configuration.

### Glob (broad, future-proof)
Glob for markdown in these roots (recursive):
- `.packmind/**/*.md`
- `.claude/**/*.md`
- `.agents/**/*.md`
- `**/skills/**/*.md`
- `**/rules/**/*.md`

### Classify
Classify found files into counts:
- **standards**: `.packmind/standards/**/*.md`
- **commands**: `.packmind/commands/**/*.md`
- **other_docs**: any markdown under `.claude/`, `.agents/`, or any `skills/` or `rules/` directory outside `.packmind`

If any exist, print exactly:

```
Existing agent docs detected:

    Standards: [N]
    Commands: [M]
    Other docs: [P]

No overwrites. New files will be added next to existing ones.
```

---

## Step 3 — Detect Project Stack (Minimal, Evidence-Based)

### Language markers (check presence)
- JS/TS: `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `tsconfig.json`
- Python: `pyproject.toml`, `requirements.txt`, `setup.py`
- Go: `go.mod`
- Rust: `Cargo.toml`
- Ruby: `Gemfile`
- JVM: `pom.xml`, `build.gradle`, `build.gradle.kts`
- .NET: `*.csproj`, `*.sln`
- PHP: `composer.json`

### Architecture markers (check directories)
- Hexagonal/DDD: `src/application/`, `src/domain/`, `src/infra/`
- Layered/MVC: `src/controllers/`, `src/services/`
- Monorepo: `packages/`, `apps/`

Print exactly:

```
Stack detected (heuristic):

    Languages: [..]

    Repo shape: [monorepo|single]

    Architecture markers: [..|none]
```

---

## Step 4 — Run Core Analyses

Read each reference file for detailed search patterns, thresholds, and insight templates. These reference files should be in the same directory as this skill:

| Analysis | Reference File | Output focus |
|----------|----------------|--------------|
| File Template Consistency | `references/file-template-consistency.md` | Commands |
| CI/Local Workflow Parity | `references/ci-local-workflow-parity.md` | Commands |
| Role Taxonomy Drift | `references/role-taxonomy-drift.md` | Standards |
| Test Data Construction | `references/test-data-construction.md` | Standards |

### Output schema (internal; do not print as-is to user)
For every finding, keep an internal record:

```
INSIGHT:
title: ...
why_it_matters: ...
confidence: [high|medium|low]
evidence:
- path[:line-line]
where_it_doesnt_apply:
- path[:line-line]
```

---

## Step 5 — Generate All Drafts

Generate all draft files in one batch.

### Standard Draft Format

For each Standard insight, create a Markdown file at `.packmind/standards/_drafts/<slug>.draft.md`:

```markdown
# Standard Name

What the standard covers and why.

## Scope

Where this standard applies (e.g., 'TypeScript files', 'React components').

## Rules

### Rule starting with action verb

Another rule can follow...

## Examples

### Good

```typescript
// Valid code example
```

### Bad

```typescript
// Invalid code example
```
```

### Command Draft Format

For each Command insight, create a Markdown file at `.packmind/commands/_drafts/<slug>.draft.md`:

```markdown
# Command Name

What the command does, why it's useful, and when it's relevant.

## When to Use

- Scenario when this command applies
- Another scenario...

## Checkpoints

- Question to validate before proceeding?

## Steps

### 1. Step Name

What this step does and how to implement it.

```typescript
// Optional code example
```

### 2. Another Step

Description of next step...
```

### Generation Rules

- Generate drafts **only from discovered insights** (no invention)
- Use evidence from analysis to populate rules/steps
- Cap output: max **5 Standards** + **5 Commands**
- Never overwrite existing files; append `-2`, `-3`, etc. if slug exists

---

## Step 6 — Present Summary & Confirm

Present the generated draft files:

```
============================================================
  ANALYSIS COMPLETE
============================================================

Target repo: [repo-name]
Stack detected: [languages], [monorepo?], [architecture markers]
Analyses run: [N] checks

DRAFTS CREATED:

Standards ([N]):
  1. [Name] → .packmind/standards/_drafts/[slug].draft.md
  2. ...

Commands ([M]):
  1. [Name] → .packmind/commands/_drafts/[slug].draft.md
  2. ...

Drafts are saved in .packmind/*/_drafts/ — you can review or edit them.
============================================================
```

Then ask via AskUserQuestion with three options:

- **Review drafts** — Open draft files for editing
- **Keep as drafts** — Exit, drafts remain for later review
- **Convert to registry format** — Convert drafts to haal-skills registry format

---

## Step 7 — Convert to Registry Format (Optional)

If user selects "Convert to registry format", convert each draft to the haal-skills registry structure:

### For Standards

1. Create competency JSON if not exists: `competencies/<repo-name>.json`
2. Add standard slug to `shared.skills` array
3. Create per-tool rule files in `rules/global/{tool}/` directories

### For Commands

1. Add command slug to competency JSON
2. Create per-tool command files in `commands/global/{tool}/` directories

### Registry Structure

```
<repo-name>-registry/
├── haal_manifest.json
├── competencies/
│   └── <repo-name>.json
├── standards/
│   └── <slug>/
│       └── standard.md
├── commands/
│   └── <slug>/
│       └── command.md
├── rules/
│   ├── global/
│   │   ├── claude/
│   │   ├── copilot/
│   │   ├── cursor/
│   │   ├── windsurf/
│   │   └── kiro/
│   └── repo/
│       ├── claude/
│       ├── copilot/
│       ├── cursor/
│       ├── windsurf/
│       └── kiro/
└── commands-formats/
    ├── global/
    └── repo/
```

Print:

```
============================================================
  CONVERSION COMPLETE
============================================================

Registry created at: <repo-name>-registry/

Competency: [repo-name]
  Standards: [N]
  Commands: [M]

Per-tool formats generated for:
  - Claude (CLAUDE.md format)
  - Copilot (.github/copilot-instructions.md format)
  - Cursor (.cursorrules format)
  - Windsurf (.windsurfrules format)
  - Kiro (.kiro/steering format)

Next step: Commit registry to GitHub for distribution
============================================================
```

---

## Edge Cases

### No patterns discovered

If analysis found no patterns:

```
============================================================
  ℹ️ NO PATTERNS DISCOVERED
============================================================

The analysis didn't find enough recurring patterns to generate standards or commands.

This can happen with smaller codebases or projects with very diverse coding styles.
You can try again later as the codebase grows, or create standards manually.
============================================================
```

### Reference files not found

If reference files are missing:

```
⚠️ Reference files not found at expected location.

Please ensure these files exist:
  - references/file-template-consistency.md
  - references/ci-local-workflow-parity.md
  - references/role-taxonomy-drift.md
  - references/test-data-construction.md

Proceeding with built-in analysis patterns.
```
