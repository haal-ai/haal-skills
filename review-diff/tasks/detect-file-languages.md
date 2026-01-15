---
task_id: "detect-file-languages"
task_name: "Detect File Languages"
dependencies: ["context.diff_file_list"]
conditions: []
---

# Detect File Languages

## Input Context
**Required Context Variables**: 
- `context.diff_file_list`: Array of changed file paths from diff
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Analyze File Extensions and Categorize by Language

1. **Extract File Extensions**:
   For each file in `context.diff_file_list`:
   - Parse file extension (e.g., `.py`, `.cpp`, `.h`, `.java`, `.go`, `.js`)
   - Handle files without extensions
   - Identify special cases (e.g., Dockerfile, Makefile)

2. **Map Extensions to Languages**:
   Create language categories based on extension mappings:
   - **Python**: `.py`
   - **C++**: `.cpp`, `.cc`, `.cxx`, `.h`, `.hpp`
   - **Java**: `.java`
   - **Go**: `.go`
   - **JavaScript/TypeScript**: `.js`, `.ts`, `.jsx`, `.tsx`
   - **Other**: All other extensions

3. **Categorize Files by Language**:
   Build mapping structure:
   ```json
   {
     "python": ["file1.py", "file2.py"],
     "cpp": ["module.cpp", "header.h"],
     "java": ["Class.java"],
     "go": ["main.go"],
     "javascript": ["app.js"],
     "other": ["config.yaml", "README.md"]
   }
   ```

4. **Filter Out Exclusions**:
   Exclude files from review:
   - **Regression test files**: `*.play`, `*.gsv`
   - **Regression directories**: `/regression/`, `/test-data/`
   - Store excluded files separately for reporting

5. **Create Language Summary**:
   ```markdown
   **Language Detection Results**:
   - Python files: [count]
   - C++ files: [count]
   - Java files: [count]
   - Go files: [count]
   - JavaScript files: [count]
   - Other files: [count]
   - Excluded files: [count]
   ```

## Output Requirements

**State Updates**:
- `context.language_categories`: Array of detected languages
- `context.files_by_language`: Object mapping languages to file lists
- `context.excluded_files`: Array of excluded file paths with reasons
- `context.reviewable_file_count`: Count of files to be reviewed
- `task_status.detect-file-languages`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Language categorization for router-based analysis
- File lists for applying language-specific standards
