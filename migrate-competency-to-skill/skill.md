---
name: migrate-competency-to-skill
description: Extract and migrate specific competency features from another branch and transform them into standalone skills
license: Apache-2.0
metadata:
  olaf_tags: [migration, competency, skill, git, transformation, architecture]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## User Interaction Protocol
1. **Parameter Collection**: Request all required migration parameters from user
2. **Source Analysis**: Analyze competency structure in source branch
3. **Migration Planning**: Present migration strategy for confirmation
4. **Skill Creation**: Execute migration following OLAF skill architecture
5. **Validation**: Test and validate migrated skill functionality

## Process

⚠️ **CRITICAL MIGRATION PROTOCOL**: You MUST follow this exact sequence. ANY deviation will result in migration failure.

### Phase 1: MANDATORY Pre-Migration Validation
1. **Parameter Validation**: Ensure all required migration parameters provided
2. **CRITICAL CONFLICT CHECK**: Check if target skill already exists - MUST complete before proceeding
3. **Source Verification**: Confirm competency exists in source branch  
4. **MANDATORY BRANCH CREATION**: Create temporary migration branch - NEVER work on main branch

### Phase 2: SAFE EXECUTION (Only After Phase 1 Complete)
1. **Git Safety Operations**: Work ONLY in temporary branch with read-only source extraction
2. **Structure Transformation**: Convert competency structure to skill architecture
3. **Schema Compliance**: Ensure adherence to olaf-skill-manifest.schema.json
4. **File Generation**: Create all required skill components

### Phase 3: MANDATORY GIT WORKFLOW COMPLETION
1. **Skill Testing**: Validate skill functionality and structure
2. **Schema Verification**: Confirm compliance with OLAF standards  
3. **MANDATORY BRANCH MERGE**: Complete proper git workflow with branch cleanup

## Input Parameters

**CRITICAL REQUIREMENT**: You MUST ask the USER to provide ALL required parameters below before proceeding. DO NOT assume or infer these parameters from context.

**Required Parameters (ALL must be provided by USER):**

- **source_branch**: string - Source branch containing the competency to migrate (e.g., "feature/olaf-feature-system")
- **competency_name**: string - Name of the competency package (e.g., "researcher")
- **feature_name**: string - Specific feature/skill within the competency to migrate (e.g., "search-and-learn")
- **target_skill_name**: string - Desired name for the new skill in kebab-case (e.g., "lean-and-search")

**Optional Parameters:**
- **description_override**: string - Override description for the new skill (if different from original)

**VALIDATION CHECKPOINT**: Before starting the Process section, verify you have explicit USER input for all required parameters. If ANY parameter is missing, ask the USER to provide it.

## Output Format
1. **Migration Log**: Detailed log of all migration steps and decisions
2. **Skill Structure**: Complete skill directory with all components
3. **Validation Report**: Schema compliance and functionality verification
4. **Documentation**: Updated skill manifest and usage instructions

## User Communication
- **Progress Updates**: Regular status updates during migration process
- **Parameter Requests**: Clear requests for missing required parameters
- **Validation Confirmations**: Present migration plan before execution
- **Error Reporting**: Clear communication of any migration issues

## Domain-Specific Rules
- **Git Safety**: Always create temporary branches for migration operations
- **Schema Compliance**: Ensure all skills follow olaf-skill-manifest.schema.json
- **File Structure**: Maintain OLAF skill architecture (prompts/, templates/, docs/, tools/)
- **Naming Convention**: Use kebab-case for skill names and proper manifest structure
- **Backup Strategy**: Preserve original competency in source branch

## Success Criteria
- All required parameters provided by user
- Source competency successfully extracted and analyzed
- New skill structure follows OLAF architecture
- Schema validation passes without errors
- Migrated skill is functional within OLAF framework

## Error Handling
- **Missing Parameters**: Stop and request missing information from user
- **Git Conflicts**: Create clean temporary branches for safe operations  
- **Schema Violations**: Fix compliance issues during migration
- **File Structure Issues**: Ensure proper OLAF skill directory organization

