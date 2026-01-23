# Generate Implementation Plan

**Source**: generate-implementation-plan/skill.md

## Overview

Generate Implementation Plan transforms a specification and system design into a detailed, executable implementation task plan with requirement traceability and optional bootstrap integration. It executes a 7-task chain with user approval gates.

## Purpose

Converting designs into actionable implementation plans requires systematic task breakdown, requirement traceability, and proper sequencing. This skill automates the creation of comprehensive implementation plans that ensure all requirements are addressed and tasks are properly ordered for execution.

## Usage

**Command**: `generate implementation plan`

**When to Use**: Use this skill after completing the design phase (Phase 3 of ESDI) when you have both a specification and design document. It's the final phase before actual implementation begins.

## Parameters

### Required Inputs
- **design_file**: Path to design.md from generate-design skill (Phase 3)
- **specification_file**: Path to specification.md from transform-raw-spec skill (Phase 2)
- **output_file**: Path for IMPLEMENTATION-TASK-PLAN.md output

### Optional Inputs
- **skill_name**: Name for the skill being implemented (default: extracted from design)
- **deliverable_kind**: One of `tool`, `skill`, or `library` (default: `skill`)
- **deliverable_root**: Output directory for deliverables
- **execution_mode**: `manual` or `bootstrap` (default: `manual`)
- **include_task_context_extraction**: Include Task 0.0 for context generation (default: `false`)
- **include_bootstrap**: Include bootstrap orchestrator command (default: `false`)
- **include_traceability**: Include requirement traceability matrix (default: `true`)

### Context Requirements
- Access to specification and design documents
- Write access for output file
- Understanding of target deliverable structure

## Output

**Deliverables**:
- Complete IMPLEMENTATION-TASK-PLAN.md
- Requirement traceability matrix
- Phased task breakdown
- Execution instructions

**Format**: Structured markdown with task definitions and traceability

## Process Flow

### Task 1: Extract Requirements and Design
- Parse specification.md and design.md
- Extract EARS requirements
- Map layers, components, and dependencies
- User approval gate

### Task 2: Generate Task Zero (Optional)
- Create Task 0.0 for context extraction
- Set up deliverable structure
- Only when bootstrap execution requested

### Task 3: Create Task Breakdown
- Map layers to implementation phases
- Generate task structure
- Define dependencies
- User approval gate

### Task 4: Validate Requirement Coverage
- Create traceability matrix
- Calculate coverage statistics
- Identify unaddressed requirements
- User approval gate

### Task 5: Generate Execution Steps
- Create execution information for each task
- Define context variables
- Specify dependencies

### Task 6: Create Bootstrap Integration (Optional)
- Generate bootstrap execution instructions
- Only when execution_mode=bootstrap

### Task 7: Generate Plan Document
- Assemble final IMPLEMENTATION-TASK-PLAN.md
- Include all sections and traceability

## Examples

### Example 1: Manual Execution Plan

**Input**:
- specification_file: `./output/specification.md`
- design_file: `./output/design.md`
- output_file: `./output/IMPLEMENTATION-TASK-PLAN.md`
- execution_mode: `manual`

**Output**: Implementation plan for manual task execution

### Example 2: Bootstrap-Ready Plan

**Input**:
- specification_file: `./output/specification.md`
- design_file: `./output/design.md`
- output_file: `./output/IMPLEMENTATION-TASK-PLAN.md`
- execution_mode: `bootstrap`
- include_bootstrap: `true`

**Output**: Implementation plan with bootstrap orchestrator integration

## Output Structure

```markdown
# {Skill Name} Implementation Task Plan

## Overview
## Output Directory Structure
## Execution Strategy

## PHASE 0: Setup & Structure Creation
  ### Task 0.0: Extract Task Contexts [CRITICAL]
  ### Task 0.1: Create Directory Structure
  ### Task 0.2: Create Coordinator

## PHASE 1: Layer 1 - {Layer Name}
  ### Task 1.1: {Component}
  ...

## Requirement Traceability Matrix
## Bootstrap Execution
```

## Related Skills

- **generate-design**: Produces design.md input (Phase 3)
- **transform-raw-spec**: Produces specification.md input (Phase 2)
- **esdi-chain**: Orchestrates generate-implementation-plan as Phase 4
- **run-implementation-plan**: Executes the generated plan

## Tips

1. **Ensure input quality**: Both specification and design must be complete
2. **Review traceability**: Verify all requirements are covered (>95% recommended)
3. **Check dependencies**: Ensure task sequencing is logical
4. **Consider execution mode**: Choose manual for review, bootstrap for automation
5. **Validate coverage**: Address any unaddressed requirements before proceeding

## Limitations

- Requires both specification.md and design.md as inputs
- Does not assume deliverable type without explicit configuration
- Bootstrap integration requires additional prompt paths
- Cannot automatically resolve requirement gaps
- Task execution information depends on deliverable structure
