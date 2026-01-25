# Tutorial: generate-dfd-from-code

## Introduction

This tutorial guides you through using the `generate-dfd-from-code` skill to create comprehensive Data Flow Diagrams from an existing codebase.

## Prerequisites

- Access to the source code you want to analyze
- A staging directory for output artifacts
- Basic understanding of DFD concepts (Context, Level 1, Level 2)

## Quick Start

### Step 1: Invoke the Skill

```
Skill: generate-dfd-from-code
Parameters:
  source_path: ./your-repos/my-application/
  project_name: my-application
  output_dir: .olaf/work/staging/my-application/dfd/
```

### Step 2: Phase A - Initial Analysis

The skill will:
1. Analyze your codebase structure
2. Identify external entities (users, APIs, databases)
3. Create a Context Diagram
4. Plan Level 1 analysis tasks

**Review Point**: Confirm the Context Diagram captures all major external interactions.

### Step 3: Phase B - Level 1 DFD

The skill will:
1. Identify 5-9 major processes
2. Map data stores
3. Document data flows
4. Decide if Level 2 is needed

**Review Point**: Verify Level 1 processes represent business functions, not implementation details.

### Step 4: Phase C - Level 2 DFD (Optional)

If Level 2 is required, the skill will:
1. Decompose complex processes
2. Show internal sub-processes
3. Document error handling paths
4. Map internal data stores

**Review Point**: Confirm Level 2 shows "how" processes work internally.

### Step 5: Phase D - Final Documentation

The skill will:
1. Consolidate all diagrams into `DFD_level_analysis.md`
2. Perform quality review
3. Prepare stakeholder summaries

## Example Output Structure

After completion, your output directory will contain:

```
.olaf/work/staging/my-application/dfd/
├── DFD_master_progress.md      # Shows 12/12 steps complete
├── my-application_analysis.md  # Detailed analysis with diagrams
├── DFD_level1_tasks.md         # Completed task checklist
├── DFD_level2_tasks.md         # (if Level 2 was needed)
└── DFD_level_analysis.md       # Final consolidated document
```

## Tips for Best Results

1. **Start with clean code**: Ensure the codebase compiles/runs
2. **Provide context**: Share any existing documentation
3. **Review at each phase**: Don't skip the review points
4. **Be specific about scope**: Define what's in/out of analysis

## Common Issues

### Too Many Level 1 Processes
If you end up with more than 9 processes, group related functions into higher-level business processes.

### Level 2 Decision Unclear
Consider Level 2 when:
- A process has complex internal logic
- Stakeholders need implementation details
- The process will be modified soon

### Missing External Entities
Check for:
- API consumers/providers
- Database connections
- File system interactions
- Message queues
- Third-party services

## Integration with run-redocumentation

When used within the `run-redocumentation` orchestrator:

1. The orchestrator invokes this skill at Step 4.1
2. DFD analysis runs as a complete self-contained process
3. Results feed into subsequent documentation steps
4. This skill is exempt from "fresh assessment" - it reads its own previous phases

## Next Steps

After completing DFD analysis:
1. Use diagrams for architecture reviews
2. Feed into functional specification generation
3. Support system modernization planning
4. Create onboarding materials for new developers
