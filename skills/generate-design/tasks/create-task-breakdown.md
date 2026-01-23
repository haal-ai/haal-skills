---
task_id: "create-task-breakdown"
task_name: "Create Task Breakdown"
dependencies: ["context.layer_definitions"]
conditions: []
---

# Create Task Breakdown

## Input Context
**Required Context Variables**: 
- `context.layer_definitions[]`: Complete layer architecture
- `context.output_file`: Where to save design document

## Task Instructions

### 1. Map Layers to Tasks

For each layer, create executable tasks:

**Task Granularity**:
- Simple layer → 1 task
- Complex layer → Multiple tasks (subtasks for layer phases)

**Task Structure**:
```
Task ID: Sequential number (0, 1, 2...)
Task Name: Action-oriented description
Layer: Which architecture layer
Input: Context variables and files needed
Processing: What the task does
Output: Files/artifacts created
Dependencies: Task IDs that must complete first
Execution Time: Estimate
Technology: Python | AI | Shell | Other
```

### 2. Describe Implementation Approach

For each task, specify implementation technology:
- **AI-based**: Tasks requiring LLM reasoning and generation
- **Script-based**: Deterministic processing (Python, Shell)
- **Manual**: Tasks requiring human decision-making
- **Hybrid**: Combination of automated and manual steps

**Note**: Do NOT generate STRAF commands or executable scripts at design stage.
These belong in Phase 4 (implementation planning).

### 3. Define Task Dependencies

Create dependency graph:
- Task 0 usually has no dependencies (initialization)
- Sequential tasks: Each depends on previous
- Parallel tasks: Same dependencies, can run concurrently
- Conditional tasks: Execute only if condition met

**Identify Critical Path**: Longest chain of sequential dependencies

**Identify Parallelizable Tasks**: Tasks with same dependencies

### 4. Calculate Total Timeline

Sum execution times:
- **Sequential path**: Add all tasks in critical path
- **Parallel execution**: Use max of concurrent tasks
- **Total estimate**: Critical path + any non-parallelizable tasks

## Output Requirements

**State Updates**:
- `context.task_breakdown[]`: Array of task objects, each with:
  - `task_id`: Sequential number
  - `task_name`: Descriptive name
  - `layer`: Which layer it implements
  - `input_variables[]`: Required context vars
  - `input_files[]`: Required file paths
  - `processing_description`: What it does
  - `output_files[]`: Created artifacts
  - `dependencies[]`: Task IDs to wait for
  - `execution_time`: Estimate
  - `technology`: Implementation approach (AI | Script | Manual | Hybrid)
  - `implementation_note`: High-level guidance on how to implement
  - `is_conditional`: Boolean
  - `condition_variable`: Variable to check (if conditional)
- `context.critical_path[]`: Task IDs in longest chain
- `context.parallelizable_tasks[]`: Groups of concurrent tasks
- `context.total_execution_time`: Sum estimate
- `task_status.create-task-breakdown`: "completed"

**User Display**:
```
📝 Task Breakdown Created

Total Tasks: [count]
Critical Path: [task count] tasks, [time] duration
Parallel Opportunities: [count] groups

Task List:
0. [name] - [layer] ([time])
1. [name] - [layer] ([time])
...
```
