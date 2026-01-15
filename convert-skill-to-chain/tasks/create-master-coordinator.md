---
task_id: "create-master-coordinator"
task_name: "Create Master Coordinator Prompt"
dependencies: ["context.task_boundaries", "context.extracted_tasks", "detected_pattern", "pattern_metadata"]
conditions: []
---

# Create Master Coordinator Prompt

## Input Context
**Required Context Variables**: 
- `context.skill_name`: Name of skill
- `context.skill_path`: Path to skill directory
- `context.task_boundaries`: Complete task chain definition
- `context.extracted_tasks`: Created task files
- `detected_pattern`: Detected workflow pattern (sequential|cyclic|session-chained|conditional|hybrid)
- `pattern_metadata`: Pattern-specific details
**Required Files**: 
- `skills/convert-skill-to-chain/kb/conversion-models.md`
**Required Tools**: File creation

## Task Instructions

### 1. Load Conversion Model

Read pattern-specific template:
```
skills/convert-skill-to-chain/kb/conversion-models.md
```

Select model based on `detected_pattern`:
- **sequential** → Model 1: Sequential Chain
- **cyclic** → Model 2: Cyclic/Iterative Pattern
- **session-chained** → Model 3: Session-Chained Workflow
- **conditional** → Model 4: Conditional Branching
- **hybrid** → Model 5: Hybrid Patterns (select based on `pattern_metadata.dominant_pattern`)

### 2. Generate Master Coordinator File

1. **Create Master Coordinator Path**:
   - File: `skills/[skill-name]/prompts/[skill-name].md`
   - This will replace original skill prompt (backup already created)

2. **Apply Pattern-Specific Template**:

   **For Sequential Pattern** (Model 1):
   - Use standard task_chain YAML
   - Simple state_management section
   - Standard execution protocol
   
   **For Cyclic Pattern** (Model 2):
   - Add `workflow_type: cyclic`
   - Include `loop_definition` section with:
     - `loop_id`, `loop_start_task`, `loop_end_task`
     - `max_iterations`, `exit_condition_var`
   - Add `loop_controls` to state_management
   - Extend execution protocol with loop handling
   
   **For Session-Chained Pattern** (Model 3):
   - Add `workflow_type: session_chained`
   - Replace task_chain with `session_chain`
   - List sub-workflow files
   - Define handoff tasks and artifacts
   - Update execution protocol for session boundaries
   
   **For Conditional Pattern** (Model 4):
   - Add `workflow_type: conditional`
   - Mark branch_controller task
   - Define branches with conditions
   - Add `branch_controls` to state_management
   - Extend execution protocol with branching logic
   
   **For Hybrid Patterns** (Model 5):
   - Combine templates based on component patterns
   - Apply dominant pattern as outer structure
   - Embed nested pattern within appropriate tasks
   - Document pattern interactions in comments

3. **Base Template Structure** (all patterns):
   
   ```markdown
   ---
   name: [skill-name]
   description: Master coordinator for [skill purpose]
   tags: [relevant, tags, master-chain]
   protocol: Propose-Act
   ---

   # [Skill Name] - Master Chain Coordinator

   ## Master Chain Protocol

   **CRITICAL EXECUTION RULES**:
   - ALWAYS display the complete task list at the start of execution
   - Execute tasks in STRICT SEQUENTIAL ORDER
   - Load only ONE task prompt at a time
   - Pass context between tasks via simple variables
   - NO anticipation or optimization across tasks
   - Each task must complete fully before next

   **STARTUP REQUIREMENT**:
   Before executing any tasks, MUST display:
   ```
   📋 [Skill Name] - Task Chain
   ================================
   Task 0: [task 0 name]
   Task 1: [task 1 name]
   ...
   ================================
   ```

   ## Task Chain Definition

   [INSERT PATTERN-SPECIFIC YAML]

   ## State Management

   [INSERT PATTERN-SPECIFIC STATE MANAGEMENT]

   ## Master Execution Protocol
   
   [INSERT PATTERN-SPECIFIC EXECUTION PROTOCOL]

   ## Task Prompt Requirements
   [Standard requirements - same for all patterns]
   ```

4. **Generate Task Chain YAML**:
   - Convert `context.task_boundaries` to appropriate YAML format
   - For sequential: standard task_chain
   - For cyclic: add loop markers and loop_definition
   - For session-chained: create session_chain
   - For conditional: add branch definitions
   - **CRITICAL**: Set correct `prompt` paths:
     - Common tasks: `../../common/tasks/[task-name].md`
     - Skill-specific tasks: `tasks/[task-name].md`
   - Define `depends_on` based on task dependencies

5. **Document State Variables**:
   - Extract all input/output variables from tasks
   - Add pattern-specific control variables
   - Create comprehensive state management section
   - Document variable flow through chain

## Output Requirements

**State Updates**:
- `context.master_file`: Path to created master coordinator
- `context.master_created`: true
- `task_status.create-master-coordinator`: "completed"

**Files Created**: 
- `skills/[skill-name]/prompts/[skill-name].md`

**Context Passed to Next Tasks**:
- Master file path for summary reporting
