# run-implementation-plan

## Overview

The `run-implementation-plan` skill is an orchestrator that executes implementation plans task-by-task with progress tracking and resume capabilities. It provides a framework-agnostic approach to systematically work through implementation tasks defined in markdown files.

## Purpose

This skill enables developers and AI agents to:
- Execute implementation plans sequentially with clear progress tracking
- Resume execution from any specific task after interruptions
- Maintain a checklist of completed and pending tasks
- Support both manual (human+agent) and automated execution workflows

## Key Features

- **Sequential Task Execution**: Processes tasks one-by-one in defined order
- **Progress Tracking**: Maintains a checklist file with timestamps and completion status
- **Resume Capability**: Start from any task ID to continue interrupted work
- **Failure Handling**: Configurable stop-on-failure or continue-with-logging behavior
- **Carry-Over Support**: Optional session handoff files for context preservation
- **Framework Agnostic**: Works with any automation or manual workflow

## Usage

Invoke the skill with the following parameters:

| Parameter | Required | Description |
|-----------|----------|-------------|
| `plan_file` | Yes | Path to the implementation plan markdown file |
| `deliverable_root` | No | Root directory for outputs (inferred from plan if omitted) |
| `checklist_path` | No | Progress tracking file (default: `.olaf/work/project-tasks/implementation-plan-checklist.md`) |
| `start_from_task` | No | Resume marker like `2.1` or `3.4` |
| `stop_on_failure` | No | Stop execution on task failure (default: true) |
| `carry_over` | No | Create carry-over files after each task (default: false) |
| `carry_over_dir` | No | Directory for carry-over files (default: `.olaf/work/carry-overs/`) |

## Parameters

### plan_file (Required)
Path to the implementation plan markdown file containing tasks to execute. The plan should have tasks discoverable via headings like `### Task 1.1: ...`.

### deliverable_root (Optional)
Root directory where outputs should be created or modified. If omitted, the skill infers this from the plan's `Target:` header.

### checklist_path (Optional)
Path to the progress tracking file. Defaults to `.olaf/work/project-tasks/implementation-plan-checklist.md`.

### start_from_task (Optional)
Task ID to resume from (e.g., `2.1`, `3.4`). Useful for continuing interrupted executions.

### stop_on_failure (Optional)
Boolean flag controlling failure behavior. When `true` (default), execution stops on first failure. When `false`, failures are logged and execution continues.

### carry_over (Optional)
When `true`, creates a carry-over file after each completed task containing context for session handoffs.

### carry_over_dir (Optional)
Directory for carry-over files. Defaults to `.olaf/work/carry-overs/`.

## Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    Load and Validate Plan                    │
│  • Open plan file                                           │
│  • Identify deliverable root, phases, and tasks             │
│  • Validate task structure (artifact, outputs, criteria)    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Establish Progress Tracking                 │
│  • Create checklist file if not exists                      │
│  • Parse existing checklist for completed tasks             │
│  • Identify next pending task                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Determine Starting Task                    │
│  • Use start_from_task if provided                          │
│  • Otherwise, use next unchecked task from checklist        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Execute Tasks Sequentially                  │
│  For each task:                                             │
│  • Propose: Restate objective, outputs, success criteria    │
│  • Act: Perform task (code changes, file edits, tests)      │
│  • Update: Mark complete in checklist with timestamp        │
│  • Handle failures based on stop_on_failure setting         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Optional: Carry-Over                      │
│  • Write carry-over file with task context                  │
│  • Include files changed and next task ID                   │
└─────────────────────────────────────────────────────────────┘
```

## Output

The skill produces:
- **Execution Report**: Which tasks ran and their status
- **Updated Checklist**: Progress tracking file with completion timestamps
- **Artifacts List**: Files created or modified during execution
- **Next Task**: Identification of the next task to run
- **Blockers**: Any issues preventing further progress

## Examples

### Basic Execution
```
Execute run-implementation-plan with:
  plan_file: ./IMPLEMENTATION-TASK-PLAN.md
```

### Resume from Specific Task
```
Execute run-implementation-plan with:
  plan_file: ./IMPLEMENTATION-TASK-PLAN.md
  start_from_task: 3.2
```

### Full Configuration
```
Execute run-implementation-plan with:
  plan_file: ./IMPLEMENTATION-TASK-PLAN.md
  deliverable_root: ./src
  checklist_path: ./progress/checklist.md
  stop_on_failure: false
  carry_over: true
  carry_over_dir: ./handoffs/
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Plan file not found | Reports error with file path |
| Invalid task format | Proposes normalization patch before proceeding |
| Task execution failure | Stops or logs based on `stop_on_failure` setting |
| Missing checklist | Creates new checklist from template |

## Related Skills

- `generate-implementation-plan` - Creates implementation plans that this skill executes
- `carry-over-session` - Manages session handoff files
- `generate-design` - Creates design documents that inform implementation plans
