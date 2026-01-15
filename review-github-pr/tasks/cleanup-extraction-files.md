---
task_id: "cleanup-extraction-files"
task_name: "Cleanup Temporary Extraction Files"
dependencies: []
conditions: []
---

# Cleanup Temporary Extraction Files

## Input Context
**Required State Variables**: 
- `context.pr_number`: PR number for file identification
- `context.timestamp`: Timestamp for file naming pattern
- `context.pr_info_file`: Path to PR info JSON file
- `context.pr_diff_file`: Path to PR diff text file
**Required Files**: Temporary analysis files
**Required Tools**: File system operations, PowerShell commands

## Task Instructions

### Clean Up Temporary Extraction Files ONLY
**PURPOSE**: Remove temporary extraction files (JSON, diff, code list) - NEVER delete review outputs or reports

**CRITICAL**: This cleanup happens BEFORE output generation to allow user to restart with clean state

1. **Identify Files to Remove (EXTRACTION FILES ONLY)**:
   - PR info file: `pr-[number]-info-[timestamp].json`
   - PR diff file: `pr-[number]-diff-[timestamp].txt`
   - Code files list: `pr-[number]-code-files-[timestamp].txt`
   - **NEVER REMOVE**: Review reports (`pr-review-*.md`), environment files (`olaf-env.txt`)

2. **Execute Cleanup Commands**:
   ```powershell
   # Remove ONLY extraction files (JSON, TXT diffs, code lists)
   Remove-Item ".olaf/work/staging/pr-reviews/pr-[pr_number]-info-*[timestamp]*.json" -Force
   Remove-Item ".olaf/work/staging/pr-reviews/pr-[pr_number]-diff-*[timestamp]*.txt" -Force
   Remove-Item ".olaf/work/staging/pr-reviews/pr-[pr_number]-code-files-*[timestamp]*.txt" -Force
   ```

3. **Verify Cleanup**:
   - Confirm files are deleted
   - Check staging directory is clean
   - Ensure no orphaned temporary files remain

4. **Preserve Important Files (CRITICAL)**:
   - **KEEP**: ALL review report files (`pr-review-*.md`) - NEVER DELETE
   - **KEEP**: Environment file (`olaf-env.txt`)
   - **KEEP**: Any other output files from previous sessions
   - **REMOVE**: Only current session extraction files (JSON, diff TXT, code list TXT)

5. **Final Verification**:
   - List remaining files in pr-reviews directory
   - Confirm only intended files remain
   - Report cleanup completion

## Output Requirements

**State Updates**:
- `context.cleanup_completed`: true
- `context.files_removed`: Array of removed file paths
- `context.session_complete`: true
- `task_status.cleanup-extraction-files`: "completed"

**Files Created**: None

**Context Passed**: 
- Clean state for output selection
- Extraction files removed, review data in memory
- User can restart without file conflicts

## Success Criteria
- Temporary extraction files successfully removed (JSON, diff TXT, code list TXT)
- ALL review reports and outputs preserved
- Environment file preserved
- Staging directory ready for output generation
- No file system errors during cleanup
- User can now choose output method with clean state