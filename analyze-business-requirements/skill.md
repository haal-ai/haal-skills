---
name: analyze-business-requirements
description: Guide the process of reviewing a business requirements document to identify potential issues and generate clarifying questions
license: Apache-2.0
metadata:
  olaf_tags: [business, requirements, analysis, review, documentation]
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
- **requirements_document**: string - Path to the business requirements document to analyze (REQUIRED)
- **strict_template_compliance**: boolean - Whether to strictly follow the template format (OPTIONAL, default: true)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Select appropriate protocol based on operation risk and impact

## Prerequisites (if applicable)
If this prompt is part of a workflow chain:
1. You MUST verify the preceding phase/action was completed
2. You WILL validate expected outcomes from previous step:
   - Business requirements document is available and accessible
   - Required template files exist in the system
   - Staging directory is accessible for output storage

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate requirements document exists and is accessible
- Check access to required tools and files

### 2. Execution Phase
You WILL execute these operations as needed:

**Terminal Operations** (when required):
- Get current timestamp using time tools, fallback to shell command if needed
- Validate command execution success

**Tool Operations** (when required):
- Use internal tool: `file_reader` for document analysis
- Use internal tool: `file_writer` for report generation

**File Operations** (when required):
- Read/Write file: `[requirements_document]` - Parse document structure and content
- Read/Write file: `.olaf/data/practices/guidances/requirements/expressing-business-needs-to-developers.md` - Apply analysis frameworks
- Read/Write file: `.olaf/data/practices/guidances/requirements/reviewing-business-requirements-for-dev-and-test.md` - Reference quality criteria
- Read/Write file: `templates/requirements-analysis-report-template.md` - Structure output format
- Write file: `.olaf/work/staging/business-requirements-analysis-YYYYMMDD-NNN.md` - Save analysis report

**Core Logic**: Execute following protocol requirements
- Apply appropriate interaction protocol
- Identify key requirements and potential structural issues
- Extract business objectives and functional requirements
- Categorize issues by severity and type (ambiguity, incompleteness, testability, inconsistencies)
- Generate constructive clarifying questions for each identified issue
- Structure analysis according to template format
- Provide actionable recommendations for improvement
- Complete core processing steps
- Provide required user confirmations

### 3. Validation Phase
You WILL validate results:
- Confirm all outputs meet template requirements
- Verify all issues include specific document section references
- Ensure constructive feedback guides improvement

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Follow template `templates/requirements-analysis-report-template.md`
- Supporting files: Analysis report saved to staging directory
- Documentation: Markdown format with proper categorization

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when each major step completes
- Location/reference of any changes made
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Summary of actions taken
- Files created/modified with locations
- Any issues encountered and resolutions

### Next Steps (if part of workflow)
You WILL clearly define:
- Immediate next actions required
- Objectives for next phase (concise, specific)
- Files/resources provided to next phase
- Dependencies for next step

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Always reference specific sections when identifying issues
- Rule 2: Generate constructive questions that guide toward solutions  
- Rule 3: Categorize issues by type (ambiguity, incompleteness, testability, inconsistencies)
- Rule 4: Follow official template structure strictly for consistency

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated
- [ ] Core logic executed successfully
- [ ] Outputs generated in specified format
- [ ] User communication completed
- [ ] Next steps defined (if applicable)

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute operations following appropriate interaction protocol
3. Generate outputs in specified format
4. Provide user communication and confirmations
5. Define next steps if part of workflow

## Error Handling
You WILL handle these scenarios:
- **Missing Parameters**: Request specific missing items from user
- **File Access Issues**: Provide clear error message and resolution steps
- **Tool Failures**: Offer alternative approaches or manual steps
- **Validation Failures**: Stop process and request user guidance

⚠️ **Critical Requirements**
- MANDATORY: Follow established interaction protocol (Act/Propose-Act/Propose-Confirm-Act)
- NEVER bypass protocol requirements
- ALWAYS validate outputs before considering task complete
- ALWAYS provide rollback instructions for destructive operations
- ALWAYS document assumptions and limitations
- ALWAYS confirm user approval for significant changes

