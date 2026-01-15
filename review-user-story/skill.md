---
name: review-user-story
description: Review user story against standard template to ensure quality, clarity, and completeness
license: Apache-2.0
metadata:
  olaf_tags: [documentation, analysis, user-story, quality, review]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters

You MUST request these parameters if not provided by the user:
- **user_story_content**: string - The user story text to be reviewed (REQUIRED)
- **template_reference**: string - Optional specific template to use for evaluation (default: user-story-review-template.md)
- **review_depth**: string - Optional depth level (basic|thorough|comprehensive) (default: thorough)
- **output_filename**: string - Optional custom filename for the output review (default: auto-generated with timestamp)

## User Interaction Protocol

You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Use Act protocol for template loading and initial analysis
- Use Propose-Confirm-Act protocol for saving the final user story review

## Process

### 1. Validation Phase

You WILL verify all requirements:
- Confirm user story content is provided and not empty
- Validate access to the specified template file
- Check that the user story has basic structure (not just a title)
- Verify timestamp can be generated for output filename

### 2. Execution Phase

1. **Load User Story**:
   - Receive user story content provided by user
   - Parse and structure the story components for analysis
   - Identify existing story elements (title, description, acceptance criteria, etc.)
   - Validate that the content contains an actual user story

2. **Load Evaluation Template**:
   - Read file: `templates/user-story-review-template.md` for evaluation criteria
   - Parse the template structure to understand all evaluation categories
   - Prepare the checklist for systematic review

3. **Analyze Against Template**:
   - Evaluate user story against each template requirement systematically:
     - **Clarity & Conciseness**: Assess title and description clarity
     - **Format**: Check "As a...I want...So that..." structure
     - **Acceptance Criteria**: Evaluate testability and completeness
     - **INVEST Principles**: Review against all 6 INVEST criteria
     - **Scope & Dependencies**: Assess scope definition and dependencies
   - Document findings per template section with specific examples
   - Assign Pass/Fail/NA status to each checklist item with detailed comments

4. **Generate Structured Review**:
   - Create markdown-formatted review following the exact template structure
   - Populate all template sections with analysis results:
     - Complete the checklist table with status and comments for each item
     - Write comprehensive review summary with overall assessment
     - List specific strengths found in the user story
     - Detail areas requiring improvement with actionable suggestions
     - Generate specific clarifying questions to help improve the story
   - Include timestamp and user story identifier in the review

### 3. Output Phase

You WILL create and save the structured review:
- Format the complete review using the template structure
- Save to: `.olaf/work/staging/user-story-reviews/user-story-review-[YYYYMMDD-HHmm].md`
- Confirm successful file creation and provide file location

## Output Format

You WILL generate outputs following this structure:
- **User Story Analysis**: Complete evaluation against template checklist with Pass/Fail/NA status
- **Structured Review Report**: Complete document following `templates/user-story-review-template.md`
- **Constructive Feedback**: Specific strengths, improvement areas, and clarifying questions
- **Saved Report**: File saved to `.olaf/work/staging/user-story-reviews/user-story-review-[YYYYMMDD-HHmm].md`

### Report Generation

You MUST create the user story review using the template: `templates/user-story-review-template.md`

You WILL populate all template sections with actual analysis results:
- **Checklist Table**: Complete every row with status (Pass/Fail/NA) and detailed comments
- **Review Summary**: Overall assessment based on checklist results
- **Strengths**: Specific positive elements identified in the user story
- **Areas for Improvement**: Concrete suggestions with examples where needed
- **Clarifying Questions**: Specific questions to help improve the story

Follow template structure: `templates/user-story-review-template.md`

**Save Output**: Create file `.olaf/work/staging/user-story-reviews/user-story-review-[YYYYMMDD-HHmm].md` where:
- YYYYMMDD-HHmm is the current timestamp from background terminal command

## Output to USER

### Progress Updates
- Confirmation when user story content is successfully parsed
- Status when template is loaded and evaluation criteria are ready
- Summary of analysis results (checklist items evaluated, issues found, etc.)
- Timestamp identifier used: [YYYYMMDD-HHmm format]
- Confirmation when review is saved to `.olaf/work/staging/user-story-reviews/`

### Completion Summary
- User story reviewed: [title or identifier]
- Overall assessment: [quality rating/summary]
- Key strengths identified: [number of positive elements with examples]
- Improvement areas: [number of issues found with specific suggestions]
- Clarifying questions generated: [number of questions for user]
- Saved review location: `.olaf/work/staging/user-story-reviews/user-story-review-[YYYYMMDD-HHmm].md`

### Next Steps

You WILL clearly define:
- Priority improvements needed based on analysis
- Specific actions to address each identified issue
- Recommendations for user story refinement
- Suggestions for stakeholder validation if needed

## Domain-Specific Rules
- Rule 1: Be thorough - examine each story component carefully without making assumptions
- Rule 2: Be constructive - frame feedback helpfully and collaboratively, not critically
- Rule 3: Reference template explicitly - use standard template as basis for all evaluations
- Rule 4: Generate actionable questions - provide specific questions that help improve the story
- Rule 5: Focus on INVEST principles - ensure the story meets independent, negotiable, valuable, estimable, small, testable criteria
- Rule 6: Validate acceptance criteria - ensure they are testable and complete

## Required Actions
1. Validate that user story content is provided and contains actual story structure
2. Load and parse the user story review template for evaluation criteria
3. Systematically evaluate the user story against every template checklist item
4. Generate comprehensive review report with specific findings and recommendations
5. Save formatted review to `.olaf/work/staging/user-story-reviews/user-story-review-[YYYYMMDD-HHmm].md`
6. Provide actionable feedback and clarifying questions based on analysis

## Error Handling

You WILL handle these scenarios:
- **No User Story Provided**: Request user to provide the user story content to review
- **Empty/Invalid Content**: Inform user that valid user story content is required
- **Template Access Issues**: Provide manual checklist structure if template is unavailable
- **Unclear Story Structure**: Note structural issues in review and ask clarifying questions
- **Missing Story Elements**: Identify missing components and suggest specific additions
- **Timestamp Generation Issues**: Use fallback timestamp format if background command fails
- **File Save Issues**: Provide clear error message and suggest alternative save location

⚠️ **Critical Requirements**
- MANDATORY: User story content must be provided before starting analysis
- MANDATORY: All analysis MUST be based on actual user story content, not assumptions
- NEVER review without loading the evaluation template first
- NEVER generate Pass/Fail ratings without specific justification in comments
- ALWAYS save the final review to staging directory with timestamp
- ALWAYS provide specific examples in feedback and suggestions
- ALWAYS include actionable clarifying questions for improvement

