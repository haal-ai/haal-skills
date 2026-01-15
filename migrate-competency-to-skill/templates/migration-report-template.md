# Competency to Skill Migration Report Template

**Purpose**: Document the complete migration process from competency feature to standalone skill  
**Used By**: migrate-competency-to-skill  
**Version**: 1.0  
**Last Updated**: 2025-11-19

## Template Structure

```markdown
# Competency to Skill Migration Report: {target_skill_name}

**Generated**: {YYYYMMDD-HHmm} UTC  
**Source Branch**: {source_branch}  
**Source Competency**: {competency_name}  
**Source Feature**: {feature_name}  
**Target Skill**: {target_skill_name}  

---

## Migration Summary

### Status
- **Migration Status**: {Success|Partial|Failed}
- **Files Migrated**: {count}
- **Components Created**: {list_components}
- **Tools Migrated**: {tool_count}
- **Schema Compliance**: {✅ Validated|❌ Failed|⚠️ Partial}
- **Duration**: {migration_time}

### Key Achievements
- {achievement_1}
- {achievement_2}
- {achievement_3}

---

## Source Analysis

### Original Competency Structure
**Competency**: `{competency_name}`  
**Location**: `{source_branch}:olaf-core/competencies/{competency_name}/`  
**Feature**: `{feature_name}`  

### Available Features in Source Competency
1. **{feature_1}**: {description_1}
2. **{feature_2}**: {description_2}
3. **{feature_3}**: {description_3}

### Migrated Feature Components
| Component | Source Path | Target Path | Status |
|-----------|------------|-------------|---------|
| Main Prompt | `prompts/{feature_name}.md` | `prompts/{target_skill_name}.md` | {✅|❌|⚠️} |
| Template | `templates/{template_name}` | `templates/{template_name}` | {✅|❌|⚠️} |
| Tool | `tools/{tool_name}` | `tools/{tool_name}` | {✅|❌|⚠️} |
| Documentation | `docs/{doc_name}` | `docs/{doc_name}` | {✅|❌|⚠️} |

---

## Transformation Applied

### Architecture Changes
1. **Directory Structure**: Competency → Skill format
   - From: `olaf-core/competencies/{competency_name}/`
   - To: `{skills_dir}{target_skill_name}/`

2. **File Organization**:
   - Created skill-specific directory structure
   - Maintained component separation (prompts, templates, docs)
   - Added skill manifest for metadata and BOM

### Prompt File Adaptations
```markdown
Original: {source_path}
Target: {target_path}

Changes Applied:
- {change_1}
- {change_2}
- {change_3}
```

### Template Adaptations
```markdown
Original Template: {template_source_path}
Target Template: {template_target_path}

Changes Applied:
- Updated file references to skills directory structure
- {other_changes}
```

### Tool Adaptations
```markdown
Original Tool: {tool_source_path}
Target Tool: {tool_target_path}

Changes Applied:
- Updated path references within tool code
- Preserved file permissions and execution rights
- {other_tool_changes}
```

### Path Reference Updates
- **From**: `competencies/{competency_name}/templates/{template_name}`
- **To**: `templates/{template_name}`

---

## Schema Compliance Validation

### Skill Manifest Schema Validation
**Schema**: `olaf-skill-manifest.schema.json`  
**Validation Result**: {✅ Passed|❌ Failed}  

#### Metadata Compliance
- [x] `id`: {target_skill_name} (kebab-case format)
- [x] `name`: {skill_display_name}
- [x] `shortDescription`: {description_text}
- [x] `objectives`: {objectives_count} objectives defined
- [x] `tags`: {tags_count} tags assigned
- [x] `status`: {status_value}
- [x] `exposure`: {exposure_value}
- [x] `version`: {version_number} (semantic versioning)
- [x] `protocol`: {protocol_value}

#### BOM (Bill of Materials) Compliance
- [x] `prompts`: {prompts_count} prompts defined with proper paths
- [x] `templates`: {templates_count} templates defined (if applicable)
- [x] `tools`: {tools_count} tools defined (if applicable)
- [x] `docs`: {docs_count} documentation files defined

#### Schema Validation Details
```json
{
  "validation_status": "{passed|failed}",
  "errors": [
    {
      "field": "{field_path}",
      "error": "{error_description}",
      "resolution": "{how_fixed}"
    }
  ]
}
```

---

## Skill Structure Created

```
{target_skill_name}/
├── skill-manifest.json          # Schema-compliant manifest with metadata and BOM
├── prompts/
│   └── {target_skill_name}.md   # Main skill prompt (adapted from competency)
├── templates/
│   └── {template_files}         # Migrated template files
├── tools/
│   └── {tool_files}             # Migrated tool files (.py, .sh, executables)
└── docs/
    └── tutorial.md              # Generated tutorial and documentation
