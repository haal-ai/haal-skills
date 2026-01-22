# Runner Execution Templates (Legacy Filename)

## Overview

Standard templates for expressing how tasks should be executed in an implementation plan.

NOTE:
- This file keeps its historical name for back-compat.
- The content is runner-agnostic and does not assume any specific execution framework or toolchain.

---

## Basic Execution Notes Structure

Use this structure in each task section:

```markdown
**Execution Notes**:
- Inputs: {minimal inputs}
- Steps: {what to do}
- Outputs: {what files/changes should exist after}
- Verification: {how to validate success}
```

---

## Execution Modes (Conceptual)

- **Manual**: human executes each task and checks off success criteria.
- **Runner-assisted**: a separate tool/agent runs tasks sequentially and updates a checklist.
- **Automated**: runner proceeds without extra human intervention; stops on failure.

---

## Template 1: Phase 0 Setup Tasks

### Task 0.0: Extract Task Contexts
```markdown
**Execution Notes**:
- Use `${task_context_extractor_prompt}` (or equivalent) to generate condensed per-task context.
- Inputs should include `bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md` and `deliverable_root=${deliverable_root}`.
```

### Task 0.1: Create Skill Structure
```markdown
**Execution Notes**:
- Create the minimal directory/file structure required by the design/spec.
- For `deliverable_kind=skill`, this may include `skill.md` and a `tasks/` tree.
```

### Task 0.2: Create Master Coordinator
```markdown
**Execution Notes**:
- Create the entrypoint/coordinator only if required by the deliverable.
```

---

## Template 2: Layer Implementation Tasks

### General Layer Task Pattern
```markdown
**Execution Notes**:
- Implement the component(s) described in the task.
- Ensure outputs are produced under the deliverable root.
- Validate against success criteria.
```

### With Context File (Post Task 0.0)
```markdown
**Execution Notes**:
- Load condensed context from `tasks/contexts/task-${task_id}-context.md` (if generated) to avoid re-loading the full plan.
```

---

## Template 3: Runner Execution

### Full Execution
```markdown
Runner inputs (conceptual):
- `plan_file=${output_dir}/IMPLEMENTATION-TASK-PLAN.md`
- `checklist_path=.olaf/work/project-tasks/task-checklist.md`
- `mode=auto`
```

### Resume from Specific Task
```markdown
Runner inputs (conceptual):
- `plan_file=${output_dir}/IMPLEMENTATION-TASK-PLAN.md`
- `checklist_path=.olaf/work/project-tasks/task-checklist.md`
- `start_from_task=2.1`
```

---

## Template 4: Optional Prompt/Task Generator

**Usage**: If your execution environment supports it, you can generate per-task prompts/instructions dynamically.

Runner inputs (conceptual):
- `task_id=${task_id}`
- `context_file=${deliverable_root}/tasks/contexts/task-${task_id}-context.md` (if generated)
- `deliverable_root=${deliverable_root}`

---

## Context Variable Patterns

### Common Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `skill_path` | Path to skill being built | `competencies/onboard-me` |
| `skill_name` | Name of skill | `onboard-me` |
| `output_dir` | Output directory | `.olaf/work/staging/esdi/20251122-repo-scanner` |
| `task_id` | Task identifier | `1.1`, `2.3` |
| `layer_num` | Layer number | `1`, `2`, `3` |
| `input_file` | Input artifact path | `${output_dir}/design.md` |
| `bootstrap_doc` | Implementation plan path | `${output_dir}/IMPLEMENTATION-TASK-PLAN.md` |
| `checklist_path` | Task tracking file | `.olaf/work/project-tasks/task-checklist.md` |

### Phase-Specific Variables

#### Phase 0 (Setup)
```
skill_name=onboard-me
target_path=competencies/onboard-me
layers=5
pattern=sequential
```

#### Phase 1+ (Layer Implementation)
```
skill_path=competencies/onboard-me
layer_number=1
input_file=.olaf/data/product/repo-name/design.md
```

#### Bootstrap Orchestrator
```
bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md
checklist_path=.olaf/work/project-tasks/task-checklist.md
start_from_task=1.1  # Optional
```

---

## Variable Interpolation Rules

Variable interpolation is runner-specific.

Guideline:
- Prefer explicit, fully qualified paths in execution notes when possible.
- When variables are used, define them once (e.g., `deliverable_root`, `plan_file`, `checklist_path`) and reuse consistently.

---

## Multi-Line Commands

If your runner is a CLI, keep commands readable:
- Use multi-line formatting supported by your shell (PowerShell backtick, Bash backslash).
- Keep inputs (`plan_file`, `deliverable_root`) explicit.

---

## Timeout Configuration

Timeouts are runner-specific.

Guideline:
- Treat context-extraction (Task 0.0) and test runs as potentially long-running.
- Use conservative defaults and allow task-level overrides.

---

## Error Handling

Runner guidance:
- Default behavior: stop on first failure.
- Record failure details in the checklist/progress file.
- Provide a resume mechanism via `start_from_task`.

---

## Quick Reference

Use these canonical inputs when describing runner execution:
- `plan_file`: path to IMPLEMENTATION-TASK-PLAN.md
- `checklist_path`: where progress is tracked
- `start_from_task`: optional resume marker
