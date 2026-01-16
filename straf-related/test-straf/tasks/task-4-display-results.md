---
task_id: "task-4"
task_name: "Display Review Results"
dependencies: ["execute-straf"]
conditions: []
---

# Task 4: Display Review Results

## Input Context
**Required State Variables**: 
- `context.straf_result`: Agent execution result (from Task 3)
- `context.straf_output_file`: Path to output file
- `context.detected_language`: Language that was reviewed
- `context.code_file_count`: Number of files reviewed
- `context.straf_execution_mode`: Should be "interactive"

**Required Files**: STRAF output file at `context.straf_output_file`
**Required Tools**: None

## Task Instructions

### Step 1: Verify Results Available

1. **Check execution mode**:
   - Verify `context.straf_execution_mode` == "interactive"
   - If "spawned": Report that results are not yet available

2. **Verify result content**:
   - Check that `context.straf_result` is not empty
   - If empty: Read from `context.straf_output_file`

### Step 2: Format and Display Review

1. **Display review header**:
   ```
   ═══════════════════════════════════════════════════════
   🤖 STRAF Agent Code Review
   ═══════════════════════════════════════════════════════
   Language: [detected_language]
   Files Reviewed: [code_file_count]
   Review Type: Automated (STRAF Agent)
   ═══════════════════════════════════════════════════════
   ```

2. **Display full review content**:
   - Show complete `context.straf_result`
   - Preserve all formatting and structure

3. **Display output location**:
   ```
   
   ═══════════════════════════════════════════════════════
   📁 Review saved to: [straf_output_file]
   ═══════════════════════════════════════════════════════
   ```

### Step 3: Provide Summary Statistics

1. **Parse review content** (optional):
   - Count critical/major/minor issues if mentioned
   - Extract overall assessment if present

2. **Display quick stats** (if parsed):
   ```
   Quick Summary:
   - Overall Assessment: [assessment]
   - Critical Issues: [count]
   - Major Issues: [count]
   - Minor Issues: [count]
   ```

## Output Requirements

**State Updates**:
- `context.review_displayed`: true
- `task_status.display-results`: "completed"

**Display to User**:
- Complete formatted review from STRAF
- Output file location
- Optional summary statistics

**Files Referenced**: 
- STRAF output file (preserved for user reference)

## Success Criteria
- Review content displayed completely
- Output file location provided
- All formatting preserved
- User can access full review

## Error Handling
- If result empty: Attempt to read from output file
- If output file missing: Report error with expected path
- If parse errors: Display raw content anyway
