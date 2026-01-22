# Tutorial: review-user-story

## Introduction

This tutorial guides you through using the `review-user-story` skill to evaluate user stories against quality standards. By the end, you'll know how to get comprehensive feedback on your user stories and improve them before development begins.

## Prerequisites

Before starting, ensure you have:

- [ ] A user story to review (with title, description, and ideally acceptance criteria)
- [ ] Access to the review template (usually included with the skill)
- [ ] Write access to the staging directory for saving reports

## Step-by-Step Instructions

### Step 1: Prepare Your User Story

Gather the user story you want to review. A complete user story typically includes:

- **Title**: Brief identifier for the story
- **Description**: "As a [role], I want [feature], so that [benefit]"
- **Acceptance Criteria**: Testable conditions for completion

Example:
```
Title: Password Reset Feature

As a registered user, I want to reset my password via email 
so that I can regain access to my account if I forget my credentials.

Acceptance Criteria:
- User can request password reset from login page
- System sends reset link to registered email within 2 minutes
- Reset link expires after 24 hours
- User must create password meeting security requirements
```

### Step 2: Invoke the Skill

Request a review of your user story:

```
Review this user story:
[paste your user story content here]
```

Or with specific options:

```
Review this user story with comprehensive depth:
[user story content]
```

### Step 3: Wait for Validation

The skill will verify:
- User story content is provided and not empty
- Template file is accessible
- Story has basic structure (not just a title)

If validation fails, provide the requested information.

### Step 4: Review the Analysis

The skill evaluates your story against multiple criteria:

**Clarity & Conciseness**:
- Is the title clear and descriptive?
- Is the description easy to understand?

**Format**:
- Does it follow "As a...I want...So that..." structure?
- Are all three parts present and meaningful?

**Acceptance Criteria**:
- Are criteria testable?
- Are they complete and unambiguous?

**INVEST Principles**:
| Principle | Question |
|-----------|----------|
| Independent | Can this story be developed without dependencies? |
| Negotiable | Is there room for discussion on implementation? |
| Valuable | Does it deliver clear value to users? |
| Estimable | Can the team estimate the effort? |
| Small | Can it be completed in one sprint? |
| Testable | Can completion be objectively verified? |

### Step 5: Interpret the Results

The generated report includes:

1. **Checklist Table**: Each item marked Pass/Fail/NA with comments
2. **Review Summary**: Overall quality assessment
3. **Strengths**: What's working well in your story
4. **Areas for Improvement**: Specific suggestions for enhancement
5. **Clarifying Questions**: Questions to help refine the story

### Step 6: Act on Feedback

Review the improvement suggestions and clarifying questions:

1. Address any "Fail" items in the checklist
2. Answer the clarifying questions to add detail
3. Incorporate suggested improvements
4. Consider re-running the review after changes

### Step 7: Access Your Report

The review is saved to:
```
.olaf/work/staging/user-story-reviews/user-story-review-[YYYYMMDD-HHmm].md
```

Share this report with your team for discussion.

## Verification Checklist

After completing the review, verify:

- [ ] Review report was generated successfully
- [ ] All checklist items have status and comments
- [ ] Strengths are identified with specific examples
- [ ] Improvement areas have actionable suggestions
- [ ] Clarifying questions are relevant and helpful
- [ ] Report is saved to the staging directory

## Troubleshooting

### "No user story provided"

**Cause**: The skill was invoked without story content.

**Solution**: Include the full user story text in your request.

### "Invalid content structure"

**Cause**: The provided text doesn't appear to be a user story.

**Solution**: Ensure your story includes at minimum a description in user story format.

### "Template not found"

**Cause**: The evaluation template file is missing or inaccessible.

**Solution**: The skill will use a fallback checklist. Contact support if this persists.

### "Cannot save report"

**Cause**: Write permission issues with the staging directory.

**Solution**: Check directory permissions or specify an alternative output location.

## Next Steps

After reviewing your user story:

1. **Refine the Story**: Address identified issues and answer clarifying questions
2. **Re-Review if Needed**: Run another review after significant changes
3. **Share with Team**: Discuss the review findings with stakeholders
4. **Document Decisions**: Record any negotiated changes to the story
5. **Proceed to Development**: Once the story passes review, it's ready for sprint planning
