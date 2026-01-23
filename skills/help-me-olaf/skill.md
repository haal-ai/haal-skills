---
name: help-me-olaf
description: Intelligent help router that discovers available skills and prompts, or captures new needs for skill creation
license: Apache-2.0
metadata:
  olaf_tags: [help, discovery, skill-search, prompt-routing, assistance, olaf]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

# Help Me - Intelligent Assistance Router

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **user_request**: string - The user's help request or problem description (REQUIRED)
- **context_info**: string - Relevant background information (OPTIONAL)
- **success_criteria**: string - What successful resolution looks like (OPTIONAL)

## User Interaction
- Discovery and search operations run without approval (non-destructive)
- Present matching skills without approval
- Ask for user approval before executing any skill
- Ask for user approval before creating a new skill

## Purpose
This prompt acts as an intelligent help discovery system that:
1. Understands user needs through conversational inquiry2. Searches for matching skills in available frameworks
3. Routes to appropriate skills or offers skill creation

## Process

### Phase 1: Understanding the Need

You WILL engage the user conversationally to understand their help request:

```
"What kind of help do you need today?
- Code review or analysis?
- Prompt creation or engineering?
- Workflow design or automation?
- Testing or quality assurance?
- Documentation or technical writing?
- Architecture or design decisions?
- Project or team management?
- Something else? (describe it)"
```

You WILL capture:
- **Primary topic** (main area of help)
- **Specific task** (what they want to accomplish)
- **Context** (relevant details about their situation)
- **Expected outcome** (what success looks like)

### Phase 2: Skill Discovery - Search Order

You MUST follow this exact search order:

#### **Search 1: Condensed OLAF Framework**
You WILL:
- Load the condensed OLAF framework patterns
- Parse all skill aliases from between markers: `<!-- OLAF_COMPETENCIES_START -->` and `<!-- OLAF_COMPETENCIES_END -->`
- Search for matching aliases using the user's keywords
- Use fuzzy matching on: topic words, partial matches, synonyms
- Extract the format: `aliases→path|Protocol`
**Success criterion**: Match found with confidence score ≥ 75%

#### **Search 2: All Available Collections**
If Search 1 fails, you WILL:
- Read `reference/competency-collections.json`
- Extract all collection names and their included skills
- For each collection, read its `competency-manifest.json`
- Search all entry_point aliases across all manifests
- Match against user keywords with fuzzy matching
**Success criterion**: Match found with confidence score ≥ 70%

#### **Search 3: Local Filesystem Search**
If Search 2 fails, you WILL:
- Search `skills/*/prompts/*.md` for all skill files
- Extract frontmatter: name, description, tags, aliases
- Search all text for user keywords
- Build confidence scores based on matches in: name (100%), description (75%), tags (50%), content (25%)
**Success criterion**: Match found with confidence score ≥ 65%

### Phase 3: Result Presentation

#### **If Skill Found:**
You WILL present:
```
✅ FOUND MATCHING SKILL

Name: [skill name]
Description: [what it does]
Location: [path/to/skill]
Aliases: [list of alternative names]
Confidence: [XX%]

Next step: Ready to execute this skill?
- Yes: Execute the skill immediately
- No: Continue searching or describe more
- Back: Return to help menu
```

You WILL execute the skill if user confirms.

#### **If Multiple Matches Found:**
You WILL present ranked options:
```
🔍 FOUND MULTIPLE MATCHES (ranked by relevance)
1. [Name] - [Confidence XX%]
   [Brief description]
2. [Name] - [Confidence XX%]
   [Brief description]
3. [Name] - [Confidence XX%]
   [Brief description]

Which one matches your need? (enter 1, 2, 3, or describe more)
```

#### **If No Skill Found:**
You WILL:
```
❌ NO EXISTING SKILL FOUND

Your need: "[user's request summary]"

I can help you create a new skill for this using the create-skill skill!

Would you like to:
1. Create a new skill for this (using create-skill)
2. Refine your search (describe differently)
3. Browse all available skills
```

### Phase 4: Skill Creation Offer

If no competency is found, you WILL offer skill creation:

You WILL:
- Summarize the user's captured need
- Explain what a new skill would do
- Offer to use **create-skill** skill to create it
- If user agrees: Execute create-skill workflow
**Captured Information** that you will have ready for create-skill:
- `user_request`: The user's articulated need
- Suggested `skill_name`: Based on their request
- Suggested `target_competency`: Based on context

### Phase 5: Information Capture (if creating new skill)

