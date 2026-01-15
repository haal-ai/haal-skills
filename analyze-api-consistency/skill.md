---
name: analyze-api-consistency
description: Workflow skill that runs full code-mapper foundation analysis on a target repository, extracts public API signatures from the code-map output, and generates a structured API consistency report for selected modules or packages.
license: Apache-2.0
---

<olaf>

# Analyze API Consistency with Code-Mapper

You WILL act as a workflow skill that runs code-mapper on a target repository using FULL foundation analysis and generates an API consistency report for selected modules, using the `templates/api-consistency-analysis-structure.md` template.

## Goal

You WILL help the user:
- Run full code-mapper foundation analysis on a target repository (NOT foundation-lite).
- Use the code-map output to extract complete public API signatures.
- Analyze naming, parameter, and return-pattern consistency across a module/package.
- Produce a structured API consistency report following `templates/api-consistency-analysis-structure.md`.

## Workflow

### 1. Collect Inputs

You MUST ask the user for:
- `project_path`: absolute path or **workspace-root–relative** path to the repository under analysis.
- `code_mapper_path`: path to the OLAF code-mapper scripts **relative to the workspace root**. The default is `scripts/code-mapper`.
- Optional: target output location if different from the default `.olaf/work/staging/code-mapper/<repo-name>/` **under the workspace root**.
- `modules`: one or more target modules/packages (language-appropriate notion, e.g. Go packages, Python modules, Java packages) to analyze for API consistency.

You MUST validate that:
- `project_path` is non-empty and clearly identifies a directory (absolute or workspace-root–relative).
- `code_mapper_path` is non-empty.
- At least one target module/package is specified.

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
- A complete report following `templates/api-consistency-analysis-structure.md` has been produced.
- All requested modules/packages have been analyzed, or clearly marked as not analyzable (with reasons).
- Major naming, parameter, and return-pattern inconsistencies have been identified and categorized by severity.
- Canonical patterns and a phased improvement roadmap have been proposed.

### 9. Usage Notes

You WILL explain to the user:
- That this skill relies on **full foundation** (`--foundation`) because the code-map output is required to see full API signatures.
- That the analysis is **syntactic and structural**, based on code-mapper outputs, and should be combined with tests and code reviews for final decisions.
