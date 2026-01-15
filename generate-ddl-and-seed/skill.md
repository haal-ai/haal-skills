---
name: generate-ddl-and-seed
description: Generate a new database schema (DDL) and initialization data from the latest OpenAPI contract and DB↔API fit analysis when no DB exists yet
license: Apache-2.0
metadata:
  olaf_tags: [database, ddl, seed-data, postgres, h2, mysql, openapi, api]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **demand_folder**: string - Demand folder under `docs/specifications/` (example: `pet-clinic-01`) (REQUIRED)
- **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
- **spec_dir**: string - Folder containing OpenAPI (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
- **data_fit_dir**: string - Folder containing DB↔API fit analyses (OPTIONAL - default: `{demand_root}/{demand_folder}/05-data-fit-analysis`)
- **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
- **data_fit_analysis_path**: string - Path to latest DB↔API fit analysis markdown (OPTIONAL - default: latest `*-data-fit-analysis*.md` in `{data_fit_dir}`)
- **db_type**: postgres|h2|mysql - Target database engine (OPTIONAL - default: postgres)
- **output_dir**: string - Output folder for DB artifacts (OPTIONAL - default: `{demand_root}/{demand_folder}/07-db-artifacts`)
- **schema_basename**: string - Base name for output files (OPTIONAL - default: `{demand_folder}`)
- **id_strategy**: uuid|identity - Primary key strategy (OPTIONAL - default: uuid)
- **seed_profile**: minimal|demo - Seed data volume and breadth (OPTIONAL - default: minimal)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because the workflow writes files into the repository.

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The `spec_dir` and `data_fit_dir` exist
- The selected `openapi_path` exists
- The selected `data_fit_analysis_path` exists
- `output_dir` is within `{demand_root}/{demand_folder}`

## Process

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters
- List files under `{spec_dir}` and `{data_fit_dir}`
- Select the latest timestamped `openapi_path` and `data_fit_analysis_path` if not provided
- Read in full:
  - `openapi_path`
  - `data_fit_analysis_path`

You MUST confirm this is a greenfield database scenario:
- If the user provides DB artifacts (DDL/migrations/ERD) or the analysis indicates an existing DB baseline, you MUST stop and ask the user whether to use `analyze-db-api-fit` instead.
<!-- </validation_phase> -->

<!-- <planning_phase> -->
### 2) Planning Phase
You WILL propose (in chat) a schema plan:
- Tables and responsibilities per domain concept
- Primary keys, foreign keys, and join strategy
- Constraints (unique, not null, check constraints where relevant)
- Index strategy based on API query patterns
- Enum strategy (lookup tables vs inline enum strings)
- Timestamp/audit fields (created_at, updated_at) if useful

You MUST propose the exact output file paths:
- `{output_dir}/{timestamp}-{schema_basename}-db-schema.sql`
- `{output_dir}/{timestamp}-{schema_basename}-db-seed.sql`

You MUST ask the user to approve the plan before writing any files.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3) Execution Phase (Only after approval)
You WILL:

#### 3.1 Generate DDL
You WILL generate one SQL file containing:
- Schema creation for the chosen `db_type`
- Ordered creation to satisfy FK dependencies

You MUST ensure portability rules per `db_type`:
- postgres: prefer `uuid` primary keys when `id_strategy=uuid`
- mysql: avoid postgres-specific types; ensure compatible defaults
- h2: keep DDL compatible with H2 dialect (avoid advanced postgres-only features)

#### 3.2 Generate seed/init data
You WILL generate deterministic seed data aligned to API flows:
- Minimal seed must satisfy referential integrity
- Demo seed may include richer examples for UI testing

You MUST ensure seed data does not include real/production data.
<!-- </execution_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] Latest OpenAPI and latest DB↔API fit analysis were selected and read
- [ ] You proposed a schema + seed plan and the user approved it
- [ ] DDL script exists at `{output_dir}/{timestamp}-{schema_basename}-db-schema.sql`
- [ ] Seed script exists at `{output_dir}/{timestamp}-{schema_basename}-db-seed.sql`

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **OpenAPI missing**: Ask the user for explicit `openapi_path`
- **DB-fit analysis missing**: Ask the user for explicit `data_fit_analysis_path`
- **Not greenfield**: Stop and redirect to `analyze-db-api-fit`
- **Ambiguous domain model**: Ask targeted questions and do not invent critical business rules


