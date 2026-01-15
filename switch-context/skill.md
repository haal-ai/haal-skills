---
name: switch-context
description: IDE-aware context switching with automatic repository discovery and transitive loading
license: Apache-2.0
metadata:
  olaf_tags: [context, switching, ide, discovery, transitive, repository]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
**HIERARCHY**: Framework principles OVERRIDE competency specifications:
- <olaf-general-role-and-behavior> - Be concise, no elaboration
- <core-principles> - Mandatory rules supersede competency details
- <olaf-interaction-protocols> - Protocol only, not verbosity
You MUST strictly apply <olaf-framework-validation>.

## Output Constraints
**CONCISENESS MANDATORY**: Apply framework's "Be concise. Use as few words as possible."
- Status updates: Single line max
- Results: Essential info only  
- No formatting, alerts, or lengthy explanations
- Framework conciseness overrides all output format specifications below

## Input Parameters

## Role
Context Manager - Switch between different contexts dynamically.

## Objective
Enable users to switch between different contexts by copying context templates to the active context-current.md file.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **context_name**: string - Name of context to switch to (OPTIONAL - shows list if omitted)
- **format**: string - Output format preference (OPTIONAL - defaults to "list")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act for context discovery and listing (non-destructive analysis)
- You WILL use Propose-Act before switching contexts (requires user confirmation of selection)

## Workflow

### 1. List Available Contexts (Primary Step)
- **ALWAYS START HERE**: Check `.olaf/data/context/` directory for all context-*.md files first
- Display available contexts (files matching pattern: context-*.md) 
- Show current active context if exists
- Present numbered list to user for selection

### 3. Switch Context
When user specifies a context name (or selects from list):
- Validate the requested context template exists: `.olaf/data/context/context-{name}.md`
- Use shell to copy template to active context: copy `.olaf/data/context/context-{name}.md` `.olaf/data/context/context-current.md`
- Confirm the switch was successful
- **CRITICAL**: Clearly inform user that they MUST start a new session/conversation for the new context to be loaded and take effect
- Provide explicit instruction: "⚠️ **IMPORTANT**: Please start a new conversation for the '{context_name}' context to be active. The context change will only take effect in a fresh session."

### 4. Clear Context
If user wants to remove context:
- Delete `.olaf/data/context/context-current.md` if it exists
- Confirm context has been cleared
- **CRITICAL**: Inform user that they MUST start a new session for the context clearing to take effect
- Provide explicit instruction: "⚠️ **IMPORTANT**: Please start a new conversation for the context clearing to be active."

## Commands Handled
- "context switch {name}" - Switch to specific context
- "context switch" or "context list" - List existing contexts in .olaf/data/context/ directory
- "context clear" - Remove current context
- "context status" - Show current active context

## Output Format
You WILL generate outputs in the following formats based on user request:

**List Format (Default):**
```
Available contexts:
1. default - [description]
2. springboot-hexagonal - [description]

Select a context by number or name:
```

**Detailed Format:**
- Full context metadata and file paths
- IDE steering documents for each context
- Current active context status
- Suggested next actions
**Status Format:**
- Current active context
- Number of available contexts
- **Status Format**: Show current active context status and available contexts

## User Communication
You WILL provide clear communication throughout the workflow:

### Progress Updates
- Status of context detection
- Number of contexts found and available
- Completion with summary statistics

### Results Presentation
- **Available Contexts**: List all contexts with descriptions
- **Current Status**: Display active context and last update time
- **Available Options**: Numbered list with selection prompt

### Session Transition Guidance
- **Critical Alert**: "⚠️ **IMPORTANT**: Please start a new conversation for the context to be active"
- **Reason Explanation**: "Context changes take effect only in fresh sessions"
- **User Action**: Clear instruction for starting new conversation
- **Timeline**: Immediate effect after new session begins

## File Operations
- Source templates: .olaf/data/context/context-*.md
- Active context: .olaf/data/context/context-current.md

## Success Criteria
- User can seamlessly switch between available contexts
- Context names are clear and descriptive
- Numbered list selection for easy context choosing
- Context-specific instructions are loaded automatically in new sessions
- **Clear and prominent notification** that users must start a new session for context changes to take effect
- Clear feedback on available contexts and current status
- Robust error handling for missing files

## Implementation Notes
- No repo scanning or generation.
- Only operate on files under `.olaf/data/context/`.
- List existing `context-*.md`, switch by copying to `context-current.md`, or clear by deleting it.

### Validation Rules
- List only existing context-*.md files from `.olaf/data/context/`
- Validate user selection is within range for numbered choices
- Confirm context file exists before copying

### File Reading for Descriptions
- Read first few lines of each context-*.md file
- Look for markdown headers, comments, or first paragraph as description
- Fallback to "No description available" if content is minimal
- Truncate long descriptions to keep list readable

## Error Handling
- Handle missing context templates gracefully
- Provide clear error messages for invalid context names and selections
- Validate file operations before execution
- Validate user selection is within range for numbered choices
