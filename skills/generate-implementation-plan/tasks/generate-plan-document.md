---
name: generate-plan-document
description: "Task 7 - Write final IMPLEMENTATION-TASK-PLAN.md"
task_id: 7
protocol: Act
---

# Task 7: Generate Plan Document

## Objective

Assemble all outputs from previous tasks into the final IMPLEMENTATION-TASK-PLAN.md file.

IMPORTANT:
- Treat the design/spec as the source of truth for *product deliverables*.
- Only include onboarding/bootstrap scaffolding when explicitly requested (e.g., `execution_mode=bootstrap`).

## Context Variables

**Required**:
- `requirements_map`: From Task 1
- `design_layers`: From Task 1
- `task_zero_spec`: From Task 2
- `task_breakdown`: From Task 3
- `traceability_matrix`: From Task 4
- `coverage_report`: From Task 4
- `task_execution_info`: From Task 5
- `bootstrap_command`: From Task 6 (may be empty when omitted)
- `output_file`: Path to write IMPLEMENTATION-TASK-PLAN.md
- `specification_file`: Original Phase 2 specification path
- `design_file`: Original Phase 3 design path

**Optional**:
- `deliverable_kind`: `tool|skill|library`
- `deliverable_root`: Root folder for product deliverables
- `execution_mode`: `manual|bootstrap`
- `include_task_context_extraction`: `true|false`
- `include_bootstrap`: `true|false`
- `skill_path`: Back-compat alias when `deliverable_kind=skill`

**Outputs**:
- ${output_file}: Complete implementation plan

## Execution Steps

### Step 1: Load Template

Use template from `templates/implementation-plan-template.md`

### Step 2: Populate Header

```markdown
# {Skill Name} Implementation Task Plan

**Version**: 1.0  
**Date**: {current_date}  
**Execution**: Sequential via a plan runner (human or agent)  
**Target**: {deliverable_root}

---
```

### Step 3: Add Overview Section

```markdown
## Overview

{Extract from design.md introduction}

**Final Outcome**: Product artifacts described in the design/spec implemented under {deliverable_root}.

**Requirement Coverage**: {coverage_percentage}% ({covered_count}/{total_requirements} requirements addressed)

**Deliverable Directory Structure** (must match design/spec):
```
{deliverable_root}/
├── {design-derived files and folders}
└── ...
```

If `execution_mode=bootstrap`, add a separate "Optional Execution Scaffolding" subsection and clearly label it as non-product scaffolding.

---
```

### Step 4: Add Execution Strategy

```markdown
## Execution Strategy

This plan is designed to be executed sequentially, one task at a time.

Execution options:
- **Manual**: a human (or IDE agent) follows each task section and produces the specified outputs.
- **Runner-assisted**: a separate "plan runner" orchestrates tasks, captures/loads per-task context, and updates a checklist.

If `execution_mode=bootstrap`, include prompt generation + Task 0.0 prerequisites.

If `execution_mode=manual`, omit onboarding/Task 0.0 references and instead describe how a human (or agent) should execute the tasks directly.

---
```

### Step 4.5: Add Requirement Traceability Matrix

```markdown
## Requirement Traceability Matrix

{Insert traceability_matrix from Task 3}

**Coverage Summary**:
{Insert coverage_report from Task 3}

---
```

### Step 5: Add Phase 0 Tasks

```markdown
## PHASE 0: Setup & Structure Creation

{Insert task_zero_spec from Task 1}

{Insert Task 0.1 spec from task_breakdown}

{Insert Task 0.2 spec from task_breakdown}

---
```

### Step 6: Add Layer Phases

For each phase in task_breakdown (Phase 1 through N):

```markdown
## PHASE {layer_id}: Layer {layer_id} - {layer_name}

{Layer description from design_layers}

{For each task in phase:}
  ### Task {task_id}: {task_name}
  
  **Artifact**: {task_artifact}
  **Execution Time**: {estimated_time}
  **Execution Notes**: {task_execution_info[task_id]}
  
  **Task Details**:
  {task_details from task_breakdown}
  
  **Reuse**:
  {reuse_references from task_breakdown}
  
  **Outputs**:
  {task_outputs from task_breakdown}
  
  **Dependencies**: {task_dependencies}
  **Success Criteria**:
  {success_criteria from task_breakdown}
  
  ---

{Next task}

---
```

### Step 7: Add Bootstrap Execution Section

```markdown
## Bootstrap Execution

{Insert bootstrap instructions from Task 6}

{Insert bootstrap_command from Task 6}

{Insert resume command pattern from Task 6}

---
```

