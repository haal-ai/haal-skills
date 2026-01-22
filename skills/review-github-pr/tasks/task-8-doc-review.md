---
task_id: "task-8"
task_name: "Documentation Review"
dependencies: []
conditions: ["no_code_files"]
---

# Task 8: Documentation Review

## Input Context
**Required State Variables**: 
- `context.code_files_found`: false (condition requirement)
- `context.file_types_summary`: Array of file extensions
- `task_outputs.task-4.helper_analysis`: PR metadata analysis results
**Required Files**: None (metadata analysis already completed)
**Required Tools**: Text analysis, summary generation

## Task Instructions

### Provide Documentation-Focused Summary
**SCOPE**: Since no code files detected, provide brief documentation review ONLY

1. **Summarize PR Metadata Quality** (from task-4):
   - Title and description assessment
   - Branch naming compliance
   - Change statistics overview

2. **Analyze Documentation/Config Structure**:
   - List file types being modified (.md, .json, .csv, etc.)
   - Assess scope of documentation changes
   - Identify configuration or resource file updates
   - **NO deep content analysis** - keep high-level

3. **Generate Brief Assessment**:
   - Focus on PR process compliance
   - Document structure and organization
   - Keep output concise (< 50 lines)
   - **DO NOT** perform code review analysis

4. **Provide Simple Recommendation**:
   - APPROVE/REQUEST CHANGES based on metadata
   - Focus on process and documentation quality
   - Include any minor fixes needed

## Output Requirements

**State Updates**:
- `context.review_type`: "documentation"
- `context.review_summary`: Brief text summary
- `context.recommendation`: "APPROVE" or "REQUEST_CHANGES"
- `context.issues_found`: Array of any issues (HIGH/MEDIUM/LOW)
- `task_status.task-8`: "completed"

**Files Created**: None

**Context Passed**: 
- Review summary for report generation
- Recommendation and issues for output formatting
- Documentation review completion signal

## Success Criteria
- Brief documentation review completed
- Process compliance assessed
- Recommendation provided
- Output kept concise and focused
- No code analysis attempted