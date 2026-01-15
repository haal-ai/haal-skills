---
name: create-task-breakdown
description: "Task 2 - Map layers to phases and generate task structure"
task_id: 2
protocol: Propose-Act
---

# Task 2: Create Task Breakdown

## Objective

Transform design layers into complete task breakdown structure with Phase 0 (setup), layer phases, and proper dependencies.

## Context Variables

**Required**:
- `design_layers`: Output from Task 0
- `task_zero_spec`: Output from Task 1

**Outputs**:
- `task_breakdown`: Structured list of all tasks across all phases

## Execution Steps

### Step 1: Generate Phase 0 (Setup)

**Fixed tasks** for every implementation:

```markdown
## PHASE 0: Setup & Structure Creation

### Task 0.0: Extract Task Contexts
{task_zero_spec from Task 1}

### Task 0.1: Create Skill Directory Structure

**Artifact**: Complete skill directory following chain model
**Execution Time**: 5 min
**STRAF Command**:
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${skill_path}/tasks/setup/create-skill-structure.md" `
  --context "skill_name=${skill_name},target_path=${skill_path}" `
  --tool-mode standard --aws-profile bedrock
```

**Task Details**:
- **Input**: Skill name, target path
- **Process**:
  1. Create directory structure following master-chain pattern
  2. Generate skill-manifest.json
  3. Create placeholder README.md

**Outputs**:
- Complete skill directory structure
- skill-manifest.json with metadata

**Dependencies**: Task 0.0 (context extraction)

### Task 0.2: Create Master Coordinator Prompt

**Artifact**: prompts/${skill_name}.md (master coordinator)
**Execution Time**: 10 min
**STRAF Command**:
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${skill_path}/tasks/setup/create-master-coordinator.md" `
  --context "skill_name=${skill_name},layers=${layer_count},pattern=sequential" `
  --tool-mode standard --aws-profile bedrock
```

**Task Details**:
- **Input**: Layer count, workflow pattern
- **Process**:
  1. Define task chain for {layer_count} layers
  2. Define state management
  3. Create execution protocol

**Outputs**:
- prompts/${skill_name}.md with complete task chain

**Dependencies**: Task 0.1 (structure created)
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
**STRAF Command**:
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "${skill_path}/tasks/layer-{layer_id}/{task-slug}.md" `
  --context "skill_path=${skill_path},component={ComponentName},layer_number={layer_id}" `
  --tool-mode standard --aws-profile bedrock
```

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

3. Special dependencies:
   - ALL tasks depend on Task 0.0 (context extraction)
   - Task 0.2 depends on Task 0.1 (structure before coordinator)
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

APPROVE to proceed to Task 3 (Generate STRAF Commands)
ADJUST if task breakdown needs refinement
```

## Success Criteria

✅ Phase 0 included with Tasks 0.0, 0.1, 0.2
✅ Task 0.0 uses exact spec from Task 1
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

→ Task 3: generate-straf-commands.md (uses task_breakdown)
