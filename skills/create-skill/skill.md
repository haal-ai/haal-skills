---
name: create-skill
description: Generate structured skills following established template and principles for OLAF skills architecture
license: Apache-2.0
metadata:
  olaf_tags: [skill, generation, engineering, template, prompt-engineer]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

If you are in need to get the date and time, you MUST use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present  it as a numbered list to ease user response:
1. **user_request**: string - The user's requirement or task description for the skill (REQUIRED)
2. **skill_name**: string - Desired name for the skill (max 4 words, kebab-case) (OPTIONAL)
3. **skill_type**: string - Type of skill: "orchestrator", "workflow", "prompt" (OPTIONAL - default: "prompt")
4. **target_plugin**: string - Plugin name to assign the skill to (REQUIRED)
5. **agent_runtime**: string - One of: "windsurf", "cascade", "github-copilot", "claude-code", "other" (OPTIONAL - you SHOULD infer, else ask)
6. **skills_root**: string - Explicit destination root folder for skills, relative to workspace root (OPTIONAL - preferred when user knows it)
5. **needs_templates**: boolean - Whether skill needs external template files (OPTIONAL - default: false)
6. **template_list**: array - List of template names/descriptions if needs_templates=true (OPTIONAL)
7. **needs_tools**: boolean - Whether skill needs tool/script files (OPTIONAL - default: false)
8. **tool_list**: array - List of tool names/types if needs_tools=true (OPTIONAL)
9. **needs_helpers**: boolean - Whether skill needs helper utility files (OPTIONAL - default: false)
10. **helper_list**: array - List of helper names/descriptions if needs_helpers=true (OPTIONAL)
11. **needs_kb**: boolean - Whether skill needs knowledge base articles (OPTIONAL - default: false)
12. **kb_list**: array - List of kb article names/topics if needs_kb=true (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You MUST use Propose-Confirm-Act for skill creation

## Process

### 1. Validation Phase
You MUST verify all requirements:
- Confirm user request is clear and actionable
- Validate skill name follows kebab-case convention (max 4 words)
- Duplicate avoidance: you MUST check for a folder named `[skill_name]/` across ALL supported local skill roots:
  - `.windsurf/skills/[skill_name]/`
  - `.claude/skills/[skill_name]/`
  - `agents/skills/[skill_name]/`
  - AND the resolved `${skills_root}/[skill_name]/` (if different)
  If any exist, you MUST stop and ask the user what to do (numbered list):
  1. Pick a different `skill_name`, OR
  2. Choose which existing skill to update in place (preferred), OR
  3. Overwrite the chosen one (delete and recreate).
- Validate skill type selection (prompt/workflow/orchestrator)
- Validate target plugin: check if it exists in `.olaf/plugins.json` or add it if missing
- Check access to required templates, tools, helpers, kb articles, principles files for newskill

### 1.a Skill Location Discovery Phase
You WILL determine where to create the skill:

**Skill Location Discovery (Local Destination):**
- You MUST create skills locally in the user's workspace, under a skills root directory determined by the active agent runtime.
- You MUST determine `skills_root` using this priority order:
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

**Critical Save Rules:**
- Final destination for the new skill MUST be: `${skills_root}/[skill_name]/`
- Before creating files, you MUST check whether `${skills_root}/[skill_name]/` already exists.
- If it exists, you MUST stop and ask for an explicit choice (numbered list):
  1. Pick a different `skill_name`, OR
  2. Overwrite (delete and recreate), OR
  3. Update in place (preserve existing files; only add/modify what is necessary).
- You MUST NOT overwrite any existing skill folder without explicit user confirmation.

**Template Validation:**
- If needs_templates=true, ask user: "Provide links to the template files"
- Copy those to the  `templates/` folder under `[skill_name]/` so that they are available to the skill and kept separate from `skill.md`

**Tool Discovery:**
- if needs_tools=true, ask user: "Provide links to the tool/script files"
- Copy those to the  `tools/` folder under `[skill_name]/` so that they are available to the skill and kept separate from `skill.md`
- Ask for tool type: python|shell|javascript|powershell

**Helper Discovery:**
- if needs_helpers=true, ask user: "Provide links to the helper files"
- Copy those to the  `helpers/` folder under `[skill_name]/` so that they are available to the skill and kept separate from `skill.md`
- Explain: "Helpers are reusable prompt fragments used by the main skill"

**Knowledge Base Discovery:**
- if needs_kb=true, ask user: "Provide links to the KB articles"
- Copy those to the  `kb/` folder under `[skill_name]/` so that they are available to the skill and kept separate from `skill.md`

### 2. Execution Phase

**Critical Knowledge Loading:**
<!-- <structure_schema> -->
You MUST read in full the canonical structure reference: `create-skill/kb/skill-structure-schema.md` and strictly conform to it
<!-- </structure_schema> -->

**Template and Principles Loading:**
<!-- <template_analysis> -->
You MUST read in full and analyze: `templates/skill-template.md` 
<!-- </template_analysis> -->

<!-- <principles_analysis> -->
You MUST read in full and apply: `templates/prompting-principles.md`
<!-- </principles_analysis> -->

**Core Logic**: You WILL execute following requirements
- Ask for user approval before creating or modifying files
- You WILL generate structured skill following template structure exactly:
  - Main prompt `skill.md` file following the skill template structure with EXTERNAL references only
  - Documentation structure (description.md, tutorial.md)
  - Optional component files based on user requirements
  - Proper folder organization under `[skill-name]/`
- You MUST use imperative language throughout ("You WILL", "You MUST")
- You WILL include XML markup for complex sections
- You MUST ensure generated skill includes comprehensive error handling
- You WILL validate generated skill includes all required template sections
- **CRITICAL**: Generated prompts must reference external files, DO NOT / NEVER embed template content
- **TEMPLATE SEPARATION**: If user needs templates, create separate files and reference them as `templates/name.md`

### 2.b Skill Structure Generation Phase
You WILL scaffold the complete skill structure:

**Determine Skills Directory:**
- Use `skills_root` (resolved in Phase 1.a)
- Set `base_path = ${skills_root}/[skill_name]/` for all subsequent operations

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
- Create `docs/tutorial.md` using step-by-step template

**Generate Component Files (Based on User Requirements):**

**Templates (if needs_templates=true):**
For each template in template_list:
- Copy in `templates/` folder
- Add template reference in main prompt as: `Follow template: /templates/[template_name].md`

**Tools (if needs_tools=true):**
For each tool in tool_list:
- Copy in `tools/` folder
- Add tool reference in main prompt as: `Execute script: /tools/[tool_name].[extension]`

**Helpers (if needs_helpers=true):**
For each helper in helper_list:
- Copy in `helpers/` folder
- Add helper reference in main prompt as appropriate

**Knowledge Base (if needs_kb=true):**
For each kb article in kb_list:
- Copy in `kb/` folder
- Add KB reference in main prompt as: `Refer to: /kb/[kb_name].md`


### 3. Plugin Assignment Phase
**Simplified Plugin Assignment:**

1. **Check if plugins.json exists**:
   - Look for `.olaf/plugins.json`
   - If not found, create it with empty plugins array

2. **Validate target_plugin**:
   - If `target_plugin` exists in plugins.json → proceed
   - If `target_plugin` not in plugins.json → add it:
     ```json
     {
       "plugins": [
         "existing-plugin",
         "<target_plugin>"
       ]
     }
     ```

3. **Add to skill metadata**:
   - Add `plugins: <target_plugin>` to skill.md front matter metadata section


### 4. Validation Phase
You WILL validate the generated skill meets all requirements:
- Follows proper skills directory structure from `/kb/skill-structure-schema.md`
- Uses imperative language consistently throughout main prompt
- Includes comprehensive error handling scenarios
- Has measurable success criteria
- Contains proper XML markup where appropriate


## User Communication

### Progress Updates
- Confirmation when skill type and name are validated
- Confirmation of component requirements (templates, tools, helpers, kb)
- Status when skill directory structure is created
- Confirmation when templates and principles are successfully loaded
- Status of component file generation (templates, tools, helpers, kb)
- Status of duplicate check results in skills directory
- Validation results for generated skill structure
- Confirmation that all external references are properly created

### Completion Summary
- Generated skill presented for review via Propose-Confirm-Act
- Validation checklist results showing schema compliance
- Save location confirmation: 
  - `${skills_root}/[skill_name]/`

### Next Steps
You WILL clearly define:
- Skill ready for use (pending user approval)
- Skill location: 
  - `${skills_root}/[skill_name]/`
- Confirmation that skill meets all quality standards
- Instructions for invoking the new skill

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Generated skill MUST follow skills architecture from `/kb/skill-structure-schema.md`
- Rule 2: Generated skill MUST follow skills principles from `/templates/prompting-principles.md`
- Rule 3: Generated prompt MUST use imperative language consistently
- Rule 4: Generated skill MUST include comprehensive error handling
- Rule 5: Skill name MUST be kebab-case, max 4 words
- Rule 6: Generated skill MUST include measurable success criteria
- Rule 7: Skill directory MUST be created locally under the resolved skills root: `${skills_root}/[skill_name]/`
- Rule 8: **CRITICAL**: Main prompt MUST reference external files, NOT embed template content
- Rule 9: **TEMPLATE SEPARATION**: Templates must be separate files in `templates/`, not embedded in prompt
- Rule 10: Component files MUST only be created if user explicitly requests them
- Rule 11: All generated external references MUST have corresponding files created

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated and obtained
- [ ] Component requirements discovered and confirmed with user
- [ ] Skill type validated and skill name approved
- [ ] Skill location determined (local) and directories validated
- [ ] Template and principles files successfully loaded and analyzed
- [ ] Duplicate check completed in local skills directories (no conflicts found)
- [ ] Complete skill structure generated following architecture
- [ ] All requested component files created (templates, tools, helpers, kb)
- [ ] Main prompt references external files correctly (no embedded templates)
- [ ] Skill assigned to target plugin (plugins.json updated)
- [ ] Plugin added to skill metadata
- [ ] User approval obtained before creating files
- [ ] All files saved successfully in correct skills directory structure (local)
- [ ] Generated skill includes all critical sections (error handling, success criteria, etc.)
- [ ] All external file references have corresponding actual files

## Error Handling
You WILL handle these scenarios:
- **Missing/Unclear Requirements**: Request specific clarification with examples
- **Skills Directory Access Failed**: Provide error message and troubleshooting steps
- **Invalid Skill Name**: Re-request valid kebab-case name (max 4 words)
- **Template/Principles File Access Failed**: Try fallback locations, provide error if all fail
- **Duplicate Skill Found**: Present existing skill and ask for modification preferences
- **Component Requirements Unclear**: Ask specific questions about each component type needed
- **Template Separation Issues**: Guide user to separate embedded templates from external references
- **User Rejection During Propose-Confirm-Act**: Request specific feedback and iterate
- **File Save Failures**: Provide alternative save methods and troubleshooting steps
- **Component File Creation Failed**: Show specific errors for templates/tools/helpers/kb creation
- **External Reference Validation Failed**: Ensure all referenced files exist and are accessible
- **Attempted Modification of Read-Only File**: Block operation, explain file is auto-generated, offer script execution


