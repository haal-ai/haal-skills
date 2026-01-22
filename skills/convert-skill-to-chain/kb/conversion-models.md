# Master-Chain Conversion Models

**Document Version**: 1.0  
**Last Updated**: 2025-11-21  
**Purpose**: Provide conversion templates for each workflow pattern

---

## Model 1: Sequential Chain (Reference Implementation)

### Pattern Characteristics
- Linear task execution
- No loops or branches
- Each task runs exactly once

### Master Coordinator Template
```yaml
task_chain:
  - task_id: 0
    task_name: retrieve-timestamp
    task_file: ../../common/tasks/retrieve-timestamp.md
  
  - task_id: 1
    task_name: [first-task]
    task_file: tasks/[first-task].md
  
  # ... additional sequential tasks
  
  - task_id: N
    task_name: [final-task]
    task_file: tasks/[final-task].md
```

### State Management
```yaml
state_management:
  simple_context_passing:
    - timestamp: Session timestamp
    - [task_output_1]: Output from task 1
    - [task_output_2]: Output from task 2
    # ... additional context variables
```

### Execution Protocol
Standard sequential execution - no special handling required.

---

## Model 2: Cyclic/Iterative Pattern

### Pattern Characteristics
- Repeating task set (loop)
- Exit conditions (user, condition, max iterations)
- Loop state persists across iterations

### Master Coordinator Template
```yaml
workflow_type: cyclic

task_chain:
  # Pre-loop tasks
  - task_id: 0
    task_name: retrieve-timestamp
    task_file: ../../common/tasks/retrieve-timestamp.md
  
  - task_id: 1
    task_name: setup-cycle
    task_file: tasks/setup-cycle.md
    purpose: Initialize loop variables and constraints
  
  # LOOP DEFINITION
  loop_definition:
    loop_id: main_cycle
    loop_start_task: 2
    loop_end_task: 5
    max_iterations: 20  # Safety limit
    exit_condition_task: 5
    exit_condition_var: continue_loop
    exit_condition_value: "yes"  # Continue if "yes", exit if "no"
  
  # Loop tasks (execute repeatedly)
  - task_id: 2
    task_name: [iteration-task-1]
    task_file: tasks/[iteration-task-1].md
    loop_member: main_cycle
    loop_role: start
  
  - task_id: 3
    task_name: [iteration-task-2]
    task_file: tasks/[iteration-task-2].md
    loop_member: main_cycle
  
  - task_id: 4
    task_name: [iteration-task-3]
    task_file: tasks/[iteration-task-3].md
    loop_member: main_cycle
  
  - task_id: 5
    task_name: check-exit-condition
    task_file: tasks/check-exit-condition.md
    loop_member: main_cycle
    loop_role: decision
    # Sets continue_loop to "yes" or "no"
  
  # Post-loop tasks (after exit)
  - task_id: 6
    task_name: generate-summary
    task_file: tasks/generate-summary.md
    purpose: Final report after loop completion
```

### State Management
```yaml
state_management:
  loop_controls:
    - loop_id: main_cycle
      current_iteration: 0  # Auto-incremented
      max_iterations: 20
      exit_condition_var: continue_loop
      exit_value: "yes"
  
  loop_persistent_context:
    # Variables that accumulate across iterations
    - iteration_history: []  # List of results per iteration
    - cumulative_score: 0
    
  iteration_specific_context:
    # Variables reset each iteration
    - current_task_result: ""
    - iteration_feedback: ""
```

### Execution Protocol Extension
```
6. **Loop Execution**:
   a. Initialize loop controls (current_iteration = 0)
   b. Execute loop_start_task through loop_end_task
   c. Increment current_iteration
   d. Evaluate exit_condition_var at decision task
   e. If continue condition met AND current_iteration < max_iterations:
      - Jump back to loop_start_task
      - Carry forward loop_persistent_context
      - Reset iteration_specific_context
   f. If exit condition met OR max_iterations reached:
      - Proceed to post-loop tasks
   g. Display iteration progress to user each cycle
```

### check-exit-condition Task Template
```markdown
---
task_id: "check-exit-condition"
task_name: "Check Loop Exit Condition"
dependencies: ["iteration_results"]
---

# Task: Check Exit Condition

## Input Context
- {{current_iteration}}: Current loop iteration number
- {{max_iterations}}: Maximum allowed iterations
- {{iteration_results}}: Results from this iteration

## Execution
1. Evaluate exit criteria:
   - User decision (ask "Continue? (yes/no)")
   - Goal achievement (check performance threshold)
   - Iteration limit (check current_iteration >= max_iterations)

2. Set exit variable:
   - If should continue: continue_loop = "yes"
   - If should exit: continue_loop = "no"

3. Display to user:
   ```
   Iteration {{current_iteration}} complete.
   Continue? {{continue_loop}}
   ```

## Output Variables
- {{continue_loop}}: "yes" or "no"
```

---

## Model 3: Session-Chained Workflow Pattern

