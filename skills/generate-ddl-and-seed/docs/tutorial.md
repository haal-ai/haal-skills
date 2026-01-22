# Tutorial: Generate DDL And Seed

## 1) Provide the demand

Invoke:
- `olaf generate-ddl-and-seed`

When asked, provide:
- `demand_folder` (example: `pet-clinic-01`)

## 2) Approve schema + seed plan

The skill will:
- Locate the latest OpenAPI and DB↔API fit analysis
- Propose a schema plan and the output file paths

You MUST approve before files are written.

## 3) Use the outputs

The result is two SQL files under:
- `docs/specifications/{demand_folder}/07-db-artifacts/`

You can apply the DDL then load the seed data in a local database.
