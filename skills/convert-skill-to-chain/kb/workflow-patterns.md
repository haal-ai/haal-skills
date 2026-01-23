# Workflow Patterns for Master-Chain Skills

**Document Version**: 1.0  
**Last Updated**: 2025-11-21  
**Purpose**: Define recognized workflow patterns that convert-skill-to-chain should handle

---

## Pattern Classification

The convert-skill-to-chain skill should recognize and support conversion of the following workflow patterns:

### 1. Sequential Chain Pattern (IMPLEMENTED)

**Description**: Linear execution of tasks in strict order, one after another.

**Characteristics**:
- Each task executes exactly once
- No branching or loops
- Context flows forward through variables
- Completion occurs after final task

**Current Implementation**: Fully supported
- Task chain defined in YAML `task_chain` section
- State management via `state_management` section
- Execution protocol enforces strict sequential order

**Example Skills**:
- `search-and-learn` (9 tasks)
- `review-github-pr` (reference pattern)

**Conversion Model**:
```yaml
task_chain:
  - task_id: 0
    task_name: retrieve-timestamp
    task_file: common/tasks/retrieve-timestamp.md
  - task_id: 1
    task_name: collect-user-parameters
    task_file: tasks/collect-user-parameters.md
  # ... sequential tasks
```

---

### 2. Cyclic/Iterative Pattern (NOT YET IMPLEMENTED)

**Description**: Workflow contains a repeating cycle of tasks that execute multiple times.

**Characteristics**:
- Defined set of tasks repeats in a loop
- Exit conditions determine when to stop:
  - Fixed iteration count (e.g., "run 5 times")
  - User decision (manual exit)
  - Conditional logic (e.g., "goal achieved")
- Loop state carries forward between iterations
- Safety limit prevents infinite loops

**Use Cases**:
- `challenge-me`: Repeated quiz cycles until user stops or mastery achieved
- Iterative refinement workflows
- Multi-round feedback processes
- Progressive learning stages

**Required Extensions**:
```yaml
task_chain:
  - task_id: 0
    task_name: setup-cycle
    task_file: tasks/setup-cycle.md
  
  # LOOP START MARKER
  - task_id: 1
    task_name: present-challenge
    task_file: tasks/present-challenge.md
    loop_start: true
    loop_id: main_cycle
  
  - task_id: 2
    task_name: evaluate-response
    task_file: tasks/evaluate-response.md
    loop_member: main_cycle
  
  - task_id: 3
    task_name: check-exit-condition
    task_file: tasks/check-exit-condition.md
    loop_member: main_cycle
    loop_decision: true
    # If continue_loop == "yes": loop back to task_id 1
    # If continue_loop == "no": proceed to task_id 4
    loop_back_to: 1
    loop_condition_var: continue_loop
    loop_condition_value: "yes"
  
  # LOOP END MARKER / POST-LOOP TASK
  - task_id: 4
    task_name: generate-final-report
    task_file: tasks/generate-final-report.md

state_management:
  loop_controls:
    - loop_id: main_cycle
      max_iterations: 10  # Safety limit
      current_iteration: 0  # Tracked automatically
      exit_condition_var: continue_loop
```

**Execution Protocol Additions**:
```
6. **Loop Handling**:
   - When loop_decision task completes, evaluate loop_condition_var
   - If condition met, increment current_iteration and jump to loop_back_to task
   - If max_iterations reached, force exit regardless of condition
   - If condition not met, proceed to next sequential task
   - Loop context variables persist across iterations
```

---

### 3. Session-Chained Workflow Pattern (NOT YET IMPLEMENTED)

**Description**: Major workflow that decomposes into multiple independent sub-workflows, each ending with prompt generation for next session.

**Characteristics**:
- Main workflow orchestrates high-level stages
- Each stage runs as separate sub-skill session
- Final task of each sub-workflow generates:
  - Next session prompt/instructions
  - Context handoff data
  - User guidance for continuation
- User manually initiates each subsequent session
- Cross-session state via file artifacts

**Use Cases**:
- Large multi-day projects
- Phased migrations or refactorings
- Review-then-implement workflows
- Discovery → Design → Implementation pipelines

**Architecture**:
```
Main Workflow: project-migration.md
├─ Stage 1 Session: analyze-codebase.md
│  └─ Final Task: generate-design-session-prompt.md
│     Output: "Run: olaf execute design-migration-plan with context from analysis-report.json"
│
├─ Stage 2 Session: design-migration-plan.md
│  └─ Final Task: generate-implementation-session-prompt.md
│     Output: "Run: olaf execute implement-migration with plan from migration-plan.json"
│
└─ Stage 3 Session: implement-migration.md
   └─ Final Task: generate-validation-session-prompt.md
      Output: "Run: olaf execute validate-migration with artifacts from implementation-results/"
```

