---
task_id: "task-4"
task_name: "PR Helper Analysis"
dependencies: []
conditions: []
---

# Task 4: PR Helper Analysis

## Input Context
**Required State Variables**: 
- `context.pr_metadata`: Complete PR metadata object
- `context.pr_title`: PR title
- `context.pr_author`: Author information
**Required Files**: None (using metadata from context)
**Required Tools**: Helper prompt execution, standards analysis

## Task Instructions

### Execute PR-Specific Helper Analysis
**SCOPE**: Apply comprehensive PR standards to metadata ONLY

1. **Load Helper Prompt**:
   - Execute `helpers/review-pr-specificities.md` helper prompt
   - Load comprehensive PR standards from practices directory

2. **Apply Standards Analysis**:
   - **Title Quality**: Action verb, scope, format compliance
   - **Description Assessment**: Purpose, changes, testing, breaking changes
   - **Branch Naming**: Convention compliance, ticket reference
   - **Change Statistics**: Scope assessment, risk evaluation
   - **Workflow Compliance**: Process adherence, approval requirements

3. **Generate Findings**:
   - Classify issues by severity: HIGH/MEDIUM/LOW
   - Focus on process and metadata quality
   - **BOUNDARY**: Metadata analysis only - no code content review

4. **Prepare Assessment**:
   - Document strengths and improvement areas
   - Identify any blocking issues
   - Generate preliminary recommendations

## Output Requirements

**State Updates**:
- `task_outputs.task-4.helper_analysis`: Complete helper analysis results
- `task_outputs.task-4.title_quality`: Assessment of title
- `task_outputs.task-4.description_quality`: Assessment of description
- `task_outputs.task-4.branch_assessment`: Branch naming evaluation
- `task_outputs.task-4.issues_found`: Array of issues by severity
- `task_status.task-4`: "completed"

**Files Created**: None

**Context Passed**: 
- PR metadata quality assessment for final reporting
- Issue classification for recommendation generation
- Process compliance evaluation

## Success Criteria
- Helper analysis successfully executed
- PR standards applied comprehensively
- Issues identified and classified by severity
- Assessment ready for integration with code analysis