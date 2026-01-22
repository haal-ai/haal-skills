# code-in-rust

## Overview

The `code-in-rust` skill assists developers coding in Rust by enforcing team practices, SOLID principles, and Git workflow standards. It provides structured coding assistance while ensuring all generated code follows established guidelines, Rust idioms, and best practices.

## Purpose

This skill enables developers to receive Rust coding assistance that:
- Enforces universal coding standards (SOLID, DI, complexity limits)
- Follows Rust-specific idioms and conventions
- Maintains proper Git workflow with worktrees and small commits
- Generates or updates unit tests for every code change

## Key Features

- **Practice Enforcement**: Loads and applies team coding standards before any assistance
- **Worktree Verification**: Ensures isolated development environment before code changes
- **Branch Protection**: Prevents direct commits to main/master/develop branches
- **Impact Analysis**: Analyzes changes before implementation
- **Test Generation**: Creates unit tests for all code changes
- **Commit Guidance**: Suggests appropriate commit messages and timing
- **Safe Code Focus**: Requires justification for unsafe code blocks

## Usage

Invoke this skill when you need assistance with Rust development tasks.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `reference` | string | No | Work item reference (Jira ticket, GitHub issue, PR URL) |
| `task_description` | string | Conditional | What to implement or fix (required if no reference) |
| `working_directory` | string | No | Path to Rust project (defaults to current workspace) |

### Example Invocation

```
Skill: code-in-rust
Parameters:
  - reference: "PROJ-123"
  - task_description: "Implement async file reader with error handling"
  - working_directory: "./crates/io"
```

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                  PRACTICES LOADING PHASE                         │
│  • Load universal-coding-standards.md                            │
│  • Load rust-coding-guidance.md                                  │
│  • Load git-workflow-guidance.md                                 │
│  • Confirm practices loaded                                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              WORKTREE + BRANCH VERIFICATION                      │
│  • Check git worktree status                                     │
│  • Guide worktree creation if needed                             │
│  • Verify not on protected branch                                │
│  • Guide branch creation if needed                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                 REQUIREMENTS INTAKE PHASE                        │
│  • Retrieve ticket/issue content if reference provided           │
│  • Confirm scope and acceptance criteria                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│            IMPACT ANALYSIS + SOLUTION PROPOSAL                   │
│  • Analyze files/modules impacted                                │
│  • Propose step-by-step solution using SRP and DI                │
│  • Create test plan                                              │
│  • Request explicit agreement                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  IMPLEMENTATION PHASE                            │
│  • Generate code following all practices                         │
│  • Apply SOLID principles                                        │
│  • Keep functions under 30 lines                                 │
│  • Use Result<_, _> for error handling                           │
│  • Generate/update unit tests                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  COMMIT GUIDANCE PHASE                           │
│  • Remind about commit timing                                    │
│  • Suggest commit message                                        │
│  • Provide commit checklist (build, test, fmt, clippy)           │
└─────────────────────────────────────────────────────────────────┘
```

## Output

The skill provides structured assistance in this format:

```markdown
## Practices Applied
[List of enforced practices]

## Requirements
[Reference/ticket summary or user requirements]

## Impact Analysis
[What will change and where]

## Proposed Solution
[Overview + implementation steps]

## Confirmation
[Explicit proceed question]

## Implementation
[Code following all practices]

## Commit Suggestion
[Suggested commit message]

## Next Steps
[What to do next]
```

## Examples

### Example 1: Implementing Error Handling

**Input:**
```
task_description: "Add custom error types for database operations"
```

**Output:** Implementation with custom error enum, `thiserror` derive macros, context propagation using `anyhow::Context`, and corresponding unit tests.

### Example 2: Adding Async Functionality

**Input:**
```
reference: "PROJ-456"
task_description: "Implement async HTTP client wrapper"
```

**Output:** Impact analysis, async implementation with trait-based dependency injection, comprehensive tests, and commit guidance.

## Domain-Specific Rules

| Rule | Description |
|------|-------------|
| Result Handling | Never generate code that ignores `Result` errors |
| Error Context | Always add context to errors at boundaries |
| Dependency Injection | Always apply DI via traits for external dependencies |
| Test Coverage | Always generate/update unit tests for changes |
| Commit Frequency | Remind about commits after significant changes |
| Worktree Verification | Verify worktree setup before modifications |
| Branch Verification | Verify new branch before modifications |
| Function Size | Keep functions under 30 lines |
| Complexity | Keep cyclomatic complexity under 10 |
| Safe Code | Prefer safe code; require justification for `unsafe` |

## Error Handling

| Scenario | Handling |
|----------|----------|
| Practice file not found | Notify user and list missing files; offer to create them |
| Git not available | Warn that Git workflow guidance cannot be enforced |
| User rejects practice | Document deviation, explain risks, proceed if user insists |
| Complex requirement | Break down into smaller, practice-compliant increments |

## Related Skills

- `code-in-go` - Similar assistance for Go development
- `review-code` - For code review tasks
- `augment-code-unit-test` - For improving test coverage
