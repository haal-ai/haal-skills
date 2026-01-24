# Git Workflow Guidance

## Agent Directives

YOU MUST apply these rules when assisting with Quarkus code:

1. **Check branch before coding** — If user is on `main`/`master`/`develop`, prompt them to create a feature branch
2. **Suggest commits every ~20 min** — Brief inline reminder, not a formal section
3. **Use conventional commits** — `<type>(<scope>): <subject>`
4. **Keep commits small** — One logical change per commit

Only mention worktrees if the user asks or has issues with parallel work.

---

## Reference: Git Practices

### Pre-Coding Setup

Before starting any coding work:
- Work in a Git worktree to isolate changes (optional but recommended)
- Create or switch to a feature/fix branch (never code directly on `main`, `master`, or `develop`)

### Why Worktree?

- Keeps your main working directory clean.
- Allows parallel work on multiple features/fixes.
- Easy to discard failed experiments.
- Enables quick context switching without stashing.

### Worktree Setup Steps

```bash
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

### Branch Verification

Before coding, verify current branch:

```bash
git status -sb
```

If on `main`, `master`, or `develop`, create a feature branch:

```bash
git checkout -b feature/<issue-id>-<short-description>
```

### Worktree Cleanup

```bash
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
✅ "Add User entity with Panache"
✅ "Implement UserRepository with custom queries"
✅ "Add UserResource REST endpoints"
✅ "Add integration tests for UserResource"
✅ "Fix null handling in UserService.findById()"
```

### Bad Commit Examples

```
❌ "WIP"
❌ "Fix stuff"
❌ "Add User entity, repository, service, resource, and tests"
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
feat(user): add email validation to CreateUserRequest

Implement RFC 5322 compliant email validation using Bean Validation.
Includes integration tests for validation errors.

Closes #123
```

```
fix(order): handle null customer in OrderService

Previously, a null customer caused NullPointerException.
Now returns Optional.empty() with proper logging.
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
fix/456-null-pointer-order-service
refactor/extract-email-service
```

## 6. Pre-Commit Checklist

Before each commit, verify:

- [ ] `./mvnw compile` succeeds
- [ ] `./mvnw test` passes
- [ ] Code follows project conventions
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
   ├── Verify (compile, test)
   ├── Commit with descriptive message
   └── Repeat

3. COMPLETE
   ├── Push branch
   ├── Create PR/MR
   └── Clean up worktree after merge
```

## 8. Emergency Procedures

### Undo Last Commit (keep changes)

```bash
git reset --soft HEAD~1
```

### Discard All Uncommitted Changes

```bash
git checkout -- .
git clean -fd
```

### Fix Last Commit Message

```bash
git commit --amend -m "New message"
```

### Add Forgotten File to Last Commit

```bash
git add ForgottenFile.java
git commit --amend --no-edit
```
