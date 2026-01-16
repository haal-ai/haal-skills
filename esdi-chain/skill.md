---
name: esdi-chain
description: "Coordinate the ESDI workflow: Exploration → Specification → Design → Implementation planning"
license: Apache-2.0
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Run-ESDI Workflow Coordinator

## Mission

Orchestrate the complete development lifecycle from initial idea to executable implementation plan through four sequential phases with review gates.

## Context Variables

**Required**:
- `idea`: Initial problem statement or goal description
- `topic`: Short topic name for folder (e.g., "repository-scanner", "api-gateway")

**Optional**:
- `output_dir`: Directory to store ESDI outputs (default: auto-generated)
- `design_patterns`: Path to design pattern guidance (default: `skills/esdi/kb/design-patterns-guidance.md`)
- `skip_reviews`: Skip review gates (default: false)
- `start_phase`: Resume from specific phase (explore|specify|design|plan)

## Output Directory Structure

**Auto-generated path** (if output_dir not provided):
```
.olaf/work/staging/esdi/YYYYMMDD-${topic}/
```

**Example**:
```
.olaf/work/staging/esdi/20251122-repository-scanner/
├── exploration-findings.md
├── specification.md
├── design.md
└── IMPLEMENTATION-TASK-PLAN.md
```

**Manual path** (if output_dir provided):
```
${output_dir}/
├── exploration-findings.md
├── specification.md
├── design.md
└── IMPLEMENTATION-TASK-PLAN.md
```

## Execution Model

**CRITICAL**: ESDI is NOT a single automated workflow. It's a 4-phase guided process:

**Phases 1-3**: Interactive IDE sessions (user engagement required)
**Phase 4**: Can be automated via STRAF agent

### How to Execute ESDI

**Option A - Manual Execution (Recommended)**:
Run each phase separately in the IDE with user engagement:
1. Phase 1: Exploration (challenge-me) - Interactive ideation
2. Phase 2: Specification (transform-raw-spec) - Interactive EARS transformation
3. Phase 3: Design (generate-design) - Interactive design review
4. Phase 4: Implementation (generate-implementation-plan) - Can automate via STRAF

**Option B - This Coordinator (Documentation Only)**:
This file documents the workflow but is NOT meant to be executed as a STRAF agent.
Use it as a reference guide for the 4-phase process.

## Workflow Execution

### Phase 0: Initialization & Session Management

**Objective**: Select existing ESDI session or create new one

**Execution**: Interactive in IDE

```
1. Get environment information and timestamp:
   Initialize session context for tracking.

2. List existing ESDI sessions:
   Execute task: tasks/list-esdi-sessions.md
   
   Display:
   - In-progress sessions (missing implementation plan)
   - Completed sessions
   - Stale/abandoned sessions
   
3. User chooses action:
   a) Resume existing ESDI session
   b) Create new ESDI session
   c) View session details
   
4a. IF RESUME EXISTING:
   - User selects session by number
   - Load esdi-status.md
   - Identify current phase and next action
   - Set $output_dir to existing session directory
   - Display: "Resuming ESDI: ${topic} at Phase ${current_phase}"
   - Skip to appropriate phase
   
4b. IF CREATE NEW:
   - Ask user for topic: "What is the topic/name for this ESDI project? (use kebab-case)"
   - Ask for idea: "Describe the problem statement or goal"
   - $topic = [user-provided-topic]
   - $output_dir = ".olaf/work/staging/esdi/${timestamp}-${topic}"
   - Create directory: New-Item -ItemType Directory -Path $output_dir -Force
   - Create esdi-status.md from template
   - Update status: Session created
   - Display: "📁 New ESDI Session: ${output_dir}"
   
5. Save state: 
   - initialization_complete = true
   - topic = ${topic}
   - output_dir = ${output_dir}
   - session_mode = "new" | "resume"
```

### Phase 1: Exploration

**Objective**: Discover requirements and constraints

**Execution**: Interactive in IDE with GitHub Copilot agent
**User Engagement**: HIGH - Iterative ideation cycles until user says "save"

