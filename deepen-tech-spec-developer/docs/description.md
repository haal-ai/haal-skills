# deepen-tech-spec-developer

## Overview

The `deepen-tech-spec-developer` skill performs deep-dive technical analysis focused on developer concerns including code quality, unit testing, architecture patterns, and design principles. It creates comprehensive, evidence-based documentation organized into focused chapters.

## Purpose

This skill helps development teams understand and document the technical implementation details of their applications. It provides actionable insights into code quality, testing practices, and architectural decisions with evidence linked directly to source code.

## Key Features

- **Evidence-Based Analysis**: Every claim includes source links and code snippets
- **Chapter Organization**: Documentation split into focused, manageable chapters
- **Developer Focus**: Covers code quality, testing, architecture, and dependencies
- **Session Management**: Supports multi-session work with carry-over capability
- **Interactive Review**: User approval required after each chapter
- **Thoroughness Priority**: Prioritizes completeness over brevity

## Usage

Invoke with required parameters:

```
@deepen-tech-spec-developer tech_spec_path=docs/tech-spec.md application_name=my-service
```

Resume from specific chapter:

```
@deepen-tech-spec-developer tech_spec_path=docs/tech-spec.md application_name=my-service chapter_focus="Unit Testing"
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tech_spec_path | string | Yes | Path to existing technical specification file |
| application_name | string | Yes | Application name in kebab-case format |
| chapter_focus | string | No | Specific chapter to start with |

## Chapter Structure

The documentation is organized into 6 developer-focused chapters:

### Chapter 1: Architecture & Design Patterns Assessment
- Design pattern usage (Factory, Singleton, Observer, etc.)
- SOLID principles adherence with violation examples
- Component coupling analysis
- Code organization assessment
- Performance implications

### Chapter 2: API Implementation Quality Analysis
- Endpoint implementation review
- Error handling assessment
- Validation strategy evaluation
- Security implementation
- Documentation quality

### Chapter 3: Data Access & Transaction Management
- ORM pattern analysis
- Transaction boundary assessment
- Connection management
- Query optimization
- Database integration

### Chapter 4: Error Handling & Exception Strategy
- Exception hierarchy evaluation
- Logging strategy assessment
- Debugging capabilities
- Error recovery patterns
- Monitoring integration

### Chapter 5: Unit Testing & Code Quality Evaluation
- Test coverage analysis
- Test quality assessment
- Testing patterns
- TDD practices
- Edge case coverage

### Chapter 6: Module Dependencies & Structure Assessment
- Dependency injection evaluation
- Module boundaries
- Coupling analysis
- Configuration management
- Build process assessment

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEEP-DIVE WORKFLOW                           │
├─────────────────────────────────────────────────────────────────┤
│ 1. Validation Phase                                             │
│    - Verify tech spec file exists                               │
│    - Validate application name format                           │
│    - Check for existing chapter files                           │
│    ↓                                                            │
│ 2. Tech Spec Analysis                                           │
│    - Extract architecture details                               │
│    - Identify key components                                    │
│    - Map technology stack                                       │
│    ↓                                                            │
│ 3. Chapter Planning                                             │
│    - Present chapter outline                                    │
│    - Get user approval (Propose-Confirm-Act)                    │
│    ↓                                                            │
│ 4. Chapter Development Cycle (for each chapter)                 │
│    a. Deep Analysis - Extract technical information             │
│    b. Documentation - Create chapter with examples              │
│    c. User Review - Present and get feedback                    │
│    d. Session Management - Offer session transition             │
│    ↓                                                            │
│ 5. Completion                                                   │
│    - All chapters documented                                    │
│    - Cross-references validated                                 │
│    - Summary provided                                           │
└─────────────────────────────────────────────────────────────────┘
```

## Output

Chapter files are saved to:
`.olaf/work/staging/specs/deep-dive-{application_name}-chapter-{N}-{chapter-name}-YYYYMMDD-NNN.md`

### Chapter Template Structure

```markdown
# Chapter {N}: {Chapter Title} - {Application Name}

## Chapter Overview
- Purpose and scope
- Key topics covered
- Prerequisites

## Detailed Analysis
[Evidence-based technical analysis]

## Implementation Details
[Code examples with source links]

## Best Practices
[Recommendations and guidelines]

## Common Issues & Solutions
[Troubleshooting guidance]

## References & Further Reading
[Additional resources]
```

## Evidence Requirements

Every non-trivial claim must include:

- **Source**: Concrete artifact (code/config/spec/test)
- **Location**: Link to exact file with line range
- **Snippet**: Short quoted identifier for verification

```
Example:
Claim: "OrderService uses constructor injection"
Source: src/main/java/com/example/OrderService.java
Location: Lines 15-20
Snippet: `public OrderService(OrderRepository repo, PaymentClient client)`
```

## Examples

### Example 1: Starting Deep-Dive Analysis

```
User: @deepen-tech-spec-developer tech_spec_path=docs/tech-spec.md 
      application_name=order-service

Agent:
Tech Spec Analysis Complete
===========================
Application: order-service
Architecture: Spring Boot Microservice
Components: 12 identified

Proposed Chapter Structure:
1. Architecture & Design Patterns Assessment
2. API Implementation Quality Analysis
[...]

Do you approve this chapter structure?
```

### Example 2: Chapter Completion with Session Break

```
Agent:
Chapter 1 complete and approved.

Would you like to continue with the next chapter in a new session?

User: yes

Agent:
Carry-over note created.
Please start your next session with 'carry-on' to continue 
with Chapter 2: API Implementation Quality Analysis.
```

## Domain-Specific Rules

- Always analyze actual code, not just spec content
- Include practical examples with validation
- Provide actionable recommendations
- Execute user review after each chapter
- Offer session transition after chapter completion
- Every claim must include evidence with source links
- Prefer completeness over concision

## Error Handling

| Error Condition | Handling |
|----------------|----------|
| Missing tech spec file | Request correct path |
| Invalid application name | Request kebab-case format |
| File access issues | Offer alternatives or manual input |
| Chapter generation failure | Provide fallback manual steps |
| Carry-over failure | Offer manual state documentation |

## Related Skills

- `generate-tech-spec-from-code` - Generate initial technical specification
- `bootstrap-functional-spec-from-code` - Generate functional specification
- `analyze-function-complexity` - Analyze code complexity metrics
- `carry-over-session` - Save session state for continuation
