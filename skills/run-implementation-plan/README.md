# Run Implementation Plan

Runs a reviewed `IMPLEMENTATION-TASK-PLAN.md` sequentially and tracks progress in a checklist.

## When to use

- You already generated an implementation plan (e.g., with `generate-implementation-plan`).
- You want a repeatable way to execute tasks one-by-one with resume support.
- You do **not** want the plan to assume a specific execution framework.

## Inputs

- `plan_file` (required)
- `checklist_path` (optional)
- `start_from_task` (optional)

## Outputs

- A checklist markdown file that tracks completion.
