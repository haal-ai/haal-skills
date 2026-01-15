---
name: [verb-entity-complement skill name]
description: [Brief description of what this skill accomplishes]
tags: [tag1, tag2, tag3, tag4]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **param_name**: type|options - Description (REQUIRED/OPTIONAL)
- **param_name**: type|options - Description (REQUIRED/OPTIONAL)
- **optional_param**: type|options - Optional description

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Select appropriate protocol based on operation risk and impact

## Prerequisites (if applicable)
If this skill is part of a workflow chain:
1. You MUST verify the preceding phase/action was completed
2. You WILL validate expected outcomes from previous step:
   - [Expected file/data from previous phase]
   - [Required state or configuration]
   - [Specific deliverables that must exist]

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate prerequisites are met (if applicable)
- Check access to required tools and files

### 2. Execution Phase
You WILL execute these operations as needed:

**Terminal Operations** (when required):
- Execute command: `[specific command with parameters]`
- Execute script: `/tools/script-name.[py|sh|ps1|js]` for automation
- Validate command execution success

**Tool Operations** (when required):
- Use internal tool: `tool_name` for [specific purpose]

**File Operations** (when required):
- Read file: `path/to/file.ext` for [purpose]
- Create file: `path/to/new-file.ext` with [content type]
- Update file: `path/to/existing-file.ext` for [specific changes]

### 3. Validation Phase
You WILL confirm successful completion:
- Verify all files are created/modified as expected
- Test functionality/integration (when applicable)
- Confirm deliverables meet requirements

## Output Format
Define your expected outputs:
- **Format**: [markdown|json|text|structured-data]
- **Structure**: Expected sections, headers, data organization
- **File outputs**: Any files that will be created
- **Naming conventions**: How files should be named

## User Communication
Define communication patterns:
- **Progress updates**: How you'll inform user of progress
- **Confirmations**: What you'll ask user to confirm
- **Error reporting**: How you'll communicate issues
- **Success indicators**: How you'll confirm completion

## Domain-Specific Rules
Include rules specific to your skill domain:
- **Restrictions**: What should NOT be done
- **Standards**: Required quality/format standards  
- **Conventions**: Naming, structure, or style requirements
- **Validations**: Specific checks that must pass

## Success Criteria
Define measurable success outcomes:
- [ ] All required parameters provided
- [ ] All prerequisite conditions met
- [ ] All core operations completed successfully
- [ ] All outputs generated in expected format
- [ ] All validations passed
- [ ] User confirms satisfaction with deliverables

## Error Handling
Define error scenarios and responses:
- **Missing parameters**: Request specific missing information
- **Tool failures**: Alternative approaches or clear error communication
- **File access issues**: Permission or path resolution strategies
- **Validation failures**: Correction and retry procedures

## Notes
Additional implementation notes:
- **Dependencies**: External tools, files, or conditions required
- **Performance**: Expected execution time or resource usage
- **Limitations**: Known constraints or edge cases
- **Future improvements**: Planned enhancements or extensions
