---
name: create-person-record
description: Create a new person record following the standard template and update related indexes.
license: Apache-2.0
metadata:
  olaf_tags: [documentation, people, team]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **full_name**: string - Full name of the person
- **nickname**: string - (Optional) Preferred nickname
- **email**: string - Professional email address
- **role**: string - Current role in the project/organization
- **project_start_date**: date (YYYYMMDD) - When they joined the project
- **project_end_date**: date (YYYYMMDD) - (Optional) When they left the project
- **contact_guidance**: string - When and how to contact this person
- **areas_of_expertise**: string - List of skills and expertise areas
- **project_responsibilities**: string - Key responsibilities
- **preferred_contact_methods**: string - How to reach them
- **working_hours**: string - Time zone and availability
- **notes**: string - (Optional) Additional information

## Process
1. **Record Creation**:
   - Generate filename: `[role]-[name]-[date].md`
   - Create file in `.olaf/data/peoples/`
   - Populate using `templates/project-manager/people-template.md`
2. **Documentation Updates**:
   - Add entry to `.olaf/data/peoples/people-register.md` (MANDATORY)
   - Update team directory
   - Create changelog entry in `.olaf/data/projects/changelog-register.md` ONLY IF the USER explicitly requests it
3. **Validation**:
   - Verify all required fields
   - Check for existing records
   - Ensure consistent formatting

## Output/Result Format

Use `templates/project-manager/people-template.md` to structure the person record:
- Follow the template's sections for consistency
- Create file: `.olaf/data/peoples/[role]-[name]-[date].md`
- Register entry in `.olaf/data/peoples/people-register.md`
- Changelog entry in `.olaf/data/projects/changelog-register.md` ONLY IF the USER explicitly requests it

## Success Criteria (MUST ALL BE TRUE)
- [ ] Person record file created in `.olaf/data/peoples/`
- [ ] Entry added to `.olaf/data/peoples/people-register.md`


## People Register Update (EXACT FORMAT)
Update the **Participant Table** in `.olaf/data/peoples/people-register.md` by appending a new row using this exact column order:
`| Name | Role | Primary Skills | Secondary Skills | Contact Information | When to Contact | Availability |`

New row template (replace placeholders; keep the `|` separators and `<br>` for multiple contact methods):
`| <full_name> | <role> | <primary_skills> | <secondary_skills> | Email: <email><br><other contact methods> | <when_to_contact> | <working_hours> |`

## Output to USER
1. **Confirmation**:
   - Record creation status
   - File location
   - Assigned ID/reference
2. **Next Steps**:
   - Review instructions
   - Notification setup
   - Access permissions

## Domain-Specific Rules
- Rule 1: Follow privacy guidelines
- Rule 2: Maintain consistent formatting
- Rule 3: Keep contact info up-to-date
- Rule 4: Respect working hours
- Rule 5: Document changes

## Required Actions
1. Collect person details
2. Create record file
3. Update register
4. Document in changelog
5. Confirm completion

⚠️ **Critical Notes**
- Protect personal information
- Verify email format
- Document access controls
- Include emergency contacts
- Regular review schedule

