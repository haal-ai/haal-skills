---
task_id: "validate-review-parameters"
task_name: "Validate Review Parameters and Environment"
dependencies: ["context.timestamp"]
conditions: []
---

# Validate Review Parameters and Environment

## Input Context
**Required Context Variables**: 
- `context.timestamp`: Session timestamp from environment retrieval
**Required Files**: None
**Required Tools**: Git repository access

## Task Instructions

### Parameter Validation and Environment Check

1. **Extract and Validate Parameters**:
   Collect optional parameters with defaults:
   - **diff_content**: string - Pre-collected diff content (OPTIONAL)
   - **review_scope**: string - Scope of review (OPTIONAL - default: "workspace")
     - Valid values: "workspace", "folder", "file"
   - **target_path**: string - Specific folder or file path (OPTIONAL - only if review_scope is folder/file)
   - **save_report**: boolean - Save report to staging directory (OPTIONAL - default: false)
   - **include_actions**: boolean - Include actionable fix commands (OPTIONAL - default: true)

2. **Environment Validation**:
   - **Git Repository Check**:
     - Confirm workspace is a git repository
     - Check if `.git` directory exists
     - Set `context.git_repo_valid = true` if valid
   
   - **Target Path Validation** (if specified):
     - Verify target_path exists in filesystem
     - Confirm it matches review_scope (file vs folder)
     - Store validated absolute path

3. **Parameter Storage**:
   Store validated parameters in context for subsequent tasks:
   - Store all parameters with applied defaults
   - Validate parameter combinations (e.g., target_path requires non-workspace scope)

## Output Requirements

**State Updates**:
- `context.diff_content`: Pre-provided diff content or null
- `context.review_scope`: Validated scope ("workspace", "folder", or "file")
- `context.target_path`: Validated absolute path or null
- `context.save_report`: Boolean flag
- `context.include_actions`: Boolean flag
- `context.git_repo_valid`: Boolean indicating git availability
- `task_status.validate-review-parameters`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- All review parameters available for diff collection
- Git repo validation determines if git commands can be used
