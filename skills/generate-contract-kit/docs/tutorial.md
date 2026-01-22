# Tutorial: Generate Contract Kit

## 1) Prerequisites
You should have a demand folder under `docs/specifications/` containing:
- `04-specifications/` (functional spec + OpenAPI)

Optional (if present):
- `sdks/` (generated SDK)
- `tests/bruno/` (Bruno collections)

## 2) Run the skill
```text
@[/olaf-generate-contract-kit]
demand_folder: <demand_folder>
example_language: <typescript|python|java|csharp>
```

The skill will:
- Select the latest OpenAPI and specs
- Snapshot/copy OpenAPI and specs into a bundle folder under `docs/specifications/<demand_folder>/08-contract-kit/`
- Snapshot/copy SDK and tests into the same bundle when they exist
- Generate `README.md` inside the bundle folder
- Ask for confirmation before writing
