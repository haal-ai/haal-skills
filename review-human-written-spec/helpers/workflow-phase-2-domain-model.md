---
name: workflow-phase-2-domain-model
description: Phase 2 - Domain model extraction and lifecycle reasoning for API readiness
---

CRITICAL: This is a phase prompt referenced by `/prompts/review-human-written-spec.md`.

## Process
You WILL derive an API-relevant domain model from the specification.

### A) Domain entities
You MUST identify:
- Entities (nouns that matter in the business)
- Key attributes per entity (business-level)
- Relationships (1:1, 1:N, N:N)

### B) Identifiers
You MUST identify (or flag missing):
- Primary identifiers used by the business (numbers, emails, natural keys)
- Whether identifiers are stable and unique
- Whether the API should expose natural keys or opaque IDs

### C) Lifecycles and states
You MUST identify:
- Entity lifecycle states (draft/active/cancelled/etc.)
- State transitions and triggers
- Temporal rules (start/end dates, validity windows)

### D) Reference data and enumerations
You MUST list:
- Enumerations (types, statuses, categories)
- Who manages them (staff/admin/system)

## Output (Phase Artifact)
You WILL output:
- `domain_entities`
- `relationships`
- `identifier_gaps`
- `lifecycle_gaps`

## Error Handling
If the spec uses the same word for different concepts, you MUST:
- Propose disambiguated terms
- Add an SME question to resolve naming
