---
name: analyze-api-change-impact-from-deprecation-spec
description: Analyze consumer code impact from changed/evolved/deprecated endpoints and generate a modification + retest tasklist
license: Apache-2.0
metadata:
  olaf_tags: [api, openapi, consumer, impact-analysis, deprecation, migration, testing]
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
3. **change_spec_path**: string - Path to a change/deprecation spec markdown (REQUIRED)
4. **openapi_old_path**: string - Old OpenAPI contract (OPTIONAL)
5. **openapi_new_path**: string - New OpenAPI contract (OPTIONAL)
6. **consumer_code_roots**: string[] - Roots to search for consumer usage (OPTIONAL - default: `["apps", "sdks"]`)
7. **output_dir**: string - Where to write outputs (OPTIONAL - default: `{demand_root}/{demand_folder}/10-consumer-change-impact`)

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before creating or modifying files
- Present options as numbered lists for easy selection
- Provide clear progress updates at each major step

## Prerequisites
You MUST validate:
- The demand folder exists at `{demand_root}/{demand_folder}`
- `change_spec_path` exists
- If provided, `openapi_old_path` and `openapi_new_path` exist
- `consumer_code_roots` are within the repository
- `output_dir` is within `{demand_root}/{demand_folder}`

## Process

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters
- Read in full:
  - `change_spec_path`
- If provided, read in full:
  - `openapi_old_path`
  - `openapi_new_path`
- Build a list of impacted endpoints and changes, categorized as:
  - breaking change
  - behavior change
  - deprecated
  - additive/non-breaking
<!-- </validation_phase> -->

<!-- <planning_phase> -->
### 2) Planning Phase
You WILL propose (in chat):
- The impact analysis approach (how you will map endpoints to code usage)
- The exact output path:
  - `{output_dir}/{timestamp}-{demand_folder}-consumer-impact-tasklist.md`
- The search strategy (files to scan: TS/JS, Java, tests, docs)

You MUST ask the user to approve the plan before writing any files.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3) Execution Phase (Only after approval)
You WILL:
- Search `consumer_code_roots` for impacted endpoint paths, operationIds, and client method names
- Build an impact map:
  - change -> endpoint -> code references
- Generate a tasklist with:
  - required code modifications
  - required test updates / new tests
  - fallback/compat strategies (feature flags, dual contract support) when applicable
- Generate a retest plan:
  - impacted journeys
  - impacted contract tests

You WILL write a report using the provided template.
<!-- </execution_phase> -->

## Success Criteria
You WILL consider the task complete when:
- [ ] You read the change/deprecation spec in full
- [ ] (If provided) you read OpenAPI old/new in full
- [ ] You proposed an impact plan and the user approved it
- [ ] Impact report exists at `{output_dir}/{timestamp}-{demand_folder}-consumer-impact-tasklist.md`
- [ ] All impacted code references identified
- [ ] Retest plan generated

## Required Actions
1. Validate all required input parameters and prerequisites
2. Read and analyze change/deprecation spec
3. Search consumer code for impacted endpoints
4. Generate impact report with tasklist
5. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing change spec**: Ask the user for the correct `change_spec_path`
- **Ambiguous mapping**: Ask the user which client package/module is authoritative
- **No code hits**: Explain likely causes (generated client renamed, basePath differences) and propose alternate search terms

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Change spec analyzed
- Consumer code search in progress
- Impact map generated
- Tasklist created

### Completion Summary
- Files created with locations
- Number of impacted endpoints
- Code references found
- Retest plan summary

### Next Steps
- Review impact tasklist
- Prioritize code modifications
- Execute retest plan
- Update consumer documentation


