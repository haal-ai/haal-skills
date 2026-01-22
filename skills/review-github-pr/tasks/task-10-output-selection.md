---
task_id: "task-10"
task_name: "Output Method Selection"
dependencies: []
conditions: []
---

# Task 10: Output Method Selection

## Input Context
**Required State Variables**: 
- `context.review_type`: "code" or "documentation"
- Review results available in context
**Required Files**: None
**Required Tools**: User interaction

## Task Instructions

### Ask User for Output Preference
**PURPOSE**: Determine how user wants to receive the review results

1. **Present Output Options**:
```
Review complete. Choose output: 
(A) Save to staging directory
(B) Display on screen
```

2. **Capture User Choice**:
   - Parse user response for A or B
   - Handle variations like "A", "option A", "save", "screen", "display"
   - Ask for clarification if unclear

3. **Validate Selection**:
   - Ensure valid option selected
   - Confirm choice before proceeding

## Output Requirements

**State Updates**:
- `context.output_method`: "save" or "display"
- `context.user_output_choice`: "A" or "B"
- `context.output_confirmed`: true
- `task_status.task-10`: "completed"

**Files Created**: None

**Context Passed**: 
- Output method for report generation formatting
- User preference for final output handling

## Success Criteria
- User has selected valid output method
- Choice is captured and validated
- Method is ready for report generation