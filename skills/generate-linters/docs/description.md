# generate-linters

## Overview
Reads standards and rules files with `-standard-` markers and generates executable `.js` detection programs (linters) that can check code compliance against those standards.

## Purpose
This skill exists to turn coding standards into executable linters that can automatically detect violations. Use it when you want to enforce standards programmatically, create custom lint rules from team conventions, or prepare for the `haal-lint` command.

## Key Features
- Discovers `-standard-` marked files automatically
- Generates `.js` detection programs with `@haal-linter` metadata headers
- Supports RAW mode (string/regex matching) by default
- Supports AST mode (tree-sitter parsing) when prerequisites are met
- Creates `manifest.json` for linter registry
- Integrates with `haal-lint` command workflow

## Usage
Invoke this skill by saying:
- "generate linters"
- "create detection programs from standards"
- "build linters from coding standards"

## Parameters

### Required
None - automatically discovers `-standard-` files

### Optional
1. **standards_dir**: string - Where to find standards (default: `.olaf/data/practices/standards/`)
2. **output_dir**: string - Where to save linters (default: `.olaf/data/practices/linters/`)
3. **mode**: string - Detection mode: `raw` or `ast` (default: `raw`)

## Process Flow
1. **Discovery Phase** - Scans for files with `-standard-` in filename
2. **Parsing Phase** - Extracts rules and patterns from standards
3. **Generation Phase** - Creates `.js` detection programs with metadata
4. **Registration Phase** - Updates `manifest.json` with linter entries
5. **Validation Phase** - Ensures generated linters are syntactically correct

## Output
- Linter files: `.olaf/data/practices/linters/*.js`
- Manifest file: `.olaf/data/practices/linters/manifest.json`

## Linter File Structure
Each generated `.js` file includes:

```javascript
/**
 * @haal-linter
 * @standard typescript-good-practices
 * @rule no-set-prototype-of
 * @rule-content Do not use Object.setPrototypeOf when defining errors
 * @mode RAW
 * @languages typescript, javascript
 * @severity error
 */

function checkSourceCode(input) {
  // Detection logic generated from standard
  const violations = [];
  // ... pattern matching logic
  return violations;
}
```

## Detection Modes

### RAW Mode (default)
- Uses string/regex matching
- No prerequisites required
- Works on any file content
- Good for simple pattern detection

### AST Mode (optional)
- Uses tree-sitter parsing
- Requires: `web-tree-sitter` npm package
- Requires: Language WASM files (e.g., `tree-sitter-typescript.wasm`)
- Better for structural code analysis
- Falls back gracefully if prerequisites missing

## Examples
- Generate linters from all discovered standards
- Create RAW-mode linters for TypeScript conventions
- Generate AST-mode linters for structural patterns

## Error Handling
- **No standards found**: Reports missing `-standard-` files
- **AST prerequisites missing**: Logs warning, continues with RAW mode
- **Generation failure**: Skips problematic rules, continues with others

## Related Skills
- **init-standard-rules**: Creates the `-standard-` files this skill consumes
- **haal-lint**: Runs the generated `.js` linters against code
- **create-standard**: Manually creates standards that can be linted
