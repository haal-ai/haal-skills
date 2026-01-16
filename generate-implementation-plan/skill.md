---
name: generate-implementation-plan
description: Transform design document into executable implementation task plan with requirement traceability and bootstrap integration
license: Apache-2.0
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Generate Implementation Plan - Master Coordinator

## Mission

Transform specification + system design into a detailed, executable implementation plan.

IMPORTANT:
- Do NOT assume the deliverable is an OLAF skill (with `skill.md` + `tasks/` prompt tree) unless explicitly requested in the inputs.
- Do NOT inject onboarding Task 0.0 (`extract-task-contexts.md`) or bootstrap-orchestrator execution unless explicitly requested.

## Context Variables

**Required**:
- `design_file`: Path to design.md from generate-design skill (Phase 3)
- `specification_file`: Path to specification.md from transform-raw-spec skill (Phase 2)
- `output_file`: Path for IMPLEMENTATION-TASK-PLAN.md output

**Optional**:
- `skill_name`: Name for the skill being implemented (default: extracted from design)
- `deliverable_kind`: One of `tool|skill|library` (default: `skill`)
- `deliverable_root`: Output/root directory for the actual product deliverables (default: derived from design; for `skill`, defaults to `skills/${skill_name}`)
- `skill_path`: Back-compat alias for `deliverable_root` when `deliverable_kind=skill`
- `execution_mode`: One of `manual|bootstrap` (default: `manual`)
- `include_task_context_extraction`: Include onboarding Task 0.0 condensed-context generation (default: `false`; only valid when `execution_mode=bootstrap`)
- `include_bootstrap`: Include bootstrap orchestrator command (default: `false`; only valid when `execution_mode=bootstrap`)
- `task_context_extractor_prompt`: Path to a context-extraction prompt (optional; required only if `include_task_context_extraction=true`)
- `bootstrap_orchestrator_prompt`: Path to a bootstrap/orchestrator prompt (optional; required only if `include_bootstrap=true`)
- `include_traceability`: Include requirement traceability matrix (default: true)

## Task Chain

This coordinator executes **7 sequential tasks** using the Propose-Act protocol:

```yaml
workflow:
  type: master-chain
  protocol: Propose-Act
  tasks:
    - id: 1
      name: extract-requirements-and-design
      file: tasks/extract-requirements-and-design.md
      propose_after: true
      
    - id: 2
      name: generate-task-zero
      file: tasks/generate-task-zero.md
      propose_after: true
      
    - id: 3
      name: create-task-breakdown
      file: tasks/create-task-breakdown.md
      propose_after: true
      
    - id: 4
      name: validate-requirement-coverage
      file: tasks/validate-requirement-coverage.md
      propose_after: true
      
    - id: 5
      name: generate-execution-steps
      file: tasks/generate-execution-steps.md
      propose_after: true
      
    - id: 6
      name: create-bootstrap-integration
      file: tasks/create-bootstrap-integration.md
      propose_after: true
      
    - id: 7
      name: generate-plan-document
      file: tasks/generate-plan-document.md
      propose_after: false  # Final task, just execute
```

---

## Execution Flow

### PHASE 1: Extract Requirements and Design (Task 1)

**Objective**: Parse specification.md and design.md to extract EARS requirements, layers, components, and dependencies

```
INPUT: ${specification_file}, ${design_file}
OUTPUT: requirements_map (JSON), design_layers (JSON structure)

Agent spawns: tasks/extract-requirements-and-design.md
Context: specification_file=${specification_file},design_file=${design_file}

Propose-Act Gate:
  - Present extracted layers to user
  - Show component counts per layer
  - Confirm layer mapping is correct
  → User approves or requests adjustments
```

**Expected Output**:
```json
{
  "skill_name": "repo-scanner",
  "requirements": [
    {
      "id": "REQ-F-001",
      "type": "functional",
      "text": "The system SHALL scan repository directory tree",
      "priority": "high"
    },
    {
      "id": "REQ-P-001",
      "type": "performance",
      "text": "The system SHALL process 10k files in < 30s",
      "priority": "medium"
    }
  ],
  "layers": [
    {
      "id": 1,
      "name": "Data Collection",
      "components": ["FileScanner", "MetadataExtractor"],
      "dependencies": [],
      "addresses_requirements": ["REQ-F-001"]
    },
    {
      "id": 2,
      "name": "Validation",
      "components": ["SchemaValidator", "QualityChecker"],
      "dependencies": [1],
      "addresses_requirements": ["REQ-P-001"]
    }
  ]
}
```

---

### PHASE 2: Generate Task 0.0 (Task 2)

**Objective**: Optionally create Task 0.0 (condensed context extraction) when bootstrap execution is requested

