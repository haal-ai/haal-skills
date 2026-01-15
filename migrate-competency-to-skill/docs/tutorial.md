# Migrate Competency to Skill: Complete Tutorial

## Overview
The migrate-competency-to-skill automates the extraction of competency features from git branches and their transformation into standalone skills that comply with OLAF skills architecture and schema requirements.

## When to Use This Skill
- You need to extract a specific feature from a competency on another branch
- You want to transform competency features into reusable standalone skills
- You need to ensure schema compliance for migrated skills
- You want to maintain functionality while modernizing architecture

## Prerequisites
- Git repository with competency branches available
- Understanding of OLAF competency and skills architecture
- Basic knowledge of skill manifest schema requirements

## Step-by-Step Process

### Step 1: Identify Migration Source
Before invoking the skill, identify:

1. **Source branch name**: Where the competency exists
2. **Competency name**: The competency package containing the feature
3. **Feature name**: Specific feature within the competency to migrate
4. **Target skill name**: Desired name for new skill (use kebab-case)

### Step 2: Invoke the Migration Skill
```
olaf migrate-competency-to-skill
```

You'll be prompted for required parameters:
- **Source branch**: e.g., "feature/olaf-feature-system"
- **Competency name**: e.g., "researcher"
- **Feature name**: e.g., "search-and-learn"  
- **Target skill name**: e.g., "lean-and-search"

### Step 3: Review Migration Plan
The skill will present a detailed migration plan including:
- Source validation results
- Available features in the competency
- Transformation steps to be applied
- Schema compliance requirements

### Step 4: Confirm Migration
After reviewing the plan, provide confirmation to proceed with the migration.

### Step 5: Validate Results
The skill will generate:
- Complete skill directory structure
- Schema-compliant skill manifest
- Migrated and adapted prompt files
- Documentation and tutorials
- Migration report

## Detailed Workflow

### Phase 1: Source Validation
```bash
# The skill will:
git branch -a                           # List all branches
git checkout {source_branch}            # Switch to source branch
# Validate competency structure exists
# Extract available features from competency manifest
```

### Phase 2: Feature Extraction
```bash
# Create temporary branch for migration
git checkout {current_branch}
git checkout -b temp-{target_skill_name}-migration

# Extract feature files
git show {source_branch}:olaf-core/competencies/{competency_name}/prompts/{feature_name}.md
git show {source_branch}:olaf-core/competencies/{competency_name}/templates/{template_name}
```

### Phase 3: Architecture Transformation
The skill transforms the competency structure to skills format:

**From Competency Structure:**
```
olaf-core/competencies/{competency_name}/
├── competency-manifest.json
├── prompts/
│   └── {feature_name}.md
├── templates/
│   └── {template_name}
└── docs/
    └── {feature_name}/
```

**To Skill Structure:**
```
{skills_dir}{target_skill_name}/
├── skill-manifest.json
├── prompts/
│   └── {target_skill_name}.md
├── templates/
│   └── {template_name}
├── tools/
│   └── {tool_files}
└── docs/
    └── tutorial.md
```

### Phase 4: Skill Manifest Generation
Creates schema-compliant manifest with:

**Required Metadata Fields:**
- `id`: kebab-case skill identifier
- `name`: Human-readable display name
- `shortDescription`: Concise one-line description
- `objectives`: 1-5 skill objectives
- `tags`: Relevant persona and use case tags
- `status`: experimental|proven|mainstream|deprecated
- `exposure`: export|internal|kernel
- `version`: Semantic version (MAJOR.MINOR.PATCH)
- `protocol`: Act|Propose-Act|Propose-Confirm-Act|Analyze-Report

**BOM (Bill of Materials):**
- `prompts`: All exposed prompts with paths
- `templates`: Template files (if any)
- `tools`: Tool files - Python scripts, shell scripts, executables (if any)
- `docs`: Documentation files
- Path validation against schema patterns

### Phase 5: Schema Validation
Validates against `olaf-skill-manifest.schema.json`:
- Field presence and format validation
- Pattern matching for paths and identifiers
- Enum value validation
- Array constraint checking

## Best Practices

### Choosing Target Skill Names
- Use kebab-case format: verb-entity-complement
- Be descriptive but concise
- Examples: "lean-and-search", "analyze-code-quality", "generate-tech-spec"

### Migration Considerations
- **Functionality Preservation**: Ensure all original functionality is maintained
- **Path Updates**: Update all file references to use skills directory structure
- **Documentation**: Generate comprehensive tutorials and guides
- **Testing**: Validate the migrated skill works correctly

### Schema Compliance Tips
- Validate all required fields are present
- Use proper enum values for status, exposure, protocol
- Ensure path patterns match schema requirements
- Keep descriptions within character limits

## Common Migration Scenarios

### Scenario 1: Research Competency Feature
```
Source: feature/olaf-feature-system
Competency: researcher
Feature: search-and-learn
Target: lean-and-search
```

**Transformations Applied:**
- Prompt file adapted from competency to skill format
- Template references updated to skills directory
- Tool files migrated with preserved permissions
- Documentation generated with examples
- Schema-compliant manifest created

