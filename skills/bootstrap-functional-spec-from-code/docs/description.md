# bootstrap-functional-spec-from-code

## Overview

The `bootstrap-functional-spec-from-code` skill analyzes source code to extract and describe functionalities from a business and user perspective. It creates a draft functional specification document that bridges the gap between technical implementation and business requirements.

## Purpose

This skill enables teams to generate business-focused documentation from existing codebases. It's particularly useful for legacy systems lacking documentation, onboarding new team members, or creating specifications for stakeholder communication.

## Key Features

- **Code Analysis**: Scans directory structure, identifies entry points, and extracts business logic
- **Business Logic Extraction**: Identifies core business rules, user flows, and system boundaries
- **Specification Generation**: Creates structured documentation using business-friendly language
- **Traceability**: Maintains links between specification and source code
- **Interactive Refinement**: Supports Q&A for clarification and validation

## Usage

Invoke with source path:

```
@bootstrap-functional-spec-from-code source_path=src/main/java
```

With optional parameters:

```
@bootstrap-functional-spec-from-code source_path=src/ output_format=markdown detail_level=detailed
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| source_path | string | Yes | Path to the application's source code directory |
| output_format | enum | No | Output format: markdown, html, pdf (default: markdown) |
| detail_level | enum | No | Level of detail: overview, standard, detailed (default: standard) |

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPECIFICATION GENERATION                     │
├─────────────────────────────────────────────────────────────────┤
│ 1. Code Analysis                                                │
│    - Scan directory structure                                   │
│    - Identify entry points and main components                  │
│    - Extract business logic and workflows                       │
│    - Document data models and relationships                     │
│    ↓                                                            │
│ 2. Business Logic Extraction                                    │
│    - Identify core business rules                               │
│    - Map out user flows                                         │
│    - Document system boundaries                                 │
│    - Identify external integrations                             │
│    ↓                                                            │
│ 3. Specification Generation                                     │
│    - Use functional specification template                      │
│    - Structure content for business audience                    │
│    - Include relevant code examples                             │
│    - Add visual diagrams where helpful                          │
│    ↓                                                            │
│ 4. Review & Refinement                                          │
│    - Interactive Q&A for clarification                          │
│    - Validation against source code                             │
│    - Version control integration                                │
└─────────────────────────────────────────────────────────────────┘
```

## Output

The skill generates a functional specification document saved to:
`.olaf/work/staging/functional-specifications/FunctionalSpec-YYYYMMDD-NNN.md`

### Document Structure

1. **Executive Summary** - High-level overview for stakeholders
2. **Functional Requirements** - Detailed feature descriptions
3. **User Stories** - User-centric requirement descriptions
4. **Data Models** - Business entity descriptions
5. **Integration Points** - External system connections
6. **Business Rules** - Core business logic documentation
7. **Appendices** - Technical details and assumptions

## Examples

### Example 1: Basic Analysis

```
User: @bootstrap-functional-spec-from-code source_path=src/

Agent:
Codebase Analysis Complete
==========================
- 45 source files identified
- 3 main packages detected
- 12 entry points found

Key Components:
- UserController - User management
- OrderService - Order processing
- PaymentGateway - Payment integration

Generating specification...

File created: .olaf/work/staging/functional-specifications/FunctionalSpec-20240115-001.md
```

### Example 2: Detailed Analysis with Q&A

```
User: @bootstrap-functional-spec-from-code source_path=src/ detail_level=detailed

Agent:
[Analysis output...]

Clarification Needed:
1. The OrderService has approval logic. What triggers approval requirements?
2. Multiple payment providers found. Which is primary?

User: 
1. Orders over $1000 need approval
2. Stripe is primary, PayPal is backup

Agent:
Thank you. Updating specification with clarifications...

Specification generated with 95% confidence.
```

## Domain-Specific Rules

- **Read-Only**: Never modifies source code
- **Business Focus**: Uses business-friendly language, avoids technical jargon
- **Traceability**: Includes references to source code locations
- **Consistency**: Uses consistent terminology throughout
- **Maintainability**: Structures for easy updates

## Error Handling

| Error Condition | Handling |
|----------------|----------|
| Invalid source path | Request correct path from user |
| Unreadable files | Skip and report, continue analysis |
| Complex code patterns | Document assumptions, ask for clarification |
| Missing entry points | Analyze available code, note limitations |

## Critical Notes

- Never modifies source code
- Maintains clear audit trail of analysis
- Includes confidence levels for extracted information
- Documents all assumptions made during analysis
- Supports incremental updates for evolving codebases

## Related Skills

- `generate-tech-spec-from-code` - Generate technical specifications
- `deepen-tech-spec-developer` - Deep-dive technical analysis
- `analyze-spec-vs-code` - Compare specifications against code