```

### File Details
| File | Size | Purpose | Schema Compliance |
|------|------|---------|------------------|
| `skill-manifest.json` | {size} | Skill metadata and BOM | {✅|❌} Validated |
| `prompts/{target_skill_name}.md` | {size} | Main skill workflow | {✅|❌} Referenced |
| `templates/{template_name}` | {size} | {template_purpose} | {✅|❌} Referenced |
| `tools/{tool_name}` | {size} | {tool_purpose} | {✅|❌} Referenced |
| `docs/tutorial.md` | {size} | Usage documentation | {✅|❌} Referenced |

---

## Migration Challenges and Resolutions

### Issues Encountered
1. **{Issue_1}**: {description}
   - **Resolution**: {how_resolved}
   - **Impact**: {impact_assessment}

2. **{Issue_2}**: {description}
   - **Resolution**: {how_resolved}
   - **Impact**: {impact_assessment}

### Manual Adjustments Required
- {adjustment_1}
- {adjustment_2}
- {adjustment_3}

### Validation Fixes Applied
- {fix_1}
- {fix_2}
- {fix_3}

---

## Quality Assurance

### Testing Performed
- [x] Skill manifest validates against schema
- [x] All referenced files exist and are accessible
- [x] Path references work correctly
- [x] Tool files have correct permissions and execute properly
- [x] Original functionality preserved
- [x] Documentation generated and complete

### Functionality Verification
- [x] Skill can be invoked using: `olaf {target_skill_name}`
- [x] All aliases work correctly
- [x] Input parameters properly validated
- [x] Output format matches template
- [x] Error handling preserved

---

## Next Steps

### Immediate Actions
1. **Test skill functionality**: Run the migrated skill with sample inputs
2. **Update skill index**: Add skill to competency query index if needed
3. **Documentation review**: Review generated documentation for accuracy

### Integration Tasks
1. **Competency integration**: Consider how skill integrates with existing competencies
2. **Dependency mapping**: Document any dependencies on other skills
3. **Usage patterns**: Define when to use this skill vs original competency

### Future Enhancements
- {enhancement_1}
- {enhancement_2}
- {enhancement_3}

---

## Usage Instructions

### Basic Usage
```
olaf {target_skill_name}
```

### Parameters Required
- **{param_1}**: {description}
- **{param_2}**: {description}
- **{param_3}**: {description}

### Example Session
```
olaf {target_skill_name}
{param_1}: {example_value_1}
{param_2}: {example_value_2}
{param_3}: {example_value_3}
```

---

## Appendix

### Git Operations Log
```bash
# Branch operations
ORIGINAL_BRANCH={original_branch_name}
git checkout {source_branch}                     # Source validation
git checkout $ORIGINAL_BRANCH                    # Return to original
git checkout -b temp-{target_skill_name}-migration  # Create temp branch

# File extraction
git show {source_branch}:{source_file_path} > {temp_file}

# Migration and commit
git add skills/{target_skill_name}/
git commit -m "feat: migrate {feature_name} from {competency_name}"

# Merge back and cleanup
git checkout $ORIGINAL_BRANCH                    # Return to original
git merge temp-{target_skill_name}-migration     # Merge changes
git branch -d temp-{target_skill_name}-migration # Delete temp branch
```

### Original Feature Metadata
```json
{
  "original_name": "{feature_name}",
  "original_description": "{original_description}",
  "original_tags": ["{tag_1}", "{tag_2}"],
  "original_protocol": "{original_protocol}",
  "migration_date": "{YYYYMMDD-HHmm}"
}
```

---

**Report Generated**: {YYYYMMDD-HHmm} UTC  
**Migration Tool**: migrate-competency-to-skill v1.0.0  
**Schema Version**: olaf-skill-manifest.schema.json  
**Quality Status**: {Validated|Needs Review|Failed}
```

## Placeholder Guide

- `{target_skill_name}`: The new skill name in kebab-case
- `{YYYYMMDD-HHmm}`: Timestamp in OLAF standard format
- `{source_branch}`: Source git branch name
- `{competency_name}`: Source competency name
- `{feature_name}`: Source feature name within competency
- `{Success|Partial|Failed}`: Migration status indicator
- `{count}`: Numeric count of items
- `{list_components}`: Comma-separated list of components
- `{✅|❌|⚠️}`: Status indicators (success, fail, warning)
- `{achievement_N}`: Specific migration achievements
- `{feature_N}`: Available features in source competency
- `{description_N}`: Description text
- `{change_N}`: Specific changes applied
- `{size}`: File size information
- `{issue_N}`: Migration issue description
- `{adjustment_N}`: Manual adjustment description
- `{fix_N}`: Validation fix description
- `{enhancement_N}`: Future enhancement suggestions
- `{param_N}`: Parameter names and descriptions

## Notes

- **Schema Compliance**: Every migration must validate against olaf-skill-manifest.schema.json
- **Path Validation**: All BOM paths must be verified to exist and be accessible
- **Functionality Preservation**: Original competency functionality must be maintained
- **Documentation**: Comprehensive tutorial and usage guide must be generated
- **Quality Assurance**: Multiple validation checkpoints ensure migration success
- **Cleanup**: Temporary branches and files must be removed after successful migration