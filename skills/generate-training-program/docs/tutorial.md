# Generate Training Program: Step-by-Step Tutorial

**How to Generate a Complete Onboarding Training Program from Any Codebase**

This tutorial walks you through using the `generate-training-program` skill to produce a structured, self-paced training program that helps new team members learn a codebase through hands-on exercises grounded in real code.

## Prerequisites

- A codebase (repository) to analyze — any language, any size
- An AI coding agent with codebase exploration capabilities
- Basic understanding of your project's purpose and technology stack
- Terminal access for exercise verification

## Estimated Time

- **Requirements gathering**: 5 minutes
- **Research & generation**: 15-30 minutes (depending on repo size)
- **Review & refinement**: 10-15 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Say one of the following to your AI agent:

```
create a training program for this repo
```

```
generate onboarding materials for new team members
```

```
build a self-paced training based on this codebase
```

You can also be more specific upfront:

```
Create a training program for this repo. 
We're onboarding 8 Java developers who are new to our Spring Boot codebase.
They have 2 weeks and security is a priority.
```

The more context you give upfront, the fewer questions the agent will ask.

### Step 2: Answer the Requirements Questions

The agent will ask up to 5 questions to calibrate the training. Here's what to expect and how to answer:

**Question 1: Primary language/framework focus?**

> Tell the agent which technology to focus Track 1 on.

Example answers:
- "Rust" — focuses on ownership, traits, async
- "Java + Spring Boot" — focuses on DI, annotations, records
- "TypeScript + React" — focuses on hooks, state management, type system
- "auto-detect" — let the agent figure it out from the repo

**Question 2: Team size & composition?**

> How many newcomers and what's their background?

Example answers:
- "5 junior developers straight from bootcamp"
- "10 senior engineers from a Python background"
- "3 architects doing a code review"
- "mixed — some senior, some junior"

**Question 3: Time budget?**

> How long can each person spend on training?

Example answers:
- "max 1 week total" — agent produces shorter tracks
- "2-3 days per track" — standard depth (default)
- "no constraint" — agent produces comprehensive training
- "half a day quick overview" — agent may combine tracks

**Question 4: Any specific focus areas?**

> What matters most to your team?

Example answers:
- "security is critical — emphasize it in every track"
- "performance and scalability are key concerns"
- "domain logic is complex — spend more time on Track 2"
- "nothing specific, keep it balanced"

**Question 5: Topics to skip or de-emphasize?**

> Anything you don't want covered?

Example answers:
- "skip frontend — we only care about the backend"
- "no DevOps — another team handles deployment"
- "skip testing — we'll do a separate testing workshop"
- "nothing to skip"

### Step 3: Wait for Codebase Research

The agent now performs three parallel research phases. This is the most intensive part — the agent will:

1. **Catalog language patterns** — Finds 10+ idiomatic patterns in your code (error handling, concurrency, design patterns, etc.) with exact file paths and line ranges
2. **Map the business domain** — Identifies all entities, their relationships, the core workflow, business rules, and configuration
3. **Audit testing practices** — Inventories all tests, CI quality gates, test helpers, coverage tooling, and identifies gaps

You'll see the agent exploring files, running searches, and building its understanding. This typically produces 50-100 specific code references that flow into the training materials.

### Step 4: Review the README (Landing Page)

The agent creates a `README.md` as the training program's landing page. Review it for:

- **Philosophy section** — Does it match your team's learning culture?
- **Track overview table** — Are all tracks relevant? (Small repos may have fewer tracks)
- **Learning paths** — Are the suggested paths realistic for your team backgrounds?
- **Prerequisites** — Is everything listed that newcomers need to install?

**Example README structure:**

```markdown
# Training Program — Onboarding New Team Members

**Project**: product-server
**Audience**: 10 developers, mixed backgrounds
**Format**: Self-paced, exercise-driven

## Four Training Tracks

| # | Track | Duration | Output |
|---|-------|----------|--------|
| 1 | Learn Rust via This Project | 3 half-days | Can read and modify Rust code |
| 2 | Business Domain | 2 half-days | Understand entities and workflows |
| 3 | Architecture & Performance | 3 half-days | Navigate system design decisions |
| 4 | Testing & Quality | 2 half-days | Can write tests and use CI |

## Learning Paths

| Background | Recommended order |
|---|---|
| Experienced Rust developer | 2 → 3 → 4 (skip 1) |
| Java/Python developer | 1 → 2 → 3 → 4 |
| QA engineer | 4 → 2 → 3 |
```

### Step 5: Review Each Track

Each track is a standalone markdown file. Here's what to check:

**Track 1 — Language/Framework:**
- Are the 5-6 modules covering the right language concepts for your team?
- Do the "Read these files" sections point to real files that exist?
- Are the exercises practical and self-verifiable?
- Does the self-assessment checklist cover the key competencies?

**Track 2 — Business Domain:**
- Are all major entities identified with correct file references?
- Does the domain glossary cover all important terms?
- Are the workflows described accurately?
- Will a newcomer understand what the system *does* after completing this?

