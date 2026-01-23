# Analyze API Change Impact From Deprecation Spec

## Purpose

This skill helps API consumers analyze the impact of changed, evolved, or deprecated endpoints.
It produces an impact map and a tasklist of changes + retesting required in consumer code.

## Default output

- `docs/specifications/{demand_folder}/10-consumer-change-impact/{timestamp}-{demand_folder}-consumer-impact-tasklist.md`

## Notes

This skill uses **Propose-Confirm-Act** and will always ask for approval before writing any files.
