# Generate DDL And Seed

## Purpose

This skill helps API producers in greenfield scenarios where there is no existing database.
It generates:
- a relational schema (DDL)
- deterministic seed/init data

Inputs are taken from the latest:
- OpenAPI contract in `04-specifications/`
- DB↔API fit analysis in `05-data-fit-analysis/`

## Defaults

- Target DB: PostgreSQL
- Output folder: `docs/specifications/{demand_folder}/07-db-artifacts/`

## What you get

- `{timestamp}-{demand_folder}-db-schema.sql`
- `{timestamp}-{demand_folder}-db-seed.sql`

## Notes

This skill uses **Propose-Confirm-Act** and will always ask for approval before writing any files.
