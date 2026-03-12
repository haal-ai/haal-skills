---
name: generate-training-program
description: >
  Generate a comprehensive, self-paced training program for onboarding new
  team members to any codebase. Produces up to 4 training tracks
  (language/framework, business domain, architecture, testing/QA) with
  hands-on exercises that reference real code in the repository. Works with
  any language, framework, or project size. Use when the user wants to
  create training materials for their team.
license: MIT
compatibility: Works with any AI coding agent (VS Code Copilot, Windsurf, Claude Code, Cursor, etc.)
metadata:
  author: olaf
  version: "1.1.0"
  tags: "training onboarding documentation exercises learning team education"
---

# Generate Training Program

## When to use this skill

Trigger phrases:
- "create a training program for this repo"
- "generate onboarding materials"
- "I need training for new team members"
- "build a self-paced training"
- "create learning tracks for this codebase"
- "help me onboard 10 new developers"
- "make a training plan based on this code"

## When NOT to use this skill

- If the user wants a presentation (slides), use `distill-docs-to-pptx` instead.
- If the user wants a code review or architecture assessment, just do it directly.
- If the user wants a single tutorial or how-to guide, write it directly.
- If the user wants to onboard themselves interactively, use `onboard-me` instead.

## Related Skills

- **onboard-me** — Interactive self-onboarding for a single person (live, conversational)
- **generate-tech-spec-from-code** — Generates technical specifications (can feed into Track 3)
- **generate-step-by-step-tutorial** — Creates a single tutorial (this skill creates a whole program)
- **distill-docs-to-pptx** — Turns documentation into slides (use for training presentations)
- **run-redocumentation** — Generates code documentation (complements training materials)

## Overview

This skill produces a structured, self-paced training program consisting of:

1. **README.md** — Landing page with philosophy, track overview, learning paths, prerequisites
2. **Track 1 — Language & Framework** — Learn the primary language/framework through real project code
3. **Track 2 — Business Domain** — Understand what the system does, its entities, workflows, rules
4. **Track 3 — Architecture & Performance** — System design, performance, scalability, observability
5. **Track 4 — Testing & Quality Assurance** — Test taxonomy, CI gates, load testing, quality practices

All training materials reference **real code** in the repository. Every module includes
hands-on exercises that are self-verifiable (compile, test pass, observable output).

### Adaptive Track Selection

Not every repository warrants all 4 tracks. Adapt track count to the project:

| Repository profile | Recommended tracks |
|---|---|
| Full-stack application with tests and CI | All 4 tracks |
| Library / SDK (small footprint) | Track 1 + Track 2 (merge 3 into 2) + Track 4 |
| Data pipeline / ETL | Track 1 + Track 2 + Track 3 (skip 4 if no tests) |
| Monorepo with multiple services | All 4 tracks, with a per-service appendix |
| Tiny project (< 20 files) | Single combined training document instead of 4 tracks |

When merging or skipping tracks, explain the rationale in the README.

## Output Location

All training files MUST be saved under:

```
<repo>/.olaf/work/trainings/<training-name>/
  README.md
  track-1-<language-or-framework>.md
  track-2-business-domain.md
  track-3-architecture.md
  track-4-testing-quality.md
```

The `<training-name>` folder is derived from the repository name, in kebab-case.

Example for a repo called `ofctf.product-server-poc`:
```
.olaf/work/trainings/product-server-poc/
  README.md
  track-1-learn-rust.md
  track-2-business-domain.md
  track-3-architecture.md
  track-4-testing-quality.md
```

If the user explicitly requests a different location, use that instead.

## Process

### Step 0 — Gather requirements from the user

Before doing any research, ask the user for training specificities. This step
is **mandatory** — do not skip it.

Use `vscode_askQuestions` if available, otherwise ask the questions interactively
in the conversation.

Ask the following questions (adapt wording to context):

