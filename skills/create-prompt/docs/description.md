# create-prompt

## Overview
Creates reusable prompt files with proper structure and metadata, transforming informal requests into formalized, structured prompts ready for repeated use.

## Purpose
This skill exists to help users capture and formalize their prompt ideas into well-structured, reusable prompt files. Use it when you want to save a prompt for future use, share prompts with team members, or build a library of standardized prompts for common tasks.

## Key Features
- Interactive parameter collection with numbered lists for easy responses
- Iterative drafting process with user approval at each step
- Automatic application of prompting principles from templates
- Timestamped file naming for version tracking
- Staged output in dedicated prompts folder
- Kebab-case naming convention enforcement
- Metadata generation with tags and descriptions

## Usage
Invoke this skill by saying:
- "create a prompt"
- "make a prompt for [goal]"
- "save this as a reusable prompt"

## Parameters

### Required
- **goal**: string - What the user wants the prompt to do

### Optional
- **intended_user**: string - Who will use this prompt (e.g., "developer", "product manager")
- **context**: string - Project or domain context the prompt should assume
- **constraints**: string - Constraints to respect (e.g., "must be short", "no external tools")
- **prompt_name**: string - Kebab-case name for the prompt (will be suggested if not provided)
- **tags**: array - 3-6 tags for metadata (will be suggested if not provided)

## Process Flow
1. **Validation Phase** - Validates goal clarity and ensures output folder exists
2. **Drafting Phase** - Rewrites user request in clear US English and iterates until approved
3. **Prompt Generation Phase** - Generates complete prompt file using templates and principles
4. **Proposal Phase** - Shows generated content and proposes save location
5. **Save Phase** - Writes file to `.olaf/staging/generated-prompts/` after user confirmation

## Output
- One prompt markdown file saved to `.olaf/staging/generated-prompts/{timestamp}-{prompt_name}.md`
- Summary including final file path
- Reminder to test the prompt before relying on it

## Examples
- Creating a code review prompt for team use
- Formalizing a debugging workflow into a reusable prompt
- Building a prompt library for common development tasks

## Error Handling
- **Missing goal**: Asks user what they want the prompt to do
- **Unsafe prompt_name**: Proposes corrected kebab-case name
- **User rejects draft**: Iterates until approved
- **File write failure**: Explains issue and proposes alternative filename

## Related Skills
- **create-skill**: For creating more complex, multi-file skill structures
- **convert-prompt-to-skill**: For upgrading prompts to full skills
