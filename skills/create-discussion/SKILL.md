---
name: create-discussion
description: Create a GitHub Discussion (Q&A or Proposal) in the current repository following the project's discussion templates. Checks gh CLI auth, searches for duplicates, and creates the discussion. Use when user wants to ask a question, report a problem, or propose a solution.
compatibility: Requires gh CLI installed and authenticated. Designed for Claude Code or GitHub Copilot.
allowed-tools: Bash(gh:*) Bash(where:*) Bash(which:*)
metadata:
  author: Amadeus-xDLC
  version: "1.0"
---

# Create GitHub Discussion

You MUST follow these steps in order. Do NOT skip any step.

## Step 1: Verify gh CLI is installed

Run:
```
gh --version
```

**If gh is NOT installed**, stop and display this message:

> **GitHub CLI (`gh`) is required but not installed.**
>
> Install it from: **https://cli.github.com/**
>
> - **Windows:** `winget install --id GitHub.cli` or download from the link above
> - **macOS:** `brew install gh`
> - **Linux:** See https://github.com/cli/cli/blob/trunk/docs/install_linux.md
>
> After installing, proceed to Step 2.

Then STOP and wait for the user to confirm installation.

## Step 2: Verify gh CLI is authenticated

Run:
```
gh auth status
```

**If NOT authenticated**, instruct the user:

> **You need to authenticate with GitHub.**
>
> 1. If you have a `GITHUB_TOKEN` environment variable set, clear it first:
>    - **PowerShell:** `Remove-Item Env:GITHUB_TOKEN`
>    - **Bash:** `unset GITHUB_TOKEN`
> 2. Run: `gh auth login`
> 3. Select: **GitHub.com**
> 4. Preferred protocol: **HTTPS**
> 5. Authenticate Git with GitHub credentials: **Yes**
> 6. Choose: **Login with a web browser**
> 7. Copy the one-time code displayed, press Enter, and complete authentication in your browser.
>
> Once done, tell me and I'll continue.

Then STOP and wait for user confirmation.

## Step 3: Verify Discussions are enabled and identify the repository

First, check if Discussions are enabled in the repository:
```bash
gh repo view --json hasDiscussionsEnabled,nameWithOwner,id -q '{discussions: .hasDiscussionsEnabled, owner: .nameWithOwner, id: .id}'
```

If `hasDiscussionsEnabled` is `false`, show this guidance and STOP:

> **Discussions are not enabled in this repository.**
>
> Options:
> 1. **Enable Discussions** in the repository settings on GitHub, then retry.
> 2. **Create an Issue instead** with the same content (useful for proposals or questions).
> 3. **Choose another repository** that has Discussions enabled.
>
> Which option do you prefer?

If the user chooses to create an Issue, offer to run the `generate-documented-issue` skill with the same content.

If the user chooses to enable Discussions, wait for them to confirm it’s enabled, then retry Step 3.

If `hasDiscussionsEnabled` is `true`, proceed:

Store `nameWithOwner` as `REPO` (e.g. `Owner/repo-name`) and `id` as `REPO_ID` (e.g. `R_kgDO...`). Both are needed later.

Extract `OWNER` and `REPO_NAME` by splitting `REPO` on `/`.

If this fails, ask the user to navigate to the correct repository directory.

## Step 4: Auto-detect discussion type and generate content

From the user's initial request, extract:
- **Type**: If the request contains "proposal", "solution", "evolve", "improve" → Proposal; otherwise Q&A
- **Title**: Generate a concise summary from the request
- **Body**: Structure the request into the appropriate format

Only ask follow-up questions if the initial request is too vague to create a discussion.

If needed, ask for ONLY these 2 items and then continue:
1. **Discussion type** (Q&A or Proposal)
2. **One-sentence goal** (what should this discussion achieve?)

### Auto-detection logic:
- Look for keywords: "proposal", "suggest", "evolve", "improve", "enhance", "solution"
- If found → Proposal type
- Otherwise → Q&A type

### Auto-generate title:
- Extract the core topic from the user's request
- Keep it under 60 characters
- Use title case

### Auto-generate body:
For **Q&A**:
```
**Problem:** <extracted problem statement>
**Context:** <relevant context from request>
**What I tried:** <any attempts mentioned>
```

