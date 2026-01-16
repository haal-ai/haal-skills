# Create Prompt

## Overview
Creates a staged OLAF prompt file from a raw user request.

## Purpose
Use this when you want to quickly turn an idea into a well-structured prompt, without committing it into a skill folder yet.

## What It Does
- Asks for the user’s goal and constraints
- Rewrites and expands the request into clear US English
- Generates an OLAF-formatted prompt markdown file (YAML front matter + `<olaf>`)
- Saves it to `.olaf/staging/generated-prompts/`

## Output
- `.olaf/staging/generated-prompts/{timestamp}-{prompt_name}.md`

## Notes
- The staging folder is intentionally separate from skill folders.
- The skill follows a Propose-Confirm-Act flow before writing files.
