---
name: review-skill-quality
description: Review and improve existing skills to ensure they follow template standards, have proper structure, and consistent formatting
license: Apache-2.0
metadata:
  olaf_tags: [skill, quality, review, improvement, standards]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response:
1. **skill_name**: string - The name of the skill to review and improve (REQUIRED)

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before modifying any files
- Present all proposed changes for review before applying
- Provide clear progress updates at each major step
- Use numbered lists when presenting options or findings

## Process

### 1. Validation Phase
You MUST verify all requirements:
- Validate skill exists at `skills/[skill_name]/`
- Confirm main skill file exists at `skills/[skill_name]/skill.md`
- Read the skill template: `skills/create-skill/templates/skill-template.md`

### 2. Analysis Phase
You WILL analyze the target skill for these quality issues:

**Frontmatter Issues:**
- Missing or incomplete metadata (olaf_tags, copyright, author, repository, provider)
- Outdated or vague description
- Presence of deprecated fields (e.g., `olaf_protocol`)

**Input Parameters Issues:**
- Not formatted as numbered list
- Missing instruction to "Present them as a numbered list to ease user response"
- Inconsistent REQUIRED/OPTIONAL labeling
- Missing type information

**User Interaction Issues:**
- References to vague external protocols ("defined externally", "Propose-Confirm-Act")
- Missing concrete interaction guidelines
- Not following the standard interaction pattern

**Structure Issues:**
- Missing required sections (User Communication, Success Criteria, Required Actions, Error Handling)
- User Communication missing subsections (Progress Updates, Completion Summary, Next Steps)
- Success Criteria not formatted as checkboxes
- Inconsistent section ordering

**Content Issues:**
- Inconsistent file naming (uppercase vs kebab-case)
- Inconsistent path references
- Missing `.olaf/` prefix where appropriate
- Vague or unclear instructions

**Formatting Issues:**
- Inconsistent use of imperative language ("You MUST", "You WILL")
- Missing bold formatting for parameter names
- Inconsistent bullet point styles

### 3. Reporting Phase
You WILL present findings to the user:
- List all issues found, grouped by category
- Indicate severity (critical, important, minor)
- Propose specific fixes for each issue
- Ask user: "Ready to apply these improvements?" (yes/no/edit)

### 4. Improvement Phase
After user approval, you WILL apply improvements:
- Update frontmatter with proper metadata
- Fix Input Parameters section formatting
- Replace vague User Interaction protocols with concrete guidelines
- Add missing sections following template structure
- Fix file naming and path inconsistencies
- Ensure consistent formatting throughout
- Preserve the skill's core functionality and intent

### 5. Final Validation Phase
You WILL validate the improved skill:
- Confirm all template sections are present
- Verify frontmatter follows standards
- Check that User Interaction is concrete and actionable
- Ensure Success Criteria uses checkboxes
- Validate file paths and naming conventions
- Confirm imperative language is used consistently

## Output Format
You WILL generate outputs following this structure:
- Updated skill file: `skills/[skill_name]/skill.md`
- Summary of changes made
- List of improvements applied

## User Communication

### Progress Updates
- Confirmation when skill is found and read
- Status when analyzing skill against template standards
- Notification when issues are identified
- Confirmation when improvements are applied

### Completion Summary
- Number of issues found and fixed
- Categories of improvements made
- Location of updated skill file
- Validation results

### Next Steps
- Skill is ready for use with improved quality
- Consider regenerating description.md if significant changes were made
- Review the updated skill to ensure functionality is preserved

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER change the core functionality or intent of the skill
- Rule 2: ALWAYS preserve existing domain-specific logic and rules
- Rule 3: ONLY fix structural, formatting, and standards compliance issues
- Rule 4: ALWAYS get user approval before modifying files
- Rule 5: If uncertain about a change, ask the user for guidance
- Rule 6: Maintain kebab-case naming for all files and references
- Rule 7: Use `.olaf/` prefix for OLAF-specific paths

## Success Criteria
You WILL consider the task complete when:
- [ ] Skill identified and analyzed
- [ ] All quality issues identified and categorized
- [ ] Findings presented to user for review
- [ ] User approval obtained
- [ ] Improvements applied to skill file
- [ ] Updated skill validated against template standards
- [ ] User notified of completion with summary

## Required Actions
1. Validate skill exists and read skill file
2. Read skill template for standards reference
3. Analyze skill for quality issues across all categories
4. Present findings and proposed fixes to user
5. Apply improvements after user approval
6. Validate updated skill meets standards
7. Provide completion summary

## Error Handling
You WILL handle these scenarios:
- **Skill Not Found**: List available skills in `skills/` and ask user to select
- **Missing Skill Name**: Request skill name from user
- **Skill File Missing**: Alert user that skill structure is incomplete
- **Template File Not Found**: Use built-in knowledge of template standards
- **User Rejection of Changes**: Ask for specific feedback on which changes to skip
- **File Write Failure**: Provide error details and suggest troubleshooting steps
- **Validation Failures**: Report specific issues and ask for user guidance

⚠️ **Critical Requirements**
- MANDATORY: Get user approval before modifying any files
- MANDATORY: Preserve the skill's core functionality and intent
- MANDATORY: Present all proposed changes before applying
- NEVER remove domain-specific logic or rules
- ALWAYS validate changes don't break the skill's purpose
- ALWAYS provide clear explanations for each improvement
