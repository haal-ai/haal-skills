# ESDI Chain

**Source**: esdi-chain/skill.md

## Overview

ESDI Chain coordinates the complete ESDI workflow: Exploration → Specification → Design → Implementation planning. It orchestrates four sequential phases with review gates to transform an initial idea into an executable implementation plan.

## Purpose

Developing software from an initial idea to implementation requires a structured approach that ensures requirements are properly captured, designs are well-thought-out, and implementation plans are actionable. This skill provides a guided workflow that coordinates multiple specialized skills through the ESDI methodology.

## Usage

**Command**: `esdi chain` or `run esdi`

**Protocol**: Interactive with review gates at each phase

**When to Use**: Use this skill when starting a new development project from scratch, when you have an idea that needs to be systematically developed into an implementation plan, or when you want to ensure proper documentation throughout the development lifecycle.

## Parameters

### Required Inputs
- **idea**: Initial problem statement or goal description
- **topic**: Short topic name for folder (e.g., "repository-scanner", "api-gateway")

### Optional Inputs
- **output_dir**: Directory to store ESDI outputs (default: auto-generated)
- **design_patterns**: Path to design pattern guidance (default: `skills/esdi/kb/design-patterns-guidance.md`)
- **skip_reviews**: Skip review gates (default: `false`)
- **start_phase**: Resume from specific phase - `explore`, `specify`, `design`, or `plan`

### Context Requirements
- Access to OLAF framework and skills directory
- Write access for output directory
- Terminal access for timestamp generation

## Output

**Deliverables**:
- `exploration-findings.md` - Refined ideas and research
- `specification.md` - Formal EARS requirements
- `design.md` - Layered system architecture
- `IMPLEMENTATION-TASK-PLAN.md` - Executable task breakdown

**Output Directory Structure**:
```
.olaf/work/staging/esdi/YYYYMMDD-${topic}/
├── exploration-findings.md
├── specification.md
├── design.md
└── IMPLEMENTATION-TASK-PLAN.md
```

## Process Flow

### Phase 0: Initialization
- Select existing ESDI session or create new one
- Set up output directory structure
- Create session status tracking

### Phase 1: Exploration
- Interactive ideation using challenge-me skill
- Research and citation gathering
- Trajectory documentation
- User engagement: HIGH

### Phase 2: Specification
- Transform findings into EARS requirements using transform-raw-spec skill
- 7-step specification process
- Quality checks and completeness validation
- User engagement: HIGH

### Phase 3: Design
- Create layered system design using generate-design skill
- Architecture pattern selection
- Component and interface definition
- User engagement: MEDIUM

### Phase 4: Implementation Planning
- Generate task breakdown using generate-implementation-plan skill
- Requirement traceability matrix
- Executable task definitions
- User engagement: LOW (can be automated)

## Examples

### Example 1: New Project from Idea

**Input**:
- idea: "Repository onboarding system for scanning and analyzing codebases"
- topic: "repo-scanner"

**Output**: Complete ESDI artifacts in `.olaf/work/staging/esdi/20251122-repo-scanner/`

### Example 2: Resume from Design Phase

**Input**:
- topic: "repo-scanner"
- start_phase: "design"

**Output**: Continues from Phase 3, loading previous exploration and specification outputs

## Related Skills

- **challenge-me**: Phase 1 exploration and ideation
- **transform-raw-spec**: Phase 2 EARS specification transformation
- **generate-design**: Phase 3 layered system design
- **generate-implementation-plan**: Phase 4 task breakdown generation

## Tips

1. **Start with clear ideas**: The more detailed your initial idea, the better the exploration phase
2. **Engage in reviews**: Don't skip review gates - they ensure quality at each phase
3. **Use resume capability**: If interrupted, resume from the last completed phase
4. **Document decisions**: Capture all decisions made during interactive phases
5. **Iterate as needed**: Return to earlier phases if gaps are discovered

## Limitations

- Requires all dependent skills to be available (challenge-me, transform-raw-spec, generate-design, generate-implementation-plan)
- Phases 1-3 require interactive user engagement
- Cannot fully automate the entire workflow due to decision points
- Session state is directory-based, not database-backed