For **Proposal**:
```
**Solution:** <extracted solution statement>
**Benefits:** <why this is useful>
**Where to find it:** <any pointers mentioned>
```

Example for our current request:
- Type: Proposal
- Title: "Evolving the create-skill skill for modern models"
- Body: The proposal content we prepared earlier

## Step 5: Search for similar existing discussions

Use keywords extracted from the auto-generated title to search for similar items (lightweight duplicate check).

Use the GraphQL API to fetch recent discussions:
```bash
gh api graphql -f query='{
  repository(owner: "OWNER", name: "REPO_NAME") {
    discussions(first: 20, orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes { number title url category { name } }
    }
  }
}' --jq '.data.repository.discussions.nodes[] | "#\(.number) [\(.category.name)] \(.title) - \(.url)"'
```

Replace `OWNER` and `REPO_NAME` with the values from Step 3.

Also search for related **issues** and **pull requests** (open and closed) using keywords from the title:

Issues:
```bash
gh search issues --repo "OWNER/REPO_NAME" --state open --limit 10 "TITLE_KEYWORDS"
gh search issues --repo "OWNER/REPO_NAME" --state closed --limit 10 "TITLE_KEYWORDS"
```

Pull requests:
```bash
gh search prs --repo "OWNER/REPO_NAME" --state open --limit 10 "TITLE_KEYWORDS"
gh search prs --repo "OWNER/REPO_NAME" --state closed --limit 10 "TITLE_KEYWORDS"
```

If any potentially related items are found, present them and ask:
> **I found existing items that might already address this:**
> - Discussion #... — ...
> - Issue #... — ...
> - PR #... — ...
>
> **Do you still want to create a new discussion?** (yes/no)

If no similar items are found, proceed to Step 6.

## Step 6: Get the discussion category

Use the GraphQL API to list discussion categories and their IDs:
```bash
gh api graphql -f query='{
  repository(owner: "OWNER", name: "REPO_NAME") {
    discussionCategories(first: 20) {
      nodes { id name }
    }
  }
}' --jq '.data.repository.discussionCategories.nodes[] | "\(.id) \(.name)"'
```

Replace `OWNER` and `REPO_NAME` with the values from Step 3.

Auto-select the matching category ID as `CATEGORY_ID`:
- For **Q&A**: look for a category containing "Q&A", "Questions", or "Q & A"
- For **Proposal**: look for a category containing "Ideas", "Proposals", "Show and tell", or "General"

If no exact match is found, default to "General" if available; otherwise pick the first category.

## Step 7: Preview and confirm

Show the user a preview of the auto-generated discussion:

> **Preview:**
>
> **Title:** <auto-generated title>
> **Category:** <auto-selected category>
> **Body:**
> <auto-formatted body>
>
> **Create this discussion?** (yes/no)

Wait for user confirmation. Do NOT create without explicit approval.

## Step 8: Create the discussion

Use the GraphQL API directly (no interactive prompts). Use GraphQL variables to avoid manual escaping:
```bash
gh api graphql \
  -f query='mutation($repositoryId: ID!, $categoryId: ID!, $title: String!, $body: String!) {
    createDiscussion(input: {
      repositoryId: $repositoryId,
      categoryId: $categoryId,
      title: $title,
      body: $body
    }) {
      discussion { url number }
    }
  }' \
  -f repositoryId='REPO_ID' \
  -f categoryId='CATEGORY_ID' \
  -f title='TITLE' \
  -f body='BODY' \
  --jq '.data.createDiscussion.discussion | "Discussion #\(.number) created: \(.url)"'
```

Replace `REPO_ID` with the repository ID from Step 3, `CATEGORY_ID` with the category ID from Step 6, and `TITLE`/`BODY` with the auto-generated content from Step 4.

If the command succeeds, display the URL of the created discussion.

## Error Handling

- **gh not installed**: Provide installation instructions (Step 1)
- **gh not authenticated**: Provide login procedure (Step 2)
- **Discussions not enabled**: Provide clear options to enable Discussions or fall back to issue creation (Step 3)
- **Not in a git repo**: Ask user to navigate to the correct directory
- **Discussion creation fails**: Show error, check permissions, suggest `gh auth refresh`
- **No matching category found**: Default to first available category
