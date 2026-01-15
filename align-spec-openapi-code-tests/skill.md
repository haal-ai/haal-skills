---
name: align-spec-openapi-code-tests
description: Detect drift and align functional spec, OpenAPI, implementation code, and tests with least-impact recommendations
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, drift, alignment, testing, bruno, quarkus, workflow]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

## Input Parameters
You MUST request these parameters if not provided by the user:
- **demand_folder**: string - Demand folder under `docs/specifications/` (example: `pet-clinic-01`) (REQUIRED)
- **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
- **spec_dir**: string - Folder containing functional spec + OpenAPI (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
- **data_fit_dir**: string - Folder containing DB↔API fit analyses (OPTIONAL - default: `{demand_root}/{demand_folder}/05-data-fit-analysis`)
- **functional_spec_path**: string - Path to functional spec markdown (OPTIONAL - default: latest `*-functional-spec.md` in `{spec_dir}`)
- **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
- **api_code_root**: string - Root folder of the API implementation (OPTIONAL - default: `apps/{demand_folder}-api-quarkus`)
- **sdk_root**: string - Root folder of SDK implementation (OPTIONAL - default: `sdks/{demand_folder}-sdk-ts`)
- **bruno_root_dir**: string - Root folder where Bruno collections live (OPTIONAL - default: `tests/bruno`)
- **output_dir**: string - Output folder for drift analysis (OPTIONAL - default: `{demand_root}/{demand_folder}/08-drift-analysis`)
- **alignment_mode**: analyze-only|analyze-and-align - Whether to apply alignment after approval (OPTIONAL - default: analyze-and-align)
- **implementation_pending**: boolean - If true, implementation may intentionally lag specs; user must choose source of truth (OPTIONAL - default: false)
- **source_of_truth**: code|openapi|functional_spec - What must be aligned to (OPTIONAL - default: code)

If `implementation_pending=true`, you MUST stop and ask the user to explicitly choose `source_of_truth`.

## User Interaction Protocol
You MUST follow **Propose-Confirm-Act** because this workflow writes files into the repository.

## Constraints (Hard Rules)
- You MUST NOT modify database/DDL artifacts (including anything under `{demand_root}/{demand_folder}/07-db-artifacts`, SQL migrations, or schema DDL files).
- If alignment would require DB schema changes, you MUST stop and ask the user to handle DB changes separately.

## Use Templates and Knowledge Base
- You MUST use the template at `templates/drift-alignment-report-template.md`.
- If you need technology-specific guidance, consult the local KB under `.olaf/data/kb/` before fetching anything external.

## Process

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters
- Confirm the demand folder exists at `{demand_root}/{demand_folder}`
- List files under `{spec_dir}` and `{data_fit_dir}`
- Select latest timestamped `functional_spec_path`, `openapi_path`, and `data_fit_analysis_path` (latest `*-data-fit-analysis*.md` in `{data_fit_dir}`)
- Confirm `output_dir` is within `{demand_root}/{demand_folder}`
- Read in full:
  - `functional_spec_path`
  - `openapi_path`
  - `data_fit_analysis_path` (read-only context)
<!-- </validation_phase> -->

<!-- <planning_phase> -->
### 2) Planning Phase
You WILL produce a drift-and-alignment plan (in chat) that includes:
- The explicit `source_of_truth`
- Drift categories you will evaluate:
  - Functional spec ↔ OpenAPI
  - OpenAPI ↔ code (API surface, status codes, payloads)
  - OpenAPI ↔ tests (Bruno coverage + assertions)
  - Tests ↔ code (test assumptions vs observed behavior)
- A least-impact recommendation string in this exact format:
  - `RECOMMENDATION: <TOKEN> (<1 sentence rationale>)`
- Exact output file paths:
  - `{output_dir}/{timestamp}-{demand_folder}-drift-report.md`
  - `{output_dir}/{timestamp}-{demand_folder}-alignment-plan.md`
- A proposed change set grouped by artifact:
  - Functional spec changes (if any)
  - OpenAPI changes (if any)
  - Code changes (if any)
  - Bruno test changes (if any)

You MUST ask the user to approve the plan before writing any files.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3) Execution Phase (Only after approval)

#### 3.1 Generate drift report
You WILL produce `{output_dir}/{timestamp}-{demand_folder}-drift-report.md` using `templates/drift-alignment-report-template.md`.
You MUST include:
- The `RECOMMENDATION: ...` line near the top
- Evidence links (file paths; add line references when available)
- A table summarizing mismatches and their impact (high/medium/low)

#### 3.2 Generate alignment plan
You WILL produce `{output_dir}/{timestamp}-{demand_folder}-alignment-plan.md` that:
- Lists concrete edits per artifact
- Orders changes to minimize risk
- Includes a rollback plan

#### 3.3 Apply alignment (only if `alignment_mode=analyze-and-align`)
You WILL:
- Re-state the planned edits and ask the user for final confirmation
- Apply the edits to align all artifacts to the chosen `source_of_truth`
- Ensure tests reflect the chosen truth:
  - If code is truth: adjust OpenAPI/spec/tests to match code
  - If OpenAPI/spec is truth: adjust code/tests to match

You MUST NOT modify DB/DDL artifacts.
<!-- </execution_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] Drift report and alignment plan were written to `{output_dir}`
- [ ] Recommendation string is present and actionable
- [ ] If `alignment_mode=analyze-and-align`, artifacts are aligned to `source_of_truth`
- [ ] No DB/DDL artifacts were modified

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Functional spec missing**: Ask the user for explicit `functional_spec_path`
- **OpenAPI missing**: Ask the user for explicit `openapi_path`
- **Implementation pending ambiguity**: Stop and ask user to pick `source_of_truth`
- **DB changes required**: Stop and ask user to handle DB separately
