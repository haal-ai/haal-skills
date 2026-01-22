---
task_id: "select-pr"
task_name: "PR Selection"
dependencies: []
conditions: []
---

# Select Pull Request to Review

## Input Context
**Required Context Variables**: 
- `timestamp`: Timestamp (if available from environment, optional)
**Required Files**: None
**Required Tools**: User interaction

## Task Instructions

### Get PR Number from User
**CRITICAL**: Never assume which PR to review. Always explicitly ask the user.

1. **Present Options to User**:
```
**PR Selection Required**: Which PR should I review?

**Options**:
- Specific PR number (e.g., "PR 123")
- Latest open PR (whatever branch)

Please specify the PR to review.
```

2. **Parse User Response**:
   - If user provides number: extract and validate
   - If user says "latest": set flag for latest PR discovery
   - If unclear: ask for clarification

3. **Validate Selection**:
   - Ensure PR number is numeric (if provided)
   - Confirm user intent before proceeding

## Output Requirements

**Context Variables Created**:
- `pr_number`: The selected PR number (string)
- `pr_selection_mode`: "specific" or "latest"
- `user_confirmed`: true

**Files Created**: None

**Context Passed**: 
- PR identifier for data extraction
- Selection mode for script execution

## Success Criteria
- User has provided clear PR selection
- PR number or latest flag is captured
- Selection is validated and confirmed