# generate-training-program

## Overview

Generates a comprehensive, self-paced training program for onboarding new team members to any codebase. The skill deeply analyzes the repository, then produces up to 4 training tracks — each with hands-on exercises that reference real code — so newcomers learn by doing, not just reading.

## Purpose

This skill exists to solve the "blank page" onboarding problem: a new developer joins a team, clones a repo, and has no structured path to understand it. Instead of relying on tribal knowledge or outdated wikis, this skill produces a training program that is:

- **Grounded in real code** — every exercise references actual files and line ranges
- **Self-paced** — trainees work independently at their own speed
- **Self-verifiable** — exercises produce observable output (compile, test pass, visible change)
- **Adaptive** — works with any language, framework, or project size

## Key Features

- **Multi-language support**: Rust, Java, TypeScript, Python, Go, C#, Kotlin, Ruby, PHP, Swift, and any other language via generic fallback
- **4 training tracks**: Language/framework, business domain, architecture, testing/QA
- **Adaptive track selection**: Automatically adjusts track count based on repository profile (full app, library, monorepo, tiny project)
- **Deep codebase research**: Three parallel research phases gather language patterns, domain entities, and testing practices
- **Interactive requirements gathering**: Asks about team size, time budget, focus areas before generating
- **Self-assessment checklists**: Every track ends with a checklist trainees use to verify their understanding
- **Domain glossary**: Track 2 produces a glossary of all business terms
- **Architecture diagrams**: Track 3 includes ASCII/Mermaid diagrams of the system

## Usage

Invoke this skill by saying:
- "create a training program for this repo"
- "generate onboarding materials"
- "I need training for new team members"
- "build a self-paced training"
- "create learning tracks for this codebase"
- "help me onboard 10 new developers"
- "make a training plan based on this code"

## Parameters

### Required
1. **codebase**: The repository to analyze (typically the current workspace)

### Optional (collected interactively)
2. **language_focus**: string — Primary language/framework (auto-detected if not specified)
3. **team_size**: string — Number of newcomers and their backgrounds (default: "10 from mixed backgrounds")
4. **time_budget**: string — Time constraint per track (default: "2-3 days per track")
5. **focus_areas**: string — Topics to emphasize (default: balanced)
6. **skip_topics**: string — Topics to de-emphasize or skip (default: none)

## Process Flow

1. **Requirements Gathering** — Asks user about language, team, time budget, and focus areas
2. **Deep Codebase Research** — Three parallel research phases:
   - Phase A: Language patterns catalog (10+ patterns with file references)
   - Phase B: Business domain mapping (entities, relationships, workflows)
   - Phase C: Testing & quality practices (test inventory, CI pipeline, gaps)
3. **README Generation** — Landing page with philosophy, track overview, learning paths, prerequisites
4. **Track 1 — Language/Framework** — 5-6 modules, each with read/exercise/checklist sections
5. **Track 2 — Business Domain** — 3-4 modules covering entities, rules, workflows, glossary
6. **Track 3 — Architecture** — 4 modules on system structure, data, concurrency, observability
7. **Track 4 — Testing & QA** — 3 modules on unit tests, CI gates, integration/E2E tests
8. **Final Validation** — Verifies all cross-references, code links, exercise actionability

## Output

A complete training program saved to `.olaf/work/trainings/<training-name>/`:

```
README.md                          — Landing page and learning paths
track-1-<language-or-framework>.md — Language & framework fundamentals
track-2-business-domain.md         — Domain entities, workflows, glossary
track-3-architecture.md            — System design, diagrams, decisions
track-4-testing-quality.md         — Testing practices and quality gates
```

Each track contains:
- 3-6 modules (depending on content density)
- Multiple exercises per module (read & trace, write code, break & fix)
- File references pointing to real code with line ranges
- Self-assessment checklist (8+ items)

## Examples

### Full-stack Java application
- Team: 15 new hires with Java background
- Output: All 4 tracks, Track 1 focused on Spring Boot patterns

### Small Python library
- Team: 3 senior developers from another team
- Output: Tracks 1 + 2 combined, Track 4 (testing was the concern)

### Rust monorepo with multiple services
- Team: 10 developers new to Rust
- Output: All 4 tracks, with per-service appendix in Track 3

## Error Handling

- **Very small repo (< 20 files)**: Produces a single combined document instead of 4 tracks
- **No tests found**: Skips Track 4 or converts it to "How to add tests" exercises
- **Multiple languages (polyglot)**: Focuses Track 1 on primary language, adds appendix for others
- **No CI pipeline**: Replaces CI module with constructive "Setting up CI" exercises
- **Large monorepo**: Asks user which service/module to focus on
- **Unknown language**: Uses generic fallback — identifies paradigm and core patterns from code
- **User wants partial output**: Generates only requested tracks plus minimal README

## Related Skills

- **onboard-me** — Interactive self-onboarding for a single person (live, conversational)
- **generate-tech-spec-from-code** — Generates technical specifications (can feed into Track 3)
- **generate-step-by-step-tutorial** — Creates a single tutorial (this skill creates a whole program)
- **distill-docs-to-pptx** — Turns documentation into slides (use for training presentations)
- **run-redocumentation** — Generates code documentation (complements training materials)