### Pattern Characteristics
- Multiple independent sessions
- Handoff artifacts between sessions
- User-initiated continuation

### Master Coordinator Template
```yaml
workflow_type: session_chained

session_chain:
  - session_id: 1
    session_name: [stage-1-name]
    session_skill: [stage-1-skill-name]
    session_file: sub-workflows/[stage-1].md
    handoff_task: generate-stage-2-prompt
    handoff_artifacts:
      - [artifact-1].json
      - [artifact-2].md
  
  - session_id: 2
    session_name: [stage-2-name]
    session_skill: [stage-2-skill-name]
    session_file: sub-workflows/[stage-2].md
    depends_on_session: 1
    input_artifacts:
      - [artifact-1].json
      - [artifact-2].md
    handoff_task: generate-stage-3-prompt
    handoff_artifacts:
      - [artifact-3].json
  
  - session_id: 3
    session_name: [stage-3-name]
    session_skill: [stage-3-skill-name]
    session_file: sub-workflows/[stage-3].md
    depends_on_session: 2
    input_artifacts:
      - [artifact-3].json
    handoff_task: generate-final-report

# Each sub-workflow is a separate master-chain skill
```

### Sub-Workflow Structure
Each session file (e.g., `stage-1.md`) is a complete master-chain coordinator with its own task_chain.

### Handoff Task Template
```markdown
---
task_id: "generate-next-session-prompt"
task_name: "Generate Next Session Prompt"
dependencies: ["session_outputs"]
---

# Task: Generate Next Session Prompt

## Input Context
- {{session_outputs}}: Results from current session
- {{next_session_skill}}: Name of next sub-workflow
- {{handoff_artifacts}}: Files to preserve for next session

## Execution
1. Save session outputs to artifacts:
   - Create {{handoff_artifacts}} files
   - Include all necessary context

2. Generate continuation prompt:
   ```
   ========================================
   SESSION COMPLETE - Next Steps
   ========================================
   
   Run this command to continue:
   
   olaf execute {{next_session_skill}}
   
   Context Files:
   {{handoff_artifacts}}
   
   Objective:
   {{next_stage_goal}}
   
   ========================================
   ```

3. Display to user

## Output Variables
- {{next_prompt}}: Full prompt text
- {{handoff_complete}}: "yes"
- {{artifacts_saved}}: List of created files
```

### Execution Protocol Extension
```
7. **Session Execution**:
   - Execute only ONE session per invocation
   - At handoff task:
     a. Save all artifacts
     b. Generate continuation prompt
     c. Display to user
     d. STOP execution
   - User manually invokes next session
   - Next session loads input_artifacts
```

---

## Model 4: Conditional Branching Pattern

### Pattern Characteristics
- Decision point selects execution path
- Multiple optional branches
- Branches may converge

### Master Coordinator Template
```yaml
workflow_type: conditional

task_chain:
  # Pre-branch tasks
  - task_id: 0
    task_name: retrieve-timestamp
    task_file: common/tasks/retrieve-timestamp.md
  
  - task_id: 1
    task_name: [detection-task]
    task_file: tasks/[detection-task].md
    purpose: Determine which branch to execute
  
  # Branch decision
  - task_id: 2
    task_name: branch-decision
    task_file: tasks/branch-decision.md
    branch_controller: true
    branches:
      - name: branch_a
        condition_var: [decision_variable]
        condition_value: [value_a]
        target_task: 3
      - name: branch_b
        condition_var: [decision_variable]
        condition_value: [value_b]
        target_task: 4
      - name: default
        default: true
        target_task: 5
  
  # Branch A tasks
  - task_id: 3
    task_name: [branch-a-task]
    task_file: tasks/[branch-a-task].md
    branch_id: branch_a
    converge_to: 6
  
  # Branch B tasks
  - task_id: 4
    task_name: [branch-b-task]
    task_file: tasks/[branch-b-task].md
    branch_id: branch_b
    converge_to: 6
  
  # Default branch
  - task_id: 5
    task_name: [default-task]
    task_file: tasks/[default-task].md
    branch_id: default
    converge_to: 6
  
  # Convergence point
  - task_id: 6
    task_name: [common-continuation]
    task_file: tasks/[common-continuation].md
    purpose: All branches converge here
```

### State Management
```yaml
state_management:
  branch_controls:
    - decision_variable: [variable_name]
      evaluated_at_task: 2
      selected_branch: ""  # Populated at runtime
  
  branch_context:
    - branch_result: ""  # Output from executed branch
```

### Execution Protocol Extension
```
8. **Conditional Branching**:
   a. Execute tasks up to branch_controller
   b. At branch_controller:
      - Evaluate condition_var
      - Match against branch conditions
      - Select first matching branch (or default)
      - Store selected_branch
   c. Execute only selected branch's tasks
   d. Skip all other branch tasks
   e. Jump to converge_to task
   f. Continue sequential execution
```

