 ---
name: run-implementation-plan
description: Execute an IMPLEMENTATION-TASK-PLAN.md sequentially with progress tracking and optional resume
license: Apache-2.0
metadata:
  olaf_tags: [orchestrator, execution, implementation, progress-tracking]
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

# Run Implementation Plan (Runner / Orchestrator)

## Intent

Execute a reviewed implementation plan (typically `IMPLEMENTATION-TASK-PLAN.md`) **task-by-task**, track progress in a checklist, and support resuming from a task id.

This runner is intentionally **framework-agnostic**:
- It does NOT assume STRAF, Bedrock, or any specific agent CLI.
- It can be driven manually (human+agent) or by any automation you already use.

## User Interaction
- Summarize parsed tasks and the next task to run
- Wait for user confirmation before beginning execution
- Execute tasks sequentially, updating progress

## Input Parameters

You MUST request these parameters if not provided by the user. Present them as a numbered list:

1. **plan_file**: string - Path to the implementation plan markdown file (REQUIRED)
2. **deliverable_root**: string - Root directory where outputs should be created/modified (OPTIONAL; if omitted, infer from plan header `Target:`)
3. **checklist_path**: string - Progress tracking file path (OPTIONAL; default: `.olaf/work/project-tasks/implementation-plan-checklist.md`)
4. **start_from_task**: string - Resume marker like `2.1` or `3.4` (OPTIONAL)
5. **stop_on_failure**: boolean - Stop execution when a task fails (OPTIONAL; default: true)
6. **carry_over**: boolean - Create a carry-over file after each completed task (OPTIONAL; default: false)
7. **carry_over_dir**: string - Where to write carry-over files (OPTIONAL; default: `.olaf/work/carry-overs/`)

## Assumptions / Plan Format

The runner expects tasks to be discoverable via headings like:
- `### Task 1.1: ...`

If the plan uses a different format, you MUST propose a small normalization patch to the plan and get user approval before proceeding.

## Process

### Step 1: Load and Validate Plan

You MUST:
- Open `${plan_file}` and identify:
  - Deliverable/target root (prefer `Target:` from header)
  - Phases (e.g., `## PHASE 1:`)
  - Tasks (e.g., `### Task 1.1:`)
- Validate that tasks have, at minimum:
  - Artifact (what should be produced)
  - Outputs
  - Success criteria (how to know it's done)

### Step 2: Establish Progress Tracking

You MUST:
- Create `${checklist_path}` if it does not exist (use `templates/task-checklist-template.md` as a base).
- If it exists, parse it to find:
  - Completed tasks
  - The next pending task

### Step 3: Determine Starting Task

If `start_from_task` is provided:
- Begin from that task id (even if earlier tasks are unchecked).

Else:
- Begin from the next unchecked task in `${checklist_path}`.

### Step 4: Execute Tasks Sequentially

For each task:
- **Propose**: restate task objective + expected outputs + success criteria.
- **Act**: perform the task (code changes, file edits, tests) using tools as needed.
- **Update**: mark the task complete in `${checklist_path}` with timestamp and produced artifacts.

Failure handling:
- If `stop_on_failure=true`, STOP on first failure and propose recovery/resume instructions.
- If `stop_on_failure=false`, record failure and ask whether to continue.

### Step 5 (Optional): Carry-Over

If `carry_over=true`:
- Write a carry-over file after each completed task into `${carry_over_dir}`.
- Include:
  - Task completed
  - Files changed
  - Next task id
  - Any gotchas / context

## Output

You WILL output:
- Which task(s) ran
- Updated checklist path
- Any artifacts created/modified
- Next task to run
- Any blockers
