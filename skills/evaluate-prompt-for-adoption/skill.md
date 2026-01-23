---
name: evaluate-prompt-for-adoption
description: Fetch and evaluate external prompts for potential adoption into OLAF
license: Apache-2.0
metadata:
  olaf_tags: [evaluation, adoption, quality-assessment, prompt-curation, external-sources]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response:
1. **source_url**: string - URL to the prompt (GitHub, gist, registry, webpage) (REQUIRED if source_text not provided)
2. **source_text**: string - Direct paste of prompt content (REQUIRED if source_url not provided)
3. **source_description**: string - Brief description of what the prompt does (OPTIONAL - will analyze if not provided)
4. **available_skills_list**: string - List of skills the user currently has available/installed (OPTIONAL - improves duplicate detection)

## User Interaction
You MUST follow these interaction guidelines:
- Provide thorough analysis with clear recommendation
- Present evaluation findings in structured format
- Ask for user confirmation before proceeding with adoption actions
- Use numbered lists when presenting options or findings

## Process

### 1. Acquisition Phase
You WILL fetch the prompt content:

**If source_url provided:**
- Use `fetch_webpage` tool to retrieve content from URL
- Extract prompt content from page (may be markdown, code block, raw text)
- If GitHub raw file, get direct content
- If GitHub page, extract from markdown rendering
- If gist, extract from embedded content
- If awesome list, get referenced prompt file

**If source_text provided:**
- Use provided text directly
- Validate it contains actual prompt content

**Parse Prompt Structure:**
- Identify frontmatter (if present)
- Extract description, tags, parameters
- Identify main instructions
- Find example sections
- Detect dependencies (templates, tools, data)

### 2. Similarity Check Phase
You WILL check against existing OLAF skills:

**Search Existing Skills:**
- Use `semantic_search` to find similar skills in workspace
- Search for keywords from prompt description
- Look for similar objectives/use cases
- Check prompt-engineer competency for overlap

**Optional: Check User-Visible Skills**
- If **available_skills_list** is provided, compare the external prompt against that list to detect duplicates the user may already have, even if they are not present in the current workspace.
- If **available_skills_list** is not provided, you SHOULD ask the user to paste the output of "what skills do you have?" (or provide their skills list) before finalizing an ADOPT recommendation.
- If the user cannot provide it, proceed with a workspace-only similarity check and clearly label the limitation in the report.

**Similarity Assessment:**
```
For each similar skill found:
- Calculate conceptual overlap (0-100%)
- Identify unique features in external prompt
- Identify features already in OLAF
- Determine if external prompt adds value

If available_skills_list is provided:
- Identify potential duplicates in the user's available skills
- Estimate overlap qualitatively (HIGH/MEDIUM/LOW)
```

**Similarity Verdict:**
- **HIGH (>80%)**: Already have this, skip unless significantly better
- **MEDIUM (40-80%)**: Partial overlap, extract unique parts
- **LOW (<40%)**: New capability, evaluate for adoption

### 3. Quality Evaluation Phase
You WILL assess prompt quality across dimensions:

#### 3.1 Clarity Assessment
**Evaluate:**
- ✅ Clear objective stated?
- ✅ Well-structured sections?
- ✅ Unambiguous instructions?
- ✅ Examples provided?
- ✅ Expected outputs defined?

**Rating**: Clear / Somewhat Clear / Unclear

#### 3.2 Genericity Assessment
**Evaluate:**
- ✅ Applicable to multiple use cases?
- ✅ Not too narrow/specific to one domain?
- ✅ Reusable across projects/teams?
- ✅ Domain-agnostic or valuable niche?

**Rating**: Generic / Domain-Specific / Too Narrow

#### 3.3 Parameterizability Assessment
**Evaluate:**
- ✅ Can be parameterized (inputs/outputs)?
- ✅ Supports configuration/options?
- ✅ Flexible for different contexts?
- ✅ Clear parameter structure?

**Current Parameters Detected**: [List found parameters]
**Potential Parameters**: [List parameters that could be added]

**Rating**: Highly Parameterizable / Moderately / Hardcoded

#### 3.4 LLM Independence Assessment
**Evaluate:**
- ✅ Works across different LLMs (Claude, GPT, Gemini)?
- ✅ Not tied to specific agent framework?
- ✅ No vendor-specific syntax?
- ✅ Uses standard prompt patterns?
- ⚠️ GitHub Copilot-specific features (.prompt.md)?
- ⚠️ Claude Artifacts-specific?
- ⚠️ ChatGPT plugin-specific?

**Rating**: LLM-Agnostic / Platform-Preferred / Platform-Locked

