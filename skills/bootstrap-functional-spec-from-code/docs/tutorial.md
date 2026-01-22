# Tutorial: bootstrap-functional-spec-from-code

## Introduction

This tutorial guides you through using the `bootstrap-functional-spec-from-code` skill to analyze source code and generate a functional specification document. The skill extracts business logic and user-facing functionality from code to create documentation suitable for business stakeholders.

## Prerequisites

Before starting, ensure you have:

- [ ] Access to the source code you want to analyze
- [ ] The codebase is accessible from your workspace
- [ ] Understanding of the application's general purpose
- [ ] Write access to `.olaf/work/staging/functional-specifications/`

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Start by invoking the skill with the source path:

```
@bootstrap-functional-spec-from-code source_path=src/
```

Or invoke without parameters for interactive mode:

```
@bootstrap-functional-spec-from-code
```

### Step 2: Provide Source Path

If not provided, the skill will ask:

```
Please provide the path to the application's source code:
```

Enter the path to your codebase:

```
src/main/java/com/example/myapp
```

### Step 3: Select Detail Level (Optional)

Choose the level of detail for the specification:

```
Select detail level:
1. overview - High-level summary only
2. standard - Balanced detail (default)
3. detailed - Comprehensive documentation
```

### Step 4: Review Initial Analysis

The skill analyzes your codebase and presents findings:

```
Codebase Analysis Complete
==========================

Directory Structure:
- 45 source files identified
- 3 main packages detected
- 12 entry points found

Key Components:
- UserController - User management endpoints
- OrderService - Order processing logic
- PaymentGateway - Payment integration

Business Processes:
- User registration and authentication
- Order creation and management
- Payment processing workflow
```

### Step 5: Review Identified Business Logic

The skill extracts business rules:

```
Business Logic Extracted
========================

Core Business Rules:
1. Users must verify email before placing orders
2. Orders over $1000 require manager approval
3. Payments are processed through Stripe integration
4. Refunds allowed within 30 days of purchase

User Flows:
1. Registration → Email Verification → Login
2. Browse Products → Add to Cart → Checkout → Payment
3. View Orders → Request Refund → Approval → Processing
```

### Step 6: Review Draft Specification

The skill generates the specification document:

```
Draft Specification Generated
=============================

File: .olaf/work/staging/functional-specifications/FunctionalSpec-20240115-001.md

Sections Created:
✓ Executive Summary
✓ Functional Requirements
✓ User Stories
✓ Data Models
✓ Integration Points
✓ Business Rules
✓ Appendices
```

### Step 7: Interactive Q&A

The skill may ask clarifying questions:

```
Clarification Needed:
1. The PaymentGateway references both Stripe and PayPal. 
   Which is the primary payment processor?

2. The OrderService has a "priority" field. What determines 
   order priority?
```

Provide answers to improve specification accuracy:

```
1. Stripe is primary, PayPal is fallback
2. Priority is based on customer tier: Gold > Silver > Bronze
```

### Step 8: Validate Against Source

The skill validates the specification:

```
Validation Results
==================
✓ All identified components documented
✓ Business rules traced to source code
✓ User flows match code paths
⚠ 2 assumptions made (see Appendix A)

Confidence Level: High (92%)
```

### Step 9: Review Final Output

Open and review the generated specification:

```
.olaf/work/staging/functional-specifications/FunctionalSpec-20240115-001.md
```

The document includes:
- Executive summary for stakeholders
- Detailed functional requirements
- User stories with acceptance criteria
- Data model documentation
- Integration point descriptions
- Traceability to source code

## Verification Checklist

After generation, verify:

- [ ] Specification file created in staging directory
- [ ] Executive summary accurately describes the application
- [ ] All major features are documented
- [ ] Business rules are correctly captured
- [ ] User flows match actual application behavior
- [ ] Data models reflect code structure
- [ ] Assumptions are clearly documented

## Troubleshooting

### Source Path Not Found

**Symptom**: Error "Cannot access source path"

**Cause**: Invalid or inaccessible path

**Solution**:
1. Verify the path exists
2. Use relative path from workspace root
3. Check file permissions

### Incomplete Analysis

**Symptom**: Missing components in analysis

**Cause**: Complex or non-standard code structure

**Solution**:
1. Provide more specific source path
2. Use `detail_level=detailed` for deeper analysis
3. Answer clarifying questions thoroughly

### Low Confidence Score

**Symptom**: Confidence level below 70%

**Cause**: Ambiguous code or missing documentation

**Solution**:
1. Review the assumptions section
2. Provide clarifications for uncertain areas
3. Consider adding code comments and re-running

### Business Logic Misinterpretation

**Symptom**: Incorrect business rules in specification

**Cause**: Code doesn't clearly express business intent

**Solution**:
1. Use the interactive Q&A to correct misunderstandings
2. Provide additional context about business rules
3. Review and manually edit the specification

### Large Codebase Timeout

**Symptom**: Analysis takes too long or times out

**Cause**: Very large codebase

**Solution**:
1. Analyze specific modules separately
2. Use `detail_level=overview` first
3. Focus on specific packages: `source_path=src/main/java/com/example/core`

## Output Format Options

### Markdown (Default)

```
@bootstrap-functional-spec-from-code source_path=src/ output_format=markdown
```

Standard markdown format, best for version control and editing.

### HTML

```
@bootstrap-functional-spec-from-code source_path=src/ output_format=html
```

Formatted HTML for web viewing and sharing.

### PDF

```
@bootstrap-functional-spec-from-code source_path=src/ output_format=pdf
```

PDF format for formal documentation and distribution.

## Next Steps

After generating the specification:

1. **Review with stakeholders** - Share the specification for feedback
2. **Iterate and refine** - Update based on feedback
3. **Maintain traceability** - Keep specification updated as code changes
4. **Use for planning** - Reference for feature planning and estimation
5. **Generate technical spec** - Use `generate-tech-spec-from-code` for developer documentation
