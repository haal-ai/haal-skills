---
name: init-standard-rules
description: Analyze codebase patterns and generate standards & rules for OLAF practices
license: Apache-2.0
metadata:
  olaf_tags: [onboarding, analysis, standards, rules, practices, patterns]
  copyright: Copyright (c) 2026 Haal AI
  author: Haal AI
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

# init-standard-rules

Action skill. Provides **codebase analysis for standards and rules**:
1. Analyzes codebase for patterns
2. Generates Standards and Rules
3. Saves to `.olaf/data/practices/` for immediate use

**Local-only:** No cloud service required. All outputs saved locally.

## Guarantees

- **Read-only analysis.** Analysis phase does not modify any project files.
- **Evidence required.** Every reported insight must include file-path evidence (and line ranges when feasible).
- **Focused output.** Max **5 Standards** and **5 Rules** generated per run.
- **Graceful failure.** Partial failures don't lose successful work.
- **No drafts.** Outputs are saved directly to practices folder, not as drafts.

## Definitions

- **Pattern (non-linter):** a convention a linter cannot reliably enforce (module boundaries, cross-domain communication, workflow parity, error semantics, etc).
- **Evidence:** `path[:line-line]` entries; omit line ranges only when the file isn't text-searchable.
- **Standard:** A coding standard with rules and examples.
- **Rule:** A standalone rule that can be applied across the codebase.

---

## Step 0 — Introduction

Print exactly:

```
I'll analyze your codebase to discover patterns and generate standards & rules. This usually takes ~3 minutes.
```

---

## Step 1 — Detect Existing OLAF Configuration

Before analyzing, detect and preserve any existing OLAF configuration.

### Glob (broad, future-proof)
Glob for markdown in these roots (recursive):
- `.olaf/**/*.md`
- `.claude/**/*.md`
- `.windsurf/**/*.md`
- `.cursor/**/*.md`
- `.github/instructions/**/*.md`

### Classify
Classify found files into counts:
- **standards**: `.olaf/data/practices/standards/**/*.md`
- **rules**: `.olaf/data/practices/rules/**/*.md`
- **other_docs**: any markdown under agent directories

If any exist, print exactly:

```
Existing OLAF/agent docs detected:

    Standards: [N]

    Rules: [M]

    Other docs: [P]
```

No overwrites. New files will be added next to the existing ones.

---

## Step 2 — Detect Project Stack (Minimal, Evidence-Based)

### Language markers (check presence)
- JS/TS: `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `tsconfig.json`
- Python: `pyproject.toml`, `requirements.txt`, `setup.py`
- Go: `go.mod`
- Rust: `Cargo.toml`
- Ruby: `Gemfile`
- JVM: `pom.xml`, `build.gradle`, `build.gradle.kts`
- .NET: `*.csproj`, `*.sln`
- PHP: `composer.json`
- C/C++: `CMakeLists.txt`, `Makefile`, `*.cpp`, `*.h`

### Architecture markers (check directories)
- Hexagonal/DDD: `src/application/`, `src/domain/`, `src/infra/`
- Layered/MVC: `src/controllers/`, `src/services/`
- Monorepo: `packages/`, `apps/`
- Tauri: `src-tauri/`
- SvelteKit: `src/routes/`
- Next.js: `app/`, `pages/`, `src/app/`
- Clean Architecture: `src/entities/`, `src/usecases/`
- Microservices: `services/`, `apps/service-*/`
- Quarkus: `src/main/resources/application.properties`, `quarkus-app/`, `@QuarkusMain`
- Spring Boot: `src/main/resources/application.yml`, `@SpringBootApplication`

Print exactly:

```
Stack detected (heuristic):

    Languages: [..]

    Repo shape: [monorepo|single]

    Architecture markers: [..|none]
