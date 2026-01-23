---
task_id: "extract-pr-data"
task_name: "PR Data Extraction"
dependencies: []
conditions: []
---

# Extract PR Data from GitHub

## Input Context
**Required Context Variables**: 
- `timestamp`: Timestamp for file naming
- `pr_number`: PR number to extract (if specific mode)
- `pr_selection_mode`: "specific" or "latest"
**Required Files**: None
**Required Tools**: `gh-pr-analyzer.py` script

## Task Instructions

### Execute PR Data Extraction Script
**REQUIRED**: MUST use Python script - NO FALLBACKS ALLOWED

1. **Build Command Based on Selection Mode**:
   - For specific PR (METADATA ONLY - optimized): 
     ```bash
     python skills/review-github-pr/tools/gh-pr-analyzer.py --pr [pr_number] --timestamp [timestamp] --metadata-only
     ```
   - For latest open (METADATA ONLY - optimized):
     ```bash
     python skills/review-github-pr/tools/gh-pr-analyzer.py --latest-open --timestamp [timestamp] --metadata-only
     ```

2. **Execute Script and Wait for Completion**:
   - Run command with `isBackground: false` (CRITICAL - script must complete)
   - Capture all output from script execution
   - **MANDATORY**: Wait for complete execution (typically 30 seconds)
   - Verify script completes with success message
   - Do NOT proceed until script finishes and files are created

3. **Locate Created Files**:
   - Script creates 3 files with timestamp:
     - PR Info: `.olaf/work/staging/pr-reviews/pr-[number]-info-[timestamp].json`
     - Code Files List: `.olaf/work/staging/pr-reviews/pr-[number]-code-files-[timestamp].txt` (list of code files, empty if none)
     - Diff file: `.olaf/work/staging/pr-reviews/pr-[number]-diff-[timestamp].txt` (EMPTY in metadata-only mode)
   - Files are newly created with current timestamp

4. **Handle Script Failure**:
   - If script fails: STOP execution, report error
   - Do NOT use alternative methods or fallbacks

**Note**: Code files list contains only files with code extensions (.py, .js, .ts, etc.). If empty, no code files in PR. Diff file will be populated later in Task 7 if code files exist.

## Output Requirements

**Context Variables Created**:
- `pr_info_file`: Full path to PR info JSON file
- `pr_code_files_file`: Full path to code files list text file
- `pr_diff_file`: Full path to diff text file
- `extraction_success`: true/false

**Files Created**: 
- PR metadata JSON file
- Code files list text file
- PR diff text file (empty)

**Context Passed**: 
- File paths for metadata and code file detection
- PR extraction status for validation

## Success Criteria
- PR extraction script executes successfully
- All 3 files are created (info JSON, code files list, empty diff)
- File paths are captured and validated
- Files are accessible for next tasks