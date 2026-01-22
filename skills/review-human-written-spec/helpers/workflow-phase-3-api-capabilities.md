---
name: workflow-phase-3-api-capabilities
description: Phase 3 - Map business needs to API capabilities and decision points
---

CRITICAL: This is a phase prompt referenced by `/prompts/review-human-written-spec.md`.

## Process
You WILL translate the business needs into API capability expectations.

### A) Resource list
You MUST propose:
- Candidate API resources (aligned to domain entities)
- Which resources are first-class vs nested

### B) Operations
For each resource, you MUST propose which operations are needed:
- Create
- Read (by id)
- Search/list (with filters)
- Update (full vs partial)
- Delete (hard delete vs soft delete)

### C) Query & filtering expectations
You MUST identify:
- Typical lookup scenarios
- Required filters and sort order
- Pagination expectations

### D) Error model and validation
You MUST identify:
- Validation rules implied by the business
- Expected error scenarios (duplicates, missing references, invalid state transitions)

### E) Security & access
You MUST identify:
- Roles and permissions implied by the spec
- Any privacy or audit expectations

## Output (Phase Artifact)
You WILL output:
- `candidate_resources`
- `operation_matrix`
- `api_decision_points`

## Error Handling
If the spec has no security info, you MUST:
- Flag it as a critical API design gap
- Add SME questions proposing at least two plausible models
