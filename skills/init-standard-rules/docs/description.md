# init-standard-rules

## Overview
Analyzes a codebase to extract coding standards, rules, and best practices, saving them as structured markdown files with `-standard-` markers for discovery by downstream tools.

## Purpose
This skill exists to bootstrap AI-first development by extracting team conventions and coding patterns from existing codebases. Use it when you want to create a standards registry from code, document implicit coding rules, or prepare standards for linter generation.

## Key Features
- Analyzes codebase patterns to identify coding conventions
- Extracts standards from code structure, naming, and patterns
- Generates structured markdown with `-standard-` filename markers
- Creates standards, rules, and instruction files
- Supports multiple programming languages
- Integrates with `generate-linters` workflow

## Usage
Invoke this skill by saying:
- "init standard rules"
- "extract coding standards from this codebase"
- "create standards from code patterns"

## Parameters

### Required
1. **scope**: string - Directory or files to analyze (default: project root)

### Optional
2. **language**: string - Target language filter (e.g., "typescript", "python")
3. **output_dir**: string - Where to save standards (default: `.olaf/data/practices/standards/`)

## Process Flow
1. **Discovery Phase** - Scans codebase for patterns and conventions
2. **Analysis Phase** - Identifies recurring patterns, naming conventions, architectural decisions
3. **Extraction Phase** - Derives standards and rules from observed patterns
4. **Generation Phase** - Creates structured markdown files with `-standard-` markers
5. **Validation Phase** - Ensures generated standards are discoverable and well-formed

## Output
- Standards files: `.olaf/data/practices/standards/*-standard-*.md`
- Rules files: `.olaf/data/practices/rules/*-standard-*.md`
- Instructions file: `.olaf/data/practices/instructions/*-standard-*.md`

## File Naming Convention
All generated files include `-standard-` in the filename to enable discovery by `generate-linters`:
- `typescript-good-practices-standard.md`
- `naming-conventions-standard.md`
- `error-handling-standard-rules.md`

## Examples
- Extract TypeScript standards from `src/` directory
- Generate Python coding conventions from existing modules
- Create API design standards from REST endpoints

## Error Handling
- **No patterns found**: Reports low-confidence findings and suggests manual review
- **Ambiguous patterns**: Flags for human clarification
- **File access issues**: Falls back to alternative directories

## Related Skills
- **generate-linters**: Consumes `-standard-` files to create `.js` detection programs
- **create-standard**: Creates standards manually with explicit rules
- **update-standard-rules**: Updates existing standards from new code patterns
