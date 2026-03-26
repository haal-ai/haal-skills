---
name: update-standard-rules
description: Update, add, or deprecate standards and rules based on conversation context. Triggers on explicit phrases like "update standard", "add a rule", "fix standard", or when conversation reveals patterns, conventions, or workflow changes. Proactive detection when user says "we always do X", "let us remember to Y", "that is the pattern we use".
license: Apache-2.0
metadata:
  olaf_tags: [update, standards, rules, practices, maintenance]
  copyright: Copyright (c) 2026 Haal AI
  author: Haal AI
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

# Update Standard-Rules

Evaluate the user's intent against existing OLAF practices (standards, rules) to identify what needs creating or updating. Produce a structured change report, then apply approved changes locally.

**Local-only mode:** No cloud service required. All changes saved to `.olaf/data/practices/`.

## Guarantees

- **User approval required.** No changes applied without explicit confirmation.
- **Preserve existing.** Never overwrite without backup.
- **Evidence-based.** All changes must reference conversation context or code evidence.
- **Language-aware.** Uses all language/architecture reference files.

---

## Step 1 — Understanding Your Request

**STOP. This phase runs FIRST. No file reads or analysis until this gate passes.**

Analyze the user's input and conversation context to determine intent:

### Case A: No prior conversation / empty input

Ask:

"What practice do you want to modify? For example: a **standard** (coding rule/convention) or a **rule** (specific enforcement). Please describe what you'd like to change."

**BLOCK** — do not proceed until the user responds.

### Case B: Explicit intent found

The user explicitly asked to update, add, fix, or change a standard or rule. Extract an **intent summary**:
- **Target artifact(s)**: which standard(s) or rule(s) to modify (or "new")
- **Kind of change**: create or update
- **Specifics**: any details the user provided about the change

Proceed to Step 2 with this validated intent.

### Case C: Opportunity detected from conversation

The conversation reveals an update opportunity — e.g., a convention was established, a pattern emerged, a workflow was changed, or a known artifact is now stale. Summarize the opportunity and ask:

"I noticed an opportunity to update practices: **<brief description>**. Would you like me to run the update workflow?"

**BLOCK** — do not proceed until the user confirms.

### Case D: No intent and no opportunity

Tell the user:

"I didn't detect any intent or opportunity to modify practices. What would you like to update — a standard or a rule? Please describe the change."

**BLOCK** — do not proceed until the user responds.

---

## Step 2 — Summarizing Changes

> Only proceed after Step 1 validates intent.

Summarize the validated intent:
- Which artifact(s) the user wants to modify and what kind of change
- Any specifics the user provided
- Relevant context from conversation (patterns observed, decisions made, problems encountered)

This intent summary is passed as input to analysis.

---

## Step 3 — Detect Project Stack

Detect the current project's language and architecture to select appropriate reference files.

### Language markers (check presence)
- JS/TS: `package.json`, `tsconfig.json`
- Python: `pyproject.toml`, `requirements.txt`
- Go: `go.mod`
- Rust: `Cargo.toml`
- Ruby: `Gemfile`
- JVM: `pom.xml`, `build.gradle`
- .NET: `*.csproj`, `*.sln`
- PHP: `composer.json`
- C/C++: `CMakeLists.txt`, `*.cpp`, `*.h`

### Architecture markers (check directories)
- Hexagonal/DDD: `src/application/`, `src/domain/`, `src/infra/`
- Layered/MVC: `src/controllers/`, `src/services/`
- Monorepo: `packages/`, `apps/`
- Tauri: `src-tauri/`
- SvelteKit: `src/routes/`
- Next.js: `app/`, `pages/`
- Quarkus: `@QuarkusMain`, `quarkus-app/`
- Spring Boot: `@SpringBootApplication`

Print:

```
Stack detected (heuristic):

    Languages: [..]

    Architecture markers: [..|none]
```

---

## Step 4 — Analyze Existing Practices

### Enumerate existing artifacts

Glob for existing practices:
- Standards: `.olaf/data/practices/standards/**/*.md`
- Rules: `.olaf/data/practices/rules/**/*.md`

### Select reference files

Based on detected stack, select relevant reference files from `init-standard-rules/references/`:

**Core references (always check):**
- `file-template-consistency.md`
- `role-taxonomy-drift.md`
- `test-data-construction.md`
- `ci-local-workflow-parity.md`

**Language-specific references (based on stack):**
- Rust → `rust-patterns.md`
- C# → `csharp-dotnet-patterns.md`
- C/C++ → `cpp-patterns.md`
- Go → `go-patterns.md`
- Svelte → `svelte-patterns.md`
- Angular → `angular-patterns.md`
- Quarkus → `quarkus-patterns.md`
- Spring Boot → `spring-boot-patterns.md`
- Next.js → `nextjs-patterns.md`

### Analyze against intent

For each relevant reference file:
1. Check if the intent relates to patterns defined in the reference
2. Compare existing practices against reference patterns
3. Identify gaps, conflicts, or updates needed

---

## Step 5 — Change Report

Consolidate findings into a structured report. **Number every change** for selective approval:

```
## Practice Change Report

### Standard Updates
1. [standard] <name>: <what changed and why>

### New Standards
2. [standard] <name>: <reason>

### Rule Updates
3. [rule] <name>: <what changed and why>

### New Rules
4. [rule] <name>: <reason>

### Deprecated
5. [standard|rule] <name>: <reason for deprecation>
```

**Only include sections that have actual changes** — omit empty sections.

Present this report and ask the user for approval:
- **Single change**: ask "Do you accept this change?"
- **Multiple changes**: ask "Which changes to apply?" and accept:
  - **All**: apply every numbered change
  - **Inclusion list**: "1, 3, 5" or "only 2 and 4"
  - **Exclusion list**: "all but 4" or "everything except 2"

---

## Step 6 — Applying Changes

### Create new artifacts

For each approved **new** artifact, write to:

| Artifact Type | Write Path |
|---------------|------------|
| Standard | `.olaf/data/practices/standards/<slug>.md` |
| Rule | `.olaf/data/practices/rules/<slug>.md` |

### Update existing artifacts

For each approved **update**, edit the existing file in `.olaf/data/practices/`.

### Backup before overwrite

If updating an existing file, create a backup first:
- Copy to `.olaf/data/practices/.backup/<slug>.<timestamp>.md`

### Deprecate artifacts

For deprecated artifacts:
- Move to `.olaf/data/practices/.deprecated/<slug>.md`
- Add deprecation notice at top of file

---

## Step 7 — Summary

Print:

```
============================================================
  PRACTICES UPDATED
============================================================

Created: [N] standards, [M] rules
Updated: [X] artifacts
Deprecated: [Y] artifacts

Files saved to .olaf/data/practices/
============================================================
```

---

## Reference Files

This skill uses the same reference files as `init-standard-rules`:

| Category | Files |
|----------|-------|
| Core | file-template-consistency.md, role-taxonomy-drift.md, test-data-construction.md, ci-local-workflow-parity.md |
| Language-specific | rust-patterns.md, csharp-dotnet-patterns.md, cpp-patterns.md, go-patterns.md, svelte-patterns.md, angular-patterns.md, quarkus-patterns.md, spring-boot-patterns.md, nextjs-patterns.md |
| Architecture | module-boundaries-dependencies.md, cross-domain-communication.md, cross-cutting-hotspots.md, shared-kernel-drift.md |
| Quality | error-semantics.md, data-boundary-leakage.md, authorization-boundary.md, observability-contract.md |

Reference files are located at: `skills/init-standard-rules/references/`
