---
task_id: "task-11"
task_name: "Report Generation"
dependencies: []
conditions: []
---

# Task 11: Report Generation

## Input Context
**Required State Variables**: 
- `context.output_method`: "save" or "display"
- `context.review_type`: "code" or "documentation"
- `context.pr_number`: PR number for file naming
- `context.timestamp`: Timestamp for file naming
- `context.code_review`: Code review results (if code workflow)
- `context.doc_review`: Documentation review results (if doc workflow)
- `context.helper_analysis`: PR metadata and process analysis
**Required Files**: None
**Required Tools**: Report formatting, file creation (if save option)

## Task Instructions

### Generate Final PR Review Report
**FORMAT**: Based on user's output method choice

1. **Compile Report Sections**:
   - **PR Overview**: Title, description, metadata analysis
   - **File Analysis**: Type breakdown, scope assessment
   - **Quality Assessment**: Code or documentation review results
   - **Security Assessment**: Vulnerability findings (if applicable)
   - **Process Assessment**: Workflow compliance from helper analysis
   - **Recommendation**: Final APPROVE/REQUEST CHANGES/REJECT
   - **Action Items**: Prioritized HIGH/MEDIUM/LOW issues

2. **Format Based on Output Method**:
   
   **Option A - Save to File**:
   - Create structured markdown report
   - Save to: `[staging_dir]pr-reviews/pr-review-[pr_number]-[timestamp].md`
   - Include complete analysis with all details
   - Use GitHub PR review template format
   
   **Option B - Display on Screen**:
   - Generate concise markdown for display
   - Focus on critical and high-priority items
   - Summarize key findings for readability
   - Include essential recommendation and top action items

3. **Generate Report Content**:
   - Integrate metadata analysis with code/doc review
   - Combine helper analysis findings
   - Present unified recommendation
   - Ensure action items are clearly prioritized

## Output Requirements

**State Updates**:
- `context.report_generated`: true
- `context.report_file`: Path to saved file (if option A)
- `context.report_content`: Report content (if option B)
- `context.final_recommendation`: Final recommendation
- `task_status.task-11`: "completed"

**Files Created**: 
- PR review report file (if save option selected)

**Context Passed**: 
- Report completion status for cleanup
- File path for cleanup reference

## Success Criteria
- Report successfully generated in requested format
- All analysis results integrated cohesively
- Clear recommendation and action items provided
- Output delivered according to user preference