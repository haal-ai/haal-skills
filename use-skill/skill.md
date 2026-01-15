---
name: use-skill
description: Intelligent skill discovery and execution router that searches condensed framework, local filesystem, and invokes help-me-olaf when needed
license: Apache-2.0
metadata:
  olaf_tags: [skill, discovery, routing, search, execution, workflow]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

## Input Parameters
You MUST request these parameters if not provided by the user:
- **user_request**: string - The user's task description or skill request (REQUIRED)
- **keywords**: array - Optional explicit keywords to match against (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use **Act** protocol for search and discovery operations
- You WILL use the **matched skill's protocol** for execution once found

## Purpose
This skill acts as the primary router for all user requests, implementing a cascading search strategy:
1. Search condensed OLAF framework embedded patterns2. Search local filesystem skills if no match
3. Invoke help-me-olaf if still no match4. Execute matched skill with appropriate protocol

## Process

### Step 1: Search Condensed Framework First

You WILL:
- Load the condensed OLAF framework if not already loaded
- Search embedded skill patterns between `<!-- OLAF_COMPETENCIES_START -->` and `<!-- OLAF_COMPETENCIES_END -->`
- Parse pattern format: `pattern1|pattern2|pattern3→path/to/skill.md|Protocol`
- Match user request against patterns using literal meaning and clear intent
**IMPORTANT**: 
- Match based on **literal meaning** and **clear intent**
- Do NOT use abstract interpretations
- Only trigger skills when user's words **directly correspond** to skill patterns
- Use case-insensitive matching
- Support partial word matches (e.g., "review" matches "code review")
**Success criterion**: Pattern match found with confidence ≥ 80%

### Step 2: Search Local Skills (If No Match)

If Step 1 fails, you WILL:
- Search `skills/*/prompts/*.md` for all skill files
- Read frontmatter from each file: name, description, tags, aliases
- Match against user keywords using fuzzy matching
- Build confidence scores based on:
  - Name match: 100%
  - Alias match: 90%
  - Description match: 70%
  - Tag match: 50%
  - Content match: 30%
**Scoring calculation**:
- Best match type determines confidence score
- Multiple matches increase confidence by 10% per additional match (max +30%)
- Minimum threshold: 65%
**Success criterion**: Match found with confidence ≥ 65%

### Step 3: Invoke help-me-olaf (If Still No Match)

If Steps 1 and 2 fail, you WILL:
- Invoke the `help-me-olaf` skill
- Pass the user's original request to help-me-olaf
- Let help-me-olaf guide the user through:
  - Refined search
  - Skill browsing
  - New prompt creation
**Success criterion**: User gets appropriate guidance or creates new skill

### Step 4: Execute Matched Skill

Once a skill is found, you WILL:
- Announce the matched skill:
  ```
  ✅ MATCHED SKILL: [name]
  Description: [description]
  Protocol: [Act|Propose-Act|Propose-Confirm-Act]
  Path: [path/to/skill.md]
  ```
- Load the skill file
- Read its frontmatter and content
- Execute following its specified protocol
- If no protocol specified, default to **Act** protocol

## Execution Protocols (Reference)

**Act Protocol** (Default):
- Execute directly without asking
- Used for: analysis, search, read-only operations
**Propose-Act Protocol**:
- Present plan/action to user
- Wait for agreement before acting
- Used for: modifications, generation, transformations
**Propose-Confirm-Act Protocol**:
- Step 1: Present detailed plan
- Step 2: Wait for review and agreement
- Step 3: Ask for final sign-off
- Step 4: Execute after confirmation
- Used for: critical operations, deletions, major changes

## Error Handling

You MUST handle these scenarios:

**Condensed Framework Not Found**:
- Warn user that condensed framework is missing
- Proceed to Step 2 (local search)
**No Skills Found**:
- Proceed to Step 3 (help-me-olaf)
**Multiple High-Confidence Matches**:
- Present ranked list of matches with confidence scores
- Ask user to select one or refine request
**Skill File Not Found**:
- Report error with path
- Suggest alternatives if available
- Invoke help-me-olaf for guidance

## Output Format

**When match found**:
```
✅ MATCHED SKILL: [name]
Confidence: [XX%]
Description: [brief description]
Protocol: [Act|Propose-Act|Propose-Confirm-Act]
Path: [relative/path/to/skill.md]

Executing with [Protocol] protocol...
```

**When no match found**:
```
❌ NO SKILL MATCH FOUND

Your request: "[user request]"
Searched: Condensed framework + Local filesystem

Invoking help-me-olaf for guidance...

```

**When multiple matches found**:
```
🔍 MULTIPLE MATCHES FOUND
1. [Name] - [Confidence XX%]
   [Brief description]
2. [Name] - [Confidence XX%]
   [Brief description]

Which one? (1, 2, or refine request)
```

## Examples

**Example 1: Direct condensed framework match**
```
User: "review my code"
Match: "review code|code review" → developer/prompts/review-code.md|Propose-Act
Action: Execute review-code.md with Propose-Act protocol
```

**Example 2: Local filesystem match**
```
User: "check my accessibility"
No condensed match found
Search local: Found "review-code-accessibility.md" (confidence: 85%)
Action: Execute accessibility review with Act protocol
```

**Example 3: No match - invoke help**
```
User: "faire la chambre"
No condensed match found
No local match found
Action: Invoke help-me-olaf skill to guide user
```

## Validation Checklist

Before executing, verify:
- [ ] User request captured and understood
- [ ] Condensed framework searched first
- [ ] Local filesystem searched if needed
- [ ] help-me-olaf invoked if no match
- [ ] Matched skill file exists and is readable
- [ ] Execution protocol correctly identified
- [ ] User informed of matched skill before execution

## Success Criteria
- User request successfully routed to appropriate skill
- Skill executed with correct protocol
- User informed of matched skill and execution plan
- No manual file searching required by user
- Seamless experience from request to execution
