# Generate Orchestrator

Generate-orchestrator creates a NEW orchestrator skill (a skill that uses other skills) under `skills/`.

## Usage

This skill generates orchestrator skills that orchestrate other skills.

## Outputs

Generated orchestrator skill package:
- `skills/[orchestrator_name]/skill.md`
- `skills/[orchestrator_name]/docs/description.md`
- `skills/[orchestrator_name]/docs/tutorial.md`

## Notes

- This repo no longer uses competency structures for new work.
- This repo no longer relies on skill manifests for generation.
- Prompting principles apply. This skill does NOT copy template/principles files into generated orchestrators.