| # | Question | Purpose | Default if not answered |
|---|----------|---------|----------------------|
| 1 | **Primary language/framework focus?** (e.g., "Rust", "Java + Spring Boot", "TypeScript + React") | Determines Track 1 content and overall ecosystem lens | Auto-detect from repo |
| 2 | **Team size & composition?** (how many newcomers, their backgrounds) | Calibrates depth and learning paths | "10 newcomers from mixed backgrounds" |
| 3 | **Time budget?** (e.g., "max 2 weeks", "a few days", "no constraint") | Controls module count and depth | "Practical — no more than 2-3 days per track" |
| 4 | **Any specific focus areas or topics to emphasize?** (e.g., "security is critical", "performance is key", "domain is complex") | Adjusts weighting of modules | Balanced across all tracks |
| 5 | **Any topics to skip or de-emphasize?** (e.g., "skip frontend", "no DevOps") | Avoids wasting space on irrelevant content | Nothing skipped |

If the user already provided some of this information in their initial request,
do not re-ask those questions. Only ask what's missing.

### Step 1 — Deep codebase research

This is the most critical step. Launch **three parallel research efforts** using
the `Explore` subagent (or equivalent codebase exploration tool). Each research
phase must gather precise, file-referenced material.

**Fallback strategy:** If the `Explore` subagent is not available, use
`file_search`, `grep_search`, and `semantic_search` directly to gather the same
information. The research quality is what matters, not the specific tool.

#### Research Phase A — Language Patterns Catalog

Goal: Identify idiomatic usage of the primary language/framework in the codebase.

Instructions for the Explore subagent:

> Thoroughly explore the codebase and produce a **language patterns catalog**.
> For each pattern, provide:
> - Pattern name
> - File path and line range where it appears
> - Brief explanation of why it's used
>
> Patterns to look for (adapt to the detected language):
>
> **For Rust repos:** ownership/borrowing (Arc, Rc, lifetimes), type system
> (newtypes, enums with data, const generics), traits (definition + impl,
> trait objects, async-trait, sealed pattern), error handling (anyhow vs
> thiserror, ? operator, bail!), macros (declarative + procedural), concurrency
> (tokio, rayon, channels, atomics, RwLock, DashMap), serde patterns
> (tagged unions, custom serializers, rename/skip/flatten), module system
> (pub(crate), feature flags, re-exports), CLI (clap derive), unsafe code.
>
> **For Java repos:** generics, streams, records, sealed interfaces, Spring
> annotations, dependency injection, exception handling, concurrency
> (virtual threads, CompletableFuture), build system (Maven/Gradle modules),
> design patterns (strategy, factory, builder).
>
> **For TypeScript/JavaScript repos:** type system (generics, discriminated
> unions, type guards, branded types), async/await patterns, React hooks
> or Angular signals, state management, module system, build tooling,
> testing patterns.
>
> **For Python repos:** type hints, dataclasses/pydantic, async/await,
> decorators, context managers, generators, packaging, virtual environments.
>
> **For Go repos:** interfaces, goroutines & channels, error handling patterns,
> stdlib usage, module system, struct embedding, context propagation,
> table-driven tests, build tags.
>
> **For C#/.NET repos:** generics, LINQ, async/await, dependency injection,
> middleware pipeline, Entity Framework patterns, record types, nullable
> reference types, minimal APIs vs controllers.
>
> **For Kotlin repos:** coroutines, extension functions, sealed classes,
> data classes, DSL builders, null safety, Flow/StateFlow, Spring/Ktor patterns.
>
> **For any other language:** identify the dominant paradigm (OOP, functional,
> procedural), look for common patterns (error handling, concurrency,
> serialization, configuration, module organization), and catalog at least
> 10 distinct patterns with code references.

#### Research Phase B — Business Domain Mapping

Goal: Understand the domain entities, their relationships, and the core workflow.

Instructions for the Explore subagent:

