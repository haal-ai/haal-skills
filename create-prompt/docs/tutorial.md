# Create Prompt - Tutorial

## Goal
Draft a prompt from an idea and stage it for later use.

## Example
User:
- "I need a prompt that reviews a PR diff for security issues"

Flow:
1. The skill asks for missing context/constraints.
2. It rewrites your request into clear US English and asks you to approve it.
3. It generates the final OLAF prompt markdown.
4. After your confirmation, it writes the file to `.olaf/staging/generated-prompts/`.

## Output Location
- `.olaf/staging/generated-prompts/{timestamp}-{prompt_name}.md`

## Tip
If you want to convert a staged prompt into a full skill, use `create-skill` or `convert-prompt-to-skill` depending on your workflow.
