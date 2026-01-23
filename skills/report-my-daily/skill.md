---
name: report-my-daily
description: Generate daily work report by analyzing git activity, files, PRs, carry-overs, jobs, and changelog with iterative user refinement
license: Apache-2.0
metadata:
  olaf_tags: [daily, report, git, activity, summary]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

# Daily Report Generation Skill

## Description
Generate daily work report by analyzing git activity, files, PRs, carry-overs, jobs, and changelog with iterative user refinement.

## Tags
[daily, report, git, activity, summary]

## Time Retrieval
Get current timestamp in `YYYYMMDD-HHmm` format

## Input Parameters
You MUST request these parameters if not provided by the user:
- **report_period**: string - Time period for report: "today", "yesterday", or "last X days" (REQUIRED)
- **days_count**: number - Number of days if "last X days" selected (OPTIONAL - only if report_period is "last X days")
- **include_github_reviews**: boolean - Whether to search GitHub PR reviews (OPTIONAL - default to true if possible)
- **custom_notes**: string - Additional notes or context to include (OPTIONAL)

## User Interaction
Always ask for user approval before generating or modifying reports containing personal data.

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm report period and calculate date range
- Create .olaf/data/product/daily/ directory if it doesn't exist
- Verify git repository access and user identity
- Check access to .olaf/work/carry-over/ and .olaf/data/projects/jobs/ directories
- Validate write permissions for report output

### 2. Execution Phase

**Git Activity Analysis**:
- [git_analysis] -
You WILL analyze git activity for the specified period:
- Execute git log with date range: `git --no-pager log --author="[user]" --since="[date]" --until="[date]" --oneline`
- Execute git log for merges: `git --no-pager log --author="[user]" --merges --since="[date]" --until="[date]" --oneline`
- Identify commits, merges, and branch activities
- Extract commit messages and categorize by type (feat, fix, chore, etc.)
- [/git_analysis] -

**File Status Analysis**:
- [file_status] -
You WILL analyze current file modifications:
- Execute `git --no-pager status` to identify untracked and staged files
- Execute `git --no-pager diff --name-only` for modified files
- Categorize files by type and potential impact
- Identify work in progress and pending changes
- [/file_status] -

**GitHub PR Review Analysis**:
- [github_analysis] -
You WILL attempt to identify GitHub PR Reviews (if possible):
- Search for GitHub-related activity in git log
- Look for PR-related commit messages or merge patterns
- Note: Limited to local git information unless GitHub API access available
- [/github_analysis] -

**Carry-Over Analysis**:
- [carryo_analysis] -
You WILL analyze carry-over files:
- Read all files in .olaf/work/carry-over/ directory
- Extract relevant items for the specified date range
- Identify ongoing tasks and their status
- Note any blockers or assistance needs mentioned
- [/carryo_analysis] -

**Jobs Directory Analysis**:
- [jobs_analysis] -
You WILL analyze jobs directory:
- Read .olaf/data/projects/jobs/ if exists
- Scan .olaf/data/projects/jobs/ directory for recent activity
- Identify job-related work within the date range
- Extract job status and progress information
- [/jobs_analysis] -

**Changelog Analysis**:
- [changelog_analysis] -
You WILL analyze changelog entries:
- Read .olaf/data/projects/changelog-register.md
- Filter entries for the specified date range
- Categorize changes by type and impact
- Identify user contributions and participation
- [/changelog_analysis] -

### 3. Report Synthesis

**Report Structure**:
You WILL synthesize all data into structured report:
- Organize staging into four categories:
  1. I progressed on this
  2. I participated in this
  3. I'm blocked on this
  4. I would need assistance on this
- Create concise, actionable summaries for each category
- Include relevant details and context
- Prepare initial draft for user review

**Iterative Refinement**:
You WILL cycle through user feedback until completion:
- Present draft report to user for review
- Offer options: modify, delete, add comments, save, or stop
- Apply user modifications and regenerate sections as needed
- Continue refinement cycle until user says "save" or "stop"
- Maintain report structure throughout iteration

### 4. Core Logic
Execute following requirements:
- Ask for user approval before generating or modifying reports
- Maintain data accuracy and user privacy throughout analysis
- Ensure report remains concise and actionable for daily standup use

### 5. Validation Phase
You WILL validate results:
- Confirm all data sources were analyzed successfully
- Verify report structure matches required format
- Validate timestamps and file naming conventions
- Ensure user satisfaction with final report content

