---
task_id: "retrieve-timestamp"
task_name: "Environment Information Retrieval"
dependencies: []
conditions: []
---

# Retrieve Timestamp and Environment Information

## Input Context
**Required State Variables**: None (can be run standalone)
**Required Files**: None
**Required Tools**: `get-env.py` script

## Task Instructions

### Execute Environment Info Script and Read Data
1. **Run environment info script**:
   ```bash
   python skills/common/tools/get-env.py
   ```

2. **Find environment file in staging directory**:
   - Look for file: `.olaf/work/staging/olaf-env.txt`
   - Use read_file to access the file content
   - File format: Key-value pairs with timestamp and environment details

3. **Extract timestamp and environment info**:
   - Parse file content to get timestamp value
   - Extract format: `YYYYMMDD-HHMMSS`
   - Optionally collect OS, shell, and other environment details for context
   - Store timestamp value for subsequent tasks

4. **Keep environment file**:
   - DO NOT delete the olaf-env.txt file after reading
   - Leave file in staging directory for reference
   - File remains available throughout session

## Output Requirements

**State Updates**:
- `context.timestamp`: The extracted timestamp string (YYYYMMDD-HHMMSS)
- `context.environment_extracted`: true
- `context.os_info`: Operating system information
- `context.shell_info`: Shell information
- `task_status.retrieve-timestamp`: "completed"

**Files Created**: 
- olaf-env.txt file (permanent - not deleted)

**Context Passed**: 
- Timestamp for file naming in subsequent tasks
- Environment context for session tracking

## Success Criteria
- Environment script executes successfully
- Environment file located and read
- Timestamp value extracted and stored
- Environment file preserved in staging directory