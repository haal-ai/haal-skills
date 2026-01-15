---
task_id: "update-esdi-status"
task_name: "Update ESDI Status File"
dependencies: []
conditions: []
---

# Update ESDI Status File

## Input Context
**Required Context Variables**: 
- `context.esdi_directory`: Path to ESDI session directory
- `context.phase`: Which phase completed (E | S | D | I)
- `context.artifacts[]`: List of artifact files created

**Optional**:
- `context.notes`: Any notes to add to the phase section

## Task Instructions

### 1. Load Status File

Read `${esdi_directory}/esdi-status.md`

If file doesn't exist, create from template: `templates/esdi-status-template.md`

### 2. Update Phase Status

For the completed phase (`${phase}`):

**Update Status Table**:
- Change status from ⏳/🔄 to ✅
- Set "Completed On" to current date
- Add link to final artifact

**Update Phase Section**:
```markdown
## Phase [N]: [Name]

**Status**: ✅ Completed
**Started On**: [date]
**Completed On**: [CURRENT_DATE]

**Artifacts**:
- [✅] `artifact1.md` - Description
- [✅] `artifact2.md` - Description

**Notes**: [Any notes from context]
```

### 3. Update Next Phase Status

Set next phase to "🔄 In Progress" if work has started

### 4. Update Session Metadata

**Last Updated**: Current date
**Next Action**: Determine based on completed phase:
- E completed → "Start Phase 2: Specification (transform-raw-spec)"
- S completed → "Start Phase 3: Design (generate-design)"
- D completed → "Start Phase 4: Implementation Planning (generate-implementation-plan)"
- I completed → "ESDI Complete - Ready for execution"

**Status**: 
- If Phase I completed → "Completed"
- Otherwise → "In Progress"

### 5. Add Version History Entry

```markdown
| [CURRENT_DATE] | Phase [X] | Completed [phase name] - Added [artifact list] |
```

### 6. Save Updated Status File

Write back to `${esdi_directory}/esdi-status.md`

## Output Requirements

**State Updates**:
- `context.status_file_updated`: true
- `context.session_status`: "in-progress" | "completed"
- `context.next_phase`: Next phase to work on (or "none" if complete)
- `task_status.update-esdi-status`: "completed"

**Files Created/Modified**: 
- `esdi-status.md` updated with phase completion

**Context Passed**: 
- Updated status available for session tracking

## Phase Mapping

| Phase Code | Phase Name | Final Artifact |
|------------|-----------|----------------|
| E | Exploration | `exploration-findings.md` |
| S | Specification | `specification.md` |
| D | Design | `design.md` |
| I | Implementation Planning | `IMPLEMENTATION-TASK-PLAN.md` |

## Example Updates

**After Phase E (Exploration)**:
```markdown
| Phase | Name | Status | Completed On | Final Artifact |
|-------|------|--------|--------------|----------------|
| E | Exploration | ✅ Completed | 2025-11-22 | [exploration-findings.md](exploration-findings.md) |
| S | Specification | 🔄 In Progress | - | - |
| D | Design | ⏳ Not Started | - | - |
| I | Implementation Plan | ⏳ Not Started | - | - |

**Next Action**: Start Phase 2: Specification (transform-raw-spec)
```

**After Phase I (Implementation Planning)**:
```markdown
| Phase | Name | Status | Completed On | Final Artifact |
|-------|------|--------|--------------|----------------|
| E | Exploration | ✅ Completed | 2025-11-22 | [exploration-findings.md](exploration-findings.md) |
| S | Specification | ✅ Completed | 2025-11-23 | [specification.md](specification.md) |
| D | Design | ✅ Completed | 2025-11-23 | [design.md](design.md) |
| I | Implementation Plan | ✅ Completed | 2025-11-24 | [IMPLEMENTATION-TASK-PLAN.md](IMPLEMENTATION-TASK-PLAN.md) |

**Status**: ✅ Completed
**Next Action**: Execute implementation tasks from plan
```
