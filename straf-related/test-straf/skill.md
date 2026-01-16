---
name: test-straf
description: Test STRAF agent integration for code review
license: Apache-2.0
metadata:
  olaf_tags: [straf, code-review, test, agentic]
  olaf_protocol: Propose-Act
---

# STRAF Code Review Test - Master Chain

## Master Chain Protocol

**CRITICAL EXECUTION RULES**:
- Execute tasks in STRICT SEQUENTIAL ORDER
- Load only ONE task prompt at a time
- Pass context between tasks via simple variables
- NO anticipation or optimization across tasks
- Each task must complete fully before next

**STARTUP REQUIREMENT**:
Task Chain
Task 1: Detect language from code files
Task 2: Prepare code context for review
Task 3: Execute STRAF code review
Task 4: Display review results

## Task Chain Definition

```yaml
task_chain:
  - id: "detect-language"
    name: "Detect language from code files"
    prompt: "tasks/task-1-detect-language.md"
    required: true
    
  - id: "prepare-context"
    name: "Prepare code context for review"
    prompt: "tasks/task-2-prepare-context.md"
    required: true
    
  - id: "execute-straf"
    name: "Execute STRAF code review"
    prompt: "tasks/call-straf-agent.md"
    required: true
    
  - id: "display-results"
    name: "Display review results"
    prompt: "tasks/task-4-display-results.md"
    required: true
```

## Chain Execution Flow

### Task 1: Detect Language
- Examine file extensions in workspace
- Determine if files are Python (.py) or Go (.go)
- Store language and file list in context

### Task 2: Prepare Context
- Collect code files based on detected language
- Read file contents
- Prepare context array for STRAF

### Task 3: Execute STRAF
- Select appropriate review prompt based on language
- Call STRAF agent with code context
- Wait for review completion (interactive mode)

### Task 4: Display Results
- Read STRAF output
- Format and display review
- Provide summary

## Input Requirements

**User provides**:
- One or more code files (.py or .go) in the workspace
- OR specific file paths via context

## Output Delivered

- Comprehensive code review from STRAF agent
- Language-specific analysis
- Actionable recommendations
- Review saved in staging directory

## Success Criteria

- Language correctly detected
- STRAF agent executes successfully
- Review completed and displayed
- Output file preserved for reference
