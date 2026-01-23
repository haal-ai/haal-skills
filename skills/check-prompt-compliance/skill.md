---
name: check-prompt-compliance
description: Check a prompt for compliance with OLAF prompt standards
license: Apache-2.0
metadata:
  olaf_tags: [prompt, compliance, validation, standards]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response.
1. **prompt_text**: string - The prompt content to validate (REQUIRED)
2. **target_context**: string - Context type: skill-prompt, workflow-prompt, tool-prompt, or general (OPTIONAL - default: general)

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before modifying any files
- Present compliance issues as numbered lists for clarity
- Provide clear progress updates at each validation step
- Confirm whether to generate corrected version

## Prerequisites
You MUST verify:
1. Access to `templates/prompting-principles.md` for validation rules
2. Prompt text is available (either provided or from file)

## Process

### 1. Validation Phase
You MUST verify all requirements:
- Confirm prompt_text is provided
- Load prompting principles from `templates/prompting-principles.md`
- Validate target_context if provided

### 2. Execution Phase
You MUST execute these operations:

**Load Principles:**
<!-- <principles_analysis> -->
You MUST read and apply: `templates/prompting-principles.md`
<!-- </principles_analysis> -->

**Analyze Prompt Structure:**
You WILL check for:
- Required sections (Input Parameters, Process, Success Criteria, Error Handling)
- Proper frontmatter with all required metadata
- Imperative language usage (WILL/MUST/NEVER)
- Clear separation between instructions and context
- Explicit success criteria formatted as checkboxes
- Comprehensive error handling scenarios
- Consistent heading structure and formatting
- Explicit tool usage guidance when tools are expected

**Identify Non-Compliance Issues:**
You WILL categorize issues by severity:
- **Critical**: Missing required sections, ambiguous instructions
- **Major**: Inconsistent language, missing error handling
- **Minor**: Formatting inconsistencies, unclear wording

**Generate Compliance Report:**
You WILL create a structured report with:
1. Overall compliance status (Compliant/Non-Compliant)
2. List of issues found (categorized by severity)
3. Specific recommendations for each issue
4. Rationale for each recommendation

### 3. Correction Phase (Optional)
If non-compliant and user requests correction:
- Generate corrected version preserving original intent
- Only change what improves compliance
- Highlight all changes made
- Explain rationale for each change

## Output Format
You WILL generate outputs following this structure:

**Compliance Report:**
```
# Prompt Compliance Report

## Overall Status
[Compliant/Non-Compliant]

## Critical Issues (if any)
1. [Issue description]
   - Location: [Section/line reference]
   - Recommendation: [Specific fix]
   - Rationale: [Why this matters]

## Major Issues (if any)
[Same format as critical]

## Minor Issues (if any)
[Same format as critical]

## Strengths
- [What the prompt does well]

## Summary
[Brief overall assessment]
```

**Corrected Version (if requested):**
- Full corrected prompt text
- Change log highlighting modifications
- Preservation of original functionality

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Principles loaded successfully
- Prompt analysis in progress
- Compliance check completed
- Corrected version generated (if requested)

### Completion Summary
- Total issues found by severity
- Compliance status
- Key recommendations
- Whether corrected version was generated

### Next Steps
- Review compliance report
- Decide whether to apply corrections
- Consider adopting prompt if compliant
- Use `convert-prompt-to-skill` if ready to create skill

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Preserve original intent and functionality in corrections
- Rule 2: Only flag genuine compliance issues, not style preferences
- Rule 3: Provide specific, actionable recommendations
- Rule 4: Categorize issues by severity accurately
- Rule 5: Validate against prompting principles comprehensively

## Success Criteria
You WILL consider the task complete when:
- [ ] Prompt text obtained and validated
- [ ] Prompting principles loaded from template
- [ ] Structural analysis completed
- [ ] Compliance issues identified and categorized
- [ ] Compliance report generated
- [ ] Corrected version provided (if requested and non-compliant)
- [ ] User informed of compliance status
- [ ] Next steps clearly communicated

## Required Actions
1. Load prompting principles from template file
2. Analyze prompt structure against principles
3. Identify and categorize compliance issues
4. Generate structured compliance report
5. Provide corrected version if requested

## Error Handling
You WILL handle these scenarios:
- **Missing Prompt Text**: Request prompt_text from user with clear instructions
- **Principles File Not Found**: Try alternate locations, provide error if unavailable
- **Ambiguous Context**: Ask user to clarify target_context with numbered options
- **Cannot Parse Prompt**: Report specific parsing issues and request clarification
- **Correction Not Possible**: Explain why and provide manual guidance

⚠️ **Critical Requirements**
- MANDATORY: Load and apply prompting principles from template
- NEVER modify original prompt without user approval
- ALWAYS preserve original functionality in corrections
- ALWAYS categorize issues by severity
- ALWAYS provide specific, actionable recommendations
- ALWAYS explain rationale for each compliance issue identified
