---
name: generate-design
description: Master coordinator for transforming EARS specification into layered system design
license: Apache-2.0
metadata:
  olaf_tags: [design, architecture, specification, layered-design, master-chain]
  olaf_protocol: Propose-Act
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Generate System Design - Master Chain Coordinator

## Master Chain Protocol

**CRITICAL EXECUTION RULES**:
- Execute tasks in STRICT SEQUENTIAL ORDER
- Load only ONE task prompt at a time
- Pass context between tasks via simple variables
- NO anticipation or optimization across tasks
- Each task must complete fully before next

**STARTUP REQUIREMENT**:
Task Chain
Task 1: Analyze EARS Specification
Task 2: Identify Application Type
Task 3: Design Layer Architecture
Task 4: Create Task Breakdown
Task 5: Generate Design Document

## Task Chain Definition

```yaml
task_chain:
  - id: "analyze-specification"
    name: "Analyze EARS Specification"
    prompt: "tasks/analyze-specification.md"
    required: true
    
  - id: "identify-application-type"
    name: "Identify Application Type"
    prompt: "tasks/identify-application-type.md"
    required: true
    depends_on: ["analyze-specification"]
    
  - id: "design-layer-architecture"
    name: "Design Layer Architecture"
    prompt: "tasks/design-layer-architecture.md"
    required: true
    depends_on: ["analyze-specification", "identify-application-type"]
    
  - id: "create-task-breakdown"
    name: "Create Task Breakdown"
    prompt: "tasks/create-task-breakdown.md"
    required: true
    depends_on: ["design-layer-architecture"]
    
  - id: "generate-design-document"
    name: "Generate Design Document"
    prompt: "tasks/generate-design-document.md"
    required: true
    depends_on: ["create-task-breakdown"]
```

## State Management

### Context Variables
Context is passed between tasks using simple variables:

**Input** (provided by user or ESDI):
- `specification_file`: Path to EARS specification document (default: `specification.md` from Phase 2)
- `output_file`: Path where design document should be saved
- `design_patterns`: Path to patterns guidance (default: `kb/design-patterns-guidance.md`)

**Note**: When used in ESDI workflow, `specification_file` should point to the final consolidated 
specification output from Phase 2 (transform-raw-spec), typically named `specification.md` or 
`specification-final.md` in the ESDI output directory.

**Task 1 Output** (Analyze Specification):
- `functional_requirements[]`: Key functional requirements
- `quality_attributes[]`: Performance, reliability, security
- `constraints[]`: Limitations and restrictions
- `stakeholders[]`: User personas
- `data_flow_type`: pipeline | request-response | event-driven | batch
- `interaction_model`: sync | async | batch | interactive
- `complexity_level`: simple | moderate | complex

**Task 2 Output** (Identify Application Type):
- `application_type`: etl | frontend | backend-api | cli-tool | data-analysis | event-driven | batch-processing | microservice
- `confidence_level`: high | medium | low
- `type_rationale`: Why this type was chosen
- `selected_pattern`: Pattern number and name
- `expected_layers`: Number of layers (3-5)

**Task 3 Output** (Design Layer Architecture):
- `layer_definitions[]`: Complete layer specs
- `architecture_diagram`: ASCII diagram of layers

**Task 4 Output** (Create Task Breakdown):
- `task_breakdown[]`: Executable task definitions
- `critical_path[]`: Longest sequential chain
- `parallelizable_tasks[]`: Concurrent execution groups
- `total_execution_time`: Sum estimate

**Task 5 Output** (Generate Design Document):
- `design_document_path`: Path to created file
- `design_complete`: true

## Master Execution Protocol

### 1. Execute Task Chain Loop
For each task in task_chain:

1. **Load Task Prompt**: Read task-specific prompt file from `tasks/` directory
2. **Check Dependencies**: Verify required context variables exist
3. **Execute Task**: Run task with available context
4. **Pass Context**: Make results available to next task
5. **Continue to Next**: Move to next task in chain

### 2. Propose-Act Protocol
After Task 2 (Design Layer Architecture), MUST get user approval:

```
📐 Proposed Design

Application Type: [application_type]
Pattern: [selected_pattern]
Layers: [expected_layers]

[Show architecture_diagram]

Layer Summary:
1. [Layer 1] - [purpose] ([tech])
2. [Layer 2] - [purpose] ([tech])
...

Would you like me to:
1. Proceed with this design
2. Adjust layer structure
3. Change technology choices
4. Modify application type classification
```

**Wait for approval** before proceeding to Task 3.

### 4. Complete Execution
After all tasks, confirm completion:

```
✅ System Design Complete

Output: ${output_file}

Design Summary:
- Application: [application_type]
- Pattern: [selected_pattern]
- Layers: [layer count]
- Tasks: [task count]
- Execution Time: [total estimate]

Next Step: Use generate-implementation-plan to create execution plan
```

## Input Requirements

**Required Context Variables**:
- `specification_file`: Path to EARS specification document
- `output_file`: Path where design document should be saved

**Optional Context Variables**:
- `design_patterns`: Path to design patterns guidance (default: `kb/design-patterns-guidance.md`)
- `system_type`: Hint about system type - if not provided, Task 1 will detect automatically

