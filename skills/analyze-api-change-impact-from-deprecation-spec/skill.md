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

## What This Skill Does

This skill helps you understand how API changes will affect your consumer applications and services. When your API team publishes deprecation notices or breaking changes, this skill:

🔍 **Analyzes the impact** by scanning your codebase to find all places where the changed API endpoints are used
📋 **Creates a tasklist** with specific code modifications needed for each impacted consumer
🧪 **Generates a retest plan** to ensure your changes work correctly after migration
📊 **Provides a clear report** showing exactly what needs to be changed and tested

**Use this skill when:**
- API endpoints are being deprecated or removed
- Request/response formats are changing
- Authentication or authorization requirements are updated
- You need to plan consumer migration efforts
- You want to ensure no consumer code is left behind during API evolution

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response.

1. **demand_folder**: string - The name of your project/demand folder located under `docs/specifications/` (example: `pet-clinic-01`). This helps organize the analysis output within your project structure. (REQUIRED)

2. **demand_root**: string - The base directory where your demand folders are stored (OPTIONAL - default: `docs/specifications`)

3. **change_spec_path**: string - Full path to the markdown file containing the API change/deprecation specification. This document should describe what endpoints are changing, how they're changing, and any migration guidance. (REQUIRED)

4. **openapi_old_path**: string - Full path to the previous version of your OpenAPI/Swagger specification (OPTIONAL). Providing this helps the skill understand the exact contract that was in use before the changes.

5. **openapi_new_path**: string - Full path to the new version of your OpenAPI/Swagger specification (OPTIONAL). This helps the skill understand the target contract after the changes.

6. **consumer_code_roots**: string[] - List of directory paths where your consumer code is located (OPTIONAL - default: `["apps", "sdks"]`). The skill will search these directories for API usage. Examples: `["frontend-app", "mobile-sdk", "integration-tests"]`

7. **output_dir**: string - Directory where the impact analysis report will be saved (OPTIONAL - default: `{demand_root}/{demand_folder}/10-consumer-change-impact`). The report will be named with a timestamp to avoid overwriting previous analyses.

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

## Process Overview

The skill follows a structured 3-phase approach to ensure thorough analysis and clear communication:

### Phase 1: Validation & Understanding
First, I validate all inputs and read your specifications to understand exactly what's changing.

### Phase 2: Planning & Approval  
I propose a detailed analysis plan and get your approval before proceeding with code scanning.

### Phase 3: Analysis & Reporting
I execute the analysis, identify all impacted code, and generate a comprehensive tasklist and retest plan.

---

## Process Details

<!-- <validation_phase> -->
### 1) Validation Phase
You WILL:
- Validate all required parameters and file locations
- Read and analyze the complete change specification to understand:
  - Which endpoints are affected
  - What types of changes are occurring (breaking, behavioral, deprecation, additive)
  - Migration requirements and timelines
- If provided, compare OpenAPI old/new contracts to identify:
  - Removed or modified endpoints
  - Changed request/response schemas
  - Updated authentication requirements
- Build a comprehensive list of impacted endpoints categorized by impact severity:
  - **breaking change** - Will require code updates in consumers
  - **behavior change** - May require logic updates
  - **deprecated** - Will be removed in future, needs migration planning
  - **additive/non-breaking** - New features, optional to adopt
<!-- </validation_phase> -->

<!-- <planning_phase> -->
### 2) Planning Phase
You WILL propose (in chat):
- **Impact Analysis Strategy**: How I'll map API endpoints to your consumer code
  - Search patterns (endpoint paths, HTTP methods, operation IDs)
  - File types to scan (TypeScript, JavaScript, Java, Python, tests, configs)
  - Client library detection (generated clients, custom wrappers)
- **Output Location**: Exact path where the report will be saved
  - `{output_dir}/{timestamp}-{demand_folder}-consumer-impact-tasklist.md`
- **Search Scope**: Which directories and file types to include in the analysis

You MUST get user approval before proceeding to code scanning.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3) Execution Phase (Only after approval)
You WILL:
- **Code Discovery**: Search all specified consumer code directories for:
  - Direct endpoint path references (`/api/v1/users`)
  - HTTP method calls (`GET /users`, `POST /orders`)
  - Operation ID references from OpenAPI specs
  - Generated client method names
  - API base URL configurations
- **Impact Mapping**: Create a detailed mapping showing:
  - Each API change → Affected endpoints → Specific code locations
  - Severity assessment for each impacted file
  - Dependencies between different consumer components
- **Tasklist Generation**: Create actionable tasks for:
  - **Code Modifications**: Exact changes needed in each consumer
  - **Test Updates**: Which tests need to be updated or created
  - **Migration Strategies**: Feature flags, dual contract support, gradual rollout
  - **Documentation Updates**: API docs, README files, integration guides
- **Retest Planning**: Generate comprehensive testing strategy:
  - **Integration Tests**: End-to-end flows that need validation
  - **Contract Tests**: API consumer contract compliance
  - **Regression Tests**: Ensure existing functionality still works
  - **Performance Tests**: Validate no performance degradation

You WILL write a comprehensive report using the provided template.
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


