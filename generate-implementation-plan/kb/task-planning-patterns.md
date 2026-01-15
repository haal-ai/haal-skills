# Task Planning Patterns

## Overview

Patterns for decomposing layered designs into executable implementation tasks following the OLAF onboarding competency model.

---

## Pattern 1: Layer-to-Phase Mapping

**Context**: Multi-layer architecture design needs sequential implementation

**Pattern**:
```
Design Layer → Implementation Phase → Task Group

Layer 1 (Data Collection)    → Phase 1 → Tasks 1.1-1.N (setup, scripts, prompts)
Layer 2 (Validation)          → Phase 2 → Tasks 2.1-2.N (validators, tests)
Layer 3 (Interpretation)      → Phase 3 → Tasks 3.1-3.N (processors, artifacts)
Layer 4 (Querying)            → Phase 4 → Tasks 4.1-4.N (interfaces, skills)
Layer 5 (User Interaction)    → Phase 5 → Tasks 5.1-5.N (prompts, templates)
```

**Guidelines**:
- Each layer becomes a phase
- Phases execute sequentially (dependencies flow upward)
- Tasks within a phase can be parallel or sequential based on dependencies

---

## Pattern 2: Phase 0 - Setup & Context Extraction

**Context**: All implementations need initial setup before layer implementation

**Required Tasks**:

### Task 0.0: Extract Task Contexts
**Purpose**: Generate condensed context files for each task to optimize prompt generation

**Template**:
```markdown
## Task 0.0: Extract Task Contexts

**CRITICAL**: This task MUST be executed FIRST before any other tasks

**Objective**: Generate condensed context files for universal prompt generator

**Execution**:
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md" \
  --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md,skill_path=${skill_path}" \
  --tool-mode standard \
  --aws-profile bedrock

**Outputs**:
- ${skill_path}/tasks/contexts/task-{N}-context.md (one per task)
- Condensed files: ~500 tokens vs ~50KB original (97% reduction)

**Dependencies**: None (first task)
**Duration**: 10-15 minutes
```

### Task 0.1: Create Skill Directory Structure
**Purpose**: Establish directory hierarchy for skill

### Task 0.2: Create Master Coordinator
**Purpose**: Generate main orchestrator prompt

---

## Pattern 3: Task Breakdown Structure

**Context**: Each layer needs logical task decomposition

**Structure**:
```
Phase N: Layer N - {Layer Name}

Task N.1: {Setup/Migration}
  - Migrate existing code/prompts
  - Setup directories
  - Validate prerequisites

Task N.2: {Core Implementation}
  - Implement main functionality
  - Create processing logic
  - Generate outputs

Task N.3: {Integration}
  - Connect to previous layer
  - Validate inputs/outputs
  - Test integration

Task N.4: {Validation & Testing}
  - Create tests
  - Validate outputs
  - Document behavior
```

---

## Pattern 4: STRAF Command Template

**Context**: Each task needs executable STRAF command

**Template**:
```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "{task_prompt_path}" `
  --context "{context_variables}" `
  --tool-mode {standard|auto|minimal} `
  --aws-profile bedrock
```

**Context Variables Pattern**:
```
Common variables:
- skill_path: Path to skill being built
- output_dir: Directory for outputs
- input_file: Path to input artifact
- layer_number: Current layer (1-5)

Task-specific:
- task_id: Unique task identifier (e.g., "1.1", "2.3")
- context_file: Path to condensed context (Task 0.0 output)
```

---

## Pattern 5: Dependency Management

**Context**: Tasks have dependencies that affect execution order

**Types**:

### Sequential Dependencies
```
Task 1.1 → Task 1.2 → Task 1.3
```
Each task must complete before next starts.

### Parallel Opportunities
```
Task 2.1 ──┐
Task 2.2 ──┼→ All can run simultaneously
Task 2.3 ──┘
```
Tasks with no shared dependencies can run in parallel.

### Phase Dependencies
```
Phase 1 (complete) → Phase 2 (start)
```
All tasks in a phase must complete before next phase.

### Cross-Phase Dependencies
```
Task 0.0 → ALL other tasks (context extraction)
Task 0.1 → Task 0.2 → Phase 1+ (structure before implementation)
```

---

## Pattern 6: Output Structure Definition

**Context**: Implementation needs clear output directory structure

**Pattern**:
```markdown
## Output Directory Structure

