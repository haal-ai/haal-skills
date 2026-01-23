# STRAF Skill Runner - Execution Tracking

## Execution: {execution_id}

**Timestamp**: {timestamp}
**Skill**: {skill_name}
**Status**: {status}

---

## Configuration

**Skill Path**: `{skill_path}`

**Tool Mode**: {tool_mode}
**Timeout**: {timeout}s
**AWS Profile**: {aws_profile}

---

## Parameters Gathered

{parameters_table}

---

## Context String

```
{context_string}
```

---

## Command Executed

```bash
{command}
```

---

## Process Information

**PID**: {process_pid}
**Started At**: {started_at}
**Mode**: Autonomous (spawned, non-interactive)

---

## Logs & Outputs

**STRAF Logs**: `.olaf/work/staging/straf/logs/olaf-strands-results-{timestamp}-*.md`

**Tracking File**: `.olaf/work/staging/straf/tracking/execution-{execution_id}.json`

**Spawner Script**: `.olaf/work/staging/straf/spawners/skill-{execution_id}.py`

---

## Status Updates

| Timestamp | Status | Notes |
|-----------|--------|-------|
| {started_at} | STARTED | Process spawned successfully |
| ... | RUNNING | Autonomous execution in progress |
| ... | COMPLETED / FAILED | Final status (updated by monitoring) |

---

## Output Files

*Will be populated when execution completes*

- [ ] Primary output file
- [ ] Metadata file
- [ ] Execution log

---

## Notes

- Execution is **fully autonomous** - no user interaction required
- Process runs in background while you continue working
- Check tracking JSON for live status updates
- Logs are available in real-time in STRAF logs directory

---

**Monitoring**: You can check status anytime by reading the tracking JSON file.
