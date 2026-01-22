# [System Name] Design

**Version**: 1.0  
**Status**: Design Complete  
**Last Updated**: [YYYY-MM-DD]

---

## Overview

[Brief description of system purpose, scope, and key stakeholders]

---

## Architecture: [Pattern Name]

```
[ASCII diagram showing complete layer structure with data flow arrows]

Example:
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: Data Collection                                   │
│ Purpose: Extract raw data from sources                     │
└─────────────────────────────────────────────────────────────┘
                         ↓ Produces: raw-*.json
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: Validation                                        │
│ Purpose: Verify data quality and completeness              │
└─────────────────────────────────────────────────────────────┘
                         ↓ Produces: validated-*.md
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: [Continue for all layers]                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Layer Definitions

### Layer 1: [Layer Name]

**Purpose**: [One-sentence responsibility statement]

**Input**: 
- Format: [JSON | Markdown | API | etc]
- Source: [Where data comes from]
- Required fields:
  - `field1`: [description and type]
  - `field2`: [description and type]

**Processing**:
- [Detailed description of what this layer does]
- Technology: [Python script | AI prompt | SQL query | etc]
- Rationale: [Why this technology choice]
- Execution time: [Estimated duration]

**Output**:
- Format: [file type]
- Location: `[path/to/output]`
- Structure:
  ```json
  {
    "field": "value",
    "example": "structure"
  }
  ```

**Quality Validation**:
- Success criteria: [How to verify layer completed successfully]
- Error handling: [What happens if processing fails]
- Gap detection: [How to identify missing or incomplete data]

---

[Repeat Layer Definition section for each layer]

---

## Interface Contracts

### Layer 1 → Layer 2

**File**: `raw-data.json`  
**Format**: JSON

**Required Fields**:
```json
{
  "field_name": "type (string|number|array|object)",
  "description": "what this field contains"
}
```

**Optional Fields**:
```json
{
  "optional_field": "type",
  "description": "what this field contains"
}
```

**Example**:
```json
{
  "repository": "/path/to/repo",
  "modules": [
    {
      "name": "module-1",
      "language": "typescript"
    }
  ]
}
```

**Validation Rules**:
- [Field X must not be empty]
- [Field Y must match pattern Z]
- [Field relationships and constraints]

---

[Repeat Interface Contract for each layer boundary]

---

## Task Breakdown

### Task 0: [Task Name]

**Layer**: [Which architecture layer this implements]

**Input**: 
- Context variables: `var1`, `var2`
- Files required: `[path/to/file]`

**Processing**:
[Detailed description of what this task does]

**Output**:
- Files created: `[path/to/output]`
- Artifacts: [List of generated items]

**Dependencies**: 
- Must complete after: [Task IDs]

**Execution Time**: [Estimate]

**Technology**: [Python script | AI prompt | shell command]

**STRAF Command** (if applicable):
```bash
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "path/to/task.md" \
  --context "var1=value1,var2=value2" \
  --tool-mode standard --aws-profile bedrock
```

---

[Repeat Task Definition for each task]

---

## Data Flow Diagram

```
[Detailed ASCII diagram showing how data transforms through the system]

Example:
Repository (input)
  ↓
Task 0: Initialize → context variables set
  ↓
Task 1: Extract structure → raw-structure.json
  ↓
Task 2: Extract dependencies → raw-dependencies.json
  ↓  ↓
Task 3: Validate both → validated-data.md
  ↓
Task 4: Generate artifact → artifact-build-guide.md
  ↓
User Query (output)
```

---

## Quality Gates

### Validation Checkpoints

**After Layer 1 (Data Collection)**:
- [ ] All expected files generated
- [ ] File formats valid (JSON schema validation)
- [ ] No empty/null critical fields

**After Layer 2 (Validation)**:
- [ ] Gap report generated
- [ ] Missing data items identified
- [ ] Quality score meets threshold

**After Layer 3 (Artifacts)**:
- [ ] All artifacts address requirements
- [ ] Cross-references correct
- [ ] Completeness verified

### Gap Detection Strategy

[How the system identifies and reports missing information]

**Example**:
- Compare required fields vs collected data
- Generate `gaps-and-recommendations.md`
- Suggest additional data sources or manual input

---

## Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Layer 1 | Python scripts | Fast, deterministic data extraction |
| Layer 2 | AI-based | Requires interpretation and judgment |
| Layer 3 | AI-based | Generates human-readable documentation |
| Layer 4 | Python + AI | Indexing (deterministic) + matching (semantic) |

---

## Execution Timeline

**Total Estimated Time**: [Sum of all task estimates]

**Critical Path** (longest sequential dependency chain):
```
Task 0 → Task 1 → Task 3 → Task 5 → Task 7
Total: [time estimate]
```

**Parallelizable Tasks** (can run concurrently):
- Tasks 1 & 2 (both depend only on Task 0)
- Tasks 4 & 5 (both depend on Task 3)

**Optimization Opportunities**:
- [Suggestions for parallel execution]
- [Caching strategies for repeated data]

---

## Multi-Language Support

[If system processes code/projects across multiple languages]

### Language Detection Strategy
- [How to identify which languages are present]
- [How to select appropriate analyzers]

### Language-Specific Adapters

| Language | Analyzer/Tool | Thresholds |
|----------|---------------|------------|
| TypeScript | complexity-report | Cyclomatic > 30 |
| Python | radon | Cyclomatic > 20 |
| Java | PMD | Cyclomatic > 40 |

### Aggregation Strategy
- [How results from different languages are combined]
- [Normalization approach for cross-language comparison]

---

## Complexity Thresholds

[If system analyzes code quality]

### Halstead Metrics
- **Difficulty > 30**: Flag for review (industry normal: 10-25)
- **Effort > 15,000**: Requires refactoring

### Cyclomatic Complexity (Language-Specific)

| Language | Acceptable | Monitor | Action Needed |
|----------|-----------|---------|---------------|
| TypeScript/JS | 1-20 | 21-30 | > 30 |
| Python | 1-10 | 11-20 | > 20 |
| Java/C# | 1-20 | 21-40 | > 40 |

**Philosophy**: Focus on genuine maintainability issues, not nitpick normal code.

---

## Appendix

### Design Decisions

**Decision 1**: [What was decided]
- **Rationale**: [Why this approach]
- **Alternatives considered**: [Other options]
- **Trade-offs**: [What we gain/lose]

**Decision 2**: [Continue for key decisions]

### Assumptions

- [Assumption 1 about input data]
- [Assumption 2 about environment]
- [Assumption 3 about user expertise]

### Future Enhancements

- [Potential improvement 1]
- [Potential improvement 2]

### References

- [Design pattern documentation]
- [Technology documentation links]
- [Related systems or prior art]

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial design | [Name] |
