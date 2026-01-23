---
name: analyze-changelog-and-report
description: Analyze changelog register entries, cross-reference with prompt files, identify discrepancies, and generate a summary report.
license: Apache-2.0
metadata:
  olaf_tags: [analysis, changelog, reporting, automation]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response.
1. **start_date**: string (YYYYMMDD) - The start date for changelog analysis (REQUIRED)
2. **prompt_dir**: string - Directory containing prompt files to check against (OPTIONAL)

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before creating or modifying files
- Present options as numbered lists for easy selection
- Select appropriate protocol based on operation risk and impact
- Provide clear progress updates at each major step

## Prerequisites (if applicable)
If this prompt is part of a workflow chain:
1. You MUST verify the preceding phase/action was completed
2. You WILL validate expected outcomes from previous step:
   - Changelog register exists and is accessible
   - Prompt directory is available for verification
   - Staging directory is accessible for output storage

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate date format is YYYYMMDD
- Check access to changelog register and prompt files

### 2. Execution Phase
You WILL execute these operations as needed:

**Terminal Operations** (when required):
- Get current timestamp using time tools, fallback to shell command if needed
- Validate command execution success

**Tool Operations** (when required):
- Use internal tool: `file_reader` for changelog and prompt file analysis
- Use internal tool: `file_writer` for report generation

**File Operations** (when required):
- Read file: `.olaf/data/projects/changelog-register.md` - Extract entries since start_date
- Read files: `[prompt_dir]` - Verify prompt files against changelog entries
- Read file: `skills/analyze-changelog-and-report/templates/changelog-analysis-report-template.md` - Structure output format
- Write file: `.olaf/work/staging/ChangelogSummaries/YYYYMMDD-HHMM-summary.md` - Save analysis report

**Core Logic**: Execute following protocol requirements
- Apply appropriate interaction protocol
- Parse and categorize changelog entries by type/theme
- Cross-reference with prompt files and flag discrepancies
- Present findings to user for confirmation or correction
- Generate comprehensive analysis report
- Complete core processing steps
- Provide required user confirmations

### 3. Validation Phase
You WILL validate results:
- Confirm all outputs meet template requirements
- Verify audit trail is complete and accurate
- Ensure all discrepancies have been addressed or documented

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Follow template `templates/changelog-analysis-report-template.md`
- Supporting files: Analysis report saved to staging directory
- Documentation: Interactive markdown with collapsible sections and summary statistics

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
- Rule 1: Always preserve original changelog data
- Rule 2: Maintain audit trail of all changes
- Rule 3: Flag potential issues but don't auto-correct
- Rule 4: Group related changes by theme/component

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

