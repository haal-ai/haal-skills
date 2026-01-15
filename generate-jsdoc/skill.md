---
name: generate-jsdoc
description: Generates inline JSDoc documentation for JavaScript and TypeScript files using AWS Strands multi-agent system. MODIFIES source code by adding comprehensive @param, @returns, @throws, @example, and @remarks comments. Runs in spawn mode to allow parallel work. Creates git branch by default for safety. Supports in-place modification or copy-to-folder mode.
license: Apache-2.0
metadata:
  olaf_protocol: "\"Propose-Confirm-Act\""
---

<olaf>

# Generate JSDoc Documentation

## Purpose
Generate comprehensive inline JSDoc comments for JavaScript/TypeScript source files using AWS Strands multi-agent system. **⚠️ MODIFIES SOURCE CODE** by adding JSDoc comments directly to files. Runs in spawn mode allowing the user to continue working while documentation generates in the background. **Git branch creation is DEFAULT for safety**.

## Execution Protocol: Propose-Confirm-Act

**Step 1 - Propose**: Present the execution plan with detected parameters
**Step 2 - Review**: Wait for user review and agreement ("ok" or feedback)
**Step 3 - Confirm**: Ask for final sign-off before execution
**Step 4 - Act**: Execute only after receiving final confirmation

## Input Parameters

### Optional Parameters
- `repo_folder`: Repository folder path to process
  - **Default**: Workspace root (use workspace detection)
  - **Format**: Absolute path (e.g., `c:\Users\...\haal-ide`)
  
- `output_mode`: Where to save JSDoc-documented files
  - **Default**: `in-place` (⚠️ MODIFIES source files directly in repo)
  - **Options**: `in-place` | `copy-to-folder`
  
- `output_folder`: Output directory for documented files (only if output mode is copy-to-folder)
  - **Default**: Repo folder (in-place modification)
  - **Format**: Absolute path
  
- `create_branch`: Create git branch before modification
  - **Default**: `true` (STRONGLY RECOMMENDED - auto-creates branch)
  - **Options**: `true` | `false`

## Workflow

### Step 1: Determine Repository Folder
```javascript
if (user_provided_repo) {
  repo_folder = resolve_absolute_path(user_provided_repo)
} else {
  repo_folder = workspace_root  // Use VS Code workspace root
}

// Validate repo folder exists
if (!fs.exists(repo_folder)) {
  ERROR: "Repository folder does not exist: {repo_folder}"
  EXIT
}
```

### Step 2: Determine Output Mode
```javascript
if (user_specified_output_folder) {
  output_mode = "copy-to-folder"
  output_folder = resolve_absolute_path(user_specified_output_folder)
} else {
  output_mode = "in-place"
  output_folder = repo_folder  // Same as repo (in-place modification)
}

// Create output directory if copy mode
if (output_mode === "copy-to-folder") {
  create_directory_recursive(output_folder)
}
```

### Step 3: Display Execution Plan with WARNINGS
```
════════════════════════════════════════════════════════════════════════════════
JSDOC INLINE DOCUMENTATION GENERATION (Spawn Mode)
════════════════════════════════════════════════════════════════════════════════
Repository:     {repo_folder}
Output Mode:    {output_mode}
Output Folder:  {output_folder}
Git Branch:     {branch_name} (auto-created unless --no-branch specified)
Mode:           Asynchronous (you can continue working)
════════════════════════════════════════════════════════════════════════════════

⚠️  CRITICAL WARNINGS:
{if output_mode === "in-place"}
  ⚠️  IN-PLACE MODE: Source files will be MODIFIED directly!
  ⚠️  .js and .ts files will have JSDoc comments added
  ⚠️  Git branch creation is ENABLED by default for safety
  ⚠️  Recommend committing current work before proceeding
{else}
  ℹ️  COPY MODE: Original source files will NOT be modified
  ℹ️  Documented copies will be saved to: {output_folder}
{endif}

════════════════════════════════════════════════════════════════════════════════

JSDoc Standards to be Applied:
  ✓ Comprehensive @param descriptions with types
  ✓ Detailed @returns documentation with types
  ✓ @throws for error conditions
  ✓ @example with usage examples
  ✓ @remarks for implementation context
  ✓ @see for related references

Target Quality: commit-d02da43 JSDoc standards

════════════════════════════════════════════════════════════════════════════════
```

### Step 4: Execute JSDoc Generation (Spawn Mode)

**CRITICAL**: Use the Python wrapper script to spawn the process properly.

