---
name: check-prompt-compliance
description: Check a prompt for compliance with OLAF prompt standards
license: Apache-2.0
---

<olaf>

# check-prompt-compliance

You check a user-provided prompt for compliance with OLAF prompt conventions.

## Input
- prompt_text: the prompt to validate
- target_context: optional (e.g., skill prompt, workflow prompt, tool prompt)

## Instructions
- Identify non-compliance issues (structure, required sections, ambiguity, missing constraints)
- Propose a corrected version
- If compliant, state that it is compliant and why
