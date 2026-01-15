---
name: generate-tech-spec-from-code
description: Create comprehensive technical specifications by analyzing existing codebases. Fast breadth analysis covering all essential aspects for all technical stakeholders (developers, SRE, testers, architects).
license: Apache-2.0
metadata:
  olaf_tags: [documentation, technical-spec, code-analysis, reverse-engineering, breadth-analysis]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **application_name**: string - Name of the application
- **code_path**: string - Path to the codebase
- **tech_stack**: array[string] - Technologies used in the application
- **key_components**: array[string] - Main components (e.g., ["frontend", "backend", "database"])
- **existing_docs**: array[string] - (Optional) Paths to any existing documentation

## Process

**BREADTH ANALYSIS - Fast & Comprehensive Coverage**
1. **System Overview Extraction**:
   - Technology stack identification (frameworks, databases, build tools)
   - Core component discovery and relationships
   - API endpoint catalog extraction
   - Database schema overview
   - Configuration and deployment approach
2. **Architecture Documentation**:
   - High-level system architecture
   - Component interaction patterns
   - Security mechanisms overview
   - Integration points identification
   - Deployment and infrastructure setup
3. **Quality & Risk Assessment**:
   - Technical debt identification (surface-level)
   - Security considerations overview
   - Performance characteristics assessment
   - Modernization opportunities identification
   - Risk factors documentation
4. **Stakeholder Deliverable Creation**:
   - Comprehensive 12-section technical specification
   - Readable by all technical personas (developer, SRE, tester, architect)
   - Foundation for deeper persona-specific analysis
   - Actionable modernization recommendations

## Output/Result Format

Follow template structure: `templates/developer/specification-template.md`

**Save Output**: Create file `.olaf/work/staging/specs/tech-spec-{application_name}-YYYYMMDD-NNN.md` where:
- {application_name} is the kebab-case formatted application name
- YYYYMMDD is the current date
- NNN is a sequential number (001, 002, etc.)

## Output to USER
1. **Technical Specification Document**:
   - 12-section comprehensive overview covering all technical aspects
   - Readable by all technical stakeholders (developers, SRE, testers, architects)
   - Foundation for deeper analysis by specific personas
   - Includes architecture, API, database, security, deployment overview
2. **Next Steps Guidance**:
   - Recommendation for persona-specific deep-dive analysis
   - Available deep-dive competencies:
     - Developer: `deepen-tech-spec-developer` (code quality, unit testing, architecture patterns)
     - SRE: `deepen-tech-spec-sre` (infrastructure, monitoring, deployment)
     - Tester: `deepen-tech-spec-tester` (integration testing, test architecture)
     - Architect: `deepen-tech-spec-architect` (system design, integration patterns)
   - Code quality assessment: `assess-code-quality-principles` (SOLID, DRY, testing practices)

## Domain-Specific Rules
- Rule 1: Document all user roles and permissions
- Rule 2: Include detailed workflow diagrams
- Rule 3: Document all external dependencies
- Rule 4: Provide code examples for key features
- Rule 5: Include security considerations

## Required Actions
1. Analyze codebase structure
2. Document features and workflows
3. Create technical documentation
4. Generate architecture diagrams
5. Compile modernization recommendations

⚠️ **Critical Notes**
- Never expose sensitive information
- Validate all code examples
- Maintain version control of specifications
- Document assumptions and limitations
- Keep documentation in sync with code

