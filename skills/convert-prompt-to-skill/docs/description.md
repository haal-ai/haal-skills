# Convert Prompt to Skill

## Overview

Convert Prompt to Skill transforms existing prompt files (legacy prompts, external prompts, ad-hoc documents) into properly structured OLAF skills. It preserves the original intent while restructuring content into a single `skill.md` entry point with documentation and optional component folders.

## Purpose

Teams often have valuable prompts that are not written as OLAF skills, missing clear input parameters and success criteria, or embedding templates inline instead of referencing external files. This skill provides a repeatable conversion workflow to ensure your skill library stays consistent and maintainable.

## Key Features

### 1. Multi-Source Support
- Single prompt file conversion
- Multiple prompt files merged into one skill
- Direct paste of prompt content
- Preserves original files (never modified)

### 2. Intelligent Analysis
- Extracts purpose, inputs, workflow, outputs from source
- Detects implied components (templates, tools, helpers, kb)
- Identifies common patterns and best practices
- Proposes skill name based on analysis

### 3. OLAF-Compliant Output
- Follows skill template structure exactly
- Uses imperative language throughout
- Includes comprehensive error handling
- Has measurable success criteria
- References external files (no embedded templates)

### 4. Component Support
- Optional templates folder for structured outputs
- Optional tools folder for scripts and utilities
- Optional helpers folder for reusable prompt fragments
- Optional kb folder for knowledge base articles

### 5. Plugin Integration
- Validates target plugin exists or creates it
- Updates `.olaf/plugins.json` automatically
- Adds plugin to skill metadata

### 6. Duplicate Detection
- Checks all supported skill roots for conflicts
- Prevents accidental overwrites
- Offers update-in-place or rename options

## Usage

**Command**: `convert prompt to skill`

**When to Use**: Use this skill when you want to create a new skill from existing prompt material rather than starting from scratch. Ideal for importing external prompts, modernizing legacy prompts, or consolidating multiple related prompts.

## Parameters

### Required Inputs (one of):
- **existing_prompt_path**: Path or list of paths to source prompt file(s)
- **source_text**: Copy/paste of the prompt content

### Required Inputs:
- **target_plugin**: Plugin name to assign the created skill to

### Optional Inputs
- **skill_name**: New skill folder name (kebab-case, max 4 words)
- **agent_runtime**: One of: "windsurf", "cascade", "github-copilot", "claude-code", "other"
- **skills_root**: Explicit destination root folder for skills
- **user_request**: Extra requirements or modifications to apply during conversion
- **needs_templates**: Whether skill needs external template files (default: false)
- **template_list**: List of template names if needs_templates=true
- **needs_tools**: Whether skill needs tool/script files (default: false)
- **tool_list**: List of tool names if needs_tools=true
- **needs_helpers**: Whether skill needs helper utility files (default: false)
- **helper_list**: List of helper names if needs_helpers=true
- **needs_kb**: Whether skill needs knowledge base articles (default: false)
- **kb_list**: List of kb article names if needs_kb=true

### Context Requirements
- Access to source prompt file(s) or pasted content
- Access to skill templates and prompting principles
- Write access to skills directory
- Terminal access for operations

## Output

**Deliverables**:
- New skill folder at `${skills_root}/[skill_name]/`
- Main skill prompt (`skill.md`) following OLAF template
- Documentation files (`docs/description.md`, `docs/tutorial.md`)
- Optional component folders (templates/, tools/, helpers/, kb/)
- Plugin assignment in `.olaf/plugins.json`
- Validation checklist confirming compliance

**Format**: Complete skill package with proper directory structure

## Examples

### Example 1: Single File Conversion

**Input**:
```
existing_prompt_path: prompts/legacy-code-review.md
target_plugin: code-quality
```

**Output**:
```
[skills_root]/review-code-legacy/
├── skill.md
├── docs/
│   ├── description.md
│   └── tutorial.md
```

### Example 2: Multiple Files Merged

**Input**:
```
existing_prompt_path: ["prompts/analyze-part1.md", "prompts/analyze-part2.md"]
skill_name: "analyze-comprehensive"
target_plugin: "analysis"
```

**Output**:
Single skill combining functionality from both source files.

### Example 3: Pasted Content with Components

**Input**:
```
source_text: [pasted prompt content]
skill_name: "generate-reports"
target_plugin: "reporting"
needs_templates: true
template_list: ["report-template", "summary-template"]
```

**Output**:
```
[skills_root]/generate-reports/
├── skill.md
├── docs/
│   ├── description.md
│   └── tutorial.md
├── templates/
│   ├── report-template.md
│   └── summary-template.md
```

## Conversion Process

### Phase 1: Source Analysis
1. Read and analyze prompt content
2. Extract purpose, inputs, workflow, outputs
3. Detect implied components
4. Propose skill name if not provided

### Phase 2: Missing Information Collection
1. Confirm/override proposed skill name
2. Get target plugin
3. Confirm component needs

### Phase 3: Skill Generation
1. Load skill template and prompting principles
2. Generate skill.md with proper structure
3. Create documentation files
4. Create component files if requested

### Phase 4: Validation
1. Verify directory structure
2. Check imperative language usage
3. Validate error handling
4. Confirm success criteria
5. Verify external references

## Related Skills

- **create-skill**: Create new skills from scratch (no source prompt)
- **check-prompt-compliance**: Validate converted skill quality
- **evaluate-prompt-for-adoption**: Assess external prompts before converting

## Tips & Best Practices

1. **Analyze first**: Let the skill analyze the source before providing component requirements
2. **Preserve intent**: Review converted skill to ensure original functionality preserved
3. **Check compliance**: Run check-prompt-compliance after conversion
4. **Test thoroughly**: Test the converted skill before publishing
5. **Keep originals**: Source files are never modified, keep them for reference
6. **Merge wisely**: When merging multiple files, ensure they're truly related
7. **Document changes**: Note any modifications made during conversion

## Limitations

- Conversion quality depends on clarity of source prompt(s)
- Some prompts may require follow-up iterations to clarify missing inputs/outputs
- Cannot automatically detect all implied components
- Complex domain-specific prompts may need manual refinement
- Original files are preserved but not automatically archived
- Cannot convert prompts that rely on external systems not available in OLAF

