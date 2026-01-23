---
task_id: "collect-git-diff"
task_name: "Collect Git Diff Content"
dependencies: ["context.diff_content", "context.review_scope", "context.target_path", "context.git_repo_valid"]
conditions: []
---

# Collect Git Diff Content

## Input Context
**Required Context Variables**: 
- `context.diff_content`: Pre-provided diff content (may be null)
- `context.review_scope`: Scope of review ("workspace", "folder", "file")
- `context.target_path`: Target path for scoped reviews (may be null)
- `context.git_repo_valid`: Whether git repository is available
**Required Files**: None
**Required Tools**: Git command-line tool

## Task Instructions

### Acquire Diff Content

1. **Determine Diff Source**:
   
   **IF diff_content parameter is provided**:
   - Use provided diff content directly
   - Skip git diff command execution
   - Validate diff content is not empty
   - Store as `context.diff_text`
   
   **ELSE** (need to execute git diff):
   - Verify `context.git_repo_valid == true`
   - Execute appropriate git diff command based on scope

2. **Execute Git Diff Commands** (if needed):
   
   **For "workspace" scope**:
   ```bash
   git diff
   ```
   
   **For "folder" scope**:
   ```bash
   cd [target_path]
   git diff .
   ```
   
   **For "file" scope**:
   ```bash
   git diff [target_path]
   ```

3. **Process Diff Output**:
   - Capture diff output
   - Validate diff is not empty (if empty, no changes to review)
   - Extract list of changed files from diff headers
   - Store complete diff text

4. **Extract File List**:
   Parse diff to identify changed files:
   - Look for lines starting with `diff --git a/` or `+++`
   - Extract file paths
   - Create array of changed file paths
   - Store as `context.diff_file_list`

## Output Requirements

**State Updates**:
- `context.diff_text`: Complete diff content as string
- `context.diff_file_list`: Array of changed file paths
- `context.diff_empty`: Boolean flag (true if no changes detected)
- `task_status.collect-git-diff`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Diff content for language detection and analysis
- File list for categorization by language
