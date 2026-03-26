# generate-step-by-step-tutorial

## Overview
Generate step-by-step tutorial documents from conversations or workflow files. Captures a process as a reusable, structured guide.

## Purpose
Turn ad-hoc conversations and workflows into permanent, well-structured tutorials. Use after completing a complex task or workflow that others might need to repeat.

## Key Features
- Two source types: current conversation or file-based workflow
- Multilingual support (English, French, Spanish, German)
- Timestamped output for version tracking
- Structured template with numbered steps
- Validation phase to ensure source quality
- User approval before file creation

## Usage
Invoke this skill by saying:
- "Generate a tutorial from this conversation"
- "Create a step-by-step guide from our workflow"
- "Document this process as a tutorial"

## Parameters

### Required
- **source_type**: current_conversation | file
- **workflow_name**: Name of the workflow/process being documented
- **source_file**: Path to workflow file (if source_type is "file")

### Optional
- **target_language**: English | French | Spanish | German (default: English)
- **tutorial_title**: Custom title (auto-generated if not provided)

## Process Flow
1. **Validation** — Verify source exists and has enough content
2. **Source Analysis** — Extract steps, decisions, and outcomes
3. **Structure Planning** — Organize into logical tutorial sections
4. **Draft Generation** — Create tutorial using template format
5. **User Review** — Present for approval
6. **Save** — Write timestamped tutorial file

## Output
- Markdown tutorial file with numbered steps, prerequisites, and outcomes
- Saved with timestamp in the filename

## Related Skills
- **create-practice-from-evidence**: Create practices from conversation evidence
- **onboard-local**: Generates standards from codebase analysis
