---
name: generate-contract-kit
description: Collect OpenAPI, specifications, SDK, and tests into a consumer-ready contract-kit with examples and scenario walkthroughs
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, contract, kit, examples, sdk, bruno, testing]
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
- **functional_spec_path**: string - Path to functional spec overview (OPTIONAL - default: latest `*-functional-spec.md` in `{spec_dir}`)
- **functional_spec_detailed_path**: string - Path to functional spec detailed (OPTIONAL - default: latest `*-functional-spec-detailed.md` in `{spec_dir}`)
- **openapi_path**: string - Path to OpenAPI YAML (OPTIONAL - default: latest `*-openapi.yaml` in `{spec_dir}`)
- **sdk_dir**: string - SDK root folder (OPTIONAL - default: `sdks/{demand_folder}-sdk-ts` if exists, otherwise ask)
- **bruno_root_dir**: string - Bruno tests root folder (OPTIONAL - default: `tests/bruno`)
- **github_actions_workflow_path**: string - CI workflow path for tests (OPTIONAL - default: `.github/workflows/api-tests.yml`)
- **contract_kit_output_dir**: string - Output folder for the kit bundle (OPTIONAL - default: `{demand_root}/{demand_folder}/08-contract-kit`)
- **output_basename**: string - Basename for output bundle folder (OPTIONAL - default: `demand_folder`)
- **base_url_example**: string - Example base URL shown in snippets (OPTIONAL - default: `http://localhost:8080`)
- **auth_example**: none|bearer - Auth model for examples (OPTIONAL - default: none)
- **example_language**: typescript|python|java|csharp - Additional language besides curl (REQUIRED; curl is always included)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because the workflow writes files into the repository.

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The specifications folder exists at `{spec_dir}`
- You can list and read `functional_spec_path`, `functional_spec_detailed_path`, `openapi_path`
- `contract_kit_output_dir` is within `{demand_root}/{demand_folder}`

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

You MUST also check for optional artifacts and record their presence:
- If `sdk_dir` exists, list its contents (do not assume it exists)
- If `bruno_root_dir` exists, locate relevant Bruno collections for this demand (do not assume they exist)
- If `github_actions_workflow_path` exists, reference it

If SDK/tests are missing:
- You MUST still generate the contract-kit, but mark missing items explicitly and point to the skill that can generate them (e.g., `scaffold-api-from-spec`).
<!-- </validation_phase> -->

<!-- <execution_phase> -->
### 2) Execution Phase
You WILL generate a self-contained contract-kit bundle folder (no external paths required to consume the kit).

The bundle MUST be created under `{contract_kit_output_dir}` with this structure:
 - `{contract_kit_output_dir}/{timestamp}-{output_basename}-contract-kit/`
   - `README.md`
   - `artifacts/openapi/` (snapshot)
   - `artifacts/spec/` (snapshot)
   - `artifacts/sdk/` (snapshot when present)
   - `artifacts/tests/` (snapshot when present)
   - `artifacts/ci/` (snapshot when present)

You MUST snapshot/copy artifacts into the bundle as follows:
- Copy `openapi_path` into `artifacts/openapi/` preserving the original filename.
- Copy `functional_spec_path` and `functional_spec_detailed_path` into `artifacts/spec/` preserving original filenames.
- If `sdk_dir` exists, copy it into `artifacts/sdk/`.
- If relevant tests exist under `bruno_root_dir`, copy the relevant folder(s) into `artifacts/tests/`.
- If `github_actions_workflow_path` exists, copy it into `artifacts/ci/` preserving the original filename.

When snapshotting folders, you MUST avoid copying build artifacts and dependencies (for example: `node_modules/`, `target/`, `dist/`, `.git/`).

You WILL generate `README.md` using template: `templates/contract-kit-output-format.md`.

You MUST include:

#### 2.1 Bundle Inventory
This inventory MUST reference ONLY files inside the bundle folder using relative paths.
- OpenAPI snapshot file path
- Functional spec snapshot file paths
- SDK snapshot path (if present)
- Tests snapshot path (if present)
- CI workflow path (if present)

#### 2.2 Simple examples
You MUST provide a few simple examples:
- One read-only GET (e.g., health, list, or get-by-id)
- One write example (POST or PUT/PATCH) if the API supports writes

For each example:
- Provide a `curl` snippet
- Provide a snippet in `example_language`
- Use placeholders for IDs and tokens

#### 2.3 Engaging scenario walkthrough (multi-roundtrip)
You MUST create one scenario based on the spec’s main use-case flows.
- It MUST include multiple roundtrip calls to different endpoints (at least 3)
- It MUST show how to pass IDs from one call into the next
- If auth is unspecified in the spec, you MUST not invent a full auth flow; use `AUTH_TOKEN` placeholder and flag it as an assumption.

You MUST extract the scenario narrative from the functional spec (or clearly label assumptions).

You MUST use reference: `/kb/contract-kit-checklist.md`.
<!-- </execution_phase> -->

<!-- <output_phase> -->
### 3) Output Phase
You WILL:
- Propose a self-contained bundle folder under `{contract_kit_output_dir}`
- Bundle folder name:
  - `{timestamp}-{output_basename}-contract-kit`
- `README.md` path:
  - `{contract_kit_output_dir}/{timestamp}-{output_basename}-contract-kit/README.md`
- Proposed snapshots (files/folders to be copied into the bundle)

You MUST ask for confirmation before creating folders/files or copying any artifacts.
<!-- </output_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] Latest spec inputs were selected and read
- [ ] Contract kit inventory was produced
- [ ] Simple curl + language examples were produced
- [ ] A multi-endpoint scenario walkthrough was produced
- [ ] You proposed the output file path and received user confirmation
- [ ] The bundle folder has been created under `contract_kit_output_dir`
- [ ] `README.md` has been written inside the bundle folder
- [ ] Required artifacts were snapshotted into `artifacts/` (or explicitly marked missing)

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Spec directory not found**: Ask the user to confirm where `04-specifications` lives
- **OpenAPI missing**: Ask the user for explicit `openapi_path`
- **SDK/tests missing**: Mark as missing; point to `scaffold-api-from-spec` as next step
- **Auth unclear**: Use placeholders and ask a question; do not invent details