#### 3.5 Structure Quality Assessment
**Evaluate:**
- ✅ Logical flow/sequence?
- ✅ Proper sections (input, process, output)?
- ✅ Error handling included?
- ✅ Validation steps defined?
- ✅ Clear success criteria?

**Rating**: Well-Structured / Acceptable / Needs Restructuring

### 4. Persona & Use Case Analysis
You WILL identify target users:

**Who Would Use This?**
- Developer personas: [junior, senior, architect, lead]
- Domain experts: [data scientist, designer, analyst]
- Roles: [individual contributor, team lead, manager]
- Expertise level: [beginner, intermediate, advanced]

**Use Case Scenarios:**
- Primary use case: [main scenario]
- Secondary use cases: [additional scenarios]
- Frequency: [daily, weekly, monthly, rare]
- Context: [solo work, team collaboration, project phase]

### 5. Value-Add Estimation
You WILL assess the prompt's value:

#### 5.1 Frequency vs Specificity Matrix
```
         │ High Frequency        │ Low Frequency
─────────┼──────────────────────┼─────────────────
Generic  │ HIGH VALUE ⭐⭐⭐     │ MEDIUM VALUE ⭐⭐
         │ (everyday tool)      │ (useful helper)
─────────┼──────────────────────┼─────────────────
Specific │ MEDIUM VALUE ⭐⭐     │ LOW VALUE ⭐
         │ (niche but frequent) │ (very situational)
```

**Assessment:**
- Frequency: [daily/weekly/monthly/rare]
- Specificity: [generic/domain-specific/very-narrow]
- **VALUE RATING**: [⭐⭐⭐ / ⭐⭐ / ⭐]

#### 5.2 AI Necessity Assessment
**Does this NEED AI?**
- ✅ Requires reasoning/creativity/judgment
- ⚠️ Could be partially automated with scripts
- ❌ Could be fully replaced by script/tool/automation

**Examples:**
- "Generate creative blog post" → ✅ Needs AI
- "Format JSON output" → ⚠️ AI helps but script could work
- "Calculate sum of numbers" → ❌ Script is better

**AI Necessity**: Required / Beneficial / Optional

#### 5.3 Value-Add Score
Combine factors:
```
Value Score = (Frequency × 3) + (Genericity × 2) + (AI_Necessity × 3) + (Quality × 2)

Where:
- Frequency: 1-5 (rare to daily)
- Genericity: 1-5 (very narrow to generic)
- AI_Necessity: 1-5 (scriptable to AI-required)
- Quality: 1-5 (poor to excellent)

Total: 0-50 points
```

**Value Tiers:**
- 40-50: **EXCELLENT** - Adopt immediately
- 30-39: **GOOD** - Strong candidate
- 20-29: **MODERATE** - Consider with improvements
- 10-19: **LOW** - Skip or extract specific parts
- 0-9: **POOR** - Not worth adopting

### 6. Adoption Recommendation Phase
You WILL provide final recommendation:

## Evaluation Report

### Source Information
- **URL/Source**: [source_url or "Provided Text"]
- **Description**: [extracted or provided description]
- **Author**: [if detectable]
- **License**: [if detectable]

