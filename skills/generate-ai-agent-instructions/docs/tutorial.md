# generate-ai-agent-instructions

> Step-by-step tutorial for generating AI agent instruction files

## Prerequisites
- A codebase with established patterns and conventions
- Understanding of which AI tools your team uses

## Estimated Time
5–15 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill
> "Generate AI agent instructions for this project"

Or target a specific platform:
> "Create .cursorrules for this codebase"

### Step 2: Platform Selection
If not specified, the skill auto-detects your platform by checking for existing config files:
- `.github/copilot-instructions.md` → Copilot
- `.cursorrules` → Cursor
- `.windsurfrules` → Windsurf
- `.kiro/steering/` → Kiro

You can override: "Target Copilot instructions"

### Step 3: Codebase Analysis
The skill scans your project for:
- Architecture patterns (monorepo, microservices, etc.)
- Tech stack and frameworks
- Naming conventions
- Testing patterns
- Error handling approaches
- File organization

### Step 4: Review Proposed Output
A summary of the analysis and proposed instruction content is presented. Review for:
- Accuracy of detected conventions
- Completeness of key patterns
- Appropriate level of detail

### Step 5: Merge Decision (if applicable)
If existing instruction files are found, choose whether to:
- **Merge**: Combine new analysis with existing content
- **Replace**: Overwrite with fresh analysis

### Step 6: Approve and Generate
Confirm to create the instruction files.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Wrong platform detected | Specify the platform explicitly |
| Missing conventions | Point the skill to specific example files |
| Too verbose output | Request a more concise version |
| Merge conflicts | Review merged content and edit manually |

## Verification Checklist
- [ ] Platform correctly identified
- [ ] Codebase patterns accurately captured
- [ ] Instruction file created in correct location
- [ ] Content is actionable and specific (not generic)
- [ ] Existing instructions preserved (if merge selected)
