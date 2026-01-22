---
task_id: "list-esdi-sessions"
task_name: "List Existing ESDI Sessions"
dependencies: []
conditions: []
---

# List Existing ESDI Sessions

## Input Context
**Required Context Variables**: None
**Required Files**: None
**Required Tools**: File system access

## Task Instructions

### 1. Scan ESDI Directory

**Location**: `.olaf/work/staging/esdi/`

Find all subdirectories matching pattern: `YYYYMMDD-*`

### 2. Analyze Each Session

For each ESDI session directory:

**Read Status File**: `esdi-status.md`
- Extract session metadata
- Check phase completion status
- Identify current phase

**Determine Session State**:
- **In Progress**: Missing `IMPLEMENTATION-TASK-PLAN.md` OR Phase I not completed in status
- **Completed**: Has `IMPLEMENTATION-TASK-PLAN.md` AND Phase I marked completed
- **Stale**: No updates in > 30 days

### 3. Categorize Sessions

**Active Sessions** (in-progress):
- Has status file
- Phase I not completed
- Updated within last 30 days

**Completed Sessions**:
- Has `IMPLEMENTATION-TASK-PLAN.md`
- Phase I marked completed in status

**Abandoned/Stale**:
- No status file OR
- No updates in > 30 days

### 4. Display Session List

```
📋 ESDI Sessions
═══════════════════════════════════════

🔄 IN PROGRESS (3)
──────────────────────────────────────
1. 20251122-repository-scanner
   Current Phase: Design (D)
   Last Updated: 2025-11-22
   Next: Complete design.md
   
2. 20251120-api-gateway
   Current Phase: Specification (S)
   Last Updated: 2025-11-21
   Next: Complete steps 3-7
   
3. 20251118-data-pipeline
   Current Phase: Exploration (E)
   Last Updated: 2025-11-20
   Next: Run transform-raw-spec

✅ COMPLETED (2)
──────────────────────────────────────
1. 20251115-auth-service
   Completed: 2025-11-16
   All phases: ✅
   
2. 20251110-logging-framework
   Completed: 2025-11-12
   All phases: ✅

⏸️  STALE/ABANDONED (1)
──────────────────────────────────────
1. 20251101-notification-system
   Last Updated: 2025-11-05
   Current Phase: Specification (S)
   Status: No activity for 19 days
```

### 5. Provide Action Options

```
What would you like to do?

1. Resume an existing ESDI session (select by number)
2. Create a new ESDI session
3. View details of a specific session
4. Archive completed sessions
5. Clean up abandoned sessions

Enter choice (1-5):
```

## Output Requirements

**State Updates**:
- `context.esdi_sessions[]`: Array of session objects with:
  - `directory`: Session folder name
  - `topic`: Short topic name
  - `status`: in-progress | completed | stale
  - `current_phase`: E | S | D | I
  - `last_updated`: Date
  - `next_action`: What needs to be done
  - `artifacts[]`: List of completed artifacts
- `context.active_count`: Number of in-progress sessions
- `context.completed_count`: Number of completed sessions
- `context.stale_count`: Number of stale sessions
- `task_status.list-esdi-sessions`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Session list available for user selection
- Can resume existing session or create new

## Session Object Structure

```json
{
  "directory": "20251122-repository-scanner",
  "topic": "repository-scanner",
  "idea": "Repository onboarding system",
  "status": "in-progress",
  "current_phase": "D",
  "phases_completed": ["E", "S"],
  "last_updated": "2025-11-22",
  "created": "2025-11-22",
  "next_action": "Complete design.md",
  "artifacts": {
    "exploration": ["exploration-findings.md"],
    "specification": ["specification.md", "step1-*.md", "step2-*.md", ...],
    "design": [],
    "implementation": []
  }
}
```
