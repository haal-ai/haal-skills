---
name: generate-documented-issue
description: Create a highly documented GitHub Issue for the current repository. Performs duplicate detection across issues/PRs/discussions, analyzes the codebase to identify likely impacted files, and produces clear acceptance criteria without prescribing a single solution.
compatibility: Requires gh CLI installed and authenticated.
allowed-tools: Bash(gh:*) Bash(git:*) Bash(where:*) Bash(which:*)
metadata:
  author: olaf
  version: "1.0"
---

# Generate Documented GitHub Issue

You MUST follow these steps in order. Do NOT skip any step.

## Step 1: Verify gh CLI is installed

Run:
```
gh --version
```

If gh is NOT installed, stop and instruct the user to install it from https://cli.github.com/ and then continue.

## Step 2: Verify gh CLI is authenticated

Run:
```
gh auth status
```

**If NOT authenticated**, instruct the user:

> **You need to authenticate with GitHub.**
>
> 1. If you have a `GITHUB_TOKEN` environment variable set, clear it first (gh may prefer it over keyring auth, and an invalid token will break all gh commands):
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

## Step 3: Identify the repository

Run:
```
gh repo view --json nameWithOwner,defaultBranchRef -q '{repo: .nameWithOwner, defaultBranch: .defaultBranchRef.name}'
```

Store:
- `REPO` as `Owner/repo`
- `DEFAULT_BRANCH` as the default branch name

If this fails, ask the user to navigate to the correct repository directory.

## Step 4: Collect the issue intent and evidence

Ask the user for the minimum set of inputs:
- **Title**
- **Problem statement** (1-3 sentences)
- **Impact** (who/what is affected)

Then request any of these if relevant (do not force all of them):
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Logs / stack trace / screenshots**
- **Environment** (OS, runtime, versions)
- **Constraints** (time, backward compatibility, rollout)

If the user provides an error message, file path, symbol name, or endpoint name, store it as `KEYWORDS` for later analysis.

## Step 5: Duplicate detection (MUST DO before drafting)

Use the title keywords and any key terms from the problem statement.

### 5a. Search issues (open + closed)

Run:
```
gh search issues --repo "REPO" --state open --limit 10 "TITLE_KEYWORDS"
gh search issues --repo "REPO" --state closed --limit 10 "TITLE_KEYWORDS"
```

### 5b. Search pull requests (open + closed)

Run:
```
gh search prs --repo "REPO" --state open --limit 10 "TITLE_KEYWORDS"
gh search prs --repo "REPO" --state closed --limit 10 "TITLE_KEYWORDS"
```

### 5c. Search discussions (if enabled on the repo)

Try:
```
gh search discussions --repo "REPO" --limit 10 "TITLE_KEYWORDS"
```

If this command is not supported or fails, continue without discussions search.

### 5d. Decision gate

If any potentially related **issue**, **PR**, or **discussion** is found, present them to the user and ask what to do next:

- **Option A**: Link to the existing item and stop
- **Option B**: Continue and create a new issue that references the existing item(s)

Do NOT proceed to creation without an explicit user decision.

## Step 6: Codebase impact analysis (best-effort)

Goal: identify *likely impacted files/areas* and provide actionable starting points.

### 6a. Identify entry points

If the user provided keywords (error messages, symbols, endpoints, file paths), search the repository.

Run one or more of:
```
git grep -n "KEYWORD"
```

If the user provided multiple keywords, repeat for each one.

### 6b. Recent change correlation (optional)

If the issue seems like a regression, ask for a rough timeframe (e.g. "since last week").

Run:
```
git log --oneline -n 30
```

If the repo uses conventional commits or has obvious references, capture relevant commit IDs as possible pointers.

### 6c. Impacted files list

From the grep/log results, produce a short ordered list:
- **Primary suspects** (direct matches)
- **Secondary suspects** (neighbors/owners/modules)

If no matches are found, say so and ask the user for one extra signal:
- a stack trace line
- a URL/endpoint
- a config key
- the feature name

## Step 7: Draft the documented issue (template)

Draft a GitHub issue body with this structure:

- **Summary**
- **Problem statement**
- **Impact**
- **Context / environment**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Evidence** (logs, screenshots, links)
- **Likely impacted areas**
  - List files/modules discovered in Step 6
- **Acceptance criteria**
  - Criteria must be testable and unambiguous
- **Non-goals**
- **Open questions / unknowns**
- **Potential approaches (non-prescriptive)**
  - Provide 2-4 hypotheses/options, clearly labeled as suggestions
- **References**
  - Related issues/PRs/discussions found in Step 5

Do NOT claim certainty about root cause unless the evidence supports it.

## Step 8: Preview and confirm

Show the user:
- Title
- Repository
- The full issue body
- Any suggested labels (if applicable)

Ask:
> Create this issue? (yes/no)

Do NOT create without explicit approval.

## Step 9: Create the issue

Create using gh:
```
gh issue create --repo "REPO" --title "TITLE" --body "BODY"
```

If the user requested labels/assignees, add them using the appropriate `gh` flags.

## Error handling

- If `gh` commands fail due to permissions, explain that the user needs write access or to fork and file issues in the upstream repo.
- If search results are too broad, ask the user for 1-2 more specific keywords and retry Step 5.
