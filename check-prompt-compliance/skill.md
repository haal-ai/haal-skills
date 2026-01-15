---
name: check-prompt-compliance
description: Check a prompt for compliance with OLAF prompt standards
license: Apache-2.0
metadata:
  olaf_tags: [prompt, compliance, validation, standards]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# check-prompt-compliance

You check a user-provided prompt for compliance with OLAF prompt conventions.

## Input
- prompt_text: the prompt to validate
- target_context: optional (e.g., skill prompt, workflow prompt, tool prompt)

## Instructions
- Identify non-compliance issues (structure, required sections, ambiguity, missing constraints)
- Propose a corrected version
- If compliant, state that it is compliant and why