## Output Files

**Primary Output**: `${output_file}` - Complete system design document

**Format**: Markdown with:
- Architecture diagrams (ASCII)
- Layer definitions
- Interface contracts
- Task breakdown with implementation approach (no executable commands)
- Quality gates and validation strategy

## Knowledge Base

**Design Patterns Guidance**: `kb/design-patterns-guidance.md`
- Application type classification (ETL, Frontend, Backend API, CLI, etc.)
- Proven architecture patterns
- Layer separation principles
- Technology selection guidance
- Multi-language support strategies

**Design Document Template**: `templates/design-document-template.md`
- Standard structure for design outputs
- Sections for all design aspects
- Examples and formatting

## Task Prompt Requirements

Each task prompt in `tasks/` directory must:
1. Have clear input context variables defined
2. Specify processing steps
3. Define output state updates
4. Include user-facing display format

## Example Usage

```bash
# Called from ESDI Phase 3
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/generate-design/prompts/generate-design.md" \
  --context "specification_file=./output/specification.md,output_file=./output/design.md" \
  --tool-mode standard \
  --aws-profile bedrock
```

## Quality Checklist

Before finalizing design, verify:
- [ ] Application type correctly identified
- [ ] Each layer has clear, single responsibility
- [ ] Input/output interfaces explicitly defined
- [ ] Technology choices justified for each layer
- [ ] Tasks have dependencies mapped
- [ ] Implementation approach specified for each task
- [ ] No executable commands generated (deferred to Phase 4)
- [ ] Validation checkpoints identified
- [ ] Multi-language support considered (if processing code)

## Notes

- **Master-chain pattern**: Coordinator orchestrates, tasks do the work
- **Propose-Act protocol**: User approves design before document generation
- **Application-type driven**: Different patterns for ETL vs API vs Frontend
- **Pattern library**: Reusable architecture templates in KB
- **Task isolation**: Each task prompt is independently executable

### Actions
1. Read `${specification_file}`
2. Identify system characteristics:
   - **Data flow type**: Does it collect → process → serve data? (pipeline)
   - **Interaction model**: Request-response? (service)
   - **Complexity**: Simple or multi-phase? (workflow)
   - **Iteration needs**: Refinement cycles? (iterative)
3. Extract key requirements:
   - Functional capabilities (what it must do)
   - Quality attributes (performance, reliability, etc.)
   - Constraints (technology, time, resources)
   - Stakeholders and personas (who uses it)

### Output
Store in memory:
- `system_type`: Detected pattern (pipeline|service|workflow|iterative)
- `key_requirements[]`: List of critical EARS requirements
- `stakeholders[]`: Identified user personas

---

## Step 2: Select Architecture Pattern

### Actions
1. Load design patterns guidance from `${design_patterns}`
2. Match `system_type` to pattern:
   - **Pipeline** → Pattern 1: Data Pipeline Architecture (5 layers)
   - **Service** → Pattern 2: Request-Response Service (3-4 layers)
   - **Workflow** → Pattern 3: Workflow Orchestration (chain-based)
   - **Iterative** → Pattern 4: Iterative Refinement (cyclic)
3. Identify appropriate number of layers
4. Define layer responsibilities based on requirements

### Output
Store in memory:
- `selected_pattern`: Chosen architecture pattern
- `layer_count`: Number of layers needed
- `layer_definitions[]`: Each layer's purpose and responsibility

---

## Step 3: Design Layer Architecture

### Actions
For each layer, define:

1. **Layer Name & Purpose**
   - Clear, descriptive name
   - One-sentence responsibility statement

2. **Input Interface**
   - What does this layer consume?
   - File format (JSON, Markdown, API request, etc.)
   - Required fields/structure

3. **Processing Logic**
   - What transformations/operations occur?
   - Technology choice (Python script, AI prompt, SQL query, etc.)
   - Why this technology for this layer?

4. **Output Interface**
   - What does this layer produce?
   - File format and structure
   - Handoff to next layer

5. **Quality & Validation**
   - How to verify layer completed successfully?
   - Error handling strategy
   - Gap detection approach

6. **Execution Estimate**
   - Expected time to complete (seconds/minutes)
   - Dependencies on previous layers

### Special Considerations

**Multi-Language Support** (if processing code/projects):
- Core layer: Language-agnostic logic
- Adapter sublayer: Language-specific analyzers
- Aggregation: Combine results into unified output

**AI vs Deterministic Processing**:
- **Use Python/scripts** for: Data extraction, file parsing, metrics calculation
- **Use AI prompts** for: Interpretation, explanation, recommendation generation

### Output
Store in memory:
- `architecture_diagram`: ASCII diagram showing layers and data flow
- `layer_details[]`: Complete definition for each layer

---

## Step 4: Define Interface Contracts

## Notes

- **Master-chain pattern**: Coordinator orchestrates, tasks do the work
- **Propose-Act protocol**: User approves design before document generation
- **Application-type driven**: Different patterns for ETL vs API vs Frontend
- **Pattern library**: Reusable architecture templates in KB
- **Task isolation**: Each task prompt is independently executable

