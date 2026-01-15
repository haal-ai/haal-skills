---
name: analyze-db-api-fit
description: Analyze functional spec + OpenAPI against existing database schemas to identify data gaps and integration risks for microservices
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, database, microservices, gap-analysis, data-fit]
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
- **analysis_mode**: initial|followup - Whether this is a first run or a successive run (OPTIONAL - default: initial)
- **previous_analysis_path**: string - Path to a previous data-fit analysis markdown file (OPTIONAL - required if analysis_mode=followup)
- **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
- **spec_dir**: string - Folder containing functional spec + OpenAPI (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
- **functional_spec_path**: string - Path to functional spec overview (OPTIONAL - default: latest `*-functional-spec.md` in `{spec_dir}`)
- **functional_spec_detailed_path**: string - Path to functional spec detailed (OPTIONAL - default: latest `*-functional-spec-detailed.md` in `{spec_dir}`)
- **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
- **db_artifacts_paths**: string[] - Paths to DB schema artifacts (DDL, migrations, ERD, data dictionary) (OPTIONAL)
- **db_context_notes**: string - Notes about DB ownership, source-of-truth, constraints, legacy concerns (OPTIONAL)
- **analysis_output_dir**: string - Folder where analysis markdown will be saved (OPTIONAL - default: `{demand_root}/{demand_folder}/05-data-fit-analysis`)
- **output_basename**: string - Basename for output file (OPTIONAL - default: `demand_folder`)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because the workflow writes files into the repository.

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The specifications folder exists at `{spec_dir}`
- You can list and read the spec inputs at `functional_spec_path`, `functional_spec_detailed_path`, `openapi_path`
- The `analysis_output_dir` path is within `{demand_root}/`

## Process

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters
- List all files under `{spec_dir}`
- If `functional_spec_path`, `functional_spec_detailed_path`, or `openapi_path` are not provided:
  - Select the latest timestamped file for each kind from `{spec_dir}`
  - If no candidate exists, ask the user for the correct path
- Read in full:
  - `functional_spec_path`
  - `functional_spec_detailed_path`
  - `openapi_path`
- If `analysis_mode=followup`, read `previous_analysis_path`
- If `analysis_mode=followup`, extract SME answers from the previous analysis (answer worksheet and/or SME answer column)
- If `analysis_mode=followup`, apply STRICT GATING:
  - If any **High** priority question is unanswered, ambiguous, or missing explicit **TBD + decision owner + target date**, you MUST stop and ask the user to complete the answers before proceeding
- If `db_artifacts_paths` are provided:
  - Validate each path exists
  - Read each artifact in full (or enough to extract table/column/index info)
<!-- </validation_phase> -->

<!-- <execution_phase> -->
### 2) Execution Phase
You WILL produce a single analysis report following template: `templates/db-api-fit-output-format.md`.

You WILL:

#### 2.1 Extract a data requirements inventory
From the functional specs and OpenAPI:
- Enumerate domain concepts (entities, value objects, enums)
- For each endpoint and use-case:
  - Required request fields (validation needs)
  - Required response fields (data you must be able to serve)
  - Query needs (filter/sort/pagination)
  - Identity and authorization data needs
  - Derived/aggregated data needs

#### 2.2 Propose candidate microservice boundaries (data ownership)
You WILL:
- Identify candidate bounded contexts/service candidates
- For each candidate service:
  - Data it should own (write authority)
  - Data it needs to read (reference/replicated)
  - Cross-boundary dependencies and likely integration patterns

#### 2.3 Request DB artifacts (if missing)
If `db_artifacts_paths` are missing or incomplete:
- You MUST include a structured request list using: `/kb/db-artifacts-request-checklist.md`
- You MUST produce a questions section using: `templates/questions-table-format.md`

#### 2.4 Perform DB ↔ API mapping (if DB artifacts are provided)
If `db_artifacts_paths` are provided, you WILL:
- Map each required data element to:
  - table/view + column(s)
  - join path / relationship assumptions
  - constraints/validation support (unique, FK, nullability)
  - type compatibility and encoding (enum strategy, dates, identifiers)
- Classify each requirement:
  - Covered
  - Partially covered (needs derivation/joins)
  - Missing (gap)
  - Ambiguous (needs SME decision)
- Identify performance risks:
  - required filters/sorts without indexes
  - expensive join paths
  - high-cardinality access patterns

#### 2.5 Produce gap analysis and decisions
You WILL:
- List gaps (missing columns/tables/reference data)
- List blockers for implementing business logic without DB changes
- List decisions needed (source-of-truth, ownership, replication strategy, migration approach)
- Provide a minimal next-step plan (what to ask for, what to confirm)

<!-- </execution_phase> -->

<!-- <output_phase> -->
### 3) Output Phase
You WILL:
- Propose a single markdown report saved under `{analysis_output_dir}`
- Output filename format:
  - `{timestamp}-{output_basename}-data-fit-analysis.md`

You MUST ask for confirmation before writing any files.
<!-- </output_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] The required spec inputs (functional spec + OpenAPI) were read and analyzed
- [ ] A data requirements inventory was produced
- [ ] Candidate service boundaries and data ownership assumptions were proposed
- [ ] If DB artifacts were provided: a DB-to-requirements mapping was produced with gaps
- [ ] If DB artifacts were missing: a structured request list and SME questions were produced
- [ ] You proposed the output file path and received user confirmation
- [ ] The analysis markdown file has been written to `analysis_output_dir`

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Spec directory not found**: Ask the user to confirm where `04-specifications` lives
- **Spec inputs missing**: Ask the user for explicit `functional_spec_path` / `openapi_path`
- **DB artifacts missing**: Produce the artifact request list and stop short of claiming DB coverage
- **DB artifact too large/partial**: Document limitations and ask for missing pieces (tables, constraints, indexes)
- **Conflicting sources of truth**: Document conflict and ask the user to name the authoritative system


