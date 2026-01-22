# Review Human Written Spec

## What this skill does
This skill guides a multi-phase review of a human-written specification in order to:
- Challenge ambiguities and missing decisions
- Produce a structured question set for a Subject Matter Expert (SME)
- Prepare inputs that unblock API contract design (e.g., OpenAPI)

In follow-up mode, the skill also drafts a business decision document from the SME answers.

## When to use
Use this skill when you have a business-facing specification (often incomplete or ambiguous) and you need to design an API that serves the expressed needs.

## Outputs
- A markdown review document written under `docs/specifications/<demand_folder>/02-ai-review/` (after user confirmation)
- If `review_mode=followup`, a business decisions draft written under `docs/specifications/<demand_folder>/03-business-decisions/` (after user confirmation)

After decisions are reviewed and approved by the user (approval phrase required), the workflow can generate:
- `docs/specifications/<demand_folder>/04-specifications/` (dev-ready functional spec overview + detailed functional spec (with Mermaid diagrams) + OpenAPI)

## How decisions are produced
- The SME/business owner provides answers directly in the AI review file.
- The skill synthesizes those answers into a draft decisions document (strict gating applies).

## Decisions approval gate
Before generating `04-specifications`, the user MUST review the decisions draft and reply with:
- `I approved this decision`

## Input layout
- Demand folder: `docs/specifications/<demand_folder>/`
- Human demand documents: `docs/specifications/<demand_folder>/01-demand/`

## Follow-up invocation (copy/paste)
```text
@[/olaf-review-human-written-spec]
demand_folder: <demand_folder>
review_mode: followup
previous_review_path: <path-to-previous-ai-review>
```

## Protocol
This skill asks for user approval before writing files into the repository.