## Output Format
You WILL generate outputs following this structure:

Primary deliverable: Daily report saved as .olaf/data/product/daily//daily-[YYYYMMDD-HHmm].md

Report structure:
```
# Daily Report - [Date]

## i. I progressed on this
- [Concise progress items with context]

## ii. I participated in this
- [Collaboration and review activities]

## iii. I'm blocked on this
- [Current blockers with details]

## iv. I would need assistance on this - [Areas requiring help or support]

## Additional Notes
- [Custom notes and context]
```
Character encoding: UTF-8 for compatibility
Timestamp format: YYYYMMDD-HHmm in filename

## User Communication

### Progress Updates
Confirmation when .olaf/data/product/daily/ directory is created/verified
Status of each analysis phase (git, files, carry-over, jobs, changelog)
Progress of report synthesis and categorization
User feedback incorporation status during refinement
Final report generation and save confirmation

### Success Criteria
You WILL consider the task complete when:
- [ ] Report period validated and date range calculated
- [ ] All data sources analyzed (git, files, carry-over, jobs, changelog)
- [ ] Initial report synthesized in four-category structure
- [ ] User refinement cycle completed to satisfaction
- [ ] Final report saved with timestamped filename in .olaf/data/product/daily/
- [ ] All data sources processed without privacy violations

### Error Handling
You WILL handle these scenarios:
- **Git Repository Not Found**: Provide clear error and suggest repository initialization
- **Git Command Failures**: Offer alternative analysis methods and manual input options
- **Directory Access Issues**: Create missing directories and handle permission problems
- **GitHub API Limitations**: Focus on local git data and inform user of limitations
- **Empty Data Sources**: Handle gracefully and note in report sections
- **File Write Failures**: Suggest alternative save locations and troubleshooting
- **User Refinement Conflicts**: Clarify requirements and offer structured modification options

## Critical Requirements
1. MANDATORY: Ask for user approval before generating or modifying reports
2. MANDATORY: Maintain user privacy and data security throughout analysis
3. MANDATORY: Use timestamped filename format for all daily reports
4. MANDATORY: Organize report into exactly four specified categories
5. NEVER include sensitive information like passwords or personal data
6. NEVER bypass user refinement cycle - always allow modifications
7. ALWAYS handle git command failures gracefully without stopping process
8. ALWAYS maintain .olaf/data/product/daily/ directory structure for organization
9. ALWAYS keep reports concise and actionable for daily standup meetings

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ALWAYS maintain user privacy and data security during analysis
- Rule 2: MUST create .olaf/data/product/daily/ directory structure if it doesn't exist
- Rule 3: ALWAYS use timestamped filename format: daily-[YYYYMMDD-HHmm].md
- Rule 4: MUST organize report into exactly four categories as specified
- Rule 5: NEVER include sensitive information like passwords or personal data
- Rule 6: ALWAYS allow iterative refinement until user says "save" or "stop"
- Rule 7: MUST use --no-pager option for all git commands to prevent paging issues
- Rule 8: MUST handle git command failures gracefully with alternative approaches
- Rule 9: ALWAYS keep reports concise and actionable for daily standup use

## Success Criteria
You WILL consider the task complete when:
[ ] Report period validated and date range calculated
[ ] All data sources analyzed successfully
[ ] Initial report synthesized in four-category structure
[ ] User refinement cycle completed to satisfaction
[ ] Final report saved with correct timestamped filename
[ ] .olaf/data/product/daily/ directory structure maintained
[ ] All data sources processed without privacy violations

## Required Actions1. Validate report period and calculate date range for analysis
2. Execute comprehensive analysis of all specified data sources3. Synthesize staging into four-category structured report
4. Facilitate iterative refinement with user feedback5. Save final report with timestamped filename in .olaf/data/product/daily/
6. Provide comprehensive summary and next steps

## Next Steps
You WILL clearly define:
- Daily report ready for use and sharing
- Report saved with timestamped filename for tracking
- Suggestions for follow-up actions based on blockers or assistance needs
- Recommendation to review carry-overs for next day planning

## Completion Summary
- Summary of data sources analyzed and staging count
- Report categories populated with item count
- Final report location: .olaf/data/product/daily//daily-[YYYYMMDD-HHmm].md
- User modifications applied during refinement process
- Total refinement cycles completed

