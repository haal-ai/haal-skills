---
name: generate-pptx-from-plan
description: Generate PowerPoint presentations from existing presentation plans using automated Python tools
license: Apache-2.0
metadata:
  olaf_tags: [presentation, powerpoint, automation, technical-writer, content-creation]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

## Input Parameters
You MUST request these parameters if not provided by the user:
- **plan_file_path**: string - Path to existing presentation plan (.md file) (REQUIRED)
- **output_directory**: string - Target directory for PowerPoint file (OPTIONAL, default: `.olaf/work/staging/pptx-folder/`)
- **confirmation**: boolean - User approval to proceed with generation (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- **Protocol**: Act (for direct PowerPoint generation with user confirmation)
- Present plan and get user confirmation before proceeding with generation

## Prerequisites (if applicable)
If this skill is part of a workflow chain:
1. You MUST verify the preceding phase/action was completed
2. You WILL validate expected outcomes from previous step:
   - Presentation plan file exists and is properly formatted
   - Plan follows expected markdown structure with slides
   - Content is properly structured for PowerPoint conversion

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate presentation plan file exists and is accessible
- Check Python environment and required dependencies
- Verify access to PowerPoint generation tool

### 2. Execution Phase
You WILL execute these operations as needed:

**Dependency Check**:
- Execute command: `pip show python-pptx` to verify library installation
- Execute command: `pip install python-pptx` if library not found
- Confirm Python environment has required dependencies

**Plan Validation**:
- Read file: `plan_file_path` to verify structure and content
- Validate plan follows expected markdown format
- Check that slide content is properly formatted (no bullet prefixes)
- Ensure plan structure is compatible with generation tool

**PowerPoint Generation**:
- Execute script: `/tools/generate_dynamic_pptx.py` for PowerPoint automation
- Execute command: `python /tools/generate_dynamic_pptx.py [plan-file-path] .olaf/work/staging/pptx-folder/`
- Monitor generation process for any errors or issues
- Ensure the output PowerPoint file is saved in `.olaf/work/staging/pptx-folder/`

### 3. Validation Phase
You WILL confirm successful completion:
- Verify PowerPoint file is created successfully
- Confirm presentation structure matches the plan
- Check that slides are properly formatted and readable
- Validate that content appears correctly in PowerPoint format

## Output Format
Define your expected outputs:
- **Format**: PowerPoint presentation (.pptx file)
- **Structure**: Slides generated from markdown plan with proper formatting
- **File outputs**: Timestamped PowerPoint file in staging directory
- **Naming conventions**: `[plan-name]-YYYYMMDD-HHmm.pptx`

## User Communication
Define communication patterns:
- **Progress updates**: Report dependency checks, plan validation, and generation progress
- **Confirmations**: Request user approval before proceeding with generation
- **Error reporting**: Clear messages for dependency, file access, or generation issues
- **Success indicators**: Confirmation of successful PowerPoint creation with file summary

## Domain-Specific Rules
Include rules specific to your skill domain:
- **Restrictions**: Only process properly formatted markdown presentation plans
- **Standards**: PowerPoint files must maintain original plan structure and formatting
- **Conventions**: Use timestamped naming for output files in staging directory
- **Validations**: Verify python-pptx library availability before generation

## Success Criteria
Define measurable success outcomes:
- [ ] All required parameters provided (plan file path, confirmation)
- [ ] Python environment and dependencies verified
- [ ] Presentation plan validated and properly formatted
- [ ] PowerPoint generation completed successfully
- [ ] Output file created in correct staging location
- [ ] User confirms satisfaction with generated presentation

## Error Handling
Define error scenarios and responses:
- **Missing parameters**: Request specific plan file path or confirmation
- **Tool failures**: Check Python installation, install python-pptx if missing
- **File access issues**: Validate plan file paths and staging directory permissions
- **Validation failures**: Report plan format issues and provide correction guidance
- **Generation errors**: Provide clear error messages and retry procedures

## Technical Requirements

### Dependencies
- Python environment (3.10+ recommended)
- python-pptx library (will be checked and installed if needed)
- Access to `/tools/generate_dynamic_pptx.py` automation tool
- Write access to `.olaf/work/staging/pptx-folder/`

### File Formats
- **Input**: Markdown presentation plan (.md)
- **Output**: PowerPoint presentation (.pptx)
- **Naming**: Timestamped format YYYYMMDD-HHmm

### Output Location
Generated PowerPoint file: `.olaf/work/staging/pptx-folder/[name]-YYYYMMDD-HHmm.pptx`

## Notes
This skill specializes in automated PowerPoint generation from structured presentation plans using Python automation tools. It maintains compatibility with existing presentation planning workflows and ensures professional output formatting.
