---
name: generate-dfd-from-code
description: Generate Data Flow Diagrams (DFD) from source code analysis using a multi-phase approach (Context → Level 1 → Level 2 → Final Documentation)
license: Apache-2.0
metadata:
  olaf_tags: [dfd, data-flow, architecture, analysis, documentation, reverse-engineering]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

if you are in need to get the date and time, use time tools, fallback to shell command if needed

# Generate DFD from Code - Multi-Phase Analysis

## Overview

This skill generates comprehensive Data Flow Diagrams from source code through a systematic 4-phase, 12-step process. It creates Context Diagrams, Level 1 DFDs, optional Level 2 DFDs, and final documentation.

## Input Parameters

**IMPORTANT**: When parameters are not provided, ask the USER for them.

1. **source_path**: string - Path to the application source code (REQUIRED)
2. **output_dir**: string - Directory for DFD artifacts (default: `.olaf/work/staging/{project-name}/dfd/`)
3. **project_name**: string - Name identifier for the project (REQUIRED)
4. **include_level2**: boolean - Whether to include Level 2 decomposition (default: auto-detect based on complexity)

## Output Directory Structure

All artifacts are created in `{output_dir}`:
```
{output_dir}/
├── DFD_master_progress.md      # Master progress tracking
├── {project}_analysis.md       # Main analysis document
├── DFD_level1_tasks.md         # Level 1 task tracking
├── DFD_level2_tasks.md         # Level 2 task tracking (if needed)
└── DFD_level_analysis.md       # Final consolidated documentation
```

## Multi-Phase Execution

This skill uses an internal multi-phase system that MUST read its own previous phases. Unlike other skills that use fresh assessment, DFD analysis builds progressively.

### Phase A: Initial Analysis (Steps 1-3)
Load: `helpers/dfd-phase-a-initial.md`
- Step 1: Initial System Understanding
- Step 2: Context Diagram Creation
- Step 3: Level 1 DFD Task Planning

### Phase B: Level 1 Analysis (Steps 4-7)
Load: `helpers/dfd-phase-b-level1.md`
- Step 4: Level 1 DFD Creation
- Step 5: Level 1 vs Level 2 Validation
- Step 6: Level 1 Refinement (if needed)
- Step 7: Level 2 Decision and Task Planning

### Phase C: Level 2 Analysis (Steps 8-9) - Optional
Load: `helpers/dfd-phase-c-level2.md`
- Step 8: Level 2 DFD Creation
- Step 9: Level 2 Validation

### Phase D: Final Documentation (Steps 10-12)
Load: `helpers/dfd-phase-d-final.md`
- Step 10: Final Documentation
- Step 11: Quality Review
- Step 12: Stakeholder Review

## Execution Protocol

### 1. Initialize Progress Tracking

Create `DFD_master_progress.md` with this structure:

```markdown
# Master DFD Analysis Progress for {project_name}

## Overall Progress Tracking
**Analysis Started:** {date}
**Last Updated:** {date}
**Current Phase:** Phase A
**Overall Completion:** 0/12 steps completed

## Master Task Checklist

### Phase A: Initial Analysis
- [ ] **Step 1**: Initial System Understanding
- [ ] **Step 2**: Context Diagram Creation
- [ ] **Step 3**: Level 1 DFD Task Planning

### Phase B: Level 1 Analysis
- [ ] **Step 4**: Level 1 DFD Creation
- [ ] **Step 5**: Level 1 vs Level 2 Validation
- [ ] **Step 6**: Level 1 Refinement (if needed)
- [ ] **Step 7**: Level 2 Task Planning

### Phase C: Level 2 Analysis
- [ ] **Step 8**: Level 2 DFD Creation
- [ ] **Step 9**: Level 2 Validation

### Phase D: Final Documentation
- [ ] **Step 10**: Final Documentation
- [ ] **Step 11**: Quality Review
- [ ] **Step 12**: Stakeholder Review

## Current Status
**Active Phase:** A
**Next Step:** 1
**Ready for User Review:** No

## Level 2 Decision Status
**Decision:** [Pending]
**Reason:** [To be determined in Step 7]
```

### 2. Phase Execution Logic

**Phase A Conditions:**
- Master progress file exists
- Steps 1-3 are not completed
- No `DFD_level1_tasks.md` file exists

**Phase B Conditions:**
- Steps 1-3 completed
- `DFD_level1_tasks.md` exists
- Steps 4-7 not completed

**Phase C Conditions (ALL must be true):**
- Steps 1-7 completed
- Level 2 Decision = "Yes"
- `DFD_level2_tasks.md` exists
- Steps 8-9 not completed

**Phase D Conditions (ONE of these):**
- Steps 1-9 completed AND Level 2 = "Yes"
- Steps 1-7 completed AND Level 2 = "No"

### 3. User Review Points

**🛑 MANDATORY USER REVIEW before each phase transition:**
1. Review master progress file
2. Confirm current phase status
3. Approve proceeding to next phase

## DFD Principles

### Level 1 Should Show:
- Major business functions (5-9 processes maximum)
- Primary data transformations
- High-level data stores (not implementation details)
- External entity interactions only
- **What** the system does (not how)

### Level 2 Should Show:
- Implementation details (algorithms, specific operations)
- Error handling and exception paths
- Internal data stores (temporary, cache, working data)
- Decision logic and control flows
- **How** the parent process works

### Move to Level 2 When:
- Level 1 process is complex with multiple distinct functions
- Stakeholders need to understand internal workings
- Process will be modified or extended
- Process has complex error handling or decision logic

## Required Artifact Naming (STRICT)

These filenames are REQUIRED (case-sensitive, exact):
1. `DFD_master_progress.md`
2. `{project}_analysis.md` (e.g., `MyApp_analysis.md`)
3. `DFD_level1_tasks.md`
4. `DFD_level2_tasks.md` (ONLY if Level 2 Decision = Yes)
5. `DFD_level_analysis.md` (ALWAYS create in Phase D)

**Prohibited names (DO NOT use):**
- `DFD_Final_Documentation.md`
- `Final_Documentation.md`
- Any variation not exactly `DFD_level_analysis.md`

## Integration with run-redocumentation

When called from `run-redocumentation` orchestrator:
- This skill is **EXEMPT** from fresh assessment protocol
- Execute as complete self-contained multi-phase process
- DFD results are then used for subsequent orchestrator steps
- Typically invoked at Step 4.1 of redocumentation workflow

## Error Handling

**If conditions are not met:**
- Check master progress file exists and is up to date
- Verify all required files from previous phases exist
- Ensure master progress is coherent with actual completion status
- Request user review and correction before proceeding

**If session is interrupted:**
- Master progress file maintains state
- Resume from appropriate phase based on last completed step
- User review required before resuming

## Success Criteria

- [ ] All phases completed in sequence
- [ ] Master progress accurately reflects completion
- [ ] All required artifacts created with correct names
- [ ] Level 2 decision documented (even if "No")
- [ ] Final `DFD_level_analysis.md` contains complete documentation
- [ ] Stakeholder review completed

## Example Usage

```
Skill: generate-dfd-from-code
Parameters:
  source_path: ./your-repos/my-application/
  project_name: my-application
  output_dir: .olaf/work/staging/my-application/dfd/
```

---

**Skill Type:** Multi-Phase Analysis Chain
**Framework:** OLAF Progressive Documentation
**Integration:** run-redocumentation orchestrator compatible
