# Generate Orchestrator Tutorial

Step-by-step guide for using the generate-orchestrator skill.

## Prerequisites

- OLAF framework installed
- Appropriate permissions

## Steps

1. Run the skill.
2. Provide required inputs:
	- `orchestrator_name` (kebab-case)
	- `description`
	- `skills_to_orchestrate[]` (ordered)
3. Optionally provide:
	- `review_gates[]`
	- `stop_on_failure`
4. Review the proposed generated skill structure (Propose-Confirm-Act).
5. Confirm creation.
6. Review results under `skills/[orchestrator_name]/`.

## Result

You should see a new orchestrator skill package:
- `skills/[orchestrator_name]/skill.md`
- `skills/[orchestrator_name]/docs/description.md`
- `skills/[orchestrator_name]/docs/tutorial.md`
