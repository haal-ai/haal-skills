# Git Workflow Guidance

This guidance defines the Git practices to follow during development sessions.

## 1. Pre-Coding Setup: Worktree + New Branch

**CRITICAL**: Before starting any coding work:
- You MUST work in a Git worktree to isolate your changes.
- You MUST create (or switch to) a new feature/fix branch (never code directly on `main`, `master`, or `develop`).

### Why Worktree?
- Keeps your main working directory clean.
- Allows parallel work on multiple features/fixes.
- Easy to discard failed experiments.
- Enables quick context switching without stashing.

### Worktree Setup Steps

```powershell
# 1. Ensure you're on the latest main/develop
git fetch origin
git checkout main
git pull origin main

# 2. Create a worktree for your feature/fix (this also creates a new branch)
git worktree add ../my-feature-worktree -b feature/my-feature

# 3. Navigate to the worktree
cd ../my-feature-worktree

# 4. Start coding in the isolated worktree
```

### Branch Rules

- You MUST verify current branch before coding:

```powershell
git status -sb
```

- If you are on `main`, `master`, or `develop`, you MUST create/switch to a feature branch before any code changes:

```powershell
git checkout -b feature/<issue-id>-<short-description>
```

### Worktree Cleanup

```powershell
# When done, merge or discard and clean up
git worktree remove ../my-feature-worktree
git branch -d feature/my-feature  # if merged
# or
git branch -D feature/my-feature  # if discarding
```

## 2. Small, Focused Commits

### Commit Principles
- **One logical change per commit**: Each commit should represent a single, coherent change.
- **Commit early, commit often**: Don't accumulate large changesets.
- **Keep commits under 200 lines changed** when possible.
- **Atomic commits**: Each commit should leave the codebase in a working state.

### Good Commit Examples
```
✅ "Add User struct with validation methods"
✅ "Implement repository interface for User"
✅ "Add unit tests for User validation"
✅ "Fix nil pointer in User.Validate()"
```

### Bad Commit Examples
```
❌ "WIP"
❌ "Fix stuff"
❌ "Add User model, repository, service, tests, and API endpoints"
❌ "Changes"
```

## 3. Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **test**: Adding or updating tests
- **docs**: Documentation only changes
- **chore**: Build process or auxiliary tool changes

### Examples

```
feat(user): add email validation to User struct

Implement RFC 5322 compliant email validation.
Includes unit tests for edge cases.

Closes #123
```

```
fix(api): handle nil response from external service

Previously, a nil response caused a panic.
Now returns a descriptive error.
```

## 4. Frequent Commit Rhythm

### During Development
1. **After each working increment**: Commit when a small piece works.
2. **Before refactoring**: Commit working code before restructuring.
3. **After refactoring**: Commit the refactored code separately.
4. **Before taking breaks**: Don't leave uncommitted work.

### Commit Frequency Guidelines
- **Minimum**: At least once per hour of active coding.
- **Ideal**: Every 15-30 minutes for small, logical changes.
- **Maximum uncommitted time**: 2 hours (then break down work further).

## 5. Branch Strategy

### Branch Naming
```
feature/<issue-id>-<short-description>
fix/<issue-id>-<short-description>
refactor/<short-description>
```

### Examples
```
feature/123-user-authentication
fix/456-null-pointer-handler
refactor/extract-validation-service
```

## 6. Pre-Commit Checklist

Before each commit, verify:
- [ ] Code compiles/builds successfully
- [ ] Tests pass
- [ ] Linter passes (if configured)
- [ ] Commit message follows format
- [ ] Changes are focused on a single concern
- [ ] No debug code or commented-out code included
- [ ] No secrets or credentials in the commit

## 7. Session Workflow Summary

```
1. SETUP
   └── Create worktree for isolated work

2. CODE LOOP
   ├── Make small, focused change
   ├── Verify (build, test, lint)
   ├── Commit with descriptive message
   └── Repeat

3. COMPLETE
   ├── Push branch
   ├── Create PR/MR
   └── Clean up worktree after merge
```

## 8. Emergency Procedures

### Undo Last Commit (keep changes)
```powershell
git reset --soft HEAD~1
```

### Discard All Uncommitted Changes
```powershell
git checkout -- .
git clean -fd
```

### Fix Last Commit Message
```powershell
git commit --amend -m "New message"
```

### Add Forgotten File to Last Commit
```powershell
git add forgotten-file.go
git commit --amend --no-edit
```
