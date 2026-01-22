# Tutorial: Plan DB↔API Remediation

## 1) Prerequisites
You should have:
- `docs/specifications/<demand_folder>/04-specifications/` (functional spec + OpenAPI)
- `docs/specifications/<demand_folder>/05-data-fit-analysis/` (a DB↔API fit report)

## 2) Run the skill (first pass)
```text
@[/olaf-plan-db-api-remediation]
demand_folder: <demand_folder>
plan_mode: initial
previous_data_fit_analysis_path: <path-to-data-fit-analysis>
```

The skill will:
- Summarize mismatches in delivery/user-impact terms
- Ask SME/PO questions about must-have vs can-drop
- Draft a phased remediation plan if scope is not reduced
- Propose an output file under `docs/specifications/<demand_folder>/06-delivery-impact/`

## 3) Run follow-up (after answers)
```text
@[/olaf-plan-db-api-remediation]
demand_folder: <demand_folder>
plan_mode: followup
previous_data_fit_analysis_path: <path-to-data-fit-analysis>
previous_plan_path: <path-to-previous-delivery-impact-plan>
```
