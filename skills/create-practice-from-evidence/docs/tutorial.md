# create-practice-from-evidence: Step-by-Step Tutorial

**How to Capture Engineering Practices from Real Code Evidence**

This tutorial guides you through creating a formalized good/bad practice document from actual code or commits.

## Prerequisites

- A file or commit that demonstrates the practice
- Knowledge of which domain and use case applies

## Estimated Time

5-10 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Say: "create a practice from this file" or:
- "capture this as a good practice"
- "document this bad pattern from commit abc123"

### Step 2: Provide Evidence

**AI Asks:** What is the evidence source?

**Options:**
- **File**: Provide a file path containing the pattern
- **Commit**: Provide a git SHA showing the change
- **Comment**: Paste or describe the pattern directly

### Step 3: Describe the Practice

**AI Asks:** What practice does this evidence demonstrate?

**You Provide:**
```
Always wrap Go errors with context using fmt.Errorf
```

### Step 4: Select Domain and Scope

**AI Asks:** Domain, use case, language, and deployment scope.

**Example Answers:**
```
Domain: code-fix
Use case: feature PR
Language: go
Scope: per-repo
```

### Step 5: Review Draft

**AI Shows:** Complete practice document with:
- Description and why it matters
- Good example (what to do)
- Bad example (what to avoid)
- Evidence reference

**User Options:**
1. **Approve**: Proceed to save and deploy
2. **Edit**: Request changes
3. **Cancel**: Abort

### Step 6: Deploy to Tools

**AI Asks:** Which tools should receive this practice?

**Options:** Claude, Cursor, Copilot, Windsurf (or all)

### Step 7: Confirmation

**You Should See:**
```
✓ Saved: .olaf/data/practices/good-bad/go-wrap-errors-with-context.md
✓ Deployed to: Claude, Copilot, Cursor
```

## Troubleshooting

**Issue: "File not found"**
- Verify the file path is correct and relative to the repo root

**Issue: "Commit SHA not found"**
- Ensure the commit exists in the current branch history

## Verification Checklist

- ✅ Practice file saved in `.olaf/data/practices/good-bad/`
- ✅ Good and bad examples included
- ✅ Deployed to selected AI tool directories
