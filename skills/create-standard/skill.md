---
name: create-standard
description: Create a coding standard from user intent with clarifying questions. Use when users want to define a new coding convention, best practice, or guideline. Triggers on "create a standard", "define a convention", "add a coding rule". Question-first approach for top-down standardization.
license: Apache-2.0
metadata:
  olaf_tags: [standards, conventions, guidelines, documentation, create]
  copyright: Copyright (c) 2026 Haal AI
  author: Haal AI
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

# Create Standard

Create a coding standard from user intent through a question-first approach. Generate standards that can be deployed to multiple AI tools (Claude, Cursor, Copilot, Windsurf).

**Question-first philosophy:** Clarify intent before drafting. Suitable for top-down standardization when defining new conventions.

## Output Paths by Tool

Standards are saved to tool-specific locations:

| Tool | Standard Path | Format |
|------|---------------|--------|
| **Claude** | `.claude/rules/standards/<slug>.md` | Markdown |
| **Cursor** | `.cursor/rules/standards/<slug>.mdc` | Markdown with frontmatter |
| **Copilot** | `.github/instructions/standard-<slug>.instructions.md` | GitHub instructions |
| **Windsurf** | `.windsurf/rules/standards/<slug>.md` | Markdown |
| **OLAF Central** | `.olaf/data/practices/standards/<slug>.md` | Markdown (source of truth) |

**Default:** Save to `.olaf/data/practices/standards/` as source of truth, then offer to deploy to specific tools.

## Scope: Global vs Workspace vs Per-Repo

Before saving, ask the user:

**"Should this standard apply to:"**
- **Home (Global)** — All workspaces and repos (save to user home directory)
- **Workspace** — All repos in current workspace (save to workspace root)
- **Per-repo** — Only a specific repository (save to repo root)

### Output Paths by Scope

| Scope | OLAF Path | Tool Paths |
|-------|-----------|------------|
| **Home (Global)** | `~/.olaf/data/practices/standards/` | `~/.claude/`, `~/.cursor/`, etc. |
| **Workspace** | `<workspace>/.olaf/data/practices/standards/` | `<workspace>/.claude/`, `<workspace>/.cursor/`, etc. |
| **Per-repo** | `<repo>/.olaf/data/practices/standards/` | `<repo>/.claude/`, `<repo>/.cursor/`, etc. |

**Default:** Per-repo (current repository)

---

## Step 1 — Clarify the Request

Gather essential information before drafting the standard.

### Clarification Flow

Study the user's request and identify critical gaps. The number of questions should match the request clarity:
- **1-2 questions** when the request is well-defined (clear scope, specific examples, detailed context)
- **3-5 questions** when the context is unclear or the request is vague

**Examples of focused questions:**
- "Which service or file shows the expected pattern?"
- "Is there an existing doc or rule we must stay aligned with?"
- "What specific aspect matters most (naming conventions, error handling, testing style)?"
- "Which language/framework does this apply to?"
- "Should this apply to all files or specific paths?"

Introduce questions with a simple phrase about needing clarification, then list as bullet points—no numbering, no category headers.

### Repository Access Guardrail

**Do not open or scan repository files unless the user explicitly points to them** (provides file paths or requests project-wide review). If source references are needed, ask the user to supply them.

### What to Capture

Take brief notes on:
- Title or slug (if mentioned)
- Scope guardrails
- Key references
- Expected outcomes

Keep notes concise—just enough to unlock drafting.

---

## Step 2 — Draft Standard in Markdown

Transform the understanding into a complete markdown draft with rules and examples.

### Draft Creation

1. Create a draft markdown file in `.olaf/data/practices/standards/_drafts/` (create the folder if missing) using filename `<slug>.md` (lowercase with hyphens)
2. Draft structure:
   - `# <Standard Title>` (Title Case, 2–5 words)
   - `## Description` — what the standard covers and why it exists
   - `## Scope` — comma-separated glob patterns (required)
   - `## Rules` — each rule as a `### <rule text>` subsection
   - For each rule that benefits from code examples, add:
     - `#### Good` with a language-annotated code block showing the compliant approach
     - `#### Bad` with a language-annotated code block showing the anti-pattern

### Standard Template

```markdown
# [Standard Title]

## Description

[What the standard covers and why it exists - 1-2 paragraphs]

## Scope

[Comma-separated glob patterns, e.g., **/*.ts, **/*.spec.ts]

## Rules

### [Rule 1 - action verb, max 25 words]

[Optional clarification or inline examples]

#### Good

```[language]
// Valid code example
```

#### Bad

```[language]
// Invalid code example
```

### [Rule 2 - action verb, max 25 words]

[Additional rules as needed...]
```

### Rule Writing Guidelines

1. **Start with an action verb** - Use imperative form (e.g., "Use", "Avoid", "Prefer", "Include")
2. **Be concise** - Max ~25 words per rule
3. **Be specific and actionable** - Avoid vague guidance
4. **Focus on one concept** - One rule per convention

#### Avoid Rationale Phrases

Rules describe **WHAT** to do, not **WHY**. Strip justifications and benefits—let examples demonstrate value.

**Bad (includes rationale):**
> Document props with JSDoc comments to improve developer experience.

