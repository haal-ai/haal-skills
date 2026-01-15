---
name: plan-db-api-remediation
description: Translate DB↔API fit mismatches into delivery impact decisions and a phased remediation plan
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, database, delivery, migration, remediation, impact]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>.

## Time Retrieval\nGet current timestamp using time tools, fallback to shell command if needed:
- Get current timestamp using time tools, fallback to shell command if needed-HHmm"`

## Input Parameters
You MUST request these parameters if not provided by the user:
- **demand_folder**: string - Demand folder under `docs/specifications/` (example: `pet-clinic-01`) (REQUIRED)
- **plan_mode**: initial|followup - Whether this is a first run or a successive run (OPTIONAL - default: initial)
- **previous_data_fit_analysis_path**: string - Path to a DB↔API fit analysis markdown file (REQUIRED)
- **previous_plan_path**: string - Path to a previous delivery impact plan markdown file (OPTIONAL - required if plan_mode=followup)
- **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
- **spec_dir**: string - Folder containing functional spec + OpenAPI (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
- **functional_spec_path**: string - Path to functional spec overview (OPTIONAL - default: latest `*-functional-spec.md` in `{spec_dir}`)
- **functional_spec_detailed_path**: string - Path to functional spec detailed (OPTIONAL - default: latest `*-functional-spec-detailed.md` in `{spec_dir}`)
- **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
- **delivery_target**: string - Delivery target constraint (OPTIONAL - example: `MVP in 6 weeks`)
- **existing_user_impact_tolerance**: low|medium|high - Tolerance for breaking/behavior changes (OPTIONAL)
- **delivery_output_dir**: string - Folder where delivery impact markdown will be saved (OPTIONAL - default: `{demand_root}/{demand_folder}/06-delivery-impact`)
- **output_basename**: string - Basename for output file (OPTIONAL - default: `demand_folder`)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because the workflow writes files into the repository.

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The specifications folder exists at `{spec_dir}`
- You can list and read the spec inputs at `functional_spec_path`, `functional_spec_detailed_path`, `openapi_path`
- The `delivery_output_dir` path is within `{demand_root}/`
- `previous_data_fit_analysis_path` exists and is readable

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
- Read in full:
  - `previous_data_fit_analysis_path`
- If `plan_mode=followup`:
  - Read `previous_plan_path`
  - Extract SME/PO answers from the previous plan (answer worksheet and/or SME answer column)
  - Apply STRICT GATING:
    - If any **High** priority question is unanswered, ambiguous, or missing explicit **TBD + decision owner + target date**, you MUST stop and ask the user to complete the answers before proceeding
<!-- </validation_phase> -->

<!-- <execution_phase> -->
### 2) Execution Phase
You WILL produce a single delivery impact report following template: `templates/delivery-impact-output-format.md`.

You WILL:

#### 2.1 Translate mismatches into delivery difficulties
Using:
- the functional specs
- the OpenAPI contract
- the DB↔API fit analysis

You MUST produce a prioritized list of:
- The most difficult mismatches
- Why they are difficult (schema, migration, time representation, auditability, indexing/performance, identifier strategy)
- Expected delivery impact (effort/risk)
- Expected impact on existing users (data correctness, compatibility, downtime, behavior changes)

#### 2.2 Identify “must-have” vs “can abandon/postpone” candidates
You MUST propose:
- A short list of requirements that are likely non-negotiable
- A short list of requirements that are likely candidates to postpone or simplify
- SME/PO questions that explicitly force a decision

Focus on decisions that materially affect:
- time to deliver
- impact on existing users
- scope (drop/postpone)

#### 2.3 Produce a phased remediation plan (only if scope is not reduced)
If must-have scope remains intact (no major abandonment/postponement):
- Provide a phased approach that includes:
  - schema changes
  - backfill/data insertion strategy
  - migration/rollout strategy (compatibility and rollback)
  - operational considerations (downtime, data validation, monitoring)

You MUST use reference: `/kb/remediation-plan-checklist.md`.
<!-- </execution_phase> -->

<!-- <output_phase> -->
### 3) Output Phase
You WILL:
- Propose a single markdown report saved under `{delivery_output_dir}`
- Output filename format:
  - `{timestamp}-{output_basename}-delivery-impact.md`

You MUST ask for confirmation before writing any files.
<!-- </output_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] The latest spec inputs (functional spec + OpenAPI) were read and analyzed
- [ ] The DB↔API fit analysis was read and used as an evidence source
- [ ] Delivery difficulties and user-impact implications were summarized
- [ ] Must-have vs can-drop candidates were proposed with decision questions
- [ ] If scope not reduced: a phased remediation plan was produced
- [ ] You proposed the output file path and received user confirmation
- [ ] The delivery impact markdown file has been written to `delivery_output_dir`

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Spec directory not found**: Ask the user to confirm where `04-specifications` lives
- **Spec inputs missing**: Ask the user for explicit `functional_spec_path` / `openapi_path`
- **Data-fit analysis path missing**: Ask the user for `previous_data_fit_analysis_path`
- **Follow-up plan missing prior plan**: Ask for `previous_plan_path` or switch to `plan_mode=initial`
- **Output directory missing**: Propose creating the directory and request confirmation before creating it


