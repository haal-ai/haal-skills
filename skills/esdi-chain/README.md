---
name: esdi
description: "ESDI Chain - Exploration → Specification → Design → Implementation plan generation"
version: 1.0.0
type: chain
tags: [meta-skill, workflow, development-lifecycle, esdi]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

# ESDI: Exploration → Specification → Design → Implementation

A meta-skill that chains together the complete development lifecycle from initial idea to executable implementation plan.

## Overview

**ESDI** guides you through four phases:
1. **E**xploration - Discover requirements through challenge-me prompting
2. **S**pecification - Transform findings into formal EARS specification
3. **D**esign - Create layered system design from specification
4. **I**mplementation - Generate task breakdown with STRAF commands

## Output Structure

**Auto-generated directory**:
```
.olaf/work/staging/esdi/YYYYMMDD-${topic}/
├── esdi-status.md               # ⭐ Session tracking (phases, dates, artifacts)
├── exploration-findings.md      # Discovery results (Phase 1)
├── step1-*.md through step7-*.md # EARS refinement steps (Phase 2)
├── specification.md             # ⭐ Final EARS spec (Phase 2 → 3)
├── design.md                    # Architecture & layers (Phase 3)
└── IMPLEMENTATION-TASK-PLAN.md  # Executable tasks (Phase 4)
```

**Example**:
```
.olaf/work/staging/esdi/20251122-repository-scanner/
├── exploration-findings.md      # Discovery results (Phase 1)
├── step1-*.md through step7-*.md # EARS refinement steps (Phase 2)
├── specification.md             # ⭐ Final EARS spec (Phase 2 → 3)
├── design.md                    # Architecture & layers (Phase 3)
└── IMPLEMENTATION-TASK-PLAN.md  # Executable tasks (Phase 4)
```

## Chain Links

### Link 1: Exploration (challenge-me)
- **Skill**: `challenge-me`
- **Input**: Initial idea, problem statement, or goal
- **Output**: `exploration-findings.md` - Requirements discovery, insights, constraints
- **Review**: Vibe coding with user to refine findings

### Link 2: Specification (transform-raw-spec)
- **Skill**: `transform-raw-spec` 
- **Input**: `exploration-findings.md`
- **Output**: `specification.md` - Final consolidated EARS requirements document (plus step1-7 files)
- **Review**: Vibe coding with user to validate requirements (Steps 3-5 require decisions)

### Link 3: Design (generate-design)
- **Skill**: `generate-design`
- **Input**: `specification.md` + design pattern guidance
- **Output**: `design.md` - Layered architecture, interfaces, data flows
- **Review**: Vibe coding with user to approve design

### Link 4: Implementation Planning (generate-implementation-plan)
- **Skill**: `generate-implementation-plan`
- **Input**: `design.md`
- **Output**: `IMPLEMENTATION-TASK-PLAN.md` - Task breakdown with STRAF commands
- **Auto-includes**: Task 0.0 (extract task contexts) as mandatory prep

## Usage

### Session Management

**List Existing ESDI Sessions**:
```bash
# View all ESDI sessions (in-progress, completed, stale)
# Shows which phase each session is on
```

**Resume Existing Session**:
```bash
# Select from list of in-progress sessions
# Automatically jumps to current phase
# Loads existing artifacts and status
```

**Create New Session**:
```bash
# Starts fresh ESDI workflow
# Creates new session directory with timestamp
# Initializes esdi-status.md for tracking
```

### Full Chain Execution (Auto-generated Directory)

```bash
# Run complete ESDI workflow - outputs to .olaf/work/staging/esdi/YYYYMMDD-${topic}
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/run-esdi/prompts/run-esdi-coordinator.md" \
  --context "idea=Repository onboarding system,topic=repo-scanner" \
  --tool-mode auto \
  --aws-profile bedrock

# Custom output directory
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/run-esdi/prompts/run-esdi-coordinator.md" \
  --context "idea=Repository onboarding system,topic=repo-scanner,output_dir=./my-competency" \
  --tool-mode auto \
  --aws-profile bedrock
```

### Resume from Specific Phase

