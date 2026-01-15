# Schema Compliance Guide for Skill Migrations

## Overview
This guide provides detailed information about ensuring skill manifests comply with the `olaf-skill-manifest.schema.json` schema during competency-to-skill migrations.

## Schema Structure Overview

The OLAF skill manifest schema has two main sections:
1. **metadata**: Descriptive information about the skill
2. **bom** (Bill of Materials): Components and files that make up the skill

## Metadata Section Requirements

### Required Fields

#### 1. ID Field
```json
"id": "migrate-competency-to-skill"
```
- **Pattern**: `^[a-z]+(-[a-z]+){2,3}$` (kebab-case, 3-4 words)
- **Format**: verb-entity-complement
- **Examples**: 
  - ✅ "create-prompt-template"
  - ✅ "analyze-code-quality"
  - ✅ "migrate-competency-to-skill"
  - ❌ "createprompt" (no hyphens)
  - ❌ "create-prompt-template-advanced" (too many words)

#### 2. Name Field
```json
"name": "Migrate Competency to Skill"
```
- **Type**: string
- **MinLength**: 3
- **Purpose**: Human-readable display name
- **Examples**: "Create Prompt Template", "Analyze Code Quality"

#### 3. Short Description
```json
"shortDescription": "Extract and migrate specific competency features from another branch"
```
- **Type**: string
- **MinLength**: 10
- **MaxLength**: 200
- **Purpose**: One-line explanation of skill functionality

#### 4. Version
```json
"version": "1.0.0"
```
- **Pattern**: `^\\d+\\.\\d+\\.\\d+$` (semantic versioning)
- **Format**: MAJOR.MINOR.PATCH
- **Examples**: "1.0.0", "2.1.3", "0.5.12"

#### 5. Objectives
```json
"objectives": [
  "Extract competency features from specified git branch with validation",
  "Transform competency structure to skills architecture format"
]
```
- **Type**: array of strings
- **MinItems**: 1
- **MaxItems**: 5
- **ItemMinLength**: 5
- **Purpose**: List of what the skill accomplishes

#### 6. Tags
```json
"tags": ["migration", "competency", "skill", "git", "transformation"]
```
- **Type**: array of strings
- **MinItems**: 1
- **ItemMinLength**: 2
- **Purpose**: Classification for personas, intents, and use cases

#### 7. Status
```json
"status": "proven"
```
- **Enum**: ["experimental", "proven", "mainstream", "deprecated"]
- **Purpose**: Maturity level of the skill

#### 8. Exposure
```json
"exposure": "internal"
```
- **Enum**: ["export", "internal", "kernel"]
- **Purpose**: Visibility and access level

#### 9. Protocol
```json
"protocol": "Propose-Confirm-Act"
```
- **Enum**: ["Act", "Propose-Act", "Propose-Confirm-Act", "Analyze-Report"]
- **Purpose**: Interaction pattern used by the skill

### Optional Metadata Fields

#### Author
```json
"author": "windsurf ai + p-square"
```
- **Pattern**: `^[A-Za-z]+\\s+[A-Za-z]+.*$`
- **Purpose**: Creator identification

#### Dates
```json
"created": "2025-11-19",
"updated": "2025-11-19"
```
- **Format**: date (ISO 8601)
- **Purpose**: Tracking creation and modification dates

#### Aliases
```json
"aliases": [
  "migrate competency to skill",
  "extract competency feature",
  "transform competency to skill"
]
```
- **Type**: array of strings
- **MinItems**: 1
- **ItemMinLength**: 2
- **Purpose**: Alternative phrases to invoke the skill

## BOM Section Requirements

### Required Component: Prompts
```json
"prompts": [
  {
    "name": "migrate-competency-to-skill",
    "path": "/prompts/migrate-competency-to-skill.md",
    "description": "Main migration workflow"
  }
]
```
- **Required Fields**: name, path
- **Path Pattern**: `^/prompts/`
- **MinItems**: 1
- **Purpose**: Exposed prompts that can be invoked

### Optional Components

#### Templates
```json
"templates": [
  {
    "name": "migration-report-template",
    "path": "templates/migration-report-template.md",
    "type": "markdown"
  }
]
```
- **Required Fields**: name, path
- **Optional Fields**: type
- **Purpose**: Template files used by prompts

#### Documentation
```json
"docs": [
  {
    "name": "tutorial",
    "path": "/docs/tutorial.md",
    "type": "tutorial"
  }
]
```
- **Required Fields**: name, path
- **Optional Fields**: type
- **Examples of types**: "tutorial", "reference", "guide", "description"

#### Helpers
```json
"helpers": [
  {
    "name": "validator",
    "path": "/helpers/validator.md",
    "description": "Schema validation helper"
  }
]
```
- **Required Fields**: name, path
- **Optional Fields**: description
- **Purpose**: Internal prompts used by other prompts

#### Tools
```json
"tools": [
  {
    "name": "parser",
    "path": "/tools/parser.py",
    "type": "python",
    "description": "JSON schema parser"
  }
]
```
- **Required Fields**: name, path
- **Optional Fields**: type, description
- **Purpose**: Scripts and executable tools

#### Knowledge Base
```json
"kb": [
  {
    "name": "domain-knowledge",
    "path": "/kb/domain-knowledge.md",
    "type": "reference"
  }
]
```
- **Required Fields**: name, path
- **Optional Fields**: type
- **Purpose**: Knowledge base files used by prompts

