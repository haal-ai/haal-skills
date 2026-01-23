# augment-code-unit-test

## Overview

The `augment-code-unit-test` skill iteratively improves unit test coverage by analyzing code complexity and enhancing tests for the most complex modules. It uses a scope-driven, tests-pass-first methodology to systematically identify and fill testing gaps.

## Purpose

This skill enables developers to:
- Systematically improve test coverage for specific code scopes
- Identify missing or weak tests through code analysis
- Add meaningful tests that cover error paths and edge cases
- Track progress across multiple sessions with persistent tasklists

## Key Features

- **Scope-Driven Analysis**: Focus on specific files or directories
- **Tests-Pass-First**: Ensures existing tests pass before adding new ones
- **Session Management**: Resume, restart, or start new augmentation sessions
- **Persistent Tasklists**: Track progress in Markdown checklists
- **User Approval Required**: User approval required for all test changes
- **Universal Standards**: Applies coding standards in Evolution/Refactoring Mode

## Usage

Invoke this skill when you need to improve test coverage for a codebase.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `core_dir` | string | Yes | Directory containing the codebase to analyze |
| `scope_path` | string | Yes | File or folder path relative to `core_dir` |
| `staging_dir` | string | No | Directory for session artifacts (default: `<repo_root>/.olaf/work/staging`) |
| `test_command` | string | No | Explicit test command (auto-detected if omitted) |

### Example Invocation

```
Skill: augment-code-unit-test
Parameters:
  - core_dir: "./my-project"
  - scope_path: "internal/syncer"
  - test_command: "go test ./internal/syncer/..."
```

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                   SESSION DISCOVERY                              │
│  • Scan for existing sessions in staging_dir                     │
│  • Present in-progress and completed sessions                    │
│  • Allow resume, restart, or new session                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   VALIDATION PHASE                               │
│  • Verify core_dir and scope_path exist                          │
│  • Resolve tasklist path                                         │
│  • Load or create tasklist                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   TASKLIST PHASE                                 │
│  • Load existing tasklist or create new one                      │
│  • Determine next unchecked task                                 │
│  • Update Last-run timestamp                                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              ENSURE TESTS PASS (First Priority)                  │
│  • Run test command for scope                                    │
│  • Fix failing tests if any                                      │
│  • Mark task complete when green                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              IDENTIFY MISSING/WEAK TESTS                         │
│  • Analyze code in scope                                         │
│  • Detect uncovered error paths                                  │
│  • Find complex branches without tests                           │
│  • Update tasklist with findings                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ADD MISSING TESTS                              │
│  • Propose concrete test cases                                   │
│  • Get user approval                                             │
│  • Implement approved tests                                      │
│  • Re-run tests and verify                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ITERATION AUTHORIZATION                        │
│  • Present results                                               │
│  • Recommend next action                                         │
│  • Request authorization to continue                             │
└─────────────────────────────────────────────────────────────────┘
```

## Output

### Tasklist File

Located at `[staging_dir]/unittest/<scope_path>/tasklist.md`:

```markdown
# Unit test improvement – internal/syncer

Session:
- Status: in-progress
- Scope: internal/syncer
- Last-run: 20260115-1430

- [x] Ensure tests pass for scope `internal/syncer`
  - [x] Run tests for the scope
  - [x] Fix failing tests (if any)
- [ ] Identify missing or weak tests in `internal/syncer`
  - [ ] Analyze branches and error paths
  - [ ] Analyze edge cases and boundary conditions
- [ ] Add missing tests for `internal/syncer`
  - [ ] Implement agreed new tests
  - [ ] Re-run tests for safety
```

### Progress Updates

- Current scope and active task
- Test pass/fail status
- Summary of tests added or fixed
- Coverage snapshot when available
- Path to tasklist file

## Examples

### Example 1: Starting New Session

**Input:**
```
core_dir: "./backend"
scope_path: "pkg/auth"
```

**Output:** New tasklist created, tests run for scope, gaps identified, and test proposals presented for approval.

### Example 2: Resuming Existing Session

**Input:**
```
core_dir: "./backend"
scope_path: "pkg/auth"
```

**Output:** Existing session detected, user prompted to resume or restart, continues from last unchecked task.

### Example 3: Directory Scope Analysis

**Input:**
```
core_dir: "./services"
scope_path: "internal"
```

**Output:** All modules under `internal/` enumerated, test file presence detected per module, comprehensive tasklist generated.

## Domain-Specific Rules

| Rule | Description |
|------|-------------|
| Scope-First | All actions constrained to user-provided scope |
| Tests-Pass-First | Never add new tests until existing tests pass |
| Tasklist as Truth | Markdown tasklist is single source of workflow progress |
| Test Quality | Focus on meaningful tests, not trivial ones |
| Minimal Changes | Prefer small, incremental changes with tests passing between steps |
| Worktree Required | Must run in dedicated Git worktree for the scope |

## Error Handling

| Scenario | Handling |
|----------|----------|
| Tasklist corruption | Back up and recreate minimal valid checklist |
| Test execution failure | Capture output, propose minimal fixes |
| Permission errors | Report exact path and required permissions |
| Scope resolution errors | Stop and ask user to correct path |

## Related Skills

- `code-in-go` - For Go coding assistance with test generation
- `code-in-rust` - For Rust coding assistance with test generation
- `review-code` - For code review tasks
