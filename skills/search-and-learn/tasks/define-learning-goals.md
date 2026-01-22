---
task_id: "define-learning-goals"
task_name: "Define Learning Goals"
dependencies: ["context.learning_objective", "context.current_knowledge"]
conditions: []
---

# Define Learning Goals

## Input Context
**Required Context Variables**: 
- `context.learning_objective`: User's specific learning goal
- `context.current_knowledge`: User's knowledge baseline
- `context.application_context`: Context and constraints
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Clarify and Structure Learning Objectives

1. **Clarify Specific Learning Objectives**:
   - Parse the learning_objective into specific, measurable goals
   - Identify key concepts, skills, or knowledge to acquire
   - Prioritize objectives if multiple goals present

2. **Break Down Complex Topics**:
   - Identify major topics or sub-topics within the learning objective
   - Break complex topics into manageable components
   - Sequence components logically (foundational → advanced)

3. **Establish Success Criteria**:
   - Define what "understanding" means for this topic
   - Create measurable outcomes (e.g., "able to explain X", "can implement Y")
   - Align criteria with user's application context

4. **Set Scope Boundaries**:
   - Define what is IN scope (must learn)
   - Define what is OUT of scope (optional or future learning)
   - Consider time constraints from application context

5. **Create Goals Summary**:
   ```markdown
   **Learning Goals Defined**:
   
   Primary Goals:
   - [Goal 1]
   - [Goal 2]
   
   Success Criteria:
   - [Criterion 1]
   - [Criterion 2]
   
   Scope Boundaries:
   - In Scope: [topics]
   - Out of Scope: [topics]
   ```

## Output Requirements

**State Updates**:
- `context.learning_goals`: Array of specific learning goals
- `context.success_criteria`: Array of measurable success criteria
- `context.scope_boundaries`: Object with in_scope and out_of_scope arrays
- `task_status.define-learning-goals`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Learning goals will guide search strategy development
- Success criteria will be used in final validation