#### Skill Dependencies
```json
"skill_dependencies": [
  {
    "skill_id": "time-retrieval",
    "path": "skills/time-retrieval/prompts/time-retrieval.md",
    "description": "Used for timestamp generation"
  }
]
```
- **Required Fields**: skill_id, path
- **skill_id Pattern**: `^[a-z]+(-[a-z]+)*$`
- **path Pattern**: `^skills/[a-z]+(-[a-z]+)*/prompts/[a-z]+(-[a-z]+)*\\.md$`
- **Purpose**: References to other skills this skill depends on

## Common Validation Errors and Fixes

### 1. ID Pattern Mismatch
**Error**: ID doesn't match kebab-case pattern
```json
// ❌ Wrong
"id": "migrateCompetency"

// ✅ Correct  
"id": "migrate-competency-to-skill"
```

### 2. Version Format Error
**Error**: Version doesn't follow semantic versioning
```json
// ❌ Wrong
"version": "1.0"

// ✅ Correct
"version": "1.0.0"
```

### 3. Invalid Enum Values
**Error**: Using value not in enum list
```json
// ❌ Wrong
"status": "production"

// ✅ Correct
"status": "proven"
```

### 4. Path Pattern Errors
**Error**: Path doesn't match required pattern
```json
// ❌ Wrong
"path": "prompts/main.md"

// ✅ Correct
"path": "/prompts/main.md"
```

### 5. Missing Required Fields
**Error**: Required field missing from metadata
```json
// ❌ Missing objectives
{
  "id": "test-skill",
  "name": "Test Skill",
  "shortDescription": "A test skill"
  // Missing: objectives, tags, status, exposure, version, protocol
}
```

### 6. Array Constraint Violations
**Error**: Too many or too few items in arrays
```json
// ❌ Too many objectives
"objectives": [
  "objective1", "objective2", "objective3", 
  "objective4", "objective5", "objective6"  // Max is 5
]

// ❌ No tags
"tags": []  // MinItems is 1
```

## Validation Process

### 1. Manual Schema Validation
Check each field against schema requirements:
```markdown
Metadata Checklist:
- [ ] id: kebab-case, 3-4 words
- [ ] name: Human-readable, min 3 chars
- [ ] shortDescription: 10-200 chars
- [ ] version: semantic versioning format
- [ ] objectives: 1-5 items, each min 5 chars
- [ ] tags: min 1 item, each min 2 chars
- [ ] status: valid enum value
- [ ] exposure: valid enum value
- [ ] protocol: valid enum value

BOM Checklist:
- [ ] prompts: min 1 item, paths start with /prompts/
- [ ] All referenced files exist
- [ ] Path patterns match schema requirements
```

### 2. Common Migration Adaptations

When migrating from competency to skill format:

#### Update Path References
```markdown
// Original competency reference
competencies/researcher/templates/report-template.md

// Skill format reference  
templates/learning-report-template.md
```

#### Generate Proper Aliases
```json
// Extract from original competency aliases
"aliases": [
  "search and learn",      // Original competency alias
  "lean and search",       // Skill-specific alias
  "discover knowledge",    // Functional alias
  "learning workflow"      // Use case alias
]
```

#### Create Appropriate Objectives
```json
// Transform competency description into specific objectives
"objectives": [
  "Guide systematic information discovery and knowledge acquisition",
  "Enable practical application of discovered knowledge", 
  "Create structured learning reports with validated sources",
  "Support focused learning objectives with immediate application"
]
```

## Best Practices for Schema Compliance

### 1. Naming Conventions
- Use consistent kebab-case for IDs
- Choose descriptive but concise names
- Follow verb-entity-complement pattern

### 2. Path Management
- Always use absolute paths starting with /
- Verify all referenced files exist
- Maintain consistent directory structure

### 3. Enum Values
- Use only valid enum values from schema
- Choose appropriate maturity status
- Select correct exposure level

### 4. Component Organization
- Group related files logically
- Document all external dependencies
- Maintain clear separation between prompts, templates, and docs

### 5. Validation Workflow
- Validate schema compliance before committing
- Test all file references
- Verify skill functionality after migration

## Schema Compliance Checklist

Use this checklist for every skill migration:

### Pre-Migration Planning
- [ ] Target skill ID follows kebab-case pattern (3-4 words)
- [ ] Version number planned (start with 1.0.0)
- [ ] Status level determined (experimental/proven/mainstream)
- [ ] Exposure level chosen (export/internal/kernel)

### Metadata Validation
- [ ] All required fields present
- [ ] ID matches pattern: `^[a-z]+(-[a-z]+){2,3}$`
- [ ] Version matches pattern: `^\\d+\\.\\d+\\.\\d+$`
- [ ] Status uses valid enum value
- [ ] Exposure uses valid enum value  
- [ ] Protocol uses valid enum value
- [ ] Objectives array has 1-5 items
- [ ] Tags array has minimum 1 item
- [ ] shortDescription is 10-200 characters

### BOM Validation
- [ ] Prompts section present with minimum 1 item
- [ ] All prompt paths start with /prompts/
- [ ] All referenced files exist in file system
- [ ] Template paths start with appropriate prefix (if used)
- [ ] Doc paths start with appropriate prefix (if used)
- [ ] All path patterns match schema requirements

### Post-Migration Verification
- [ ] Skill manifest validates against schema
- [ ] All file references resolve correctly
- [ ] Tool files have correct permissions and execute properly
- [ ] Skill can be invoked successfully
- [ ] Original functionality preserved
- [ ] Documentation complete and accurate

This guide ensures your migrated skills meet all schema requirements and integrate properly into the OLAF framework.