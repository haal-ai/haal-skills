---
name: workflow-phase-5-review-packaging
description: Phase 5 - Package final review and write it to docs/specifications/{demand_folder}/02-ai-review
---

CRITICAL: This phase writes a file. Always ask for user approval before writing.

## Inputs
You MUST have the artifacts from Phases 1-4:
- Intake summary
- Domain model
- API capability mapping
- SME questions table

## Process

### A) Build the review document
You MUST structure the final markdown using template: `templates/review-output-format.md`.

### B) Propose output path (Propose step)
You MUST:
- Compute `timestamp` in `YYYYMMDD-HHmm`
- Propose output file path:
  - `{review_output_dir}/{timestamp}-{output_basename}-review.md`
- Show a short preview (headings + a few key bullets, not the entire file)

### C) Confirm
You MUST ask:
- "Ready to write the review file to the repository? (yes/no)"

### D) Act
Only if user says yes:
- Write the markdown file to the proposed location

### E) Follow-up mode: draft business decisions
If `review_mode=followup` AND strict gating passed:
- Propose a business decisions output path:
  - `{decisions_output_dir}/{timestamp}-{output_basename}-business-decisions.md`
- You MUST structure the decisions document using template:
  - `templates/business-decisions-output-format.md`
- The decisions document MUST:
  - List each question ID with the SME answer (or TBD with owner/date)
  - Translate answers into clear, testable business rules suitable for OpenAPI derivation
  - Record any unresolved items explicitly
- Ask for confirmation before writing the decisions file
- Only if user says yes, write the decisions file

### F) Approval gate (required before specifications generation)
After the decisions file is written:
- You MUST ask the user to review the decisions document.
- You MUST require the user to reply with this exact sentence to approve:
  - `I approved this decision`
- If the user does not provide this exact sentence, you MUST NOT generate `04-specifications`.

### G) Generate specifications (after approval only)
Only after the approval phrase is provided:
- Propose output paths under `{spec_output_dir}`:
  - `{spec_output_dir}/{timestamp}-{output_basename}-functional-spec.md`
  - `{spec_output_dir}/{timestamp}-{output_basename}-functional-spec-detailed.md`
  - `{spec_output_dir}/{timestamp}-{output_basename}-openapi.yaml`
- You MUST structure the detailed functional spec using template:
  - `templates/functional-spec-detailed-output-format.md`
- Show a short preview of each artifact.
- Ask for confirmation before writing the specification files.
- Only if user says yes, write the specification files.

## Output
You WILL return:
- The output file path
- A short summary of what was written

## Error Handling
If the output directory does not exist:
- You MUST propose creating it and ask for confirmation before creating it
