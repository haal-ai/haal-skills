---
name: prepare-conversation-handover
description: Create a clear and concise handover document to ensure smooth transition between conversation sessions or team members.
license: Apache-2.0
metadata:
  olaf_tags: [handover, documentation, workflow, collaboration]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **author**: string - Name of the person preparing the handover
- **next_steps**: array[object] - List of tasks to be completed next
- **context**: string - (Optional) Additional context or notes
- **timezone**: string - (Optional) Timezone for timestamps (default: "CEDT")

## Process
1. **Session Analysis**:
   - Review current conversation context
   - Identify key files and resources
   - Note important decisions and discussions
   - Capture current state and progress
2. **Handover Preparation**:
   - Document file locations and purposes
   - List pending tasks with priorities
   - Note any blockers or dependencies
   - Include relevant references and links
3. **Document Generation**:
   - Create structured handover document
   - Add timestamp and metadata
   - Include clear action items
   - Ensure all critical information is captured

## Output/Result Format

Use template: `templates/handover-template.md`

The handover document should include:
- Session metadata (author, timestamp, project)
- Project state summary (1-2 sentences)
- Key files and resources with descriptions
- Next steps with owners and dependencies
- Important notes and decisions
- References to related documentation

## Output to USER
1. **Handover Document**:
   - Complete markdown file
   - Saved to `.olaf/data/handover-conversation*.md`
   - Ready for sharing or continuation
2. **Confirmation**:
   - Summary of created handover
   - Location of saved file
   - Next steps for the user

## Domain-Specific Rules
- Rule 1: Always include timestamps in specified timezone
- Rule 2: Use absolute paths for all file references
- Rule 3: Keep language clear and concise
- Rule 4: Structure information for easy scanning
- Rule 5: Include all necessary context for handover

## Required Actions
1. Gather session information2. Identify key files and resources
3. Document current state4. Define next steps
5. Generate handover document using template

⚠️ **Critical Notes**
- Always use absolute paths
- Include all necessary context
- Keep it concise but complete
- Update timestamps when reusing
- Verify all links and references