### Scenario 2: Analysis Competency Feature
```
Source: feature-analysis-tools
Competency: business-analyst
Feature: analyze-requirements
Target: analyze-business-requirements
```

**Transformations Applied:**
- Multiple prompt files consolidated or separated
- Template files migrated and adapted
- Tool files migrated with dependency documentation
- Tool dependencies documented
- Integration patterns preserved

## Troubleshooting

### Issue: Source Branch Not Found
**Symptoms**: Error message about branch not existing
**Causes**: 
- Typo in branch name
- Branch not fetched locally
- Case sensitivity issues

**Solutions**:
- List all branches: `git branch -a`
- Fetch remote branches: `git fetch --all`
- Verify exact branch name spelling

### Issue: Competency Not Found
**Symptoms**: Cannot locate competency directory
**Causes**:
- Wrong competency name
- Different directory structure on source branch
- Competency moved or renamed

**Solutions**:
- Examine branch structure manually
- List available competencies
- Check competency naming patterns

### Issue: File Reference Conflicts
**Symptoms**: Broken references after migration
**Causes**:
- Path references not updated
- Case sensitivity issues
- File structure differences

**Solutions**:
- Systematically update all file references
- Use find/replace for common path patterns
- Verify all links work in new structure
### Issue: Schema Validation Failure
**Symptoms**: Skill manifest doesn't validate against schema
**Causes**:
- Missing required fields
- Invalid enum values
- Path pattern mismatches
- Array constraint violations

**Solutions**:
- Review schema requirements carefully
- Check field formats and patterns
- Validate enum values against allowed options
- Ensure all paths exist and match patterns

### Issue: Tool Execution Problems
**Symptoms**: Tools don't execute or produce errors after migration
**Causes**:
- File permissions lost during migration
- Hardcoded paths within tool files
- Missing tool dependencies

**Solutions**:
- Restore execute permissions: `chmod +x tool_file`
- Update hardcoded paths within tool source code
- Document tool dependencies in skill manifest

## Advanced Usage

### Custom Transformations
For complex migrations, you may need to:

1. **Split Large Features**: Break down complex competency features into multiple skills
2. **Merge Related Features**: Combine small related features into single skills
3. **Add Dependencies**: Document skill dependencies for complex workflows
4. **Custom Templates**: Create skill-specific templates when needed

### Batch Migrations
For migrating multiple features from the same competency:

1. Run migration for each feature separately
2. Consider creating skill dependencies between related features
3. Maintain consistent naming patterns
4. Update documentation to cross-reference related skills

### Integration Testing
After migration, test integration:

1. **Skill Invocation**: Ensure skill can be called correctly
2. **Parameter Validation**: Test all input parameter scenarios
3. **Output Generation**: Verify output matches expected format
4. **Error Handling**: Test error scenarios and edge cases

## Migration Checklist

### Pre-Migration
- [ ] Source branch identified and accessible
- [ ] Competency and feature names verified
- [ ] Target skill name chosen (kebab-case)
- [ ] Current branch state saved/committed

### During Migration
- [ ] Source validation completed successfully
- [ ] Feature extraction completed
- [ ] Architecture transformation applied
- [ ] Skill manifest generated and validated
- [ ] All file references updated
- [ ] Documentation generated

### Post-Migration
- [ ] Schema validation passed
- [ ] Skill functionality tested
- [ ] Migration report generated
- [ ] Temporary branches cleaned up
- [ ] Changes committed to target branch

### Quality Assurance
- [ ] All original functionality preserved
- [ ] Path references work correctly
- [ ] Documentation is comprehensive
- [ ] Error handling maintained
- [ ] Schema compliance verified

## Integration with Other Skills

### Complementary Skills
- **create-skill**: For creating entirely new skills from scratch
- **validate-olaf-artifacts**: For additional validation of migrated skills
- **review-code**: For reviewing migrated code quality

### Workflow Combinations
1. **Migrate → Test → Document**
   - Use migrate-competency-to-skill for migration
   - Test functionality manually
   - Enhance documentation as needed

2. **Analyze → Migrate → Integrate**
   - Analyze source competency structure
   - Migrate specific features
   - Integrate with existing skill ecosystem

## Best Practices Summary

1. **Preparation**: Always validate source before starting migration
2. **Naming**: Use consistent, descriptive kebab-case naming
3. **Functionality**: Preserve all original behavior
4. **Documentation**: Generate comprehensive tutorials and guides
5. **Validation**: Ensure schema compliance throughout process
6. **Testing**: Validate migrated skill functionality
7. **Cleanup**: Remove temporary files and branches
8. **Integration**: Consider how skill fits into broader ecosystem

## Conclusion

The migrate-competency-to-skill automates the complex process of extracting competency features and transforming them into standalone, schema-compliant skills. By following this tutorial and using the provided validation checkpoints, you can successfully migrate features while maintaining functionality and ensuring architectural compliance.

For additional help, use the `help-me-olaf` skill with questions about migration processes or schema compliance.