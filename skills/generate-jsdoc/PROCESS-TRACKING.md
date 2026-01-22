# JSDoc Generation Process Tracking

The generate-jsdoc skill includes an automatic process tracking system that registers and monitors spawned JSDoc generation processes.

## Overview

When you invoke `generate-jsdoc`, a background process is spawned that runs independently of VS Code. This process is tracked via a JSON registry file that allows you to monitor progress and check status.

## Process Registry Location

```
.olaf/work/straf-locks/jsdoc-generation-processes.json
```

This file is created automatically in your workspace and contains information about all spawned JSDoc generation processes.

## Registry Format

```json
{
  "processes": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "jsdoc-gen-my-project",
      "repo": "/absolute/path/to/repository",
      "output": "/absolute/path/to/output",
      "mode": "in-place",
      "status": "running",
      "started_at": "2025-11-25T14:30:22.123456",
      "completed_at": "2025-11-25T14:45:33.654321",
      "pid": 12345,
      "log_file": "/path/to/.jsdoc-generation.log"
    }
  ]
}
```

## Field Descriptions

| Field | Description |
|-------|-------------|
| `id` | Unique UUID for this process |
| `name` | Human-readable name (e.g., `jsdoc-gen-my-project`) |
| `repo` | Absolute path to repository being processed |
| `output` | Absolute path to output directory |
| `mode` | Operation mode: `in-place` or `copy-to-folder` |
| `status` | Current status: `running`, `completed`, `failed`, `interrupted` |
| `started_at` | ISO8601 timestamp when process started |
| `completed_at` | ISO8601 timestamp when process completed (if finished) |
| `pid` | Process ID (Unix/Linux only, Windows uses batch file) |
| `log_file` | Absolute path to log file for this process |

## Process Statuses

### `running`
- Process is currently active
- Generating JSDoc comments
- Log file being updated in real-time

### `completed`
- Process finished successfully
- All files processed
- JSDoc comments added to files
- Check output directory/repository for results

### `failed`
- Process encountered an error
- Check log file for error details
- May need to fix issue and rerun

### `interrupted`
- User interrupted process (Ctrl+C)
- Partial results may be available
- Process supports resume - run again to continue

## Checking Process Status

### Using the Check Tool

```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py
```

**Sample Output:**
```
════════════════════════════════════════════════════════════════════════════════
JSDOC GENERATION PROCESSES
════════════════════════════════════════════════════════════════════════════════

1. 🔄 jsdoc-gen-my-project
   ID: 550e8400-e29b-41d4-a716-446655440000
   Status: RUNNING
   Repository: /home/user/my-project
   Output: /home/user/my-project
   Mode: in-place
   Started: 2025-11-25T14:30:22.123456
   PID: 12345
   Log: /home/user/my-project/.jsdoc-generation.log [✓]
   Log Size: 245.3 KB

────────────────────────────────────────────────────────────────────────────────
Summary: 1 total | 1 running | 0 completed | 0 failed | 0 interrupted
────────────────────────────────────────────────────────────────────────────────

Running Processes:
  • jsdoc-gen-my-project - Monitor: tail -f /home/user/my-project/.jsdoc-generation.log
```

### JSON Output

```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py --json
```

Returns raw JSON for programmatic processing.

### Specifying Workspace

```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py --workspace /path/to/workspace
```

## Monitoring Process Progress

### Real-Time Log Monitoring

**Windows PowerShell:**
```powershell
Get-Content .jsdoc-generation.log -Tail 20 -Wait
```

**Unix/Linux:**
```bash
tail -f .jsdoc-generation.log
```

### Log File Contents

The log file contains:
- Repository analysis results
- File discovery (count of .js and .ts files)
- Per-file processing status
- Success/failure indicators
- Final summary with statistics

**Sample Log Output:**
```
Phase 1/2: Analyzing repository structure...
  Found 45 JavaScript files
  Found 23 TypeScript files
  Total: 68 files
  Will process: 68 files

Phase 2/2: Generating JSDoc documentation...
  Processing files one at a time (this may take a while)
  Progress saved after each file (safe to interrupt with Ctrl+C)

  🔄 Starting: src/services/userService.ts
[OK] [1/68] src/services/userService.ts
[OK] [2/68] src/utils/helpers.js
...
[OK] [68/68] src/components/App.tsx

[OK] JSDoc generation completed successfully!
Files processed: 68
Duration: 15.3 minutes
```

## Automatic Status Updates

The `check-jsdoc-processes.py` tool automatically updates process status by examining log files:

1. **Completion Detection**: Looks for `[OK] JSDoc generation completed successfully!`
2. **Failure Detection**: Looks for `ERROR`, `FAILED`, or `Error:` markers
3. **Interrupt Detection**: Looks for `Interrupted by user` or `KeyboardInterrupt`

When detected, the process status is updated in the registry and a `completed_at` timestamp is added.

## Process Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. User invokes: "olaf generate jsdoc"                         │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│ 2. Skill validates parameters and displays plan                │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│ 3. Execute: spawn-jsdoc-generator.py spawns background process │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│ 4. Register: Process entry created in registry                 │
│    - Assigned UUID and descriptive name                        │
│    - Status: running                                            │
│    - Log file path recorded                                     │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│ 5. Background: straf-cli jsdoc-gen executes                    │
│    - Analyzes repository                                        │
│    - Processes files in parallel                                │
│    - Logs progress to log file                                  │
│    - Can be interrupted and resumed                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│ 6. Monitor: User can check status anytime                      │
│    - Run check-jsdoc-processes.py                              │
│    - Monitor log file                                           │
│    - Continue working in parallel                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│ 7. Complete: Process finishes                                  │
│    - Log file shows completion marker                           │
│    - Status auto-updated to "completed"                         │
│    - completed_at timestamp added                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│ 8. Review: User reviews changes and commits                    │
└─────────────────────────────────────────────────────────────────┘
```

## Troubleshooting

### Process Stuck in "running" Status

**Check:**
1. Is log file growing? `ls -lh .jsdoc-generation.log`
2. Is process actually running? Check system processes
3. Any errors in log? `tail -100 .jsdoc-generation.log`

**Solutions:**
- Wait longer (large codebases take 30-60 minutes)
- Check log file for errors
- If truly stuck, kill process and restart

### Log File Not Found

**Cause**: Process may have failed to start

**Check:**
- Registry entry exists?
- Path to straf-cli correct?
- AWS credentials configured?

### Multiple Processes Running

You can have multiple JSDoc generation processes running simultaneously for different repositories or subfolders. Each gets a unique ID and name.

**View all:**
```bash
python skills/generate-jsdoc/tools/check-jsdoc-processes.py
```

## Best Practices

1. **Check status before starting new process**: Avoid duplicate processes on same repository
2. **Monitor long-running processes**: Check log periodically for progress
3. **Clean up completed processes**: Archive or remove old registry entries as needed
4. **Use JSON output for automation**: Integrate with scripts using `--json` flag
5. **Review log files**: Keep for debugging if issues arise

## Related Documentation

- See `docs/description.md` for skill overview
- See `docs/tutorial.md` for step-by-step guide
- See `prompts/generate-jsdoc.md` for technical workflow
