---
name: generate-plan-document
description: "Task 5 - Write final IMPLEMENTATION-TASK-PLAN.md"
task_id: 5
protocol: Act
---

# Task 5: Generate Plan Document

## Objective

Assemble all outputs from previous tasks into the final IMPLEMENTATION-TASK-PLAN.md file following the onboarding competency pattern.

## Context Variables

**Required**:
- `requirements_map`: From Task 0
- `design_layers`: From Task 0
- `task_zero_spec`: From Task 1
- `task_breakdown`: From Task 2
- `traceability_matrix`: From Task 3
- `coverage_report`: From Task 3
- `task_commands`: From Task 4
- `bootstrap_command`: From Task 5
- `output_file`: Path to write IMPLEMENTATION-TASK-PLAN.md
- `specification_file`: Original Phase 2 specification path
- `design_file`: Original Phase 3 design path

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
**Execution**: Sequential via STRAF Agents  
**Target**: {skill_path}

---
```

### Step 3: Add Overview Section

```markdown
## Overview

{Extract from design.md introduction}

**Final Outcome**: {skill_path} with master coordinator and task prompts executable via STRAF agents.

**Requirement Coverage**: {coverage_percentage}% ({covered_count}/{total_requirements} requirements addressed)

**Output Directory Structure**:
```
{skill_path}/
├── skill-manifest.json
├── README.md
├── prompts/
│   └── {skill-name}.md (master coordinator)
├── tasks/
│   ├── contexts/          # Task 0.0 outputs
│   ├── setup/             # Phase 0 prompts
│   ├── layer-1/           # Phase 1 prompts
│   ├── layer-2/           # Phase 2 prompts
│   └── layer-N/
├── tools/                 # Python scripts (if applicable)
├── kb/                    # Knowledge artifacts
└── definitions/           # Supporting files
```

---
```

### Step 4: Add Execution Strategy

```markdown
## Execution Strategy

Each task will be submitted to STRAF agent using:

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "<task-prompt-path>" `
  --context "<context-variables>" `
  --tool-mode standard `
  --aws-profile bedrock
```

**Task Prompt Generation**: Tasks use universal-task-prompt-generator.md with condensed contexts from Task 0.0

**Prerequisites**: Task 0.0 MUST complete first to generate context files

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
  **STRAF Command**:
  ```powershell
  {task_commands[task_id]}
  ```
  
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

{Insert bootstrap instructions from Task 4}

{Insert bootstrap_command from Task 4}

{Insert resume command pattern from Task 4}

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

Before executing bootstrap:

1. ✅ **AWS credentials configured**
   - Profile: bedrock
   - Region: {aws_region}
   
2. ✅ **STRAF agent operational**
   - Path: .olaf/core/agentic/straf/olaf_strands_agent.py
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

✅ Skill directory structure created ({skill_path})
✅ Master coordinator prompt implemented
✅ All layer components implemented
✅ Integration tests created and passing
✅ Knowledge base artifacts generated
✅ README and documentation complete
✅ Skill executable via STRAF agent
✅ Ready for production use

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

python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=${output_file},checklist_path=.olaf/work/project-tasks/task-checklist.md" `
  --tool-mode auto `
  --aws-profile bedrock

⚠️ IMPORTANT: Run Task 0.0 manually FIRST to extract task contexts!
```

## Success Criteria

✅ Complete IMPLEMENTATION-TASK-PLAN.md written
✅ All sections populated from previous tasks
✅ Requirement traceability matrix included
✅ Coverage statistics documented
✅ Task 0.0 included with CRITICAL annotation
✅ STRAF commands formatted correctly
✅ Bootstrap execution section complete
✅ File valid markdown syntax
✅ Ready for bootstrap orchestrator

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
