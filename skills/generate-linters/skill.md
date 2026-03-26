---
name: generate-linters
description: Read standards from OLAF practices folders and generate .js detection programs (verifiers) for each rule
license: Apache-2.0
metadata:
  olaf_tags: [linting, standards, quality, codegen, detection-programs]
  copyright: Copyright (c) 2026 Haal AI
  author: Haal AI
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

# generate-linters

Action skill. Reads standards from OLAF practices directories and generates `.js` detection programs (verifiers) that can be executed by the `haal-lint` command.

**Local-only:** No cloud service required. All outputs saved locally.

## Guarantees

- **Standards-driven.** Only generates linters from existing standard files.
- **Evidence-based.** Every generated `.js` traces back to a standard rule.
- **Non-destructive.** Never overwrites existing `.js` linters; appends version suffix.
- **Packmind-compatible.** Generated `.js` follows the same `checkSourceCode(input)` contract as Packmind detection programs.

## Definitions

- **Standard:** A markdown file in `.olaf/data/practices/standards/` containing coding rules with good/bad examples.
- **Detection program (verifier):** A `.js` file containing a `checkSourceCode(input)` function that returns an array of violation line numbers (0-indexed) or `{ line, character }` objects.
- **Source code state:**
  - `RAW` **(default, zero prerequisites)** — function receives raw file content as a string. Detection via regex and string operations.
  - `AST` **(optional, requires tree-sitter)** — function receives a parsed AST object. Detection via tree traversal.

## Prerequisites

### RAW mode (default)

**None.** RAW mode works with pure string/regex matching on file content. No external tools or libraries needed.

### AST mode (optional)

AST mode requires **tree-sitter** with language-specific WASM binaries on the user's machine:

