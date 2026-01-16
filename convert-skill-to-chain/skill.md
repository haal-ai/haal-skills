---
name: convert-skill-to-chain
description: Master coordinator for converting existing OLAF skills to the master-chain pattern
license: Apache-2.0
metadata:
  olaf_tags: [skill-conversion, refactoring, master-chain, automation]
  olaf_protocol: Propose-Act
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Convert Skill to Master Chain - Coordinator

## Master Chain Protocol

**CRITICAL EXECUTION RULES**:
- Execute tasks in STRICT SEQUENTIAL ORDER
- Load only ONE task prompt at a time
- Pass context between tasks via simple variables
- NO anticipation or optimization across tasks
- Each task must complete fully before next

**STARTUP REQUIREMENT**:
Task Chain
Task 1: Select skill to convert
Task 2: Backup original skill prompt
Task 3: Analyze existing skill structure
Task 4: Detect workflow pattern
Task 5: Evaluate if conversion is necessary
Task 6: Search for reusable common tasks
Task 7: Identify task boundaries
Task 8: Extract individual tasks
Task 9: Create master coordinator prompt
Task 10: Update task registry with new tasks
Task 11: Generate conversion summary

## Task Chain Definition

```yaml
task_chain:
  - id: "select-skill"
    name: "Select skill to convert"
    prompt: "tasks/select-skill.md"
    required: true
    
  - id: "backup-original-skill"
    name: "Backup original skill prompt"
    prompt: "tasks/backup-file.md"
    required: true
    depends_on: ["select-skill"]
    
  - id: "analyze-skill-structure"
    name: "Analyze existing skill structure"
    prompt: "tasks/analyze-skill-structure.md"
    required: true
    depends_on: ["backup-original-skill"]
    
  - id: "detect-workflow-pattern"
    name: "Detect workflow pattern"
    prompt: "tasks/detect-workflow-pattern.md"
    required: true
    depends_on: ["analyze-skill-structure"]
    
  - id: "evaluate-conversion-necessity"
    name: "Evaluate if conversion is necessary"
    prompt: "tasks/evaluate-conversion-necessity.md"
    required: true
    depends_on: ["detect-workflow-pattern", "analyze-skill-structure"]
    
  - id: "search-common-tasks"
    name: "Search for reusable common tasks"
    prompt: "tasks/search-common-tasks.md"
    required: true
    depends_on: ["evaluate-conversion-necessity"]
    
  - id: "identify-task-boundaries"
    name: "Identify task boundaries"
    prompt: "tasks/identify-task-boundaries.md"
    required: true
    depends_on: ["analyze-skill-structure", "search-common-tasks"]
    
  - id: "extract-tasks"
    name: "Extract individual tasks"
    prompt: "tasks/extract-tasks.md"
    required: true
    depends_on: ["identify-task-boundaries"]
    
  - id: "create-master-coordinator"
    name: "Create master coordinator prompt"
    prompt: "tasks/create-master-coordinator.md"
    required: true
    depends_on: ["extract-tasks"]
    
  - id: "update-task-registry"
    name: "Update task registry with new tasks"
    prompt: "tasks/update-task-registry.md"
    required: true
    depends_on: ["extract-tasks"]
    
  - id: "generate-summary"
    name: "Generate conversion summary"
    prompt: "tasks/generate-summary.md"
    required: true
    depends_on: ["create-master-coordinator", "update-task-registry"]
```

## State Management