```
INPUT: design_layers, ${deliverable_root}
OUTPUT: task_zero_spec

Agent spawns: tasks/generate-task-zero.md
Context: execution_mode=${execution_mode},include_task_context_extraction=${include_task_context_extraction},task_context_extractor_prompt=${task_context_extractor_prompt},deliverable_root=${deliverable_root}

Propose-Act Gate:
  - Present Task 0.0 specification
  - Show context extraction pattern
  - Confirm it is enabled/desired (or omitted)
  → User approves
```

**Expected Output**:
```markdown
## Task 0.0: Extract Task Contexts

**CRITICAL**: Execute FIRST before all other tasks

**Objective**: Generate condensed context files for task execution

**Task Prompt**: `${task_context_extractor_prompt}`  
**Context**: `bootstrap_doc=${output_file},deliverable_root=${deliverable_root}`

**Outputs**:
- ${deliverable_root}/tasks/contexts/task-{N}-context.md
- ~97% size reduction vs original plan
```

---

### PHASE 3: Create Task Breakdown (Task 3)

**Objective**: Map layers to phases and generate task structure

```
INPUT: design_layers
OUTPUT: task_breakdown (structured task list)

Agent spawns: tasks/create-task-breakdown.md
Context: design_layers=${design_layers}

Propose-Act Gate:
  - Present complete task breakdown
  - Show phases 0-N with all tasks
  - Display dependency graph
  - Confirm sequencing is correct
  → User approves or adjusts
```

**Expected Output**:
```
Phase 0: Setup (optional; only if required)
  - Task 0.0: Extract Task Contexts (optional)
  - Task 0.1: Create Deliverable Structure (optional)
  - Task 0.2: Create Coordinator/Entrypoint (optional)

Phase 1: Layer 1 - Data Collection (4 tasks)
  - Task 1.1: Migrate FileScanner
  - Task 1.2: Migrate MetadataExtractor
  - Task 1.3: Create Integration Tests
  - Task 1.4: Validate Outputs

Phase 2: Layer 2 - Validation (3 tasks)
  - Task 2.1: Implement SchemaValidator
  - Task 2.2: Implement QualityChecker
  - Task 2.3: Create Validation Tests
```

---

### PHASE 4: Validate Requirement Coverage (Task 4)

**Objective**: Verify all EARS requirements from Phase 2 are addressed in task breakdown

```
INPUT: requirements_map, task_breakdown
OUTPUT: traceability_matrix, coverage_report

Agent spawns: tasks/validate-requirement-coverage.md
Context: requirements_map=${requirements_map},task_breakdown=${task_breakdown}

Propose-Act Gate:
  - Present requirement traceability matrix
  - Show coverage statistics (e.g., 45/47 requirements covered)
  - Highlight any unaddressed requirements
  - Confirm coverage is acceptable
  → User approves or requests additional tasks
```

**Expected Output**:
```markdown
# Requirement Traceability Matrix

| Req ID | Requirement | Layer | Tasks | Status |
|--------|-------------|-------|-------|--------|
| REQ-F-001 | System SHALL scan repository | Layer 1 | 1.1, 1.2 | ✅ Covered |
| REQ-F-002 | System SHALL validate metadata | Layer 2 | 2.1 | ✅ Covered |
| REQ-P-001 | Process 10k files in < 30s | Layer 1 | 1.3 | ✅ Covered |
| REQ-S-001 | Use secure file access | Layer 1 | 1.1 | ⚠️ Partial |

**Coverage**: 45/47 requirements (95.7%)
**Unaddressed**: REQ-F-015, REQ-S-003
```

---

### PHASE 5: Generate Execution Steps (Task 5)

**Objective**: Create execution steps for each task

```
INPUT: task_breakdown
OUTPUT: task_commands (commands for each task)

Agent spawns: tasks/generate-execution-steps.md
Context: task_breakdown=${task_breakdown},skill_path=${skill_path}

Propose-Act Gate:
  - Present task execution information
  - Show context variable usage
  - Confirm task structure
  → User approves
```

**Expected Output**:
```
# Task 1.1: Migrate FileScanner
**Task Prompt**: `${skill_path}/tasks/layer-1/migrate-file-scanner.md`
**Context**: `skill_path=${skill_path},component=FileScanner`
**Dependencies**: Task 0.0, 0.1, 0.2
```

---

### PHASE 6: Create Bootstrap Integration (Task 6)

**Objective**: Optionally generate bootstrap execution instructions when `execution_mode=bootstrap`