You WILL capture:
- **What** they want to accomplish (task description)
- **Why** they need it (problem being solved)
- **Context** (relevant background)
- **Success criteria** (how they'll know it works)
- **Constraints** (limitations or requirements)

You WILL format this as a clear need statement for the create-skill skill.

## User Interaction Flow

```
User: "Help me with something"
Agent: Ask clarifying questions → Understand need
Agent: Search 1 (condensed) → Match? YES → Execute
Agent: Search 2 (collections) → Match? YES → Execute
Agent: Search 3 (filesystem) → Match? YES → Execute
Agent: Capture need → Offer create-skill → User agrees?
Agent: Execute create-skill with captured information
```

## Domain-Specific Rules

You MUST follow these constraints:
- **Rule 1**: Always ask for clarification before searching if the request is vague
- **Rule 2**: Show confidence scores to help user evaluate relevance
- **Rule 3**: Offer to search differently if user is unsatisfied
- **Rule 4**: Never assume - always ask about context and goals
- **Rule 5**: Preserve all captured information for skill creation
- **Rule 6**: Present create-skill offer clearly as next step after unsuccessful search
- **Rule 7**: Execute only if user explicitly confirms skill match
- **Rule 8**: Handle search errors gracefully (missing files, read errors, etc.)

## Search Implementation Details

### Condensed Framework Search
```
1. Read .olaf/work/reference/.condensed/olaf-framework-condensed.md2. Find markers: <!-- OLAF_COMPETENCIES_START --> to <!-- OLAF_COMPETENCIES_END -->
3. Parse each line: aliases→path|Protocol4. Split aliases by | (pipe character)
5. Match user keywords against each alias6. Score: exact match=100, partial=80, synonym=60
7. Return all matches with scores ≥ 75%
```

### Collections Search
```
1. Read reference/competency-collections.json
2. For each collection_id in JSON3. Read competencies/[collection_id]/competency-manifest.json
4. Extract all entry_points[].aliases5. Match against user keywords (same scoring as above)
6. Return matches sorted by score
```

### Filesystem Search
```
1. Glob: skills/*/prompts/*.md2. For each file found:
   - Extract YAML frontmatter (name, description, tags)
   - Parse first 500 chars of content
   - Score matches in each field with weights3. Return top 10 matches sorted by score
```

## Critical Requirements
⚠️ **MANDATORY - Non-negotiable constraints:**
- ALWAYS apply the three-phase search in order (condensed → collections → filesystem)
- NEVER skip confidence score display - helps users understand matches
- NEVER execute a competency without explicit user confirmation
- ALWAYS preserve captured user information through entire session
- NEVER assume competency match - require user confirmation
- ALWAYS handle missing/inaccessible files gracefully with fallback search
- NEVER terminate help without offering create-skill if no competency found
- ALWAYS show search process for transparency to user
- NEVER proceed to create-skill without full need capture
- ALWAYS present top matches ranked by confidence score

## Error Handling

You WILL handle gracefully:
- **File not found**: "Framework file not accessible, searching alternatives..."
- **Invalid JSON**: "Collection metadata not readable, searching filesystem..."
- **No matches found**: Present to user, offer capture → create-skill
- **Ambiguous request**: Ask clarifying questions
- **User confusion**: Explain search process, offer manual browsing

## Success Criteria

You WILL consider the task complete when:
- [ ] User's need is clearly understood and documented
- [ ] Skill search completed in all 3 phases
- [ ] User either executed a skill OR agreed to create-skill
- [ ] If creating: All required parameters captured for create-skill
- [ ] User knows what happens next (execution or creation workflow)

## Output Format

Present information in clear sections:
```
🔍 HELP DISCOVERY IN PROGRESS

Step 1: Understanding your need...
[Clarifying questions and response]

Step 2: Searching condensed framework...
[Search results with confidence]

Step 3: [Continues if needed]

Step 4: [Next action]
```

## Next Steps After Skill Found

If skill is found:
- Execute immediately for non-destructive operations
- Ask for user approval before executing skills that modify files
- For file creation/modification, show proposal, wait for review, then execute

If no skill found:
- Capture need completely
- Prepare for create-skill workflow
- User approves → Trigger create-skill with all captured info

## Quick Reference: Skill Patterns

Common topics and their skill patterns:
- "create/generate/write prompt" → create-prompt
- "create/generate/new skill" → create-skill
- "review/analyze code" → review-code
- "test/augment tests" → augment-code-unit-test
- "workflow/automate" → generate-orchestrator
- "collection/select" → select-competency-collection
- "help/guidance/what can" → help-me ← YOU ARE HERE

## Implementation Notes
- Use the condensed framework as the primary source (most up-to-date)
- Collections provide secondary search when condensed misses something
- Filesystem search is comprehensive but slower fallback
- Always show user the search process for transparency
- Confidence scores help users understand why a match was suggested
- Preserve captured information through entire session
