# Scaffold Angular Frontend From Spec

Run:

```text
@[/scaffold-angular-frontend-from-spec]
demand_folder: <demand_folder>
```

You can optionally provide:
- `openapi_path`
- `functional_spec_path`
- `ui_output_dir`

The skill will:
- select the latest spec artifacts by default
- propose a UI plan (journeys, screens, components)
- after approval, scaffold the Angular app and implement the first journey
