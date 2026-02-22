# extract-meeting-notes

## What It Does
Extracts structured meeting notes from a pasted transcript. Produces a clean Markdown report containing:
- A 5-line summary of the meeting
- A table of actions with assigned owners
- A list of issues raised that need attention
- Author and date metadata

## When To Use
- After a recorded meeting where you have a transcript (e.g., Teams/Zoom auto-transcription)
- When you need to quickly share meeting outcomes with participants
- To create actionable follow-ups from a discussion

## Input
- Paste the transcript directly in the conversation
- Author name and meeting date (the skill will ask if not provided)

## Output
- A structured Markdown file following the template in `templates/meeting-notes-template.md`

## Example Usage
> Paste your transcript, then say: "extract meeting notes"
>
> Or say: "extract meeting notes" — the skill will invite you to paste the transcript.

The skill will:
1. Ask for your name (author) and the meeting date
2. Analyze the pasted transcript
3. Present a draft with summary, actions, and issues
4. Save the approved notes to a file of your choice

## Structure
```
extract-meeting-notes/
├── skill.md                           # Main skill prompt
├── templates/
│   └── meeting-notes-template.md      # Output template with author/date fields
└── docs/
    └── description.md                 # This file
```
