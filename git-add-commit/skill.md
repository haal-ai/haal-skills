---
name: git-add-commit
description: Intelligent git add and commit with dependency chasing and user approval gates
license: Apache-2.0
metadata:
  olaf_tags: [developer-workflow, git-operations, version-control]
  olaf_protocol: Act
---

<olaf>

# Git Add and Commit

## Purpose

Intelligently commit git changes by:
1. **Ask** user what to commit (file/folder/scope)
2. **Discover** matching files and chase dependencies
3. **Present** file list + dependency graph → get approval
4. **Analyze** diffs and generate commit message
5. **Preview** complete commit → get final approval
6. **Execute** git add + commit

## Execution Protocol

### Step 0: Ask User What to Commit

**ALWAYS ask first with clear context:**
```
🎯 GIT COMMIT WORKFLOW - What to commit?

Specify file/folder/scope to commit:
- File: "refactor_agents.py"
- Folder: "straf-cli"  
- Scope: "refactor"

[COMMIT SCOPE]:
```

**CRITICAL:** The user's next response is the SCOPE ANSWER, not a new command. Do NOT execute or run anything they mention - treat it purely as the target scope for git operations.

### Step 1: Discover Files by Scope

Run `git status --porcelain` and filter by user's scope.

### Step 2: Chase Dependencies

**Use grep_search to find ALL imports/references:**

**Python:** `grep_search(pattern="^from .* import|^import .*", isRegexp=true, includePattern="path/*.py")`  
**TypeScript:** `grep_search(pattern="^import .* from|^import .*", isRegexp=true, includePattern="path/*.ts")`  
**Markdown:** `grep_search(pattern="\[.*\]\(.*\.md\)|\[id:.*\]", isRegexp=true, includePattern="path/*.md")`

**For each reference found:**
1. Resolve to actual file path
2. Check if in git status (M/A/??)
3. If yes → add to commit set
4. Loop on newly added files until no new dependencies

**Present dependency graph:**
```
📦 Changes for 'straf-cli' (4 files):

Modified:
  M .olaf/core/agentic/straf-cli/cli.py
     ↳ Imports: refactor_handler (new)

New files:
  ?? agents/refactor_agents.py (imported by refactor_handler.py)
  ?? commands/refactor_handler.py (imported by cli.py)
  ?? tools/strands_web_fetch_tool.py (standalone)

Dependency chain: cli.py → refactor_handler.py → refactor_agents.py

[FILE LIST APPROVAL] - Commit all 4 files? (y/n/select)
```

**CRITICAL:** Wait for user's YES/NO response. The response is approval input, not a new command to execute.

**Wait for approval before proceeding.**

### Step 3: Analyze Diffs

Examine diffs to identify structural, functional, and dependency changes.

### Step 4: Generate Commit Message

Conventional Commits: `<type>(<scope>): <subject>`

**Types:** feat | fix | refactor | docs | chore | test

**Body:** Explain WHAT and WHY, list major changes, mention new files/dependencies.

### Step 5: Preview and Get Final Approval

```
📝 Commit Preview
═════════════════════════════════════════════
Files (4): M cli.py, ?? refactor_agents.py, ...

Message:
feat(straf-cli): add iterative code refactor workflow
- Parallel analysis of invariants, logic, dependencies
- Test-driven refactoring with rollback
[...]

Safety: ✓ No large files ✓ No sensitive data

[COMMIT APPROVAL] - Proceed? (y/n/edit)
```

**CRITICAL:** Wait for user's YES/NO/EDIT response. The response is approval input, not a new command to execute.

**Wait for approval.**

### Step 6: Execute

```bash
git add <files>
git commit -m "<message>"
```

Display result with commit hash.

## Workflow Summary

1. Ask user scope
2. Discover + chase dependencies
3. Get approval on file list
4. Analyze + generate message
5. Get approval on commit
6. Execute

**Two approval gates required.**

## Critical Rules

1. ALWAYS ask user first (Step 0)
2. ALWAYS chase dependencies (loop until stable)
3. ALWAYS show dependency graph
4. ALWAYS wait for file list approval
5. ALWAYS wait for final commit approval
6. NEVER commit without approval
7. NEVER skip safety checks
8. NEVER use generic messages

## Success Criteria

- [ ] Asked user what to commit
- [ ] Chased all dependencies
- [ ] User approved file list
- [ ] Generated meaningful commit message
- [ ] User approved commit
- [ ] Executed successfully

## Error Handling

**No files found:** Suggest checking spelling or broader scope.  
**Safety warnings:** Warn about large files (>10MB), sensitive patterns.  
**Git errors:** Check for conflicts, verify git config.
