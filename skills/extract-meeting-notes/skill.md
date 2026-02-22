---
name: extract-meeting-notes
description: Extract structured meeting notes (summary, actions, issues) from a pasted meeting transcript. Produces a clean Markdown report with author and date metadata.
argument-hint: "[paste transcript or describe meeting] - extract meeting notes"
license: Apache-2.0
metadata:
  tags: [meeting, transcript, summary, actions, notes]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/Amadeus-xDLC/genai.claude-code-evaluation
  provider: Haal AI
---

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user:
- **transcript**: string - The meeting transcript content (REQUIRED — see Transcript Acquisition below)
- **author**: string - Name of the person creating these notes (REQUIRED)
- **date**: string - Date of the meeting in YYYY-MM-DD format (REQUIRED — suggest today's date as default)
- **output_file**: string - Path for the output notes file (OPTIONAL — ask user where to save)

## User Interaction
- You MUST ask for `author` and `date` if not provided
- You MUST ask for user approval before saving the output file
- Present extracted actions and issues for review before finalizing

## Transcript Acquisition
The transcript can be provided in two ways. You MUST detect which applies:

1. **Already pasted**: The user has pasted the transcript content in their message along with (or before) the skill invocation. In this case, use that content directly — do NOT ask for it again.
2. **Not yet provided**: The user invoked the skill without pasting content. In this case, you MUST invite the user to paste the transcript:
   > "Please paste your meeting transcript below and I'll extract the notes."

You MUST NOT ask for a file path. The expected workflow is paste-based.

## Process

### 1. Validation Phase
You MUST verify all requirements:
- Confirm transcript content has been provided (pasted by user)
- Confirm `author` and `date` are provided (prompt user if missing)
- If output file location not specified, ask the user where to save

### 2. Transcript Analysis Phase
You MUST read the full transcript file and extract the following:

**Identify Speakers:**
- Detect all unique speakers/participants mentioned in the transcript
- Note who joined late or left early

**Extract Summary (5 lines max):**
- Identify the main topics discussed
- Capture key decisions made
- Note the overall outcome or conclusion
- You MUST limit the summary to exactly 5 concise lines

**Extract Actions:**
- Identify all commitments, tasks, or follow-ups mentioned
- For each action, determine:
  - **What**: The specific action to be taken
  - **Who**: The person responsible (use speaker names from the transcript)
- Present actions as a Markdown table

**Extract Issues:**
- Identify concerns, risks, blockers, or unresolved questions raised during the meeting
- For each issue, provide a brief description of why it needs attention
- Present issues as a numbered list with bold issue title and description

### 3. Output Generation Phase
You MUST generate the output file following the template: `templates/meeting-notes-template.md`

- Fill in all template fields with extracted data
- Ensure the `author` and `date` fields are populated from user input
- Ensure `participants` lists all detected speakers

### 4. Validation Phase
You WILL validate results:
- Confirm summary is exactly 5 lines
- Confirm every action has an owner
- Confirm issues are clearly described
- Present the draft to the user for approval before saving

## Output Format
You WILL generate the output following the template: `templates/meeting-notes-template.md`

**OUTPUT LOCATION**: The generated notes file WILL be saved to the `output_file` path specified by the user.

## User Communication

### Progress Updates
- Confirmation when transcript is received and speakers are identified
- Draft presented for user review before saving

### Completion Summary
- Summary of what was extracted (number of actions, issues)
- Location of the saved notes file

### Next Steps
You WILL suggest:
- Review the generated notes and share with meeting participants
- Track the identified actions in your project management tool
- Address the flagged issues in upcoming discussions

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Summary MUST be exactly 5 lines — no more, no less
- Rule 2: Every action MUST have an identified owner
- Rule 3: You MUST NOT fabricate information — only extract what is explicitly stated or strongly implied in the transcript
- Rule 4: Speaker names MUST match how they appear in the transcript
- Rule 5: The output MUST follow the template structure from `templates/meeting-notes-template.md`
- Rule 6: Author and date MUST appear in the output metadata section

## Success Criteria
You WILL consider the task complete when:
- [ ] Transcript content received from user
- [ ] All speakers/participants identified
- [ ] Summary extracted (exactly 5 lines)
- [ ] All actions extracted with owners
- [ ] All issues extracted with descriptions
- [ ] Output generated following the template
- [ ] Author and date fields populated
- [ ] User approved the output
- [ ] File saved to specified location

## Error Handling
You WILL handle these scenarios:
- **No transcript provided**: Invite user to paste the transcript content
- **Transcript too short or unclear**: Inform user the content seems incomplete, ask if they want to paste more
- **No clear speakers identified**: Ask user to clarify speaker names
- **No actions found**: Explicitly state "No actions identified" in the output
- **No issues found**: Explicitly state "No issues identified" in the output
- **Ambiguous action owner**: Present ambiguity to user and ask for clarification
- **User rejects draft**: Ask for specific feedback and regenerate
