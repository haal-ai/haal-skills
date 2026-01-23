# Analyze API Change Impact From Deprecation Spec

Run:

```text
@[/analyze-api-change-impact-from-deprecation-spec]
demand_folder: <demand_folder>
change_spec_path: <path-to-change-spec>
```

Optionally provide:
- `openapi_old_path`
- `openapi_new_path`
- `consumer_code_roots`

The skill will:
- read the change spec (and OpenAPI diffs if provided)
- propose a search and impact analysis plan
- after approval, generate an impact map, tasklist, and retest plan under `10-consumer-change-impact/`
