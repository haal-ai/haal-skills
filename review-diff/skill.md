---
name: review-diff
description: Master coordinator for comprehensive code review of git diffs using language-specific standards
license: Apache-2.0
metadata:
  olaf_tags: [code-review, git, diff, quality, standards, workflow, master-chain]
  olaf_protocol: Propose-Act
---

# Review Diff - Master Chain Coordinator

## Master Chain Protocol

**CRITICAL EXECUTION RULES**:
- ALWAYS display the complete task list at the start of execution
- Execute tasks in STRICT SEQUENTIAL ORDER
- Load only ONE task prompt at a time
- Pass context between tasks via simple variables
- NO anticipation or optimization across tasks
- Each task must complete fully before next

You MUST ensure that underlying tasks (especially `load-practices-for-diff`
and `analyze-diff-with-router`) load and apply the same standards stack as
`review-code`:
- Repository practices from `.olaf/data/practices/practices/good-bad/*.md`.
- Any team- or language-specific standards in `.olaf/data/practices/standards/`.
- The **Universal Coding Standards** in
  `.olaf/data/practices/standards/universal-coding-standards.md`, treating the
  **Evolution/Refactoring Mode** as default for existing code and
  **Creation/New Code Mode** only when the diff introduces new modules.

**STARTUP REQUIREMENT**:
Before executing any tasks, MUST display:
```
📋 Review Diff - Git Code Review
================================
Task 0: Retrieve timestamp and environment info
Task 1: Validate review parameters and environment
Task 2: Collect git diff content
Task 3: Detect file languages
Task 4: Load repository practices for changed files
Task 5: Analyze diff with language router (applying practices first)
Task 6: Generate review report
================================
```

## Task Chain Definition

```yaml
task_chain:
  - id: "retrieve-timestamp"
    name: "Retrieve timestamp and environment info"
    prompt: "../../common/tasks/retrieve-timestamp.md"
    required: true
    
  - id: "validate-review-parameters"
    name: "Validate review parameters and environment"
    prompt: "tasks/validate-review-parameters.md"
    required: true
    depends_on: ["retrieve-timestamp"]
    
  - id: "collect-git-diff"
    name: "Collect git diff content"
    prompt: "tasks/collect-git-diff.md"
    required: true
    depends_on: ["validate-review-parameters"]
    
  - id: "detect-file-languages"
    name: "Detect file languages"
    prompt: "tasks/detect-file-languages.md"
    required: true
    depends_on: ["collect-git-diff"]
    
  - id: "load-practices-for-diff"
    name: "Load repository practices for changed files"
    prompt: "tasks/load-practices-for-diff.md"
    required: true
    depends_on: ["detect-file-languages"]
    
  - id: "analyze-diff-with-router"
    name: "Analyze diff with language router"
    prompt: "tasks/analyze-diff-with-router.md"
    required: true
    depends_on: ["load-practices-for-diff"]
    
  - id: "generate-review-report"
    name: "Generate review report"
    prompt: "tasks/generate-review-report.md"
    required: true
    depends_on: ["analyze-diff-with-router"]
```

## State Management

### Simple Context Passing
Context is passed between tasks using simple variables:
- `timestamp`: Session timestamp (YYYYMMDD-HHMMSS)
- `os_info`: Operating system information
- `shell_info`: Shell information

### Task 0 Outputs (retrieve-timestamp)
- `timestamp`: Extracted timestamp string
- `environment_extracted`: Boolean flag
- `os_info`: OS details
- `shell_info`: Shell details

### Task 1 Outputs (validate-review-parameters)
- `diff_content`: Pre-provided diff content or null
- `review_scope`: "workspace", "folder", or "file"
- `target_path`: Validated absolute path or null
- `save_report`: Boolean flag
- `include_actions`: Boolean flag
- `git_repo_valid`: Boolean indicating git availability

### Task 2 Outputs (collect-git-diff)
- `diff_text`: Complete diff content as string
- `diff_file_list`: Array of changed file paths
- `diff_empty`: Boolean flag (true if no changes)

### Task 3 Outputs (detect-file-languages)
- `language_categories`: Array of detected languages
- `files_by_language`: Object mapping languages to file lists
- `excluded_files`: Array of excluded file paths
- `reviewable_file_count`: Count of files to review

### Task 4 Outputs (analyze-diff-with-router)
- `findings`: Structured findings object (HIGH/MEDIUM/LOW)
- `security_issues`: Array of security findings
- `quality_issues`: Array of code quality issues
- `actionable_commands`: Array of fix commands
- `findings_count`: Total number of findings

### Task 5 Outputs (generate-review-report)
- `report_file`: Path to saved report (if saved)
- `actions_file`: Path to actions file (if saved)
- `report_displayed`: Boolean flag
- `report_summary`: Summary statistics object

## Master Execution Protocol

### 1. Initialize Session
Display task list (mandatory startup requirement).

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
- **Empty Diff**: Complete gracefully with message if no changes detected
- **Git Not Available**: Error if git_repo_valid=false and diff_content not provided

## Execution Instructions

When invoked, execute this pattern:

1. **Display Task List** (mandatory startup)
2. **Execute Task 0**: Load and run retrieve-timestamp task
3. **Execute Task 1**: Load and run validate-review-parameters task
4. **Execute Task 2**: Load and run collect-git-diff task
5. **Execute Task 3**: Load and run detect-file-languages task
6. **Execute Task 4**: Load and run analyze-diff-with-router task
7. **Execute Task 5**: Load and run generate-review-report task

**NO SHORTCUTS**: Load each task prompt individually and execute completely before next task.

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

## Usage Examples

### Example 1: Review Workspace Changes
```
olaf review-diff
```
Uses defaults: workspace scope, display report, include actions

### Example 2: Review Specific Folder
```
olaf review-diff review_scope=folder target_path=src/
```

### Example 3: Save Report to File
```
olaf review-diff save_report=true
```
Saves to: `.olaf/work/staging/diff-reviews/review-report-[timestamp].md`

### Example 4: Pre-provided Diff Content
```
olaf review-diff diff_content="[diff text]"
```
Uses provided diff instead of executing git diff
