---
task_id: "analyze-specification"
task_name: "Analyze EARS Specification"
dependencies: ["context.specification_file"]
conditions: []
---

# Analyze EARS Specification

## Input Context
**Required Context Variables**: 
- `context.specification_file`: Path to EARS specification document (from Phase 2: `specification.md`)

**Expected File Format**:
The specification file should be the final consolidated output from transform-raw-spec (Phase 2),
containing:
- Complete EARS requirements (all domains)
- Integrated decisions from Steps 3-5
- Application type identification
- Architecture patterns suggestions
- Testability framework summary

## Task Instructions

### 1. Load Specification
Read complete `${specification_file}` (typically `specification.md` from ESDI Phase 2 output folder).

### 2. Extract Requirements

Identify and categorize:

**Functional Requirements** (what system must do):
- System SHALL statements
- Feature descriptions
- Capabilities and operations

**Quality Attributes**:
- Performance requirements (response time, throughput)
- Reliability needs (uptime, error handling)
- Security constraints (authentication, authorization)
- Scalability needs (concurrent users, data volume)

**Constraints**:
- Technology limitations
- Time/budget restrictions
- Resource availability
- Integration requirements

**Stakeholders & Personas**:
- Who will use the system
- What are their goals
- What are their pain points

### 3. Identify Data Flow Characteristics

Determine:
- **Data sources**: Where does data come from?
- **Data transformations**: How is data changed?
- **Data destinations**: Where does data go?
- **Data volume**: Small/medium/large datasets
- **Processing frequency**: Real-time/batch/scheduled

### 4. Determine Interaction Model

Classify:
- **Synchronous**: Request → Response (APIs, queries)
- **Asynchronous**: Events → Handlers (event processing)
- **Batch**: Scheduled jobs → Outputs (periodic processing)
- **Interactive**: User actions → System responses (UI)

### 5. Assess Complexity

Evaluate:
- **Simple**: Single concern, straightforward flow (3 layers)
- **Moderate**: Multiple concerns, some branching (4 layers)
- **Complex**: Many concerns, conditional flows (5+ layers)

## Output Requirements

**State Updates**:
- `context.functional_requirements[]`: List of key functional requirements
- `context.quality_attributes[]`: Performance, reliability, security needs
- `context.constraints[]`: Limitations and restrictions
- `context.stakeholders[]`: User personas
- `context.data_flow_type`: pipeline | request-response | event-driven | batch
- `context.interaction_model`: sync | async | batch | interactive
- `context.complexity_level`: simple | moderate | complex
- `task_status.analyze-specification`: "completed"

**User Display**:
```
📋 Specification Analysis Complete

Key Requirements: [count] functional, [count] quality attributes
Data Flow: [data_flow_type]
Interaction: [interaction_model]
Complexity: [complexity_level]
```
