# Tutorial: deepen-tech-spec-developer

## Introduction

This tutorial guides you through using the `deepen-tech-spec-developer` skill to create comprehensive deep-dive technical documentation focused on developer concerns. The skill analyzes code quality, architecture patterns, testing practices, and provides evidence-based assessments.

## Prerequisites

Before starting, ensure you have:

- [ ] An existing technical specification file
- [ ] Access to the application's source code
- [ ] Application name in kebab-case format
- [ ] Write access to `.olaf/work/staging/specs/`

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Start by invoking the skill with required parameters:

```
@deepen-tech-spec-developer tech_spec_path=docs/tech-spec.md application_name=my-application
```

Or invoke for interactive parameter collection:

```
@deepen-tech-spec-developer
```

### Step 2: Provide Required Parameters

If not provided, the skill will request:

```
Please provide the following:
1. Path to existing technical specification file:
2. Application name (kebab-case):
```

Enter the values:

```
1. docs/technical-specification.md
2. order-management-service
```

### Step 3: Review Tech Spec Analysis

The skill analyzes your existing specification:

```
Tech Spec Analysis Complete
===========================

Application: order-management-service
Architecture: Microservices with Spring Boot
Technology Stack:
- Java 17
- Spring Boot 3.x
- PostgreSQL
- Redis Cache
- RabbitMQ

Key Components Identified:
- OrderController
- OrderService
- PaymentIntegration
- InventoryClient
```

### Step 4: Review Chapter Outline

The skill presents the chapter structure for approval:

```
Proposed Chapter Structure
==========================

1. Architecture & Design Patterns Assessment
2. API Implementation Quality Analysis
3. Data Access & Transaction Management
4. Error Handling & Exception Strategy
5. Unit Testing & Code Quality Evaluation
6. Module Dependencies & Structure Assessment

Do you approve this chapter structure? (yes/no/modify)
```

Approve or request modifications:

```
yes
```

### Step 5: Chapter Development Cycle

For each chapter, the skill follows this cycle:

#### 5a. Deep Analysis

```
Analyzing Chapter 1: Architecture & Design Patterns Assessment
==============================================================

Scanning codebase for:
- Design pattern implementations
- SOLID principles adherence
- Component coupling relationships
- Code organization patterns
```

#### 5b. Documentation Generation

```
Chapter 1 Generated
===================

File: .olaf/work/staging/specs/deep-dive-order-management-service-chapter-01-architecture-design-patterns-20240115-001.md

Sections:
✓ Design Patterns Found (Factory, Repository, Strategy)
✓ SOLID Principles Evaluation
✓ Component Coupling Analysis
✓ Code Organization Assessment
✓ Performance Implications
```

#### 5c. User Review

```
Please review Chapter 1: Architecture & Design Patterns Assessment.

Are you satisfied with the depth and detail? (yes/no/feedback)
```

Provide feedback or approve:

```
yes
```

### Step 6: Session Management Decision

After each chapter, decide on session management:

```
Chapter 1 complete and approved.

Would you like to continue with the next chapter in a new session?
This helps manage memory and ensures optimal performance.

Options:
1. Continue in current session
2. Start new session (recommended for large codebases)
```

#### Option 1: Continue in Current Session

```
1
```

The skill proceeds to Chapter 2 immediately.

#### Option 2: Start New Session

```
2
```

The skill creates a carry-over note:

```
Carry-over note created.

Please start your next session with 'carry-on' to continue 
with Chapter 2: API Implementation Quality Analysis.

Progress saved:
- Application: order-management-service
- Completed: Chapter 1
- Next: Chapter 2
- Files: 1 chapter file created
```

### Step 7: Resume in New Session (if applicable)

In your new session:

```
@carry-on
```

The skill resumes from where you left off:

```
Resuming deep-dive documentation for: order-management-service

Progress:
✓ Chapter 1: Architecture & Design Patterns Assessment
→ Chapter 2: API Implementation Quality Analysis (starting)
○ Chapter 3-6: Pending

Continuing with Chapter 2...
```

### Step 8: Complete All Chapters

Repeat the chapter cycle for all 6 chapters:

1. Architecture & Design Patterns Assessment
2. API Implementation Quality Analysis
3. Data Access & Transaction Management
4. Error Handling & Exception Strategy
5. Unit Testing & Code Quality Evaluation
6. Module Dependencies & Structure Assessment

### Step 9: Review Final Documentation

After all chapters are complete:

```
Deep-Dive Documentation Complete
================================

Application: order-management-service
Chapters: 6/6 completed

Files Created:
- deep-dive-order-management-service-chapter-01-architecture-design-patterns-20240115-001.md
- deep-dive-order-management-service-chapter-02-api-implementation-quality-20240115-002.md
- deep-dive-order-management-service-chapter-03-data-access-transaction-20240115-003.md
- deep-dive-order-management-service-chapter-04-error-handling-exception-20240115-004.md
- deep-dive-order-management-service-chapter-05-unit-testing-code-quality-20240115-005.md
- deep-dive-order-management-service-chapter-06-module-dependencies-structure-20240115-006.md

Location: .olaf/work/staging/specs/
```

## Verification Checklist

After completion, verify:

- [ ] All 6 chapter files created
- [ ] Each chapter contains evidence-based analysis
- [ ] Code examples are accurate and functional
- [ ] Source links provided for all claims
- [ ] Recommendations are actionable
- [ ] Cross-references between chapters work

## Troubleshooting

### Tech Spec File Not Found

**Symptom**: Error "Cannot find tech spec file"

**Cause**: Invalid path or file doesn't exist

**Solution**:
1. Verify the file path is correct
2. Use path relative to workspace root
3. Check file permissions

### Invalid Application Name

**Symptom**: Error "Application name must be kebab-case"

**Cause**: Name contains invalid characters

**Solution**: Use lowercase letters and hyphens only:
- ✓ `order-management-service`
- ✗ `OrderManagementService`
- ✗ `order_management_service`

### Low Evidence Quality

**Symptom**: Chapter contains many assumptions

**Cause**: Code doesn't clearly express patterns

**Solution**:
1. Review the assumptions section
2. Provide additional context
3. Point to specific code areas for analysis

### Session Carry-Over Failed

**Symptom**: Cannot resume in new session

**Cause**: Carry-over note not created properly

**Solution**:
1. Check `.olaf/work/staging/` for carry-over files
2. Manually note your progress
3. Restart with `chapter_focus` parameter:
   ```
   @deepen-tech-spec-developer tech_spec_path=docs/tech-spec.md 
   application_name=my-app chapter_focus="API Implementation"
   ```

### Chapter Generation Timeout

**Symptom**: Analysis takes too long

**Cause**: Very large codebase or complex patterns

**Solution**:
1. Use session breaks between chapters
2. Focus on specific modules if possible
3. Accept overview-level analysis for complex areas

## Evidence Requirements

The skill requires evidence for all claims:

```
Example Evidence Format:
========================

Claim: "The OrderService uses the Repository pattern"

Evidence:
- Source: src/main/java/com/example/order/OrderRepository.java
- Location: Lines 15-45
- Snippet: `public interface OrderRepository extends JpaRepository<Order, Long>`
```

If evidence cannot be provided, the claim is marked as an assumption.

## Next Steps

After completing deep-dive documentation:

1. **Share with team** - Distribute chapters to relevant developers
2. **Address findings** - Create tasks for identified issues
3. **Update regularly** - Re-run analysis after major changes
4. **Cross-reference** - Link to functional specifications
5. **Use for onboarding** - Include in developer onboarding materials
