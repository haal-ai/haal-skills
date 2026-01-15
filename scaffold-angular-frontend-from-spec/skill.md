---
name: scaffold-angular-frontend-from-spec
description: Scaffold an Angular (Angular Material) consumer UI implementing spec-defined journeys beyond CRUD
license: Apache-2.0
metadata:
  olaf_tags: [frontend, angular, angular-material, openapi, consumer, ui, scaffolding]
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
- **ui_output_dir**: string - Where to scaffold the Angular app (OPTIONAL - default: `apps/{demand_folder}-consumer-ui-ng`)
- **design_system**: string - UI design system (OPTIONAL - default: `Angular Material`)
- **implementation_mode**: plan-only|scaffold-only|scaffold-and-implement - How far to go (OPTIONAL - default: plan-only)
- **journey_focus**: string[] - Optional list of named journeys/scenarios to prioritize (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because the workflow writes files into the repository.

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- The `spec_dir` exists and contains expected artifacts
- The selected `openapi_path` exists
- The selected `functional_spec_path` exists
- `ui_output_dir` is within the repository

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
You WILL propose (in chat) a UI plan that includes:
- Target personas (consumer context) and key user journeys derived from the functional spec
- Screen map / navigation model
- Component breakdown (pages + reusable components)
- API consumption strategy:
  - base URL configuration
  - typed client approach (manual thin client wrappers unless user requests code generation)
- State management approach (simple service state by default)
- Error and loading states
- Acceptance criteria for increment 1 (1 end-to-end journey usable in the browser)

You MUST ask the user to approve the plan before writing any files.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3) Execution Phase (Only after approval)
You WILL:

#### 3.1 Scaffold Angular app
You WILL scaffold an Angular application under `ui_output_dir`.

#### 3.2 Add Angular Material
You WILL configure Angular Material as the default design system (theme, typography, layout primitives).

#### 3.3 Implement journeys (beyond CRUD)
You WILL implement the first increment as a scenario-driven flow:
- One multi-step journey that maps to multiple API calls (if applicable)
- Page-level routing
- Basic form validation, errors, and loading indicators

You MUST keep implementation aligned to the spec and OpenAPI contract.
<!-- </execution_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] Latest functional spec + latest OpenAPI were selected and read
- [ ] You proposed a UI plan and the user approved it
- [ ] Angular app scaffold exists under `ui_output_dir`
- [ ] Angular Material is configured
- [ ] At least one spec-defined journey is implemented end-to-end (as per `implementation_mode`)

## Error Handling
You WILL handle these scenarios:
- **Demand folder not found**: Ask the user for the correct `demand_folder`
- **Spec directory not found**: Ask the user to confirm where `04-specifications` lives
- **OpenAPI missing**: Ask the user for explicit `openapi_path`
- **Functional spec missing**: Ask the user for explicit `functional_spec_path`
- **Tooling missing (Node, Angular CLI)**: Explain what is missing and propose minimal install steps