```
Run challenge-me skill manually in IDE:

@workspace /new Create intelligent onboarding system for repository scanning

The agent will guide you through:
  - Ideation cycles with challenges and refinements
  - Research and citation gathering
  - Trajectory documentation
  - Loop until you say "save"

Expected outputs in ${output_dir}:
  - think.md (final refined ideas)
  - path.md (evolution trajectory)
  - sources.md (citations)
  - reco.md (recommendations)
  OR
  - exploration-findings.md (consolidated exploration output)

⭐ Update status:
  Execute task: tasks/update-esdi-status.md
  - phase = "E"
  - artifacts = ["exploration-findings.md"]
  - Mark Phase E as completed in esdi-status.md

Save state: exploration_complete = true
```

### Phase 2: Specification

**Objective**: Transform findings into formal EARS requirements

**Execution**: Interactive in IDE with GitHub Copilot agent
**User Engagement**: HIGH - Decision making at steps 3, 4, 5

```
Run transform-raw-spec skill manually in IDE:

@workspace Transform think.md into EARS specification using Propose-Act protocol

Input: ${output_dir}/think.md (and reco.md for recommendations)
Output: ${output_dir}/

The agent will guide you through 7 steps:
  - Step 1: Clarify & Group (automated)
  - Step 2: Transform to EARS (automated)
  - Step 3: Quality Check (USER DECISIONS REQUIRED)
  - Step 4: Completeness (USER DECISIONS REQUIRED)
  - Step 5: Challenge & Amplify (USER DECISIONS REQUIRED)
  - Step 6: Visual Documentation (automated)
  - Step 7: Testability Assessment (automated)

Expected outputs in ${output_dir}:
  - step1-<timestamp>.md through step7-<timestamp>.md
  - specification.md ⭐ FINAL consolidated EARS spec (for Phase 3)

⭐ Update status:
  Execute task: tasks/update-esdi-status.md
  - phase = "S"
  - artifacts = ["specification.md", "step1-*.md", "step2-*.md", ..., "step7-*.md"]
  - Mark Phase S as completed in esdi-status.md

Save state: specification_complete = true
```

### Phase 3: Design

**Objective**: Create layered system design

**Execution**: Interactive in IDE with GitHub Copilot agent
**User Engagement**: MEDIUM - Review and refine architecture

```
Run generate-design skill manually in IDE:

@workspace Generate layered system design from EARS specification

Input: ${output_dir}/specification.md ⭐ (final EARS from Phase 2)
Output: ${output_dir}/design.md

The agent will guide you through:
  - Analyze EARS specification
  - Identify application type
  - Design layer architecture
  - Create task breakdown
  - Generate design document

User reviews and refines the architecture during this process.

Expected output in ${output_dir}:
  - design.md (complete layered system design)

⭐ Update status:
  Execute task: tasks/update-esdi-status.md
  - phase = "D"
  - artifacts = ["design.md"]
  - Mark Phase D as completed in esdi-status.md

Save state: design_complete = true
```

### Phase 4: Implementation Planning

**Objective**: Generate task breakdown with STRAF commands and requirement traceability

**Execution**: Automated via STRAF agent
**User Engagement**: LOW - Can run autonomously

```
Run via STRAF agent (command line):

python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "skills/generate-implementation-plan/skill.md" `
  --context "specification_file=${output_dir}/specification.md,design_file=${output_dir}/design.md,output_file=${output_dir}/IMPLEMENTATION-TASK-PLAN.md,skill_path=skills/${topic}" `
  --tool-mode standard `
  --aws-profile bedrock

Auto-validation:
  - Verify Task 0.0 (extract contexts) is included
  - Check requirement traceability matrix generated
  - Validate requirement coverage (≥85% recommended)
  - Check all tasks have STRAF commands
  - Validate dependencies are logical

Expected output in ${output_dir}:
  - IMPLEMENTATION-TASK-PLAN.md (complete task breakdown with requirement traceability)

