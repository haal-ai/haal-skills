---
name: convert-prompt-to-skill
description: Create a structured skill from existing prompt file(s) using OLAF templates and principles
license: Apache-2.0
metadata:
  olaf_tags: [prompt, conversion, refactor, template, generation, skill]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response.
1. **existing_prompt_path**: string | string[] - Source prompt file path(s) (REQUIRED if source_text not provided)
2. **source_text**: string - Copy/paste of the prompt content (REQUIRED if existing_prompt_path not provided)
3. **skill_name**: string - New skill name in kebab-case, max 4 words (OPTIONAL - you SHOULD propose based on analysis)
4. **target_plugin**: string - Plugin name to assign the new skill to (REQUIRED)
5. **agent_runtime**: string - One of: "windsurf", "cascade", "github-copilot", "claude-code", "other" (OPTIONAL - you SHOULD infer, else ask)
6. **skills_root**: string - Explicit destination root folder for skills, relative to workspace root (OPTIONAL - preferred when user knows it)
5. **user_request**: string - Extra requirements or modifications to apply during conversion (OPTIONAL)
6. **needs_templates**: boolean - Whether skill needs external template files (OPTIONAL - default: false)
7. **template_list**: array - List of template names/descriptions if needs_templates=true (OPTIONAL)
8. **needs_tools**: boolean - Whether skill needs tool/script files (OPTIONAL - default: false)
9.  **tool_list**: array - List of tool names/types if needs_tools=true (OPTIONAL)
10. **needs_helpers**: boolean - Whether skill needs helper utility files (OPTIONAL - default: false)
11. **helper_list**: array - List of helper names/descriptions if needs_helpers=true (OPTIONAL)
12. **needs_kb**: boolean - Whether skill needs knowledge base articles (OPTIONAL - default: false)
13. **kb_list**: array - List of kb article names/topics if needs_kb=true (OPTIONAL)

## Skill Location Discovery (Local Destination)
You MUST determine where to create the converted skill BEFORE writing any files.

**Determine `skills_root` using this priority order:**
1. If user provided `skills_root`, you MUST use it.
2. Else you MUST infer `skills_root` from the workspace:
  - If `.windsurf/skills/` exists → use `.windsurf/skills`
  - Else if `.claude/skills/` exists → use `.claude/skills`
  - Else if `agents/skills/` exists → use `agents/skills`
  - Else you MUST ask the user to choose `agent_runtime` (numbered list) and set `skills_root` using the mapping below.
3. If you must rely on `agent_runtime`, use this mapping:
  - `windsurf` or `cascade` → `.windsurf/skills`
  - `github-copilot` or `claude-code` → `.claude/skills`
  - `other` → `agents/skills`

**Prior-Presence Check (Mandatory):**
- Final destination MUST be: `${skills_root}/[skill_name]/`
- Before creating files, you MUST check whether `${skills_root}/[skill_name]/` already exists.
- If it exists, you MUST stop and ask for an explicit choice (numbered list):
  1. Pick a different `skill_name`, OR
  2. Overwrite (delete and recreate), OR
  3. Update in place (preserve existing files; only add/modify what is necessary).
- You MUST NOT overwrite any existing skill folder without explicit user confirmation.

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act for skill conversion due to high impact

## Process

### 0. Prompt Availability Phase
You MUST determine whether you already have the source prompt content available:

- If the prompt content is present in the conversation/context, you MUST use it as `source_text`.
- Else if `existing_prompt_path` is provided, you MUST read the file(s).
- Else you MUST ask the user for the prompt, using one of these options:
  1. Provide `existing_prompt_path` (file path), OR
  2. Paste `source_text` directly

You MUST NOT ask for optional/complementary information (components, templates, tools) until after you have analyzed the prompt.

### 1. Validation Phase
You WILL verify all requirements:
- Validate that at least one of `source_text` or `existing_prompt_path` is available
- If `existing_prompt_path` is provided, verify all source file paths exist (array supported)
- Ensure `templates/skill-template.md` and `templates/prompting-principles.md` are readable
- Duplicate avoidance: you MUST check for a folder named `[skill_name]/` across ALL supported local skill roots:
  - `.windsurf/skills/[skill_name]/`
  - `.claude/skills/[skill_name]/`
  - `agents/skills/[skill_name]/`
  - AND the resolved `${skills_root}/[skill_name]/` (if different)
  If any exist, you MUST stop and ask the user what to do (numbered list):
  1. Pick a different `skill_name`, OR
  2. Choose which existing skill to update in place (preferred), OR
  3. Overwrite the chosen one (delete and recreate).

### 1.b Source Analysis Phase
You MUST analyze the prompt thoroughly BEFORE asking for complementary information.

