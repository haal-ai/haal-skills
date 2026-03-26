# review-skill-quality

## Overview
Review and improve existing skills to ensure they follow template standards, have proper structure, and consistent formatting.

## Purpose
Maintain quality and consistency across the skill catalog by reviewing skill files against established template standards. Identifies issues, proposes improvements, and applies fixes after approval.

## Key Features
- Checks frontmatter (name, description, license, metadata)
- Validates input parameters and user interaction sections
- Reviews process structure and content completeness
- Assesses formatting consistency
- Severity-based findings (critical, warning, info)
- Applies improvements after user approval

## Usage
Invoke this skill by saying:
- "Review the quality of the email-assistant skill"
- "Check if my skill follows the template"
- "Improve the generate-pptx skill quality"

## Parameters

### Required
- **skill_name**: Name of the skill to review (must exist in `skills/[skill_name]/`)

## Process Flow
1. **Validation** — Verify skill exists at `skills/[skill_name]/`
2. **Frontmatter Check** — Validate YAML frontmatter fields
3. **Structure Review** — Check sections against template
4. **Content Assessment** — Evaluate quality of descriptions, parameters, process
5. **Formatting Check** — Verify markdown formatting consistency
6. **Findings Report** — Present issues with severity levels
7. **User Approval** — Get confirmation before applying changes
8. **Apply Improvements** — Update the skill file

## Output
- Quality report with findings categorized by severity
- Improved skill file (after approval)

## Related Skills
- **create-standard**: Quality standards for codebases
- **test-skill**: Test fixture for validation