```bash
# Resume from design phase
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/run-esdi/prompts/run-esdi-coordinator.md" \
  --context "topic=repo-scanner,start_phase=design" \
  --tool-mode auto \
  --aws-profile bedrock
```

## Chain Configuration

```yaml
chain:
  name: run-esdi
  phases:
    - id: explore
      skill: challenge-me
      inputs:
        - idea: ${user_idea}
      outputs:
        - findings: exploration-findings.md
      review_required: true
      
    - id: specify
      skill: transform-raw-spec
      inputs:
        - raw_spec: ${explore.findings}
      outputs:
        - specification: specification.md
      review_required: true
      
    - id: design
      skill: generate-design
      inputs:
        - specification: ${specify.specification}
        - patterns: ${design_patterns_guidance}
      outputs:
        - design: design.md
      review_required: true
      
    - id: plan
      skill: generate-implementation-plan
      inputs:
        - design: ${design.design}
      outputs:
        - plan: IMPLEMENTATION-TASK-PLAN.md
      review_required: false  # Auto-generated, ready for bootstrap
```

## Design Pattern Guidance

The design phase uses guidance files to ensure consistent patterns:

```
skills/esdi/kb/
├── design-patterns-guidance.md
│   ├── Layered architecture
│   ├── Event-driven patterns
│   ├── Microservices patterns
│   └── Data flow patterns
└── layered-architecture-template.md
    ├── Layer definition template
    ├── Interface specifications
    └── Success criteria per layer
```

## Output Structure

After running ESDI chain with auto-generated directory, you'll have:

```
.olaf/work/staging/esdi/YYYYMMDD-${topic}/
├── exploration-findings.md      # Phase 1 output
├── specification.md             # Phase 2 output (EARS format)
├── design.md                    # Phase 3 output (layered architecture)
├── IMPLEMENTATION-TASK-PLAN.md  # Phase 4 output (ready for bootstrap)
└── kb/
    └── [design artifacts]
```

**Directory Naming**:
- `YYYYMMDD`: Timestamp of execution (e.g., 20250102)
- `${topic}`: User-provided topic parameter (e.g., repo-scanner)
- Example: `.olaf/work/staging/esdi/20250102-repo-scanner/`

## Integration with Bootstrap

Once ESDI completes, execute the implementation plan:

```bash
# Run bootstrap orchestrator with generated plan
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" \
  --context "bootstrap_doc=.olaf/work/staging/esdi/20250102-repo-scanner/IMPLEMENTATION-TASK-PLAN.md,checklist_path=.olaf/work/project-tasks/task-checklist.md" \
  --tool-mode auto \
  --aws-profile bedrock
```

## Example: Onboarding Competency

The onboarding competency was developed using ESDI principles:

1. **Exploration**: Analyzed repository onboarding needs → findings
2. **Specification**: Created EARS requirements for onboarding system
3. **Design**: Designed 5-layer architecture (ONBOARDING-SYSTEM-DESIGN.md)
4. **Implementation**: Generated 47-task plan (IMPLEMENTATION-TASK-PLAN.md)
5. **Bootstrap**: Executed via bootstrap-orchestrator.md

## Benefits

✅ **Structured approach** - No ad-hoc development
✅ **Review gates** - User validates each phase
✅ **Pattern reuse** - Design guidance ensures consistency  
✅ **Automation ready** - Output feeds directly into bootstrap
✅ **Traceable** - Clear lineage from idea to implementation

## Future Enhancements

- [ ] Automated design pattern selection based on specification
- [ ] Cost/time estimation from implementation plan
- [ ] Dependency analysis across tasks
- [ ] Auto-generation of test plans from specification

## Dependencies

**Existing Skills**:
- ✅ `challenge-me` (exploration)
- ✅ `transform-raw-spec` (specification refinement)
- ✅ `generate-design` (architecture design with application type detection)
- ✅ `generate-implementation-plan` (design → task breakdown with Task 0.0)

## Notes

This meta-skill represents the **ideal OLAF development workflow**. Once all dependencies exist, any new competency can be bootstrapped end-to-end without manual "vibe coding" beyond review gates.
