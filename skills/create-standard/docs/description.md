# create-standard

## Overview
Create coding standards from user intent through a question-first approach. Generates standards deployable to multiple AI tools (Claude, Cursor, Copilot, Windsurf, Kiro).

## Purpose
Define new coding conventions, best practices, or guidelines through interactive clarification. Use when you want to codify a team practice as a reusable, enforceable standard across AI-assisted development tools.

## Key Features
- Question-first philosophy: clarifies intent before drafting
- Multi-tool deployment (Claude, Cursor, Copilot, Windsurf)
- Scope control: Global (home), Workspace, or Per-repo
- Structured standard format with rules and code examples
- Draft review cycle with user approval gates
- OLAF central storage as source of truth

## Usage
Invoke this skill by saying:
- "create a standard for TypeScript testing conventions"
- "define a convention for error handling"
- "add a coding rule for naming"

## Parameters

### Required
- **topic/intent**: What the standard should cover (provided in conversation)

### Optional
- **scope**: home | workspace | per-repo (default: per-repo)
- **target_tools**: Which AI tools to deploy to (default: asks user)

## Process Flow
1. **Clarify the Request** — Ask 1-5 focused questions based on clarity
2. **Draft Standard** — Create markdown in `_drafts/` with title, description, scope, rules, and examples
3. **Review** — Present formatted recap, allow edits
4. **Save** — Move from drafts to `.olaf/data/practices/standards/`
5. **Deploy** — Convert and save to selected tool-specific paths
6. **Summary** — Print creation report

## Output
- Standard markdown file in `.olaf/data/practices/standards/<slug>.md`
- Tool-specific files (e.g., `.claude/rules/standards/`, `.cursor/rules/standards/`)

## Related Skills
- **update-standard-rules**: Update or deprecate existing standards
- **init-standard-rules**: Initialize standards from existing codebase patterns
- **generate-linters**: Generate lint rules from standards
