---
name: list-skills
description: Present a concise list of all available skills from the current index
license: Apache-2.0
metadata:
  olaf_tags: [skill, list, index, query]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read the full reference/.condensed/olaf-framework-condensed.md.

Refer to reference/query-competency-index.md which is wrapped in the <olaf-query-competency-index> tag for the list of skills.

Instructions:
- Read the full <olaf-interaction-protocols>.
- Present a concise list of all available competencies from the current index.
- Output MUST be a numbered list.
- Each line MUST follow this exact format:
  - `N. <Skill Name> - <Protocol>`
- Do NOT include prompt paths, descriptions, tags, or any additional fields in the list output.
- If the user did not specify a particular task, ask 1-2 clarifying questions to narrow choices.
- When the user selects an item, execute the corresponding competency file.

Example format:
1. Analyze Project Onboarding - Propose-Act
2. Prepare Conversation Handover - Propose-Confirm-Act
3. Store Conversation Record - Act
