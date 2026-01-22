---
task_id: "design-layer-architecture"
task_name: "Design Layer Architecture"
dependencies: ["context.application_type", "context.selected_pattern", "context.functional_requirements"]
conditions: []
---

# Design Layer Architecture

## Input Context
**Required Context Variables**: 
- `context.application_type`: Identified application type
- `context.selected_pattern`: Chosen design pattern
- `context.expected_layers`: Number of layers to design
- `context.functional_requirements[]`: What system must do
- `context.data_flow_type`: Data flow characteristic

**Required Files**:
- `skills/generate-design/kb/design-patterns-guidance.md`

## Task Instructions

### 1. Load Pattern Guidance
Read design patterns KB to get template for `${selected_pattern}`.

### 2. Define Layer Responsibilities

For each layer (up to `${expected_layers}`):

**Layer N: [Name]**

**Purpose**: One-sentence responsibility statement
- Must align with requirements
- Single concern only
- Clear boundary with other layers

**Technology Choice**:
- Python script (for deterministic data operations)
- AI prompt (for interpretation, recommendations)
- SQL query (for database operations)
- API call (for external integrations)
- UI component (for frontend rendering)

**Rationale**: Why this technology for this specific layer?

### 3. Define Layer Interfaces

For each layer:

**Input Interface**:
- Format: JSON | Markdown | API request | Event | User action
- Required fields: [list with types]
- Optional fields: [list with types]
- Example structure

**Output Interface**:
- Format: [type]
- Structure: [fields]
- Handoff to: [next layer name]
- Example structure

### 4. Map Requirements to Layers

For each functional requirement, identify which layer(s) implement it:
```
Requirement: "System SHALL extract project dependencies"
→ Layer 1: Data Collection (Python script scans package.json)

Requirement: "System SHALL recommend refactoring opportunities"
→ Layer 3: Interpretation (AI analyzes complexity metrics)
```

### 5. Define Quality Gates

For each layer, specify validation:
- **Success criteria**: How to verify layer completed successfully
- **Error handling**: What happens on failure
- **Gap detection**: How to identify missing data

### 6. Estimate Execution Times

For each layer:
- Consider data volume
- Account for technology (Python fast, AI slower)
- Factor in dependencies on external systems

## Output Requirements

**State Updates**:
- `context.layer_definitions[]`: Array of layer objects, each with:
  - `layer_id`: Sequential number (1, 2, 3...)
  - `layer_name`: Descriptive name
  - `purpose`: Responsibility statement
  - `technology`: Chosen tech
  - `tech_rationale`: Why this choice
  - `input_format`: Data format received
  - `input_fields[]`: Required input structure
  - `output_format`: Data format produced
  - `output_fields[]`: Output structure
  - `handoff_to`: Next layer name
  - `quality_gate`: Validation approach
  - `execution_time_estimate`: Duration
  - `implements_requirements[]`: Which requirements this layer satisfies
- `context.architecture_diagram`: ASCII diagram of layers and flow
- `task_status.design-layer-architecture`: "completed"

**User Display**:
```
🏗️ Layer Architecture Designed

Layers: [count]
Pattern: [selected_pattern]

[ASCII diagram showing layers and data flow]

Layer Breakdown:
1. [Layer 1 name] - [purpose] ([tech])
2. [Layer 2 name] - [purpose] ([tech])
...
```