> Map the **business domain** of this codebase. Produce:
>
> 1. **Entity inventory**: All domain entities (structs, classes, models) with
>    file locations and field descriptions
> 2. **Entity relationships**: How entities reference each other (1:1, 1:N, N:M)
> 3. **Core workflow/pipeline**: The main business process from input to output
> 4. **Business rules**: Any rule engines, validators, or decision logic
> 5. **Data sources**: Where data comes from (files, APIs, databases, generators)
> 6. **Configuration**: What's configurable and where config files live
>
> For each entity, provide the file path, line range, and key fields.

#### Research Phase C — Testing & Quality Practices

Goal: Catalog all testing and quality infrastructure.

Instructions for the Explore subagent:

> Catalog the **testing and quality assurance** practices:
>
> 1. **Test inventory**: All test files, count of tests per file, test framework
> 2. **Test helpers/utilities**: Any builders, factories, DSL macros, fixtures
> 3. **CI pipeline**: All quality gates (lint, format, test, coverage, security)
> 4. **Pre-commit hooks**: Any hooks and what they check
> 5. **Load/stress tests**: Any performance testing scripts or configs
> 6. **E2E tests**: Any end-to-end testing (shell scripts, browser tests)
> 7. **Coverage tooling**: How coverage is measured and thresholds
> 8. **Gaps**: What types of tests are missing or underrepresented

### Step 2 — Create the README (landing page)

Create `README.md` in the training folder with this structure:

```markdown
# Training Program — Onboarding New Team Members

**Project**: <project name>
**Audience**: <from user input>
**Format**: Self-paced, exercise-driven, using this repository as the playground
**Time commitment**: Each track is 3–5 half-days. Tracks can be taken independently.

## Philosophy

- Learn by doing, not by reading
- The codebase IS the textbook
- Short feedback loops — exercises produce visible output within minutes
- Progressive difficulty — start reading code, end writing code

## Four Training Tracks

| # | Track | Who is it for? | Duration | Output |
|---|-------|---------------|----------|--------|
| 1 | [<Track 1 title>](track-1-<slug>.md) | <audience> | <N> half-days | <capability> |
| 2 | [<Track 2 title>](track-2-business-domain.md) | <audience> | <N> half-days | <capability> |
| 3 | [Architecture & Performance](track-3-architecture.md) | <audience> | <N> half-days | <capability> |
| 4 | [Testing & Quality](track-4-testing-quality.md) | <audience> | <N> half-days | <capability> |

## Recommended Learning Paths

<table with paths per background>

## Prerequisites

<language toolchain, build tools, how to generate test data>

## Exercise Verification

<explain that all exercises are self-verifiable>
```

### Step 3 — Create Track 1 (Language/Framework)

This track is the most variable — its content depends entirely on the primary
language/framework identified in Step 0.

**Structure requirements:**

- **5-6 modules** (one per half-day), each covering a core language concept
- Each module has **3 subsections** minimum, each with:
  - "Read these files" — specific file paths and line ranges
  - "Concepts to understand" — bullet list of what to learn
  - "Exercise" — a hands-on task verified by compile/test/run
- End with a **Self-Assessment Checklist** (10 items minimum)

**Module topics by language:**

| Language | Suggested modules |
|----------|------------------|
| Rust | Types & structs, Ownership & borrowing, Error handling, Traits & generics, Concurrency & async, Macros & serde |
| Java | Types & generics, OOP & patterns, Exception handling, Spring framework, Concurrency, Build & modules |
| TypeScript | Type system, Async/await, Framework patterns (React/Angular/Vue), State management, Module system, Tooling |
| Python | Type hints & dataclasses, OOP & patterns, Async patterns, Framework (Django/FastAPI), Packaging, Tooling |
| Go | Types & interfaces, Goroutines & channels, Error handling, Stdlib patterns, Modules, Testing |
| C# | Types & generics, LINQ & async, Dependency injection, .NET patterns, NuGet & projects, Testing |
| Kotlin | Coroutines, Extension functions, Sealed classes, DSL builders, Null safety, Spring/Ktor |
| Ruby | Metaprogramming, Blocks & procs, Rails conventions, Gems & bundler, Testing (RSpec), Active Record |
| PHP | Type system, Composer, Laravel/Symfony patterns, Middleware, ORM patterns, Testing (PHPUnit) |
| Swift | Protocols, Closures, Optionals, Concurrency (async/await), SwiftUI/UIKit, Package Manager |
| Other | Identify dominant paradigm, core patterns, error handling, concurrency model, module system, tooling |

