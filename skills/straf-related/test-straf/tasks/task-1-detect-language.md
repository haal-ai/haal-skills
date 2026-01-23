---
task_id: "task-1"
task_name: "Detect Language from Code Files"
dependencies: []
conditions: []
---

# Task 1: Detect Language from Code Files

## Input Context
**Required State Variables**: 
- `context.timestamp`: Session timestamp (from Task 0)

**Optional Input**:
- User may provide file paths in the request
- User may mention specific language

**Required Files**: None
**Required Tools**: File search capabilities

## Task Instructions

### Step 1: Identify Code Files in Workspace

1. **Search for Python files**:
   - Use file_search tool with pattern: `**/*.py`
   - Exclude common non-code directories: `**/node_modules/**`, `**/__pycache__/**`, `**/venv/**`, `**/.venv/**`
   - Store found files in `python_files` array
   - Count Python files

2. **Search for Go files**:
   - Use file_search tool with pattern: `**/*.go`
   - Exclude test files if not reviewing tests: `**/*_test.go`
   - Store found files in `go_files` array
   - Count Go files

### Step 2: Determine Primary Language

1. **User-specified language**:
   - If user mentioned "Python" or ".py" → set language to "python"
   - If user mentioned "Go" or ".go" → set language to "go"

2. **Auto-detect from file counts**:
   - If Python files > Go files → set language to "python"
   - If Go files > Python files → set language to "go"
   - If both equal and both > 0 → ask user which to review
   - If no files found → report error and stop

### Step 3: Select Files for Review

1. **Filter by language**:
   - If language is "python": use `python_files` array
   - If language is "go": use `go_files` array

2. **Limit file count** (if too many):
   - If more than 10 files found:
     - Inform user about file count
     - Ask if they want to review all or specify files
     - Allow user to provide specific file paths
   - If 10 or fewer: proceed with all files

3. **Store selected files**:
   - Save final file list in `context.code_files` array
   - Save file count in `context.code_file_count`

## Output Requirements

**State Updates**:
- `context.detected_language`: "python" or "go"
- `context.code_files`: Array of absolute file paths to review
- `context.code_file_count`: Number of files to review
- `task_status.detect-language`: "completed"

**Display to User**:
```
🔍 Language Detection
===================
Detected: [language]
Files found: [count]
Files to review:
- [file 1]
- [file 2]
- [...]
```

**Context Passed**: 
- Language for prompt selection in Task 3
- File list for context preparation in Task 2

## Success Criteria
- Language detected successfully
- At least one code file identified
- File list stored and ready for next task

## Error Handling
- If no code files found: Report error and provide guidance
- If multiple languages: Ask user to clarify
- If file count too large: Request user input for filtering
