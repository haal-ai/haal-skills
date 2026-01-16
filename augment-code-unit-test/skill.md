---
name: augment-code-unit-test
description: Iteratively improve unit test coverage by analyzing code complexity and enhancing tests for the most complex modules
license: Apache-2.0
metadata:
  olaf_tags: [iterative, unit-testing, code-analysis, complexity, coverage]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

⚠️ **MANDATORY WORKTREE REQUIREMENT**
- You MUST run this skill inside a **dedicated Git worktree for the scope**, not in your main worktree.
- Recommended pattern: create a worktree named like `<scope>-augment-unit-test` from your primary repo, for example:
  - `git worktree add ../.olaf-core-scripts-olaf-augment-unit-test`
- All code and test changes produced by this skill MUST stay in that dedicated worktree. You can delete the worktree when the augmentation work is complete.

You MUST also load and apply the **Universal Coding Standards** in
Evolution/Refactoring Mode:
- Read `.olaf/data/practices/standards/universal-coding-standards.md`.
- Treat existing public APIs and observable behavior as **frozen**: unit
  tests MUST characterize and protect current behavior, not change it.
- Focus this skill on increasing coverage and improving test quality around
  current behavior; any proposals for API or behavior changes must be clearly
  called out and separated from the augmentation work.

## Time Retrieval\s*Get current timestamp in `YYYYMMDD-HHmm` format

## Time Retrieval
Get current timestamp in `YYYYMMDD-HHmm` format.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **core_dir**: string - Directory containing the codebase to analyze (**REQUIRED**)
- **scope_path**: string  File or folder path **relative to `core_dir`** that defines the test-improvement scope (**REQUIRED**). Examples:
  - `internal/syncer`
  - `internal/syncer/syncer.go`
- **staging_dir**: string - Directory for persisted augmentation session artifacts (OPTIONAL).
  - Default: `<repo_root>/.olaf/work/staging` where `<repo_root>` is the git/worktree root that contains `.olaf/`.
  - Tasklists are stored under: `[staging_dir]/unittest/<scope_path-as-directories>/tasklist.md`.
- **test_command**: string  Optional explicit test command for the scope. If omitted, you MUST infer a reasonable default based on the language/framework and repository
  conventions (for Go, prefer `go test ./...` or `go test ./<scope-dir>`).


## Session Discovery and Selection (User-Friendly UX)

You MUST provide a user-friendly way to reuse or restart existing unit-test augmentation sessions:

- When the user has **not** provided `scope_path` (or explicitly asks to browse existing sessions), you MUST:
  - Scan `[staging_dir]/unittest/` recursively for all `tasklist.md` files.
  - For each `tasklist.md`, read the header and checklist to determine:
    - `Scope` (from the header `Scope: <scope_path>` line).
    - `Status`:
      - `in-progress` if at least one checklist item remains unchecked (`- [ ]`).
      - `completed` if all checklist items are checked (`- [x]`).
    - `Last-run` (from the header `Last-run: <timestamp>` line, if present).
  - Present a summarized list to the user, grouping entries as:
    - **In-progress sessions**: show `scope_path` and `Last-run`.
    - **Completed sessions**.
  - Ask the user which action they prefer:
    - Resume an **in-progress** session.
    - Restart a **completed** session.
    - Start a **new** session for a new `scope_path`.
- When the user selects an existing session from this list:
  - Set `scope_path` to the corresponding scope.
  - Load its `tasklist.md` and continue using the rules in **Tasklist Creation vs. Loading** and **Tasklist Phase**.
- When the user selects **new session**:
  - Ask for `scope_path` (relative to `core_dir`) and optional `test_command`.
  - Derive `tasklist_path` and create a fresh tasklist as described below.

- When the user **has already provided** `scope_path`:
  - Skip the global session list by default (to minimize friction).
  - Go directly to the tasklist for that `scope_path`, applying the **Tasklist Creation vs. Loading** rules.
  - You MAY still summarize whether this is a new, in-progress, or completed session for clarity.

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Use **Propose-Confirm-Act** for any change that modifies tests or code.
- Use **Act** for routine, low-risk operations such as listing files,
  reading existing tests, or parsing tasklists.
- When in doubt, prefer **Propose-Confirm-Act**.

