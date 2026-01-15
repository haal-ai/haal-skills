---
task_id: "create-research-plan"
task_name: "Create Research Plan"
dependencies: ["validate-research-topic"]
---

# Task: Create Research Plan

## Input Context
**Required Context Variables**: 
- `context.validated_topic`: String - Validated research topic
- `context.scope_statement`: Object - Scope boundaries
- `context.key_questions`: Array - Key research questions
- `context.information_needs`: Object - Required source types
- `context.timestamp`: String - Session timestamp (YYYYMMDD-HHMMSS)
- `context.output_dir`: String - Output directory path

**Required Files**: 
- Template: `[skill_path]/templates/research-plan-template.md`

**Required Tools**: File writing

## Task Instructions

### Generate Structured Research Plan

1. **Load Research Plan Template**:
   - Read template from skill templates directory
   - Prepare to populate with validated context

2. **Populate Plan Sections**:

   **A. Executive Summary**:
   - Topic statement from `validated_topic`
   - Brief overview of research goals
   - Expected deliverables

   **B. Scope Statement**:
   - Included areas from `scope_statement.included`
   - Excluded areas from `scope_statement.excluded`
   - Rationale for boundaries

   **C. Key Research Questions**:
   - List all questions from `key_questions`
   - Group related questions if appropriate
   - Indicate priority order

   **D. Proposed Chapter Structure**:
   - Create hierarchical outline based on research questions
   - Typical structure:
     - Chapter 1: Introduction and Background
     - Chapter 2-N: Core research areas (one per major question)
     - Chapter N+1: Analysis and Synthesis
     - Chapter N+2: Conclusions and Recommendations
   - Include brief description of each chapter's focus
   - Estimate scope (e.g., "2-3 pages")

   **E. Source Strategy**:
   - Map source types from `information_needs` to chapters
   - Specify web search queries for current information:
     - "[topic] 2025"
     - "[tool] latest features"
     - "[domain] current trends"
   - Identify academic/technical documentation needs
   - Note validation requirements (URL collection, currency)

   **F. Timeline and Milestones** (if provided):
   - Research phase duration
   - Writing phase duration
   - Review and revision timeline

3. **Generate File Path**:
   - Format: `[output_dir]/research-plan-[timestamp].md`
   - Example: `.olaf/work/staging/research-plan-20251121-1755.md`

4. **Write Research Plan File**:
   - Save populated template to generated path
   - Verify file written successfully

5. **Display Plan for User Approval**:
   ```
   ============================================
   RESEARCH PLAN - APPROVAL REQUIRED
   ============================================
   
   [Display full plan content]
   
   ============================================
   Plan saved to: [file path]
   
   Please review and approve before proceeding.
   - Type 'approve' to continue with research
   - Type 'revise' to modify the plan
   - Suggest specific changes if needed
   ============================================
   ```

6. **Wait for User Approval**:
   - Pause execution until user responds
   - If approved: proceed to next task
   - If revisions requested: note changes needed (coordinator handles loop)

## Output Requirements

**Context Variables Created**:
- `context.research_plan_file`: String - Path to saved research plan
- `context.chapter_structure`: Array - List of chapters with metadata
  ```
  [
    {
      "chapter_number": 1,
      "title": "Introduction and Background",
      "focus": "Overview of topic and context",
      "estimated_scope": "2-3 pages",
      "key_questions": [1, 2]
    },
    ...
  ]
  ```
- `context.total_chapters`: Integer - Total number of chapters
- `context.source_strategy`: Object - Source types mapped to chapters
- `context.plan_approved`: Boolean - Set by coordinator after user approval

**Files Created**: 
- Research plan file at `[output_dir]/research-plan-[timestamp].md`

**Context Passed to Next Tasks**:
- Research plan file path for reference
- Chapter structure for iterative chapter writing
- Source strategy to guide research approach

## User Approval Protocol

This task implements a **PROPOSE-CONFIRM-ACT** checkpoint:
- **Propose**: Display complete research plan
- **Confirm**: Wait for explicit user approval
- **Act**: Only proceed if approved (coordinator handles this)

The coordinator must check `plan_approved` before advancing to chapter research.
