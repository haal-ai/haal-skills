# run-redocumentation

## Overview

The `run-redocumentation` skill executes systematic redocumentation of multi-repository or complex applications by following an orchestrator plan, tracking progress, and generating carry-over files at each step. It uses a Fresh Assessment methodology that prioritizes direct source code analysis over reading previous analysis documents.

## Purpose

This skill enables documentation maintainers to:
- Execute systematic redocumentation workflows
- Track progress across multiple sessions
- Generate carry-over files for session continuity
- Ensure fresh insights through direct source analysis

## Key Features

- **Fresh Assessment Methodology**: Focuses on direct source code analysis rather than synthesizing previous documents
- **Orchestrator-Driven**: Follows a predefined plan with sequential steps
- **Progress Tracking**: Maintains detailed progress files with timestamps and status
- **Carry-Over Generation**: Creates session handoff files for continuity
- **Quality Gates**: Validates completeness at each step
- **Multi-Project Support**: Reusable across different project types

## Usage

Invoke this skill when you need to execute a step in a systematic redocumentation process.

### Parameters

This skill uses file-based configuration rather than direct parameters:

| File | Location | Description |
|------|----------|-------------|
| Orchestrator Plan | `.olaf/work/staging/{project-name}/artifacts/redocument-{project-name}-orchestrator.md` | Defines the sequence of documentation steps |
| Progress Tracker | `.olaf/work/staging/{project-name}/artifacts/redocument-{project-name}-progress.md` | Tracks completion status of each step |
| Target Application | `your-repos/{project-name}/` | Source code to analyze |

### Example Project Setup

```
.olaf/work/staging/ecommerce-platform/
├── artifacts/
│   ├── redocument-ecommerce-platform-orchestrator.md
│   └── redocument-ecommerce-platform-progress.md
└── carry-overs/
    └── carry-over-20260115-1430.txt

your-repos/ecommerce-platform/
├── src/
├── tests/
└── docs/
```

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP 1: REVIEW CURRENT PROGRESS                  │
│  • Locate progress tracker file                                  │
│  • Load orchestrator plan                                        │
│  • Identify next pending step                                    │
│  • Validate prerequisites                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              STEP 1.5: FRESH ASSESSMENT PROTOCOL                 │
│  • Review progress tracker for structure only                    │
│  • Target analysis at actual source code                         │
│  • Avoid reading previous analysis documents                     │
│  • Generate NEW insights through direct examination              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              STEP 2: EXECUTE NEXT STEP                           │
│  • Load specific OLAF competency for the step                    │
│  • Apply competency to source code directly                      │
│  • Follow competency's protocol                                  │
│  • Generate artifacts with fresh findings                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              STEP 3: UPDATE PROGRESS TRACKING                    │
│  • Update step status (Started → Completed)                      │
│  • Record timestamps (YYYYMMDD-HHmm format)                      │
│  • Document generated artifact locations                         │
│  • Note any issues encountered                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              STEP 4: GENERATE CARRY-OVER FILE                    │
│  • Create carry-over in carry-overs/ directory                   │
│  • Include completion summary                                    │
│  • Prepare next step context                                     │
│  • Follow naming: carry-over-YYYYMMDD-HHmm.txt                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              STEP 5: PREPARE NEXT ITERATION                      │
│  • Identify next step in orchestration plan                      │
│  • Validate readiness to proceed                                 │
│  • Provide clear status for continuation                         │
└─────────────────────────────────────────────────────────────────┘
```

## Output

### Progress Tracker Updates

The progress file is updated with:
- Step status changes
- Start and completion timestamps
- Generated artifact locations
- Issues or notes encountered
- Overall progress metrics

### Carry-Over Files

Generated in `carry-overs/` directory with:
- Current step completion summary
- Next step preparation details
- Context for continuation
- Key artifacts and findings
- Named: `carry-over-YYYYMMDD-HHmm.txt`

### Step-Specific Artifacts

Documentation artifacts generated based on the orchestrator plan, stored in the staging directory.

## Examples

### Example 1: Web Application Redocumentation

**Project Setup:**
```
Project Name: ecommerce-platform
Orchestrator: .olaf/work/staging/ecommerce-platform/artifacts/redocument-ecommerce-platform-orchestrator.md
Progress: .olaf/work/staging/ecommerce-platform/artifacts/redocument-ecommerce-platform-progress.md
Source: your-repos/ecommerce-platform/
```

**Execution:** Skill identifies next step (e.g., "Analyze API endpoints"), loads appropriate competency, analyzes source code directly, generates API documentation, updates progress, creates carry-over file.

### Example 2: Microservices Documentation

**Project Setup:**
```
Project Name: payment-gateway
Orchestrator: .olaf/work/staging/payment-gateway/artifacts/redocument-payment-gateway-orchestrator.md
Progress: .olaf/work/staging/payment-gateway/artifacts/redocument-payment-gateway-progress.md
Source: your-repos/payment-gateway/
```

**Execution:** Skill processes each microservice according to orchestrator plan, tracking progress across multiple sessions.

## Fresh Assessment Methodology

### Why Fresh Assessment?

| Problem | Solution |
|---------|----------|
| Synthesis loops | Direct code analysis prevents rewriting existing content |
| Reduced discovery | Fresh examination uncovers implementation gaps |
| Echo chambers | Avoids document-to-document synthesis |
| Stale insights | Each step generates NEW findings |

### What to Analyze

- Source code files
- Configuration files
- Build scripts
- API contracts
- Database schemas

### What NOT to Read

- Previous step analysis documents (except for structure)
- Prior documentation artifacts
- Historical analysis reports

### Exception: DFD Analysis

The DFD (Data Flow Diagram) competency is exempt from fresh assessment protocol as it uses its own multi-phase system (Phase A→B→C→D) that requires reading its own previous phases.

## Error Handling

| Scenario | Handling |
|----------|----------|
| Execution issues | Document in progress tracker |
| Failed steps | Create detailed error reports |
| Missing prerequisites | Provide recovery recommendations |
| Carry-over context issues | Include error context for troubleshooting |

## Success Criteria

- [ ] Next step identified and executed successfully
- [ ] Progress tracker updated accurately
- [ ] Required artifacts generated and stored properly
- [ ] Carry-over file created with complete context
- [ ] System ready for next iteration or completion

## Related Skills

- `carry-over-session` - For session handoff management
- `generate-orchestrator` - For creating orchestration plans
- `store-conversation-record` - For conversation documentation