## Prerequisites & Scope Handling

This workflow is **scope-driven** and **tests-pass-first**:

1. **Scope Resolution**
   - Resolve `scope_path` against `core_dir` to determine the absolute scope.
   - Detect whether the scope is a **file** or a **directory**:
     - File scope: focus analysis and proposals on that single file and its
       tests.
     - Directory scope: include all code and tests under that directory.

2. **Tasklist Location**
   - Derive a deterministic tasklist path from the scope:
     - `tasklist_dir = [staging_dir]/unittest/<scope_path-as-directories>/`
       where `scope_path` components become subdirectories.
       - Example: `scope_path = internal/syncer` 
         `tasklist_dir = [staging_dir]/unittest/internal/syncer/`
   - The **tasklist file** is:
     - `tasklist_path = tasklist_dir + "tasklist.md"`

   **When is it created?**
   - On the first run for a given `scope_path`, during **Tasklist Phase → Load or Create Tasklist**.
   - If `tasklist_path` already exists, it is loaded and updated (e.g., `Last-run`).

3. **Tasklist Creation vs. Loading**
   - If `tasklist_path` **exists**:
     - Read it and parse the header section (title and `Session:` block) if present.
     - Derive the checklist state:
       - If at least one `- [ ]` remains, treat the session as **in-progress**.
       - If no unchecked tasks remain, treat the session as **completed**.
     - Update the `Last-run` timestamp in the header using the current time
       (see **Time Retrieval**).
     - Keep the `Status` field consistent with the checklist state:
       - `Status: in-progress` when any `- [ ]` remains.
       - `Status: completed` when all checklist items are `- [x]`.
     - For **in-progress** sessions:
       - Inform the user that a session already exists for this `scope_path`.
       - Ask whether to:
         - **Resume** from the next unchecked task (first line starting with
           `- [ ]`), or
         - **Restart** by appending a new checklist section or resetting the
           checklist while preserving previous content.
     - For **completed** sessions:
       - Ask whether to:
         - **Restart** the session for this scope (for example by appending a
           new checklist section), or
         - Leave it completed and stop for this invocation.
   - If `tasklist_path` **does not exist**:
     - Create a new Markdown tasklist with the default, tickable structure (see
       "Tasklist Format" below), including the `Session` metadata block.
     - Initialize `Status: in-progress` and set `Last-run` to the current
       timestamp.
     - Treat the first top-level task as the active one.

4. **Tests-Pass-First Gate**
   - For every scope, you MUST:
     - First ensure that **existing tests pass** for that scope.
     - Only after tests are green may you propose and add **new tests**.
   - This rule has priority over coverage metrics or hotspot-style analysis.

## Tasklist Format

The tasklist at `tasklist_path` is a human- and machine-readable Markdown file
with a tickable checklist. A recommended initial structure is:

```markdown
# Unit test improvement – <scope_path>

Session:
- Status: in-progress
- Scope: <scope_path>
- Last-run: <timestamp>

- [ ] Ensure tests pass for scope `<scope_path>`
  - [ ] Run tests for the scope
  - [ ] Fix failing tests (if any)
- [ ] Identify missing or weak tests in `<scope_path>`
  - [ ] Analyze branches and error paths
  - [ ] Analyze edge cases and boundary conditions
- [ ] Add missing tests for `<scope_path>`
  - [ ] Implement agreed new tests
  - [ ] Re-run tests for safety
```

Rules:
- You MUST preserve any existing user edits in `tasklist.md` and only append or
  tick tasks; do not delete user-authored tasks.
- You MUST use the standard Markdown checklist syntax `- [ ]` and `- [x]`.
- When completing a task, toggle exactly one `- [ ]` to `- [x]` and persist the
  change.
