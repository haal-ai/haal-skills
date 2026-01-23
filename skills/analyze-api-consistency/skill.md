---
name: analyze-api-consistency
description: Workflow skill that runs full code-mapper foundation analysis on a target repository, extracts public API signatures from the code-map output, and generates a structured API consistency report for selected modules or packages.
license: Apache-2.0
metadata:
  olaf_tags: [api-analysis, consistency, code-mapper, workflow]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response.
1. **project_path**: string - Absolute path or workspace-root-relative path to the repository under analysis (REQUIRED)
2. **code_mapper_path**: string - Path to the OLAF code-mapper scripts relative to workspace root (OPTIONAL - default: `scripts/code-mapper`)
3. **modules**: string[] - One or more target modules/packages to analyze for API consistency (REQUIRED)
4. **output_location**: string - Target output location if different from default (OPTIONAL - default: `.olaf/work/staging/code-mapper/<repo-name>/`)

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before running code-mapper or saving reports
- Present options as numbered lists for easy selection
- Provide clear progress updates at each major step
- Confirm whether to reuse or rerun foundation analysis

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate `project_path` is non-empty and identifies a directory
- Validate `code_mapper_path` is non-empty
- Confirm at least one target module/package is specified
- Resolve output directory based on workspace root and user input

### 2. Check Foundation Outputs and Run Full Foundation if Needed

You WILL resolve the output directory based on the workspace root and user input (default: `.olaf/work/staging/code-mapper/<repo-name>/`).

You MUST check for the presence of the **full foundation outputs** required for API analysis, including:
- The code-map/code-index file that contains full public API signatures for the repository (for example: a `CODE_MAP`/`code-index` style file produced by full foundation).

You WILL behave as follows:
- If the required full foundation outputs are **missing** for the target repository, you WILL instruct the user to run full foundation analysis from the workspace root:

```bash
cd <workspace-root>
python <code-mapper-path>/run.py --foundation <project-path>
```

- If the required outputs **exist** in the resolved output directory, you WILL explicitly ask the user whether they want to:
  - **Reuse** the existing full foundation outputs, or
  - **Rerun full foundation** and overwrite the existing files.

- Only if the user clearly chooses to rerun/overwrite, you WILL instruct them to run the full foundation command again. Otherwise you WILL proceed using the existing outputs.

### 3. Extract Public API Signatures from Foundation Outputs

Using the full foundation outputs in the resolved output directory, you WILL:

1. Locate the code-map / code-index file that contains public function/method signatures for the target modules.
2. For each module/package requested by the user:
   - Extract all public functions/methods and their full signatures (name, parameters, return types) from the code-map.
   - Group signatures by module/package.
3. Build an internal working set of public APIs to analyze, including:
   - Module/package name.
   - Source file path.
   - Function/method name.
   - Full parameter list and return type.

### 4. Analyze API Consistency Across Modules

For the extracted public APIs, you WILL analyze consistency along these dimensions:

1. **Naming Conventions**:
   - Verb patterns (e.g., get/fetch/retrieve, list/find, create/add).
   - Noun patterns for the same concepts (e.g., User/UserData/UserInfo).
   - Prefix/suffix usage (e.g., `IsValid` vs `ValidateX`, `ForRepo` suffixes).

2. **Parameter Patterns**:
   - Parameter order variations for similar functions.
   - Different names for the same concept (e.g., `id/userId/userID`, `repo/name`, `branch/ref`).
   - Handling of optional parameters (flags, options objects, defaulted parameters).

3. **Return Patterns and Error Handling**:
   - Error signaling patterns (return values vs exceptions/errors vs special values).
   - Success indicators (boolean vs object vs void).
   - Asynchronous patterns if applicable (callbacks vs futures/promises vs async/await).

You WILL identify and group inconsistencies by severity:

- **HIGH impact**: patterns that are likely to confuse users or break expectations.
- **MEDIUM impact**: patterns that are error-prone or reduce discoverability.
- **LOW impact**: patterns that are mostly stylistic or polish issues.

For each HIGH impact inconsistency, you WILL:
- Identify the "canonical" pattern (most used, most idiomatic, or best-practice).
- List all functions that deviate from this canonical pattern.
- For each deviating function, use the foundation outputs as your primary source; where necessary, you MAY suggest running code-mapper impact queries to understand callers, but you MUST NOT assume impact-query output is available unless explicitly provided.