{skill_path}/
├── skill-manifest.json       # Task 0.1
├── README.md                  # Task 0.1
├── prompts/
│   └── {skill-name}.md       # Task 0.2 (master coordinator)
├── tasks/
│   ├── contexts/             # Task 0.0 outputs
│   │   ├── task-1.1-context.md
│   │   └── task-{N}-context.md
│   ├── layer-1/              # Phase 1 prompts
│   ├── layer-2/              # Phase 2 prompts
│   └── layer-N/
├── tools/                    # Phase 1+ (Python scripts)
├── kb/                       # Phase 3+ (knowledge artifacts)
└── definitions/              # Supporting files
```

---

## Pattern 7: Bootstrap Integration

**Context**: Implementation plan must integrate with bootstrap orchestrator

**Required Sections**:

### 1. Execution Strategy
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

**Task Prompt Generation**: Universal prompt generator with condensed contexts
**Prerequisites**: Task 0.0 must complete first
```

### 2. Bootstrap Command Template
```markdown
## Bootstrap Execution

Execute all tasks via bootstrap orchestrator:

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" \
  --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md,checklist_path=.olaf/work/project-tasks/task-checklist.md" \
  --tool-mode auto \
  --aws-profile bedrock
```
```

---

## Pattern 8: Task Documentation Template

**Context**: Each task needs consistent documentation

**Template**:
```markdown
### Task {N.M}: {Task Name}

**Artifact**: {Primary output/deliverable}
**Execution Time**: {Estimated duration}
**STRAF Command**:
```powershell
{STRAF command}
```

**Task Details**:
- **Input**: {Required inputs}
- **Process**:
  1. {Step 1}
  2. {Step 2}
  N. {Step N}

**Reuse**:
- **Inspire from**: {Existing file/pattern to reference}
- **Pattern**: {Pattern name from this KB}

**Outputs**:
- {Output 1}
- {Output N}

**Dependencies**: {Previous tasks that must complete}
**Success Criteria**:
- ✅ {Criterion 1}
- ✅ {Criterion N}
```

---

## Usage Guide

When generating implementation plans:

1. **Start with Phase 0**: Always include Task 0.0 (context extraction)
2. **Map layers to phases**: Use Pattern 1
3. **Break down each phase**: Apply Pattern 3
4. **Generate STRAF commands**: Use Pattern 4
5. **Document dependencies**: Apply Pattern 5
6. **Define output structure**: Use Pattern 6
7. **Add bootstrap integration**: Use Pattern 7
8. **Document each task**: Follow Pattern 8

---

## Example: 3-Layer Design → Implementation Plan

**Input Design**:
```
Layer 1: Data Ingestion (API client, file reader)
Layer 2: Transformation (normalizer, enricher)
Layer 3: Storage (database writer, cache manager)
```

**Output Plan**:
```
Phase 0: Setup
  - Task 0.0: Extract task contexts
  - Task 0.1: Create skill structure
  - Task 0.2: Create master coordinator

Phase 1: Layer 1 - Data Ingestion
  - Task 1.1: Implement API client
  - Task 1.2: Implement file reader
  - Task 1.3: Create ingestion tests

Phase 2: Layer 2 - Transformation
  - Task 2.1: Implement normalizer
  - Task 2.2: Implement enricher
  - Task 2.3: Create transformation tests

Phase 3: Layer 3 - Storage
  - Task 3.1: Implement database writer
  - Task 3.2: Implement cache manager
  - Task 3.3: Create storage tests

Bootstrap: Execute via bootstrap-orchestrator.md
```