**Track 3 — Architecture:**
- Are the architecture diagrams (ASCII/Mermaid) accurate?
- Do the decision tables explain *why*, not just *what*?
- Are concurrency and performance exercises safe to run?

**Track 4 — Testing & QA:**
- Does the test inventory match reality?
- Are the CI quality gates documented accurately?
- Do the "quality improvement exercises" target real gaps?

### Step 6: Request Adjustments

If anything needs changing, tell the agent specifically:

```
Track 1 Module 3 is too advanced for our team — 
simplify the concurrency exercises and add more basic examples.
```

```
Add a module on database migrations to Track 2 — 
that's a big part of our domain.
```

```
Track 4 should mention our Playwright E2E tests in tests/e2e/.
```

### Step 7: Distribute to Your Team

The training program lives in `.olaf/work/trainings/<training-name>/`. To share it:

**Option A: Commit to repo**
```bash
git add .olaf/work/trainings/
git commit -m "Add onboarding training program"
git push
```

**Option B: Copy to a shared location**
```bash
cp -r .olaf/work/trainings/<training-name>/ /shared/training/
```

**Option C: Generate a presentation**
Use the `distill-docs-to-pptx` skill to create a slide deck from the README for a kick-off meeting.

## Verification Checklist

After generation, verify:

- [ ] README.md has a learning paths table with at least 3 backgrounds
- [ ] Each track has 3-6 modules with exercises
- [ ] All "Read these files" references point to existing files
- [ ] Each exercise has clear verification instructions (compile, test, observe)
- [ ] Each track ends with a Self-Assessment Checklist (8+ items)
- [ ] Track 2 includes a Domain Glossary
- [ ] Track 3 includes at least one architecture diagram
- [ ] Cross-references between tracks are valid links

## Troubleshooting

### "The agent produced fewer than 4 tracks"

This is intentional for small or specialized repos. A library with 15 files doesn't need a full architecture track. Check the README for the agent's rationale.

### "Code references point to files that don't exist"

Ask the agent to re-validate: "Please verify all file references in the training program." The agent will use `file_search` to confirm each path.

### "Exercises are too hard / too easy"

Tell the agent your team's level and ask for recalibration: "Our team is all junior — simplify the exercises in Track 1 and add more guided examples."

### "Domain track is shallow"

If the business domain is complex but poorly documented in code, the agent may not have enough signals. Consider: "Add these domain concepts to Track 2: [list]" or pair the training with a domain expert walkthrough.

### "Training takes too long for our time budget"

Ask the agent to reduce scope: "Compress the whole program into a 2-day training — combine tracks and keep only the essential exercises."

## Example Walkthrough

### Scenario: Spring Boot microservice, 8 new Java developers, 2 weeks

**You say:**
```
Create a training program for this repo. We're onboarding 8 Java developers 
who have Spring experience but are new to this codebase. They have 2 weeks.
Focus on the domain — it's complex. Skip DevOps.
```

**Agent asks:** (only what's missing)
```
Got it. A few quick questions:
1. Any specific areas to emphasize beyond domain? (e.g., security, performance)
2. Should I cover the test suite in depth, or just an overview?
```

**You answer:**
```
1. Security — we handle PII data
2. Full depth on testing — we have gaps to fill
```

**Agent generates:**
```
.olaf/work/trainings/payment-service/
  README.md                      — Landing page, 2-week schedule
  track-1-learn-java-spring.md   — 5 modules, Spring Boot patterns
  track-2-business-domain.md     — 4 modules, PII handling, glossary
  track-3-architecture.md        — 3 modules (no DevOps, as requested)
  track-4-testing-quality.md     — 3 modules, security testing emphasis
```

**Training highlights:**
- Track 1 includes a module on Spring Security annotations in the codebase
- Track 2 has a "PII Data Flow" exercise tracing sensitive data through the system
- Track 3 skips the deployment module (DevOps excluded)
- Track 4 includes "Security Testing Gaps" with exercises to write missing tests

## Best Practices

1. **Run it early** — Generate the training before the new team members arrive, not the day they join
2. **Review with a senior** — Have an experienced team member review the generated content
3. **Iterate** — Use the training program, collect feedback, and regenerate with improvements
4. **Pair with live sessions** — The training is self-paced, but a weekly Q&A session accelerates learning
5. **Keep it fresh** — Regenerate after major refactors or architectural changes
6. **Start small** — For a first run, try it on a small service before tackling the monorepo

## Integration with Other Skills

| Workflow step | Skill to use |
|---|---|
| Generate the training program | `generate-training-program` (this skill) |
| Create a kick-off presentation | `distill-docs-to-pptx` from the README |
| Generate deep tech specs for Track 3 | `generate-tech-spec-from-code` |
| Create individual how-to guides | `generate-step-by-step-tutorial` |
| Update documentation after training feedback | `run-redocumentation` |
| Interactive onboarding for one person | `onboard-me` |
