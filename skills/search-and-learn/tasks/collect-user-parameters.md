---
task_id: "collect-user-parameters"
task_name: "Collect User Parameters"
dependencies: ["context.timestamp"]
conditions: []
---

# Collect User Parameters

## Input Context
**Required Context Variables**: 
- `context.timestamp`: Session timestamp
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Request and Validate Input Parameters

1. **Request Required Parameters**:
   Present user with parameter requirements:
   ```
   **Search and Learn - Required Parameters**
   
   Please provide the following information:
   
   1. **Learning Objective**: 
      What specific question, skill, problem, or topic do you want to understand?
   
   2. **Current Knowledge**: 
      What is your current knowledge level and previous experience with this topic?
   
   3. **Application Context**: 
      What related skills, time constraints, or application context should I consider?
   ```

2. **Collect User Responses**:
   - Wait for user to provide all three parameters
   - If any parameter is missing, request it specifically

3. **Validate Parameters**:
   - Ensure learning_objective is specific and clear
   - Confirm current_knowledge provides useful baseline
   - Verify application_context gives necessary constraints

4. **Store Parameters**:
   - Save validated parameters to context for subsequent tasks

## Output Requirements

**State Updates**:
- `context.learning_objective`: User's specific learning goal (string)
- `context.current_knowledge`: User's knowledge baseline (string)
- `context.application_context`: Context and constraints (string)
- `task_status.collect-user-parameters`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- All three parameters will be used in validate-prerequisites and define-learning-goals tasks
