# Drift Analysis Report

RECOMMENDATION: <TOKEN> (<1 sentence rationale>)

## Metadata
- Demand: <demand_folder>
- Timestamp: <YYYYMMDD-HHmm>
- Source of truth: <code|openapi|functional_spec>
- Inputs:
  - Functional spec: <path>
  - OpenAPI: <path>
  - Code roots: <paths>
  - Tests: <paths>

## Executive Summary
- Drift items found: <count>
- High impact: <count>
- Medium impact: <count>
- Low impact: <count>

## Drift Summary Table
| Area | Item | Expected (truth) | Observed | Impact | Evidence |
|------|------|-------------------|----------|--------|----------|
| OpenAPI ↔ Code | <endpoint> | <...> | <...> | High/Med/Low | <file:line> |

## Functional Spec ↔ OpenAPI
- <drift item>

## OpenAPI ↔ Code
- <drift item>

## OpenAPI ↔ Tests (Bruno)
- <drift item>

## Tests ↔ Code
- <drift item>

## DB/DDL Safety Check
- Confirmed no DB/DDL artifacts were modified.

## Open Questions
- <question>
