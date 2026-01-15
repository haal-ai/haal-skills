# Create Skill

**Source**: skills/create-skill/prompts/create-skill.md

## Overview

Create Skill is a comprehensive skill that generates new structured skills following OLAF's established skills architecture and best practices. It guides you through the entire skill creation lifecycle, from initial requirements gathering to skill manifest creation and proper directory structure setup.

## Purpose

Creating high-quality, consistent skills is essential for maintaining OLAF's effectiveness and reliability in the new skills-based architecture. This skill solves the challenge of ensuring all skills follow the proper structure, include complete manifests, have proper dependency management, and integrate seamlessly with the OLAF framework. It eliminates the guesswork from skill engineering by providing a structured, validated approach.

## Usage

**Command**: `create skill`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this skill whenever you need to create a new skill in the OLAF skills architecture. It's particularly valuable when you want to ensure your skill follows all OLAF standards, includes proper error handling, has complete metadata, and integrates correctly with the skills registry.

## Parameters

### Required Inputs
- **user_request**: The requirement or task description that the new skill should address
- **skill_name**: Desired name for the skill (max 4 words, kebab-case format)
- **skill_type**: Type of skill being created: "orchestrator", "workflow", or "prompt"

### Optional Inputs
None - all parameters are required for proper skill creation

### Context Requirements
- Access to OLAF skills directory structure
- Read access to skill templates and prompting principles
- Write access to skills folder for new skill creation
- Terminal access for timestamp generation
- Access to skill manifest schema for validation

## Output

**Deliverables**:
- Complete skill directory structure under `skills/[skill_name]/`
- Main skill prompt file following OLAF template
- Skill manifest (skill-manifest.json) conforming to schema
- Documentation files (description.md, tutorial.md)
- Proper BOM (Bill of Materials) with all dependencies
- Validation checklist confirming schema compliance

**Format**: Complete skill package with proper directory structure and manifest

## Examples

### Example 1: Creating a Code Analysis Skill

**Input**:
- user_request: "Create a skill to analyze code quality and suggest improvements"
- skill_name: "analyze-code-quality"
- skill_type: "prompt"

**Output**: Complete skill at `skills/analyze-code-quality/` with:
- `prompts/analyze-code-quality.md` - Main skill prompt
- `skill-manifest.json` - Complete metadata and BOM
- `docs/description.md` - Skill documentation
- `docs/tutorial.md` - Step-by-step usage guide

### Example 2: Creating an Orchestrator Skill

**Input**:
- user_request: "Create an orchestrator skill to manage a complete development workflow"
- skill_name: "dev-workflow-manager"
- skill_type: "orchestrator"

**Output**: Complete orchestrator skill with workflow coordination capabilities

## Related Skills

- **convert-prompt**: Convert existing prompts to skills format
- **check-prompt-compliance**: Validate created skills against standards
- **generate-step-by-step-tutorial**: Create detailed tutorials for skills

## Tips

1. **Choose descriptive names**: Use clear, action-oriented names that describe what the skill does
2. **Select appropriate type**: 
   - Use "prompt" for simple, standalone skills
   - Use "orchestrator" for complex skills that coordinate multiple operations
   - Use "workflow" for step-by-step process skills
3. **Provide clear requirements**: The more detailed your user_request, the better the generated skill
4. **Review generated structure**: Always review the complete skill structure before approval
5. **Test your skill**: After creation, test the skill to ensure it works as expected

## Limitations

- Requires proper OLAF framework setup and access to skills directory
- Cannot automatically migrate dependencies from other systems
- Generated skills require manual testing and refinement
- Complex orchestrator skills may need additional workflow coordination setup
- BOM dependencies must be manually populated for external tool dependencies

## Best Practices

1. **Follow naming conventions**: Always use kebab-case, max 4 words
2. **Define clear objectives**: Include specific, measurable objectives in your user request
3. **Consider dependencies**: Think about what templates, tools, or knowledge base articles your skill will need
4. **Plan for error handling**: Consider edge cases and failure scenarios in your requirements
5. **Document thoroughly**: Provide comprehensive documentation for skill usage and maintenance