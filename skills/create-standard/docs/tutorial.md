# create-standard

> Step-by-step tutorial for creating a new coding standard

## Prerequisites
- A codebase or project context where the standard applies
- Clear idea of what convention you want to standardize

## Estimated Time
5–15 minutes (depending on standard complexity)

## Step-by-Step Instructions

### Step 1: Invoke the Skill
Tell your AI assistant you want to create a standard:
> "Create a standard for error handling in our Go services"

### Step 2: Answer Clarification Questions
The skill asks 1-5 focused questions to understand your intent:
- Which files or services does this apply to?
- What framework or language?
- Are there existing patterns to follow?

Answer concisely — the skill needs just enough to start drafting.

### Step 3: Review the Draft
A markdown draft is created in `.olaf/data/practices/standards/_drafts/`. Review:
- Standard title and description
- Scope (glob patterns)
- Each rule (action verb, max 25 words)
- Good/Bad code examples

You can edit the draft file directly or request changes.

### Step 4: Approve the Standard
Confirm the draft is ready. The standard moves from `_drafts/` to the final location.

### Step 5: Choose Deployment Targets
Select which AI tools should receive the standard:
- Claude (`.claude/rules/standards/`)
- Cursor (`.cursor/rules/standards/`)
- Copilot (`.github/instructions/`)
- Windsurf (`.windsurf/rules/standards/`)
- All of the above
- None (keep in OLAF only)

### Step 6: Verify Deployment
Check that files were created in the selected tool directories.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Standard too broad | Split into multiple focused standards |
| Rules are vague | Rewrite with action verbs and specific constraints |
| Wrong scope patterns | Edit the `## Scope` section with correct globs |
| Tool file not created | Re-run deployment step for that tool |

## Verification Checklist
- [ ] Standard has a clear title and description
- [ ] Scope patterns match intended files
- [ ] Each rule starts with an action verb
- [ ] Code examples are realistic and correct
- [ ] Standard saved in `.olaf/data/practices/standards/`
- [ ] Deployed to selected AI tools