1. `web-tree-sitter` npm package
2. Per-language `.wasm` files in a known directory:
   - `tree-sitter-typescript.wasm`
   - `tree-sitter-javascript.wasm`
   - `tree-sitter-cpp.wasm`
   - `tree-sitter-go.wasm`
   - `tree-sitter-python.wasm`
   - `tree-sitter-java.wasm`
   - `tree-sitter-c-sharp.wasm`
   - `tree-sitter-ruby.wasm`
   - `tree-sitter-php.wasm`
   - `tree-sitter-kotlin.wasm`
   - `tree-sitter-swift.wasm`
   - (and others per Packmind's `linter-ast` package)

The AST is normalized to this shape (same as Packmind):

```typescript
interface ASTNode {
  type: string;     // e.g. "class_declaration", "function_declaration"
  text: string;     // source text of the node
  line: number;     // 1-indexed line number
  children: ASTNode[];
}
```

**When AST prerequisites are not met**, the skill must:
- Skip AST-mode generation for that language
- Fall back to RAW mode with a `// TODO: Consider converting to AST mode` comment
- Log a warning to the user

---

## Step 0 — Introduction

Print exactly:

```
I'll scan your standards and generate .js detection programs (verifiers) for the haal-lint command.
```

---

## Step 1 — Discover Standards

### Scan directories (broad, future-proof)

Glob for markdown files **with `-standard-` in the filename** in these roots (recursive):

- `.olaf/data/practices/standards/*-standard-*.md`
- `.olaf/data/practices/rules/*-standard-*.md`
- `.claude/**/*-standard-*.md`
- `.windsurf/**/*-standard-*.md`
- `.cursor/**/*-standard-*.md`
- `.github/instructions/**/*-standard-*.md`

### Discovery rule

A file is a lintable standard/rule if:

1. **Its filename contains `-standard-`** (the naming convention set by `init-standard-rules`)
2. It contains at least one rule section (e.g. `## Rules`, `### Rule`, or bullet points with Good/Bad examples)

Files **without** `-standard-` in the name are ignored — they may be commands, skills, workflows, or other non-lintable documents.

### Print discovery summary

```
Standards discovered:

    .olaf/data/practices/standards/: [N] files
    .claude/: [M] files
    .windsurf/: [P] files
    .cursor/: [Q] files
    .github/instructions/: [R] files

    Total standards: [T]
    Total rules extracted: [U]
```

---

## Step 2 — Parse Standards into Rules

For each standard file, extract rules:

### Rule extraction

```
Standard: typescript-good-practices.md
  Rule 1: "Do not use Object.setPrototypeOf when defining errors"
    - Scope: typescript, javascript
    - Severity: error
    - Good example: class MyError extends Error { ... }
    - Bad example: Object.setPrototypeOf(this, MyError.prototype)
    
  Rule 2: "Use intersection types for DTO enrichment"
    - Scope: typescript
    - Severity: error
    - Good example: type UserDTO = User & { role: string }
    - Bad example: interface UserDTO { id: string; name: string; role: string }
```

### Internal rule structure

```typescript
interface ExtractedRule {
  standardSlug: string;
  standardFile: string;
  ruleId: string;          // slug derived from rule title
  ruleContent: string;     // full rule text
  severity: 'error' | 'warning';
  languages: string[];     // detected from scope or file extensions in examples
  goodExamples: string[];
  badExamples: string[];
}
```

---

## Step 3 — Generate .js Detection Programs

For each extracted rule, generate a `.js` file.

### Detection program contract (same as Packmind)

Every generated `.js` must contain a function with this exact signature:

```javascript
function checkSourceCode(input) {
  // input: raw source code string (RAW mode)
  //    or: parsed AST object (AST mode)
  //
  // Returns: array of violation locations
  //   - number: 0-indexed line number
  //   - { line: number, character: number }: line + column (0-indexed)
  //   - empty array: no violations
}
```

### Generation strategy

**Always generate RAW mode by default.** Only generate AST mode if explicitly requested and prerequisites are met.

| Rule Type | Default Mode | Strategy |
|-----------|-------------|----------|
| **Forbidden pattern** (e.g., "Do not use X") | `RAW` | Regex/string search for forbidden pattern |
| **Required pattern** (e.g., "Always use X") | `RAW` | Search for contexts where pattern should exist but doesn't |
| **Naming convention** | `RAW` | Regex match on identifiers |
| **Structural pattern** (e.g., "Use intersection types") | `RAW` | Multi-line regex with context checks |
| **Complex structural** (only if AST available) | `AST` | AST traversal for deep structure checks |

### Example: Forbidden pattern → RAW mode .js

**Standard rule:** "Do not use `Object.setPrototypeOf` when defining errors."

**Generated `.js`:**

```javascript
// Standard: typescript-good-practices
// Rule: Do not use Object.setPrototypeOf when defining errors
// Mode: RAW
// Languages: typescript, javascript
// Severity: error

function checkSourceCode(input) {
  const violations = [];
  const lines = input.split('\n');

  // Check if file contains an error class
  const hasErrorClass = /class\s+\w+\s+extends\s+Error/.test(input);
  if (!hasErrorClass) return violations;

  for (let i = 0; i < lines.length; i++) {
    if (/Object\.setPrototypeOf\s*\(/.test(lines[i])) {
      violations.push(i); // 0-indexed line number
    }
  }

  return violations;
}
```

### Example: Required pattern → RAW mode .js

**Standard rule:** "Use intersection types for DTO enrichment instead of re-declaring fields."

**Generated `.js`:**

```javascript
// Standard: typescript-good-practices
// Rule: Use intersection types for DTO enrichment
// Mode: RAW
// Languages: typescript
// Severity: error

function checkSourceCode(input) {
  const violations = [];
  const lines = input.split('\n');

  // Find interface/type definitions that look like DTOs
  const dtoPattern = /^(export\s+)?(interface|type)\s+\w*(DTO|Dto|Response|Payload)\b/;

  for (let i = 0; i < lines.length; i++) {
    if (dtoPattern.test(lines[i])) {
      // Check if it's an interface with manually declared fields
      // instead of intersection type
      if (/^(export\s+)?interface\s+/.test(lines[i])) {
        violations.push(i);
      }
    }
  }

  return violations;
}
```

### File naming convention

```
.olaf/data/practices/linters/<standard-slug>--<rule-id>.js
```

Example:
```
.olaf/data/practices/linters/typescript-good-practices--no-set-prototype-of.js
.olaf/data/practices/linters/typescript-good-practices--use-intersection-types.js
.olaf/data/practices/linters/testing-good-practices--verb-first-test-names.js
```

### Metadata header in each .js

Every generated `.js` must start with a metadata comment block:

```javascript
// @haal-linter
// @standard: <standard-slug>
// @rule: <rule-id>
// @rule-content: <full rule text, single line>
// @mode: RAW | AST
// @languages: typescript, javascript
// @severity: error | warning
// @generated: <ISO timestamp>
// @source: <path to source standard file>
```

---

## Step 4 — Write Output

### Create output directory

```
.olaf/data/practices/linters/
```

### Write .js files

For each generated detection program:
1. Check if file already exists
2. If exists, append version suffix: `--v2.js`, `--v3.js`
3. Write the `.js` file

### Write manifest

Create/update `.olaf/data/practices/linters/manifest.json`:

```json
{
  "generatedAt": "2026-03-18T10:00:00Z",
  "standardsProcessed": 3,
  "rulesProcessed": 7,
  "lintersGenerated": 7,
  "linters": [
    {
      "file": "typescript-good-practices--no-set-prototype-of.js",
      "standard": "typescript-good-practices",
      "rule": "no-set-prototype-of",
      "mode": "RAW",
      "languages": ["typescript", "javascript"],
      "severity": "error"
    }
  ]
}
```

---

## Step 5 — Present Summary

```
============================================================
  LINTER GENERATION COMPLETE
============================================================

Standards processed: [N]
Rules extracted: [M]
Linters generated: [P]

LINTERS CREATED:
  1. [standard]--[rule].js (RAW, [languages], [severity])
  2. ...

Output: .olaf/data/practices/linters/
Manifest: .olaf/data/practices/linters/manifest.json

Run `haal-lint` to execute these linters against your codebase.
============================================================
```

---

## Edge Cases

### No standards found

```
No standard files found in any practices directory.

Run `init-standard-rules` first to generate standards from your codebase.
```

### Rule too complex for automatic .js generation

If a rule is too semantic or abstract for reliable regex/AST detection:

```
⚠️ Rule "[rule]" in [standard] is too semantic for reliable automatic detection.
   Generating a best-effort verifier with TODO markers.
   Review and refine the generated .js manually.
```

Generate a stub with `// TODO:` markers for manual refinement.

### Existing linters

```
Found [N] existing linters in .olaf/data/practices/linters/
New linters will not overwrite existing ones.
```
