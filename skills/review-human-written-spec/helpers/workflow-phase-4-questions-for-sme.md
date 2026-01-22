---
name: workflow-phase-4-questions-for-sme
description: Phase 4 - Produce SME questions with rationale and options
---

CRITICAL: This phase MUST use reference: `/kb/api-design-question-catalog.md`.

## Process
You WILL produce a comprehensive SME questionnaire.

### A) Coverage rule
You MUST cover, at minimum:
- Identity and uniqueness rules
- Lifecycle and state transitions
- Required searches and filters
- Error handling and validation expectations
- Security roles and access model
- Auditability requirements
- Concurrency/idempotency expectations (where relevant)
- Data retention / deletion rules

### B) Question construction
For each question, you MUST provide:
- Question text (clear, single topic)
- Why it matters (API design impact)
- Proposed options (2+ when feasible)
- Priority (High/Medium/Low)
- What it blocks (e.g., endpoint design, schema, search)
- Reference to spec section(s) (if available)

You MUST format the questions according to template: `templates/questions-table-format.md`.

## Output (Phase Artifact)
You WILL output:
- `sme_questions_table`
- `critical_decisions_summary`

## Error Handling
If you cannot find evidence in the spec for a topic, you MUST:
- Still ask the question
- Mark it as "Not specified in the provided document"
