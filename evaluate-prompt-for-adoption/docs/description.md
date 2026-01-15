# Evaluate Prompt for Adoption

## Overview

The `evaluate-prompt-for-adoption` skill helps you systematically assess external prompts (from GitHub, awesome lists, registries, or the web) to determine if they're worth adopting into your OLAF framework.

## Purpose

Before importing every interesting prompt you find, you need to evaluate:
- Is it similar to what we already have?
- Is it high quality?
- Will anyone actually use it?
- Does it add real value?
- Is it worth the maintenance burden?

This skill provides a structured evaluation framework to make informed adoption decisions.

## Key Features

### 1. Multi-Source Fetching
Retrieve prompts from various sources:
- **GitHub repositories** - Raw files or repo browse
- **GitHub gists** - Public prompt collections
- **Awesome lists** - Curated prompt libraries
- **Web pages** - Blog posts, documentation
- **Direct paste** - Copy/paste prompt text

### 2. Similarity Detection
Avoid duplicates by checking against existing OLAF skills:
- Semantic search across workspace
- Overlap percentage calculation
- Unique feature identification
- Merge vs adopt decision support

### 3. Multi-Dimensional Quality Assessment
Evaluate prompts across **5 quality dimensions**:

#### Clarity
- Clear objective?
- Well-structured?
- Unambiguous instructions?
- Examples provided?

#### Genericity
- Applicable to multiple use cases?
- Reusable across projects?
- Domain-agnostic or valuable niche?

#### Parameterizability
- Can be configured?
- Supports inputs/outputs?
- Flexible for different contexts?

#### LLM Independence
- Works across LLMs (Claude, GPT, Gemini)?
- Not platform-locked?
- Standard prompt patterns?

#### Structure Quality
- Logical flow?
- Proper sections?
- Error handling?
- Validation steps?

### 4. Persona & Use Case Analysis
Identify who would use this prompt:
- Developer personas (junior, senior, architect)
- Domain experts (data scientist, designer)
- Expertise levels (beginner, intermediate, advanced)
- Use case frequency (daily, weekly, rare)

### 5. Value-Add Estimation

**Frequency × Specificity Matrix**:
```
         │ High Frequency        │ Low Frequency
─────────┼──────────────────────┼─────────────────
Generic  │ HIGH VALUE ⭐⭐⭐     │ MEDIUM VALUE ⭐⭐
         │ (everyday tool)      │ (useful helper)
─────────┼──────────────────────┼─────────────────
Specific │ MEDIUM VALUE ⭐⭐     │ LOW VALUE ⭐
         │ (niche but frequent) │ (very situational)
```

**AI Necessity Assessment**:
- ✅ Requires AI (reasoning, creativity)
- ⚠️ Benefits from AI but could script
- ❌ Better as script/tool

**Value Score** (0-50 points):
- 40-50: **EXCELLENT** - Adopt immediately
- 30-39: **GOOD** - Strong candidate
- 20-29: **MODERATE** - Consider with improvements
- 10-19: **LOW** - Skip or extract parts
- 0-9: **POOR** - Not worth it

### 6. Actionable Recommendations

Clear recommendation with rationale:
- **ADOPT** - Import as-is or with minor tweaks
- **ADOPT WITH MODIFICATIONS** - Needs improvements first
- **EXTRACT PARTS** - Take specific patterns, not whole prompt
- **SKIP** - Not valuable or duplicative

## Use Cases

### Scenario 1: GitHub Awesome List Discovery
You find a promising prompt in awesome-chatgpt-prompts:

```
User: "evaluate this prompt: https://github.com/awesome/prompts/blob/main/code-reviewer.md"

→ Fetches prompt from GitHub
→ Checks: Do we have code review skills?
→ Compares to existing review-code, review-diff skills
→ Finds 60% overlap but unique features
→ Rates: Clarity ✅, Genericity ✅, AI-required ✅
→ Value score: 38/50 (GOOD)
→ Recommends: ADOPT WITH MODIFICATIONS (extract unique review criteria, merge into review-code)
```

### Scenario 2: Blog Post Prompt
You see an interesting prompt in a blog:

```
User: "evaluate prompt from https://example.com/blog/amazing-prompt"

→ Fetches from webpage
→ Extracts prompt from article
→ Checks similarity: LOW (15% overlap)
→ Rates quality across 5 dimensions
→ Analyzes: High frequency + Generic = HIGH VALUE
→ Value score: 42/50 (EXCELLENT)
→ Recommends: ADOPT - create as new skill
→ Suggests: Use create-skill, competency: productivity
```

### Scenario 3: Direct Paste Evaluation
You copied a prompt from Slack:

```
User: "evaluate this prompt: [pastes content]"

→ Analyzes pasted text
→ Finds: Very specific to one use case
→ Rates: Genericity ❌ (Too Narrow)
→ Frequency: Rare
→ Value score: 12/50 (LOW)
→ Recommends: SKIP - too specific, low reuse potential
```

### Scenario 4: Gist Collection
You found a gist with multiple prompts:

```
User: "evaluate prompts from https://gist.github.com/user/abc123"

→ Fetches gist
→ Finds 5 prompts in gist
→ Evaluates each separately
→ Results:
  - Prompt 1: ADOPT (45/50)
  - Prompt 2: SKIP (duplicate of existing)
  - Prompt 3: EXTRACT PARTS (good pattern, merge into existing)
  - Prompt 4: ADOPT WITH MODIFICATIONS (needs parameterization)
  - Prompt 5: SKIP (better as script)
```

## Evaluation Report Example

