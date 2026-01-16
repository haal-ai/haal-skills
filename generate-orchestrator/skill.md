---
name: generate-orchestrator
description: Generate orchestrator skills (skills that orchestrate other skills) under skills/
license: Apache-2.0
metadata:
  olaf_tags: [orchestrator, workflow, orchestration, automation, code-generation, templates]
  olaf_protocol: Propose-Confirm-Act
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.


## User Interaction Protocol
You MUST use Propose-Confirm-Act for any file or folder creation.

## Template Variables
- `[orchestrator_name]`: Name of the orchestrator skill being generated (kebab-case)

## Input Parameters
You MUST request missing parameters from the user before proceeding. Provide a numbered list with types and required/optional status.
1. **orchestrator_name**: string - Name for the new orchestrator skill (kebab-case, max 4 words) (REQUIRED)
2. **description**: string - Brief description of orchestrator purpose (REQUIRED)
3. **skills_to_orchestrate**: array - Ordered list of skill names to orchestrate (REQUIRED)
4. **review_gates**: array - Named checkpoints requiring user confirmation (OPTIONAL)
5. **stop_on_failure**: boolean - Whether to stop the orchestrator when a step fails (OPTIONAL - default: true)
6. **mode**: string - Generation mode (interactive|specification) (OPTIONAL - default: interactive)

## Process

## Template and Principles Loading
You MUST read in full and apply:
- `templates/prompting-principles.md`

You MUST read in full and follow:
- `templates/orchestrator-skill-template.md`

### 1. Validate Inputs
- If mode=interactive: collect and validate required parameters
- Else if mode=specification: ask user for the specification content or file path and validate it

### 2. Select and Load Template
- You MUST use `templates/orchestrator-skill-template.md` as the structural reference
- You WILL tailor the generated orchestrator skill to the user's orchestration needs

### 3. Gather Orchestration Details
- If interactive: Ask orchestrator-specific questions until all required parameters are complete
- If specification: Validate specification against the required sections of the orchestrator skill template

### 4. Generate Orchestrator Skill Package
You WILL generate an orchestrator as a first-class OLAF skill under `skills/`.

**Target output path**:
- `skills/[orchestrator_name]/skill.md`
- `skills/[orchestrator_name]/docs/description.md`
- `skills/[orchestrator_name]/docs/tutorial.md`

You MUST NOT copy prompting principles or template files into the generated orchestrator skill.

You MUST NOT generate competency files or use competency folder structures.
You MUST NOT generate or reference skill manifests.


### 5. Validate and Save
- Verify all required sections exist in `skills/[orchestrator_name]/skill.md`
- Verify required parameters are satisfied (`skills_to_orchestrate[]` must be non-empty)
- If `skills/[orchestrator_name]/` already exists, you MUST prompt for confirmation before overwriting

## Output Format

You WILL generate outputs following this structure:
- Primary deliverable: Generated orchestrator skill package
- File location: `skills/[orchestrator_name]/`
- Validation report: Summary of generated orchestrator and checks performed

## Error Handling
- If invalid input detected, provide specific error message
- If template not found, list available templates
- If specification invalid, provide validation errors
- If file already exists, prompt for confirmation

⚠️ **Critical Requirements**
- MANDATORY: Generated orchestrators must include framework validation
- NEVER compromise template structure
- ALWAYS validate input parameters before processing
- ALWAYS use kebab-case for file names

## Orchestrator Requirements
The generated orchestrator skill MUST:
- Explicitly list the skills to orchestrate (from `skills_to_orchestrate[]`)
- Define the execution order and any review gates
- Define stop-on-failure behavior and recovery guidance
- Define what context/output is passed from one step to the next
