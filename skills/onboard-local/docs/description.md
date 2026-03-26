# onboard-local

## Overview
Local-only codebase onboarding that analyzes project patterns and generates draft standards and commands without requiring cloud services or authentication.

## Purpose
Bootstrap a project with coding standards and reusable commands by analyzing existing code patterns. Runs entirely offline with read-only analysis and draft-first approach.

## Key Features
- No cloud dependency (fully offline)
- Read-only analysis phase (no project modifications)
- Evidence-based insights (file-path references required)
- Drafts before final (review cycle)
- Focused output: max 5 standards + 5 commands per run
- Stack auto-detection
- Optional registry format conversion

## Usage
Invoke this skill by saying:
- "Onboard this project locally"
- "Analyze this codebase and generate standards"
- "Set up local conventions for this repo"

## Parameters

### Required
- **project_path**: Path to the codebase to analyze (default: current directory)

### Optional
- **max_standards**: Maximum standards to generate (default: 5)
- **max_commands**: Maximum commands to generate (default: 5)

## Process Flow
1. **Introduction** — Explain what will happen
2. **Stack Detection** — Identify languages, frameworks, build tools
3. **Core Analysis** — Scan for patterns, conventions, anti-patterns
4. **Generate Standards** — Create draft standards with evidence
5. **Generate Commands** — Create draft commands for common tasks
6. **Review** — Present drafts for approval
7. **Save** — Write final versions to `.olaf/data/practices/`
8. **Registry Conversion** — Optionally convert to registry format

## Output
- Up to 5 coding standards in `.olaf/data/practices/standards/`
- Up to 5 reusable commands in `.olaf/data/practices/commands/`
- Each backed by evidence from the codebase

## Related Skills
- **create-standard**: Interactively create a single standard
- **update-standard-rules**: Maintain existing standards
- **generate-ai-agent-instructions**: Generate AI tool instructions from analysis
