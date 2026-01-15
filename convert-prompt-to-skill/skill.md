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

## Input Parameters
You MUST request these parameters if not provided by the user:
- **existing_prompt_path**: string | string[] - Source prompt file path(s) (REQUIRED)
- **prompt_name**: string - New prompt name in kebab-case, 3-4 words (REQUIRED)
- **user_request**: string - Extra requirements or modifications to apply (OPTIONAL)
- **needs_templates**: boolean - Whether skill needs external template files (OPTIONAL - default: false)
- **template_list**: array - List of template names/descriptions if needs_templates=true (OPTIONAL)
- **needs_tools**: boolean - Whether skill needs tool/script files (OPTIONAL - default: false)
- **tool_list**: array - List of tool names/types if needs_tools=true (OPTIONAL)
- **needs_helpers**: boolean - Whether skill needs helper utility files (OPTIONAL - default: false)
- **helper_list**: array - List of helper names/descriptions if needs_helpers=true (OPTIONAL)
- **needs_kb**: boolean - Whether skill needs knowledge base articles (OPTIONAL - default: false)
- **kb_list**: array - List of kb article names/topics if needs_kb=true (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act for skill conversion due to high impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Verify all source file paths exist (array supported)
- Validate `prompt_name` matches `^[a-z]+(-[a-z]+){2,3}$` (3-4 words in kebab-case)
- Check `skills/` for existing skills with same name or similar functionality
- Ensure `templates/prompt-template.md` and `templates/prompting-principles.md` are readable
- Confirm `competencies/my-prompts/` exists
- Check access to required template and principles files from skill templates

### 1.b Component Discovery Phase
You WILL determine what optional components the user needs:

**Template Discovery:**
- Ask user: "Will your skill need external template files (separate from embedded templates in the prompt)?"
- If YES: "What templates will you need? (e.g., 'output-format.md', 'validation-checklist.md')"
- Explain: "External templates are referenced as `templates/name.md` and kept separate from prompt content"

**Tool Discovery:**
- Ask user: "Will your skill need tool/script files?"
- If YES: "What tools/scripts will you need? (e.g., 'analyzer.py', 'formatter.sh', 'validator.js')"
- Ask for tool type: python|shell|javascript|powershell

**Helper Discovery:**
- Ask user: "Will your skill need helper utility prompts?"
- If YES: "What helpers will you need? (e.g., 'input-validator.md', 'output-formatter.md')"
- Explain: "Helpers are reusable prompt fragments used by the main skill"

**Knowledge Base Discovery:**
- Ask user: "Will your skill need knowledge base articles?"
- If YES: "What KB articles will you need? (e.g., 'coding-standards.md', 'best-practices.md')"
- Ask for KB type: reference|specification|examples|data

### 2. Execution Phase

**Critical Knowledge Loading:**
<!-- <structure_schema> -->
You MUST read canonical structure reference: `skills/create-skill/kb/skill-structure-schema.md`
<!-- </structure_schema> -->

<!-- <file_safety_rules> -->
You MUST read file modification rules: `skills/create-skill/kb/file-modification-rules.md`
<!-- </file_safety_rules> -->

<!-- <skill_schema> -->
You MUST read and validate against: `.olaf/schemas/olaf-skill-manifest.schema.json`
<!-- </skill_schema> -->

<!-- <competency_schema> -->
You MUST read and validate against: `.olaf/schemas/olaf-competency-manifest.schema.json`
<!-- </competency_schema> -->

**Source Analysis:**
- Read and analyze all source files
- Extract purpose, inputs, workflow, outputs, rules/constraints, success criteria, error handling
- If multiple sources: identify common patterns, merge complementary parts, resolve conflicts, preserve best practices

**Template & Principles Loading:**
<!-- <template_analysis> -->
You MUST read and analyze: `templates/prompt-template.md`
<!-- </template_analysis> -->

<!-- <principles_analysis> -->
You MUST read and apply: `templates/prompting-principles.md`
<!-- </principles_analysis> -->

**Core Logic**: You WILL execute following protocol requirements
- You MUST apply Propose-Confirm-Act protocol for user approval
- You WILL generate structured skill following template structure exactly:
  - Skill manifest with proper metadata and complete BOM
  - Main prompt file following prompt template structure with EXTERNAL references only
  - Documentation structure (description.md, tutorial.md)
  - Optional component files based on user requirements
  - Proper folder organization under `skills/[prompt_name]/`
- You MUST use imperative language throughout ("You WILL", "You MUST")
- You WILL include XML markup for complex sections
- You MUST ensure generated skill includes comprehensive error handling
- You WILL validate generated skill includes all required template sections
- **CRITICAL**: Generated prompts must reference external files, NOT embed template content
- **TEMPLATE SEPARATION**: If user needs templates, create separate files and reference them as `templates/name.md`

### 2.b Skill Structure Generation Phase
You WILL scaffold the complete skill structure:

**Create Skill Directory Structure:**
- Create base folder: `skills/[prompt_name]/`
- Create required subdirectories:
  - `prompts/` - Main skill prompt and any workflows
  - `docs/` - Skill documentation
- Create optional subdirectories based on user requirements:
  - `templates/` - External template files (only if needs_templates=true)
  - `tools/` - Tools/scripts (only if needs_tools=true)
  - `kb/` - Knowledge base articles (only if needs_kb=true)
  - `helpers/` - Helper utilities (only if needs_helpers=true)

**Generate Core Files:**
- Create main prompt: `prompts/[prompt_name].md` using skill template structure
- Generate `skill-manifest.json` with complete BOM including all user-requested components
- Create `docs/description.md` with skill overview and usage
- Create `docs/tutorial.md` using step-by-step template

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

### 3. Registration Phase (my-prompts)
You WILL assign the skill to my-prompts competency:

**CRITICAL**: Follow file modification rules from knowledge base - competency index is READ-ONLY

- Read competency manifest: `competencies/my-prompts/competency-manifest.json`
- Add skill reference to the competency's skills array (✅ SAFE - direct edit)
- Update competency manifest file following schema
- ❌ NEVER directly edit query-competency-index.md (auto-generated)

**Competency Manifest Update:**
**CRITICAL**: Update manifest following `.olaf/schemas/olaf-competency-manifest.schema.json`
- Add skill entry to competency's skills array per schema
- Include required fields: id, path, description, patterns, protocol
- Include skill metadata (name, description, tags, patterns, protocol)
- Validate competency manifest against schema after update
- Ensure all field types and structures match schema requirements

### 4. Skills Registry Update Phase
**CRITICAL FILE SAFETY**: query-competency-index.md is READ-ONLY (auto-generated)

You MUST follow file modification rules from knowledge base:

**Safe Operations (Direct Edit):**
- ✅ Competency manifest already updated in Phase 3
- ✅ Skill files created in new skill directory
- ✅ Any manual skill registries (check for auto-generated markers)

**Read-Only Operations (Script Required):**
- ❌ NEVER directly edit query-competency-index.md
- ❌ NEVER directly edit olaf-framework-condensed.md
- ❌ NEVER modify files with AUTO-GENERATED markers
- ✅ OFFER to run regeneration scripts instead

**Detection of Auto-Generated Files:**
- Check file headers for `<!-- AUTO-GENERATED -->` marker
- Known read-only: query-competency-index.md, olaf-framework-condensed.md
- If uncertain, check against file-modification-rules.md

### 5. Reindexing Proposal Phase
**CRITICAL**: query-competency-index.md is READ-ONLY and MUST NOT be edited directly

You MUST offer script execution, NOT direct file modification:

**Reindexing Offer:**
Present to user:
```
✅ Skill created successfully from source prompt(s)!
✅ Competency manifest updated with new skill reference

Next step: Regenerate competency index to make your skill discoverable?

The query-competency-index.md is auto-generated and needs regeneration.
This will run: python scripts/select_collection.py --collection [collection]

Ready to regenerate? (yes/no)
```

**User Education:**
Explain why we use script instead of direct edit:
```
Note: The competency index (query-competency-index.md) is auto-generated.
Direct edits would be lost on next regeneration.

We've updated the competency manifest (source of truth).
Now we need to regenerate the index from all manifests.
```

**Reindexing Execution:**
If user agrees:
- Run: `python .olaf/scripts/select_collection.py --collection [user_collection]`
- User's active collection will be used (script handles defaults if not specified)
- Wait for script completion
- Validate that pattern markers are still intact in condensed framework
- Confirm new skill pattern is now in condensed framework

### 6. Validation Phase
You WILL validate the generated skill meets all requirements:
- **SCHEMA VALIDATION**: Validate skill manifest against `.olaf/schemas/olaf-skill-manifest.schema.json`
- **SCHEMA VALIDATION**: Validate competency manifest against `.olaf/schemas/olaf-competency-manifest.schema.json`
- Conforms to skill manifest schema completely (all required fields, correct types, valid patterns)
- Follows proper skills directory structure from `/kb/skill-structure-schema.md`
- Uses imperative language consistently throughout main prompt
- Includes comprehensive error handling scenarios
- Has measurable success criteria
- Contains proper XML markup where appropriate
- All BOM paths are valid and relative to skill root (start with `/`)
- All files referenced in BOM actually exist
- Original intent and functionality preserved from source prompt(s)

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete skill with all files and proper structure
- Validation checklist: Compliance verification against schema and principles
- Source comparison: Brief analysis of improvements vs. original source(s)
- Skill location specification: `skills/[prompt_name]/`

## Success Criteria
You WILL consider the task complete when:
- [ ] All source file paths validated and analyzed
- [ ] Component requirements discovered and confirmed with user
- [ ] Prompt name validated (3-4 words, kebab-case)
- [ ] Template and principles files successfully loaded and analyzed
- [ ] Duplicate check completed in skills directory (no conflicts found)
- [ ] Complete skill structure generated following architecture
- [ ] All requested component files created (templates, tools, helpers, kb)
- [ ] Main prompt references external files correctly (no embedded templates)
- [ ] Skill manifest validates against schema with complete BOM
- [ ] Skill assigned to my-prompts competency (manifest updated)
- [ ] User approval obtained via Propose-Confirm-Act protocol
- [ ] All files saved successfully in correct skills directory structure
- [ ] Generated skill includes all critical sections (error handling, success criteria, etc.)
- [ ] BOM properly populated with all user-requested components
- [ ] All external file references have corresponding actual files
- [ ] Original functionality preserved from source prompt(s)
- [ ] Improvements documented and explained to user
- [ ] Reindexing offered and completed if user agreed
- [ ] Skill can be discovered and invoked through OLAF framework

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Generated skill MUST follow skills architecture from `/kb/skill-structure-schema.md`
- Rule 2: **SCHEMA COMPLIANCE**: Skill manifest MUST validate against `.olaf/schemas/olaf-skill-manifest.schema.json`
- Rule 2b: **SCHEMA COMPLIANCE**: Competency manifest updates MUST validate against `.olaf/schemas/olaf-competency-manifest.schema.json`
- Rule 3: Generated prompt MUST use imperative language consistently
- Rule 4: Generated skill MUST include comprehensive error handling
- Rule 5: Skill name MUST be kebab-case, 3-4 words
- Rule 6: Generated skill MUST include measurable success criteria
- Rule 7: Skill directory MUST be created under `skills/`
- Rule 8: All BOM paths MUST be relative to skill root and start with `/`
- Rule 9: **CRITICAL**: Main prompt MUST reference external files, NOT embed template content
- Rule 10: **TEMPLATE SEPARATION**: Templates must be separate files in `templates/`, not embedded in prompt
- Rule 11: Component files MUST only be created if user explicitly requests them
- Rule 12: All generated external references MUST have corresponding files created
- Rule 13: **FILE SAFETY**: Follow modification rules from `/kb/file-modification-rules.md` - NEVER edit auto-generated files
- Rule 14: **READ-ONLY FILES**: query-competency-index.md and olaf-framework-condensed.md are auto-generated - offer script execution instead
- Rule 15: **COMPETENCY UPDATES**: Only modify competency manifests directly, regenerate indexes via scripts
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
- **Invalid Prompt Name**: Re-request valid kebab-case name (3-4 words)
- **Skills Directory Access Failed**: Provide error message and troubleshooting steps
- **Template/Principles File Access Failed**: Try fallback locations, provide error if all fail
- **Duplicate Skill Found**: Present existing skill and ask for modification preferences
- **Component Requirements Unclear**: Ask specific questions about each component type needed
- **Template Separation Issues**: Guide user to separate embedded templates from external references
- **Schema Validation Failed**: Show specific validation errors and correct manifest
- **User Rejection During Propose-Confirm-Act**: Request specific feedback and iterate
- **File Save Failures**: Provide alternative save methods and troubleshooting steps
- **Component File Creation Failed**: Show specific errors for templates/tools/helpers/kb creation
- **BOM Population Failed**: Validate all component paths and regenerate BOM
- **External Reference Validation Failed**: Ensure all referenced files exist and are accessible
- **Skills Registry Update Failed**: Inform user and provide manual update instructions
- **Reindexing Script Not Found**: Provide alternate path suggestions and manual reindexing instructions
- **Reindexing Script Execution Failed**: Show error output and troubleshooting steps
- **Attempted Modification of Read-Only File**: Block operation, explain file is auto-generated, offer script execution
- **Auto-Generated File Detection Failed**: Default to safe mode - offer script execution for any index/condensed files
- **Source Analysis Failed**: Request clarification or alternate source files

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol for all skill conversion
- MANDATORY: Generated skills MUST follow skills architecture exactly
- MANDATORY: Ask user about component needs - never assume what they want
- MANDATORY: Separate external templates from embedded templates in prompts
- MANDATORY: NEVER modify original source file(s)
- NEVER generate skills that don't validate against the schema
- NEVER skip validation phase - all generated skills must be verified
- NEVER embed template content in prompts - always use external file references
- NEVER create component files without user explicitly requesting them
- ALWAYS ensure generated skills include comprehensive error handling
- ALWAYS validate that generated skills include measurable success criteria
- ALWAYS create actual files for all external references in the prompt
- ALWAYS populate complete BOM with all user-requested components
- ALWAYS use relative paths starting with `/` in BOM manifest
- ALWAYS preserve original functionality from source prompt(s)
- NEVER save skills without explicit user approval