## CRITICAL ERROR PREVENTION

⚠️ **MANDATORY SAFEGUARDS**: These specific error scenarios MUST be prevented:

### NEVER SKIP CONFLICT CHECK
- **ERROR**: "Skill already exists but not detected"
- **PREVENTION**: ALWAYS check `skills/{target_skill_name}/` exists BEFORE any work
- **ENFORCEMENT**: If skill exists, STOP and ask USER for explicit decision

### NEVER WORK ON MAIN BRANCH
- **ERROR**: "Migration performed directly on working branch"  
- **PREVENTION**: ALWAYS create `temp-{target_skill_name}-migration` branch FIRST
- **ENFORCEMENT**: Verify branch creation successful before proceeding with any migration work

### NEVER SKIP GIT WORKFLOW
- **ERROR**: "No temporary branch cleanup performed"
- **PREVENTION**: ALWAYS complete full merge and branch deletion sequence
- **ENFORCEMENT**: Temporary branches MUST be merged back and deleted after migration

**VIOLATION CONSEQUENCE**: If ANY of these safeguards are bypassed, the migration is considered failed and must be corrected.

## Implementation Details

### CRITICAL FIRST STEP: Mandatory Pre-Migration Validations

⚠️ **MANDATORY ENFORCEMENT**: You MUST complete ALL validation steps below BEFORE proceeding with any migration work. Failure to follow this sequence will result in process failure.

### Step 1: Validate Source Branch and Competency

**1. MANDATORY: Check skill name conflicts FIRST**:
   - **CRITICAL**: Check if target skill already exists: `skills/{target_skill_name}/`
   - **IF SKILL EXISTS**: STOP immediately and present options to USER:
     - **STOP**: Cancel migration process (recommended)
     - **OVERRIDE**: Replace existing skill (DESTRUCTIVE - require explicit USER confirmation)
     - **RENAME**: Use different skill name (prompt for new name)
   - **IF RENAME chosen**: Validate new name doesn't conflict with existing skills
   - **MANDATORY**: Update target_skill_name parameter with final chosen name
   - **DO NOT PROCEED** until USER confirms action for existing skill conflict

**2. MANDATORY: Validate source branch and competency**:
   - List all branches to verify source branch exists
   - Switch to source branch temporarily to examine structure
   - Find competency manifest: `olaf-core/competencies/{competency_name}/competency-manifest.json`
   - Validate competency contains the specified feature
   - Document available features for user confirmation

**3. MANDATORY: Extract feature information**:
   - Get feature prompt file path and content
   - Get associated template files
   - Get associated tool files (Python scripts, executables, etc.)
   - Get documentation files
   - Note any dependencies or related files

### Step 2: MANDATORY Git Safety Protocol

⚠️ **CRITICAL**: You MUST create a temporary branch for all migration work. NEVER work directly on the main working branch.

**1. MANDATORY: Create temporary migration branch**:
   - **CRITICAL**: Switch back to current working branch FIRST
   - **MANDATORY**: Create temporary branch: `temp-{target_skill_name}-migration`
   - **VERIFY**: Confirm branch creation successful before proceeding
   - **SAFETY**: Extract feature files using `git show` command (read-only operation)

### Step 3: Transform to Skill Architecture

**ONLY PROCEED AFTER COMPLETING STEPS 1 & 2**

1. **Create skill directory structure**:
   - Create: `skills/{target_skill_name}/`
   - Create subdirectories: `prompts/`, `templates/`, `tools/`, `docs/`

2. **Adapt main prompt file**:
   - **FIRST**: Read the skill template structure from `templates/skill-template.md` in this skill directory
   - Transform competency prompt to skill format following the skill-template structure
   - Update metadata and frontmatter to match skill template format
   - Convert file references to use skills directory structure
   - **CRITICAL OUTPUT DIRECTORY UPDATE**: Change any output directory references to use `.olaf/work/staging/` instead of `findings_dir`, `output_dir`, or similar directories
   - Maintain all original functionality and validation rules
   - Ensure all sections from skill-template are present: Input Parameters, User Interaction Protocol, Process (3 phases), Output Format, User Communication, Domain-Specific Rules, Success Criteria, Error Handling

