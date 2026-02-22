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

## Step 3: Identify the repository and get its ID

Run:
```
gh repo view --json nameWithOwner,id -q '{owner: .nameWithOwner, id: .id}'
```

Store `nameWithOwner` as `REPO` (e.g. `Owner/repo-name`) and `id` as `REPO_ID` (e.g. `R_kgDO...`). Both are needed later.

Extract `OWNER` and `REPO_NAME` by splitting `REPO` on `/`.

If this fails, ask the user to navigate to the correct repository directory.

## Step 4: Ask the user what type of discussion to create

Present this choice to the user:

> **What type of discussion do you want to create?**
>
> 1. **Q&A** — Ask a question, report a problem, or request help
> 2. **Proposal** — Share a solution, tip, or workflow you found valuable

Wait for the user's selection.

## Step 5: Collect discussion content

### If Q&A:

Ask the user to provide:
1. **Title** — short summary of the question/problem
2. **Problem** — one-sentence description of the issue or question
3. **Context** — tool/plugin/model used, OS, language (only what's relevant)
4. **What I tried** — brief list of what was already attempted

### If Proposal:

Ask the user to provide:
1. **Title** — short summary of the solution
2. **Solution** — one-sentence summary of what was built or discovered
3. **Benefits** — why this is useful, what problem it solves
4. **Where to find it** — path in the repo, link to code/docs, or contribution folder

## Step 6: Search for similar existing discussions

Use the GraphQL API to fetch recent discussions and look for similar ones:
```
gh api graphql -f query='{
  repository(owner: "OWNER", name: "REPO_NAME") {
    discussions(first: 20, orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes { number title url category { name } }
    }
  }
}' --jq '.data.repository.discussions.nodes[] | "#\(.number) [\(.category.name)] \(.title) - \(.url)"'
```

Replace `OWNER` and `REPO_NAME` with the values from Step 3.

Compare the returned titles against the user's title and problem/solution keywords.

Also search for related **issues** and **pull requests** (open and closed). Use the user's title keywords as the query.

Issues:
```
gh search issues --repo "OWNER/REPO_NAME" --state open --limit 10 "TITLE_KEYWORDS"
gh search issues --repo "OWNER/REPO_NAME" --state closed --limit 10 "TITLE_KEYWORDS"
```

Pull requests:
```
gh search prs --repo "OWNER/REPO_NAME" --state open --limit 10 "TITLE_KEYWORDS"
gh search prs --repo "OWNER/REPO_NAME" --state closed --limit 10 "TITLE_KEYWORDS"
```

Replace `OWNER/REPO_NAME` with the repository from Step 3.

If any potentially related **discussions**, **issues**, or **pull requests** are found (open or closed), present them to the user and ask what to do next:

> **I found existing items that might already address this:**
>
> - Discussion #... — ...
> - Issue #... — ...
> - PR #... — ...
>
> **Do you still want to create a new discussion, or would you rather contribute to an existing item?**

If the user chooses an existing item, provide the link and stop.

**If similar discussions are found**, present them to the user:

> **I found these existing discussions that might be related:**
>
> - #123 — Title of discussion 1
> - #456 — Title of discussion 2
>
> **Do you still want to create a new discussion, or would you rather contribute to an existing one?**

If the user wants to contribute to an existing one, provide the link and stop.

If the user wants to proceed, continue to Step 7.

**If no similar discussions are found**, inform the user and proceed to Step 7.

## Step 7: Get the discussion category

Use the GraphQL API to list discussion categories and their IDs:
```
gh api graphql -f query='{
  repository(owner: "OWNER", name: "REPO_NAME") {
    discussionCategories(first: 20) {
      nodes { id name }
    }
  }
}' --jq '.data.repository.discussionCategories.nodes[] | "\(.id) \(.name)"'
```

Replace `OWNER` and `REPO_NAME` with the values from Step 3.

Store the matching category ID as `CATEGORY_ID`. Match the user's discussion type:
- For **Q&A**: look for a category containing "Q&A", "Questions", or "Q & A"
- For **Proposal**: look for a category containing "Ideas", "Proposals", "Show and tell", or "General"

If the exact match is unclear, present the available categories and ask the user to pick one.

## Step 8: Format the discussion body

### Q&A format:
```
**Problem:** <user's problem>
**Context:** <user's context>
**What I tried:** <user's attempts>
```

### Proposal format:
```
**Solution:** <user's solution>
**Benefits:** <user's benefits>
**Where to find it:** <user's pointer>
```

## Step 9: Preview and confirm

Show the user a preview of the discussion:

> **Preview:**
>
> **Title:** <title>
> **Category:** <category>
> **Body:**
> <formatted body>
>
> **Create this discussion?** (yes/no)

Wait for user confirmation. Do NOT create without explicit approval.

## Step 10: Create the discussion

Use the GraphQL API to create the discussion:
```
gh api graphql -f query='mutation {
  createDiscussion(input: {
    repositoryId: "REPO_ID",
    categoryId: "CATEGORY_ID",
    title: "TITLE",
    body: "BODY"
  }) {
    discussion { url number }
  }
}' --jq '.data.createDiscussion.discussion | "Discussion #\(.number) created: \(.url)"'
```

Replace `REPO_ID` with the repository ID from Step 3, `CATEGORY_ID` with the category ID from Step 7, and `TITLE`/`BODY` with the formatted content from Step 8.

Escape any double quotes and newlines in `TITLE` and `BODY` before inserting them into the GraphQL query.

If the command succeeds, display the URL of the created discussion.

If it fails, show the error and suggest troubleshooting steps.

## Error Handling

- **gh not installed**: Provide installation instructions (Step 1)
- **gh not authenticated**: Provide login procedure (Step 2)
- **Not in a git repo**: Ask user to navigate to the correct directory
- **Discussion creation fails**: Show error, check permissions, suggest `gh auth refresh`
- **No matching category found**: List available categories and ask user to choose
