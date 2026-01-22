---
task_id: "backup-file"
task_name: "Backup File with Timestamp"
dependencies: ["context.timestamp"]
conditions: []
---

# Backup File with Timestamp

## Input Context
**Required Context Variables**: 
- `context.file_to_backup`: Full path to the file to backup
- `context.backup_dir`: Directory where backup should be created (optional - defaults to [file-dir]/backups/)
- `context.timestamp`: Session timestamp (YYYYMMDD-HHMMSS)
- `context.backup_suffix`: Optional suffix for backup filename (defaults to "backup")
**Required Files**: File specified in `context.file_to_backup`
**Required Tools**: File copy operations

## Task Instructions

### Create Timestamped Backup

1. **Determine Backup Location**:
   - If `context.backup_dir` provided: use that directory
   - Otherwise: create `backups/` subdirectory next to original file
   - Create backup directory if it doesn't exist

2. **Generate Backup Filename**:
   - Extract original filename and extension
   - Format: `[filename]-[suffix]-[timestamp].[ext]`
   - Example: `review-code-backup-20251120-143022.md`
   - Default suffix: "backup" (can be overridden via `context.backup_suffix`)

3. **Copy File to Backup**:
   - Use shell command to copy file (preserves all attributes)
   - PowerShell: `Copy-Item -Path "[source]" -Destination "[backup-path]"`
   - Bash: `cp "[source]" "[backup-path]"`
   - Preserve exact content (no modifications)

4. **Verify Backup**:
   - Confirm backup file exists
   - Check file size matches original
   - Store backup path for reference

5. **Display Confirmation**:
   ```
   Backup created: [backup-path]
   Original file preserved.
   ```

## Output Requirements

**State Updates**:
- `context.backup_file`: Full path to created backup file
- `context.backup_created`: true
- `context.backup_timestamp`: Timestamp used in filename
- `task_status.backup-file`: "completed"

**Files Created**: 
- Backup file at specified or default location

**Context Passed to Next Tasks**:
- Backup path available for rollback if needed
- Confirms safe to proceed with modifications

## Usage Examples

### Backup a skill prompt
```
context.file_to_backup = "skills/review-code/prompts/review-code.md"
context.timestamp = "20251120-143022"
→ Creates: skills/review-code/prompts/backups/review-code-backup-20251120-143022.md
```

### Backup a configuration file
```
context.file_to_backup = ".olaf/_olaf-config.json"
context.backup_dir = ".olaf/backups/configs"
context.backup_suffix = "pre-update"
context.timestamp = "20251120-143022"
→ Creates: .olaf/backups/configs/olaf-config-pre-update-20251120-143022.json
```