### branch-decision Task Template
```markdown
---
task_id: "branch-decision"
task_name: "Branch Decision Controller"
dependencies: ["decision_variable"]
---

# Task: Branch Decision

## Input Context
- {{decision_variable}}: Value to evaluate
- {{branches}}: Available branch definitions

## Execution
1. Load branch definitions from master coordinator
2. Evaluate {{decision_variable}} against each branch condition
3. Select first matching branch (or default)
4. Set {{selected_branch}}
5. Display: "Branch selected: {{selected_branch}}"

## Output Variables
- {{selected_branch}}: Name of selected branch
- {{target_task_id}}: Next task to execute
```

---

## Model 5: Hybrid Patterns

### Pattern Characteristics
- Combines multiple pattern types
- Requires nested or sequential pattern application

### Common Hybrid Combinations

#### Hybrid 1: Cyclic + Conditional
**Use Case**: Loop with conditional branches inside iterations

```yaml
workflow_type: hybrid
primary_pattern: cyclic
secondary_pattern: conditional

task_chain:
  # Setup
  - task_id: 0
    task_name: retrieve-timestamp
    task_file: common/tasks/retrieve-timestamp.md
  
  # Loop with conditional inside
  loop_definition:
    loop_id: main_cycle
    loop_start_task: 1
    loop_end_task: 5
    max_iterations: 10
  
  - task_id: 1
    task_name: iteration-setup
    task_file: tasks/iteration-setup.md
    loop_member: main_cycle
  
  # Conditional branch INSIDE loop
  - task_id: 2
    task_name: branch-decision
    task_file: tasks/branch-decision.md
    loop_member: main_cycle
    branch_controller: true
    branches:
      - condition_var: difficulty_level
        condition_value: "easy"
        target_task: 3
      - condition_var: difficulty_level
        condition_value: "hard"
        target_task: 4
  
  - task_id: 3
    task_name: easy-challenge
    task_file: tasks/easy-challenge.md
    loop_member: main_cycle
    branch_id: easy
    converge_to: 5
  
  - task_id: 4
    task_name: hard-challenge
    task_file: tasks/hard-challenge.md
    loop_member: main_cycle
    branch_id: hard
    converge_to: 5
  
  - task_id: 5
    task_name: check-exit
    task_file: tasks/check-exit.md
    loop_member: main_cycle
    loop_role: decision
  
  # Post-loop
  - task_id: 6
    task_name: generate-summary
    task_file: tasks/generate-summary.md
```

**Execution**: Each loop iteration includes a conditional branch selection.

#### Hybrid 2: Sequential + Conditional
**Use Case**: Linear flow with optional enhancement steps

```yaml
workflow_type: hybrid
primary_pattern: sequential
secondary_pattern: conditional

task_chain:
  - task_id: 0
    task_name: core-task-1
    task_file: tasks/core-task-1.md
  
  - task_id: 1
    task_name: core-task-2
    task_file: tasks/core-task-2.md
  
  # Optional branch based on results
  - task_id: 2
    task_name: enhancement-decision
    task_file: tasks/enhancement-decision.md
    branch_controller: true
    branches:
      - condition_var: needs_enhancement
        condition_value: "yes"
        target_task: 3
      - default: true
        target_task: 4
  
  - task_id: 3
    task_name: apply-enhancement
    task_file: tasks/apply-enhancement.md
    branch_id: enhancement
    converge_to: 4
  
  - task_id: 4
    task_name: finalize
    task_file: tasks/finalize.md
```

#### Hybrid 3: Session-Chained + Cyclic
**Use Case**: Multi-session workflow where each session has iterative stages

Each session sub-workflow uses cyclic pattern internally while the main coordinator uses session-chained pattern.

---

## Pattern Selection Logic

### Decision Tree
```
1. Does skill have multiple sessions with handoffs?
   YES → session-chained (may have nested patterns in sub-workflows)
   NO → Continue

2. Does skill have repeating task sets?
   YES → Check for branches inside loop
      YES → hybrid (cyclic + conditional)
      NO → cyclic
   NO → Continue

3. Does skill have conditional branches?
   YES → Check for loops
      YES → hybrid (conditional + cyclic) [unusual]
      NO → conditional
   NO → sequential
```

### Hybrid Pattern Strategy
For hybrid patterns:
1. Identify **dominant pattern** (usually the outer structure)
2. Identify **nested pattern** (usually inside iterations or branches)
3. Apply dominant pattern template first
4. Embed nested pattern within appropriate tasks

---

## Conversion Workflow Integration

When detect-workflow-pattern returns `detected_pattern`:

1. **Sequential**: Use existing conversion logic (current implementation)
2. **Cyclic**: Apply Model 2 template, create loop control tasks
3. **Session-Chained**: Apply Model 3 template, create sub-workflow files
4. **Conditional**: Apply Model 4 template, create branch decision logic
5. **Hybrid**: Apply dominant pattern template, embed nested pattern

---

**End of Document**
