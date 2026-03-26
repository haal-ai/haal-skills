# create-discussion: Step-by-Step Tutorial

**How to Create a GitHub Discussion from Your IDE**

This tutorial walks you through creating a well-structured GitHub Discussion directly from your development environment.

## Prerequisites

- gh CLI installed and authenticated (`gh auth status`)
- Discussions enabled in the target repository
- Network access to github.com

## Estimated Time

2-5 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Say: "create a discussion" or:
- "open a GitHub discussion about X"
- "ask a question on discussions"
- "propose a solution for Y"

### Step 2: Provide Your Topic

**AI Asks:** What would you like to discuss?

**You Provide:**
```
I want to propose adding a CI pipeline for automated testing
```

### Step 3: Type Detection

**What AI Does:**
- Analyzes keywords in your request
- Detects type: Q&A (questions, help) or Proposal (propose, suggest, add)

**You Should See:**
```
Detected type: Proposal
Title: "Add CI pipeline for automated testing"
```

### Step 4: Duplicate Check

**What AI Does:**
- Searches existing discussions for similar topics
- Reports any matches found

**You Should See:**
```
Searching for similar discussions...
No duplicates found. Proceeding with creation.
```

### Step 5: Preview and Approve

**AI Shows:** Draft of the discussion with title and body

**User Options:**
1. **Approve**: Type "yes" to create
2. **Edit**: Request changes to title or body
3. **Cancel**: Abort creation

### Step 6: Discussion Created

**You Should See:**
```
✓ Discussion created successfully
URL: https://github.com/owner/repo/discussions/42
```

## Troubleshooting

**Issue: "gh CLI not found"**
- Install gh: https://cli.github.com/
- Run `gh auth login` to authenticate

**Issue: "Discussions not enabled"**
- Enable Discussions in repository Settings > Features
- Or use `generate-documented-issue` as an alternative

**Issue: "Duplicate found"**
- Review the existing discussion
- Decide whether to proceed or comment on the existing one

## Verification Checklist

- ✅ gh CLI authenticated
- ✅ Discussions enabled in repository
- ✅ No duplicates found
- ✅ Discussion created with URL returned
