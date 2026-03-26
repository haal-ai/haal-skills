# review-skill-quality

> Step-by-step tutorial for reviewing and improving skill quality

## Prerequisites
- An existing skill in the `skills/` directory to review

## Estimated Time
5–10 minutes

## Step-by-Step Instructions

### Step 1: Specify the Skill
> "Review the quality of the email-assistant skill"

### Step 2: Validation
The skill verifies that `skills/[skill_name]/` exists and contains a `skill.md` file.

### Step 3: Review Findings
The skill checks against template standards and presents findings:

**Critical** — Must fix:
- Missing required frontmatter fields
- No input parameters section
- Missing process steps

**Warning** — Should fix:
- Missing code examples
- Incomplete parameter descriptions
- Inconsistent formatting

**Info** — Nice to fix:
- Style improvements
- Additional documentation opportunities

### Step 4: Review Proposed Changes
Each proposed change is shown with:
- What will change
- Why it's needed
- Before/after preview

### Step 5: Approve Changes
Confirm which changes to apply. You can approve all, some, or none.

### Step 6: Verify Results
Open the updated skill file to confirm improvements.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Skill not found | Check the skill name matches the directory name |
| Too many findings | Focus on critical issues first |
| Changes break the skill | Revert and apply changes one at a time |

## Verification Checklist
- [ ] Skill exists and was found
- [ ] Frontmatter validated
- [ ] Structure matches template
- [ ] Findings reviewed
- [ ] Approved changes applied
- [ ] Updated skill still works correctly