**Source Analysis:**
- Read and analyze the prompt content (from `source_text` and/or `existing_prompt_path`)
- Extract purpose, inputs, workflow, outputs, rules/constraints, success criteria, error handling
- Detect likely components implied by the prompt:
  - templates (explicit output schemas, structured output formats)
  - tools (scripts/commands the prompt requires)
  - helpers (reusable sub-prompts / repeated instructions)
  - kb (domain reference material)
- If multiple sources: identify common patterns, merge complementary parts, resolve conflicts, preserve best practices

**Derived Proposal (from analysis):**
- You SHOULD propose a `skill_name` (kebab-case, max 4 words) if not provided
- You SHOULD propose defaults for needs_templates/tools/helpers/kb based on what the prompt actually requires

### 1.c Missing Information Collection Phase
After analysis, you MUST ask ONLY for what is missing.

Examples of what you may still need to ask:
1. `target_plugin` (required)
2. Confirm/override the proposed `skill_name`
3. Confirm/override inferred component needs and lists

When asking questions, ALWAYS use numbered lists.

### 2. Execution Phase

**Critical Knowledge Loading:**
<!-- <structure_schema> -->
You MUST read canonical structure reference: `kb/skill-structure-schema.md`
<!-- </structure_schema> -->


**NOTE**: Source analysis MUST have already been completed in Phase 1.b before proceeding.

**Template & Principles Loading:**
<!-- <template_analysis> -->
You MUST read and analyze: `templates/skill-template.md`
<!-- </template_analysis> -->

<!-- <principles_analysis> -->
You MUST read and apply: `templates/prompting-principles.md`
<!-- </principles_analysis> -->

**Core Logic**: You WILL execute following protocol requirements
- You MUST apply Propose-Confirm-Act protocol for user approval
- You WILL generate structured skill following template structure exactly:
  - New skill folder at: `${skills_root}/[skill_name]/`
  - Main prompt file: `skill.md` following skill template structure with EXTERNAL references only
  - Documentation structure (`docs/description.md`, `docs/tutorial.md`)
  - Optional component files based on user requirements
- You MUST use imperative language throughout ("You WILL", "You MUST")
- You WILL include XML markup for complex sections
- You MUST ensure generated skill includes comprehensive error handling
- You WILL validate generated skill incl  udes all required template sections
- **CRITICAL**: Generated prompts must reference external files, NOT embed template content
- **TEMPLATE SEPARATION**: If user needs templates, create separate files and reference them as `templates/name.md`

### 2.b Skill Structure Generation Phase
You WILL scaffold the complete skill structure:

**Create Skill Directory Structure:**
- Create base folder: `${skills_root}/[skill_name]/`
- Create required subdirectories:
  - `docs/` - Skill documentation
- Create optional subdirectories based on user requirements:
  - `templates/` - External template files (only if needs_templates=true)
  - `tools/` - Tools/scripts (only if needs_tools=true)
  - `kb/` - Knowledge base articles (only if needs_kb=true)
  - `helpers/` - Helper utilities (only if needs_helpers=true)

**Generate Core Files:**
- Create main prompt: `skill.md` using skill template structure
- Create `docs/description.md` with skill overview and usage
- Create `docs/tutorial.md` with step-by-step usage for this converted skill

**Generate Component Files (Based on User Requirements):**

**Templates (if needs_templates=true):**
For each template in template_list:
- Create skeleton template file: `templates/[template_name].md`
- Include template structure with placeholders
- Add template reference in main prompt as: `Follow template: /templates/[template_name].md`

**Tools (if needs_tools=true):**
For each tool in tool_list:
- Create skeleton tool file: `tools/[tool_name].[extension]`
- Include basic tool structure for the specified type (python/shell/javascript/powershell)
- Add tool reference in main prompt as: `Execute script: /tools/[tool_name].[extension]`

**Helpers (if needs_helpers=true):**
For each helper in helper_list:
- Create skeleton helper file: `helpers/[helper_name].md`
- Include basic helper prompt structure
- Add helper reference in main prompt as appropriate

**Knowledge Base (if needs_kb=true):**
For each kb article in kb_list:
- Create skeleton KB file: `kb/[kb_name].md`
- Include KB article structure based on type (reference/specification/examples/data)
- Add KB reference in main prompt as: `Refer to: /kb/[kb_name].md`

### 3. Plugin Assignment Phase
You WILL assign the new skill to a plugin:

1. Check if `.olaf/plugins.json` exists
  - If not found, create it with an empty plugins array
2. Validate `target_plugin`
  - If `target_plugin` exists in plugins.json → proceed
  - If missing → add it to the plugins array
