# Tutorial: create-changelog-entry

## Introduction
Add properly formatted entries to your project's changelog with linked detail files.

## Prerequisites
- Existing changelog structure in `.olaf/data/product/`
- Clear description of the change to document

## Step-by-Step Instructions

### Step 1: Invoke the Skill
```
@create-changelog-entry
```

### Step 2: Select Changelog Type
Choose:
- **Functional** - User-facing changes (Feature, Enhancement, Documentation)
- **Technical** - Internal changes (Refactor, Fix, Infrastructure)

### Step 3: Provide Entry Details
- **entry_type**: Category label (Feature, Fix, etc.)
- **entry_description**: One-line summary
- **additional_context**: Detailed explanation for the linked file

### Step 4: Review Proposed Paths
Confirm the changelog and detail file locations before writing.

### Step 5: Verify Results
Check that:
- Entry appears in the correct date section
- Detail file was created
- Link is clickable

## Verification Checklist
- [ ] Changelog type is correct
- [ ] Entry appears at top of today's section
- [ ] Detail file contains full context
- [ ] Markdown link works

## Troubleshooting

### Entry in wrong date section
Verify system date is correct. The skill uses current date for section placement.

### Link doesn't work
Ensure the detail file path matches the link format exactly.

## Next Steps
- Review changelog with `analyze-changelog-and-report`
- Archive old entries with `archive-changelog-entries`
