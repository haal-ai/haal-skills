---
name: review-human-written-spec
description: Multi-phase workflow to challenge a human-written specification and produce SME questions needed for API design
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, requirements, spec-review, questionnaire]
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
- **review_mode**: initial|followup - Whether this is the first review or a successive review (OPTIONAL - default: initial)
- **previous_review_path**: string - Path to a previous AI review file (OPTIONAL - required if review_mode=followup)
- **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
- **demand_input_dir**: string - Folder containing human demand documents (OPTIONAL - default: `{demand_root}/{demand_folder}/01-demand`)
- **review_output_dir**: string - Folder where review markdown will be saved (OPTIONAL - default: `{demand_root}/{demand_folder}/02-ai-review`)
- **decisions_output_dir**: string - Folder where business decisions will be saved (OPTIONAL - default: `{demand_root}/{demand_folder}/03-business-decisions`)
- **spec_output_dir**: string - Folder where dev-ready specifications will be saved (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
- **output_basename**: string - Basename for output file (OPTIONAL - default: `demand_folder`)
- **api_intent**: string - Intended API consumer/use-case (OPTIONAL - default: "Design an API that serves the expressed business needs")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because the workflow writes files into the repository.

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The demand input folder exists at `{demand_input_dir}`
- You can list and read all files inside `{demand_input_dir}`
- The `review_output_dir` path is within `{demand_root}/`

## Process

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters
- List all files under `{demand_input_dir}`
- Read all demand input documents under `{demand_input_dir}` (all files) in full
- If `review_mode=followup`, read the previous review at `previous_review_path`
- If `review_mode=followup`, extract SME answers from the previous review (answer worksheet and/or SME answer column)
- If `review_mode=followup`, apply STRICT GATING:
  - If any **High** priority question is unanswered, ambiguous, or missing explicit **TBD + decision owner + target date**, you MUST stop and ask the user to complete the answers before proceeding
- Confirm the output path you plan to write to before writing any files
<!-- </validation_phase> -->

<!-- <execution_phase> -->
### 2) Execution Phase (Multi-Phase Review)
You WILL execute the phases in order and carry forward artifacts between phases:

1. Execute: `/helpers/workflow-phase-1-intake.md`
2. Execute: `/helpers/workflow-phase-2-domain-model.md`
3. Execute: `/helpers/workflow-phase-3-api-capabilities.md`
4. Execute: `/helpers/workflow-phase-4-questions-for-sme.md`
5. Execute: `/helpers/workflow-phase-5-review-packaging.md`

During the process:
- You MUST use `/kb/api-design-question-catalog.md` to ensure coverage of common API design blockers.
- You MUST structure the final review using template: `templates/review-output-format.md`
- You MUST format the questions using template: `templates/questions-table-format.md`
<!-- </execution_phase> -->

<!-- <output_phase> -->
### 3) Output Phase
You WILL produce:
- A single markdown review document saved under `review_output_dir`
- Output filename format:
  - `{timestamp}-{output_basename}-review.md`

If `review_mode=followup`:
- You MUST also produce a business decision draft saved under `decisions_output_dir`
- Decisions filename format:
  - `{timestamp}-{output_basename}-business-decisions.md`

After the business decisions draft is written:
- You MUST require explicit user approval before generating specifications.
- The user MUST reply with this exact sentence:
  - `I approved this decision`

Only after approval:
- You MUST produce dev-ready specifications under `spec_output_dir`:
  - `{timestamp}-{output_basename}-functional-spec.md`
  - `{timestamp}-{output_basename}-functional-spec-detailed.md`
  - `{timestamp}-{output_basename}-openapi.yaml`

The review MUST include:
- Key findings
- Assumptions you inferred (explicitly labeled as assumptions)
- Missing decisions required for API design
- SME question set with "why it matters" and proposed options
- A small "API design implications" section mapping questions to likely API areas
<!-- </output_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] You have extracted requirements, rules, actors, and processes from the demand documents
- [ ] You have identified ambiguities and missing decisions that block API design
- [ ] You have produced SME questions with rationale and options
- [ ] You have proposed the output file path and received user confirmation
- [ ] The review markdown file has been written to `review_output_dir`
- [ ] If `review_mode=followup`, strict gating has passed and the business decisions draft has been written to `decisions_output_dir`
- [ ] If decisions were approved, the specifications were written to `spec_output_dir` (overview functional spec, detailed functional spec, OpenAPI)

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Demand input folder not found**: Ask the user to create `{demand_root}/{demand_folder}/01-demand` and place the documents there
- **Demand content too vague**: Still produce questions; mark items as "cannot be determined from the provided demand documents"
- **Follow-up review missing prior review**: Ask for `previous_review_path` or switch to `review_mode=initial`
- **Output directory missing**: Propose creating the directory and request confirmation before doing so


