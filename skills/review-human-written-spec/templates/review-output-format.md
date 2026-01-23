# AI Review of Human-Written Specification

## 0) How to use this review (SME + producer workflow)

### 0.1 SME: answer directly in this file
- The SME SHOULD edit this AI review document directly.
- Fill the **SME answer worksheet** and/or the **SME answer** column in the questions table.

### 0.2 Producer: generate business decisions (drafted by the skill)
- After SME answers are filled, run a **follow-up review**.
- In follow-up mode, the skill will generate a **business decision draft** under:
  - `docs/specifications/<demand_folder>/03-business-decisions/`

### 0.3 Producer: approve decisions, then generate specifications
- After the decisions draft is written, the user MUST review it.
- To approve and allow spec generation, the user MUST reply with this exact sentence:
  - `I approved this decision`
- Only after approval, the workflow will generate `docs/specifications/<demand_folder>/04-specifications/`:
  - A dev-ready functional specification (overview)
  - A dev-ready functional specification (detailed, including Mermaid diagrams)
  - An OpenAPI specification

### 0.4 Copy/paste to run the follow-up review
```text
@[/olaf-review-human-written-spec]
demand_folder: <demand_folder>
review_mode: followup
previous_review_path: <path-to-previous-ai-review>
```

### 0.5 Strict gating rule
- If any **High** priority question is unanswered, ambiguous, or missing an explicit **TBD + decision owner + target date**, the follow-up run MUST stop and ask for clarification.

## 1) Review metadata
- Spec title:
- Spec path:
- Review timestamp (YYYYMMDD-HHmm):
- Review mode (initial/followup):
- Intended API goal:

## 2) Executive summary
- What the spec enables well:
- What is unclear / missing:
- Highest-risk gaps (top 5):

## 3) Extracted scope
### 3.1 In-scope capabilities

### 3.2 Out-of-scope items

### 3.3 Primary actors / roles

## 4) Extracted business rules and data
### 4.1 Business rules

### 4.2 Data elements (business-level)

## 5) Domain model (API-relevant)
### 5.1 Entities and relationships

### 5.2 Identifiers

### 5.3 Lifecycles and states

## 6) API design implications (draft)
- Candidate resources:
- Expected operations:
- Key searches/filters:
- Security assumptions:

## 7) Questions for the Subject Matter Expert (SME)
Use the template: `templates/questions-table-format.md`.

### 7.1 How to provide answers (for the SME)
- Answer **each question ID** (Q-001, Q-002, …).
- If the question includes “Proposed options”, you MAY answer using:
  - The **option number(s)**, and
  - Any necessary rule details (thresholds, durations, constraints).
- If none of the options fit, answer with **"Custom:"** followed by the rule in plain language.
- If you cannot decide now, answer with **"TBD"** and provide who decides + by when.

### 7.2 What happens next (after answers are provided)
- Update the demand documents so decisions become part of the source of truth.
- Run a follow-up review to resolve questions and remove assumptions.
- Produce the OpenAPI contract draft (schemas, lifecycle/status, errors, security, search/pagination).
- Generate API tests (Postman/Bruno) from the contract.

### 7.3 SME answer worksheet
Provide a simple table for SME answers (or link to a separate answers file).

## 8) Assumptions made by this review
List assumptions explicitly. Each assumption MUST be challengeable.

## 9) Follow-up plan
- What to confirm next with the SME:
- What decisions unlock OpenAPI design:
