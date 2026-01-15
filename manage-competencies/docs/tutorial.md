# Manage Competencies Tutorial

## Quick Start

### Create a New Competency

```
User: create competency my-new-tool
```

The skill will:
1. Ask for pack name (e.g., "developer")
2. Ask for description
3. Show proposed structure
4. Create all files on confirmation

### Edit an Existing Competency

```
User: edit competency my-tool
```

Options:
- Add/modify files
- Update manifest
- Update documentation

### Delete a Competency

```
User: delete competency old-tool
```

The skill will:
1. Check for dependencies
2. Show impact
3. Require explicit confirmation

### Validate a Competency

```
User: validate competency my-tool
```

Checks:
- Required files present
- Manifest JSON validity
- Entry points exist
- Dependencies valid

## Best Practices

1. Always validate after creating/editing
2. Check dependencies before deleting
3. Use kebab-case names
4. Start with "experimental" status
5. Document thoroughly

## Examples

### Example 1: Create PDF Analysis Competency

```
User: create competency pdf-analysis

Skill asks:
- Pack: document-processing
- Description: Comprehensive PDF document analysis

Result: Full competency structure created
```

### Example 2: Validate Before Deployment

```
User: validate competency pdf-analysis

Result: ✅ All checks pass
```
