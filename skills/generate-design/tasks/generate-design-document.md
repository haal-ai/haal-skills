---
task_id: "generate-design-document"
task_name: "Generate Design Document"
dependencies: ["context.layer_definitions", "context.task_breakdown", "context.output_file"]
conditions: []
---

# Generate Design Document

## Input Context
**Required Context Variables**: 
- `context.application_type`: Application type
- `context.selected_pattern`: Design pattern used
- `context.layer_definitions[]`: Complete layer architecture
- `context.task_breakdown[]`: Task definitions
- `context.architecture_diagram`: ASCII diagram
- `context.output_file`: Path to save design document

**Required Files**:
- `templates/design-document-template.md`

## Task Instructions

### 1. Load Template
Read design document template.

### 2. Populate Document Sections

**Header**:
- Extract system name from specification
- Set version to 1.0
- Set date to current timestamp

**Overview**:
- Brief system description
- Application type
- Key stakeholders

**Architecture Diagram**:
- Insert `${architecture_diagram}` ASCII art

**Layer Definitions**:
For each layer in `${layer_definitions}`:
- Layer name and purpose
- Input/output interfaces with examples
- Processing description
- Technology choice and rationale
- Quality validation
- Execution time estimate

**Interface Contracts**:
For each layer boundary:
- File format specification
- Required and optional fields
- Example data structures
- Validation rules

**Task Breakdown**:
For each task in `${task_breakdown}`:
- Task ID and name
- Layer association
- Input requirements
- Processing description
- Output artifacts
- Dependencies
- Implementation approach (AI/Script/Manual/Hybrid)

**Data Flow Diagram**:
- Show complete flow from input to output
- Highlight transformations at each layer

**Quality Gates**:
- Validation checkpoints per layer
- Gap detection strategy
- Error handling approach

**Technology Stack**:
- List technologies per layer
- Rationale for each choice

**Execution Timeline**:
- Total estimated time
- Critical path tasks
- Parallel execution opportunities

**Appendix**:
- Design decisions and rationale
- Assumptions
- Future enhancements
- References

### 3. Apply Application-Specific Guidance

**For ETL/Data Pipeline**:
- Emphasize data validation between layers
- Include data quality metrics
- Show transformation rules

**For Backend API**:
- Include API endpoint definitions
- Show request/response schemas
- Document error codes

**For Frontend**:
- Include component hierarchy
- Show state management flow
- Document UI/UX patterns

**For CLI Tool**:
- Include command syntax
- Show argument parsing
- Document output formats

### 4. Write Document
Save complete design to `${output_file}`.

## Output Requirements

**State Updates**:
- `context.design_document_path`: Path to created file
- `context.design_complete`: true
- `task_status.generate-design-document`: "completed"

**User Display**:
```
✅ Design Document Generated

File: ${output_file}
Size: [file size]
Sections: [count]

Summary:
- Application Type: [type]
- Pattern: [pattern]
- Layers: [count]
- Tasks: [count]
- Estimated Time: [total]
```

**File Output**: `${output_file}` - Complete design document in Markdown format
