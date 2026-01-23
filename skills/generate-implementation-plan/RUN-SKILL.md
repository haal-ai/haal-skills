# Execute Generate Implementation Plan Skill

## Standalone Execution

Run this skill directly on an existing design.md file:

```powershell
# Use your environment's prompt runner / IDE agent to execute:
# - prompt: skills/generate-implementation-plan/skill.md
# - context: specification_file=...,design_file=...,output_file=...,execution_mode=manual
```

## Example: Generate Plan for ESDI Output

```powershell
# Assuming ESDI generated design.md in .olaf/work/staging/esdi/20251122-repo-scanner/
# prompt: skills/generate-implementation-plan/skill.md
# context: specification_file=.olaf/work/staging/esdi/20251122-repo-scanner/specification.md,design_file=.olaf/work/staging/esdi/20251122-repo-scanner/design.md,output_file=.olaf/work/staging/esdi/20251122-repo-scanner/IMPLEMENTATION-TASK-PLAN.md,execution_mode=manual
```

## Context Variables

**Required**:
- `specification_file`: Path to specification.md from transform-raw-spec skill
- `design_file`: Path to design.md from generate-design skill
- `output_file`: Path for IMPLEMENTATION-TASK-PLAN.md output

**Optional**:
- `deliverable_kind`: `tool|skill|library` (default: `skill`)
- `deliverable_root`: Root directory for deliverables
- `skill_path`: Back-compat alias for deliverable_root when generating an OLAF skill
- `skill_name`: Override skill name (default: extracted from design)
- `execution_mode`: `manual|bootstrap` (default: `manual`)
- `include_task_context_extraction`: `true|false` (default: `false`)
- `include_bootstrap`: `true|false` (default: `false`)
- `task_context_extractor_prompt`: Required if `include_task_context_extraction=true`
- `bootstrap_orchestrator_prompt`: Required if `include_bootstrap=true`

## What Happens

1. **Task 1**: Extract requirements + design layers → User approval gate
2. **Task 2**: Optionally generates Task 0.0 (condensed task context extraction) → User approval gate
3. **Task 3**: Creates complete task breakdown → User approval gate
4. **Task 4**: Validates requirement coverage → User approval gate
5. **Task 5**: Generates runner-agnostic execution notes for tasks → User approval gate
6. **Task 6**: Optionally creates bootstrap/runner integration info → User approval gate
7. **Task 7**: Writes final IMPLEMENTATION-TASK-PLAN.md → Act

## After Generation

If you generated a manual plan (`execution_mode=manual`), execute tasks manually.

If you generated a bootstrap plan (`execution_mode=bootstrap`), you must provide working paths for:
- `task_context_extractor_prompt` (if using Task 0.0)
- `bootstrap_orchestrator_prompt` (if using bootstrap orchestration)

## Via ESDI Workflow (Recommended)

This skill is automatically invoked in ESDI Phase 4:

```powershell
# Use your ESDI entrypoint to run phases 1-4.
# If you have a prompt runner, point it at the ESDI coordinator prompt and provide idea/topic context.
```

ESDI will run all 4 phases:
1. Exploration (challenge-me)
2. Specification (transform-raw-spec)
3. Design (generate-design)
4. **Implementation Planning (generate-implementation-plan)** ← THIS SKILL

## Notes

- ⚠️ **Task 0.0 must be run manually FIRST** before bootstrap execution
- ✅ All user approval gates require user approval
- 📊 Typical execution: 20-30 minutes for plan generation
- 🚀 Bootstrap execution: Varies by plan size (estimate in plan)

## Troubleshooting

**If design.md format not recognized**:
- Ensure design.md has "Layer 1:", "Layer 2:" sections
- Components should be listed under each layer
- Dependencies should be explicit

**If skill_path conflicts**:
- Check if target path already exists
- Provide unique skill_path in context variables

**If Task 0.0 fails**:
- Verify implementation plan is valid markdown
- Check skill_path directory is writable
- Ensure your runner/agent has necessary permissions
