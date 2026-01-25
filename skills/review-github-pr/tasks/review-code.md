---
task_id: "review-code"
task_name: "Code Review Execution"
dependencies: []
conditions: ["code_files_found"]
---

# Review Code Changes

## Input Context
**Required State Variables**: 
- `context.code_files_found`: true (condition requirement)
- `context.code_file_paths`: Array of code file paths
- `context.pr_number`: PR number for diff fetching
- `context.code_file_count`: Number of code files detected
- `context.pr_code_files_file`: Path to code files list file
**Required Files**: Code files list file (must exist)
**Required Tools**: gh-pr-analyzer.py, review-diff competency execution

## Task Instructions

### Execute Comprehensive Code Review with Optimized Diff Fetching
**OPTIMIZATION**: Fetch diff ONLY for code files (not documentation)

**Step 1: Fetch Filtered Diff for Code Files Only**

1. **Build Filtered Diff Command**:
   - Use code files list file from context (`context.pr_code_files_file`)
   - Pass file path to analyzer with `--files-from` flag
   - Analyzer reads file list and fetches diff only for those files
   
   ```bash
   python skills/review-github-pr/tools/gh-pr-analyzer.py \
     --pr [pr_number] \
       --files-from [pr_code_files_file]
   ```

2. **Execute Filtered Diff Fetch**:
   - Run command with `isBackground: false` (CRITICAL - must complete)
   - **MANDATORY**: Wait for complete execution (may take 30 seconds for merged PRs using git fallback)
   - Script reads code files list from file
   - Script fetches diff (uses `gh pr diff` or `git show` fallback for merged PRs)
   - Script prints the exact output file paths. Capture them from stdout:
     - `📄 PR Info: ...`
     - `📄 Diff: ...`
   - Verify script completes successfully before proceeding
   - Diff contains ONLY code file diffs (not documentation)

3. **Verify Diff File Updated**:
   - Set `context.pr_info_file` and `context.pr_diff_file` from the script output
   - Confirm the diff file now contains content
   - Read filtered diff content for review

**Step 2: Execute Code Review**

4. **Prepare Code Review Parameters**:
   - Use filtered diff content (code files only)
   - Set review scope to workspace-level
   - Include action items in review output
   - Disable report saving (PR review handles output)

5. **Execute review-diff Competency**:
   ```
   EXECUTE: skills/review-diff
   PARAMETERS:
   - diff_content: [filtered diff from step 1]
   - save_report: false
   - include_actions: true
   - review_scope: workspace
   ```

6. **Capture Review Results**:
   - Code quality assessment
   - Security vulnerability analysis
   - Performance considerations
   - Testing recommendations
   - Action items prioritized by severity

7. **Process Review Output**:
   - Extract key findings and recommendations
   - Categorize issues: HIGH/MEDIUM/LOW
   - Identify any blocking concerns
   - Prepare for integration with metadata analysis

## Output Requirements

**State Updates**:
- `task_outputs.task-7.code_review`: Complete code review results
- `task_outputs.task-7.code_quality_score`: Quality assessment
- `task_outputs.task-7.security_issues`: Array of security concerns
- `task_outputs.task-7.action_items`: Prioritized action list
- `task_outputs.task-7.diff_loaded`: true (now loaded with code files only)
- `context.review_type`: "code"
- `context.recommendation`: "APPROVE"/"REQUEST_CHANGES"/"REJECT"
- `task_status.review-code`: "completed"

**Files Created**: None (gh-pr-analyzer updates existing diff file)

**Context Passed**: 
- Complete code analysis for final report
- Security and quality assessments
- Prioritized action items for user
- Filtered diff content (code files only)

## Success Criteria
- Filtered diff successfully fetched (code files only)
- review-diff competency executes successfully
- Complete code analysis performed
- Issues identified and prioritized
- Recommendation generated based on findings
- Token usage optimized (documentation files excluded from diff)