---
name: workflow-phase-1-intake
description: Phase 1 - Intake and scoping for human specification review
---

CRITICAL: This is a phase prompt referenced by `/prompts/review-human-written-spec.md`.

## Inputs
You MUST have:
- The full text of all demand documents from `{demand_input_dir}` (already read)
- `api_intent`
- `review_mode` (+ `previous_review_path` if followup)

## Process
You WILL produce a structured intake summary:

### A) Specification metadata
You WILL extract or infer:
- Title
- Version/date (if stated)
- Authors/stakeholders (if stated)
- Intended audience

### B) Business scope
You WILL list:
- In-scope capabilities
- Out-of-scope items
- Primary users/roles

### C) Business processes
You WILL identify:
- Key processes / workflows
- Triggers and outcomes
- Any SLAs or business constraints

### D) Business rules and data
You WILL extract:
- Business rules (explicit)
- Data elements (explicit)
- Constraints and validations (explicit)

### E) Ambiguities and missing info (early list)
You WILL list the first set of gaps that block API design.

## Output (Phase Artifact)
You WILL output:
- `intake_summary`
- `extracted_requirements_list`
- `initial_gap_list`

## Error Handling
If the specification is inconsistent, you MUST:
- Quote the conflicting passages (short excerpts)
- State why it is a conflict
- Add it to the gap list
