# create-skill-description

## Overview
Generates comprehensive description.md documentation for existing skills by analyzing skill files and extracting key information into a standardized, user-focused format.

## Purpose
This skill exists to automate the creation of skill documentation, ensuring consistent, complete, and accurate descriptions for all skills. Use it when you've created a new skill and need documentation, or when updating documentation for existing skills.

## Key Features
- Automatic skill discovery and validation
- Comprehensive skill file analysis
- Structured documentation generation with 10 standard sections
- User review and approval workflow before saving
- Overwrite protection with explicit confirmation
- Automatic directory creation if missing
- Clear, concise, user-focused writing style
- Markdown best practices enforcement

## Usage
Invoke this skill by saying:
- "create skill description for [skill_name]"
- "generate documentation for [skill_name]"
- "document the [skill_name] skill"

## Parameters

### Required
- **skill_name**: string - The name/ID of the skill to document

### Optional
- **skill_path**: string - Absolute path to the skill directory (will be auto-detected if not provided)

## Process Flow
1. **Validation Phase** - Validates skill exists, checks for existing description.md
2. **Execution Phase** - Reads and analyzes skill file, extracts metadata and structure
3. **Proposal Phase** - Presents generated documentation for user review
4. **Confirmation Phase** - Awaits user approval (yes/no/edit)
5. **Save Phase** - Saves file to `skills/[skill_name]/docs/description.md`

## Output
- `description.md` file in markdown format
- Saved to: `skills/[skill_name]/docs/description.md`
- Contains 10 standard sections: Overview, Purpose, Key Features, Usage, Parameters, Process Flow, Output, Examples, Error Handling, Related Skills

## Examples
- Generating documentation for a newly created skill
- Updating documentation after skill modifications
- Creating consistent documentation across a skill library

## Error Handling
- **Skill Not Found**: Lists available skills and asks user to select
- **Missing Skill Name**: Lists available skills and asks which to document
- **Skill File Missing**: Alerts that skill structure is incomplete
- **description.md Already Exists**: Warns user and asks for confirmation to overwrite
- **/docs/ Directory Missing**: Creates directory automatically before saving
- **File Save Failure**: Provides alternative save location suggestions
- **User Rejection During Review**: Asks for specific feedback and regenerates
- **Invalid Skill Structure**: Suggests running validation or repair skill
- **Cannot Read Skill File**: Checks file permissions and provides troubleshooting

## Related Skills
- **create-skill**: For creating new skills with structure and templates
- **create-prompt**: For creating simpler prompt files
