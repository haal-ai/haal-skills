# Tutorial: Analyze DB ↔ API Fit

## 1) Prerequisites
You should have a demand folder under `docs/specifications/` containing:
- `04-specifications/` (functional spec + OpenAPI)

## 2) Run the skill (first pass)
Invoke the skill and provide:
- `demand_folder` (example: `pet-clinic-01`)

The skill will:
- Extract data requirements from the functional specs + OpenAPI
- Produce a DB artifacts request list and SME questions
- Propose an output file path under `docs/specifications/<demand_folder>/05-data-fit-analysis/`
- Ask for confirmation before writing

## 3) Provide DB artifacts
Gather one or more of:
- DDL (schema export)
- Migrations (Flyway/Liquibase/EF/Alembic)
- ERD
- Data dictionary

Provide their paths as `db_artifacts_paths` on the next run.

## 4) Run the skill (follow-up mapping)
```text
@[/olaf-analyze-db-api-fit]
demand_folder: <demand_folder>
analysis_mode: followup
previous_analysis_path: <path-to-previous-data-fit-analysis>
db_artifacts_paths:
  - <path-to-ddl-or-migrations>
  - <path-to-erd-or-data-dictionary>
```

The follow-up run will:
- Map required API/domain data to DB tables/columns
- Identify missing fields and other blockers
- Produce an updated report in `05-data-fit-analysis/`