### Simple Context Passing
Context is passed between tasks using simple variables:
- `skill_name`: Name of skill to convert
- `skill_path`: Path to skill directory
- `skill_prompt_file`: Path to main skill prompt
- `file_to_backup`: Set to skill_prompt_file for backup task
- `backup_file`: Path to backup of original skill
- `skill_structure`: Analysis of current structure
- `detected_pattern`: Detected workflow pattern (sequential|cyclic|session-chained|conditional|hybrid)
- `pattern_confidence`: Confidence level (high|medium|low)
- `pattern_metadata`: Pattern-specific details (loop boundaries, branches, sessions, etc.)
- `conversion_necessary`: Boolean flag indicating if conversion should proceed
- `conversion_reason`: Explanation of conversion decision
- `complexity_score`: Numeric complexity score (1-10)
- `conversion_model`: Selected conversion model based on detected pattern
- `common_tasks_found`: List of reusable common tasks
- `task_boundaries`: Identified task breakdown
- `extracted_tasks`: List of created task files
- `master_file`: Path to new master coordinator
- `registry_updated`: Boolean flag
- `conversion_summary`: Summary text

## Master Execution Protocol

### 1. Execute Task Chain Loop
For each task in task_chain:

1. **Load Task Prompt**: Read task-specific prompt file
2. **Check Dependencies**: Verify required context variables exist
3. **Execute Task**: Run task with available context
4. **Pass Context**: Make results available to next task
5. **Continue to Next**: Move to next task in chain

### 2. Task Execution Template
```markdown
**EXECUTING TASK: [task_name]**

**Context Available**:
- Previous Results: [available variables]

**Task-Specific Instructions**:
[load_and_execute_task_prompt]

**Context Updates**: 
- Store results in simple variables for next tasks
```

### 3. Error Handling
- **Task Failure**: Stop chain, report error
- **Missing Dependencies**: Show clear dependency requirements
- **Script Failures**: Display script output and exit
- **Conversion Not Necessary**: Stop chain after Task 5 if `conversion_necessary = false`
  - Display decision message clearly
  - Explain why conversion is skipped
  - Exit gracefully without error status

## Early Termination Protocol

**When Task 5 (evaluate-conversion-necessity) determines conversion is not needed**:

1. Display the decision message from Task 5
2. Show final summary:
   ```
  Analysis Complete - No Conversion Needed
   ============================================
   Skill: {{skill_name}}
   Complexity: {{complexity_score}}/10
   
   This skill remains as a single-prompt implementation.
   No further action required.
   ```
3. STOP chain execution (do NOT proceed to Tasks 6-11)
4. Return success status (this is not an error condition)

## Task Prompt Requirements

Each task prompt MUST include:

### Header Structure
```markdown
---
task_id: "task-name"
task_name: "[descriptive name]"
dependencies: ["context-variable-Y"]
---

# Task: [Name]

## Input Context
**Required Context Variables**: [list]
**Required Files**: [list] 
**Required Tools**: [list]

## Task Instructions
[focused task-specific instructions]

## Output Requirements
**Context Variables Created**: [what to store]
**Files Created**: [list]
```

### Focus Principles
- **Single Responsibility**: Each task does ONE thing only
- **Clear Boundaries**: Explicit input/output definitions
- **No Forward References**: No mention of future tasks
- **Context Driven**: Use only provided context variables
- **Atomic Completion**: Complete task or fail, no partial states

## Execution Instructions

When invoked, execute this pattern:

1. **Execute Task 1**: Load and run select-skill task
2. **Execute Task 2**: Load and run backup-original-skill task
3. **Execute Task 3**: Load and run analyze-skill-structure task
4. **Execute Task 4**: Load and run detect-workflow-pattern task
5. **Execute Task 5**: Load and run evaluate-conversion-necessity task
   - **CRITICAL**: If `conversion_necessary = false`, STOP chain here
   - Display decision message and exit gracefully
   - Only proceed if `conversion_necessary = true`
6. **Execute Task 6**: Load and run search-common-tasks task
7. **Execute Task 7**: Load and run identify-task-boundaries task
8. **Execute Task 8**: Load and run extract-tasks task
9. **Execute Task 9**: Load and run create-master-coordinator task
10. **Execute Task 10**: Load and run update-task-registry task
11. **Execute Task 11**: Load and run generate-summary task

**NO SHORTCUTS**: Load each task prompt individually and execute completely before next task.