### Step 8: Add Summary Sections

```markdown
## Summary

**Total Phases**: {total_phases}  
**Total Tasks**: {total_tasks}  
**Estimated Time**: {estimated_total_time} minutes (~{hours} hours)

**Execution Order**:
1. Phase 0 (Setup) - 3 tasks
2. Phase 1 ({layer_1_name}) - {layer_1_tasks} tasks
3. Phase 2 ({layer_2_name}) - {layer_2_tasks} tasks
...
N. Phase {N} ({layer_N_name}) - {layer_N_tasks} tasks

**Critical Dependencies**:
- Task 0.0 → ALL tasks (context extraction)
- Task 0.1 → Task 0.2 (structure before coordinator)
- Phase N → Phase N+1 (sequential layer implementation)

---

## Prerequisites

Before starting execution:

1. ✅ **Plan reviewed and approved**
2. ✅ **Workspace ready** (tooling installed, repo cloned, env configured as required by the design)
3. ✅ **Progress tracking available** (a checklist file if using a runner)
   - Version: Latest
   
3. ✅ **Design document available**
   - Path: {design_file}
   - Validated and approved
   
4. ⚠️ **Task 0.0 executed manually FIRST**
   - Generates context files in {skill_path}/tasks/contexts/
   - Required for universal prompt generator

---

## Success Criteria

Upon completion of ALL tasks:

✅ Product deliverables implemented under `{deliverable_root}`
✅ Any required entrypoints implemented (only if design/spec requires)
✅ All layer components implemented
✅ Integration tests created and passing
✅ Knowledge base artifacts generated
✅ README and documentation complete
✅ Ready for user review and execution

---

## Notes

This implementation plan was generated by the ESDI workflow:
- **Phase 1 (Exploration)**: {exploration_doc}
- **Phase 2 (Specification)**: {specification_file}
- **Phase 3 (Design)**: {design_file}
- **Phase 4 (Implementation Planning)**: THIS DOCUMENT

**Requirement Traceability**: All tasks mapped to EARS requirements from Phase 2 specification.
**Coverage**: {coverage_percentage}% of requirements addressed in implementation plan.

**Next Step**: Execute via bootstrap-orchestrator.md to build the complete skill.
**Next Step**: Execute tasks sequentially (manually or via a runner) and track progress in a checklist.

---
```

### Step 9: Write File

```
Write complete assembled document to ${output_file}
Validate markdown syntax
Confirm file created successfully
```

### Step 10: Display Completion Message

```
✅ Implementation Plan Generated Successfully

📁 File: ${output_file}
📊 Size: {file_size} KB
📋 Phases: {total_phases}
🎯 Tasks: {total_tasks}
⏱️ Estimated Time: {estimated_total_time} minutes

Ready for Bootstrap Execution:

- If `execution_mode=manual`: start with Phase 1 tasks.
- If `execution_mode=bootstrap`: ensure any enabled Phase 0 tasks (including optional Task 0.0) are completed as specified, then run your chosen runner with `plan_file=${output_file}` and a `checklist_path`.
```

## Success Criteria

✅ Complete IMPLEMENTATION-TASK-PLAN.md written
✅ All sections populated from previous tasks
✅ Requirement traceability matrix included
✅ Coverage statistics documented
✅ Task 0.0 included with CRITICAL annotation
✅ Execution strategy is runner-agnostic (no framework-specific commands assumed)
✅ Optional bootstrap section included only when explicitly enabled
✅ File valid markdown syntax
✅ Ready for sequential execution

## Error Handling

**If output_file write fails**:
```
Error: Cannot write to ${output_file}

Check:
- Directory exists
- Write permissions
- Disk space available

Retry with alternative path
```

**If template missing sections**:
```
Warning: Template section {section_name} not found

Use default section structure
Document which sections auto-generated
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "output_file": "${output_file}",
  "file_size_kb": 156,
  "total_phases": 6,
  "total_tasks": 47,
  "estimated_time_minutes": 470,
  "sections": [
    "Overview",
    "Execution Strategy",
    "Phase 0-5",
    "Bootstrap Execution",
    "Summary",
    "Prerequisites",
    "Success Criteria"
  ]
}
```

## Completion

**Final Task**: Implementation plan complete and ready for execution.

**Next Step**: Execute bootstrap-orchestrator.md to build the skill autonomously.
**Next Step**: Execute tasks sequentially (manually or via your runner) to implement the deliverable.
