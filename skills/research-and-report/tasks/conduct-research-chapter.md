---
task_id: "conduct-research-chapter"
task_name: "Conduct Research Chapter"
dependencies: ["create-research-plan"]
iterative: true
---

# Task: Conduct Research Chapter

## Input Context
**Required Context Variables**: 
- `context.chapter_structure`: Array - Full chapter structure
- `context.current_chapter_index`: Integer - Index of chapter to research (0-based)
- `context.research_plan_file`: String - Path to research plan for reference
- `context.source_strategy`: Object - Source types for this chapter
- `context.timestamp`: String - Session timestamp
- `context.output_dir`: String - Output directory path
- `context.report_file`: String - Path to cumulative report file (created if not exists)

**Required Files**: 
- Research plan file (for reference)
- Template: `[skill_path]/templates/research-report-template.md` (first iteration only)

**Required Tools**: 
- Web search (http_request)
- File writing/appending

## Task Instructions

### Research and Write Single Chapter

**ITERATIVE EXECUTION**: This task executes once per chapter. The coordinator loops until all chapters complete.

1. **Get Current Chapter Details**:
   - Extract chapter info from `chapter_structure[current_chapter_index]`
   - Chapter number, title, focus, key questions
   - Display: "Researching Chapter [N]: [Title]"

2. **Conduct Web Research**:
   
   **A. Execute Targeted Searches**:
   - Use http_request tool to search for current information
   - Query patterns based on chapter focus:
     - "[topic] 2025" for current state
     - "[tool/technology] latest features"
     - "[domain] current trends"
     - "[concept] best practices"
   - Collect at least 3-5 web sources per chapter
   
   **B. MANDATORY URL Collection**:
   - Every source MUST include full URL
   - Format: `[Source Title](https://full-url.com)`
   - NO generic references allowed
   - Verify URLs are accessible
   
   **C. Validate Information Currency**:
   - Prioritize sources from 2024-2025
   - Note publication/update dates
   - Flag outdated information
   - Cross-reference multiple sources

3. **Synthesize Chapter Content**:
   
   **A. Structure Chapter**:
   - Use chapter title as main heading (## level)
   - Create 3-5 subsections addressing key questions
   - Include:
     - Introduction paragraph
     - Core content with evidence
     - Summary or transition to next chapter
   
   **B. Integrate Sources**:
   - Cite sources inline using [Source Title](URL) format
   - Include direct quotes where valuable
   - Paraphrase and synthesize information
   - Provide attribution for all claims
   
   **C. Format Content**:
   - Use markdown formatting (headings, lists, tables)
   - Include examples or case studies if relevant
   - Add emphasis for key points
   - Ensure readability and flow

4. **Collect Source Metadata**:
   - For each source used, capture:
     ```
     {
       "title": "Source Title",
       "url": "https://full-url.com",
       "accessed_date": "[timestamp]",
       "relevance": "Brief note on why used",
       "currency": "2024|2025|older"
     }
     ```
   - Store in `chapter_sources` array

5. **Initialize or Append to Report File**:
   
   **First Chapter (index 0)**:
   - Load report template
   - Add title page with research topic
   - Add placeholder for Table of Contents
   - Append first chapter content
   - Save to `[output_dir]/research-report-[timestamp].md`
   
   **Subsequent Chapters**:
   - Read existing report file
   - Append new chapter content
   - Save updated report

6. **Display Chapter for User Approval**:
   ```
   ============================================
   CHAPTER [N] COMPLETE - APPROVAL REQUIRED
   ============================================
   Title: [Chapter Title]
   
   [Display chapter content]
   
   Sources Used:
   - [Source 1 Title](URL)
   - [Source 2 Title](URL)
   ...
   
   ============================================
   Chapter saved to: [report_file]
   
   Please review and approve before proceeding.
   - Type 'approve' to continue to next chapter
   - Type 'revise' to modify this chapter
   - Suggest specific changes if needed
   ============================================
   ```

7. **Update Iteration State**:
   - If approved: increment `current_chapter_index`
   - Check if more chapters remain
   - Signal completion status to coordinator

## Output Requirements

**Context Variables Created/Updated**:
- `context.current_chapter_index`: Integer - Incremented for next iteration
- `context.chapter_sources`: Array - Sources for current chapter
- `context.all_sources`: Array - Cumulative sources from all chapters
- `context.report_file`: String - Path to cumulative report file
- `context.chapter_approved`: Boolean - Set by coordinator after user approval
- `context.chapters_complete`: Boolean - True when all chapters done

**Files Created/Updated**: 
- Research report file (created or appended) at `[output_dir]/research-report-[timestamp].md`

**Context Passed to Next Iteration/Task**:
- Updated chapter index for next iteration
- Cumulative sources for validation task
- Report file path for finalization task

## Iteration Control

**Loop Condition**: `current_chapter_index < total_chapters`

**Coordinator Responsibilities**:
- Initialize `current_chapter_index = 0` before first iteration
- Check `chapter_approved` before incrementing index
- Loop back to this task while chapters remain
- Proceed to next task when `chapters_complete = true`

## User Approval

This task requires user approval per chapter:
- Display completed chapter with sources
- Wait for explicit user approval
- Proceed to next chapter only if approved

The coordinator must enforce approval before continuing iteration.