Always adapt to what's actually in the codebase — don't invent patterns that aren't there.

### Step 4 — Create Track 2 (Business Domain)

This track is about understanding **what the system does**, not how it's coded.

**Structure requirements:**

- **3-4 modules** (one per half-day)
- Module 1: Core entities (what are the main nouns?)
- Module 2: Relationships and rules (how do entities interact?)
- Module 3: The main workflow/pipeline (end-to-end data flow)
- Module 4 (optional): Data generation, configuration, edge cases
- Each module must include:
  - Entity/concept tables with definitions
  - File references for each entity
  - At least 2 exercises (trace a workflow, create test data, modify a rule)
- End with a **Domain Glossary** (all domain terms defined)
- End with a **Self-Assessment Checklist**

### Step 5 — Create Track 3 (Architecture & Performance)

This track covers system design, not business logic.

**Structure requirements:**

- **4 modules** (one per half-day)
- Module 1: System structure (workspace/project layout, dependency graph, module boundaries)
- Module 2: Data storage & query patterns (how data is stored, indexed, queried)
- Module 3: Concurrency & hot path (threading, async, locks, lock-free paths)
- Module 4: Observability & deployment (metrics, logging, Docker, CI/CD, security)
- Each module must include:
  - Architecture diagrams (ASCII/Mermaid)
  - Decision tables (what/why/alternatives/trade-offs)
  - At least 2 exercises (run a benchmark, trace a hot path, review security)
- End with an **Architecture Decision Records** summary table
- End with a **Self-Assessment Checklist**

### Step 6 — Create Track 4 (Testing & Quality)

This track covers all QA practices.

**Structure requirements:**

- **3 modules** (one per half-day)
- Module 1: Unit testing (how to write tests in this repo, test helpers, test DSLs)
- Module 2: CI quality gates (linting, formatting, Clippy/ESLint, coverage, pre-commit)
- Module 3: Integration tests, E2E tests, load tests (k6, Playwright, shell scripts)
- Include a **Quality Improvement Exercises** section with real gaps to fill
- Include a **Continuous Improvement Plan** (quick wins, medium effort, larger initiatives)
- End with a **Self-Assessment Checklist**

### Step 7 — Final validation

After creating all 5 files, verify:

1. All file cross-references are valid (links between tracks, links to README)
2. All code references point to files that exist (verify with `file_search`)
3. Exercise instructions are actionable (specific commands to run)
4. Each track has at least 6 exercises total
5. Each track ends with a Self-Assessment Checklist of 8+ items
6. The README learning paths table covers at least 3 different backgrounds

## Quality Principles

### Exercise Design

Every exercise MUST be:
- **Self-verifiable**: Produces a clear pass/fail signal (test passes, compiles, output matches)
- **Scoped**: Completable in 15-30 minutes
- **Progressive**: Within each module, exercises build on each other
- **Real**: Operates on the actual codebase, not toy examples

Exercise types (use a mix):
| Type | Description | Verification |
|------|-------------|-------------|
| Read & trace | Follow a code path and document what you find | Written answer matches expected |
| Add a field/method | Extend existing code and fix all compilation errors | `compile` passes |
| Write a test | Test existing behavior | `test` passes |
| Modify & observe | Change a parameter and observe the effect | Measurable difference |
| Break & fix | Intentionally break something, observe the error, fix it | `compile`/`test` passes |
| Create new | Write a new function, type, or module | `test` passes |