```python
# Path to spawn wrapper
wrapper_path = workspace_root + "/skills/generate-jsdoc/tools/spawn-jsdoc-generator.py"

# Build command
# Note: The wrapper will handle --no-branch flag based on create_branch parameter
if (create_branch === false) {
  no_branch_flag = "--no-branch"
} else {
  no_branch_flag = ""  // Default: create branch
}

command = f'python "{wrapper_path}" --repo "{repo_folder}" --output "{output_folder}" --workspace "{workspace_root}" {no_branch_flag}'

# Execute spawn wrapper (it handles background execution internally)
run_in_terminal(
  command=command,
  explanation="Generating JSDoc documentation in background",
  isBackground=false  # Wrapper spawns the actual process
)
```

**Important Notes**:
- Wrapper script handles directory changes and true spawn mode
- Process is detached and runs independently
- User can continue working immediately
- Wrapper displays progress information

### Step 5: Inform User

```
🚀 JSDoc generation started in background!

Process Details:
  - Process ID: {process_id}
  - Process Name: {process_name}
  - Status: running
  - Log: {log_file}
  - Registry: .olaf/work/straf-locks/jsdoc-generation-processes.json

{if output_mode === "in-place"}
⚠️  SOURCE FILES WILL BE MODIFIED
  - Git branch: {branch_name} (created)
  - Files will be updated with JSDoc comments
  - Review changes before committing
{else}
ℹ️  COPY MODE ACTIVE
  - Original files: Unchanged
  - Documented copies: {output_folder}
{endif}

You can continue working. The process will:
  1. Analyze repository structure (scan .js and .ts files)
  2. Generate JSDoc comments for each file (parallel processing)
  3. Save documented files to: {output_folder}
  4. Log progress and results

Estimated time: 
  - Small codebase (<100 files): ~5-10 minutes
  - Medium codebase (100-500 files): ~10-30 minutes
  - Large codebase (500+ files): ~30-60 minutes

📊 Check status anytime:
   python skills/generate-jsdoc/tools/check-jsdoc-processes.py

📝 Monitor progress:
   Get-Content {log_file} -Tail 20

{if output_mode === "in-place"}
🔍 Review changes after completion:
   git diff  # See all changes
   git status  # Check modified files
{endif}

### Tracking & Monitoring

Process tracking is automatically enabled. Each spawned process:
- Receives a unique process ID (UUID)
- Gets a descriptive name based on the repo folder (e.g., `jsdoc-gen-my-project`)
- Is registered in: `.olaf/work/straf-locks/jsdoc-generation-processes.json`
- Logs detailed progress to: `{log_file}`

**Check process status:**
```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py
```

**Process registry format:**
```json
{
  "processes": [
    {
      "id": "uuid",
      "name": "jsdoc-gen-<folder>",
      "repo": "/absolute/path/to/repo",
      "output": "/absolute/path/to/output",
      "mode": "in-place|copy-to-folder",
      "status": "running|completed|failed",
      "started_at": "ISO8601 timestamp",
      "pid": "process_id (Unix only)",
      "log_file": "/path/to/generation.log"
    }
  ]
}
```

**Completion detection:**
- Process status automatically updates when log shows completion marker
- Final log line indicates success or failure
- Check for modified files in repo or output folder

{if output_mode === "in-place"}
When complete, review changes:
  git diff
  git log -1 --stat
  # Review all JSDoc additions

To commit changes:
  git add .
  git commit -m "docs: add comprehensive JSDoc comments"
{else}
When complete, documented files will be available at:
  {output_folder}/
  # Copy desired files back to repo if needed
{endif}
```

## Error Handling

### Repository Folder Not Found
```
❌ Error: Repository folder does not exist
   Path: {repo_folder}
   
   Please verify the path and try again.
```

### CLI Not Found
```
❌ Error: straf-cli not found
   Expected at: {workspace_root}/.olaf/core/agentic/straf-cli
   
   Please ensure the straf-cli tool is installed.
```

### Output Folder Creation Failed
```
❌ Error: Cannot create output folder
   Path: {output_folder}
   Reason: {error_message}
   
   Please check permissions and try again.
```

### Git Repository Issues
```
⚠️  Warning: Not a git repository
   Path: {repo_folder}
   
   Git branch creation skipped. Proceeding with JSDoc generation.
   STRONGLY RECOMMEND: Initialize git repository first!
```

## Example Invocations

