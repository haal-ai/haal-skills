# List Competencies

## Overview

Displays all available competencies and skills from the OLAF index, helping users discover and understand available OLAF capabilities.

## Purpose

Users need a way to see what competencies and skills are available in OLAF. This skill provides a comprehensive list with metadata, protocols, and usage guidance.

## Usage

**Command**: `list competencies`, `list competency`, `show competencies`, `list olaf commands`, `competency list`

**Protocol**: Act

**When to Use**: When you want to see all available OLAF competencies and skills, or discover what capabilities are available.

## Parameters

None required. Optional: specific category or tag filter.

## Key Features

- **Complete listing**: Shows all available competencies from the index
- **Metadata display**: Includes title, prompt path, and protocol for each
- **Clarifying questions**: Helps narrow down choices if needed
- **Direct execution**: Can execute selected competency immediately
- **Discovery aid**: Helps users understand OLAF's capabilities

## Execution

The skill:
1. Reads the OLAF competency index (`<olaf-query-competency-index>`)
2. Presents a formatted list of competencies with:
   - Competency title
   - Prompt file path
   - Interaction protocol (Act, Propose-Act, Propose-Confirm-Act)
3. Asks clarifying questions if user needs help choosing
4. Executes selected competency when requested

## Output Format

**Example**:
```
1. Analyze project onboarding — prompt: analyze-project-onboarding.md — Protocol: Propose-Act
2. Prepare conversation handover — prompt: prepare-conversation-handover.md — Protocol: Propose-Confirm-Act
3. Store conversation record — prompt: store-conversation-record.md — Protocol: Act
4. Time retrieval — prompt: time-retrieval.md — Protocol: Act
...
```

## User Interaction Flow

1. **List request**: User asks to see competencies
2. **Display list**: Shows all available competencies with metadata
3. **Clarify (optional)**: If needed, ask questions to narrow choices
4. **Selection**: User selects a competency
5. **Execution**: Execute the corresponding competency file

## Clarifying Questions

If user doesn't specify a task, ask:
- "Are you looking for a specific type of task? (e.g., project management, code analysis, documentation)"
- "What area are you interested in? (e.g., git operations, stash management, assessment)"

## Outputs

- Formatted list of all competencies
- Metadata for each competency (title, path, protocol)
- Optional: filtered list based on category/tag
- Optional: execution of selected competency

## Integration

This skill helps users discover and use:
- All skills in `skills/`
- All competencies referenced in the index
- Protocol information for proper usage
- Direct access to competency execution

## Reference Files

- Reads from: `core/reference/query-competency-index.md` (or similar index file)
- Lists items from: `skills/` and legacy `core/competencies/`

## Technical Requirements

- **Recommended LLM**: Validated primarily with Windsurf using GPT Low Reasoning and GitHub Sonnet 4.x
- **Tool Dependency**: Minimal - mostly pure LLM capabilities
- **Platform Limitations**: Cross-platform compatible

## Maintenance

- **Team**: admin
- **Primary Maintainer**: OLAF Framework Core Team
- **Status**: proven
- **Exposure**: kernel
