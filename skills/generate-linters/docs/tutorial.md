# generate-linters: Step-by-Step Tutorial

**How to Create Executable Linters from Coding Standards**

This tutorial guides you through generating `.js` detection programs from standards files, ready to be run by the `haal-lint` command.

## Prerequisites

- Standards files with `-standard-` markers in `.olaf/data/practices/standards/`
- (Optional) For AST mode: `web-tree-sitter` installed + language WASM files

## Estimated Time

10-20 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Say: "generate linters" or:
- "create detection programs from standards"
- "build linters for my standards"

### Step 2: Discovery

**What AI Does:**
1. Scans `.olaf/data/practices/standards/` for `-standard-` files
2. Scans `.olaf/data/practices/rules/` for `-standard-` files
3. Parses each file for rules and patterns

**You Should See:**
```
Scanning for standards...
Found 3 standard files:
  - typescript-naming-conventions-standard.md
  - error-handling-patterns-standard.md
  - api-design-standard.md

Extracted 12 rules total
```

### Step 3: Select Detection Mode

**AI Asks:** "Which detection mode should I use?"

**Options:**
1. **RAW** (default) - String/regex matching, no prerequisites
2. **AST** - Tree-sitter parsing, requires WASM files

**For RAW mode:**
```
raw
```

**For AST mode:**
```
ast
```

**Note:** AST mode requires:
- `npm install web-tree-sitter`
- WASM files in `./tree-sitter/` or `node_modules/`

### Step 4: Preview Generated Linters

**AI Shows:**
Preview of each linter with:
- Standard and rule it checks
- Detection logic summary
- Languages it applies to
- Severity level

**Example:**
```javascript
/**
 * @haal-linter
 * @standard typescript-naming-conventions
 * @rule camel-case-variables
 * @rule-content Use camelCase for variable names
 * @mode RAW
 * @languages typescript, javascript
 * @severity warning
 */

function checkSourceCode(input) {
  const violations = [];
  // Detects: const my_var = ...
  // Detects: const MyVar = ...
  const pattern = /(?:const|let|var)\s+([A-Z_][A-Z0-9_]*)\s*=/g;
  // ... detection logic
  return violations;
}
```

### Step 5: Approve Generation

**AI Asks:** "Generate these linters?"

**User Options:**
1. **Approve**: Type "yes" to create all
2. **Select**: Choose specific rules to generate
3. **Modify**: Request changes to detection logic

### Step 6: Linters Generated

**What AI Does:**
1. Creates `.js` files in `.olaf/data/practices/linters/`
2. Creates `manifest.json` with linter registry

**You Should See:**
```
✓ Created: .olaf/data/practices/linters/typescript-naming--camel-case.js
✓ Created: .olaf/data/practices/linters/typescript-naming--pascal-case.js
✓ Created: .olaf/data/practices/linters/error-handling--no-set-prototype.js
✓ Created: .olaf/data/practices/linters/manifest.json

Generated 12 linters from 3 standards
```

### Step 7: Verify Output

**User Action:**
Check generated linters:

```bash
ls .olaf/data/practices/linters/
# Should show *.js files

cat .olaf/data/practices/linters/manifest.json
# Should list all linters with metadata
```

### Step 8: Run Lint Check

**User Action:**
Test the generated linters:

```
/haal-lint
```

**Expected Result:**
```
Loaded 12 linters from .olaf/data/practices/linters/

Scanning . ...
Found 45 files to check (32 TypeScript, 13 JavaScript)

============================================================
  HAAL LINT RESULTS
============================================================

Files checked: 45
Linters executed: 12
Files with violations: 3
Total violations: 7
...
```

## Linter File Structure

Each generated `.js` file follows this structure:

```javascript
/**
 * @haal-linter
 * @standard [standard-slug]
 * @rule [rule-id]
 * @rule-content [human-readable rule]
 * @mode RAW | AST
 * @languages [comma-separated list]
 * @severity error | warning
 */

function checkSourceCode(input) {
  // input = raw file content (RAW mode)
  // input = AST nodes (AST mode)

  const violations = [];

  // Detection logic here
  // Return 0-indexed line numbers or { line, character } objects

  return violations;
}
```

## Detection Modes Compared

| Feature | RAW Mode | AST Mode |
|---------|----------|----------|
| Prerequisites | None | tree-sitter + WASM |
| Detection | String/regex | Structural parsing |
| Accuracy | Good for patterns | Better for structure |
| Speed | Fast | Slower |
| Fallback | N/A | Falls back to RAW |

## Troubleshooting

**Issue: "No standards found"**
- Run `init-standard-rules` first
- Check files have `-standard-` in filename
- Verify `.olaf/data/practices/standards/` exists

**Issue: "AST mode unavailable"**
- Install: `npm install web-tree-sitter`
- Download WASM files to `./tree-sitter/`
- Or use RAW mode (default)

**Issue: "Linter throws error"**
- Check generated `.js` for syntax errors
- Verify pattern regex is valid
- Report issue for regeneration

## Verification Checklist

✅ **Files Created**
- `.js` files exist in `.olaf/data/practices/linters/`
- `manifest.json` exists and is valid JSON

✅ **Metadata Headers**
- Each linter has `@haal-linter` header
- Standard, rule, mode, languages, severity defined

✅ **Detection Logic**
- `checkSourceCode(input)` function exists
- Returns violations array
- Handles edge cases

## Next Steps

1. **Run lint**: Use `/haal-lint` to check your codebase
2. **Review results**: Check `.olaf/work/lint-review/*.md`
3. **Iterate**: Refine standards and regenerate linters

## Workflow Summary

```
init-standard-rules → *-standard-*.md files
         ↓
generate-linters → *.js linters
         ↓
haal-lint → lint results in .olaf/work/lint-review/
```
