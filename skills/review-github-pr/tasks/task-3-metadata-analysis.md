---
task_id: "task-3"
task_name: "PR Metadata Analysis"
dependencies: []
conditions: []
---

# Task 3: PR Metadata Analysis

## Input Context
**Required State Variables**: 
- `context.pr_info_file`: Path to PR metadata JSON file
**Required Files**: PR info JSON file (must exist)
**Required Tools**: JSON parsing, file reading

## Task Instructions

### Read and Analyze PR Metadata ONLY
**CRITICAL**: Read ONLY the JSON metadata file - do NOT access the diff file in this step

1. **Read PR Info JSON File**:
   - Use file path from `context.pr_info_file`
   - Load complete JSON content using read_file tool
   - Parse JSON structure for metadata fields

2. **Extract Key Metadata**:
   - **Basic Info**: title, description (body), author, state
   - **Branch Info**: baseRefName, headRefName, number
   - **Statistics**: additions, deletions, changedFiles
   - **Files Array**: List of modified files with paths and stats
   - **Timestamps**: createdAt, updatedAt

3. **Validate Metadata Completeness**:
   - Ensure all required fields are present
   - Check for empty or null critical fields
   - Verify file statistics match files array

4. **Store for Analysis**:
   - Prepare metadata for downstream analysis
   - **BOUNDARY**: Metadata only - no code/diff content analysis

## Output Requirements

**State Updates**:
- `task_outputs.task-3.pr_metadata`: Complete parsed metadata object
- `task_outputs.task-3.metadata_valid`: boolean validation result
- `context.pr_title`: PR title string
- `context.pr_author`: Author information
- `context.files_list`: Array of file paths
- `task_status.task-3`: "completed"

**Files Created**: None

**Context Passed**: 
- Complete PR metadata for helper analysis
- File list for type detection
- Basic PR info for reporting

## Success Criteria
- PR metadata JSON successfully read and parsed
- All key metadata fields extracted
- Metadata validation completed
- Data prepared for next task analysis