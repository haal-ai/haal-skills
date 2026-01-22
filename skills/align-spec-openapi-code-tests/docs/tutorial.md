# Tutorial

1. Provide a `demand_folder` (example: `pet-clinic-01`).
2. Confirm which artifact is the source of truth (default is code).
3. Review the proposed drift report + alignment plan outputs under `docs/specifications/{demand_folder}/08-drift-analysis/`.
4. Confirm the alignment changes.
5. Re-run tests and validate alignment.

Notes:
- If implementation is pending, explicitly choose the source of truth.
- DB/DDL artifacts are not modified by this skill.
