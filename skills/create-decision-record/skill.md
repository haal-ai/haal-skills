---
name: create-decision-record
description: Create a new decision record following the standard template and update related indexes.
license: Apache-2.0
metadata:
  olaf_tags: [documentation, decision-making, governance]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **title**: string - Concise description of the decision
- **type**: enum[Architecture,Project,Business,Functional,People,Technical,Security,Other] - Type of decision
- **status**: enum[Proposed,Accepted,Replaced,Superseded] - (Optional) Decision status (default: Proposed)
- **context**: string - Background and problem statement
- **drivers**: string - Key factors influencing the decision
- **options**: string - Options considered with pros and cons
- **decision**: string - (Optional) Selected option if already determined
- **decision_makers**: string - Individuals responsible for the decision
- **stakeholders**: string - Affected parties and stakeholders

## Process
1. **Record Creation**:
   - Generate unique ID (DR-YYYYMMDD-NN)
   - Create file in `.olaf/data/product/decision-records/`
   - Populate using `templates/project-manager/decision-record-template.md`
2. **Documentation Updates**:
   - Add entry to `.olaf/data/product/decision-records/decision-records-register.md`
   - Update relevant indexes
   - Create changelog entry
3. **Validation**:
   - Verify all required fields
   - Check for similar decisions
   - Ensure proper formatting

## Output/Result Format

Use `templates/project-manager/decision-record-template.md` to structure the decision record:
- Follow the template's sections for consistency
- Create file: `.olaf/data/product/decision-records/YYYYMMDD-title-as-kebab-case.md`
- Register entry in `.olaf/data/product/decision-records/decision-records-register.md`
- Changelog entry in `.olaf/data/projects/changelog-register.md`

## Output to USER
1. **Confirmation**:
   - Record creation status
   - File location
   - Assigned decision ID
2. **Next Steps**:
   - Review instructions
   - Stakeholder notification
   - Follow-up actions

## Domain-Specific Rules
- Rule 0: NEVER create, modify, or delete any file under `~/.olaf/` (e.g., `~/.olaf/`). All writes MUST be within the current repo workspace (i.e., paths rooted at `.olaf/`).
- Rule 1: Follow existing naming conventions
- Rule 2: Maintain cross-references
- Rule 3: Preserve decision history
- Rule 4: Ensure traceability
- Rule 5: Keep records up-to-date

## Required Actions
1. Generate decision ID
2. Create record file
3. Update register
4. Document in changelog
5. Confirm completion

⚠️ **Critical Notes**
- Never modify existing decisions
- Maintain audit trail
- Include all stakeholders
- Document assumptions
- Keep records concise
