---
name: {prompt_name}
description: {prompt_description}
license: Apache-2.0
metadata:
  olaf_tags: [{tag1}, {tag2}, {tag3}]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Goal
{user_goal_in_clear_english}

## Input Parameters
You MUST request these parameters if not provided by the user:
1. **context**: string - Any relevant project context (OPTIONAL)
2. **constraints**: string - Constraints to respect (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Select appropriate protocol based on operation risk and impact

## Process

### 1. Clarify
You WILL ask targeted questions until you can proceed.

### 2. Execute
You WILL complete the user’s request following the rules and constraints.

### 3. Validate
You WILL validate the output against the goal and constraints.

## Output Format
You WILL output results in a clear, structured format.

## Success Criteria
- [ ] The prompt is clear, unambiguous, and written in US English
- [ ] Required inputs are explicitly requested
- [ ] Steps are written using imperative language (You WILL / You MUST)
- [ ] Error cases are handled

## Error Handling
You WILL handle these scenarios:
- **Missing Information**: Ask for the minimum missing details
- **Ambiguous Goal**: Propose 2-3 interpretations and ask the user to choose
- **Constraint Conflict**: Explain the conflict and ask which constraint wins