3. **Migrate template files**:
   - Copy and adapt template files to skills format (use the exact template from the source)
   - Update template references and paths
   - Maintain template structure and functionality

4. **Migrate tool files**:
   - Copy tool files (Python scripts, shell scripts, executables) to skills format
   - Update tool references and paths in prompt files
   - Maintain tool functionality and dependencies
   - Preserve file permissions for executable tools

5. **Create documentation**:
   - Generate comprehensive description.md and tutorial.md using the template: `templates/step-by-step-tutorial-template.md`
   - Follow step-by-step tutorial template structure for consistent tutorial documentation
   - Include examples and practical usage scenarios


### Step 4: Generate Skill Manifest
1. **Create compliant skill manifest**:
   - Follow schema: `schemas/olaf-skill-manifest.schema.json`
   - Include all required metadata fields
   - Generate proper aliases from original competency avoiding conflicts:
     - If skill was renamed, create unique aliases that don't conflict with existing skills
     - Check existing skills' aliases in `reference/query-competency-index.md`
     - Generate alternative phrasings and synonyms for the renamed skill
     - Ensure aliases reflect the new skill name while maintaining discoverability
   - Document all components in BOM (Bill of Materials)

2. **Validate manifest structure**:
   - Ensure `metadata` section compliance:
     - `id`: kebab-case format (verb-entity-complement)
     - `name`: Human-readable display name
     - `shortDescription`: One-line explanation (10-200 chars)
     - `objectives`: 1-5 skill objectives
     - `tags`: Relevant tags for persona and use cases
     - `status`: experimental|proven|mainstream|deprecated
     - `exposure`: export|internal|kernel
     - `version`: Semantic version (MAJOR.MINOR.PATCH)
     - `protocol`: Act|Propose-Act|Propose-Confirm-Act|Analyze-Report

   - Ensure `bom` section compliance:
     - `prompts`: Array with name, path, description
     - `templates`: Array with name, path, type (if applicable)
     - `tools`: Array with name, path, type, description (if applicable)
     - `docs`: Array with name, path, type (if applicable)
     - Validate path patterns match schema requirements

### Step 5: Schema Validation and Cleanup
1. **Validate skill manifest against schema**:
   - Check all required fields present
   - Verify pattern matching for id, version, paths
   - Ensure enum values are valid
   - Validate array constraints (minItems, maxItems)

2. **Test skill structure**:
   - Verify all referenced files exist
   - Check path consistency across manifest and file system
   - Ensure templates and tools reference correct skill paths
   - Verify tool file permissions are preserved

### Step 5: MANDATORY Git Workflow Completion

⚠️ **CRITICAL**: You MUST follow the complete git workflow for safe migration completion.

**3. MANDATORY: Complete git workflow with temporary branch**:
   - Add new skill to git: `git add skills/{target_skill_name}/`
   - Commit with descriptive message including migration source
   - **CRITICAL**: Switch back to original branch: `git checkout {original_branch}`
   - **MANDATORY**: Merge temporary branch: `git merge temp-{target_skill_name}-migration`
   - **CLEANUP**: Delete temporary branch: `git branch -d temp-{target_skill_name}-migration`
   - Clean up any temporary files used during extraction

### Step 6: Migration Summary
1. **Document migration process**:
   - Source competency and feature information
   - Files migrated and transformations applied
   - Schema compliance verification
   - Any limitations or manual adjustments needed

## Output Format

