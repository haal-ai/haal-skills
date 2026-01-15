---
task_id: "finalize-report"
task_name: "Finalize Report"
dependencies: ["validate-sources"]
---

# Task: Finalize Report

## Input Context
**Required Context Variables**: 
- `context.report_file`: String - Path to cumulative report file
- `context.research_plan_file`: String - Path to research plan
- `context.validated_sources`: Array - All validated sources
- `context.source_validation_report`: String - Validation report text
- `context.validated_topic`: String - Research topic
- `context.timestamp`: String - Session timestamp

**Required Files**: 
- Cumulative research report file
- Research plan file (for reference)

**Required Tools**: File reading and writing

## Task Instructions

### Compile and Format Final Report

1. **Read Current Report Content**:
   - Load existing report file from `report_file`
   - Verify all chapters are present
   - Check for placeholder TOC

2. **Generate Table of Contents**:
   
   **A. Extract Chapter Headings**:
   - Scan report for all ## level headings (chapters)
   - Extract chapter numbers and titles
   - Note page/section numbers (if applicable)
   
   **B. Format TOC**:
   ```markdown
   ## Table of Contents
   
   1. [Chapter Title](#chapter-title-anchor)
   2. [Chapter Title](#chapter-title-anchor)
   ...
   
   Appendices
   - [Sources](#sources)
   - [Source Validation Report](#source-validation-report)
   ```
   
   **C. Replace TOC Placeholder**:
   - Find and replace TOC placeholder in report
   - Insert generated TOC

3. **Add Executive Summary** (if not already present):
   - Synthesize key findings from all chapters
   - Highlight main conclusions
   - Summarize recommendations
   - Keep to 1-2 paragraphs
   - Insert after title page, before TOC

4. **Compile Sources Section**:
   
   **A. Create Sources Appendix**:
   ```markdown
   ## Appendix A: Sources
   
   ### Chapter 1: [Title]
   1. [Source Title](URL) - Accessed [date]
   2. [Source Title](URL) - Accessed [date]
   
   ### Chapter 2: [Title]
   ...
   ```
   
   **B. Group by Chapter**:
   - Organize sources by chapter they appeared in
   - Include access date and URL for each
   - Maintain chronological order within chapters

5. **Add Source Validation Report**:
   - Insert validation report as Appendix B
   - Include full validation statistics
   - List any warnings or issues found
   - Format for readability

6. **Format Final Document**:
   
   **A. Ensure Consistent Formatting**:
   - Verify heading hierarchy (# title, ## chapters, ### sections)
   - Check list formatting
   - Ensure proper spacing between sections
   - Validate markdown syntax
   
   **B. Add Document Metadata**:
   ```markdown
   ---
   title: [Research Topic]
   date: [timestamp formatted as readable date]
   author: OLAF Research Assistant
   version: 1.0
   ---
   ```

7. **Write Final Report**:
   - Save complete formatted report to same file path
   - Overwrite previous version with finalized version
   - Verify file written successfully

8. **Generate Completion Summary**:
   ```
   ============================================
   RESEARCH REPORT COMPLETE
   ============================================
   
   Topic: [validated_topic]
   Report File: [report_file]
   
   Statistics:
   - Total Chapters: [count]
   - Total Sources: [count]
   - Validated URLs: [count] ([percentage]% accessible)
   - Research Duration: [if trackable]
   
   Key Findings:
   [Brief bullet points of main insights]
   
   Deliverables:
   - Research Plan: [research_plan_file]
   - Final Report: [report_file]
   
   ============================================
   Report ready for review and delivery.
   ============================================
   ```

9. **Display Summary to User**:
   - Show completion summary
   - Provide file paths for easy access
   - Invite user to review final report

## Output Requirements

**Context Variables Created**:
- `context.final_report_file`: String - Path to finalized report (same as report_file)
- `context.completion_summary`: String - Summary text
- `context.report_statistics`: Object - Stats about report
  ```
  {
    "total_chapters": [count],
    "total_sources": [count],
    "validated_sources": [count],
    "accessibility_rate": [percentage],
    "currency_rate": [percentage]
  }
  ```
- `context.task_complete`: Boolean - True

**Files Created/Updated**: 
- Final research report (updated) at `report_file` path

**Context Passed to Summary Task**:
- Completion summary for final output
- Report statistics for documentation
- File paths for user reference

## Quality Checks

Before finalizing, verify:
- [ ] Table of Contents generated and inserted
- [ ] All chapters present in correct order
- [ ] Executive summary included
- [ ] Sources appendix complete with all URLs
- [ ] Validation report included
- [ ] Consistent formatting throughout
- [ ] Document metadata present
- [ ] File saved successfully

If any check fails, log warning and attempt to fix.
