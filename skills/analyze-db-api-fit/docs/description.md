# Analyze DB API Fit

## What this skill does
This skill analyzes a functional specification and OpenAPI contract against existing database schema artifacts in order to:
- Extract the data requirements needed to implement the API business logic
- Propose candidate microservice boundaries and data ownership assumptions
- Map required API/domain data to existing DB tables/columns when DB artifacts are provided
- Identify data gaps, constraints mismatches, and decisions required to proceed

## When to use
Use this skill when you have:
- A detailed functional spec and an OpenAPI definition
- An existing database (or multiple databases) that may already contain the data
- A need to determine whether the API can be implemented without changing the database

## Outputs
- A markdown data-fit analysis written under:
  - `docs/specifications/<demand_folder>/05-data-fit-analysis/` (after user confirmation)

## DB artifacts expected
The skill can run in two modes:
- **Without DB artifacts**: produces a data requirements inventory plus a structured request list for DB schemas and SME questions.
- **With DB artifacts**: produces a DB ↔ requirements mapping and a gap/risk assessment.

## Notes

This skill will always ask for approval before writing any files.
