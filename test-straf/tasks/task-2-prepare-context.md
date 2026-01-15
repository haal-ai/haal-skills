---
task_id: "task-2"
task_name: "Prepare Code Context for STRAF"
dependencies: ["detect-language"]
conditions: []
---

# Task 2: Prepare Code Context for STRAF

## Input Context
**Required State Variables**: 
- `context.detected_language`: "python" or "go"
- `context.code_files`: Array of file paths to review
- `context.code_file_count`: Number of files
- `context.timestamp`: Session timestamp

**Required Files**: Code files specified in `context.code_files`
**Required Tools**: File reading capabilities

## Task Instructions

### Step 0: Detect Project Root

1. **Find project root**:
   - Search upward for `.git` directory
   - Store absolute path in `context.project_root`
   - This ensures correct path resolution for STRAF wrapper

### Step 1: Select STRAF Prompt Based on Language

1. **Determine prompt path**:
   - If `context.detected_language` == "python":
     - Set `context.straf_prompt` = "review-python-code.md"
   - If `context.detected_language` == "go":
     - Set `context.straf_prompt` = "review-go-code.md"

2. **Verify prompt exists**:
   - Check if file exists at `~/.olaf/core/agentic/straf/prompts/[prompt_name]`
   - If not found: Report error

### Step 2: Build Full Prompt Path

1. **Build absolute prompt path**:
   - Combine: `~/.olaf/core/agentic/straf/prompts/{context.straf_prompt}`
   - Store in `context.straf_prompt_full_path`
   - Verify file exists at this path

### Step 3: Build Context File with Code Content

1. **Create context file path**:
   - Path: `.olaf/work/staging/straf-context-{context.timestamp}.txt`
   - Store in `context.straf_context_file_path`

2. **Read and concatenate all code files**:
   - For each file in `context.code_files`:
     - Read entire file content
     - Format: `=== File: {file_path} ===\n{content}\n\n`
     - Append to context file

3. **Write context file**:
   - Save concatenated content to `context.straf_context_file_path`
   - This file will be passed to STRAF wrapper

### Step 4: Prepare Context Files Array (LEGACY)

1. **Set context files**:
   - Assign `context.straf_context_files` = `context.code_files`
   - This array will be passed to STRAF agent

2. **Set execution mode**:
   - Set `context.straf_mode` = "interactive"
   - Interactive mode ensures we wait for results

### Step 5: Verify File Accessibility

1. **Check each file exists**:
   - For each file in `context.code_files`:
     - Verify file is accessible
     - Check file size (warn if > 100KB per file)

2. **Calculate total context size**:
   - Sum all file sizes
   - If total > 500KB: Warn user and ask to proceed or reduce files

## Output Requirements

**State Updates**:
- `context.straf_prompt`: Prompt file name for STRAF
- `context.straf_prompt_full_path`: Absolute path to prompt file
- `context.straf_context_file_path`: Path to context file with code content
- `context.project_root`: Absolute path to project root
- `context.straf_context_files`: Array of file paths for STRAF (legacy)
- `context.straf_mode`: "interactive"
- `task_status.prepare-context`: "completed"

**Display to User**:
```
📝 Preparing STRAF Context
========================
Language: [detected_language]
Review Prompt: [straf_prompt]
Files to review: [code_file_count]
Execution Mode: Interactive (will wait for results)
```

**Context Passed**: 
- STRAF prompt path
- Context files array
- Execution mode for Task 3

## Success Criteria
- Correct prompt selected for language
- Context files array populated
- All files accessible
- Ready to execute STRAF agent

## Error Handling
- If prompt not found: Report missing prompt error
- If files inaccessible: Report which files are missing
- If context too large: Request user confirmation or file reduction


