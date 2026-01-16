---
name: create-prompt
description: Draft and stage an OLAF prompt file from a raw user request
license: Apache-2.0
metadata:
  olaf_tags: [prompt, generation, staging, prompt-engineer]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response:
1. **raw_request**: string - What the user wants the prompt to do (REQUIRED)
2. **intended_user**: string - Who will use this prompt (e.g., "developer", "product manager") (OPTIONAL)
3. **context**: string - Project or domain context the prompt should assume (OPTIONAL)
4. **constraints**: string - Constraints to respect (e.g., "must be short", "no external tools") (OPTIONAL)
5. **prompt_name**: string - Kebab-case name for the prompt (OPTIONAL - will be suggested)
6. **tags**: array - 3-6 tags for metadata (OPTIONAL - will be suggested)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- You WILL use **Propose-Confirm-Act** because you will create files under `.olaf/`

## Process

### 1. Validation Phase
You WILL validate:
- The user goal is clear enough to write a prompt
- The output folder exists (create if missing): `.olaf/work/staging/generated-prompts/`
- The output file name is safe (kebab-case slug, no path separators)

### 2. Drafting Phase
You WILL:
1. Rewrite the user’s request into clear US English (expanded + unambiguous)
2. Present the rewritten version and ask: "Is this correct? (yes/no/edit)"
3. If "edit": ask what to change and iterate until user says "yes"

### 3. Prompt Generation Phase
You MUST apply the principles in `templates/prompting-principles.md`.

You WILL generate a complete OLAF prompt markdown file using template:
- `templates/generated-prompt-template.md`

You MUST fill these placeholders:
- `{prompt_name}`
- `{prompt_description}`
- `{user_goal_in_clear_english}`
- `{tag1}..{tagN}`

### 4. Proposal Phase
You WILL show the full generated prompt file content and propose:
- Output folder: `.olaf/staging/generated-prompts/`
- Output filename: `{prompt_name}.md` 

Ask: "Ready to write this file? (yes/no/edit)"

### 5. Save Phase (Act)
After user confirmation:
- Create `.olaf/staging/generated-prompts/` if missing
- Write the prompt file to `.olaf/staging/generated-prompts/{timestamp}-{prompt_name}.md`
- Confirm the final path

## Output Format
You WILL produce:
- One prompt markdown file staged under `.olaf/staging/generated-prompts/`
- A short summary including the final file path

## Success Criteria
You WILL consider the task complete when:
- [ ] The rewritten request is approved by the user
- [ ] A prompt file is generated that follows `templates/prompting-principles.md`
- [ ] The prompt file is saved under `.olaf/staging/generated-prompts/`

## Error Handling
You WILL handle:
- **Missing raw_request**: Ask the user what they want the prompt to do
- **Unsafe prompt_name**: Propose a corrected kebab-case name
- **User rejects draft**: Iterate until approved
- **File write failure**: Explain why and propose an alternative filename

</olaf>
