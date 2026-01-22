# Tutorial: Generate JSDoc Documentation

This tutorial walks you through using the `generate-jsdoc` skill to add comprehensive inline JSDoc comments to your JavaScript and TypeScript codebase.

## Prerequisites

- OLAF framework loaded
- AWS credentials configured for Bedrock
- Git repository initialized (recommended)
- Source code committed (recommended)

## Tutorial Steps

### Step 1: Prepare Your Repository

**IMPORTANT**: Before running JSDoc generation, ensure your current work is committed.

```bash
# Check current status
git status

# If you have uncommitted changes, commit them
git add .
git commit -m "feat: current work before JSDoc generation"
```

**Why?** The skill will create a new branch automatically, but it's safer to have a clean working directory first.

### Step 2: Invoke the Skill (Basic)

Simply invoke OLAF with the generate jsdoc command:

```
User: "olaf generate jsdoc"
```

**What happens:**
1. OLAF validates the repository exists
2. Determines output mode: `in-place` (default)
3. Creates git branch: `docs-jsdoc-gen-20251125-143022`
4. Displays execution plan with warnings
5. Spawns background process
6. Returns control to you immediately

**Expected Output:**
```
════════════════════════════════════════════════════════════════════════════════
JSDOC INLINE DOCUMENTATION GENERATION (Spawn Mode)
════════════════════════════════════════════════════════════════════════════════
Repository:     c:\Users\you\project
Output Mode:    in-place
Git Branch:     docs-jsdoc-gen-20251125-143022 (auto-created)
Mode:           Asynchronous (you can continue working)
════════════════════════════════════════════════════════════════════════════════

⚠️  CRITICAL WARNINGS:
  ⚠️  IN-PLACE MODE: Source files will be MODIFIED directly!
  ⚠️  Git branch creation is ENABLED by default for safety

🚀 JSDoc generation started in background!

Process ID: abc-123-xyz
Status: running
Log: .jsdoc-generation.log

Estimated time: 10-30 minutes
```

### Step 3: Continue Working

You can **continue working** while JSDoc generation runs in the background:

- Edit other files
- Run tests
- Code review
- Any other VS Code activities

The process runs independently at LOW priority to minimize impact.

### Step 4: Monitor Progress (Optional)

**Check current status:**
```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py
```

**Monitor real-time progress:**
```bash
# Windows
Get-Content .jsdoc-generation.log -Tail 20 -Wait

# Unix/Linux
tail -f .jsdoc-generation.log
```

### Step 5: Review Changes

When the process completes, review the changes:

```bash
# See what files were modified
git status

# Review actual changes
git diff

# Or review specific files
git diff src/services/myService.ts
```

**What to look for:**
- JSDoc comments added above functions/classes
- Comprehensive @param descriptions
- Detailed @returns documentation
- @throws for error cases
- @example with code samples

### Step 6: Commit or Discard

**Option A: Commit the changes**

If you're satisfied with the JSDoc comments:

```bash
git add .
git commit -m "docs: add comprehensive JSDoc comments to all source files"

# Optionally merge back to main
git checkout main
git merge docs-jsdoc-gen-20251125-143022
```

**Option B: Discard the changes**

If you're not satisfied:

```bash
# Discard all changes
git checkout .

# Return to main branch
git checkout main

# Delete the JSDoc branch
git branch -D docs-jsdoc-gen-20251125-143022
```

## Advanced Scenarios

### Scenario 1: Generate JSDoc for Specific Subfolder

```
User: "olaf generate jsdoc for src/services"
```

This processes only the `src/services` subfolder instead of the entire repository.

### Scenario 2: Preview Mode (Copy to Folder)

```
User: "olaf generate jsdoc to c:\temp\jsdoc-preview"
```

**Benefits:**
- Original files untouched
- Review output before applying to source
- Compare side-by-side

**Workflow:**
1. Generated files saved to `c:\temp\jsdoc-preview`
2. Review the documented files
3. If satisfied, copy desired files back to repository
4. Commit manually

### Scenario 3: Skip Git Branch (⚠️ Advanced Users Only)

```
User: "olaf generate jsdoc --no-branch"
```

**⚠️ WARNING**: This modifies files on your current branch without creating a safety branch.

**Only use this if:**
- You have uncommitted changes you want to preserve on current branch
- You're working on a feature branch already
- You understand the risk and want direct modification

## Common Issues and Solutions

### Issue 1: "Not a git repository"

**Solution**: Initialize git first
```bash
git init
git add .
git commit -m "Initial commit before JSDoc"
```

### Issue 2: Process seems stuck

**Check status:**
```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py
```

**Check log file:**
```bash
Get-Content .jsdoc-generation.log -Tail 50
```

### Issue 3: Want to interrupt process

**Press Ctrl+C in the terminal where process is running**

The process supports resume, so you can restart later:
```
User: "olaf generate jsdoc"
# It will resume from last processed file
```

## Tips and Best Practices

1. **Always commit first**: Have a clean working directory before starting
2. **Use git branches**: Let the skill create the branch automatically (default)
3. **Review changes**: Don't blindly commit - review the JSDoc additions
4. **Start small**: Test on a small subfolder first
5. **Monitor progress**: Check logs periodically for large codebases
6. **Plan for time**: Large codebases can take 30-60 minutes

## Next Steps

After completing this tutorial, you can:

- Generate JSDoc for different parts of your codebase
- Customize JSDoc styles by editing source files after generation
- Generate external documentation with the `generate-external-docs` skill
- Integrate JSDoc into your CI/CD pipeline

## Related Skills

- `generate-external-docs`: Generate MkDocs external documentation
- `propose-commit-thread`: Create structured commit messages for JSDoc changes
