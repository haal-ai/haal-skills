---
name: scaffold-api-from-spec
description: Incrementally scaffold a Quarkus API, TypeScript SDK, and Bruno CLI tests from the latest functional spec, OpenAPI contract, and DB↔API fit analysis
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, quarkus, typescript, sdk, bruno, testing, scaffolding]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user:
- **demand_folder**: string - Demand folder under `docs/specifications/` (example: `pet-clinic-01`) (REQUIRED)
- **demand_root**: string - Root folder for demands (OPTIONAL - default: `docs/specifications`)
- **spec_dir**: string - Folder containing functional spec + OpenAPI (OPTIONAL - default: `{demand_root}/{demand_folder}/04-specifications`)
- **data_fit_dir**: string - Folder containing DB↔API fit analyses (OPTIONAL - default: `{demand_root}/{demand_folder}/05-data-fit-analysis`)
- **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
- **data_fit_analysis_path**: string - Path to latest DB↔API fit analysis markdown (OPTIONAL - default: latest `*-data-fit-analysis*.md` in `{data_fit_dir}`)
- **api_output_dir**: string - Where to scaffold the Quarkus API project (OPTIONAL - default: `apps/{demand_folder}-api-quarkus`)
- **sdk_output_dir**: string - Where to scaffold the TypeScript SDK project (OPTIONAL - default: `sdks/{demand_folder}-sdk-ts`)
- **bruno_root_dir**: string - Where to place Bruno collections (OPTIONAL - default: `tests/bruno`)
- **github_actions_workflow_path**: string - Path to the GitHub Actions workflow for Bruno tests (OPTIONAL - default: `.github/workflows/api-tests.yml`)
- **implementation_mode**: plan-only|scaffold-only|scaffold-and-implement - How far to go (OPTIONAL - default: scaffold-and-implement)
- **increment_strategy**: health-plus-one|resource-first - Implementation slicing strategy (OPTIONAL - default: health-plus-one)

## User Interaction
- Always ask for user approval before writing or modifying files

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The `spec_dir` and `data_fit_dir` exist and contain expected artifacts
- The selected `openapi_path` exists
- The selected `data_fit_analysis_path` exists
- All output directories are within the repository

## Process

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters
- List all files under `{spec_dir}` and `{data_fit_dir}`
- Select the latest timestamped `openapi_path` and `data_fit_analysis_path` if not provided
- Read in full:
  - `openapi_path`
  - `data_fit_analysis_path`
- Apply strict gating:
  - If the selected DB↔API fit analysis contains unresolved **High** priority SME questions (unanswered, ambiguous, or missing explicit decision owner + target date), you MUST stop and ask the user to resolve them before any code generation.
<!-- </validation_phase> -->

<!-- <planning_phase> -->
### 2) Planning Phase
You WILL produce an incremental task plan (in chat) that includes:
- Project scaffolding tasks (Quarkus server, TypeScript SDK, Bruno tests, GitHub Action)
- First increment scope:
  - Health endpoint + 1 business endpoint implemented end-to-end
  - Bruno happy-path + negative test(s)
- Clear acceptance criteria:
  - `bru run --env local` passes
  - GitHub Actions run passes with HTML and/or JUnit report artifacts

You MUST ask the user to approve the plan before writing any files.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3) Execution Phase (Only after approval)
You WILL:

#### 3.1 Scaffold Quarkus server
You WILL scaffold a Quarkus project under `api_output_dir` and wire server stubs to the OpenAPI contract.

#### 3.2 Scaffold TypeScript SDK
You WILL generate a TypeScript SDK under `sdk_output_dir` from the OpenAPI contract.

#### 3.3 Create Bruno tests (CLI-first)
You WILL create a Bruno project under `bruno_root_dir`:
- `bruno.json`
- `collections/` organized by resource/use-case
- `environments/local.bru` and `environments/ci.bru`

You WILL ensure tests are runnable via Bruno CLI:
- Install: `npm install -g @usebruno/cli`
- Run: `bru run --env local`

#### 3.4 Add GitHub Actions workflow
You WILL add `github_actions_workflow_path` that:
- Sets up Node.js 20
- Installs `@usebruno/cli`
- Runs `bru run --env ci --reporter-html results.html --reporter-junit results.xml`
- Uploads the reports as artifacts

#### 3.5 Implement increment 1
If `implementation_mode=scaffold-and-implement`, you WILL implement the first increment end-to-end:
- health endpoint
- 1 business endpoint
- make Bruno tests pass locally
- ensure the CI workflow passes
<!-- </execution_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] You selected the latest OpenAPI + latest DB↔API fit analysis for the demand
- [ ] You produced an incremental plan and the user approved it
- [ ] Quarkus server scaffolding exists and can start
- [ ] TypeScript SDK scaffolding exists
- [ ] Bruno tests exist under `tests/bruno` and pass locally via `bru run --env local`
- [ ] GitHub Actions workflow exists and passes

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Spec directory not found**: Ask the user to confirm where `04-specifications` lives
- **OpenAPI missing**: Ask the user for explicit `openapi_path`
- **Data-fit analysis missing**: Ask the user for explicit `data_fit_analysis_path`
- **Unresolved High priority questions**: Stop and request SME answers before code generation
- **Tooling missing (Node, Maven/Gradle, Quarkus CLI)**: Explain what is missing and propose the minimal install steps