### Migration Report Structure:
```markdown
# Competency to Skill Migration Report: {target_skill_name}

**Generated**: {YYYYMMDD-HHmm} UTC
**Source Branch**: {source_branch}
**Source Competency**: {competency_name}
**Source Feature**: {feature_name}
**Target Skill**: {target_skill_name}

## Migration Summary
- **Files Migrated**: {count}
- **Components Created**: prompts, templates, tools, docs, manifest
- **Schema Compliance**: ✅ Validated against olaf-skill-manifest.schema.json
- **Status**: {Success|Partial|Failed}

## Source Analysis
### Original Competency Structure
[Details about source competency and feature]

### Feature Components
[List of files and components migrated]

## Transformation Applied
### Architecture Changes
[Competency to skill architecture adaptations]

### File Adaptations
[Specific changes made to prompt files, templates, etc.]

### Manifest Generation
[Skill manifest creation and schema compliance details]

## Skill Structure Created
```
{target_skill_name}/
├── skill-manifest.json
├── prompts/
│   └── {target_skill_name}.md
├── templates/
│   └── [template files]
├── tools/
│   └── [tool files: .py, .sh, executables]
└── docs/
    └── tutorial.md
```

## Next Steps
[Usage instructions and recommendations]
```

## Migration Rules

- **Rule 1**: Always validate source branch and competency existence before proceeding
- **Rule 2**: Maintain all original functionality when transforming to skill format
- **Rule 3**: Generate schema-compliant skill manifest with all required fields
- **Rule 4**: Update all file references to use skills directory structure including tools
- **Rule 5**: **CRITICAL OUTPUT STANDARDIZATION** - Always change output directory references to `.olaf/work/staging/` instead of `findings_dir`, `output_dir`, or other output folders
- **Rule 6**: Preserve tool file permissions and functionality during migration
- **Rule 7**: Create comprehensive documentation and tutorial
- **Rule 8**: Validate manifest against schema before completion
- **Rule 9**: Ensure complete git workflow: merge to original branch and delete temporary branch
- **Rule 10**: Clean up temporary files and branches after successful migration

## Error Handling

### Common Issues and Solutions:

1. **Skill name conflicts**:
   - Check if target skill directory already exists
   - Present conflict resolution options to user
   - If renaming, validate new name and generate appropriate aliases

2. **Source branch not found**:
2. **Source branch not found**:
   - List available branches for user selection
   - Verify branch name spelling and case sensitivity

3. **Competency not found**:
3. **Competency not found**:
   - List available competencies in source branch
   - Verify competency directory structure

4. **Feature not found in competency**:
4. **Feature not found in competency**:
   - List available features in competency manifest
   - Check alternative naming patterns

5. **Schema validation failure**:
   - Report specific validation errors
   - Provide correction suggestions
   - Allow manual manifest adjustment

5. **File reference conflicts**:
   - Document path conflicts and resolution for templates and tools
   - Update references systematically in prompt files
   - Verify all links work in new structure
   - Ensure tool paths are correctly updated

6. **Tool execution issues**:
   - Verify tool file permissions after migration
   - Test tool functionality in new directory structure
   - Update any hardcoded paths within tool files

7. **Output directory inconsistency**:
   - Scan prompt files for output directory references (findings_dir, output_dir, etc.)
   - Systematically replace with staging_dir for consistency
   - Update any template files that reference output directories
   - Ensure all skill outputs are directed to staging area

## Usage Example

```
olaf migrate-competency-to-skill
Source branch: feature/olaf-feature-system
Competency name: researcher  
Feature name: search-and-learn
Target skill name: lean-and-search
```

This will migrate the "search-and-learn" feature from the researcher competency on the feature/olaf-feature-system branch into a new "lean-and-search" skill with full schema compliance.

## Git Workflow Details

### Critical Git Operations Sequence
The migration process MUST follow this exact git workflow to ensure proper branch management:

1. **Initial State Capture**:
   ```bash
   # Record current branch
   ORIGINAL_BRANCH=$(git branch --show-current)
   
   # Ensure working directory is clean
   git status --porcelain
   ```

2. **Source Branch Validation**:
   ```bash
   # Verify source branch exists
   git branch -a | grep {source_branch}
   
   # Temporarily switch to source branch for validation
   git checkout {source_branch}
   # [Perform competency structure validation]
   git checkout $ORIGINAL_BRANCH
   ```

3. **Temporary Branch Creation**:
   ```bash
   # Create temporary migration branch from current state
   git checkout -b temp-{target_skill_name}-migration
   
   # Extract files using git show (no checkout needed)
   git show {source_branch}:path/to/source/file > temp_file
   ```