⭐ Update status:
  Execute task: tasks/update-esdi-status.md
  - phase = "I"
  - artifacts = ["IMPLEMENTATION-TASK-PLAN.md"]
  - Mark Phase I as completed in esdi-status.md
  - Set session status to "Completed"

Save state: implementation_plan_complete = true
```

### Phase 5: Ready for Bootstrap

```
Display completion message:

✅ ESDI Workflow Complete!

📁 Output Directory: ${output_dir}

Generated Artifacts:
  Phase 1 - Exploration:
    ✅ think.md     - Final refined ideas
    ✅ path.md      - Evolution trajectory  
    ✅ sources.md   - Citations and references
    ✅ reco.md      - Actionable recommendations
  
  Phase 2 - Specification:
    ✅ step1-*.md through step7-*.md - EARS transformation steps
    ✅ specification.md - Consolidated formal requirements
  
  Phase 3 - Design:
    ✅ design.md - Layered system architecture
  
  Phase 4 - Implementation:
    ✅ IMPLEMENTATION-TASK-PLAN.md - Task breakdown with STRAF commands

Next Step: Execute implementation plan

  python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
    --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" \
    --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md" \
    --tool-mode auto \
    --aws-profile bedrock
```

## State Management

Track progress across phases:

```json
{
  "workflow": "esdi",
  "topic": "repository-scanner",
  "timestamp": "20251122",
  "output_dir": ".olaf/work/staging/esdi/20251122-repository-scanner",
  "current_phase": "design",
  "phases": {
    "init": { "status": "completed", "output": null },
    "explore": { "status": "completed", "output": "exploration-findings.md" },
    "specify": { "status": "completed", "output": "specification.md" },
    "design": { "status": "in-progress", "output": "design.md" },
    "plan": { "status": "pending", "output": "IMPLEMENTATION-TASK-PLAN.md" }
  }
}
```

## Error Handling

```
IF phase fails:
  - Log error details
  - Save current state
  - Allow resume from failed phase
  - Provide diagnostic information

IF user cancels review:
  - Save current state
  - Exit gracefully
  - Allow resume later
```

## Success Criteria

✅ All 4 phases completed
✅ Each output file exists and is valid
✅ Implementation plan includes Task 0.0
✅ All review gates passed (if enabled)
✅ Ready for bootstrap execution

## Resume Capability

```bash
# Resume from specific phase with same topic
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/run-esdi/prompts/run-esdi-coordinator.md" \
  --context "topic=repository-scanner,start_phase=design" \
  --tool-mode standard \
  --aws-profile bedrock
```

The coordinator will:
1. Look for existing output directory: `.olaf/work/staging/esdi/YYYYMMDD-${topic}`
2. Verify previous phases completed
3. Continue from specified phase

## Tools Required

- `file_write`: Save outputs from each phase
- `file_read`: Load inputs for next phase
- `spawn_straf_child_agent`: Invoke phase skills
- `json_state`: Manage workflow state

## Example Execution

```bash
# Start new ESDI workflow (auto-generated directory)
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/run-esdi/prompts/run-esdi-coordinator.md" \
  --context "idea=Repository onboarding system,topic=repo-scanner" \
  --tool-mode auto \
  --aws-profile bedrock

# Output will be in: .olaf/work/staging/esdi/20251122-repo-scanner/

# Start with custom output directory
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/run-esdi/prompts/run-esdi-coordinator.md" \
  --context "idea=Repository onboarding system,topic=repo-scanner,output_dir=./custom/path" \
  --tool-mode auto \
  --aws-profile bedrock
```

## Integration Notes

This coordinator is **agnostic to implementation** - it only orchestrates the workflow. Each phase skill (challenge-me, transform-raw-spec, generate-design, generate-implementation-plan) contains the actual logic.

**Dependencies** (must exist before ESDI can run):
- ✅ challenge-me skill
- ✅ transform-raw-spec skill
- ✅ generate-design skill
- ✅ generate-implementation-plan skill
