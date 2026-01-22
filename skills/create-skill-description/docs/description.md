# Create Skill Description

## Overview
The `create-skill-description` skill generates comprehensive `docs/description.md` documentation files for existing skills in the OLAF framework.

## Purpose
This skill automates the documentation process for skills by analyzing their content and structure, then generating well-formatted description files that explain what the skill does, how to use it, and what parameters it requires. This ensures consistent, high-quality documentation across all skills.

## Key Features
- **Interactive Skill Selection** - Lists available skills if name not provided
- **Automatic Content Analysis** - Reads and extracts key information from skill files
- **Structured Documentation** - Generates comprehensive descriptions with standardized sections
- **Safe Overwrite Protection** - Warns before overwriting existing documentation
- **User Review Process** - Shows generated content before saving (asks for user approval)

## Usage

### Invocation
You can trigger this skill using any of these commands:
- `olaf create-skill-description`
- `olaf document skill`
- `olaf generate skill docs`
- `olaf add skill description`
- `olaf create description file`

### Basic Usage
1. Invoke the skill with one of the commands above
2. Provide the skill name when asked (or select from list)
3. Review the generated description.md content
4. Confirm to save or request edits

## Parameters

### Required Parameters
- **skill_name** (string) - The name/ID of the skill to document
  - Must match an existing skill directory in `skills/`
  - If not provided, skill will list available skills for selection

### Optional Parameters
- **skill_path** (string) - Absolute path to the skill directory
  - Auto-detected if not provided
  - Only needed for skills in non-standard locations

## Process Flow

1. **Validation** - Verify skill exists and locate its files
2. **Analysis** - Read the skill file to extract metadata, parameters, process, outputs, and rules
3. **Generation** - Create description.md with comprehensive documentation sections
4. **Proposal** - Present generated content to user for review
5. **Confirmation** - Wait for user approval or edit requests
6. **Save** - Write description.md to the skill's /docs/ folder

## Output

The skill generates a `description.md` file saved to:
```
skills/[skill-name]/docs/description.md
```

### Description Sections
1. Overview - Brief summary of skill functionality
2. Purpose - Why the skill exists and when to use it
3. Key Features - Main capabilities and highlights
4. Usage - Invocation commands and basic workflow
5. Parameters - Required and optional parameters with descriptions
6. Process Flow - High-level execution steps
7. Output - What the skill produces
8. Examples - Common use cases
9. Error Handling - Common errors and solutions
10. Related Skills - Dependencies or complementary skills

## Examples

### Example 1: Document a Specific Skill
```
User: olaf create-skill-description
Assistant: Which skill would you like to document?
User: review-code-quality
Assistant: [Analyzes skill and generates description]
         [Shows generated content]
         Ready to save this documentation? (yes/no/edit)
User: yes
Assistant: ✅ Documentation saved to skills/review-code-quality/docs/description.md
```

### Example 2: Using Skill Name Parameter
```
User: olaf create-skill-description for generate-test-cases
Assistant: [Analyzes skill]
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

**Skill Not Found**
- **Symptom**: Specified skill doesn't exist
- **Resolution**: Skill lists available skills for selection

**Missing Skill File**
- **Symptom**: Skill directory exists but main skill file missing
- **Resolution**: Alert user to incomplete skill structure

**description.md Already Exists**
- **Symptom**: Target file already exists
- **Resolution**: Warn user and request confirmation to overwrite

**File Save Failure**
- **Symptom**: Cannot write to /docs/ folder
- **Resolution**: Check permissions, suggest alternative locations

## Related Skills

- **create-skill** - Creates new skills (which this skill documents)
- **convert-prompt-to-skill** - Converts prompt content into a skill structure

## Notes

- This skill uses the **Propose-Confirm-Act** protocol for safety
- Documentation is auto-generated but can be edited after saving
- Existing description.md files are preserved unless user confirms overwrite
- The skill analyzes the target skill's `skill.md` to generate accurate documentation
