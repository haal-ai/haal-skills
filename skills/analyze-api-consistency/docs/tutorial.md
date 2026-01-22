# Analyze API Consistency - Tutorial

1. From your workspace root (directory containing `.olaf/`), identify the target project path.
2. Run full code-mapper foundation analysis:

   ```bash
   cd <workspace-root>
   python scripts/code-mapper/run.py --foundation <project-path>
   ```

3. Invoke the `analyze-api-consistency` skill and provide:
   - `project_path` (absolute or workspace-root–relative).
   - `code_mapper_path` if different from the default `scripts/code-mapper`.
   - Optional custom output directory under `.olaf/work/staging/code-mapper/`.
   - One or more target modules/packages to analyze.

4. The skill will:
   - Reuse or rerun full foundation as needed.
   - Extract public API signatures for the selected modules from the code-map.
   - Analyze naming, parameter, and return-pattern consistency.
   - Generate a markdown report following `templates/api-consistency-analysis-structure.md`.

5. Review the report and, if desired, confirm a path under `.olaf/work/staging/code-mapper/<repo-name>/` to save it (for example `api-consistency-analysis.md`).