```markdown
## Evaluation Report

### Source Information
- **URL**: https://github.com/f/awesome-chatgpt-prompts/blob/main/prompts.csv#L42
- **Description**: Act as a Linux Terminal
- **Author**: Fatih Kadir Akın
- **License**: CC0-1.0

### Similarity Analysis
- **Similar OLAF Skills**: None found (0% overlap)
- **Unique Features**: Interactive terminal simulation, command execution feedback
- **Similarity Verdict**: LOW - New capability

### Quality Assessment
| Dimension | Rating | Notes |
|-----------|--------|-------|
| Clarity | Clear | Well-defined objective and behavior |
| Genericity | Domain-Specific | Specific to Linux terminal simulation |
| Parameterizability | Moderate | Could add shell type parameter |
| LLM Independence | Agnostic | Works across all LLMs |
| Structure | Acceptable | Clear but could add error handling |

### Persona & Use Cases
- **Target Personas**: Developers (junior to senior), System administrators, DevOps engineers
- **Primary Use Case**: Learning/practicing Linux commands safely
- **Frequency**: Weekly (learning contexts)

### Value-Add Analysis
- **Frequency × Specificity**: MEDIUM VALUE ⭐⭐ (domain-specific but useful)
- **AI Necessity**: Required (needs understanding of Linux commands)
- **Value Score**: 32/50 points - GOOD

### Final Recommendation

**🎯 RECOMMENDATION**: ADOPT WITH MODIFICATIONS

**Rationale**:
Unique capability not in OLAF. Good quality but could be enhanced with error handling. Value score indicates strong adoption candidate.

**Modifications needed**:
1. Add error handling capabilities
2. Add error handling section
3. Add examples of common command interactions
4. Structure as OLAF skill with proper manifest

**Estimated effort**: Medium (2-3 hours to properly structure)

### Next Steps
1. Use `create-skill` to build OLAF-native version with modifications
2. Add to `learning-tools` or `development` competency
3. Include parameterization for different shells
4. Add comprehensive examples and error handling
```

## Benefits

### For Teams
- **Curated Library**: Only high-quality prompts enter OLAF
- **No Duplicates**: Systematic similarity checking
- **Clear Criteria**: Objective evaluation framework
- **Value Focus**: Prioritize high-impact prompts

### For Individuals
- **Save Time**: Quick evaluation vs lengthy trial-and-error
- **Better Decisions**: Data-driven adoption choices
- **Learn Patterns**: Understand what makes prompts valuable
- **Avoid Clutter**: Don't import low-value prompts

### For Projects
- **Quality Standards**: Maintain high bar for prompts
- **Strategic Growth**: Grow library intentionally
- **Resource Efficiency**: Focus on high-ROI prompts
- **Maintenance Burden**: Avoid adopting hard-to-maintain prompts

## Integration with Other Skills

### Evaluation → Import Flow
```
1. evaluate-prompt-for-adoption (this skill)
   ↓ [if ADOPT recommendation]
2. import-prompt-unchanged (as-is import)
   OR
3. convert-prompt (modernize to OLAF standards)
   OR
4. create-skill (build OLAF-native version)
```

### Evaluation → Enhancement Flow
```
1. evaluate-prompt-for-adoption
   ↓ [if EXTRACT PARTS recommendation]
2. Identify target OLAF skill
   ↓
3. Extract valuable patterns/techniques
   ↓
4. Enhance existing skill with extracted parts
```

## Best Practices

### When to Evaluate
- ✅ Before importing any external prompt
- ✅ When exploring awesome lists or registries
- ✅ After seeing interesting blog post prompts
- ✅ When team member suggests new prompt
- ✅ During periodic prompt library audits

### What to Look For
- ✅ High value score (30+)
- ✅ Low similarity to existing (<40%)
- ✅ Clear quality ratings
- ✅ AI necessity (not scriptable)
- ✅ Realistic use frequency

### Red Flags
- ❌ High similarity (>80%) without significant improvements
- ❌ Platform-locked (only works on one LLM/agent)
- ❌ Unclear or poorly structured
- ❌ Too specific (one-time use)
- ❌ Better as script/tool than prompt

## Advanced Usage

### Batch Evaluation
Evaluate multiple prompts from a collection:
```
User: "evaluate all prompts from https://github.com/awesome/prompts/"

→ Fetches repository
→ Identifies prompt files
→ Evaluates each individually
→ Provides summary report with recommendations
```

### Comparative Evaluation
Compare two similar prompts:
```
User: "evaluate and compare:
  - https://github.com/user1/code-review-prompt
  - https://github.com/user2/better-code-review"

→ Evaluates both
→ Compares quality scores
→ Recommends best one or hybrid approach
```

### Periodic Re-evaluation
Re-evaluate adopted prompts periodically:
```
User: "re-evaluate my-imported-skill against current OLAF standards"

→ Checks if better alternatives now exist in OLAF
→ Assesses if still valuable
→ Recommends: keep, enhance, or deprecate
```

## Metrics Tracked

The evaluation provides quantifiable metrics:
- **Similarity Score**: 0-100% overlap with existing skills
- **Quality Ratings**: 5 dimensions (Clear/Acceptable/Poor scale)
- **Value Score**: 0-50 points weighted formula
- **AI Necessity**: Required/Beneficial/Optional
- **Frequency**: Daily/Weekly/Monthly/Rare
- **Effort Estimate**: Low/Medium/High for modifications

## Common Evaluation Outcomes

### Outcome Distribution (typical)
- **ADOPT** - 20% (truly new, high-value prompts)
- **ADOPT WITH MODIFICATIONS** - 30% (good but needs work)
- **EXTRACT PARTS** - 25% (valuable patterns to merge)
- **SKIP** - 25% (duplicates or low value)

This distribution helps maintain a curated, high-quality OLAF library while avoiding prompt bloat.
