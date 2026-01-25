# generate-dfd-from-code

## Overview

Generate comprehensive Data Flow Diagrams (DFD) from source code through systematic multi-phase analysis. This skill creates Context Diagrams, Level 1 DFDs, optional Level 2 DFDs, and consolidated final documentation.

## Key Features

- **Multi-Phase Approach**: 4 phases, 12 steps for thorough analysis
- **Progressive Documentation**: Each phase builds on previous work
- **Automatic Level 2 Decision**: Determines if Level 2 decomposition is needed
- **Quality Gates**: Built-in validation at each phase transition
- **Stakeholder-Ready Output**: Business and technical summaries

## When to Use

- Reverse-engineering existing applications
- Creating architecture documentation
- Understanding data flows in legacy systems
- Preparing for system modernization
- Onboarding new team members to a codebase

## Integration

This skill integrates with the `run-redocumentation` orchestrator and is typically invoked at Step 4.1 of systematic redocumentation workflows.

## Output Artifacts

- `DFD_master_progress.md` - Progress tracking
- `{project}_analysis.md` - Main analysis document
- `DFD_level1_tasks.md` - Level 1 task tracking
- `DFD_level2_tasks.md` - Level 2 task tracking (if needed)
- `DFD_level_analysis.md` - Final consolidated documentation
