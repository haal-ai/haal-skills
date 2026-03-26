# email-assistant

## Overview
Draft, reply to, or rewrite emails from pasted text. Asks for tone, conciseness, and language preferences, then produces a clean subject line and email body.

## Purpose
Quickly compose professional emails without spending time on structure and tone. Use when you need to draft a new email, reply to a received message, or rewrite an existing draft with different tone or brevity.

## Key Features
- Three modes: draft, reply, rewrite
- Tone control: professional, friendly, or casual (friends)
- Conciseness levels: very short (2-5 sentences) to long (~350 words)
- Multilingual output (default: English)
- Paste-based input (no file paths required)
- Staging file output with user approval
- Quality checks to prevent fabricated information

## Usage
Invoke this skill by saying:
- "Draft an email to the team about the release"
- "Reply to this email" (paste the email)
- "Rewrite this email in a friendlier tone"

## Parameters

### Required
- **mode**: draft | reply | rewrite
- **input_text**: The email content or notes (pasted)
- **tone**: professional | friendly | friends
- **conciseness**: very_short | short | medium | long

### Optional
- **language**: Output language (default: English)
- **recipient**: Recipient name/role
- **sender**: Sender name
- **subject_hint**: Subject line guidance
- **signature**: Signature block to append
- **output_file**: Output path (default: `.olaf/work/staging/emails/`)

## Process Flow
1. **Determine Intent** — Identify mode and gather context
2. **Collect Parameters** — Ask for tone, conciseness, language via menus
3. **Draft Email** — Generate subject line and formatted body
4. **Quality Check** — Verify no fabricated facts, correct tone/language
5. **User Approval** — Present email and confirm before saving
6. **Save** — Write to staging file

## Output
- Formatted email with subject and body
- Saved to `.olaf/work/staging/emails/email-[mode]-YYYYMMDD-HHmm.md`

## Related Skills
- **clean-srt-transcript**: For cleaning up text from other sources
