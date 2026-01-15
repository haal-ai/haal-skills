---
name: create-prompt-description
description: Generate description.md documentation for existing prompts
license: Apache-2.0
metadata:
  olaf_tags: [documentation, prompt, description, generate]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **prompt_name**: string - The name/ID of the prompt to document (REQUIRED)
- **prompt_path**: string - Absolute path to the prompt directory (OPTIONAL - will be auto-detected if not provided)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act for documentation generation due to file creation impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
<!-- <prompt_identification> -->
- If `prompt_name` not provided, list available prompts in `skills/` and ask user to select
- Validate prompt exists at `skills/[prompt_name]/`
- Confirm main prompt file exists at `skills/[prompt_name]/prompts/[prompt_name].md`
- Check if `/docs/` directory exists; create if missing
- Verify `/docs/description.md` doesn't already exist (warn user if it does, ask for confirmation to overwrite)
<!-- </prompt_identification> -->

### 2. Execution Phase

**Prompt Analysis:**
<!-- <read_prompt> -->
You MUST read and analyze the target prompt file:
- Read: `skills/[prompt_name]/prompts/[prompt_name].md`
- Extract prompt metadata (name, description, tags from frontmatter)
- Identify input parameters and their types
- Determine user interaction protocol
- Extract process steps and workflow
- Identify output format and deliverables
- Note domain-specific rules and constraints
- Capture success criteria
- Document error handling scenarios
<!-- </read_prompt> -->

**Manifest Analysis:**
<!-- <read_manifest> -->
You SHOULD read skill manifest if available:
- Read: `skills/[prompt_name]/skill-manifest.json`
- Extract additional metadata (objectives, aliases, version)
- Identify BOM components (templates, tools, helpers, kb)
- Note skill dependencies if any
<!-- </read_manifest> -->

**Core Logic**: Generate description.md following proposal-confirmation workflow
<!-- <generate_description> -->
You WILL generate description.md with these sections:
1. **Overview** - What the prompt does (1-2 sentences)
2. **Purpose** - Why this prompt exists and when to use it
3. **Key Features** - Bullet list of main capabilities
4. **Usage** - How to invoke the prompt (with aliases if available)
5. **Parameters** - Required and optional parameters with descriptions
6. **Process Flow** - High-level steps the prompt executes
7. **Output** - What the prompt generates/produces
8. **Examples** - Common use cases (if identifiable from prompt)
9. **Error Handling** - Common errors and resolutions
10. **Related Skills** - Dependencies or complementary skills (if any)

**IMPORTANT**: Description MUST be clear, concise, and user-focused
<!-- </generate_description> -->

### 3. Proposal Phase
You WILL present the generated documentation:
<!-- <propose_content> -->
- Display generated description.md content for user review
- Highlight key sections: Overview, Parameters, Usage
- Indicate save location: `skills/[prompt_name]/docs/description.md`
- Ask user: "Ready to save this documentation?" (yes/no/edit)
<!-- </propose_content> -->

### 4. Confirmation Phase
You WILL await final user approval:
<!-- <confirm_save> -->
- If user says "edit", ask what changes are needed and regenerate
- If user says "no", ask if they want to cancel or provide different requirements
- If user says "yes", proceed to save the file
<!-- </confirm_save> -->

### 5. Save Phase
You WILL save the documentation:
<!-- <save_documentation> -->
- Ensure directory exists: `skills/[prompt_name]/docs/`
- Save file: `skills/[prompt_name]/docs/description.md`
- Confirm successful save
<!-- </save_documentation> -->

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: `description.md` file in markdown format
- File location: `skills/[prompt_name]/docs/description.md`
- Format: Well-structured markdown with clear headings and sections
- Style: Professional, concise, user-focused documentation

## User Communication

### Progress Updates
- Confirmation when prompt is found and validated
- Status when reading and analyzing prompt content
- Notification when description is being generated
- Presentation of generated content for review

### Completion Summary
- Documentation generated and presented for review
- Save location confirmed: `skills/[prompt_name]/docs/description.md`
- File successfully saved (after confirmation)
- Next steps: Documentation is ready for use

### Next Steps
You WILL clearly define:
- Documentation saved successfully
- Location: `skills/[prompt_name]/docs/description.md`
- User can now view/edit the description as needed
- Consider creating tutorial.md for step-by-step usage guide

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER overwrite existing description.md without explicit user confirmation
- Rule 2: Description MUST be accurate to the actual prompt functionality
- Rule 3: Generated documentation MUST be in US English
- Rule 4: Save location MUST be in the prompt's /docs/ folder
- Rule 5: If prompt doesn't exist, list available prompts for user selection
- Rule 6: Documentation MUST follow markdown best practices
- Rule 7: All sections in description.md MUST be populated (no empty sections)
- Rule 8: Parameters MUST clearly indicate REQUIRED vs OPTIONAL

## Success Criteria
You WILL consider the task complete when:
- [ ] Prompt identified and validated
- [ ] Prompt file successfully read and analyzed
- [ ] Skill manifest read (if available)
- [ ] description.md generated with all required sections
- [ ] Content presented to user for review
- [ ] User provided final confirmation
- [ ] File saved to correct location: `skills/[prompt_name]/docs/description.md`
- [ ] User notified of successful save
- [ ] Next steps communicated

## Required Actions
1. Validate prompt exists and read prompt file
2. Analyze prompt content and extract key information
3. Generate comprehensive description.md following Propose-Confirm-Act protocol
4. Save file after user confirmation
5. Confirm completion and provide next steps

## Error Handling
You WILL handle these scenarios:
- **Prompt Not Found**: List available prompts in `skills/` and ask user to select
- **Missing Prompt Name**: List available prompts and ask user which one to document
- **Prompt File Missing**: Alert user that prompt structure is incomplete, cannot generate documentation
- **description.md Already Exists**: Warn user and ask for confirmation to overwrite
- **/docs/ Directory Missing**: Create directory automatically before saving
- **File Save Failure**: Provide alternative save location suggestions
- **User Rejection During Review**: Ask for specific feedback and regenerate documentation
- **Invalid Prompt Structure**: Alert user and suggest running validation or repair skill
- **Cannot Read Prompt File**: Check file permissions and provide troubleshooting steps

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol for all documentation generation
- MANDATORY: Read and analyze actual prompt content before generating description
- MANDATORY: Save description.md in prompt's /docs/ folder (not elsewhere)
- MANDATORY: Generate all sections (no incomplete documentation)
- NEVER overwrite existing description.md without user confirmation
- NEVER generate documentation without reading the actual prompt file
- ALWAYS validate prompt exists before attempting documentation
- ALWAYS present generated content for user review before saving
- ALWAYS provide clear, accurate, user-focused documentation
