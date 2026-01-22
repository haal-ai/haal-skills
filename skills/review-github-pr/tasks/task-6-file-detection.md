---
task_id: "task-6"
task_name: "File Type Detection"
dependencies: []
conditions: []
---

# Task 6: File Type Detection

## Input Context
**Required State Variables**: 
- `context.pr_code_files_file`: Path to code files list text file
**Required Files**: Code files list text file (must exist)
**Required Tools**: File reading

## Task Instructions

### Check Code Files List
**SIMPLE CHECK**: Just verify if code files list exists and has content

1. **Read Code Files List**:
   - Use file path from `context.pr_code_files_file`
   - Read complete file content using read_file tool
   - File format: One file path per line (or empty if no code files)

2. **Determine Code Presence**:
   - If file is empty (0 lines or only whitespace): NO code files
   - If file has content (file paths listed): YES code files
   - Store list of code file paths if present

3. **Make Branch Decision**:
   - **Code Files Found**: Set condition for code review workflow
   - **No Code Files**: Set condition for documentation review workflow

## Output Requirements

**State Updates**:
- `context.code_files_found`: boolean (true if file has content, false if empty)
- `context.code_file_paths`: array of code file paths (empty array if none)
- `context.code_file_count`: number of code files
- `task_status.task-6`: "completed"

**Files Created**: None

**Context Passed**: 
- File type determination for branching logic
- Code file paths list for diff filtering
- Branch direction for downstream workflow selection

## Success Criteria
- Code files list successfully read
- Code vs non-code determination is made
- File paths captured (if any)
- Branch condition is set for next task selection