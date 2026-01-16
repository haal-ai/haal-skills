# Tutorial: Scaffold API From Spec

## 1) Provide the demand

Invoke:
- `olaf scaffold-api-from-spec`

When asked, provide:
- `demand_folder` (example: `pet-clinic-01`)

## 2) Review and approve the plan

The skill will:
- Locate the latest OpenAPI and DB↔API fit analysis
- Propose an incremental implementation plan

You MUST approve the plan before any files are written.

## 3) Run tests locally

Once Bruno tests are created:
- Install Bruno CLI: `npm install -g @usebruno/cli`
- Run from the Bruno project folder: `bru run --env local`

## 4) Verify CI

A GitHub Actions workflow will run the same Bruno tests using `--env ci` and upload reports as artifacts.
