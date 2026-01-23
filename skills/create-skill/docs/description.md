# create-skill

## Overview
Creates new skills with complete directory structure, templates, documentation, and optional components (tools, KB articles, helpers), following established skill architecture and prompting principles.

## Purpose
This skill exists to standardize and streamline the creation of new reusable agent capabilities. Use it when you want to build a new skill, formalize a workflow into a reusable component, or create team-shared agent capabilities with proper structure and documentation.

## Key Features
- Step-by-step parameter collection (one question at a time)
- Flexible save locations (user home, workspace, or specific tool folders)
- Automatic skill name suggestion based on goal
- Support for multiple skill types (prompt, workflow, orchestrator)
- Optional component scaffolding (templates, tools, KB, helpers)
- Duplicate detection and conflict resolution
- Automatic documentation generation (description.md, tutorial.md)
- Plugin assignment and metadata management
- Template and principles validation
- External file reference enforcement (no embedded templates)

## Usage
Invoke this skill by saying:
- "create a skill"
- "make a skill for [goal]"
- "build a reusable agent capability"

## Parameters

### Required
1. **goal**: string - What should this skill do? What's the purpose?

### Optional (collected interactively)
2. **skill_name**: string - Skill name (max 4 words, kebab-case) - will be suggested based on goal
3. **skill_type**: string - Type: "orchestrator", "workflow", or "prompt" (default: "prompt")
4. **needs_templates**: boolean - Does it need external template files? (default: false)
5. **needs_tools**: boolean - Does it need tool/script files? (default: false)
6. **needs_kb**: boolean - Does it need knowledge base articles? (default: false)
7. **skills_root**: string - Destination folder for skills (will be auto-detected)

## Process Flow
1. **Parameter Collection Phase** - Collects parameters one at a time in logical order
2. **Validation Phase** - Validates goal, skill name, and skill type
3. **Skill Destination Phase** - Determines save location (user home vs workspace vs specific tool)
4. **Component Discovery Phase** - Gathers template, tool, and KB requirements
5. **Execution Phase** - Loads templates and principles, generates skill structure
6. **Skill Structure Generation Phase** - Creates directories and all required files
7. **Plugin Assignment Phase** - Updates plugins.json and skill metadata
8. **Validation Phase** - Validates generated skill meets all requirements

## Output
- Complete skill directory structure at `${skills_root}/[skill_name]/`
- Main prompt file: `skill.md`
- Documentation files: `docs/description.md`, `docs/tutorial.md`
- Optional component files in `templates/`, `tools/`, `kb/`, `helpers/` folders
- Updated `plugins.json` with skill assignment

## Examples
- Creating a code review skill with custom templates
- Building an API scaffolding skill with tool scripts
- Developing a documentation generation skill with KB articles

## Error Handling
- **Missing/Unclear Requirements**: Requests specific clarification with examples
- **Skills Directory Access Failed**: Provides error message and troubleshooting steps
- **Invalid Skill Name**: Re-requests valid kebab-case name (max 4 words)
- **Template/Principles File Access Failed**: Tries fallback locations
- **Duplicate Skill Found**: Presents existing skill and asks for modification preferences
- **Component Requirements Unclear**: Asks specific questions about each component type
- **Template Separation Issues**: Guides user to separate embedded templates from external references
- **File Save Failures**: Provides alternative save methods and troubleshooting steps
- **External Reference Validation Failed**: Ensures all referenced files exist

## Related Skills
- **create-prompt**: For simpler, single-file prompt creation
- **create-skill-description**: For generating documentation for existing skills
- **convert-prompt-to-skill**: For upgrading prompts to full skills
