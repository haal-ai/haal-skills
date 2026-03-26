---
mode: "agent"
description: "Run the Haal linter against the codebase using .js detection programs from standards"
---

# haal-lint

Run the Haal linter: execute all `.js` detection programs from `.olaf/data/practices/linters/` against the codebase and save timestamped results.

## When to Use

- Before committing code changes
- During code review
- After refactoring to check standards compliance

## Preconditions

- `.olaf/data/practices/linters/` directory exists with `.js` detection programs
- If no linters found, suggest running `generate-linters` skill first
- **RAW mode** (default): no prerequisites
- **AST mode** (optional): requires `web-tree-sitter` + language `.wasm` files

## Steps

### Step 1 — Load Linters

1. Read all `.js` files from `.olaf/data/practices/linters/`
2. Parse the `@haal-linter` metadata header from each file:
   - `@standard`: standard slug
   - `@rule`: rule ID
   - `@rule-content`: human-readable rule text
   - `@mode`: `RAW` or `AST`
   - `@languages`: comma-separated language list
   - `@severity`: `error` or `warning`
3. Also read `manifest.json` if available for cross-reference

Print:

```
Loaded [N] linters from .olaf/data/practices/linters/

Standards covered:
  - [standard-1] ([count] rules)
  - [standard-2] ([count] rules)
```

If no linters found:

```
No linters found in .olaf/data/practices/linters/

Run the `generate-linters` skill first to create detection programs from your standards.
```

### Step 2 — Collect Target Files

1. Determine the lint scope:
   - Default: entire project (from git root)
   - With `--path <dir>`: specific directory
   - With `--path <file>`: single file
2. Collect files, respecting excludes:
   - `node_modules/`, `dist/`, `.git/`, `build/`, `vendor/`
   - Patterns from `.gitignore`
   - Patterns from `.olaf/lint-ignore` if it exists
3. Detect file language from extension

Print:

```
Scanning [path]...
Found [N] files to check ([M] TypeScript, [P] JavaScript, ...)
```

### Step 3 — Execute Linters

For each file:

1. Determine applicable linters by matching file language against linter `@languages`
2. Read file content
3. For each matching linter:
   - If `@mode: RAW`: pass raw file content to `checkSourceCode(input)`
   - If `@mode: AST`: parse file to AST, then pass AST to `checkSourceCode(input)`
4. Collect returned violations (0-indexed line numbers or `{ line, character }` objects)
5. Convert to 1-indexed for display

Execution model (same as Packmind):

```javascript
const func = new Function('input', `
  ${linterJsCode}
  return checkSourceCode(input);
`);
const violations = func(fileContentOrAst);
```

Error handling:
- If a linter throws: log error, skip it, continue with remaining linters
- If a file can't be read: log warning, skip it, continue

### Step 4 — Format Results

Print to console:

```
============================================================
  HAAL LINT RESULTS
============================================================

Files checked: [N]
Linters executed: [M]
Files with violations: [P]
Total violations: [V]

VIOLATIONS:

[file]:[line] [SEVERITY] [standard/rule]
  Rule: [rule content]

============================================================
  SUMMARY
============================================================

Errors: [E]
Warnings: [W]

[If errors > 0]
FAILED — Fix [E] errors above.

[If only warnings]
PASSED with [W] warnings.

[If no violations]
PASSED — No violations found.
============================================================
```

### Step 5 — Save Results

Save results to `.olaf/work/lint-review/` with ISO timestamp:

**Markdown:** `.olaf/work/lint-review/<YYYY-MM-DDTHH-MM-SS>.md`

```markdown
# Haal Lint Review — <ISO timestamp>

## Summary

- **Files checked:** [N]
- **Linters executed:** [M]
- **Violations:** [V] ([E] errors, [W] warnings)
- **Result:** PASSED | FAILED

## Violations

### [file]

| Line | Severity | Standard | Rule | Description |
|------|----------|----------|------|-------------|
| [line] | ERROR | [standard] | [rule-id] | [rule content] |
```

**JSON:** `.olaf/work/lint-review/<YYYY-MM-DDTHH-MM-SS>.json`

```json
{
  "timestamp": "2026-03-18T10:00:00Z",
  "summary": {
    "filesChecked": 42,
    "lintersExecuted": 7,
    "totalViolations": 3,
    "errors": 2,
    "warnings": 1,
    "result": "FAILED"
  },
  "violations": [
    {
      "file": "src/errors/CustomError.ts",
      "line": 4,
      "severity": "error",
      "standard": "typescript-good-practices",
      "rule": "no-set-prototype-of",
      "ruleContent": "Do not use Object.setPrototypeOf when defining errors"
    }
  ]
}
```

## Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--path` | Path to lint (file or directory) | `.` (git root) |
| `--severity` | Minimum severity to report | `warning` |
| `--standard` | Only run linters for this standard | All |
| `--changed-files` | Only lint git-modified files | `false` |
| `--changed-lines` | Only report violations on changed lines | `false` |
