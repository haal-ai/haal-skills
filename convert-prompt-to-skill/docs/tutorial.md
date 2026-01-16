# Tutorial: Convert Prompt to Skill

## Overview
This tutorial walks through converting one or more existing prompt files into a new OLAF skill folder (`skill.md` + docs + optional components).

## Prerequisites
1. You have at least one prompt file to convert
2. You know which plugin should own the new skill (the `target_plugin` value)

## Estimated Time
15-30 minutes (depends on prompt complexity)

## Steps

### Step 1: Provide Source Prompt Path(s)
Give the file path (or list of file paths) for the prompt(s) you want to convert.

### Step 2: Provide Target Plugin
Specify the plugin to assign the new skill to:
1. existing plugin name, or
2. a new plugin name (it will be added to `.olaf/plugins.json`)

### Step 3: Provide Skill Name (Optional)
If you don’t provide one, the conversion will propose a kebab-case name (max 4 words).

### Step 4: Decide on Optional Components
Answer whether the new skill needs any of:
1. templates
2. tools
3. helpers
4. knowledge base files

Only the requested component folders/files are created.

### Step 5: Review the Proposed Skill
Review the proposed new skill folder:
- `skill.md` matches the skill template structure
- external templates are referenced, not embedded
- error handling and success criteria are explicit

### Step 6: Confirm and Generate
Approve the conversion (Propose-Confirm-Act), then generate the skill folder and files.

## Verification Checklist
- [ ] New folder created at repo root with the expected name
- [ ] `skill.md` exists and is the main entry point
- [ ] `docs/description.md` exists
- [ ] `docs/tutorial.md` exists
- [ ] Optional component folders only exist if requested
- [ ] Skill plugin assignment recorded in `skill.md` metadata and `.olaf/plugins.json`

## Troubleshooting
- **Source file not found**: verify the path(s) and try again
- **Skill name conflict**: choose a different kebab-case name
- **Unclear prompt intent**: add `user_request` guidance (what to preserve/change)

## Next Steps
- Run `check-prompt-compliance` on the generated `skill.md`
- Test the skill with a real example invocation
