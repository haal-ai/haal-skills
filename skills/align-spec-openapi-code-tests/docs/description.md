# Align Spec, OpenAPI, Code, and Tests

Detect drift across functional specifications, OpenAPI, implementation code, and Bruno CLI tests for a given demand. The skill produces a drift report and an alignment plan under `docs/specifications/{demand_folder}/08-drift-analysis/`.

Defaults:
- Source of truth: code
- Output folder: `docs/specifications/{demand_folder}/08-drift-analysis`

Constraints:
- DB/DDL artifacts are never modified.