### 5. Generate API Consistency Report

You WILL generate a structured API consistency report following `templates/api-consistency-analysis-structure.md`.

You MUST:
- Populate the "Extracted Public Function Signatures" section with a per-module list of public APIs and their signatures.
- Document all identified inconsistencies with clear descriptions and affected APIs.
- Provide a severity summary (HIGH/MEDIUM/LOW) with counts and short descriptions.
- Recommend canonical patterns for:
  - Repository reference representation (if applicable).
  - Verb choices for remote/local operations.
  - Parameter naming and ordering for recurring concepts.
- For each HIGH impact issue, include a detailed impact analysis:
  - Current state.
  - Proposed unified API.
  - Files/functions affected (as far as determinable from the foundation outputs).
- Propose an actionable improvement roadmap with phases (Immediate / Next / Future).
- Include a risk assessment and rollback considerations.

You WILL output **in the assistant response**:
- A single markdown document that follows `templates/api-consistency-analysis-structure.md`.
- A short summary of key findings and recommended next steps (e.g., "standardize on struct-based RepoRef", "rename Load* to Fetch*", etc.).

### 6. Output and Saving

You WILL THEN:
- Propose auto-saving the generated report to a sensible default path under the code-mapper staging area, for example:
  `.olaf/work/staging/code-mapper/<repo-name>/api-consistency-analysis.md`.
- Ask the user to confirm or override this target path.

Only AFTER explicit user confirmation, you MAY perform the save operation to the confirmed path (or instruct the caller/tool to do so). If the user declines, you MUST leave the report as response-only output.

### 7. Error Handling and Edge Cases

You MUST handle these situations explicitly:

- **Missing full foundation outputs**: If the required code-map/code-index file is missing:
  - Ask the user to confirm that full foundation analysis (with `--foundation`) was run successfully.
  - Suggest re-running full foundation if needed.

- **No public APIs found for a module**:
  - Document that the module does not expose public APIs according to the code-map.
  - Clearly indicate this in the report instead of guessing.

- **Ambiguous or partial module matches**:
  - If the requested module name is ambiguous, ask the user to clarify the exact module/package paths.

- **Incomplete signature information**:
  - If some signatures are incomplete in the foundation outputs, explicitly call this out and limit the analysis to what is known.

### 8. Success Criteria
You WILL consider the API consistency analysis successful when:
- [ ] A complete report following `templates/api-consistency-analysis-structure.md` has been produced
- [ ] All requested modules/packages have been analyzed, or clearly marked as not analyzable (with reasons)
- [ ] Major naming, parameter, and return-pattern inconsistencies have been identified and categorized by severity
- [ ] Canonical patterns and a phased improvement roadmap have been proposed
- [ ] User approved saving the report to the specified location

## Required Actions
1. Validate all required input parameters
2. Check for full foundation outputs or run foundation analysis
3. Extract public API signatures from code-map
4. Analyze API consistency across modules
5. Generate structured report following template
6. Save report after user confirmation

## Error Handling
You MUST handle these situations explicitly:
- **Missing full foundation outputs**: Ask user to confirm full foundation analysis was run, suggest re-running if needed
- **No public APIs found for a module**: Document in report that module does not expose public APIs
- **Ambiguous or partial module matches**: Ask user to clarify exact module/package paths
- **Incomplete signature information**: Call out limitations and analyze only what is known

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Foundation outputs validated or analysis running
- API signatures extracted
- Consistency analysis in progress
- Report generated

### Completion Summary
- Number of modules analyzed
- Inconsistencies found by severity
- Canonical patterns recommended
- Report saved location

### Next Steps
- Review API consistency report
- Prioritize high-impact inconsistencies
- Plan refactoring phases
- Update API documentation

⚠️ **Critical Requirements**
- MANDATORY: Use FULL foundation analysis (--foundation), not foundation-lite
- ALWAYS ask user whether to reuse or rerun existing foundation outputs
- ALWAYS provide evidence with file:line references
- ALWAYS categorize inconsistencies by severity (HIGH/MEDIUM/LOW)
- ALWAYS propose canonical patterns with clear rationale
- NEVER assume impact-query output is available unless explicitly provided
