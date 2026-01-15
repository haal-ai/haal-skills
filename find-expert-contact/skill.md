---
name: find-expert-contact
description: Analyze person registers and records to recommend appropriate contacts for specific questions or problems based on expertise matching
license: Apache-2.0
metadata:
  olaf_tags: [contact-lookup, expertise-matching, team-directory, people-analysis]
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
- **question_or_problem**: string - The specific question, problem, or type of assistance needed
- **urgency_level**: enum[low,medium,high,critical] - (Optional) Urgency level to determine contact method
- **preferred_contact_method**: enum[email,chat,meeting,any] - (Optional) Preferred way to reach out

## Process
1. **Question Analysis**:
   - Parse the question/problem to identify key topics and domains
   - Extract technical keywords and business context
   - Determine the type of expertise required
   - Assess complexity level and urgency2. **Person Register Review**:
   - Read all person records from `.olaf/data/peoples/`
   - Parse each person's areas of expertise and proficiency levels
   - Review project responsibilities and roles
   - Check contact guidance and availability preferences3. **Expertise Matching**:
   - Map question requirements to person expertise areas
   - Score compatibility based on:
     - Direct expertise match
     - Role relevance
     - Project responsibilities alignment
     - Past experience indicators
   - Consider availability and preferred contact methods4. **Contact Recommendation**:
   - Rank potential contacts by match score
   - Filter by availability and contact preferences
   - Consider urgency level vs. person's working hours
   - Provide alternative contacts for backup

## Output/Result Format

Use `#[[file:templates/contact-recommendation-template.md]]` to structure the recommendations:
- Follow the template's sections for consistency
- Include match reasoning and confidence levels
- Provide multiple contact options when available
- Document alternative approaches if no direct match found

## Output to USER
1. **Primary Recommendation**:
   - Best match contact person
   - Expertise alignment explanation
   - Recommended contact method and timing
   - Confidence level (High/Medium/Low)
2. **Alternative Contacts**:
   - Secondary options with rationale
   - Escalation contacts for complex issues
   - Team/group contacts for collaborative topics3. **Contact Strategy**:
   - Suggested approach for reaching out
   - Context to provide when contacting
   - Expected response timeframe
   - Follow-up recommendations

## Domain-Specific Rules
- Rule 1: Always provide rationale for contact recommendations
- Rule 2: Respect working hours and time zones when suggesting contact timing
- Rule 3: Consider urgency vs. expertise - sometimes faster response trumps perfect match
- Rule 4: Suggest escalation paths for critical issues
- Rule 5: Recommend team/group contacts for cross-functional topics

## Required Actions
1. Analyze the question/problem context2. Review all available person records
3. Score expertise matches objectively4. Generate prioritized contact recommendations
5. Provide actionable contact strategy

⚠️ **Critical Notes**
- Never invent contact information not in person records
- Respect contact preferences and working hours
- Consider cultural and communication style preferences
- Always provide backup options when possible
- Include confidence levels in recommendations
