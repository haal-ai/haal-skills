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

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# check-prompt-compliance

You check a user-provided prompt for compliance with OLAF prompt conventions.

## Template and Principles Loading
You MUST read in full and apply:
- `templates/prompting-principles.md`

## Input
- prompt_text: the prompt to validate
- target_context: optional (e.g., skill prompt, workflow prompt, tool prompt)

## Instructions
- Identify non-compliance issues (structure, required sections, ambiguity, missing constraints)
- Validate the prompt against the principles in `templates/prompting-principles.md`, including:
  - Imperative language (WILL/MUST/NEVER) where appropriate
  - Explicit success criteria / acceptance checks
  - Clear separation between instructions and context
  - Explicit tool usage guidance when tools are expected
  - Consistent headings/formatting and comprehensive error handling when relevant
- Propose a corrected version (keep original intent; change only what improves compliance)
- If compliant, state that it is compliant and why
