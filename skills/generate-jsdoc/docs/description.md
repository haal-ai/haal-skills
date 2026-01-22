# Generate JSDoc Documentation

## Overview

The `generate-jsdoc` skill generates comprehensive inline JSDoc comments for JavaScript and TypeScript source files using the AWS Strands multi-agent system.

**⚠️ CRITICAL**: This skill **MODIFIES SOURCE CODE** by adding JSDoc documentation directly to your files.

## Key Features

- **Inline Documentation**: Adds comprehensive JSDoc comments to .js and .ts files
- **High-Quality Output**: Matches commit-d02da43 JSDoc standards with detailed @param, @returns, @throws, @example, and @remarks
- **Spawn Mode**: Runs in background, allowing you to continue working
- **Git Safety**: Creates git branch automatically (default) to protect against unwanted changes
- **Two Modes**: In-place modification or copy-to-folder
- **Process Tracking**: Monitor progress via `.olaf/work/straf-locks/jsdoc-generation-processes.json`
- **Resume Support**: Can resume interrupted operations

## Safety Features

### Automatic Git Branch Creation

**Default Behavior**: The skill creates a git branch automatically before modifying any files.

- Branch name format: `docs-jsdoc-gen-YYYYMMDD-HHMMSS`
- Must explicitly use `--no-branch` flag to disable (NOT RECOMMENDED)
- Provides safety net to review and discard changes if needed

### Two Operating Modes

1. **In-Place Mode** (default):
   - Modifies source files directly in repository
   - ⚠️ Changes original files
   - ✅ Git branch creation enabled by default
   - Use when you want to update your actual source code

2. **Copy-to-Folder Mode**:
   - Creates documented copies in separate directory
   - ℹ️ Original files remain untouched
   - Use when you want to preview changes first

## Usage

### Basic Usage (In-Place, Default)
```
User: "olaf generate jsdoc"
```
- Processes entire workspace repository
- Creates git branch automatically
- Modifies source files with JSDoc comments

### Specific Folder
```
User: "olaf generate jsdoc for vscode-extension"
```
- Processes only the vscode-extension subfolder
- Creates git branch
- Modifies files in that subfolder only

### Copy Mode (Safe Preview)
```
User: "olaf generate jsdoc to c:\temp\jsdoc-output"
```
- Processes entire repository
- Saves documented copies to specified folder
- Original files untouched

### Without Git Branch (⚠️ NOT RECOMMENDED)
```
User: "olaf generate jsdoc --no-branch"
```
- Modifies files without creating branch
- Changes applied to current branch
- No easy way to undo

## JSDoc Standards Applied

The skill generates comprehensive JSDoc documentation including:

- **@param**: Detailed parameter descriptions with types
- **@returns**: Return value documentation with types
- **@throws**: Error conditions and exception types
- **@example**: Usage examples with code snippets
- **@remarks**: Implementation notes and context
- **@see**: Related references and links

**Quality Target**: Matches commit-d02da43 JSDoc standards

## Process Monitoring

### Check Status
```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py
```

### Monitor Progress
```bash
# Windows
Get-Content .jsdoc-generation.log -Tail 20

# Unix/Linux
tail -f .jsdoc-generation.log
```

### Process Registry
Location: `.olaf/work/straf-locks/jsdoc-generation-processes.json`

Contains:
- Process ID and name
- Repository and output paths
- Operating mode (in-place | copy-to-folder)
- Status (running | completed | failed | interrupted)
- Timestamps
- Log file location

## Performance

| Codebase Size | Est. Time | Files/Min |
|--------------|-----------|-----------|
| Small (<100 files) | 5-10 min | 10-20 |
| Medium (100-500 files) | 10-30 min | 10-20 |
| Large (500+ files) | 30-60 min | 8-15 |

**Note**: Actual time depends on:
- File size and complexity
- Number of functions/classes per file
- AWS Bedrock API response time
- System resources

## Review and Commit Changes

### After Completion (In-Place Mode)

1. **Review changes**:
   ```bash
   git diff
   git status
   ```

2. **Commit if satisfied**:
   ```bash
   git add .
   git commit -m "docs: add comprehensive JSDoc comments"
   ```

3. **Discard if not satisfied**:
   ```bash
   git checkout .
   git checkout main  # Return to main branch
   git branch -D docs/jsdoc-gen-YYYYMMDD-HHMMSS  # Delete branch
   ```

## Dependencies

- Python 3.x
- AWS credentials configured for Bedrock
- straf-cli installed at `.olaf/core/agentic/straf-cli/`
- Git (optional but strongly recommended)

## Tags

`documentation`, `jsdoc`, `inline-docs`, `spawn`, `async`, `strands`, `code-modification`