```

---

## Step 3 — Run Analyses

Read each reference file for detailed search patterns, thresholds, and insight templates.

### Core Analyses

| Analysis | Reference File | Output focus |
|----------|----------------|--------------|
| File Template Consistency | `references/file-template-consistency.md` | Rules |
| CI/Local Workflow Parity | `references/ci-local-workflow-parity.md` | Rules |
| Role Taxonomy Drift | `references/role-taxonomy-drift.md` | Standards |
| Test Data Construction | `references/test-data-construction.md` | Standards |

### Language-Specific Analyses

| Analysis | Reference File | Languages |
|----------|----------------|-----------|
| Rust Patterns | `references/rust-patterns.md` | Rust |
| C#/.NET Patterns | `references/csharp-dotnet-patterns.md` | C# |
| C/C++ Patterns | `references/cpp-patterns.md` | C, C++ |
| Svelte Patterns | `references/svelte-patterns.md` | Svelte |
| Angular Patterns | `references/angular-patterns.md` | Angular |
| Go Patterns | `references/go-patterns.md` | Go |
| Quarkus Patterns | `references/quarkus-patterns.md` | Quarkus |
| Spring Boot Patterns | `references/spring-boot-patterns.md` | Spring Boot |
| Next.js Patterns | `references/nextjs-patterns.md` | Next.js |

**Selection logic:**
- If `Cargo.toml` detected → run `rust-patterns.md`
- If `*.csproj` or `*.sln` detected → run `csharp-dotnet-patterns.md`
- If `CMakeLists.txt` or `*.cpp` detected → run `cpp-patterns.md`
- If `*.svelte` files detected → run `svelte-patterns.md`
- If `*.component.ts` with `@Component` detected → run `angular-patterns.md`
- If `go.mod` detected → run `go-patterns.md`
- If `@QuarkusMain` or `quarkus-app/` detected → run `quarkus-patterns.md`
- If `@SpringBootApplication` detected → run `spring-boot-patterns.md`
- If `app/` with `page.tsx` or `pages/` detected → run `nextjs-patterns.md`

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

## Step 4 — Generate Standards & Rules

Generate all files in one batch, using the formats defined below.

### Standard Format

For each Standard insight, create a Markdown file at `.olaf/data/practices/standards/<slug>-standard-.md`:

> **Naming convention:** All standard files MUST include `-standard-` in the filename. This marker is used by `generate-linters` to discover lintable standards.

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

### Rule Format

For each Rule insight, create a Markdown file at `.olaf/data/practices/rules/<slug>-standard-.md`:

> **Naming convention:** All rule files MUST include `-standard-` in the filename. This marker is used by `generate-linters` to discover lintable rules.

```markdown
# Rule Name

What the rule enforces and why.

## Applies to

- File patterns or contexts where this rule applies

## Description

Detailed description of the rule.

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

### Generation Rules

- Generate files **only from discovered insights** (no invention)
- Use evidence from analysis to populate rules/steps
- Cap output: max **5 Standards** + **5 Rules**
- Never overwrite existing files; append `-2`, `-3`, etc. if slug exists

---

## Step 5 — Present Summary

Present the generated files:

```
============================================================
  ANALYSIS COMPLETE
============================================================

Stack detected: [languages], [monorepo?], [architecture markers]
Analyses run: [N] checks

STANDARDS CREATED ([N]):
  1. [Name] → .olaf/data/practices/standards/[slug]-standard-.md
  2. ...

RULES CREATED ([M]):
  1. [Name] → .olaf/data/practices/rules/[slug]-standard-.md
  2. ...

Files are ready for use in .olaf/data/practices/
============================================================
```

---

## Step 6 — No Patterns Discovered

If analysis found no patterns:

```
============================================================
  ℹ️ NO PATTERNS DISCOVERED
============================================================

The analysis didn't find enough recurring patterns to generate standards or rules.

This can happen with smaller codebases or projects with very diverse coding styles.
You can try again later as the codebase grows.
============================================================
```

---

## Output Directory Structure

After running this skill, the `.olaf/data/practices/` directory will contain:

```
.olaf/data/practices/
├── standards/
│   ├── tool-adapter-pattern-standard-.md
│   ├── error-handling-pattern-standard-.md
│   └── ...
└── rules/
    ├── use-test-factories-standard-.md
    ├── ci-local-parity-standard-.md
    └── ...
```

These files can be:
1. Reviewed and edited by the user
2. Converted to agent-specific formats by other skills
3. Stored in a haal-skills registry for distribution
