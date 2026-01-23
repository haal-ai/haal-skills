---
task_id: "select-output-method"
task_name: "Output Method Selection"
dependencies: []
conditions: []
---

# Select Output Method

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
(C) Skip report / I'm done
```

2. **Capture User Choice**:
   - Parse user response for A, B, or C
   - Handle variations like "A", "option A", "save", "screen", "display", "skip", "done", "none"
   - If user says "none", "skip", "done", or "I'm done" → treat as option C
   - Ask for clarification if unclear

3. **Validate Selection**:
   - Ensure valid option selected
   - If option C: skip to workflow completion (no Task 11)
   - Confirm choice before proceeding

## Output Requirements

**State Updates**:
- `context.output_method`: "save" or "display" or "skip"
- `context.user_output_choice`: "A" or "B" or "C"
- `context.output_confirmed`: true
- `context.skip_report`: true (if option C selected)
- `task_status.select-output-method`: "completed"

**Files Created**: None

**Context Passed**: 
- Output method for report generation formatting
- User preference for final output handling

## Success Criteria
- User has selected valid output method (A, B, or C)
- Choice is captured and validated
- If skip option (C) selected: workflow terminates after this task
- If output option (A or B) selected: method is ready for report generation