**Required Extensions**:
```yaml
workflow_type: session_chained
session_chain:
  - session_id: 1
    session_skill: analyze-codebase
    session_file: sub-workflows/analyze-codebase.md
    handoff_task: generate-design-session-prompt
    handoff_artifacts:
      - analysis-report.json
      - codebase-inventory.md
  
  - session_id: 2
    session_skill: design-migration-plan
    session_file: sub-workflows/design-migration-plan.md
    depends_on_session: 1
    handoff_task: generate-implementation-session-prompt
    handoff_artifacts:
      - migration-plan.json
      - dependency-graph.md
  
  - session_id: 3
    session_skill: implement-migration
    session_file: sub-workflows/implement-migration.md
    depends_on_session: 2
    handoff_task: generate-validation-session-prompt
```

**Handoff Task Template**:
```markdown
# Task: Generate Next Session Prompt

## Input Variables
- {{session_outputs}}: Results from current session
- {{next_session_skill}}: Name of next sub-workflow

## Execution
1. Package session results into handoff artifacts
2. Generate prompt for next session:
   ```
   Execute: olaf {{next_session_skill}}
   Context: Load from {{artifact_paths}}
   Objective: {{next_stage_goal}}
   ```
3. Display user instructions for continuation
4. Mark current session complete

## Output Variables
- {{next_prompt}}: Full prompt for next session
- {{handoff_complete}}: "yes"
```

---

### 4. Conditional Branching Pattern (NOT YET IMPLEMENTED)

**Description**: Workflow executes different sub-workflows based on runtime conditions.

**Characteristics**:
- Decision point evaluates condition
- Different execution paths based on result
- Sub-workflows are optional (may not execute)
- Paths may converge back to main flow
- No loops, just branching logic

**Use Cases**:
- Error recovery workflows
- Platform-specific execution
- Optional enhancement steps
- Context-dependent processing

**Required Extensions**:
```yaml
task_chain:
  - task_id: 0
    task_name: detect-environment
    task_file: tasks/detect-environment.md
  
  - task_id: 1
    task_name: branch-decision
    task_file: tasks/branch-decision.md
    conditional_branch: true
    branches:
      - condition_var: platform_type
        condition_value: "windows"
        target_task: 2
      - condition_var: platform_type
        condition_value: "linux"
        target_task: 3
      - condition_var: platform_type
        condition_value: "macos"
        target_task: 4
      - default: true
        target_task: 5
  
  # Branch A: Windows-specific tasks
  - task_id: 2
    task_name: windows-setup
    task_file: tasks/windows-setup.md
    branch_id: windows_branch
    converge_to: 5
  
  # Branch B: Linux-specific tasks
  - task_id: 3
    task_name: linux-setup
    task_file: tasks/linux-setup.md
    branch_id: linux_branch
    converge_to: 5
  
  # Branch C: macOS-specific tasks
  - task_id: 4
    task_name: macos-setup
    task_file: tasks/macos-setup.md
    branch_id: macos_branch
    converge_to: 5
  
  # Convergence point
  - task_id: 5
    task_name: common-finalization
    task_file: tasks/common-finalization.md
```

**Execution Protocol Additions**:
```
7. **Conditional Branching**:
   - When conditional_branch task completes, evaluate all branch conditions
   - Execute first matching branch's target_task
   - Skip all other branch tasks
   - Jump to converge_to task when branch completes
   - If no conditions match, execute default branch
```

---

## Pattern Recognition Algorithm

When converting a skill, convert-skill-to-chain should:

### Phase 1: Pattern Detection
1. **Analyze skill structure**:
   - Count execution paths
   - Identify loop indicators (keywords: "repeat", "until", "while", "iterate")
   - Detect session markers (keywords: "next session", "handoff", "continue in")
   - Find conditional logic (keywords: "if", "based on", "depending on")

2. **Classify primary pattern**:
   - Sequential: Single linear path, no branches/loops
   - Cyclic: Contains repeating task set
   - Session-Chained: Multiple sub-skills with handoffs
   - Conditional: Multiple branches, no loops

### Phase 2: Apply Conversion Model
- **Pattern 1 (Sequential)**: Use current implementation
- **Pattern 2 (Cyclic)**: Apply loop extension model
- **Pattern 3 (Session-Chained)**: Apply session-chain model
- **Pattern 4 (Conditional)**: Apply branching model

### Phase 3: Validation
- Verify all execution paths terminate
- Check for infinite loop risks (add max_iterations)
- Ensure state variables are properly defined
- Validate handoff artifacts exist for session-chained

---

## Implementation Priority

**Phase 1** (Current): Sequential Chain
**Phase 2** (Next): Cyclic/Iterative Pattern
**Phase 3**: Conditional Branching Pattern  
**Phase 4**: Session-Chained Workflow Pattern

---

## Notes for Skill Enhancement

When extending convert-skill-to-chain:

1. **Backward Compatibility**: Ensure Pattern 1 (sequential) conversions remain unchanged
2. **Pattern Detection**: Add task "detect-workflow-pattern" before analysis
3. **Model Selection**: Choose conversion template based on detected pattern
4. **Validation**: Add pattern-specific validation tasks
5. **Registry**: Update task-registry.json with new loop/branch-aware tasks

---

**End of Document**
