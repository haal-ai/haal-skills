# Context Switch - Description

## Overview
Context Switch allows users to switch between different project contexts by selecting from available templates stored in `.olaf/data/context/`.

## What It Does
- Lists all available context files (context-*.md) from `.olaf/data/context/`
- Displays them as a numbered list
- User selects a context by number
- Copies the selected context to `context-current.md`
- Reminds user to start new session for context to activate

## How It Works
1. **List Phase**: Scans `.olaf/data/context/` for all `context-*.md` files (excluding `context-current.md`)
2. **Selection Phase**: User picks a number from the list
3. **Copy Phase**: Selected context file is copied to `.olaf/data/context/context-current.md`
4. **Activation Phase**: User starts new conversation/session to load the new context

## Bootstrap Integration
The OLAF bootstrap process (see `.windsurf/rules/olaf-bootstrap-skills.md`) automatically loads the active context at the start of each new session.

**Load order**:
- `.olaf/context/current-context.md` (preferred)
- `.olaf/data/context/context-current.md` (legacy)
- `.olaf/data/context/context-default.md` (fallback)

## Key Files
- **Context Templates**: `.olaf/data/context/context-*.md` (e.g., context-default.md)
- **Active Context**: `.olaf/data/context/context-current.md` (loaded at bootstrap)
- **Bootstrap Rules**: `.windsurf/rules/olaf-bootstrap-skills.md`

## Commands
- `context switch` - List contexts and switch
- `context list` - List available contexts
- `context clear` - Delete context-current.md
- `context status` - Show current active context

## When to Use
- Switching between different projects
- Applying project-specific configurations
- Changing working context without editing files manually
