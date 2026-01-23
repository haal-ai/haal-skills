# Scaffold API From Spec

## Purpose

This skill incrementally scaffolds an API implementation and its consumer assets from demand artifacts:
- Functional specification + OpenAPI contract (from `04-specifications/`)
- DB↔API fit analysis (from `05-data-fit-analysis/`)

Default target platform is Quarkus, with a TypeScript SDK for Angular/React clients.

## What you get

- A Quarkus server scaffold wired to the OpenAPI contract
- A TypeScript SDK scaffold generated from the OpenAPI contract
- A Bruno test suite runnable locally via CLI and in GitHub Actions

## How to invoke

Run:
- `olaf scaffold-api-from-spec`

Then provide the `demand_folder` when asked.

## Notes

This skill uses **Propose-Confirm-Act** and will always ask for approval before writing any files.
