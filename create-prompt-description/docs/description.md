# Create Prompt Description

## Overview
The `create-prompt-description` skill generates comprehensive `description.md` documentation files for existing prompts in the OLAF framework.

## Purpose
This skill automates the documentation process for prompts by analyzing their content and structure, then generating well-formatted description files that explain what the prompt does, how to use it, and what parameters it requires. This ensures consistent, high-quality documentation across all prompts.

## Key Features
- **Interactive Prompt Selection** - Lists available prompts if name not provided
- **Automatic Content Analysis** - Reads and extracts key information from prompt files
- **Manifest Integration** - Incorporates metadata from skill manifests when available
- **Structured Documentation** - Generates comprehensive descriptions with standardized sections
- **Safe Overwrite Protection** - Warns before overwriting existing documentation
- **User Review Process** - Shows generated content before saving (Propose-Confirm-Act protocol)

## Usage

### Invocation
You can trigger this skill using any of these commands:
- `olaf create-prompt-description`
- `olaf document prompt`
- `olaf generate prompt docs`
- `olaf add prompt description`
- `olaf create description file`

### Basic Usage
1. Invoke the skill with one of the commands above
2. Provide the prompt name when asked (or select from list)
3. Review the generated description.md content
4. Confirm to save or request edits

## Parameters

### Required Parameters
- **prompt_name** (string) - The name/ID of the prompt to document
  - Must match an existing prompt directory in `skills/`
  - If not provided, skill will list available prompts for selection

### Optional Parameters
- **prompt_path** (string) - Absolute path to the prompt directory
  - Auto-detected if not provided
  - Only needed for prompts in non-standard locations

## Process Flow

1. **Validation** - Verify prompt exists and locate its files
2. **Analysis** - Read prompt file and skill manifest to extract information
3. **Generation** - Create description.md with comprehensive documentation sections
4. **Proposal** - Present generated content to user for review
5. **Confirmation** - Wait for user approval or edit requests
6. **Save** - Write description.md to the prompt's /docs/ folder

## Output

The skill generates a `description.md` file saved to:
```
skills/[prompt-name]/docs/description.md
```

### Description Sections
1. Overview - Brief summary of prompt functionality
2. Purpose - Why the prompt exists and when to use it
3. Key Features - Main capabilities and highlights
4. Usage - Invocation commands and basic workflow
5. Parameters - Required and optional parameters with descriptions
6. Process Flow - High-level execution steps
7. Output - What the prompt produces
8. Examples - Common use cases
9. Error Handling - Common errors and solutions
10. Related Skills - Dependencies or complementary skills

## Examples

### Example 1: Document a Specific Prompt
```
User: olaf document prompt
Assistant: Which prompt would you like to document?
User: review-code-quality
Assistant: [Analyzes prompt and generates description]
         [Shows generated content]
         Ready to save this documentation? (yes/no/edit)
User: yes
Assistant: ✅ Documentation saved to skills/review-code-quality/docs/description.md
```

### Example 2: Using Prompt Name Parameter
```
User: olaf create-prompt-description for generate-test-cases
Assistant: [Analyzes prompt]
         [Generates and shows description]
         Ready to save? (yes/no/edit)
User: edit
Assistant: What changes would you like?
User: Add more examples
Assistant: [Regenerates with additional examples]
         Ready to save? (yes/no/edit)
User: yes
```

## Error Handling

### Common Errors

**Prompt Not Found**
- **Symptom**: Specified prompt doesn't exist
- **Resolution**: Skill lists available prompts for selection

**Missing Prompt File**
- **Symptom**: Prompt directory exists but main prompt file missing
- **Resolution**: Alert user to incomplete prompt structure

**description.md Already Exists**
- **Symptom**: Target file already exists
- **Resolution**: Warn user and request confirmation to overwrite

**File Save Failure**
- **Symptom**: Cannot write to /docs/ folder
- **Resolution**: Check permissions, suggest alternative locations

## Related Skills

- **create-prompt** - Creates new prompts (which this skill documents)
- **convert-prompt** - Converts instructions to prompts (may need documentation afterward)
- **create-skill** - Creates complex skills with multiple components

## Notes

- This skill uses the **Propose-Confirm-Act** protocol for safety
- Documentation is auto-generated but can be edited after saving
- Existing description.md files are preserved unless user confirms overwrite
- The skill analyzes both the prompt file and skill manifest for complete information