### Code References

Every "Read these files" section must include:
- Exact file path relative to repo root (e.g., `crates/ofc-models/src/flight.rs`)
- Line range when relevant (e.g., "lines 208–244")
- Brief description of what to look for

Never reference files without verifying they exist.

### Tone and Style

- Second person ("you") — direct address to the trainee
- Present tense — "This struct represents..." not "This struct represented..."
- Tables over prose — for comparisons, inventories, concept definitions
- Code snippets — short, focused, from the actual codebase
- No fluff — every sentence teaches something or directs an action

## Adaptation Guidelines

The skill must adapt to any technology stack. Here's how each track flexes:

| Track | What changes | What stays constant |
|-------|-------------|-------------------|
| Track 1 | Language, frameworks, patterns, tools | Structure (modules → read → exercise → checklist) |
| Track 2 | Domain entities, terminology, workflows | Structure (entities → relationships → pipeline → glossary) |
| Track 3 | Storage tech, concurrency model, deployment | Structure (layout → data → concurrency → ops) |
| Track 4 | Test frameworks, CI tools, linters | Structure (unit → CI → integration → improvement plan) |

## Example Track 1 Titles by Language

| Language | Track 1 title | Example modules |
|----------|--------------|----------------|
| Rust | "Learn Rust via This Project" | Ownership, Traits, Error handling, Macros, Async |
| Java | "Learn Modern Java via This Project" | Generics, Streams, Spring DI, Virtual threads, Records |
| TypeScript | "Learn TypeScript via This Project" | Type system, Async, React/Angular patterns, State mgmt |
| Python | "Learn Python via This Project" | Type hints, Dataclasses, Async, FastAPI/Django, Packaging |
| Go | "Learn Go via This Project" | Interfaces, Goroutines, Error handling, Stdlib, Modules |
| C# | "Learn C# via This Project" | Generics, LINQ, Async, DI, .NET patterns, Testing |
| Kotlin | "Learn Kotlin via This Project" | Coroutines, Extensions, Sealed classes, DSLs, Null safety |
| Ruby | "Learn Ruby via This Project" | Metaprogramming, Blocks, Rails, Active Record, RSpec |
| PHP | "Learn PHP via This Project" | Types, Composer, Laravel/Symfony, Middleware, PHPUnit |
| Swift | "Learn Swift via This Project" | Protocols, Optionals, Concurrency, SwiftUI/UIKit |
| Other | "Learn <Language> via This Project" | Adapt modules to the language's core concepts |

## Error Handling & Edge Cases

| Situation | How to handle |
|---|---|
| **Very small repo** (< 20 files) | Produce a single combined training document instead of 4 separate tracks. Explain why in a note. |
| **No tests in the repo** | Skip Track 4 or reduce it to a single module on "How to add tests to this project" with exercises that create the first tests. |
| **Multiple languages** (polyglot repo) | Create Track 1 for the primary language. Add an appendix covering the secondary language(s) with key patterns only. |
| **No CI pipeline** | In Track 4, replace the CI module with "Setting up CI for this project" — a constructive exercise. |
| **Extremely large monorepo** | Focus the training on the service/module the user specifies. Ask which area to target if unclear. |
| **Missing domain knowledge** | If the domain is unclear from code alone, note it honestly and suggest the trainee pair with a domain expert for Track 2. |
| **Language not in the table** | Use the "Other" row as a template. Identify the language's paradigm and core concepts from the codebase itself. |
| **User wants only one track** | Generate only the requested track plus a minimal README. Do not force all 4 tracks. |
| **Research phase finds very little** | Reduce module count and depth proportionally. A 3-module track is better than 6 modules of padding. |
