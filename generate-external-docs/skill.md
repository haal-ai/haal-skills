---
name: generate-external-docs
description: Generates external documentation files (index.md, architecture.md, control-flow.md, use-cases.md, mkdocs.yml) using AWS Strands multi-agent system. Runs in spawn mode to allow parallel work. Output defaults to .olaf/data/product/documentations/<repo>/<folder>.
license: Apache-2.0
metadata:
  olaf_protocol: "\"Act\""
---

<olaf>

# Generate External Documentation

## Purpose
Generate comprehensive external documentation (MkDocs format) from codebase analysis using AWS Strands multi-agent system. Runs in spawn mode allowing the user to continue working while documentation generates in the background.

## Execution Protocol: Act

Execute immediately without confirmation. The process runs asynchronously.

## Input Parameters

### Optional Parameters
- `root_folder`: Root folder path for analysis
  - **Default**: Workspace root (use workspace detection)
  - **Format**: Absolute path (e.g., `c:\Users\...\haal-ide`)
  
- `output_folder`: Output directory for generated documentation
  - **Default**: `.olaf/data/product/documentations/<repo-name>/<relative-root-path>`
  - **Format**: Absolute path
  - **Structure**: 
    - If root is workspace root: `.olaf/data/product/documentations/<repo-name>/root`
    - If root is subfolder: `.olaf/data/product/documentations/<repo-name>/<subfolder-name>`

## Workflow

### Step 1: Determine Root Folder
```javascript
if (user_provided_root) {
  root_folder = resolve_absolute_path(user_provided_root)
} else {
  root_folder = workspace_root  // Use VS Code workspace root
}

// Validate root folder exists
if (!fs.exists(root_folder)) {
  ERROR: "Root folder does not exist: {root_folder}"
  EXIT
}
```

### Step 2: Determine Output Folder
```javascript
// Extract repository name from workspace or root folder
repo_name = extract_repo_name(workspace_root)  // e.g., "haal-ide"

// Calculate relative path from workspace root to analysis root
if (root_folder === workspace_root) {
  folder_suffix = "root"
} else {
  // Get relative path and convert to folder name
  rel_path = relative_path(workspace_root, root_folder)
  folder_suffix = rel_path.replace(/[\/\\]/g, '-')  // e.g., "core-scripts"
}

if (user_provided_output) {
  output_folder = resolve_absolute_path(user_provided_output)
} else {
  output_folder = workspace_root + "/.olaf/data/product/documentations/" + repo_name + "/" + folder_suffix
}

// Create output directory if it doesn't exist
create_directory_recursive(output_folder)
```

### Step 3: Display Execution Plan
```
════════════════════════════════════════════════════════════════════════════════
EXTERNAL DOCUMENTATION GENERATION (Spawn Mode)
════════════════════════════════════════════════════════════════════════════════
Root Folder:    {root_folder}
Output Folder:  {output_folder}
Repository:     {repo_name}
Mode:           Asynchronous (you can continue working)
════════════════════════════════════════════════════════════════════════════════

Documentation Files to Generate:
  ✓ index.md - Project overview
  ✓ architecture.md - Technical architecture + Mermaid diagrams
  ✓ control-flow.md - Process flows + Mermaid diagrams  
  ✓ use-cases.md - Functional use cases
  ✓ mkdocs.yml - MkDocs configuration
  ✓ VALIDATION_REPORT.md - Quality validation

════════════════════════════════════════════════════════════════════════════════
```

### Step 4: Execute Documentation Generation (Spawn Mode)

**CRITICAL**: Use the Python wrapper script to spawn the process properly.

