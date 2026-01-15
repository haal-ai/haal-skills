---
name: research-and-report
description: Structured research with comprehensive reporting and current information validation
license: Apache-2.0
metadata:
  olaf_tags: [research, reporting, web-search, analysis, documentation]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Web Search Integration and Source Collection

## Process

### Phase 1: Validation
1. **Topic Analysis**: Break down research request into specific domains and questions
2. **Source Planning**: Identify appropriate web sources and search strategies
3. **Template Selection**: Choose appropriate report template from `templates/`

### Phase 2: Execution
1. **Web Research**: Conduct thorough web searches, collecting URLs for all sources
2. **Information Synthesis**: Analyze findings from multiple sources, ensuring current information  
3. **Report Generation**: Create structured reports using appropriate templates
4. **Source Documentation**: Include all URLs and ensure accessibility
5. **Current Information Validation**: Verify that sources are recent and relevant

### Phase 3: Validation
1. **Source Verification**: Confirm all URLs are accessible and relevant
2. **Quality Check**: Ensure comprehensive coverage of research topic
3. **Output Review**: Validate report structure and completeness

## Research Guidelines

- **Search for current data** on tools, pricing, features, and market conditions
- **Validate training data** against recent web sources when possible
- **Use targeted queries**: "[topic] 2025", "[tool] latest features", "[topic] current trends"
- **Document currency**: Note when information was found and from what type of source
- **Prioritize recent**: When conflicting information exists, favor current web sources
- **MANDATORY URL COLLECTION**: Every source MUST include full URL - NO generic references allowed
- **Source Format**: All sources must use format: `[Source Title](full-url)` 
- **REJECT GENERIC SOURCES**: Any reference without specific URL or DOI is unacceptable

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.

- **research_topic**: string - Specific topic or question to research
- **scope_boundaries**: string - What is included and excluded from research
- **expected_outcomes**: string - Expected deliverables and target audience
- **timeline**: string - Optional research and writing timeline

## Output Format
1. **Research Plan**: Structured outline using `templates/research-plan-template.md`
2. **Comprehensive Report**: Final report using `templates/research-report-template.md`
3. **Source Documentation**: Complete URL list with accessibility verification
4. **Executive Summary**: Key findings and recommendations

## User Communication
- **Progress Updates**: Regular status updates during lengthy research
- **Clarification Requests**: Prompt for missing parameters or scope clarification
- **Source Verification**: Present all URLs for user validation
- **Quality Assurance**: Confirm deliverable meets expectations

## Domain-Specific Rules
- **MANDATORY URL COLLECTION**: Every source MUST include full URL - NO generic references allowed
- **Source Format**: All sources must use format: `[Source Title](full-url)` 
- **REJECT GENERIC SOURCES**: Any reference without specific URL or DOI is unacceptable
- **Search for current data** on tools, pricing, features, and market conditions
- **Validate training data** against recent web sources when possible
- **Use targeted queries**: "[topic] 2025", "[tool] latest features", "[topic] current trends"
- **Document currency**: Note when information was found and from what type of source
- **Prioritize recent**: When conflicting information exists, favor current web sources

## Success Criteria
- All sources include specific, accessible URLs
- Information is current and validated against web sources
- Research plan approved by user before execution
- Report follows approved structure and templates
- User confirms deliverable meets expectations

## Error Handling
- **Missing URLs**: Reject any source without specific URL
- **Inaccessible Sources**: Verify all URLs work before including
- **Outdated Information**: Flag when training data conflicts with current sources
- **Scope Creep**: Return to user for clarification if research exceeds boundaries

## Implementation Details

### Planning Phase
- Receive research topic from user and clarify ambiguities
- Analyze topic to define research boundaries
- Create detailed research plan including:
  - **Scope Statement**: What is included and excluded
  - **Key Research Questions**: Primary questions to answer
  - **Proposed Chapter Structure**: Hierarchical outline
  - **Potential Sources**: Preliminary source list including:
    - **Web Research**: Current vendor sites, industry reports, community forums
    - **Search Strategy**: Specific queries planned for current information validation
    - **Academic/Internal**: Training data, documentation, internal knowledge
- Save research plan to: `.olaf/work/staging//research-plan-YYYYMMDD-HHmm.md`
- Present plan to user for approval

### Execution Phase
- Begin research and writing following approved chapter structure
- For each chapter sequentially:
  - Conduct in-depth research using outlined methods and sources:
    - **Web Search First**: Use targeted queries to gather current information
    - **Validate Training Data**: Cross-check knowledge against recent web sources
    - **Prioritize Current**: Use most recent information when conflicts exist
  - Synthesize gathered information into clear, concise content
  - **Include source currency indicators**: Mark information as current vs. training data
  - **Note information freshness**: Include search dates for web-sourced information
  - Draft chapter with appropriate formatting (headings, lists, tables)
  - Present completed chapter to user for review
  - Add approved chapter content to: `.olaf/work/staging//research-report-YYYYMMDD-HHmm.md`

### Finalization Phase
- Compile all approved chapters into single cohesive report
- Add title page and generate table of contents
- Ensure consistent formatting throughout document
- Save final report to: `.olaf/work/staging//research-report-YYYYMMDD-HHmm.md`
- Notify user of completion with file path

## File Outputs

Research deliverables following timestamp conventions and templates:

- **Research Plan**: `research-plan-YYYYMMDD-HHmm.md`
  - Use template: `templates/research-plan-template.md`
  - Includes scope statement, key research questions, chapter structure, potential sources

- **Research Report**: `research-report-YYYYMMDD-HHmm.md` (updated per chapter, finalized with TOC)
  - Use template: `templates/research-report-template.md`
  - Complete compiled report with title page, table of contents, and all approved chapters

## Output to USER

- Research plan created: [file path]
- Chapters completed: [number/total chapters]
- Final report delivered: [file path and completion timestamp]
- Key findings summary: [brief overview of main insights]

## Research Rules

- Rule 1: Research plan MUST be approved by user before any research begins
- Rule 2: Each chapter MUST be presented for user approval before proceeding to next
- Rule 3: All file paths and naming conventions must follow specified timestamp format
- Rule 4: Use Propose-Confirm-Act protocol for all major deliverable approvals
- Rule 5: **Web search current information** whenever researching tools, market conditions, or rapidly changing topics
- Rule 6: **MANDATORY URL COLLECTION** - Every source MUST have full URL, reject generic references
- Rule 7: **Source validation** - All sources must be accessible and current (prefer 2024-2025 content)