3. Add plugin to the new skill metadata
  - Add `plugins: [target_plugin]` to the new skill `skill.md` frontmatter metadata

### 4. Validation Phase
You WILL validate the generated skill meets all requirements:
- Follows proper skill directory structure from `kb/skill-structure-schema.md`
- Uses imperative language consistently throughout main prompt
- Includes comprehensive error handling scenarios
- Has measurable success criteria
- Contains proper XML markup where appropriate
- Any optional component directories only exist if explicitly requested
- All external references in `skill.md` have corresponding files created
- Skill name is kebab-case, max 4 words
## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete skill with all files and proper structure
 Validation checklist: Compliance verification against structure and principles
- Source comparison: Brief analysis of improvements vs. original source(s)
- Skill location specification: `${skills_root}/[skill_name]/`

## Success Criteria
You WILL consider the task complete when:
- [ ] Prompt content obtained (path or paste) and analyzed thoroughly
- [ ] Missing information requested (only what analysis could not infer)
- [ ] `skill_name` validated (kebab-case, max 4 words)
- [ ] `target_plugin` validated and recorded
- [ ] Template and principles files successfully loaded and applied
- [ ] Duplicate check completed (no conflicting skill folder name)
- [ ] Complete skill structure generated following architecture
- [ ] All requested component files created (templates, tools, helpers, kb)
- [ ] Main prompt references external files correctly (no embedded templates)
- [ ] Plugin assignment completed (`.olaf/plugins.json` and `skill.md` metadata)
- [ ] User approval obtained via Propose-Confirm-Act protocol
- [ ] All files saved successfully in the new skill folder
- [ ] Generated skill includes all critical sections (error handling, success criteria, etc.)
- [ ] All external file references have corresponding actual files
- [ ] Original functionality preserved from source prompt(s)
- [ ] Improvements documented and explained to user
- [ ] Skill can be discovered and invoked through OLAF framework

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Generated skill MUST follow skills architecture from `kb/skill-structure-schema.md`
- Rule 3: Generated prompt MUST use imperative language consistently
- Rule 4: Generated skill MUST include comprehensive error handling
- Rule 5: Skill name MUST be kebab-case, 3-4 words
- Rule 6: Generated skill MUST include measurable success criteria
- Rule 7: Skill directory MUST be created locally under the resolved skills root: `${skills_root}/[skill_name]/`
- Rule 9: **CRITICAL**: Main prompt MUST reference external files, NOT embed template content
- Rule 10: **TEMPLATE SEPARATION**: Templates must be separate files in `templates/`, not embedded in prompt
- Rule 11: Component files MUST only be created if user explicitly requests them
- Rule 12: All generated external references MUST have corresponding files created
- Rule 16: **SOURCE PRESERVATION**: NEVER modify original source file(s)
- Rule 17: **FUNCTIONALITY PRESERVATION**: Original intent and functionality must be preserved

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute operations following Propose-Confirm-Act protocol
3. Generate outputs in specified format
4. Provide user communication and confirmations
5. Define next steps for skill usage

## Error Handling
You WILL handle these scenarios:
- **Missing/Invalid Source Path(s)**: Request correct path(s) with examples
- **Invalid Skill Name**: Re-request valid kebab-case name (3-4 words)
- **Skill Folder Creation Failed**: Provide error message and troubleshooting steps
- **Template/Principles File Access Failed**: Try fallback locations, provide error if all fail
- **Duplicate Skill Found**: Present existing skill and ask for modification preferences
- **Component Requirements Unclear**: Ask specific questions about each component type needed
- **Template Separation Issues**: Guide user to separate embedded templates from external references
- **User Rejection During Propose-Confirm-Act**: Request specific feedback and iterate
- **File Save Failures**: Provide alternative save methods and troubleshooting steps
- **Component File Creation Failed**: Show specific errors for templates/tools/helpers/kb creation
- **External Reference Validation Failed**: Ensure all referenced files exist and are accessible

- **Source Analysis Failed**: Request clarification or alternate source files

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol for all skill conversion
- MANDATORY: Generated skills MUST follow skills architecture exactly
- MANDATORY: Ask user about component needs - never assume what they want
- MANDATORY: Separate external templates from embedded templates in prompts
- MANDATORY: NEVER modify original source file(s)
- NEVER skip validation phase - all generated skills must be verified
- NEVER embed template content in prompts - always use external file references
- NEVER create component files without user explicitly requesting them
- ALWAYS ensure generated skills include comprehensive error handling
- ALWAYS validate that generated skills include measurable success criteria
- ALWAYS create actual files for all external references in the prompt
- ALWAYS preserve original functionality from source prompt(s)
- NEVER save skills without explicit user approval
