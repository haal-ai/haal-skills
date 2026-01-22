# Tutorial: Review a human specification for API design readiness

## 1) Provide the input specification
- Create (or pick) a demand folder under `docs/specifications/` (example: `pet-clinic-01/`)
- Place the demand documents under: `docs/specifications/<demand_folder>/01-demand/`

## 2) Run the skill
Invoke the skill and provide:
- `demand_folder` (example: `pet-clinic-01`)
- Optionally `review_mode=followup` and `previous_review_path`

## 3) Review and confirm file writing
The skill will:
- Produce the review content
- Propose an output file path under `docs/specifications/<demand_folder>/02-ai-review/`
- Ask for confirmation before writing

## 4) SME answers (edit the AI review directly)
- The SME SHOULD edit the generated AI review file directly.
- Fill the SME answer worksheet (and/or SME answer column) for each question.

## 5) Follow-up review (generates business decisions + strict gating)
After the SME answers are filled, run a follow-up review by copy/pasting:

```text
@[/olaf-review-human-written-spec]
demand_folder: <demand_folder>
review_mode: followup
previous_review_path: <path-to-previous-ai-review>
```

In follow-up mode the skill will:
- Enforce strict gating on High-priority questions
- Draft business decisions under `docs/specifications/<demand_folder>/03-business-decisions/`

After the decisions draft is written:
- Review it
- To approve and allow spec generation, reply with this exact sentence:
  - `I approved this decision`

Only after approval, the workflow will generate `docs/specifications/<demand_folder>/04-specifications/`:
- A dev-ready functional specification (overview)
- A dev-ready functional specification (detailed, including Mermaid diagrams)
- An OpenAPI specification
