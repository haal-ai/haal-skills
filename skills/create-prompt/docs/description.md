# create-prompt

## Overview
Drafts and stages an OLAF prompt file from a raw user request, asking for user approval before creating files.

## Purpose
Transform informal prompt ideas into properly structured OLAF prompt files, following established templates and prompting principles.

## Key Features
- Rewrites raw requests into clear, unambiguous English
- Applies prompting best practices from templates
- Uses Propose-Confirm-Act for safe file creation
- Generates timestamped prompt files

## Usage
```
@create-prompt
```

## Parameters
| Parameter | Required | Description |
|-----------|----------|-------------|
| raw_request | Yes | What the user wants the prompt to do |
| intended_user | No | Target audience (developer, PM, etc.) |
| context | No | Project or domain context |
| constraints | No | Limitations to respect |
| prompt_name | No | Kebab-case name (auto-suggested) |
| tags | No | 3-6 metadata tags (auto-suggested) |

## Process Flow
1. Validates user goal is clear enough
2. Rewrites request into clear US English
3. Gets user approval on rewritten version
4. Generates prompt using template
5. Proposes file save location
6. Saves after user confirmation

## Output
- Prompt file: `.olaf/staging/generated-prompts/{timestamp}-{prompt_name}.md`
- Summary with final file path

## Error Handling
| Scenario | Resolution |
|----------|------------|
| Missing raw_request | Asks what the prompt should do |
| Unsafe prompt_name | Proposes corrected kebab-case name |
| User rejects draft | Iterates until approved |

## Related Skills
- `convert-prompt-to-skill` - Convert prompts to full skills
- `evaluate-prompt-for-adoption` - Assess prompt quality
