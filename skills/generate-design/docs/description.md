# Generate Design

**Source**: generate-design/skill.md

## Overview

Generate Design is a master coordinator skill that transforms an EARS specification into a layered system design. It executes a 5-task chain with user approval gates to analyze specifications, identify application types, design layer architecture, create task breakdowns, and generate comprehensive design documents.

## Purpose

Creating well-structured system designs from specifications requires systematic analysis and proven architectural patterns. This skill automates the design process by analyzing EARS requirements, selecting appropriate architecture patterns, and generating detailed layer definitions with clear interfaces and responsibilities.

## Usage

**Command**: `generate design`

**When to Use**: Use this skill after completing the specification phase (Phase 2 of ESDI) when you have a formal EARS specification and need to create a system architecture. It's essential for ensuring your design addresses all requirements and follows proven patterns.

## Parameters

### Required Inputs
- **specification_file**: Path to EARS specification document (from Phase 2)
- **output_file**: Path where design document should be saved

### Optional Inputs
- **design_patterns**: Path to design patterns guidance (default: `kb/design-patterns-guidance.md`)
- **system_type**: Hint about system type (auto-detected if not provided)

### Context Requirements
- Access to specification document
- Access to design patterns knowledge base
- Write access for output file

## Output

**Deliverables**:
- Complete design document in markdown format
- Architecture diagrams (ASCII)
- Layer definitions with interfaces
- Task breakdown with implementation approach

**Format**: Structured markdown with diagrams and specifications

## Process Flow

### Task 1: Analyze EARS Specification
- Parse specification document
- Extract functional requirements
- Identify quality attributes and constraints
- Determine data flow type and interaction model

### Task 2: Identify Application Type
- Match system characteristics to patterns
- Select appropriate architecture pattern
- Determine number of layers needed
- User approval gate for user approval

### Task 3: Design Layer Architecture
- Define layer responsibilities
- Specify input/output interfaces
- Select technologies for each layer
- Create architecture diagram

### Task 4: Create Task Breakdown
- Map layers to implementation tasks
- Define dependencies
- Estimate execution time
- Identify parallelizable tasks

### Task 5: Generate Design Document
- Assemble all design elements
- Create comprehensive documentation
- Include quality gates and validation

## Application Types Supported

- **ETL**: Data Pipeline Architecture (5 layers)
- **Frontend**: UI Component Architecture
- **Backend API**: Request-Response Service (3-4 layers)
- **CLI Tool**: Command-Line Architecture
- **Data Analysis**: Analytics Pipeline
- **Event-Driven**: Event Processing Architecture
- **Batch Processing**: Batch Job Architecture
- **Microservice**: Service Mesh Architecture

## Examples

### Example 1: CLI Tool Design

**Input**:
- specification_file: `./output/specification.md`
- output_file: `./output/design.md`

**Output**: 
- Application type: CLI Tool
- 4-layer architecture
- Complete design document with task breakdown

### Example 2: API Service Design

**Input**:
- specification_file: `./specs/api-spec.md`
- output_file: `./designs/api-design.md`
- system_type: `backend-api`

**Output**:
- Request-Response Service pattern
- 3-layer architecture
- API endpoint definitions and data models

## Related Skills

- **transform-raw-spec**: Produces specification.md input (Phase 2)
- **generate-implementation-plan**: Consumes design.md output (Phase 4)
- **esdi-chain**: Orchestrates generate-design as Phase 3

## Tips

1. **Ensure specification quality**: Design quality depends on specification completeness
2. **Review application type**: Verify the detected type matches your intent
3. **Approve architecture early**: Use the user approval gate to confirm direction
4. **Consider multi-language**: Enable language-agnostic design for polyglot projects
5. **Validate interfaces**: Ensure layer interfaces are clearly defined

## Limitations

- Requires formal EARS specification as input
- Application type detection may need manual override
- Complex systems may require multiple design iterations
- Does not generate executable code (deferred to Phase 4)
- ASCII diagrams have limited visual complexity
