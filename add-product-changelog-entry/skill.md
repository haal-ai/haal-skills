---
name: add-product-changelog-entry
description: Add entries to functional or technical product changelogs with linked detail files
license: Apache-2.0
metadata:
  olaf_tags: [changelog, product, documentation, functional, technical]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

## Input Parameters
You MUST request these parameters if not provided by the user:
- **changelog_type**: enum[Functional,Technical] - Type of changelog to update (REQUIRED)
- **entry_type**: string - Entry type label used at the start of the changelog line (REQUIRED)
- **entry_description**: string - Concise description of the change (REQUIRED)
- **additional_context**: string - Detailed information for the linked detail file (REQUIRED)
- **subject_name**: string - Brief subject name for the detail file (kebab-case) (OPTIONAL - auto-generated if not provided)

## Workspace Safety (MANDATORY)
Before any file read/write operations, you MUST:
1. Detect the git repository root using `git rev-parse --show-toplevel`.
2. If git root cannot be determined, STOP and ask the user to run the skill from within a git repository.
3. Resolve repository output targets relative to the git root:
   - Changelog and detail file targets under `.olaf/data/product/...` MUST be resolved as `<git_root>/.olaf/data/product/...`.
4. Resolve skill-local resources relative to the skill directory (NOT the git root):
   - For example, `templates/[changelog_type-lowercase]-changelog-template.md` is resolved within this skill folder.
5. Validate that every resolved repository output target path is a descendant of the git root directory.
6. Display a preflight summary of the exact resolved repository output paths you will modify/create and wait for explicit user approval before proceeding.

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Use Propose-Act protocol for this competency (file modifications with user review)

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

**Template Loading**:
- Load appropriate template: `templates/[changelog_type-lowercase]-changelog-template.md`
- Parse template for detail file structure only

**Changelog Line Format (REGISTER INSERTION)**:
- The inserted line in `.olaf/data/product/changelog-[changelog_type-lowercase].md` MUST follow this exact format:
  - `- <entry_type>: <entry_description> [Details]([changelog_type-lowercase]/[subject_name].md)`

**File Operations**:
- Read current changelog: `<git_root>/.olaf/data/product/changelog-[changelog_type-lowercase].md`
- Determine if date section exists, create if needed
- Insert new entry at top of current date's entries
- Create detail file: `<git_root>/.olaf/data/product/[changelog_type-lowercase]/[subject_name].md`
- Populate detail file using template structure with additional_context

**Core Logic**: Execute following template requirements
- Do NOT infer the changelog line format from templates
- Generate clickable markdown link format: `[Details]([subfolder]/[subject_name].md)`
- Maintain proper date section hierarchy (YYYY-MM format, then YYYY-MM-DD subsections)
- Preserve existing formatting and structure

### 3. Validation Phase
You WILL validate results:
- Confirm entry added to correct changelog file
- Verify detail file created with proper content
- Check markdown link is properly formatted and clickable
- Validate no existing structure was damaged

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Updated changelog file with new entry
- Supporting files: Detail file in appropriate subfolder
- Link verification: Confirm clickable markdown links work

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation of changelog type selection
- Template loading success
- Date retrieved and formatted
- File operations completed

### Completion Summary
- Entry added to: `changelog-[type].md` with date: [YYYY-MM-DD]
- Detail file created: `[type]/[subject].md`
- Clickable link verified: `[Details]([type]/[subject].md)`
- Entry position: Top of current date section

### Next Steps
You WILL clearly define:
- Changelog entry is live and linked
- Detail file can be edited for additional context
- Files are ready for git commit/web publishing

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 0: NEVER create, modify, or delete any file under `~/.olaf/` (e.g., `~/.olaf/`). All writes MUST be within the current repo workspace (i.e., paths rooted at `.olaf/`).
- Rule 1: Always add new entries to the top of their date section (reverse chronological order)
- Rule 2: Create missing date sections following format: `## YYYY-MM` then `### YYYY-MM-DD`
- Rule 3: Use kebab-case for all detail file names (lowercase, hyphens only)
- Rule 4: Preserve all existing changelog formatting and structure
- Rule 5: Generate clickable markdown links using format: `[Details](subfolder/filename.md)`

## Success Criteria
You WILL consider the task complete when:
- [ ] Changelog type validated and template loaded
- [ ] Current date retrieved using terminal
- [ ] Entry added to correct date section in appropriate changelog
- [ ] Detail file created with template structure and user context
- [ ] Markdown link properly formatted and clickable
- [ ] No existing structure damaged or modified

## Required Actions
1. Validate all required input parameters
2. Load appropriate changelog template
3. Execute file operations following template structure
4. Generate outputs with proper linking
5. Provide user communication and verification

## Error Handling
You WILL handle these scenarios:
- **Invalid Changelog Type**: Re-request with valid options (Functional/Technical)
- **Template Not Found**: Provide error and manual template guidance
- **Date Command Failure**: Provide fallback date determination method
- **File Access Issues**: Check permissions and provide alternative approaches
- **Malformed Existing Changelog**: Attempt repair or request manual intervention
- **Link Generation Failure**: Provide manual link format instructions

?? **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol (propose changes, get approval, then execute)
- NEVER modify files without user approval
- ALWAYS preserve existing changelog structure
- ALWAYS generate clickable markdown links
- ALWAYS create detail files using template structure
- ALWAYS add entries in reverse chronological order within date sections

