---
name: extract-design-layers
description: "Task 0 - Extract layers and components from design.md"
task_id: 0
protocol: Propose-Act
---

# Task 0: Extract Design Layers

## Objective

Parse design.md and extract structured information about layers, components, and dependencies to drive implementation planning.

## Context Variables

**Required**:
- `design_file`: Path to design.md file

**Outputs**:
- `design_layers`: JSON structure with layers and components
- `skill_name`: Extracted skill name
- `layer_count`: Number of layers

## Execution Steps

### Step 1: Read Design Document

```
1. Read ${design_file}
2. Locate "System Architecture" or "Layered Design" section
3. Extract skill name from title or overview
```

### Step 2: Extract Layers

For each layer in the design:

```
Parse:
- Layer number (1-N)
- Layer name
- Layer description
- Layer responsibilities
- Layer components/modules
- Layer dependencies (which layers it depends on)
```

**Layer Detection Patterns**:
```
- "Layer 1:", "Layer N:" headings
- "### Layer {N}" markdown headers
- Component lists under each layer
- Dependency mentions ("depends on Layer X")
```

### Step 3: Extract Components

For each component within a layer:

```
Parse:
- Component name
- Component type (script, prompt, processor, validator, etc.)
- Component purpose
- Component inputs/outputs
- Implementation notes
```

### Step 4: Analyze Dependencies

```
1. Identify inter-layer dependencies
2. Identify intra-layer dependencies
3. Determine execution sequence
4. Flag circular dependencies (error)
```

### Step 5: Build Structured Output

Generate JSON:

```json
{
  "skill_name": "repository-scanner",
  "description": "Automated repository analysis and documentation",
  "layers": [
    {
      "id": 1,
      "name": "Data Collection",
      "description": "Scan repository and extract raw metadata",
      "components": [
        {
          "name": "FileScanner",
          "type": "python-script",
          "purpose": "Recursively scan directory tree",
          "inputs": ["repository_path"],
          "outputs": ["file_list.json"]
        },
        {
          "name": "MetadataExtractor",
          "type": "python-script",
          "purpose": "Extract file metadata (size, dates, etc.)",
          "inputs": ["file_list.json"],
          "outputs": ["metadata.json"]
        }
      ],
      "dependencies": [],
      "estimated_tasks": 4
    },
    {
      "id": 2,
      "name": "Validation",
      "description": "Validate and normalize collected data",
      "components": [
        {
          "name": "SchemaValidator",
          "type": "python-script",
          "purpose": "Validate metadata against schema",
          "inputs": ["metadata.json"],
          "outputs": ["validated_metadata.json"]
        }
      ],
      "dependencies": [1],
      "estimated_tasks": 3
    }
  ],
  "total_layers": 2,
  "total_components": 3,
  "estimated_total_tasks": 10
}
```

### Step 6: Propose to User

**CRITICAL**: Use Propose-Act protocol

```
Present to user:

📊 Design Analysis Complete

Skill Name: {skill_name}
Layers Found: {total_layers}
Components Found: {total_components}

Layer Breakdown:
  Layer 1: {name} - {component_count} components
  Layer 2: {name} - {component_count} components
  ...

Estimated Implementation Tasks: {estimated_total_tasks}
  - Phase 0 (Setup): 3 tasks
  - Phase 1 (Layer 1): {layer_1_tasks} tasks
  - Phase 2 (Layer 2): {layer_2_tasks} tasks
  ...

Dependencies:
  ✅ No circular dependencies detected
  → Sequential execution: Layer 1 → Layer 2 → ...

APPROVE to proceed to Task 1 (Generate Task 0.0)
ADJUST if layer extraction needs refinement
```

## Success Criteria

✅ All layers extracted with names and descriptions
✅ All components identified with types and purposes
✅ Dependencies mapped correctly (no circular deps)
✅ Estimated task counts calculated
✅ JSON structure valid and complete
✅ User approved via Propose-Act gate

## Error Handling

**If design.md format unrecognized**:
```
Error: Could not parse layer structure from design.md

Expected format:
  ### Layer 1: {Name}
  **Description**: ...
  **Components**:
  - {Component 1}: {Description}
  - {Component 2}: {Description}

Provide guidance and retry.
```

**If circular dependencies found**:
```
Error: Circular dependency detected
  Layer 2 depends on Layer 3
  Layer 3 depends on Layer 2

Resolution required before proceeding.
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "design_layers": { ... },
  "skill_name": "repository-scanner",
  "layer_count": 5,
  "total_components": 12,
  "estimated_tasks": 47
}
```

## Next Task

→ Task 1: generate-task-zero.md (uses design_layers output)
