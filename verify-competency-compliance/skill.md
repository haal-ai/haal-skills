---
name: verify-competency-compliance
description: Verify a competency package complies with OLAF standards and required artifacts
license: Apache-2.0
---

# verify-competency-compliance

You verify that a given OLAF competency package is compliant.

## Input
- competency_id
- local_root (optional)

## Instructions
- Validate the competency manifest exists and is well-formed
- Validate referenced skills exist and contain skill-manifest.json
- Report issues and propose fixes
