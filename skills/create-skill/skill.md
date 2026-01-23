---
name: create-skill
description: Create a new skill with proper structure and templates. Use when user says "create a skill", "make a skill for...", or wants to build a reusable agent capability.
argument-hint: "[goal] - describe what the skill should do"
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
You MUST request these parameters if not provided by the user. Present them in this logical order:

**Start with the idea:**
1. **goal**: string - What should this skill do? What's the purpose? (REQUIRED)

**Then name and classify it:**
2. **skill_name**: string - What should we call it? (max 4 words, kebab-case) (OPTIONAL - will suggest based on goal)
3. **skill_type**: string - Type: "orchestrator", "workflow", "prompt" (OPTIONAL - default: "prompt")

**Then determine what it needs:**
4. **needs_templates**: boolean - Does it need external template files? (OPTIONAL - default: false)
5. **needs_tools**: boolean - Does it need tool/script files? (OPTIONAL - default: false)
6. **needs_kb**: boolean - Does it need knowledge base articles? (OPTIONAL - default: false)

**Finally, where to save it:**
7. **skills_root**: string - Destination folder for skills (OPTIONAL - will auto-detect)

## User Interaction
- Always ask for user approval before creating or modifying files

## Process

**CRITICAL ENTRY POINT**: When this skill is invoked, you MUST immediately ask for the **goal** parameter if not provided. Do NOT ask multiple questions at once. Follow the Input Parameters order strictly — one question at a time, waiting for user response before proceeding.

### 0. Parameter Collection Phase
You MUST collect parameters in this exact order, one at a time:

1. **First, ask for goal** (REQUIRED): "What should this skill do? What's the purpose?"
   - Wait for user response before continuing
   
2. **Then suggest a name**: Based on the goal, propose a skill name (kebab-case, max 4 words)
   - Ask: "Based on your goal, I suggest naming it `[suggested-name]`. Does that work, or would you prefer something else?"
   
3. **Then determine skill type**: Ask which type fits best
   - Ask: "What type of skill is this? (prompt / workflow / orchestrator) — default is 'prompt'"

4. **Then ask about components**: Ask about each component need
   - Ask: "Does this skill need any of these? (answer yes/no for each)"
     - Templates (external template files)?
     - Tools (scripts/utilities)?
     - Knowledge base articles?

5. **Finally, determine save location**: Proceed to Phase 1.a

Only after collecting all parameters, proceed to validation.

### 1. Validation Phase
You MUST verify all requirements:
- Confirm user goal is clear and actionable
- Validate skill name follows kebab-case convention (max 4 words)
- Validate skill type selection (prompt/workflow/orchestrator)

### 1.a Skill Destination Phase
You MUST ask the user where to save the skill:

**Ask:** "Where should this skill be saved?"
1. **For me (all my repos)** - Save to user home directory
2. **For this repo (team)** - Save to workspace skills folders
3. **Specific tool only** - Save to one specific tool's folder

**If user chooses "For me (all my repos)":**
Ask which tools they use (can select multiple):
- Claude Code → `~/.claude/skills/[skill_name]/`
- Windsurf → `~/.windsurf/skills/[skill_name]/`
- Kiro → `~/.kiro/skills/[skill_name]/`
- GitHub Copilot → `~/.github/skills/[skill_name]/`

**If user chooses "For this repo (team)":**
Detect which tool folders exist in workspace and ask which to target (can select "all"):
- `.claude/skills/`
- `.windsurf/skills/`
- `.kiro/skills/`
- `.github/skills/`
- `agents/skills/`

If user says "all", save to all detected folders.

**If user chooses "Specific tool only":**
Ask which tool and save to that folder only.

**Duplicate Check:**
Before creating, check if `[skill_name]/` exists in any target location.
If found, ask:
1. Pick a different name
2. Update existing skill
3. Overwrite (delete and recreate)

### 1.b Component Discovery Phase

**If needs_templates=true:**
Ask: "Provide links to the template files or describe what templates you need"
Templates go in `templates/` folder under the skill.

**If needs_tools=true:**
Ask: "Provide links to the tool/script files or describe what tools you need"
Prefer Python over shell scripts. Tools go in `tools/` folder.

**If needs_kb=true:**
Ask: "Provide links to the KB articles or describe what knowledge base content you need"
KB articles go in `kb/` folder.

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
- Generated skill presented for review with user approval
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
- **User Rejection During Review**: Request specific feedback and iterate
- **File Save Failures**: Provide alternative save methods and troubleshooting steps
- **Component File Creation Failed**: Show specific errors for templates/tools/helpers/kb creation
- **External Reference Validation Failed**: Ensure all referenced files exist and are accessible
- **Attempted Modification of Read-Only File**: Block operation, explain file is auto-generated, offer script execution