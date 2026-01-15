---
name: review-producer-api-as-consumer
description: Review functional spec + OpenAPI from a consumer perspective and produce questions for producers plus early dev priorities
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, consumer, spec-review, questions, integration]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **demand_folder**: string - Demand folder under `docs/specifications/` (example: `pet-clinic-01`) (REQUIRED)
- **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
- **spec_dir**: string - Folder containing functional spec + OpenAPI (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
- **functional_spec_path**: string - Path to functional specification markdown (OPTIONAL - default: latest `*.md` under `{spec_dir}` excluding OpenAPI)
- **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
- **consumer_context**: string - Target consumer context (channels, platforms, auth model, envs, constraints) (OPTIONAL)
- **output_dir**: string - Where to write the consumer review (OPTIONAL - default: `{demand_root}/{demand_folder}/09-consumer-review`)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because the workflow writes files into the repository.

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The `spec_dir` exists and contains expected artifacts
- The selected `openapi_path` exists
- The selected `functional_spec_path` exists
- `output_dir` is within `{demand_root}/{demand_folder}`

## Process

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters
- List files under `{spec_dir}`
- Select the latest timestamped `openapi_path` if not provided
- Select `functional_spec_path` if not provided
- Read in full:
  - `functional_spec_path`
  - `openapi_path`
<!-- </validation_phase> -->

<!-- <planning_phase> -->
### 2) Planning Phase
You WILL propose (in chat) a review plan:
- What consumer implementation you assume (web app, mobile, server-to-server)
- Priority journeys/use-cases from the spec
- Top contract risks and unknowns to resolve early
- The exact output path:
  - `{output_dir}/{timestamp}-{demand_folder}-consumer-review.md`

You MUST ask the user to approve the plan before writing any files.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3) Execution Phase (Only after approval)
You WILL write a consumer review report using the provided template.

You MUST include:
- Questions for producers (contract clarifications)
- Consumer integration assumptions (auth, pagination, idempotency, error model)
- Gaps/risks in OpenAPI for client generation (schema quality, examples)
- Early development priorities (what to implement/prototype first)
<!-- </execution_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] Latest functional spec + latest OpenAPI were selected and read
- [ ] You proposed a review plan and the user approved it
- [ ] Consumer review output exists at `{output_dir}/{timestamp}-{demand_folder}-consumer-review.md`

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Spec directory not found**: Ask the user to provide the correct `spec_dir` (folder that contains BOTH the functional spec markdown and the OpenAPI file).
  - Default expected location is: `{demand_root}/{demand_folder}/04-specifications`
  - If there are multiple candidate folders, ask them to provide explicit paths for BOTH:
    - `functional_spec_path` (the markdown spec you should review)
    - `openapi_path` (the OpenAPI contract, typically `*.yaml` / `*.yml` and often named like `*-openapi.yaml`)
- **OpenAPI missing**: Ask the user for explicit `openapi_path`
- **Functional spec missing**: Ask the user for explicit `functional_spec_path`

