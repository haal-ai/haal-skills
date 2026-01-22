---
# YAML preamble (update fields programmatically before saving)
id: {{id}}
name: {{title}}
shortDescription: {{short_description}}
domain: {{domain}}
use_case: {{use_case}}
language: {{language}}
status: draft
created: {{created_timestamp}}
updated: {{created_timestamp}}
---

# {{title}}

## Summary
- Type: {{practice_type}} practice (good/bad/both)
- ID: {{id}}
- Short description: {{short_description}}

## Description
{{long_description}}

## Why This Matters
{{why_important}}

## Good Practice
- Explanation:
{{good_explanation}}

- Example:
```{{language}}
{{good_example_code}}
```

## Bad Practice
- Explanation:
{{bad_explanation}}

- Example:
```{{language}}
{{bad_example_code}}
```

## Sources
- Files: {{sources_files}}
- Commits: {{sources_commits}}
- User comment: {{user_comment}}
