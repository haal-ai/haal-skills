---
task_id: "identify-application-type"
task_name: "Identify Application Type"
dependencies: ["context.specification_file"]
conditions: []
---

# Identify Application Type

## Input Context
**Required Context Variables**: 
- `context.specification_file`: Path to EARS specification

## Task Instructions

### 1. Load Specification
Read `${specification_file}` to understand what system is being designed.

### 2. Analyze Characteristics

Look for indicators of application type:

**ETL / Data Pipeline**:
- Keywords: extract, transform, load, data processing, pipeline, aggregation
- Requirements mention moving data between systems
- Focus on data transformation and quality

**Frontend Application**:
- Keywords: user interface, UI, components, views, pages, forms
- Requirements describe user interactions and visual elements
- Focus on user experience

**Backend API**:
- Keywords: API, endpoints, REST, GraphQL, services, requests
- Requirements describe data operations and business logic
- Focus on request handling and responses

**CLI Tool**:
- Keywords: command-line, CLI, terminal, commands, arguments
- Requirements describe command-based interactions
- Focus on terminal operations

**Pure Data Analysis**:
- Keywords: analyze, report, metrics, insights, statistics
- Requirements focus on understanding existing data
- No data creation, only interpretation

**Event-Driven System**:
- Keywords: events, listeners, triggers, notifications, webhooks
- Requirements describe reacting to occurrences
- Focus on asynchronous processing

**Batch Processing**:
- Keywords: batch, scheduled, periodic, bulk, jobs
- Requirements mention processing large volumes
- Focus on scheduled execution

**Microservice**:
- Keywords: service, single responsibility, domain-specific
- Requirements define narrow scope within larger system
- Focus on specific business capability

### 3. Classify Application

Based on analysis, set:
- `application_type`: One of [etl, frontend, backend-api, cli-tool, data-analysis, event-driven, batch-processing, microservice]
- `confidence_level`: high | medium | low
- `type_rationale`: Brief explanation of why this type was chosen

### 4. Identify Pattern Match

Map application type to design pattern:
- **etl, data-analysis, batch-processing** → Pattern 1: ETL / Data Pipeline
- **backend-api, microservice** → Pattern 2: Request-Response Service
- **cli-tool, event-driven** → Pattern 3: Workflow Orchestration
- **frontend** → Pattern 4: Component-Based Frontend
- **iterative systems** → Pattern 5: Iterative Refinement

Set:
- `selected_pattern`: Pattern number and name
- `expected_layers`: Estimated number of layers (3-5)

## Output Requirements

**State Updates**:
- `context.application_type`: Identified type
- `context.confidence_level`: Classification confidence
- `context.type_rationale`: Reasoning
- `context.selected_pattern`: Chosen design pattern
- `context.expected_layers`: Number of layers to design
- `task_status.identify-application-type`: "completed"

**User Display**:
```
🔍 Application Type Identified

Type: [application_type]
Confidence: [confidence_level]
Rationale: [type_rationale]

📐 Selected Pattern: [selected_pattern]
Expected Layers: [expected_layers]
```