```python
# Path to spawn wrapper
wrapper_path = workspace_root + "/skills/generate-external-docs/tools/spawn-doc-generator.py"

# Build command
command = f'python "{wrapper_path}" --root "{root_folder}" --output "{output_folder}" --workspace "{workspace_root}"'

# Execute spawn wrapper (it handles background execution internally)
run_in_terminal(
  command=command,
  explanation="Generating external documentation in background",
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
🚀 Documentation generation started in background!

Process Details:
  - Process ID: {process_id}
  - Process Name: {process_name}
  - Status: running
  - Log: {output_folder}/generation.log
  - Registry: .olaf/work/straf-locks/doc-generation-processes.json

You can continue working. The process will:
  1. Analyze repository structure
  2. Generate documentation files (parallel)
  3. Validate documentation quality
  4. Save files to: {output_folder}

Estimated time: 5-15 minutes (depending on codebase size)

📊 Check status anytime:
   python skills/generate-external-docs/tools/check-doc-processes.py

📝 Monitor progress:
   Get-Content {output_folder}/generation.log -Tail 20

To check progress, look for terminal output in VS Code terminal panel.

### Tracking & Monitoring

Process tracking is automatically enabled. Each spawned process:
- Receives a unique process ID (UUID)
- Gets a descriptive name based on the root folder (e.g., `doc-gen-olaf`)
- Is registered in: `.olaf/work/straf-locks/doc-generation-processes.json`
- Logs detailed progress to: `{output_folder}/generation.log`

**Check process status:**
```bash
python skills/generate-external-docs/tools/check-doc-processes.py
```

**Process registry format:**
```json
{
  "processes": [
    {
      "id": "uuid",
      "name": "doc-gen-<folder>",
      "root": "/absolute/path/to/root",
      "output": "/absolute/path/to/output",
      "status": "running|completed|failed",
      "started_at": "ISO8601 timestamp",
      "pid": "process_id (Unix only)",
      "log_file": "/path/to/generation.log"
    }
  ]
}
```

**Completion detection:**
- Process status automatically updates when log shows `[OK]` marker
- Check for `VALIDATION_REPORT.md` in output folder
- Final log line: "External documentation completed successfully"

When complete, files will be available at:
  {output_folder}/content/index.md
  {output_folder}/content/architecture.md
  {output_folder}/content/control-flow.md
  {output_folder}/content/use-cases.md
  {output_folder}/mkdocs.yml

To preview documentation:
  cd {output_folder}
  mkdocs serve
  # Then open http://localhost:8000
```

## Error Handling

### Root Folder Not Found
```
❌ Error: Root folder does not exist
   Path: {root_folder}
   
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

## Example Invocations

### Example 1: Generate docs for entire repository (default)
```
User: "olaf generate external docs"

→ root_folder: {workspace_root}
→ output_folder: {workspace_root}\.olaf\data\product\documentations\<repo-name>\root
```

### Example 2: Generate docs for specific subfolder
```
User: "olaf generate external docs for scripts"

→ root_folder: {workspace_root}\.olaf\core\scripts
→ output_folder: {workspace_root}\.olaf\data\product\documentations\<repo-name>\core-scripts
```

### Example 3: Custom root and output
```
User: "olaf generate external docs from C:\path\to\project to C:\path\to\docs"

→ root_folder: C:\path\to\project
→ output_folder: C:\path\to\docs
```

## Success Criteria

- ✅ Root folder validated and exists
- ✅ Output folder created successfully
- ✅ Command executed in spawn mode (background)
- ✅ Process registered in tracking system
- ✅ Process ID and name assigned
- ✅ User informed about background execution
- ✅ User can continue working immediately
- ✅ User knows how to check process status

## Context Variables

**Input**:
- `user_root_folder` (optional): User-provided root folder path
- `user_output_folder` (optional): User-provided output folder path
- `workspace_root`: VS Code workspace root path

**Created**:
- `root_folder`: Resolved absolute path to analysis root
- `output_folder`: Resolved absolute path to output directory
- `repo_name`: Repository name extracted from workspace
- `process_id`: Unique UUID for spawned process
- `process_name`: Descriptive name (e.g., doc-gen-olaf)
- `command`: Full command executed
- `log_file`: Path to generation.log
- `registry_file`: Path to process tracking JSON

**Persistent**:
- `.olaf/work/straf-locks/doc-generation-processes.json`: Process registry
- `{output_folder}/generation.log`: Process execution log

## Dependencies

**Required Tools**:
- Python 3.x (for straf-cli)
- AWS credentials configured (for Bedrock)
- straf-cli installed at `.olaf/core/agentic/straf-cli/`

**Required Agent Functions**:
- `run_in_terminal` (with `isBackground=true`)
- File system access for path validation

## Notes

**Spawn Mode Benefits**:
- User continues working without interruption
- Documentation generates in parallel
- No blocking on long-running tasks
- Terminal output visible for monitoring

**Output Structure**:
```
{output_folder}/
  content/
    index.md
    architecture.md
    control-flow.md
    use-cases.md
  mkdocs.yml
  VALIDATION_REPORT.md
```

**Performance**:
- Small codebase (<100 files): ~2-5 minutes
- Medium codebase (100-1000 files): ~5-10 minutes  
- Large codebase (1000+ files): ~10-20 minutes
