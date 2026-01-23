---
name: extract-requirements-and-design
description: "Task 1 - Extract EARS requirements and design layers with traceability mapping"
task_id: 1
protocol: Propose-Act
---

# Task 1: Extract Requirements and Design

## Objective

Parse specification.md (Phase 2) and design.md (Phase 3) to extract:
1. EARS requirements from specification
2. Layered architecture from design
3. Requirement-to-layer mapping for traceability

## Context Variables

**Required**:
- `specification_file`: Path to specification.md (Phase 2 output)
- `design_file`: Path to design.md (Phase 3 output)

**Outputs**:
- `requirements_map`: JSON structure with all EARS requirements
- `design_layers`: JSON structure with layers and components
- `requirement_layer_mapping`: Initial mapping of requirements to layers
- `skill_name`: Extracted skill name

## Execution Steps

### Step 1: Extract EARS Requirements from Specification

```
1. Read ${specification_file}
2. Parse all EARS requirement sections:
   - Functional Requirements (SHALL/MUST statements)
   - Performance Requirements (response times, throughput)
   - Security Requirements (authentication, authorization, data protection)
   - Usability Requirements (user experience, accessibility)
   - Reliability Requirements (uptime, error handling)
   
3. Extract each requirement:
   - Requirement ID (e.g., REQ-F-001, REQ-P-001)
   - Type (functional, performance, security, usability, reliability)
   - Full requirement text
   - Priority (high, medium, low) if specified
   - Acceptance criteria if available
```

**EARS Pattern Detection**:
```
- "The system SHALL..." → Functional requirement
- "The system MUST..." → Functional requirement (mandatory)
- "The system SHOULD..." → Optional requirement
- "WHEN <trigger> the system SHALL..." → Event-driven requirement
- "WHERE <condition> the system SHALL..." → Conditional requirement
- "WHILE <state> the system SHALL..." → State-based requirement
```

### Step 2: Extract Design Layers

```
1. Read ${design_file}
2. Locate "System Architecture" or "Layered Design" section
3. Extract skill name from title or overview

For each layer:
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

### Step 3: Extract Components per Layer

For each component within a layer:

```
Parse:
- Component name
- Component type (script, prompt, processor, validator, etc.)
- Component purpose
- Component inputs/outputs
- Implementation notes
```

### Step 4: Map Requirements to Layers

```
For each requirement in requirements_map:
  1. Analyze requirement text
  2. Identify which layer(s) address this requirement
  3. Match based on:
     - Keyword matching (e.g., "scan" → Data Collection layer)
     - Functional alignment (e.g., "validate" → Validation layer)
     - Design document references
  
  4. Create mapping:
     requirement_id → [layer_ids that address it]
```

**Mapping Strategy**:
```
- Functional requirements → Usually map to specific layers
- Performance requirements → May span multiple layers
- Security requirements → Often cross-cutting concerns
- Usability requirements → Usually presentation/interface layers
- Reliability requirements → Often cross-cutting or infrastructure layer
```

### Step 5: Build Structured Output

Generate JSON structures:

```json
{
  "skill_name": "repository-scanner",
  "requirements": [
    {
      "id": "REQ-F-001",
      "type": "functional",
      "category": "data-collection",
      "text": "The system SHALL recursively scan repository directory tree",
      "priority": "high",
      "acceptance_criteria": [
        "All files and directories discovered",
        "Handles symbolic links correctly",
        "Respects .gitignore patterns"
      ]
    },
    {
      "id": "REQ-F-002",
      "type": "functional",
      "category": "validation",
      "text": "The system SHALL validate metadata against schema",
      "priority": "high",
      "acceptance_criteria": [
        "Schema validation passes for valid data",
        "Clear error messages for invalid data"
      ]
    },
    {
      "id": "REQ-P-001",
      "type": "performance",
      "text": "The system SHALL process 10,000 files in less than 30 seconds",
      "priority": "medium",
      "acceptance_criteria": [
        "Performance test shows <30s for 10k files"
      ]
    },
    {
      "id": "REQ-S-001",
      "type": "security",
      "text": "The system SHALL use secure file access permissions",
      "priority": "high",
      "acceptance_criteria": [
        "No elevated privileges required",
        "File access respects OS permissions"
      ]
    }
  ],
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
      "addresses_requirements": ["REQ-F-001", "REQ-P-001", "REQ-S-001"],
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
        },
        {
          "name": "QualityChecker",
          "type": "python-script",
          "purpose": "Check data quality and completeness",
          "inputs": ["validated_metadata.json"],
          "outputs": ["quality_report.json"]
        }
      ],
      "dependencies": [1],
      "addresses_requirements": ["REQ-F-002"],
      "estimated_tasks": 3
    }
  ],
  "requirement_layer_mapping": {
    "REQ-F-001": [1],
    "REQ-F-002": [2],
    "REQ-P-001": [1],
    "REQ-S-001": [1]
  },
  "total_requirements": 4,
  "total_layers": 2,
  "total_components": 4,
  "estimated_total_tasks": 10
}
```

### Step 6: Propose to User

**CRITICAL**: Ask for user approval before proceeding

```
Present to user:

📊 Requirements & Design Analysis Complete

Skill Name: {skill_name}

📋 EARS Requirements Found: {total_requirements}
  - Functional: {functional_count}
  - Performance: {performance_count}
  - Security: {security_count}
  - Usability: {usability_count}
  - Reliability: {reliability_count}

🏗️ Design Layers Found: {total_layers}
  - Layer 1: {name} - {component_count} components → Addresses {req_count} requirements
  - Layer 2: {name} - {component_count} components → Addresses {req_count} requirements
  ...

🔗 Initial Requirement Mapping:
  {For each layer, show which requirements it addresses}

⚠️ Potential Gaps:
  {List any requirements not clearly mapped to layers}

Does this extraction look correct?
```

### Step 7: User Approval Gate

Wait for user response:
- **"yes" / "approved"** → Proceed to next task
- **"adjust X"** → Refine extraction and re-propose
- **"add mapping"** → Add missing requirement-to-layer mappings

## Success Criteria

✅ All EARS requirements extracted from specification.md
✅ All layers and components extracted from design.md
✅ Skill name identified correctly
✅ Initial requirement-to-layer mapping created
✅ Requirements categorized by type (functional, performance, etc.)
✅ No parsing errors or missing sections
✅ User approves extraction

## Error Handling

**If specification.md not found**:
```
Error: Cannot read specification file: ${specification_file}

This file should be the final output from ESDI Phase 2 (transform-raw-spec).

Expected location: .olaf/work/staging/esdi/{timestamp}-{topic}/specification.md

Please verify the path or regenerate Phase 2 specification.
```

**If design.md not found**:
```
Error: Cannot read design file: ${design_file}

This file should be the output from ESDI Phase 3 (generate-design).

Expected location: .olaf/work/staging/esdi/{timestamp}-{topic}/design.md

Please verify the path or regenerate Phase 3 design.
```

**If requirements not in EARS format**:
```
Warning: Some requirements do not follow EARS pattern

Non-EARS requirements found:
  - {requirement_text}
  
These will be included but may need refinement.
Consider re-running Phase 2 with stricter EARS validation.
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "skill_name": "repository-scanner",
  "requirements_count": 47,
  "layers_count": 5,
  "components_count": 18,
  "mapped_requirements": 45,
  "unmapped_requirements": 2,
  "requirements_map": {...},
  "design_layers": {...},
  "requirement_layer_mapping": {...}
}
```

## Next Task

Proceed to Task 1: Generate Task 0.0 specification
