---
name: search-and-learn
description: Master coordinator for systematic information discovery, knowledge acquisition, and practical application with lean methodology
license: Apache-2.0
metadata:
  olaf_tags: [research, learning, information, knowledge, search, discovery, systematic, master-chain]
  olaf_protocol: Propose-Act
---

# Search and Learn - Master Chain Coordinator

## Master Chain Protocol

**CRITICAL EXECUTION RULES**:
- Execute tasks in STRICT SEQUENTIAL ORDER
- Load only ONE task prompt at a time
- Pass context between tasks via simple variables
- NO anticipation or optimization across tasks
- Each task must complete fully before next

**STARTUP REQUIREMENT**:
Task Chain
Task 1: Collect user parameters
Task 2: Validate prerequisites
Task 3: Define learning goals
Task 4: Develop search strategy
Task 5: Execute systematic search
Task 6: Evaluate and synthesize information
Task 7: Apply and test learning
Task 8: Generate learning report

## Task Chain Definition

```yaml
task_chain:
  - id: "collect-user-parameters"
    name: "Collect user parameters"
    prompt: "tasks/collect-user-parameters.md"
    required: true
    
  - id: "validate-prerequisites"
    name: "Validate prerequisites"
    prompt: "tasks/validate-prerequisites.md"
    required: true
    depends_on: ["collect-user-parameters"]
    
  - id: "define-learning-goals"
    name: "Define learning goals"
    prompt: "tasks/define-learning-goals.md"
    required: true
    depends_on: ["collect-user-parameters"]
    
  - id: "develop-search-strategy"
    name: "Develop search strategy"
    prompt: "tasks/develop-search-strategy.md"
    required: true
    depends_on: ["define-learning-goals"]
    
  - id: "execute-systematic-search"
    name: "Execute systematic search"
    prompt: "tasks/execute-systematic-search.md"
    required: true
    depends_on: ["develop-search-strategy"]
    
  - id: "evaluate-synthesize-information"
    name: "Evaluate and synthesize information"
    prompt: "tasks/evaluate-synthesize-information.md"
    required: true
    depends_on: ["execute-systematic-search"]
    
  - id: "apply-test-learning"
    name: "Apply and test learning"
    prompt: "tasks/apply-test-learning.md"
    required: true
    depends_on: ["evaluate-synthesize-information"]
    
  - id: "generate-learning-report"
    name: "Generate learning report"
    prompt: "tasks/generate-learning-report.md"
    required: true
    depends_on: ["apply-test-learning"]
```

## State Management

### Simple Context Passing
Context is passed between tasks using simple variables:
- `timestamp`: Session timestamp (YYYYMMDD-HHMMSS)
- `environment_extracted`: Boolean flag for environment data
- `os_info`: Operating system information
- `shell_info`: Shell information
- `learning_objective`: User's specific learning goal
- `current_knowledge`: User's knowledge baseline
- `application_context`: Context and constraints
- `prerequisites_met`: Boolean flag for validation status
- `validation_notes`: Validation warnings or confirmations
- `learning_goals`: Array of specific learning goals
- `success_criteria`: Array of measurable success criteria
- `scope_boundaries`: Object with in_scope and out_of_scope arrays
- `search_queries`: Array of formulated search queries
- `information_sources`: Array of prioritized source types
- `search_sequence`: Ordered search plan
- `sources_found`: Array of source objects with URLs and metadata
- `raw_information`: Extracted key points and quotes
- `information_gaps`: Identified missing information
- `synthesized_knowledge`: Organized knowledge by topic/goal
- `key_insights`: Array of key insights and takeaways
- `concept_relationships`: Map of concept connections
- `credibility_assessment`: Confidence levels for different topics
- `practical_applications`: Array of use cases and examples
- `understanding_validation`: Success criteria assessment
- `actionable_takeaways`: Key insights and next steps
- `knowledge_gaps`: Remaining areas for future learning
- `report_file`: Path to created learning report
- `report_created`: Boolean flag for report creation

## Master Execution Protocol

### 1. Initialize Session
Get environment info and timestamp by executing Task 0.

### 2. Execute Task Chain Loop
For each task in task_chain:

1. **Load Task Prompt**: Read task-specific prompt file
2. **Check Dependencies**: Verify required context variables exist
3. **Execute Task**: Run task with available context
4. **Pass Context**: Make results available to next task
5. **Continue to Next**: Move to next task in chain

### 3. Task Execution Template
```markdown
**EXECUTING TASK: [task_name]**

**Context Available**:
- Session Timestamp: [timestamp]
- Previous Results: [available variables]

**Task-Specific Instructions**:
[load_and_execute_task_prompt]

**Context Updates**: 
- Store results in simple variables for next tasks
```

### 4. Error Handling
- **Task Failure**: Stop chain, report error
- **Missing Dependencies**: Show clear dependency requirements
- **Script Failures**: Display script output and exit

## Task Prompt Requirements

Each task prompt MUST include:

### Header Structure
```markdown
---
task_id: "task-name"
task_name: "[descriptive name]"
dependencies: ["context-variable-Y"]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
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

1. **Execute Task 1**: Load and run collect-user-parameters task
2. **Execute Task 2**: Load and run validate-prerequisites task
3. **Execute Task 3**: Load and run define-learning-goals task
4. **Execute Task 4**: Load and run develop-search-strategy task
5. **Execute Task 5**: Load and run execute-systematic-search task
6. **Execute Task 6**: Load and run evaluate-synthesize-information task
7. **Execute Task 7**: Load and run apply-test-learning task
8.  **Execute Task 8**: Load and run generate-learning-report task

**NO SHORTCUTS**: Load each task prompt individually and execute completely before next task.