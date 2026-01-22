# Delivery Impact & Remediation Plan (DB ↔ API)

## 0) How to use this plan (SME/PO + producer workflow)

### 0.1 SME/PO: answer directly in this file
- The SME/PO SHOULD edit this plan document directly.
- Fill section **6.2 SME/PO answer worksheet**.

### 0.2 Producer: re-run in follow-up mode (strict gating)
- After answers are filled, run a **follow-up**.
- In follow-up mode, the skill will:
  - Validate that answers are clear enough (strict gating)
  - Produce an updated plan with fewer assumptions

### 0.3 Copy/paste to run follow-up
```text
@[/olaf-plan-db-api-remediation]
demand_folder: <demand_folder>
plan_mode: followup
previous_data_fit_analysis_path: <path-to-data-fit-analysis>
previous_plan_path: <path-to-previous-delivery-impact-plan>
```

### 0.4 Strict gating rule
- If any **High** priority question is unanswered, ambiguous, or missing an explicit **TBD + decision owner + target date**, the follow-up run MUST stop and ask for clarification.

## 1) Document metadata
- Demand folder:
- Source data-fit analysis path:
- Functional spec path:
- Functional spec (detailed) path:
- OpenAPI path:
- Plan timestamp (YYYYMMDD-HHmm):
- Plan mode (initial/followup):
- Delivery target (if provided):
- Existing user impact tolerance (if provided):

## 2) Executive summary
- One-paragraph summary of the key difficulties and why they matter.
- Top 5 delivery blockers.

## 3) Delivery difficulties (mismatch-to-impact translation)
For each item:
- What the API/business requires
- What the DB currently supports (or not)
- Delivery impact (effort/risk)
- Impact on existing users (compatibility/data correctness/downtime)
- Options (keep vs simplify)

## 4) Must-have vs can drop/postpone candidates
- Must-have candidates (likely non-negotiable)
- Can drop/postpone candidates (reduce scope, reduce risk)

## 5) Questions for the SME/PO (delivery + impact decisions)
Use the template: `templates/questions-table-format.md`.

### 5.1 What happens next (after answers are provided)
- If scope can be reduced: update requirements/OpenAPI accordingly, then re-run.
- If scope cannot be reduced: approve a phased remediation plan (below) and execute it.

### 5.2 SME/PO answer worksheet
Provide long-form answers (preferred) per question ID.

| Question ID | SME/PO answer | Decision status (Decided/TBD) | Decision owner | Target date |
|---|---|---|---|---|
| Q-001 |  |  |  |  |

## 6) Phased remediation plan (only if scope is not reduced)

### Phase 0: Decisions, acceptance criteria, and release constraints

### Phase 1: Minimal compatible schema changes (no breaking changes)

### Phase 2: Backfill / data insertion / migration

### Phase 3: New capabilities requiring new tables (e.g., appointments)

### Phase 4: Hardening (audit, performance, monitoring)

## 7) Approval gate
- If you approve this plan, reply with this exact sentence:
  - `I approved this plan`
- If you do not approve, reply with:
  - What is wrong
  - What you want changed
  - Which requirements you want to abandon/postpone (if needed)
