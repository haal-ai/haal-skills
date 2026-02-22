---
name: email-assistant
description: Draft, reply to, or rewrite emails from pasted text. Asks for tone, conciseness, and language (default English). Produces a clean subject + email body and saves to a staging file after user approval.
argument-hint: "[paste email/text] - email assistant"
license: Apache-2.0
metadata:
  tags: [email, writing, reply, rewrite, tone, language]
  author: olaf
  provider: Haal AI
---

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user:
- **mode**: enum[draft,reply,rewrite] - What the user wants to do (REQUIRED)
- **input_text**: string - The email content or notes (REQUIRED — paste-based)
- **tone**: enum[professional,friendly,friends] - Desired tone (REQUIRED)
- **conciseness**: enum[very_short,short,medium,long] - How concise the email should be (REQUIRED)
- **language**: string - Output language (default: "english") (OPTIONAL)
- **recipient**: string - Recipient name/role (OPTIONAL)
- **sender**: string - Sender name (OPTIONAL)
- **subject_hint**: string - Subject guidance if the user has one (OPTIONAL)
- **signature**: string - Signature block to append (OPTIONAL)
- **output_file**: string - Output path (OPTIONAL — default to staging path below)

## User Interaction
- You MUST ask the user to choose `mode` if unclear.
- You MUST ask for `tone` and `conciseness` if not provided.
- Default `language` is English; you MUST allow the user to pick another language.
- You MUST ask for user approval before saving to disk.

When asking for choices, you MUST present them as a short menu and wait for the user's selection. Some chat clients render these as clickable options; if not, the user can reply with the option number/letter.

**Mode menu (if needed):**
```
Choose mode:
1) draft   — create a new email from notes
2) reply   — reply to a received email thread
3) rewrite — rewrite an existing draft
Reply with 1, 2, or 3.
```

**Tone menu (REQUIRED):**
```
Choose tone:
1) professional
2) friendly
3) friends
Reply with 1, 2, or 3.
```

**Conciseness menu (REQUIRED):**
```
Choose conciseness:
1) very_short
2) short
3) medium
4) long
Reply with 1, 2, 3, or 4.
```

**Language menu (OPTIONAL):**
```
Language (default: english)
A) english
B) french
C) another (type the language name)
Reply with A, B, or C.
```

You MUST accept common variants like "1", "option 1", "professional", "fr", "french", etc. If unclear, ask the user to pick again.

## Input Acquisition (paste-based)
The source text can be provided in two ways. You MUST detect which applies:

1. **Already pasted**: The user pasted the incoming email / draft / notes in their message along with (or before) invoking the skill. Use that content directly.
2. **Not yet provided**: The user invoked the skill without pasting content. Ask:
   > "Please paste the email (or your notes) and I’ll draft it." 

You MUST NOT require a file path.

## Process

### 1) Determine intent and ask minimal clarifying questions
Based on `mode`, you MUST ensure you have enough context:

- **draft**: goal + key points + any constraints (deadline, ask, link).
- **reply**: what the user wants to say back + any decision/ask.
- **rewrite**: what should change (tone, brevity, structure), and what must remain unchanged.

If important information is missing (recipient, goal, dates, promises, numbers), ask concise questions before drafting.

### 2) Draft subject + body
You MUST generate:
- A **Subject** line appropriate to the tone and conciseness.
- A full **Body** with:
  - greeting (adapt to tone)
  - 1 short context line
  - main message (bullets allowed for clarity)
  - call to action / next step if relevant
  - closing
  - signature if provided

### 3) Quality checks (MUST DO)
You MUST verify:
- The email does NOT invent facts.
- The email matches requested `tone`, `conciseness`, and `language`.
- The email is polite and clear.
- If the user asked for another language, keep names, product names, and URLs unchanged.

### 4) Output generation
You MUST format the final output using the template:
- `templates/email-template.md`

Default output path (if `output_file` not provided):
- `.olaf/work/staging/emails/email-[mode]-YYYYMMDD-HHmm.md`

You MUST:
- Present the rendered email to the user.
- Ask:
  > "Save this to `<output_file>`? (yes/no)"
- Only save if the user says yes.

## Domain-Specific Rules
- Rule 1: Do NOT fabricate information.
- Rule 2: Keep the email aligned with the chosen tone:
  - `professional`: formal, concise, no slang
  - `friendly`: warm, still professional
  - `friends`: casual, short, can be more informal
- Rule 3: Keep conciseness aligned with the chosen level:
  - `very_short`: 2-5 sentences
  - `short`: 1 short paragraph + optional bullets
  - `medium`: 2-3 short paragraphs
  - `long`: up to ~250-350 words, still structured
- Rule 4: Never include secrets, tokens, or private data unless the user explicitly provided them.

## Success Criteria
You WILL consider the task complete when:
- [ ] Mode, tone, conciseness, and language are confirmed
- [ ] Subject and email body are drafted
- [ ] Output follows the template
- [ ] User approves final content
- [ ] File is saved (if user approved)

## Error Handling
You WILL handle these scenarios:
- **No input text provided**: Ask the user to paste the email/notes
- **Unclear intent**: Ask 1-3 focused clarification questions
- **Conflicting instructions**: Ask the user which requirement wins (tone vs brevity vs completeness)
- **User rejects draft**: Ask what to change and regenerate
