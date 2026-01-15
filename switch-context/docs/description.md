# Context Switch - Description

## Overview
Context Switch allows users to switch between different project contexts by selecting from available templates stored in `docs/data/context/`.

## What It Does
- Lists all available context files (context-*.md) from `docs/data/context/`
- Displays them as a numbered list
- User selects a context by number
- Copies the selected context to `context-current.md`
- Reminds user to start new session for context to activate

## How It Works
1. **List Phase**: Scans `docs/data/context/` for all `context-*.md` files (excluding `context-current.md`)
2. **Selection Phase**: User picks a number from the list
3. **Copy Phase**: Selected context file is copied to `docs/data/context/context-current.md`
4. **Activation Phase**: User starts new conversation/session to load the new context

## Bootstrap Integration
The OLAF bootstrap process (in `.github/copilot-instructions.md`) automatically loads `context-current.md` if it exists, applying project-specific context to the session.

## Key Files
- **Context Templates**: `docs/data/context/context-*.md` (e.g., context-default.md)
- **Active Context**: `docs/data/context/context-current.md` (loaded at bootstrap)
- **Skill Prompt**: `skills/switch-context/prompts/switch-context.md`

## Commands
- `context switch` - List contexts and switch
- `context list` - List available contexts
- `context clear` - Delete context-current.md
- `context status` - Show current active context

## When to Use
- Switching between different projects
- Applying project-specific configurations
- Changing working context without editing files manually
