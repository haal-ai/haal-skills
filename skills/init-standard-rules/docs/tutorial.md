# init-standard-rules: Step-by-Step Tutorial

**How to Extract Coding Standards from Your Codebase**

This tutorial guides you through extracting coding standards, rules, and best practices from an existing codebase to create a standards registry for AI-first development.

## Prerequisites

- A codebase with established patterns and conventions
- Write access to `.olaf/data/practices/` directory
- Understanding of the coding patterns you want to capture

## Estimated Time

15-30 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Say: "init standard rules" or describe what you want:
- "extract coding standards from this codebase"
- "create standards from src/ directory"

### Step 2: Specify Scope

**AI Asks:** "Which part of the codebase should I analyze?"

**You Provide:**
```
src/
```

**Options:**
- Specific directory: `src/components/`
- Multiple directories: `src/, tests/`
- Entire project: `.` (default)

### Step 3: Language Filter (Optional)

**AI Asks:** "Should I filter by programming language?"

**You Provide:**
```
typescript
```

**Or skip:**
```
all languages
```

### Step 4: Analysis Runs

**What AI Does:**
1. Scans files in scope
2. Identifies recurring patterns:
   - Naming conventions
   - File structure patterns
   - Import/export patterns
   - Error handling patterns
   - Code organization patterns
3. Extracts conventions as candidate standards

**You Should See:**
```
Scanning src/...
Found 142 TypeScript files

Analyzing patterns...
  - Naming conventions: camelCase for variables, PascalCase for classes
  - File structure: barrel exports in index.ts
  - Error handling: custom error classes extend BaseError
  - Imports: grouped by external, internal, relative

Extracted 8 candidate standards
```

### Step 5: Review Extracted Standards

**AI Shows:**
Preview of each extracted standard with:
- Standard name
- Description
- Detected rules
- Example code snippets

**Example:**
```markdown
## Standard: typescript-naming-conventions

### Rules
1. Use camelCase for variables and functions
2. Use PascalCase for classes and types
3. Use UPPER_SNAKE_CASE for constants

### Examples
// Good
const userName = 'Alice';
class UserService {}
const MAX_RETRIES = 3;

// Bad
const user_name = 'Alice';
class userService {}
const maxRetries = 3;
```

### Step 6: Approve or Modify

**AI Asks:** "Do these standards look correct?"

**User Options:**
1. **Approve**: Type "approved" to save
2. **Modify**: Request changes to specific standards
3. **Add**: Request additional patterns to capture

**Example Feedback:**
```
Add a rule about interface naming - they should start with I
```

### Step 7: Files Generated

**What AI Does:**
Creates files with `-standard-` markers:

```
.olaf/data/practices/
├── standards/
│   ├── typescript-naming-conventions-standard.md
│   └── error-handling-patterns-standard.md
├── rules/
│   ├── typescript-naming-standard-rules.md
│   └── error-handling-standard-rules.md
└── instructions/
    └── coding-instructions-standard.md
```

**You Should See:**
```
✓ Created: .olaf/data/practices/standards/typescript-naming-conventions-standard.md
✓ Created: .olaf/data/practices/rules/typescript-naming-standard-rules.md
✓ Created: .olaf/data/practices/standards/error-handling-patterns-standard.md
✓ Created: .olaf/data/practices/rules/error-handling-standard-rules.md
```

### Step 8: Verify Output

**User Action:**
Check generated files:

```bash
ls .olaf/data/practices/standards/
# Should show *-standard-*.md files

cat .olaf/data/practices/standards/typescript-naming-conventions-standard.md
```

## Verification Checklist

✅ **Files Created**
- Standards files exist in `.olaf/data/practices/standards/`
- Rules files exist in `.olaf/data/practices/rules/`
- All files have `-standard-` in filename

✅ **Content Quality**
- Standards are clear and actionable
- Rules are specific and testable
- Examples illustrate good and bad patterns

✅ **Discovery Ready**
- Files can be found by `generate-linters` skill
- Filenames follow `-standard-` convention

## Troubleshooting

**Issue: "No patterns found"**
- Ensure codebase has consistent patterns
- Try narrowing scope to well-organized directories
- Check if language filter matches your files

**Issue: "Too many standards extracted"**
- Focus on specific directories
- Request consolidation of similar patterns
- Manually select which standards to keep

**Issue: "Standards don't match team conventions"**
- Review and modify extracted standards
- Add missing patterns manually
- Run with different scope

## Next Steps

1. **Generate linters**: Run `generate-linters` to create detection programs
2. **Run lint**: Use `haal-lint` command to check code compliance
3. **Iterate**: Refine standards based on lint results

## Workflow Summary

```
init-standard-rules
       ↓
.olaf/data/practices/standards/*-standard-*.md
       ↓
generate-linters
       ↓
.olaf/data/practices/linters/*.js
       ↓
haal-lint
       ↓
.olaf/work/lint-review/*.md
```
