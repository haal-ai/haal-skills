# Convert Prompt to Skill

## Overview

Convert Prompt to Skill turns one or more existing prompt files (legacy prompts, external prompts, ad-hoc docs) into a new skill folder that matches the current OLAF skill layout.

It preserves the original intent while restructuring it into a single `skill.md` entry point, plus `docs/` and any optional component folders (templates/tools/helpers/kb) as needed.

## Purpose

Teams often have valuable prompts that are:
- not written as OLAF skills
- missing clear input parameters and success criteria
- embedding templates inline instead of referencing external files

This skill provides a repeatable conversion workflow so your skill library stays consistent and maintainable.

## Usage

- **Skill**: `convert-prompt-to-skill`
- **Protocol**: Propose-Confirm-Act

Use this when you want to create a new skill from existing prompt material rather than starting from scratch.

## Parameters

### Required Inputs
- **existing_prompt_path**: path or list of paths to source prompt file(s)
- **target_plugin**: plugin name to assign the created skill to

### Optional Inputs
- **skill_name**: new skill folder name (kebab-case, max 4 words)
- **user_request**: extra constraints (what to preserve, what to change)
- **needs_templates/tools/helpers/kb** (+ corresponding lists): whether to create optional component folders

## Output

Creates a new skill folder at the repo root:

- `[skill_name]/skill.md`
- `[skill_name]/docs/description.md`
- `[skill_name]/docs/tutorial.md`

Optional folders created only when requested:
- `templates/`, `tools/`, `helpers/`, `kb/`

The new `skill.md` frontmatter includes plugin assignment (`plugins: [target_plugin]`).

## Related Skills

- `create-skill`: create a brand new skill without a source prompt
- `check-prompt-compliance`: validate the converted `skill.md` quality and conventions

## Limitations

- Conversion quality depends on the clarity of the source prompt(s)
- Some prompts may require follow-up iterations to clarify missing inputs/outputs
