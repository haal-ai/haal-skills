# Create Skill

## Overview

Create Skill generates new structured skills following OLAF's established skills architecture and best practices. It guides you through the entire skill creation lifecycle, from initial requirements gathering to proper directory structure setup, ensuring all skills follow consistent standards.

## Purpose

Creating high-quality, consistent skills is essential for maintaining OLAF's effectiveness and reliability. This skill solves the challenge of ensuring all skills follow the proper structure, include clear input parameters and success criteria, use imperative language, and integrate seamlessly with the OLAF framework.

## Key Features

### 1. Structured Skill Generation
- Follows OLAF skill template structure exactly
- Uses imperative language throughout (WILL/MUST/NEVER)
- Includes comprehensive error handling
- Has measurable success criteria

### 2. Component Support
- Optional templates folder for external template files
- Optional tools folder for scripts and utilities
- Optional helpers folder for reusable prompt fragments
- Optional kb folder for knowledge base articles

### 3. Plugin Integration
- Validates target plugin exists or creates it
- Updates `.olaf/plugins.json` automatically
- Adds plugin to skill metadata

### 4. Duplicate Detection
- Checks all supported skill roots for conflicts
- Prevents accidental overwrites
- Offers update-in-place or rename options

### 5. Skill Location Discovery
- Automatically determines skills root directory
- Supports multiple agent runtimes (Windsurf, Claude, GitHub Copilot)
- Respects user-provided paths

## Usage

**Command**: `create skill`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this skill when you need to create a new skill in the OLAF skills architecture. It's particularly valuable when you want to ensure your skill follows all OLAF standards, includes proper error handling, has complete metadata, and integrates correctly with the framework.

## Parameters

### Required Inputs
- **user_request**: The requirement or task description for the skill
- **target_plugin**: Plugin name to assign the skill to

### Optional Inputs
- **skill_name**: Desired name for the skill (max 4 words, kebab-case)
- **skill_type**: Type of skill: "orchestrator", "workflow", or "prompt" (default: "prompt")
- **agent_runtime**: One of: "windsurf", "cascade", "github-copilot", "claude-code", "other"
- **skills_root**: Explicit destination root folder for skills
- **needs_templates**: Whether skill needs external template files (default: false)
- **template_list**: List of template names if needs_templates=true
- **needs_tools**: Whether skill needs tool/script files (default: false)
- **tool_list**: List of tool names if needs_tools=true
- **needs_helpers**: Whether skill needs helper utility files (default: false)
- **helper_list**: List of helper names if needs_helpers=true
- **needs_kb**: Whether skill needs knowledge base articles (default: false)
- **kb_list**: List of kb article names if needs_kb=true

### Context Requirements
- Access to OLAF skills directory structure
- Read access to skill templates and prompting principles
- Write access to the repository for new skill creation
- Terminal access for timestamp generation

## Output

**Deliverables**:
- Complete skill directory structure at `${skills_root}/[skill_name]/`
- Main skill prompt file (`skill.md`) following OLAF template
- Documentation files (`docs/description.md`, `docs/tutorial.md`)
- Optional component folders (templates/, tools/, helpers/, kb/)
- Validation checklist confirming structure and conventions
- Plugin assignment in `.olaf/plugins.json`

**Format**: Complete skill package with proper directory structure

## Examples

### Example 1: Simple Prompt Skill

**Input**:
```
user_request: "Create a skill to analyze code quality and suggest improvements"
skill_name: "analyze-code-quality"
skill_type: "prompt"
target_plugin: "code-quality"
```

**Output**: Complete skill at `[skills_root]/analyze-code-quality/` with:
- `skill.md` - Main skill prompt
- `docs/description.md` - Skill documentation
- `docs/tutorial.md` - Step-by-step usage guide

### Example 2: Skill with Templates

**Input**:
```
user_request: "Create a skill to generate API documentation"
skill_name: "generate-api-docs"
target_plugin: "documentation"
needs_templates: true
template_list: ["api-doc-template", "endpoint-template"]
```

**Output**: Complete skill with:
- `skill.md` - Main prompt with template references
- `docs/` - Documentation files
- `templates/api-doc-template.md` - API documentation template
- `templates/endpoint-template.md` - Endpoint documentation template

### Example 3: Orchestrator Skill

**Input**:
```
user_request: "Create an orchestrator skill to manage a complete development workflow"
skill_name: "dev-workflow-manager"
skill_type: "orchestrator"
target_plugin: "workflows"
needs_tools: true
tool_list: ["workflow-validator.py"]
```

**Output**: Complete orchestrator skill with workflow coordination capabilities and tool scripts

## Related Skills

- **convert-prompt-to-skill**: Convert existing prompts to skill format
- **check-prompt-compliance**: Validate created skills against standards
- **evaluate-prompt-for-adoption**: Evaluate external prompts before creating skills

## Tips & Best Practices

1. **Choose descriptive names**: Use clear, action-oriented names that describe what the skill does
2. **Select appropriate type**: 
   - Use "prompt" for simple, standalone skills
   - Use "orchestrator" for complex skills coordinating multiple operations
   - Use "workflow" for step-by-step process skills
3. **Provide clear requirements**: The more detailed your user_request, the better the generated skill
4. **Review generated structure**: Always review the complete skill structure before approval
5. **Test your skill**: After creation, test the skill to ensure it works as expected
6. **Follow naming conventions**: Always use kebab-case, max 4 words
7. **Plan for error handling**: Consider edge cases and failure scenarios
8. **Document thoroughly**: Provide comprehensive documentation for skill usage

## Limitations

- Requires proper OLAF framework setup and access to skills directory
- Cannot automatically migrate dependencies from other systems
- Generated skills require manual testing and refinement
- Complex orchestrator skills may need additional workflow coordination setup
- Skill name must be unique across all skill roots
- Cannot modify read-only or auto-generated files