### Example 1: Generate JSDoc for entire repo (in-place, default)
```
User: "olaf generate jsdoc"

→ repo_folder: {workspace_root}
→ output_mode: in-place
→ output_folder: {workspace_root} (MODIFIES SOURCE)
→ create_branch: true
→ branch_name: docs-jsdoc-gen-20251125-143022 (auto-created)
→ ⚠️ WARNING: Source files will be modified with JSDoc comments
```

### Example 2: Generate JSDoc for specific subfolder (in-place)
```
User: "olaf generate jsdoc for vscode-extension"

→ repo_folder: {workspace_root}\vscode-extension
→ output_mode: in-place
→ output_folder: {workspace_root}\vscode-extension (MODIFIES SOURCE)
→ create_branch: true
→ ⚠️ WARNING: Source files in vscode-extension/ will be modified
```

### Example 3: Generate JSDoc to separate output folder (copy mode)
```
User: "olaf generate jsdoc to C:\\path\\to\\jsdoc-output"

→ repo_folder: {workspace_root}
→ output_mode: copy-to-folder
→ output_folder: C:\\path\\to\\jsdoc-output
→ create_branch: false (not needed - no source modification)
→ ℹ️ Original source files will NOT be modified
```

### Example 4: Generate JSDoc without git branch (⚠️ NOT RECOMMENDED)
```
User: "olaf generate jsdoc --no-branch"

→ repo_folder: {workspace_root}
→ output_mode: in-place
→ output_folder: {workspace_root} (MODIFIES SOURCE)
→ create_branch: false
→ ⚠️ WARNING: Source files will be modified WITHOUT git branch protection!
```

## Success Criteria

- ✅ Repository folder validated and exists
- ✅ Output folder determined correctly
- ✅ Output mode (in-place vs copy) determined
- ✅ Git branch created (unless explicitly disabled)
- ✅ Command executed in spawn mode (background)
- ✅ Process registered in tracking system
- ✅ Process ID and name assigned
- ✅ User warned about source code modification (if in-place)
- ✅ User informed about background execution
- ✅ User can continue working immediately
- ✅ User knows how to check process status

## Context Variables

**Input**:
- `user_repo_folder` (optional): User-provided repository folder path
- `user_output_folder` (optional): User-provided output folder path
- `user_create_branch` (optional): User preference for git branch creation (default: true)
- `workspace_root`: VS Code workspace root path

**Created**:
- `repo_folder`: Resolved absolute path to repository
- `output_mode`: Determined mode (in-place | copy-to-folder)
- `output_folder`: Resolved absolute path to output directory
- `create_branch`: Whether to create git branch (default: true)
- `branch_name`: Generated branch name (e.g., docs/jsdoc-gen-20251125-143022)
- `process_id`: Unique UUID for spawned process
- `process_name`: Descriptive name (e.g., jsdoc-gen-my-project)
- `command`: Full command executed
- `log_file`: Path to generation.log
- `registry_file`: Path to process tracking JSON

**Persistent**:
- `.olaf/work/straf-locks/jsdoc-generation-processes.json`: Process registry
- `{log_file}`: Process execution log

## Dependencies

**Required Tools**:
- Python 3.x (for straf-cli)
- AWS credentials configured (for Bedrock)
- straf-cli installed at `.olaf/core/agentic/straf-cli/`
- Git (for branch creation - optional but recommended)

**Required Agent Functions**:
- `run_in_terminal` (with `isBackground=false` for wrapper)
- File system access for path validation

## Notes

**Spawn Mode Benefits**:
- User continues working without interruption
- JSDoc generation runs in parallel
- No blocking on long-running tasks
- Terminal output visible for monitoring

**Git Branch Safety**:
- **DEFAULT BEHAVIOR**: Creates git branch automatically
- Branch name format: `docs-jsdoc-gen-YYYYMMDD-HHMMSS`
- User must explicitly use `--no-branch` to disable
- Protects against unwanted source code changes

**Output Modes**:
- **in-place**: Modifies original source files (⚠️ requires git branch)
- **copy-to-folder**: Creates documented copies (ℹ️ originals untouched)

**Performance**:
- Small codebase (<100 files): ~5-10 minutes
- Medium codebase (100-500 files): ~10-30 minutes
- Large codebase (500+ files): ~30-60 minutes
- Processing rate: ~3-10 files/minute (depends on file size and complexity)

**Resume Support**:
- Process can be interrupted (Ctrl+C)
- Progress is saved after each file
- Rerun command to resume from last processed file
