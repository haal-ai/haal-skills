# Contract Kit Checklist

Use this checklist to ensure the kit is runnable, not just a list of files.

## 1) Inventory completeness
- OpenAPI snapshot exists inside the bundle
- Spec snapshots exist inside the bundle
- SDK snapshot exists inside the bundle (or explicitly marked missing)
- Tests snapshot exists inside the bundle (or explicitly marked missing)

## 2) Examples quality
- At least one GET example
- At least one write example if the API supports writes
- Examples include headers/content-type where needed
- Examples use placeholders (BASE_URL, AUTH_TOKEN, IDs)

## 3) Scenario walkthrough
- At least 3 endpoint calls
- Carries an ID from one call to another
- Narrative ties back to spec/use-case

## 4) Test alignment
- Examples should be consistent with the Bruno tests when present
- Explicitly say how to run tests locally
- The kit can be consumed without navigating to any external repo paths

## 5) No invented auth
- If auth is unclear, use placeholders and ask a question
