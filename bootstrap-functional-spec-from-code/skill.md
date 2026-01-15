---
name: bootstrap-functional-spec-from-code
description: Analyze source code to extract and describe its functionalities from a business and user perspective, creating a draft functional specification.
license: Apache-2.0
metadata:
  olaf_tags: [generation, documentation, analysis, functional-spec]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **source_path**: string - Path to the application's source code or codebase directory
- **output_format**: enum[markdown,html,pdf] - (Optional) Output format (default: markdown)
- **detail_level**: enum[overview,standard,detailed] - (Optional) Level of detail (default: standard)

## Process
1. **Code Analysis**:
   - Scan directory structure
   - Identify entry points and main components
   - Extract business logic and workflows
   - Document data models and relationships
2. **Business Logic Extraction**:
   - Identify core business rules
   - Map out user flows
   - Document system boundaries
   - Identify external integrations
3. **Specification Generation**:
   - Use template: `templates/business-analyst/functional-specification-template.md`
   - Structure content for business audience
   - Include relevant code examples
   - Add visual diagrams where helpful

## Output/Result Format

Use `templates/business-analyst/functional-specification-template.md` to structure the specification:
- Follow the template's sections for consistency
- Save as: `.olaf/work/staging/functional-specifications/FunctionalSpec-YYYYMMDD-NNN.md` where:
- YYYYMMDD is the current date
- NNN is a sequential number (001, 002, etc.)
- Structured markdown document
- Business-focused language ( no technical jargon)
- Technical details in appendices

## Output to USER
1. **Initial Analysis**:
   - Codebase overview
   - Identified components
   - Key business processes
2. **Draft Specification**:
   - Executive summary
   - Functional requirements
   - User stories
   - Data models
   - Integration points
3. **Review & Refinement**:
   - Interactive Q&A
   - Validation against source
   - Version control integration

## Domain-Specific Rules
- Rule 1: Focus on business value and user needs
- Rule 2: Maintain clear separation between technical and business views
- Rule 3: Include traceability to source code
- Rule 4: Use consistent terminology
- Rule 5: Structure for maintainability

## Required Actions
1. Analyze source code structure
2. Extract business logic
3. Generate specification draft
4. Validate against source
5. Save and version output

⚠️ **Critical Notes**
- Never modify source code
- Maintain clear audit trail
- Include confidence levels
- Document assumptions
- Support incremental updates

