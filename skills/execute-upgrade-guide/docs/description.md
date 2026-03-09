# execute-upgrade-guide

## What It Does

Consumes an upgrade guide produced by `generate-upgrade-guide` and executes it step-by-step with safety gates, version applicability checks, and progress tracking. Before any modification, it validates that the target is at the expected starting version.

## When To Use

- When you have an upgrade guide (from `generate-upgrade-guide`) and want to apply it to a target repository
- When you need a controlled, auditable upgrade process with rollback support
- When an LLM or human needs to execute a versioned upgrade with verification at each step

## Key Features

- **Version applicability check**: Detects the target's current version (git tags, package.json, pom.xml, pyproject.toml, etc.) and validates it matches the guide's expected start version
- **Safety-first execution**: Every step requires explicit user confirmation before running
- **Progress tracking**: Maintains a progress file with step status, timestamps, and notes
- **Pre-upgrade checkpoint**: Creates a git stash or backup branch before any modifications
- **Dry-run mode**: Preview all steps without executing anything
- **Resume support**: Resume from a specific step if execution was interrupted
- **Rollback support**: Built-in rollback to pre-upgrade state at any point
- **Post-upgrade verification**: Runs verification steps and reports pass/fail

## Components

| Component | Purpose |
|-----------|---------|
| `skill.md` | Main skill definition and LLM execution instructions |
| `tools/check_version_applicability.py` | Python script to detect current version and check applicability |

## Workflow

```
generate-upgrade-guide        execute-upgrade-guide
┌──────────────────┐         ┌──────────────────────┐
│ start_tag        │         │ Load guide            │
│ end_tag          │────────▶│ Check applicability   │
│ → upgrade guide  │  guide  │ Create checkpoint     │
└──────────────────┘  .md    │ Execute steps (1..N)  │
                             │ Verify post-upgrade   │
                             │ Finalize & report     │
                             └──────────────────────┘
```

## Version Detection Methods

The applicability check script tries these strategies in order:

1. Git tag exact match on HEAD
2. Git describe (closest tag)
3. `package.json` (Node.js)
4. `pom.xml` (Java/Maven)
5. `pyproject.toml` (Python)
6. `setup.py` (Python legacy)
7. `VERSION` / `version.txt` files
8. `build.gradle` / `build.gradle.kts` (Gradle)

## Applicability Results

| Recommendation | Meaning |
|---------------|---------|
| `PROCEED` | Version matches — safe to upgrade |
| `ALREADY_UPGRADED` | Target is already at end version |
| `UPGRADE_TO_START_FIRST` | Target is at an earlier version |
| `NOT_APPLICABLE_PAST_TARGET` | Target is past the end version |
| `PARTIAL_UPGRADE_REVIEW` | Target is between start and end — possible partial upgrade |
| `MANUAL_CHECK_REQUIRED` | Could not detect version — manual confirmation needed |

## Prerequisites

- Python 3.9+ for the applicability check script
- Git installed and repository accessible
- An upgrade guide file produced by `generate-upgrade-guide`
