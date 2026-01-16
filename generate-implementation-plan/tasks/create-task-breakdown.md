---
name: create-task-breakdown
description: "Task 3 - Map layers to phases and generate task structure"
task_id: 3
protocol: Propose-Act
---

# Task 3: Create Task Breakdown

## Objective

Transform design layers into a complete task breakdown structure with phases, tasks, and proper dependencies.

IMPORTANT:
- Do NOT force an onboarding-style Phase 0 (Task 0.0 / 0.1 / 0.2) unless explicitly requested.
- Do NOT assume the deliverable is an OLAF skill under `skills/`.

## Context Variables

**Required**:
- `design_layers`: Output from Task 1
- `task_zero_spec`: Output from Task 2

**Optional**:
- `deliverable_kind`: `tool|skill|library` (default: `skill`)
- `deliverable_root`: Root folder for product deliverables
- `execution_mode`: `manual|bootstrap` (default: `manual`)
- `include_task_context_extraction`: `true|false` (default: `false`)

**Outputs**:
- `task_breakdown`: Structured list of all tasks across all phases

## Execution Steps

### Step 1: Generate Phase 0 (Setup)

Phase 0 is OPTIONAL.

Only include onboarding Task 0.0 (context extraction) when:
- `execution_mode=bootstrap` AND `include_task_context_extraction=true`

Only include "create skill structure" / "create master coordinator" tasks when:
- the design/spec explicitly requires creating an OLAF skill, OR `deliverable_kind=skill`.

```markdown
## PHASE 0: Setup (Optional)

### Task 0.0: Extract Task Contexts (Optional)
{task_zero_spec from Task 2, or omit entirely when not enabled}

### Task 0.1: Create Deliverable Directory Structure (Optional)

**Artifact**: Required folders/files to begin implementation (only what design/spec requires)
**Execution Time**: 5 min
**Execution Notes**:
- Create only the folders/files required by the design/spec under `${deliverable_root}`.
- If you have a runner, capture this as a simple filesystem task.

**Task Details**:
- **Input**: Skill name, target path
- **Process**:
  1. Create directory structure following master-chain pattern
  2. Create placeholder skill.md
  3. Create placeholder README.md

**Outputs**:
- Minimal directory structure required by design/spec

**Dependencies**: Task 0.0 only if Task 0.0 is enabled

### Task 0.2: Create Coordinator/Entrypoint (Optional)

**Artifact**: Coordinator/entrypoint ONLY if required by design/spec (e.g., `skill.md` for an OLAF skill)
**Execution Time**: 10 min
**Execution Notes**:
- Implement the entrypoint/coordinator only if the product deliverable requires it.
- For non-skill deliverables, this may be a CLI entrypoint, library API surface, or minimal bootstrap.

**Task Details**:
- **Input**: Layer count, workflow pattern
- **Process**:
  1. Define task chain for {layer_count} layers
  2. Define state management
  3. Create execution protocol

**Outputs**:
- Entry/coordinator artifacts if required

**Dependencies**: Task 0.1 (if included)
```

### Step 2: Generate Layer Phases

For each layer in design_layers:

```
PHASE {layer_id}: Layer {layer_id} - {layer_name}

For each component in layer:
  Generate task following pattern:
  
  Task {layer_id}.{component_num}: {Component Action}
  
  Example:
    Layer 1, Component "FileScanner" → Task 1.1: Migrate FileScanner
    Layer 1, Component "MetadataExtractor" → Task 1.2: Migrate MetadataExtractor
```

**Task Template** (per component):

```markdown
### Task {layer_id}.{num}: {Action} {ComponentName}

**Artifact**: {Component output or deliverable}
**Execution Time**: {Estimated time}
**Execution Notes**:
- Follow the Task Details and produce the Outputs.
- If using a runner, ensure it passes the minimal required context (component name, layer number, paths) and records artifacts.

**Task Details**:
- **Input**: {Component inputs from design}
- **Process**:
  1. {Step 1 from component purpose}
  2. {Step 2}
  N. {Step N}

**Reuse**:
- **Inspire from**: {Related existing implementation}
- **Pattern**: {Applicable pattern from kb/}

**Outputs**:
- {Component outputs from design}

**Dependencies**: {Previous task IDs}
**Success Criteria**:
- ✅ {Criterion 1}
- ✅ {Criterion 2}
```

### Step 3: Add Integration/Test Tasks Per Layer

After component tasks, add:

