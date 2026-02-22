# Tutorial: extract-meeting-notes

## Quick Start

1. Say **"extract meeting notes"** in your AI assistant
2. Paste your meeting transcript when prompted (or paste it alongside the command)
3. Provide your name and the meeting date when asked
4. Review the draft — approve or request changes
5. The skill saves the final notes to a file of your choice

## Example

```
> extract meeting notes

Please paste your meeting transcript below and I'll extract the notes.

> [paste transcript here]

Author? > Jane Doe
Date? > 2026-02-20

[Draft presented with summary, actions, issues]

Looks good? > yes
Saved to: ./meeting-notes-2026-02-20.md
```

## Tips

- Works with any transcript format (Teams, Zoom, manual notes)
- The summary is always exactly 5 lines — concise by design
- Every action gets an owner extracted from the transcript
- If the skill can't determine who owns an action, it will ask you
- You can re-run on the same transcript to refine the output

## Output

The generated file follows the template in `templates/meeting-notes-template.md` and includes:

- Metadata (author, date)
- Participant list
- 5-line summary
- Actions table with owners
- Issues list with descriptions
