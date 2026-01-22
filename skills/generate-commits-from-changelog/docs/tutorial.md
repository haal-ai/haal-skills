# Tutorial: Generate Commits from Changelog

## Overview
This tutorial guides you through using the Generate Commits from Changelog skill to create meaningful Git commits from your changelog entries and repository changes.

## Prerequisites
- Git repository initialized and configured
- Changelog file with documented changes
- Staged or unstaged changes in your repository
- Understanding of conventional commit format
- Terminal access for Git operations

## Estimated Time
15-30 minutes

## Steps

### Step 1: Prepare Your Repository
Ensure your repository has changes ready to commit:
```bash
git status
```

**Expected Result**: List of modified, added, or deleted files displayed.

### Step 2: Invoke the Skill
Start the commit generation process:
```
generate commits from changelog
```

**Expected Result**: The skill begins analyzing your repository and changelog.

### Step 3: Provide Changelog Path (Optional)
If prompted, specify your changelog location:
```
Example: .olaf/data/projects/changelog-register.md
```

**Expected Result**: Changelog file is located and parsed.

### Step 4: Review Initial Analysis
The skill analyzes your repository state:
- Staged changes
- Modified files
- Added files
- Deleted files
- Untracked files

**Expected Result**: Summary of all detected changes displayed.

### Step 5: Review Changelog Mapping
The skill maps changelog entries to file changes:
```
Changelog Entry: "Added user authentication feature"
Mapped Files: src/auth/login.js, src/auth/register.js
```

**Expected Result**: Clear mapping between documentation and code changes.

### Step 6: Review Proposed Commits
Examine the generated commit plan:
```
Commit 1: feat(auth): add user authentication
  Files: src/auth/login.js, src/auth/register.js
  Changelog: Entry #42

Commit 2: fix(api): resolve timeout issue
  Files: src/api/client.js
  Changelog: Entry #43
```

**Expected Result**: Logical grouping of changes into atomic commits.

### Step 7: Choose Review Option
Select how to proceed:
```
Options:
1. Accept all commits
2. Modify individual commits
3. Regenerate messages
4. Abort operation
```

**Expected Result**: Your selection is acknowledged.

### Step 8: Approve or Modify Commits
For each commit (in interactive mode):
- Review the commit message
- Verify included files
- Approve or request changes

**Expected Result**: All commits reviewed and approved.

### Step 9: Execute Commits
After approval, commits are created:
```bash
Creating commit 1/3: feat(auth): add user authentication
Creating commit 2/3: fix(api): resolve timeout issue
Creating commit 3/3: docs: update API documentation
```

**Expected Result**: All commits successfully created.

### Step 10: Verify Results
Check your Git history:
```bash
git log --oneline -5
```

**Expected Result**: New commits visible with proper messages.

## Expected Outcomes

### Successful Completion
- All changelog entries mapped to commits
- Atomic commits with conventional format
- Clear commit messages with references
- Repository history updated

### Execution Summary
- Total commits created
- Files included per commit
- Changelog references linked
- Any warnings or skipped items

### Validation Checklist
- [ ] All staged changes committed
- [ ] Commit messages follow conventional format
- [ ] Changelog entries referenced
- [ ] No sensitive information committed
- [ ] Branch policies respected

## Troubleshooting

### Common Issues

**Issue**: "No changelog entries found"
**Solution**: Verify changelog path and ensure entries exist for the time period

**Issue**: "Merge conflict detected"
**Solution**: Resolve merge conflicts manually before running the skill

**Issue**: "Branch protection prevents commit"
**Solution**: Create a feature branch or adjust branch protection settings

**Issue**: "Untracked files not included"
**Solution**: Stage untracked files with `git add` before running

### Best Practices

1. **Review before executing**: Always review proposed commits in interactive mode
2. **Keep changelog updated**: Maintain your changelog for accurate commit mapping
3. **Use atomic commits**: Let the skill group related changes appropriately
4. **Sign important commits**: Enable commit signing for release commits
5. **Reference issues**: Include issue numbers in changelog entries

## Next Steps

After generating commits:
1. **Push changes**: Push commits to remote repository
2. **Create pull request**: If working on a feature branch
3. **Update changelog**: Mark entries as committed
4. **Tag releases**: Create version tags if applicable
5. **Notify team**: Share commit summary with team members
