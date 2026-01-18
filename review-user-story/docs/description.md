# review-user-story

## Overview

The `review-user-story` skill reviews user stories against a standard template to ensure quality, clarity, and completeness. It provides systematic evaluation using INVEST principles and generates actionable feedback for improvement.

## Purpose

This skill helps product owners, business analysts, and development teams ensure their user stories meet quality standards before development begins. By evaluating stories against established criteria, it identifies gaps, ambiguities, and areas for improvement early in the process.

## Key Features

- **Template-Based Evaluation**: Reviews stories against a comprehensive checklist template
- **INVEST Principles Assessment**: Evaluates Independent, Negotiable, Valuable, Estimable, Small, and Testable criteria
- **Acceptance Criteria Validation**: Ensures acceptance criteria are testable and complete
- **Structured Feedback**: Generates organized reports with strengths, improvements, and clarifying questions
- **Configurable Depth**: Supports basic, thorough, or comprehensive review levels

## Usage

Invoke the skill with the following parameters:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `user_story_content` | string | Yes | - | The user story text to be reviewed |
| `template_reference` | string | No | user-story-review-template.md | Specific template for evaluation |
| `review_depth` | string | No | thorough | Depth level: basic, thorough, or comprehensive |
| `output_filename` | string | No | auto-generated | Custom filename for the output review |

## Process Flow

1. **Validation Phase**: Confirms user story content is provided and template is accessible
2. **Load User Story**: Parses and structures story components for analysis
3. **Load Evaluation Template**: Reads evaluation criteria from template file
4. **Analyze Against Template**: Evaluates story against each requirement systematically
5. **Generate Structured Review**: Creates markdown-formatted review with findings
6. **Output Phase**: Saves review to staging directory with timestamp

## Output

The skill generates a comprehensive review report containing:

- **Checklist Table**: Pass/Fail/NA status with detailed comments for each item
- **Review Summary**: Overall assessment based on checklist results
- **Strengths**: Specific positive elements identified in the user story
- **Areas for Improvement**: Concrete suggestions with examples
- **Clarifying Questions**: Specific questions to help improve the story

Reports are saved to: `.olaf/work/staging/user-story-reviews/user-story-review-[YYYYMMDD-HHmm].md`

## Examples

**Basic review**:
```
Review this user story:
As a customer, I want to reset my password so that I can regain access to my account.
```

**Thorough review with custom output**:
```
Review this user story with comprehensive depth:
[user story content]
Save as: password-reset-story-review.md
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| No user story provided | Requests user to provide the story content |
| Empty/invalid content | Informs user that valid content is required |
| Template access issues | Provides manual checklist structure as fallback |
| Unclear story structure | Notes structural issues and asks clarifying questions |
| Missing story elements | Identifies missing components and suggests additions |

## Related Skills

- `analyze-business-requirements` - For broader requirements analysis
- `review-prd-spec` - For reviewing product requirement documents