```markdown
### Task {layer_id}.{N-1}: Create Integration Tests

**Artifact**: Test suite for Layer {layer_id}
**Execution Time**: 15 min
**Task Details**:
- **Input**: All Layer {layer_id} components
- **Process**:
  1. Create test cases for each component
  2. Create integration tests for layer workflow
  3. Setup test fixtures

**Dependencies**: All previous Layer {layer_id} tasks

### Task {layer_id}.{N}: Validate Layer Outputs

**Artifact**: Validated Layer {layer_id} outputs
**Execution Time**: 10 min
**Task Details**:
- **Input**: Layer {layer_id} outputs
- **Process**:
  1. Run validation tests
  2. Check output format compliance
  3. Verify data quality

**Dependencies**: Task {layer_id}.{N-1} (tests created)
```

### Step 4: Calculate Dependencies

For each task:

```
1. Intra-phase dependencies:
   - Task 1.2 depends on Task 1.1 (if components share data)
   - Task 1.3 (tests) depends on Tasks 1.1, 1.2 (all components)

2. Inter-phase dependencies:
   - All Phase 2 tasks depend on Phase 1 completion
   - Layer N depends on Layer N-1 (per design dependencies)

3. Special dependencies (ONLY if the related tasks are enabled):
  - Tasks may depend on Task 0.0 (context extraction)
  - Coordinator depends on structure creation
```

### Step 5: Calculate Task Counts

```
total_tasks = 3 (Phase 0) + sum(layer_tasks)

Example:
  Phase 0: 3 tasks
  Phase 1 (4 components + 2 integration) = 6 tasks
  Phase 2 (2 components + 2 integration) = 4 tasks
  Phase 3 (3 components + 2 integration) = 5 tasks
  Total: 3 + 6 + 4 + 5 = 18 tasks
```

### Step 6: Propose to User

**CRITICAL**: Use Propose-Act protocol

```
Present to user:

📋 Complete Task Breakdown Generated

Total Phases: {phase_count} (Phase 0 + {layer_count} layers)
Total Tasks: {total_tasks}

Phase Breakdown:
  ✅ Phase 0: Setup (3 tasks)
    - Task 0.0: Extract Task Contexts [CRITICAL FIRST]
    - Task 0.1: Create Skill Directory Structure
    - Task 0.2: Create Master Coordinator Prompt
  
  ✅ Phase 1: Layer 1 - {layer_1_name} ({layer_1_task_count} tasks)
    - Task 1.1: {Component 1}
    - Task 1.2: {Component 2}
    ...
    - Task 1.{N-1}: Create Integration Tests
    - Task 1.{N}: Validate Layer Outputs
  
  ✅ Phase 2: Layer 2 - {layer_2_name} ({layer_2_task_count} tasks)
    ...

Dependency Graph:
  Task 0.0 → ALL tasks (context extraction)
  Task 0.1 → Task 0.2 → Phase 1+
  Phase 1 → Phase 2 → Phase 3 → ...

Execution Order: Sequential by phase, parallel within phase where possible

APPROVE to proceed to Task 4 (Validate Requirement Coverage)
ADJUST if task breakdown needs refinement
```

## Success Criteria

✅ Phase 0 included with Tasks 0.0, 0.1, 0.2
✅ Task 0.0 uses exact spec from Task 2
✅ Each layer mapped to a phase
✅ Each component mapped to a task
✅ Integration and validation tasks added per layer
✅ All dependencies calculated correctly
✅ Task counts accurate
✅ User approved via Propose-Act gate

## Error Handling

**If component missing type**:
```
Warning: Component {name} has no type specified
Default to: "implementation" type
Suggest: Implement {ComponentName}
```

**If too many tasks (>100)**:
```
Warning: {total_tasks} tasks detected (high complexity)
Consider: Group related components into single tasks
Suggest: Combine utilities, helpers into "Implement Support Components"
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "task_breakdown": [
    {
      "phase": 0,
      "phase_name": "Setup",
      "tasks": [
        {
          "id": "0.0",
          "name": "Extract Task Contexts",
          "spec": "{task_zero_spec}",
          "dependencies": []
        },
        {
          "id": "0.1",
          "name": "Create Skill Directory Structure",
          "dependencies": ["0.0"]
        }
      ]
    },
    {
      "phase": 1,
      "phase_name": "Layer 1 - Data Collection",
      "tasks": [...]
    }
  ],
  "total_phases": 6,
  "total_tasks": 47
}
```

## Next Task

→ Task 4: validate-requirement-coverage.md (uses task_breakdown)