- You MUST keep the `Session` metadata (`Status`, `Scope`, `Last-run`) consistent
  with the checklist state and the most recent invocation as described in
  **Tasklist Creation vs. Loading**.
 - For **directory scopes**, when creating or enriching a tasklist you MUST:
   - Enumerate all immediate modules/packages under `scope_path` (for example,
     `main` and subdirectories under `internal/`).
   - Detect whether each module has at least one `*_test.<ext>` file.
   - Add or update checklist sub-items under "Identify missing or weak tests" to
     reflect module-level test presence and obvious gaps (for example,
     "`internal/syncer`: review existing tests and identify missing error-path
     coverage").
   - NEVER silently treat the scope as fully covered without recording, at
     minimum, whether each module has tests.

## Process

### 1. Validation Phase

You WILL verify all requirements **before** making any changes:

- Confirm all required parameters (`core_dir`, `scope_path`, `staging_dir`) are
  provided.
- Normalize and validate paths:
  - Ensure `core_dir` exists and is a directory.
  - Ensure `scope_abs_path = core_dir + scope_path` exists.
- Resolve `tasklist_path` as described in **Tasklist Location**.
- Determine whether `scope_path` refers to a file or directory.

### 2. Tasklist Phase

You WILL use the tasklist as the single source of truth for the workflow
status within the scope:

1. **Load or Create Tasklist**
   - If `tasklist_path` exists: read it into memory.
   - If it does not exist: create it with the default content shown above.

2. **Determine Next Task**
   - Find the **first** checklist line that starts with `- [ ]`.
   - Treat this as the **current active task**.
   - If no unchecked tasks remain, the workflow for this scope is considered
     **complete**.

3. **Respect Task Semantics**
   - If the active task relates to **tests passing** (e.g., "Ensure tests pass
     for scope"): you MUST run tests and fix failures before moving on.
   - If the active task relates to **identifying missing tests**: you MUST
     analyze code vs tests and produce a concrete list of missing/weak tests.
   - If the active task relates to **adding tests**: you MUST propose concrete
     test additions, get user approval, implement them, and re-run tests.

### 3. Execution Phase

Execution is always **tests-pass-first** within the chosen scope.

#### 3.1 Ensure Tests Pass for Scope

When the active task is to ensure tests pass:

1. **Determine Test Command**
   - If `test_command` was provided: use it as-is.
   - Otherwise, infer a reasonable default based on:
     - Language/framework of the code under `scope_path`.
     - Repository conventions (for Go modules, prefer `go test ./...` or
       `go test ./<scope-dir>`).

2. **Run Tests**
   - Execute the test command in the appropriate working directory.
   - Capture exit code and output.

3. **Interpret Results**
   - If tests **pass**:
     - Mark the relevant checklist items as completed (`- [x]`).
   - If tests **fail**:
     - Summarize the failing tests and error messages.
     - Propose a concrete, minimal set of code or test changes to fix them,
       following the universal coding standards.
     - Use **Propose-Confirm-Act** before applying any fix.
     - Re-run tests until they pass or until you reach a clearly-articulated
       blocking issue.

#### 3.2 Identify Missing or Weak Tests

Once tests pass and the tasklist indicates that the next task is about
"Identify missing or weak tests":

1. **Analyze Code in Scope**
   - Enumerate the functions, methods, and key branches under `scope_path`.
   - Enumerate the existing tests that reference those units.

2. **Detect Gaps**
   - Look for:
     - Uncovered error paths and boundary conditions.
     - Complex branches without direct tests.
     - Public APIs in scope that lack characterization tests.

3. **Update Tasklist and Communicate**
   - Summarize the missing/weak tests as sub-items under the relevant
     checklist entry in `tasklist.md`.
   - Present the same summary to the user as a proposed plan for new tests.

#### 3.3 Add Missing Tests

When the active task is to add tests for the scope:

1. **Propose Concrete Tests**
   - For each identified gap, propose one or more specific test cases with:
     - Test name.
     - Scenario/arrange conditions.
     - Expected behavior/assertions.

2. **Get User Approval (Propose-Confirm-Act)**
   - Present the proposed test additions grouped by concern (e.g., error paths,
     edge cases).
   - Wait for user approval or requested adjustments.

3. **Implement Tests**
   - Add or update test files within the scope.
   - Keep all changes minimal and focused on test behavior; do not change public
     API behavior unless explicitly requested and clearly separated.

4. **Re-run Tests and Finalize**
   - Re-run the test command.
   - If tests pass: mark the corresponding checklist items as completed.
   - If tests fail: propose and apply minimal fixes, re-running until green or
     a blocking issue is documented.

### 4. Validation Phase

You WILL validate results at the end of each invocation:

- Confirm that all changes are reflected in `tasklist.md` with accurate
  `- [x]` and `- [ ]` markers.
- Confirm that tests for the scope either:
  - Pass successfully, or
  - Have clearly documented failures and proposed fixes.
- Confirm that any added tests are meaningful (not trivial getters/setters) and
  aligned with the universal coding standards.

## User Communication

You WILL provide these updates to the user:

### Progress Updates
- Current scope (`scope_path`) and active task.
- Whether tests currently pass for the scope.
- Summary of tests added or fixed in the most recent step.
- A brief coverage snapshot when possible, for example:
  - Number of modules/packages in the scope and how many have `*_test` files.
  - If the test command or repository setup provides coverage data (such as
    `go test -cover` or a recent `coverage.out` file), summarize the available
    overall or per-package coverage numbers without running extra tools beyond
    the agreed test command unless explicitly authorized by the user.
- Path to the tasklist file:
  - `[staging_dir]/unittest/<scope_path>/tasklist.md`

### Iteration Authorization

After completing the current task, you WILL:

1. **Present Results:**
   - Describe what was done (tests run, fixes applied, tests added).
   - Show the updated state of the key checklist items.
2. **Provide Recommendation:**
   - **Continue:** e.g., "Tests now pass; next I recommend identifying missing
     tests for `<scope_path>`."
   - **Stop:** e.g., "Tests pass and planned tests are implemented; scope
     appears complete for now."
   - **Modify:** e.g., "Encountered persistent failures; recommend adjusting
     scope or revisiting implementation before adding more tests."
3. **Request Authorization:**
   - Ask explicitly whether to proceed to the next unchecked task in the
     tasklist.

### Completion Summary

When all checklist items in `tasklist.md` for a scope are checked:

- Summarize:
  - Key areas covered by tests.
  - Number or nature of tests added/updated.
  - Remaining known risks or open questions (if any).
- Confirm that the scope is considered **complete** for this workflow but
  remains open to future iterations if the user expands or edits the tasklist.

## Domain-Specific Rules

You MUST follow these constraints:

- **Scope-First:** All actions are constrained to the user-provided
  `scope_path` (file or directory) and its tests.
- **Tests-Pass-First:** Never propose or add new tests until existing tests for
  the scope pass or you have clearly identified and proposed fixes for
  failures.
- **Tasklist as Source of Truth:** The Markdown tasklist in
  `[staging_dir]/unittest/<scope_path>/tasklist.md` is the single source of
  truth for workflow progress in that scope.
- **Test Quality:** Focus on meaningful tests; do not add trivial or
  redundant tests.
- **Minimal Changes:** Prefer small, incremental changes with tests always
  passing between steps.

## Success Criteria

You WILL consider the task complete **for a given scope** when:

- [ ] All checklist items in `tasklist.md` for that scope are marked as
  completed (`- [x]`).
- [ ] Tests for the scope pass successfully using the agreed `test_command`.
- [ ] Identified missing/weak tests for the scope have been addressed or
  explicitly documented as deferred.

## Required Actions

1. Resolve `core_dir`, `scope_path`, and `staging_dir`; derive `tasklist_path`.
2. Load or create the scope-specific `tasklist.md`.
3. Determine the next unchecked task and execute it, respecting the
   tests-pass-first rule.
4. Update `tasklist.md` to reflect progress and communicate results to the
   user.
5. Ask the user whether to proceed to the next unchecked task.

## Error Handling

You WILL handle these scenarios:

- **Tasklist Corruption:** If `tasklist.md` cannot be parsed, back it up and
  recreate a minimal, valid checklist while preserving user content as a
  comment block.
- **Test Execution Failure:** Capture and summarize failure output; propose
  minimal, standards-compliant fixes; do not silently ignore failing tests.
- **Permission Errors:** If you cannot write to `tasklist.md` or test files,
  report the exact path and required permissions.
- **Scope Resolution Errors:** If `scope_path` does not exist under `core_dir`,
  stop and ask the user to correct the path.

⚠️ **Critical Requirements**
- ALWAYS respect Propose-Confirm-Act for any change to tests or production
  code.
- NEVER add new tests before confirming the current tests for the scope are
  passing or have an agreed fix plan.
- ALWAYS use the tasklist in `[staging_dir]/unittest/<scope_path>/` as the
  progress reference for the scope.


