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

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response.
1. **demand_folder**: string - Demand folder under `docs/specifications/` (example: `pet-clinic-01`) (REQUIRED)
2. **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
3. **spec_dir**: string - Folder containing functional spec + OpenAPI (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
4. **data_fit_dir**: string - Folder containing DB↔API fit analyses (OPTIONAL - default: `{demand_root}/{demand_folder}/05-data-fit-analysis`)
5. **functional_spec_path**: string - Path to functional spec markdown (OPTIONAL - default: latest `*-functional-spec.md` in `{spec_dir}`)
6. **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
7. **api_code_root**: string - Root folder of the API implementation (OPTIONAL - default: `apps/{demand_folder}-api-quarkus`)
8. **sdk_root**: string - Root folder of SDK implementation (OPTIONAL - default: `sdks/{demand_folder}-sdk-ts`)
9. **bruno_root_dir**: string - Root folder where Bruno collections live (OPTIONAL - default: `tests/bruno`)
10. **output_dir**: string - Output folder for drift analysis (OPTIONAL - default: `{demand_root}/{demand_folder}/08-drift-analysis`)
11. **alignment_mode**: analyze-only|analyze-and-align - Whether to apply alignment after approval (OPTIONAL - default: analyze-and-align)
12. **implementation_pending**: boolean - If true, implementation may intentionally lag specs; user must choose source of truth (OPTIONAL - default: false)
13. **source_of_truth**: code|openapi|functional_spec - What must be aligned to (OPTIONAL - default: code)

If `implementation_pending=true`, you MUST stop and ask the user to explicitly choose `source_of_truth`.

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before creating or modifying files
- Present options as numbered lists for easy selection
- Use **Propose-Confirm-Act** because this workflow writes files into the repository
- Provide clear progress updates at each major step

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
- [ ] User approved all changes before application
- [ ] All outputs follow template structure

## Required Actions
1. Validate all required input parameters and prerequisites
2. Generate drift report and alignment plan following templates
3. Apply alignment only after user confirmation (if mode=analyze-and-align)
4. Provide user communication and confirmations
5. Ensure no DB/DDL artifacts are modified

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Functional spec missing**: Ask the user for explicit `functional_spec_path`
- **OpenAPI missing**: Ask the user for explicit `openapi_path`
- **Implementation pending ambiguity**: Stop and ask user to pick `source_of_truth`
- **DB changes required**: Stop and ask user to handle DB separately

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Validation phase completed
- Drift analysis in progress
- Alignment plan generated
- Changes applied (if applicable)

### Completion Summary
- Files created with locations
- Drift categories identified
- Alignment actions taken
- Any issues encountered and resolutions

### Next Steps
- Review drift report and alignment plan
- Verify aligned artifacts
- Run tests to validate changes
- Update documentation if needed

⚠️ **Critical Requirements**
- MANDATORY: Ask for user approval before modifying any files
- NEVER modify DB/DDL artifacts under any circumstances
- ALWAYS use templates for report generation
- ALWAYS provide evidence with file:line references
- ALWAYS stop if DB schema changes are required
