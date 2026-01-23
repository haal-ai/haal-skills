---
name: create-changelog-entry
description: Add entries to functional or technical product changelogs with linked detail files
license: Apache-2.0
metadata:
  olaf_tags: [changelog, product, documentation, functional, technical]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

## Time Retrieval
Get current timestamp using time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user:
- **changelog_type**: enum[Functional,Technical] - Type of changelog to update (REQUIRED)
- **entry_type**: string - Entry type label used at the start of the changelog line (REQUIRED)
- **entry_description**: string - Concise description of the change (REQUIRED)
- **additional_context**: string - Detailed information for the linked detail file (REQUIRED)
- **subject_name**: string - Brief subject name for the detail file (kebab-case) (OPTIONAL - auto-generated if not provided)

## Workspace Safety (MANDATORY)
Before any file read/write operations, you MUST:
1. Compute the exact output paths you intend to write:
    - Changelog file: `.olaf/data/product/changelog-[changelog_type-lowercase].md`
    - Detail file: `.olaf/data/product/[changelog_type-lowercase]/[subject_name].md`
2. Only write files under `<.olaf/data/product/`.

## User Interaction

You MUST follow these interaction guidelines:
- Ask for user approval before creating or modifying files (changelog and detail files)
- Present resolved file paths for confirmation before writing
- Confirm entry format and placement in changelog structure
- Provide clear verification of clickable markdown links

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm changelog_type is either "Functional" or "Technical"
- Validate entry_type matches the target changelog conventions:
  - If Functional: Feature|Documentation|Enhancement|Setup
  - If Technical: Refactor|Architecture|Infrastructure|Fix|Cleanup|Breaking|Setup
- Validate entry_description is concise and clear
- Check additional_context provides sufficient detail
- Auto-generate subject_name from entry_description if not provided

### 2. Execution Phase
You WILL execute these operations:

**Preflight**:
- Print the resolved changelog + detail file paths.
- Wait for user confirmation before creating/modifying any files.

**Changelog Line Format (REGISTER INSERTION)**:
- The inserted line in `.olaf/data/product/changelog-[changelog_type-lowercase].md` MUST follow this exact format:
  - `- <entry_type>: <entry_description> [Details]([changelog_type-lowercase]/[subject_name].md)`

**File Operations**:
- Read current changelog: `.olaf/data/product/changelog-[changelog_type-lowercase].md`
- Determine if date section exists, create if needed
- Insert new entry at top of current date's entries
- Create detail file: `.olaf/data/product/[changelog_type-lowercase]/[subject_name].md`
- Populate detail file with `additional_context`

**Core Logic**
- Generate clickable markdown link format: `[Details]([subfolder]/[subject_name].md)`
- Maintain proper date section hierarchy (YYYY-MM format, then YYYY-MM-DD subsections)
- Preserve existing formatting and structure

### 3. Validation Phase
You WILL validate results:
- Confirm entry added to correct changelog file
- Verify detail file created with proper content
- Link verification: Confirm clickable markdown links work

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation of changelog type selection
- Date retrieved and formatted
- File operations completed

### Completion Summary
- Entry added to: `changelog-[type].md` with date: [YYYY-MM-DD]
- Detail file created: `[type]/[subject].md`
- Clickable link verified: `[Details]([type]/[subject].md)`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 0:All writes MUST be within the current repo workspace (i.e., paths rooted at `.olaf/`).
- Rule 1: Always add new entries to the top of their date section (reverse chronological order)
- Rule 2: Create missing date sections following format: `## YYYY-MM` then `### YYYY-MM-DD`
- Rule 3: Use kebab-case for all detail file names (lowercase, hyphens only)
- Rule 4: Preserve all existing changelog formatting and structure
- Rule 5: Generate clickable markdown links using format: `[Details](subfolder/filename.md)`

## Success Criteria
You WILL consider the task complete when:
- [ ] Changelog type validated
- [ ] Current date retrieved using terminal
- [ ] Entry added to correct date section in appropriate changelog
- [ ] Detail file created with user context
- [ ] Markdown link properly formatted and clickable
- [ ] No existing structure damaged or modified

## Required Actions
1. Validate all required input parameters
2. Execute file operations
3. Generate outputs with proper linking
4. Provide user communication and verification

## Error Handling
You WILL handle these scenarios:
- **Invalid Changelog Type**: Re-request with valid options (Functional/Technical)
- **Date Command Failure**: Provide fallback date determination method
- **File Access Issues**: Check permissions and provide alternative approaches
- **Malformed Existing Changelog**: Attempt repair or request manual intervention
- **Link Generation Failure**: Provide manual link format instructions

⚠️ **Critical Requirements**
- MANDATORY: Ask for user approval before modifying files (propose changes, get approval, then execute)
- NEVER modify files without user approval
- ALWAYS preserve existing changelog structure
- ALWAYS generate clickable markdown links
- ALWAYS create detail files with user-provided context
- ALWAYS add entries in reverse chronological order within date sections
