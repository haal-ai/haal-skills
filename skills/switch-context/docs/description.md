# switch-context

## Overview

The `switch-context` skill enables dynamic switching between pre-existing context files stored in the `.olaf/data/context/` directory. It manages context templates that customize AI agent behavior for different projects, workflows, or environments.

## Purpose

This skill allows users to quickly switch between different operational contexts without manually editing configuration files. Each context can contain project-specific instructions, coding standards, or workflow preferences that the AI agent follows in subsequent sessions.

## Key Features

- **Context Discovery**: Lists all available context templates in the context directory
- **Context Switching**: Copies selected context template to the active context file
- **Context Clearing**: Removes the current active context
- **Status Display**: Shows current active context and available options
- **Session Guidance**: Provides clear instructions about session restart requirements

## Usage

List available contexts:

```
@switch-context
```

Switch to a specific context:

```
@switch-context context_name=springboot-hexagonal
```

Clear current context:

```
@switch-context clear
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| context_name | string | No | Name of context to switch to (shows list if omitted) |
| format | string | No | Output format: list or detailed (default: list) |

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT SWITCHING                            │
├─────────────────────────────────────────────────────────────────┤
│ 1. List Available Contexts                                      │
│    - Scan .olaf/data/context/ for context-*.md files            │
│    - Display numbered list with descriptions                    │
│    ↓                                                            │
│ 2. User Selection                                               │
│    - Accept context name or number                              │
│    - Validate selection exists                                  │
│    ↓                                                            │
│ 3. Switch Context                                               │
│    - Copy context-{name}.md to context-current.md               │
│    - Confirm successful switch                                  │
│    ↓                                                            │
│ 4. Session Guidance                                             │
│    - Inform user to start new session                           │
│    - Context takes effect in fresh session                      │
└─────────────────────────────────────────────────────────────────┘
```

## Output

The skill provides context management information:

**List Format (Default):**
```
Available contexts:
1. default - General purpose context
2. springboot-hexagonal - Spring Boot with hexagonal architecture
3. react-frontend - React frontend development

Current active: springboot-hexagonal

Select a context by number or name:
```

**Status Format:**
```
Current Context: springboot-hexagonal
Available Contexts: 3
Last Updated: 2024-01-15
```

## Commands

| Command | Description |
|---------|-------------|
| `context switch {name}` | Switch to specific context |
| `context switch` or `context list` | List available contexts |
| `context clear` | Remove current context |
| `context status` | Show current active context |

## File Structure

```
.olaf/data/context/
├── context-default.md          # Default context template
├── context-springboot.md       # Spring Boot context
├── context-react.md            # React development context
├── context-current.md          # Active context (managed by skill)
└── context-{custom}.md         # Custom context templates
```

## Examples

### Example 1: List and Select Context

```
User: @switch-context

Agent:
Available contexts:
1. default - General purpose development
2. springboot-hexagonal - Spring Boot hexagonal architecture
3. python-fastapi - Python FastAPI development

Current active: default

Select a context by number or name:

User: 2

Agent:
✓ Context switched to: springboot-hexagonal

⚠️ IMPORTANT: Please start a new conversation for the 
'springboot-hexagonal' context to be active. The context 
change will only take effect in a fresh session.
```

### Example 2: Direct Context Switch

```
User: @switch-context context_name=python-fastapi

Agent:
✓ Context switched to: python-fastapi

⚠️ IMPORTANT: Please start a new conversation for the 
'python-fastapi' context to be active.
```

### Example 3: Clear Context

```
User: @switch-context clear

Agent:
✓ Context cleared successfully

⚠️ IMPORTANT: Please start a new conversation for the 
context clearing to be active.
```

## Error Handling

| Error Condition | Handling |
|----------------|----------|
| Context not found | Display error with available contexts list |
| Invalid selection | Request valid number or name |
| File access error | Report error and suggest manual check |
| No contexts available | Inform user and suggest creating context files |

## Important Notes

- **Session Restart Required**: Context changes only take effect in new sessions
- **No Code Generation**: This skill only manages context files, not code
- **Local Files Only**: Operates only on files in `.olaf/data/context/`
- **Non-Destructive**: Original context templates are never modified

## Related Skills

- `carry-over-session` - Preserve session state across conversations
- `carry-on-session` - Resume from carried-over session state
- `store-conversation-record` - Save conversation for future reference