### Similarity Analysis
- **Similarity Scope Used**: [workspace-only / workspace+available_skills_list]
- **Similar OLAF Skills (workspace)**: [list with overlap %]
- **Possible User Skill Duplicates**: [list from available_skills_list, or "Not provided"]
- **Unique Features**: [what this adds that OLAF doesn't have]
- **Similarity Verdict**: [HIGH/MEDIUM/LOW - recommendation]

### Quality Assessment
| Dimension | Rating | Notes |
|-----------|--------|-------|
| Clarity | [Clear/Somewhat/Unclear] | [brief comment] |
| Genericity | [Generic/Domain/Narrow] | [brief comment] |
| Parameterizability | [High/Moderate/Hardcoded] | [brief comment] |
| LLM Independence | [Agnostic/Preferred/Locked] | [brief comment] |
| Structure | [Well/Acceptable/Needs Work] | [brief comment] |

### Persona & Use Cases
- **Target Personas**: [list]
- **Primary Use Case**: [description]
- **Frequency**: [daily/weekly/monthly/rare]

### Value-Add Analysis
- **Frequency × Specificity**: [HIGH/MEDIUM/LOW VALUE]
- **AI Necessity**: [Required/Beneficial/Optional]
- **Value Score**: [X/50 points] - [EXCELLENT/GOOD/MODERATE/LOW/POOR]

### Final Recommendation

**🎯 RECOMMENDATION**: [ADOPT / ADOPT WITH MODIFICATIONS / EXTRACT PARTS / SKIP]

**Rationale**:
[2-3 sentences explaining why]

**If ADOPT:**
- Suggested skill name: [kebab-case-name]
- Suggested competency: [competency-name]
- Priority: [high/medium/low]

**If ADOPT WITH MODIFICATIONS:**
- Modifications needed:
  1. [modification 1]
  2. [modification 2]
- Estimated effort: [low/medium/high]

**If EXTRACT PARTS:**
- Parts worth extracting:
  1. [specific technique/pattern]
  2. [specific section]
- Integration approach: [where to add in OLAF]

**If SKIP:**
- Reason: [why not valuable]
- Alternative: [existing OLAF skill that covers this]

### Next Steps
**If adopting:**
1. Use `convert-prompt` to modernize to OLAF standards, OR
2. Use `create-skill` to build OLAF-native version

**If extracting:**
1. Identify target OLAF skill to enhance
2. Extract specific patterns/techniques
3. Integrate into existing skill

## Output Format
You WILL generate outputs following this structure:

**Evaluation Report** (as defined in Process section)

**Interactive Follow-up:**
After presenting report, ask user:
- "Would you like me to proceed with [RECOMMENDATION]?"
- If **available_skills_list** was not provided: "To avoid adopting a duplicate, can you paste your available skills list (answer to 'what skills do you have?')?"
- If ADOPT: "Should I modernize it now using convert-prompt, or package an OLAF-native version with create-skill?"
- If EXTRACT: "Which OLAF skill should I enhance with the extracted parts?"

## User Communication

### Progress Updates
- Confirmation when prompt content is fetched/received
- Status when analyzing similarity to existing skills
- Notification when quality evaluation is complete
- Presentation of evaluation report with recommendation

### Completion Summary
- Final recommendation (ADOPT/MODIFY/EXTRACT/SKIP)
- Value score and rationale
- Similar skills identified
- Next steps for adoption (if applicable)

### Next Steps
- If ADOPT: Use convert-prompt or create-skill to integrate
- If EXTRACT: Identify target skill and integration approach
- If SKIP: Consider alternative existing skills
- Review evaluation report for detailed analysis

## Domain-Specific Rules
You MUST follow these constraints:

**Fetch Rules:**
- ALWAYS check if URL is accessible before analysis
- HANDLE different source formats (GitHub, gists, raw files, web pages)
- EXTRACT actual prompt content, not surrounding page chrome

**Similarity Rules:**
- NEVER recommend adopting near-duplicate (>80% overlap)
- ALWAYS highlight unique features even in similar prompts
- CONSIDER merging similar prompts rather than having both
- If **available_skills_list** is provided, treat near-duplicates from that list as duplicates for adoption decisions
- If **available_skills_list** is not provided, explicitly label the similarity check as workspace-only

**Quality Rules:**
- BE HONEST about quality issues
- DON'T let popularity/stars override quality assessment
- CONSIDER if prompt is well-suited for OLAF or needs adaptation

**Value Rules:**
- PRIORITIZE high-frequency generic prompts
- DON'T dismiss niche prompts if exceptionally well-crafted
- CONSIDER team/project context in frequency estimation

**Recommendation Rules:**
- PROVIDE SPECIFIC next steps, not vague suggestions
- ESTIMATE effort required for modifications
- SUGGEST specific OLAF skills to enhance if extracting

## Success Criteria
You WILL consider the task complete when:
- [ ] Prompt content fetched or received
- [ ] Similarity check completed against existing skills
- [ ] Quality evaluation completed across all dimensions
- [ ] Value-add score calculated
- [ ] Evaluation report generated with clear recommendation
- [ ] User presented with findings and next steps
- [ ] User confirmation obtained for any adoption actions

## Required Actions
1. Fetch or receive prompt content
2. Parse prompt structure and extract metadata
3. Check similarity against existing OLAF skills
4. Evaluate quality across all dimensions
5. Calculate value-add score
6. Generate evaluation report with recommendation
7. Present findings to user and await confirmation

## Error Handling
You WILL handle these scenarios:
- **URL Not Accessible**: Request alternative source or direct text paste
- **Invalid Prompt Content**: Ask user to verify source or provide clearer content
- **Similarity Check Fails**: Proceed with quality evaluation, note limitation
- **Missing available_skills_list**: Warn about potential duplicates, proceed with workspace-only check
- **Unclear Recommendation**: Provide multiple options with trade-offs

⚠️ **Critical Requirements**
- MANDATORY: Fetch actual prompt content before evaluating
- MANDATORY: Check similarity to existing OLAF skills
- NEVER recommend adopting duplicates without strong justification
- ALWAYS provide VALUE SCORE and clear rationale
- ALWAYS suggest concrete next steps