```
INPUT: ${output_file}, ${deliverable_root}
OUTPUT: bootstrap_instructions

Agent spawns: tasks/create-bootstrap-integration.md
Context: execution_mode=${execution_mode},include_bootstrap=${include_bootstrap},bootstrap_orchestrator_prompt=${bootstrap_orchestrator_prompt},output_file=${output_file}

Propose-Act Gate:
  - Present bootstrap instructions
  - Show integration approach
  - Confirm ready for execution
  → User approves
```

**Expected Output**:
```markdown
# Execute Complete Implementation Plan
**Task Prompt**: `${bootstrap_orchestrator_prompt}`
**Context**: `bootstrap_doc=${output_file},checklist_path=.olaf/work/project-tasks/task-checklist.md`
```

---

### PHASE 7: Generate Plan Document (Task 7)

**Objective**: Write final IMPLEMENTATION-TASK-PLAN.md

```
INPUT: All previous outputs
OUTPUT: ${output_file}

Agent spawns: tasks/generate-plan-document.md
Context: all_task_data=${collected_data},output_file=${output_file}

NO Propose-Act Gate (final assembly)
```

**Expected Output**: Complete IMPLEMENTATION-TASK-PLAN.md

---

## State Management

Track progress across tasks:

```json
{
  "workflow": "generate-implementation-plan",
  "design_file": ".olaf/work/staging/esdi/20251122-repo-scanner/design.md",
  "output_file": ".olaf/work/staging/esdi/20251122-repo-scanner/IMPLEMENTATION-TASK-PLAN.md",
  "current_task": 2,
  "tasks": {
    "extract-requirements-and-design": {
      "status": "completed",
      "output": {
        "skill_name": "repo-scanner",
        "layers": [...],
        "total_components": 12
      }
    },
    "generate-task-zero": {
      "status": "completed",
      "output": "task_zero_spec.md"
    },
    "create-task-breakdown": {
      "status": "in-progress"
    }
  }
}
```

---

## Success Criteria

✅ **All EARS requirements** from Phase 2 extracted and mapped
✅ **Requirement traceability matrix** generated
✅ **Requirement coverage** validated (>95% recommended)
✅ **All layers** mapped to implementation phases with requirement references
✅ **Task execution information** generated for every task
✅ **Bootstrap integration** instructions provided
✅ **Dependencies** properly sequenced
✅ **Output structure** follows onboarding competency model
✅ **Ready for execution** via bootstrap orchestrator

---

## Error Handling

```
IF layer extraction fails:
  - Log error details
  - Provide design.md format guidance
  - Allow retry with corrections

IF task breakdown invalid:
  - Show dependency conflicts
  - Suggest resolution
  - Allow manual adjustment

IF task execution information generation fails:
  - Show problematic task
  - Provide structure template
  - Allow manual completion
```

---

## Output Structure

Final IMPLEMENTATION-TASK-PLAN.md contains:

```markdown
# {Skill Name} Implementation Task Plan

**Version**: 1.0
**Date**: {timestamp}
**Execution**: Sequential task execution
**Target**: {skill_path}

## Overview
{High-level description from design}

## Output Directory Structure
{Expected file tree}

## Execution Strategy
{How to execute tasks sequentially}

## PHASE 0: Setup & Structure Creation
  ### Task 0.0: Extract Task Contexts [CRITICAL - FIRST]
  ### Task 0.1: Create Skill Directory Structure
  ### Task 0.2: Create Master Coordinator Prompt

## PHASE 1: Layer 1 - {Layer Name}
  ### Task 1.1: {Component/Feature}
  ...

## PHASE N: Layer N - {Layer Name}
  ...

## Bootstrap Execution
{Bootstrap orchestrator command}
```

---

## Integration Notes

This coordinator produces the final artifact of the ESDI workflow:
- **Input**: 
  - specification.md from Phase 2 (transform-raw-spec) - EARS requirements
  - design.md from Phase 3 (generate-design) - Layered architecture
- **Output**: IMPLEMENTATION-TASK-PLAN.md for bootstrap execution with requirement traceability
- **Next Step**: Execute via bootstrap-orchestrator.md

**Dependencies**:
- ✅ generate-design skill (produces design.md)
- ✅ bootstrap-orchestrator prompt (executes plan)
- ✅ universal-task-prompt-generator (generates task prompts)

---

## Tools Required

- `file_read`: Read design.md
- `file_write`: Write IMPLEMENTATION-TASK-PLAN.md
- `json_parse`: Parse design layers
- `template_render`: Generate templates

---

## Example Execution

Invoke the generate-implementation-plan skill:

**Context**:
- `design_file`: Path to design.md from generate-design skill
- `output_file`: Path for IMPLEMENTATION-TASK-PLAN.md
- `skill_path`: Target skill directory path

**Result**: IMPLEMENTATION-TASK-PLAN.md ready for bootstrap execution
