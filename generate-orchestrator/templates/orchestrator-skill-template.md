# Orchestrator Skill Scaffold (Template)

This file is a scaffold for the GENERATED orchestrator skill package.
It is meant to be used as a structure/example with placeholders (similar to `skills/create-skill/templates/skill-template.md`).

---

## 1) `skills/[orchestrator_name]/skill.md`

```yaml
---
name: [verb-entity-complement orchestrator name]
description: [Brief description of what this orchestrator coordinates]
license: Apache-2.0
metadata:
  tags: [orchestrator, workflow, coordination, automation]
  plugins: [plugin1, plugin2]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---
```

```markdown
<olaf>

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list:
1. **description**: string - Brief description of orchestrator purpose (REQUIRED)
2. **skills_to_orchestrate**: array - Ordered list of skill names to execute (OPTIONAL)
3. **review_gates**: array - Named checkpoints requiring user confirmation (OPTIONAL)
4. **stop_on_failure**: boolean - Stop the orchestrator when a step fails (OPTIONAL - default: true)
5. **context_contract**: object|string - What each step produces and what next step consumes (OPTIONAL)

**Notes:**
- When this orchestrator is generated, it will typically be created with a fixed baked-in plan (the orchestrator already knows which skills it orchestrates).
- You MAY allow `skills_to_orchestrate` as a runtime override, but only if it does not break the orchestrator's intent.

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Use Propose-Confirm-Act for modifications

## Process

### 1. Validation Phase
You MUST verify:
- The orchestrator has an explicit list of skills to run (either baked-in OR provided via `skills_to_orchestrate[]`)
- If `skills_to_orchestrate[]` is provided: it is not empty
- Each referenced skill name exists under `skills/` (or the user provides the correct names)
- The execution order is explicit
- Required inputs/outputs between steps are understood

### 2. Execution Phase
You WILL orchestrate the workflow in strict step order.

#### Example Orchestration Plan (placeholder)
1. Step 1: Execute `[skill-name-1]`
   - Inputs: [what the user must provide]
   - Outputs: [files/variables produced]
   - Review gate: [optional gate name]

2. Step 2: Execute `[skill-name-2]`
   - Inputs: [what comes from step 1]
   - Outputs: [files/variables produced]

#### Failure Handling (placeholder)
- If a step fails and `stop_on_failure=true`: STOP and provide recovery instructions
- If `stop_on_failure=false`: record the failure and ask the user whether to continue

### 3. Validation Phase
You WILL validate:
- The goal is met: [define what “met” means]
- Expected artifacts exist (if applicable):
  - [path/to/artifact-1]
  - [path/to/artifact-2]

## Output Format
You WILL output:
- Execution summary (what ran, in what order)
- Files created/modified (paths)
- Any blockers or open questions
- Next steps

## User Communication
You WILL provide:
- Progress updates per step
- A completion summary

## Success Criteria
- [ ] All required parameters validated
- [ ] Orchestration steps defined
- [ ] Steps executed (or intentionally stopped) according to gates/failure policy
- [ ] Outputs validated

## Error Handling
You WILL handle:
- Missing parameters
- Unknown skill names
- Missing expected artifacts
- Partial failure and recovery

⚠️ **Critical Requirements**
- NEVER reference competency structures
- NEVER rely on skill manifests
- ALWAYS use imperative language consistently
```

---

## 2) `skills/[orchestrator_name]/docs/description.md`

```markdown
# [Orchestrator Name]

## Overview
[What this orchestrator does]

## When to Use
[Scenarios]

## Inputs
- `description`
- `skills_to_orchestrate[]` (if runtime override is supported)

## Outputs
[What files/decisions it produces]

## Limitations
[Constraints]
```

---

## 3) `skills/[orchestrator_name]/docs/tutorial.md`

```markdown
# [Orchestrator Name] - Tutorial

## Prerequisites
- [Any prerequisites]

## Steps
1. [Step]
2. [Step]
3. [Step]

## Example
- description: "[example description]"
- skills_to_orchestrate: ["skill-a", "skill-b"]

## Troubleshooting
- [Common issue] → [Resolution]
```
