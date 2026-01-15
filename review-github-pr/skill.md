---
name: review-github-pr
description: Master coordinator for chained GitHub Pull Request review execution
license: Apache-2.0
metadata:
  olaf_tags: [code-review, github, pull-request, master-chain]
  olaf_protocol: Propose-Act
---

# GitHub PR Review - Master Chain Coordinator

## Master Chain Protocol

**CRITICAL EXECUTION RULES**:
- Execute tasks in STRICT SEQUENTIAL ORDER
- Load only ONE task prompt at a time
- Pass context between tasks via simple variables
- NO anticipation or optimization across tasks
- Each task must complete fully before next

**STARTUP REQUIREMENT**:
Task Chain
Task 1: Select which Pull Request to analyze
Task 2: Get PR Data from GitHub (metadata and Diff)
Task 3: Load PR Metadata for analysis
Task 4: Get analyzer for metadata and do the analysis
Task 5: Get Diff data for potential analysis
Task 6: Detect if code files are in the diff
Task 7: Do code analysis (if code files are present) [CONDITIONAL]
Task 8: Review Documentation [CONDITIONAL]
Task 9: Cleanup temporary extraction files
Task 10: Ask user what output he/she/it wants
Task 11: Generate Final Report

## Task Chain Definition

```yaml
task_chain:
  - id: "select-pr" 
    name: "Select which Pull Request to analyze"
    prompt: "tasks/select-pr.md"
    required: true
    
  - id: "extract-pr-data"
    name: "Get PR Data from GitHub (metadata and Diff)" 
    prompt: "tasks/extract-pr-data.md"
    required: true
    depends_on: ["select-pr"]
    
  - id: "analyze-metadata"
    name: "Load PR Metadata for analysis"
    prompt: "tasks/analyze-metadata.md" 
    required: true
    depends_on: ["extract-pr-data"]
    
  - id: "analyze-pr-standards"
    name: "Get analyzer for metadata and do the analysis"
    prompt: "tasks/analyze-pr-standards.md"
    required: true 
    depends_on: ["analyze-metadata"]
    
  - id: "prepare-diff"
    name: "Get Diff data for potential analysis"
    prompt: "tasks/prepare-diff.md"
    required: true
    depends_on: ["extract-pr-data"]
    
  - id: "detect-file-types"
    name: "Detect if code files are in the diff"
    prompt: "tasks/detect-file-types.md"
    required: true
    depends_on: ["analyze-metadata", "prepare-diff"]
    
  - id: "review-code"
    name: "Do code analysis (if code files are present)"
    prompt: "tasks/review-code.md"
    required: false
    depends_on: ["detect-file-types"]
    condition: "code_files_found"
    
  - id: "review-documentation"
    name: "Review Documentation"
    prompt: "tasks/review-documentation.md" 
    required: false
    depends_on: ["detect-file-types"]
    condition: "no_code_files"
    
  - id: "cleanup-extraction-files"
    name: "Cleanup temporary extraction files"
    prompt: "tasks/cleanup-extraction-files.md"
    required: true
    depends_on: ["review-code", "review-documentation"]
    
  - id: "select-output-method"
    name: "Ask user what output he/she/it wants"
    prompt: "tasks/select-output-method.md"
    required: true
    depends_on: ["cleanup-extraction-files"]
    
  - id: "generate-report"
    name: "Generate Final Report"
    prompt: "tasks/generate-report.md"
    required: false
    depends_on: ["select-output-method"]
    condition: "output_not_skipped"
```

## State Management

### Simple Context Passing
Context is passed between tasks using simple variables:
- `timestamp`: Session timestamp (YYYYMMDD-HHMMSS)
- `pr_number`: Selected PR number
- `pr_info_file`: Path to PR metadata JSON
- `pr_diff_file`: Path to diff text file  
- `code_files_found`: Boolean for code vs documentation
- `review_type`: "code" or "documentation"
- `review_summary`: Brief review text
- `recommendation`: "APPROVE" or "REQUEST_CHANGES"
- `skip_report`: Boolean to skip Task 11 (set by Task 10)

## Master Execution Protocol

### 1. Initialize Session
Initialize session context for tracking.

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

### 5. Session Recovery
Tasks are independent - no session recovery needed.
Each execution starts fresh with environment info.

## Task Prompt Requirements

Each task prompt MUST include:

### Header Structure
```markdown
---
task_id: "task-X"
task_name: "[descriptive name]"
dependencies: ["context-variable-Y", "context-variable-Z"]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

# Task X: [Name]

## Input Context
**Required Context Variables**: [list]
**Required Files**: [list] 
**Required Tools**: [list]

## Task Instructions
[focused task-specific instructions]

## Output Requirements
**Context Variables Created**: [what to store]
**Files Created**: [list]
**Context Passed**: [what next tasks need]
```

### Focus Principles
- **Single Responsibility**: Each task does ONE thing only
- **Clear Boundaries**: Explicit input/output definitions
- **No Forward References**: No mention of future tasks
- **Context Driven**: Use only provided context variables
- **Atomic Completion**: Complete task or fail, no partial states



