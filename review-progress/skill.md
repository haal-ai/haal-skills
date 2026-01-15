---
name: review-progress
description: Conduct a comprehensive work review to assess progress, identify accomplishments, and plan upcoming priorities.
license: Apache-2.0
metadata:
  olaf_tags: [review, progress, planning, assessment]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters

You MUST request these parameters if not provided by the user:
- **review_period**: string - Time period to review (e.g., "past 7 days", "Q2 2025") (REQUIRED)
- **data_sources**: array[string] - Specific data sources to analyze (REQUIRED - ask user to specify)
- **project_path**: string - Path to project/repository to analyze (OPTIONAL - auto-detect if in workspace)
- **focus_areas**: array[string] - (Optional) Specific projects or metrics to focus on
- **team_members**: array[string] - (Optional) Team members to include in the review
- **metrics**: array[enum] - (Optional) Key metrics to evaluate (velocity, quality, delivery, etc.)

## User Interaction Protocol

You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Use Propose-Act protocol for data collection and analysis
- Use Propose-Confirm-Act protocol for saving the final progress report

## Process

### 1. Validation Phase

You WILL verify all requirements:
- Confirm review period is clearly defined
- Validate access to specified data sources
- Check project path accessibility (if provided)
- Verify user has specified what data sources to analyze

### 2. Execution Phase

**Data Collection**: You WILL gather information from user-specified sources:

#### Git Repository Analysis (if requested):
- Run: `git log --since="[review_period_start]" --until="[review_period_end]" --oneline`
- Run: `git diff --stat --since="[review_period_start]"`
- Check merged PRs and closed issues for the period
- Analyze commit frequency and patterns

#### Project File Analysis (if requested):
- Read: Recent updates to README.md, CHANGELOG.md files
- Scan: Task lists in markdown files (TODO.md, tasks.md, etc.)
- Review: Project documentation updates
- Check: File modification patterns using `git log --name-status`

#### OLAF-specific Data Analysis (if requested):
- Read: Contents of `.olaf/work/staging/` for completed work
- Scan: Conversation records from recent period
- Review: Completed skill executions and outputs
- Analyze: Decision records and progress files

#### Workspace Analysis (if requested):
- List: Recently modified files in workspace
- Check: Active branches and development status
- Review: Open issues or TODO items in code comments

**Progress Analysis**: You WILL process collected data:
- Compare activities against stated goals
- Identify achievement patterns and blockers
- Calculate productivity metrics from available data
- Assess resource allocation and team performance

**Report Generation**: You WILL create structured progress report:
- Use template: `templates/progress-review-template.md`
- Populate all template sections with actual data
- Include specific examples and metrics
- Add timestamp and review period information
- Save to: `.olaf/work/staging/progress-reviews/progress-review-[YYYYMMDD-HHmm].md`

### 3. Validation Phase

You WILL validate the final report:
- Confirm all requested data sources were analyzed
- Verify report follows template structure completely
- Check that insights are data-driven and specific
- Ensure recommendations are actionable

## Output Format

You WILL generate outputs following this structure:
- **Progress Analysis Report**: Data-driven assessment with specific metrics and examples
- **Structured Progress Report**: Complete document following `templates/progress-review-template.md`
- **Actionable Recommendations**: Specific next steps based on findings
- **Saved Report**: File saved to `.olaf/work/staging/progress-reviews/progress-review-[YYYYMMDD-HHmm].md`

### Report Generation

You MUST create the progress report using the template: `templates/progress-review-template.md`

You WILL populate all template placeholders with actual data collected from specified sources.

## User Communication

### Progress Updates
- Confirmation when data sources are successfully accessed
- Summary of data collection results (commits, files analyzed, etc.)
- Status updates during analysis phase
- Timestamp identifier used: [YYYYMMDD-HHmm format]
- Confirmation when report is saved to `.olaf/work/staging/progress-reviews/`

### Completion Summary
- Total data points analyzed from each source
- Key findings and trend analysis
- Priority recommendations based on data
- Saved report location: `.olaf/work/staging/progress-reviews/progress-review-[YYYYMMDD-HHmm].md`

### Next Steps

You WILL clearly define:
- Priority actions based on progress analysis
- Specific goals for the next review period
- Resource needs and timeline adjustments
- Follow-up review schedule recommendations

## Output to USER
1. **Progress Overview**:
   - Goals vs. actuals
   - Major achievements
   - Key challenges
2. **Detailed Analysis**:
   - Project status updates
   - Team performance metrics
   - Resource utilization
3. **Next Steps**:
   - Priority actions
   - Timeline adjustments
   - Resource needs

## Domain-Specific Rules
- Rule 1: Focus on data-driven insights
- Rule 2: Maintain constructive feedback
- Rule 3: Align with business objectives
- Rule 4: Consider team capacity
- Rule 5: Document assumptions

## Required Actions
1. Validate all required input parameters and data source access
2. Execute data collection from user-specified sources (git, files, workspace, OLAF data)
3. Analyze collected data for trends, achievements, and blockers
4. Generate comprehensive progress report using template structure
5. Save formatted report to `.olaf/work/staging/progress-reviews/progress-review-[YYYYMMDD-HHmm].md`
6. Provide actionable recommendations based on analysis

## Error Handling

You WILL handle these scenarios:
- **No Data Sources Specified**: Request user to specify which data sources to analyze
- **Inaccessible Data Sources**: Inform user and ask for alternative sources or paths
- **Empty Review Period**: Ask user to specify a valid time period with available data
- **Git Repository Issues**: Check if current directory is a git repo, suggest alternatives
- **File Access Issues**: Provide clear error messages and request alternative file paths
- **No Recent Activity**: Report findings accurately and suggest extending review period
- **Template Access Issues**: Provide manual structure if template is unavailable

⚠️ **Critical Requirements**
- MANDATORY: Ask user to specify which data sources to analyze before starting
- MANDATORY: All analysis MUST be based on actual collected data, not assumptions
- NEVER analyze data sources without user permission
- NEVER generate reports without concrete data from specified sources  
- ALWAYS save the final report to staging directory with timestamp
- ALWAYS provide specific examples and metrics in findings
- ALWAYS include data source references in the report