4. **Skill Creation and Commit**:
   ```bash
   # Create skill structure and files
   # [Perform all migration steps]
   
   # Stage new skill
   git add skills/{target_skill_name}/
   
   # Commit migration on temporary branch
   git commit -m "feat: migrate {feature_name} from {competency_name} competency
   
   - Source: {source_branch}:{competency_path}
   - Target: skills/{target_skill_name}/
   - Schema compliance: validated against olaf-skill-manifest.schema.json
   - Migration date: $(date -u +%Y-%m-%d)"
   ```

5. **Merge Back to Original Branch**:
   ```bash
   # Switch back to original branch
   git checkout $ORIGINAL_BRANCH
   
   # Merge temporary branch (fast-forward if possible)
   git merge temp-{target_skill_name}-migration
   
   # Verify merge success
   if [ $? -eq 0 ]; then
       echo "✅ Migration successfully merged to $ORIGINAL_BRANCH"
   else
       echo "❌ Merge failed - manual resolution required"
       exit 1
   fi
   ```

6. **Cleanup Temporary Branch**:
   ```bash
   # Delete temporary branch after successful merge
   git branch -d temp-{target_skill_name}-migration
   
   # Verify cleanup
   git branch | grep temp-{target_skill_name}-migration
   if [ $? -ne 0 ]; then
       echo "✅ Temporary branch successfully deleted"
   else
       echo "⚠️ Temporary branch still exists - manual cleanup needed"
   fi
   ```

7. **Final State Verification**:
   ```bash
   # Confirm we're back on original branch
   CURRENT_BRANCH=$(git branch --show-current)
   if [ "$CURRENT_BRANCH" = "$ORIGINAL_BRANCH" ]; then
       echo "✅ Returned to original branch: $ORIGINAL_BRANCH"
   else
       echo "❌ Branch mismatch - expected $ORIGINAL_BRANCH, got $CURRENT_BRANCH"
   fi
   
   # Verify skill structure exists
   ls -la skills/{target_skill_name}/
   ```

### Critical Safety Checks

**Before Starting Migration**:
- [ ] Working directory is clean (no uncommitted changes)
- [ ] Current branch is recorded for return
- [ ] Source branch exists and is accessible
- [ ] Target skill name doesn't conflict with existing skills

**During Migration**:
- [ ] Temporary branch created successfully
- [ ] All source files extracted without errors
- [ ] Skill structure created completely
- [ ] Schema validation passes

**After Migration**:
- [ ] Changes committed to temporary branch
- [ ] Temporary branch merged to original branch
- [ ] Temporary branch deleted successfully
- [ ] Currently on original branch
- [ ] New skill structure verified and accessible

This git workflow ensures no data loss, proper branch management, and clean integration of migrated skills.

---

## FINAL CRITICAL REQUIREMENTS

⚠️ **ABSOLUTE ENFORCEMENT**: These requirements are MANDATORY for every migration. Violation will result in immediate process termination:

### MANDATORY EXECUTION ORDER
1. **Phase 1 MUST be completed in full** before proceeding to Phase 2
2. **Temporary branch creation is MANDATORY** - NEVER work on main branch
3. **Conflict checking is REQUIRED** before any file operations
4. **Complete git workflow is NON-NEGOTIABLE** - merge and cleanup MUST occur

### ZERO TOLERANCE VIOLATIONS
- **NO shortcuts or "quick migrations"** - follow complete protocol
- **NO direct branch work** - temporary branches are MANDATORY
- **NO skipping validations** - all checks must be performed
- **NO incomplete workflows** - merge and cleanup MUST be completed

### SUCCESS VERIFICATION
Migration is only successful when:
1. ✅ All validation steps completed
2. ✅ Temporary branch created and used exclusively  
3. ✅ Complete git workflow executed (merge + cleanup)
4. ✅ No process violations occurred
5. ✅ All CRITICAL safeguards followed

**ENFORCEMENT**: Any deviation from this protocol will be considered a migration failure requiring immediate correction.
```
