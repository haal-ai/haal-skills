---
name: generate-spec-from-dfd
description: Transform DFD analysis into a precise, developer-implementable functional specification
license: Apache-2.0
metadata:
  olaf_tags: [specification, dfd, functional-spec, documentation, developer]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

if you are in need to get the date and time, use time tools, fallback to shell command if needed

# Generate Functional Specification from DFD Analysis

## Objective

Transform any existing DFD analysis into a precise, developer-implementable functional specification. Use the DFD documentation as the primary source, then examine the actual codebase only to replace vague terms with exact values and confirm technical details.

## Input Parameters

**IMPORTANT**: When parameters are not provided, ask the USER for them.

1. **dfd_analysis_path**: string - Path to DFD analysis files (REQUIRED)
   - Look for `{project}_analysis.md` as primary source
   - Also check for `DFD_level1_tasks.md`, `DFD_level2_tasks.md`
2. **source_path**: string - Path to source code for confirmation (REQUIRED)
3. **output_file**: string - Path for functional specification output (default: `functional_spec.md` in DFD directory)
4. **project_name**: string - Name identifier for the project (REQUIRED)

## Primary Input Sources (In Order)

1. **DFD Analysis File** (`{project}_analysis.md`) - Primary source for system understanding
2. **DFD Executive Summary** (if available) - Business context and value proposition
3. **DFD Level 1 and Level 2 task files** - Process decomposition details
4. **Actual codebase** - Only for confirming exact values, versions, and patterns

## Process

### Step 1: Extract Business Requirements from DFD Context

**From Context Diagram:**
- Identify all external entities and their exact roles
- Map each data flow to specific functional requirements
- Define system boundary precisely based on DFD scope

**Required Output Format:**
```markdown
### Business Context (from DFD Analysis)
**System Purpose:** [Extract exact purpose from DFD documentation]
**External Entities:** [List all entities from Context Diagram with roles]
**Primary Data Flows:** [List all flows from Context Diagram]
**System Boundary:** [Define what is inside vs outside the system]
```

### Step 2: Convert Level 1 Processes to Functional Requirements

**From Level 1 DFD:**
- Each process → One functional requirement (FR-N)
- Process inputs → Interface requirements
- Process outputs → Output specifications
- Process purpose → Functional behavior

**Required Mapping:**
```
P[N]: [Process Name] → FR-[N]: [Functional Requirement Name]
```

**Template for each process:**
```markdown
### FR-[N]: [Process Name from Level 1 DFD]
**Source Process:** [Level 1 Process ID and name]
**Requirement:** The system SHALL [exact function from DFD process description]

**Inputs (from DFD):**
- [List exact data flows entering this process]

**Outputs (from DFD):**
- [List exact data flows leaving this process]

**Implementation Requirements (from codebase confirmation):**
- [Specific libraries/frameworks with exact versions]
- [Exact algorithms/methods from code]
- [Performance constraints from code]

**Level 2 Decomposition (if applicable):**
- [Sub-processes from Level 2 DFD with exact specifications]
```

### Step 3: Use Level 2 DFD for Implementation Details

**From Level 2 Decomposition (if available):**
- Sub-processes → Specific technical requirements
- Internal data flows → Data transformation specifications
- Internal data stores → Storage requirements

### Step 4: Replace Vague Terms with Codebase Facts

**Only after DFD analysis, examine codebase to replace:**
- "multiple [items]" → Count exact number from actual implementation
- "various [types]" → List exact types from codebase
- "appropriate [values]" → Find actual values in code
- "reasonable [limits]" → Extract actual limits from implementation

## Precision Requirements

### Eliminate Vague Language

**Prohibited Words:** "etc.", "various", "multiple", "some", "many", "appropriate", "suitable", "around", "approximately"

**Replacement Rules:**
- "supports various technologies" → "supports exactly [N] technologies: [complete list]"
- "handles multiple formats" → "processes exactly [N] file formats: [.ext1, .ext2, ...]"
- "reasonable timeout" → "maximum [N] seconds timeout"
- "good performance" → "completes analysis within [N] seconds for repositories up to [size]"

### Exact Specifications Required

- **Version numbers:** From requirements/dependencies (Flask==2.1.2, not Flask 2.x)
- **File patterns:** From actual code (exact patterns, not "patterns")
- **API endpoints:** From source (exact paths and methods)
- **Error codes:** From actual error handling code
- **Performance metrics:** From actual implementation

## Document Structure Requirements

### 1. Executive Summary (from DFD Analysis)
- System purpose (exact text from DFD analysis)
- External entity definitions (all entities from Context Diagram)
- Primary data flows (mapped from Context Diagram)
- Business value proposition

### 2. Functional Requirements (from Level 1 DFD)
- One FR per Level 1 process
- Complete input/output specifications
- Implementation requirements from codebase

### 3. Data Store Specifications (from DFD Data Stores)
- Storage requirements and format specifications

### 4. External Interface Specifications (from Context Diagram)
- Interface specifications per external entity

### 5. Non-Functional Requirements
- Performance (from process complexity)
- Security (from security-related processes)
- Quality requirements

## Quality Assurance Checklist

### DFD Traceability Validation
- [ ] Every Level 1 process mapped to a functional requirement
- [ ] Every data flow mapped to an interface specification
- [ ] Every data store mapped to storage requirements
- [ ] Every external entity mapped to interface requirements
- [ ] All Level 2 sub-processes included in implementation details

### Precision Validation
- [ ] No "etc." or "various" - all lists complete and exact
- [ ] No approximations - all measurements precise
- [ ] No subjective terms - all criteria measurable
- [ ] All version numbers exact (from dependency files)
- [ ] All patterns specific (from actual implementation code)

### Developer Usability Check
- [ ] Requirements implementable without clarification
- [ ] All technical specifications include exact tools/versions
- [ ] Performance requirements measurable and testable
- [ ] Error conditions and responses specified
- [ ] Interface specifications complete with data formats

## Output

The generated functional specification must enable a developer to:
1. **Implement the complete system** without additional requirements gathering
2. **Write comprehensive tests** using the provided acceptance criteria
3. **Validate system behavior** against specific measurable requirements
4. **Deploy the system** using exact dependency and configuration specifications
5. **Troubleshoot issues** using specific error codes and logging requirements

## Integration

This skill is typically used after `generate-dfd-from-code` completes. It takes the DFD artifacts as input and produces a developer-ready functional specification.

**Typical workflow:**
1. `generate-dfd-from-code` → Creates DFD analysis
2. `generate-spec-from-dfd` → Creates functional specification (this skill)
3. `plan-rewrite-from-spec` → Creates implementation plan (optional)

---

**Skill Type:** Documentation Generation
**Framework:** OLAF Specification Generation
**Prerequisites:** Completed DFD analysis from `generate-dfd-from-code`