**Good (action only):**
> Document component props with JSDoc comments (`/** ... */`) describing purpose and defaults.

#### Rule Splitting

If a rule addresses 2+ distinct concerns, **proactively split** it into separate rules.

**Bad (too broad):**
> Create centralized color constants for consistent palettes using semantic naming.

**Good (split):**
- Define color constants in `theme/colors.ts` using semantic names
- Use semantic color tokens instead of literal hex values

### Examples Guidelines

- Examples should be realistic and directly relevant
- Keep code snippets minimal—only include what's necessary
- Annotate every code block with its language (e.g., `typescript`, `python`, `go`)

Valid language values:
- `typescript`, `javascript`, `tsx`, `jsx`
- `python`, `java`, `go`, `rust`, `csharp`
- `php`, `ruby`, `kotlin`, `swift`, `dart`, `sql`
- `html`, `css`, `scss`, `yaml`, `json`
- `markdown`, `bash`

---

## Step 3 — Review Before Saving

**Before saving**, get explicit user approval:

1. **Display a formatted recap** of the standard content:

```
---
Name: <standard name>

Description: <description>

Scope: <scope>

Rules:

1. <rule content>
   - ✓ <good example>
   - ✗ <bad example>
2. <rule content>
   - ✓ <good example>
   - ✗ <bad example>
...
---
```

2. **Provide the file path** to the draft markdown file so users can open and edit it.

3. Ask: **"Here is the standard draft. The file is at `<path>` if you want to edit it. Do you approve?"**

4. **Wait for explicit user confirmation** before proceeding.

5. If the user requests changes, go back to Step 2 to make adjustments.

---

## Step 4 — Save Standard

After approval:

1. **Re-read the draft file** from disk to capture any user edits.

2. **Save to source of truth:**
   - Move from `_drafts/` to `.olaf/data/practices/standards/<slug>.md`

3. **Ask which tools to deploy to:**

```
Standard saved to .olaf/data/practices/standards/<slug>.md

Deploy to which tools?
- Claude (.claude/rules/standards/)
- Cursor (.cursor/rules/standards/)
- Copilot (.github/instructions/)
- Windsurf (.windsurf/rules/standards/)
- All of the above
- None (keep in .olaf/ only)
```

---

## Step 5 — Deploy to Tools

For each selected tool, convert and save:

### Claude

```markdown
<!-- .claude/rules/standards/<slug>.md -->
# [Standard Title]

[Content from source standard]
```

### Cursor

```markdown
<!-- .cursor/rules/standards/<slug>.mdc -->
---
description: [Standard description]
globs: [scope patterns]
---
# [Standard Title]

[Content from source standard]
```

### Copilot

```markdown
<!-- .github/instructions/standard-<slug>.instructions.md -->
---
description: [Standard description]
applyTo: [scope patterns]
---
# [Standard Title]

[Content from source standard]
```

### Windsurf

```markdown
<!-- .windsurf/rules/standards/<slug>.md -->
# [Standard Title]

[Content from source standard]
```

---

## Step 6 — Summary

Print:

```
============================================================
  STANDARD CREATED
============================================================

Name: [Standard Title]
Slug: [slug]
Rules: [N] rules

Source of truth:
  .olaf/data/practices/standards/[slug].md

Deployed to:
  - [Tool 1]: [path]
  - [Tool 2]: [path]
  - ...

Draft cleaned up.
============================================================
```

---

## Complete Example

**User request:** "Create a standard for TypeScript testing conventions"

**Clarification questions:**
- Does this apply to all test files or specific test types (unit, integration, e2e)?
- What testing framework are you using (Jest, Vitest, Mocha)?
- Are there specific patterns you want to enforce (naming, structure, assertions)?

**Draft file:** `.olaf/data/practices/standards/_drafts/typescript-testing-conventions.md`

```markdown
# TypeScript Testing Conventions

## Description

Enforce consistent testing patterns in TypeScript test files to improve readability, maintainability, and reliability.

## Scope

**/*.spec.ts,**/*.test.ts

## Rules

### Use descriptive test names that explain expected behavior

#### Good

```typescript
it('returns empty array when no items match filter')
```

#### Bad

```typescript
it('test filter')
```

### Follow Arrange-Act-Assert pattern in test structure

#### Good

```typescript
const input = createInput();
const result = processInput(input);
expect(result).toEqual(expected);
```

#### Bad

```typescript
expect(processInput(createInput())).toEqual(expected);
```

### Use one assertion per test for better error isolation

#### Good

```typescript
it('validates name', () => { expect(result.name).toBe('test'); });
it('validates age', () => { expect(result.age).toBe(25); });
```

#### Bad

```typescript
it('validates user', () => { 
  expect(result.name).toBe('test'); 
  expect(result.age).toBe(25); 
});
```
```

---

## Quick Reference

| Section | Required | Description |
|---------|----------|-------------|
| `# Title` | Yes | Title Case, descriptive, 2–5 words |
| `## Description` | Yes | What and why |
| `## Scope` | Yes | Comma-separated glob patterns |
| `## Rules` | Yes | Contains rule subsections |
| `### Rule text` | Yes (≥1) | Rule text (verb-first, max ~25 words) |
| `#### Good` | No | Valid code in fenced block |
| `#### Bad` | No | Invalid code in fenced block |
