# generate-documented-issue

> Step-by-step tutorial for creating documented GitHub Issues

## Prerequisites
- GitHub CLI (`gh`) installed and authenticated
- Git repository with a GitHub remote

## Estimated Time
5–10 minutes

## Step-by-Step Instructions

### Step 1: Verify Setup
The skill automatically checks:
- `gh --version` is available
- `gh auth status` confirms authentication

If not set up, install from https://cli.github.com/ and run `gh auth login`.

### Step 2: Describe the Issue
> "Create an issue: the authentication middleware bypasses rate limiting for admin users"

Provide as much context as possible — the more detail, the better the issue.

### Step 3: Duplicate Detection
The skill searches existing:
- **Open issues** for similar titles/descriptions
- **Pull requests** that may already address the problem
- **Discussions** with related topics

If duplicates are found, you'll be shown matches and asked whether to proceed.

### Step 4: Impact Analysis
The skill scans the codebase to identify files and components likely affected by the issue. This information is included in the issue body.

### Step 5: Review the Draft
A preview of the issue is shown:
- Title
- Description with context
- Impact analysis (affected files)
- Acceptance criteria
- Labels (if any)

Request changes or approve.

### Step 6: Create the Issue
The skill runs `gh issue create` and provides the issue URL.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `gh: command not found` | Install GitHub CLI from https://cli.github.com/ |
| Authentication failed | Run `gh auth login` and follow prompts |
| Wrong repository detected | Specify the repo explicitly |
| Duplicate found | Review the match and decide to proceed or reference existing |

## Verification Checklist
- [ ] gh CLI installed and authenticated
- [ ] Repository correctly identified
- [ ] Duplicate check completed
- [ ] Impact analysis included
- [ ] Acceptance criteria are clear and testable
- [ ] Issue created successfully (URL provided)
