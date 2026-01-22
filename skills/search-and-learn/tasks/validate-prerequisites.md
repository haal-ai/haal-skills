---
task_id: "validate-prerequisites"
task_name: "Validate Prerequisites"
dependencies: ["context.learning_objective"]
conditions: []
---

# Validate Prerequisites

## Input Context
**Required Context Variables**: 
- `context.learning_objective`: User's learning goal
- `context.current_knowledge`: User's knowledge baseline
- `context.application_context`: Context and constraints
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Verify Requirements and Access

1. **Check Parameter Completeness**:
   - Verify all required parameters are provided and non-empty
   - Confirm learning_objective is specific enough to guide search

2. **Verify Tool Access**:
   - Confirm ability to perform web searches
   - Verify file system access for saving reports
   - Check template file availability (if applicable)

3. **Validate Scope**:
   - Ensure learning objective is achievable within session
   - Confirm no blocking prerequisites (e.g., specialized tools unavailable)

4. **Report Validation Status**:
   If all prerequisites met:
   ```
   ✅ Prerequisites validated successfully
   - Parameters: Complete
   - Tools: Available
   - Scope: Achievable
   ```
   
   If issues found, report them clearly for resolution.

## Output Requirements

**State Updates**:
- `context.prerequisites_met`: Boolean (true/false)
- `context.validation_notes`: Any warnings or confirmations (string)
- `task_status.validate-prerequisites`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Confirmation that execution can proceed to learning goals definition
