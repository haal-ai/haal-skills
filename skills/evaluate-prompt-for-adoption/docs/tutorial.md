# Evaluate Prompt for Adoption: Step-by-Step Tutorial

**How to Assess External Prompts Before Importing**

This tutorial demonstrates how to evaluate external prompts for potential adoption into your OLAF framework using a structured assessment process.

## Prerequisites

- OLAF framework installed and active
- Internet connection (for fetching from URLs)
- Access to existing OLAF skills for similarity checking

## Estimated Time

10-15 minutes per prompt evaluation

## Step-by-Step Instructions

### Step 1: Invoke the Skill

**User Action:**
```
evaluate prompt for adoption
```

**AI Response:**
Acknowledges request and asks for the prompt source.

### Step 2: Provide Prompt Source

**Option A - URL:**
```
source_url: https://github.com/f/awesome-chatgpt-prompts/blob/main/prompts/linux-terminal.txt
```

**Option B - Direct Paste:**
```
source_text: [paste your prompt content here]
```

**What AI Does:**
- If URL: Fetches content from the source
- Extracts prompt content from page (markdown, code block, raw text)
- Parses prompt structure (frontmatter, description, instructions)

**You Should See:**
```
✓ Fetching prompt from URL...
✓ Retrieved 245 characters
✓ Detected prompt type: Interactive simulation
```

### Step 3: Similarity Check

**What AI Does:**
1. Searches existing OLAF skills for similar capabilities
2. Calculates conceptual overlap percentage
3. Identifies unique features in external prompt
4. Determines similarity verdict

**You Should See:**
```
Checking similarity to existing OLAF skills...
✓ Searched 96 skills
✓ Found 0 similar skills (0% overlap)
✓ Similarity Verdict: LOW - New capability
```

**If Similar Skills Found:**
```
✓ Found 2 similar skills:
  - review-code (75% overlap)
  - review-diff (45% overlap)
✓ Similarity Verdict: HIGH - Mostly duplicate
```

### Step 4: Optional - Provide Available Skills List

**AI May Ask:**
"To avoid adopting a duplicate, can you paste your available skills list?"

**User Provides (Optional):**
```
available_skills_list: review-code, review-diff, analyze-function-complexity, ...
```

**Why This Helps:**
- Detects duplicates you may already have installed
- Improves accuracy of similarity assessment
- Prevents importing skills you already own

### Step 5: Quality Evaluation

**What AI Does:**
Evaluates prompt across 5 dimensions:

**Clarity Assessment:**
```
✓ Clear objective stated? YES
✓ Well-structured sections? YES
✓ Unambiguous instructions? YES
✓ Examples provided? NO
✓ Expected outputs defined? YES
Rating: Clear
```

**Genericity Assessment:**
```
✓ Applicable to multiple use cases? YES
✓ Not too narrow/specific? YES
✓ Reusable across projects? YES
Rating: Generic
```

**Parameterizability Assessment:**
```
✓ Can be parameterized? MODERATE
✓ Supports configuration? LIMITED
✓ Flexible for contexts? YES
Rating: Moderate
```

**LLM Independence Assessment:**
```
✓ Works across LLMs? YES
✓ Not platform-locked? YES
✓ Standard patterns? YES
Rating: Agnostic
```

**Structure Quality Assessment:**
```
✓ Logical flow? YES
✓ Proper sections? PARTIAL
✓ Error handling? NO
✓ Success criteria? NO
Rating: Acceptable
```

### Step 6: Persona & Use Case Analysis

**What AI Determines:**
```
### Persona & Use Cases
- Target Personas: Developers (junior to senior), DevOps engineers
- Primary Use Case: Learning/practicing Linux commands safely
- Secondary Use Cases: Testing command sequences, documentation
- Frequency: Weekly (learning contexts)
- Context: Solo work, training sessions
```

### Step 7: Value-Add Calculation

**What AI Calculates:**
```
Value Score Calculation:
- Frequency: 3/5 (weekly) × 3 = 9 points
- Genericity: 3/5 (domain-specific) × 2 = 6 points
- AI Necessity: 5/5 (requires understanding) × 3 = 15 points
- Quality: 4/5 (acceptable) × 2 = 8 points

Total: 38/50 points - GOOD
```

**Value Tiers:**
- 40-50: EXCELLENT - Adopt immediately
- 30-39: GOOD - Strong candidate
- 20-29: MODERATE - Consider with improvements
- 10-19: LOW - Skip or extract parts
- 0-9: POOR - Not worth it

### Step 8: Review Evaluation Report

**AI Provides Complete Report:**
```markdown
## Evaluation Report

### Source Information
- URL: https://github.com/.../linux-terminal.txt
- Description: Act as a Linux Terminal
- Author: Community contribution
- License: CC0-1.0

### Similarity Analysis
- Similarity Scope: Workspace-only
- Similar OLAF Skills: None (0% overlap)
- Unique Features: Terminal simulation, command execution
- Similarity Verdict: LOW - New capability ✅

### Quality Assessment
| Dimension | Rating | Notes |
|-----------|--------|-------|
| Clarity | Clear | Well-defined behavior |
| Genericity | Domain-Specific | Linux-specific |
| Parameterizability | Moderate | Could add shell types |
| LLM Independence | Agnostic | Works anywhere |
| Structure | Acceptable | Could add error handling |

### Persona & Use Cases
- Target Personas: Developers, sysadmins, DevOps
- Primary Use Case: Safe Linux command practice
- Frequency: Weekly

### Value-Add Analysis
- Frequency × Specificity: MEDIUM VALUE ⭐⭐
- AI Necessity: Required
- Value Score: 38/50 - GOOD

### Final Recommendation

🎯 RECOMMENDATION: ADOPT WITH MODIFICATIONS

Rationale: Unique capability not in OLAF. Good quality but needs
parameterization and error handling.

Modifications needed:
1. Add shell_type parameter (bash/zsh/fish)
2. Add error handling section
3. Structure as proper OLAF skill

Estimated effort: Medium (2-3 hours)

### Next Steps
1. Use create-skill to build OLAF-native version
2. Add to learning-tools competency
3. Include parameterization for different shells
```

### Step 9: Decide on Action

**AI Asks:**
"Would you like me to proceed with ADOPT WITH MODIFICATIONS?"

**User Options:**
1. **Yes, create skill**: Proceeds to create-skill or convert-prompt-to-skill
2. **Extract parts only**: Identifies specific patterns to merge into existing skills
3. **Skip for now**: Saves evaluation for later reference
4. **Re-evaluate**: Request different assessment criteria

**Example Response:**
```
Yes, create an OLAF-native version using create-skill
```

### Step 10: Follow-Up Action

**If ADOPT:**
```
✓ Proceeding to create-skill...
✓ Skill name: simulate-linux-terminal
✓ Target competency: learning-tools
```

**If EXTRACT PARTS:**
```
Parts to extract:
1. Command simulation pattern → add to existing skill
2. Interactive feedback format → merge into review-code

Would you like me to enhance the existing skill now?
```

## Verification Checklist

After evaluation, verify:

✅ **Source fetched correctly** (content retrieved)
✅ **Similarity check completed** (overlap calculated)
✅ **Quality assessed** (all 5 dimensions rated)
✅ **Value score calculated** (0-50 points)
✅ **Recommendation provided** (ADOPT/SKIP/EXTRACT)
✅ **Next steps defined** (actionable guidance)

## Understanding Recommendations

| Recommendation | When Used | Action |
|----------------|-----------|--------|
| ADOPT | Low similarity, high value | Import as-is or minor tweaks |
| ADOPT WITH MODIFICATIONS | Good but needs work | Improve then import |
| EXTRACT PARTS | Medium similarity, some unique value | Merge into existing |
| SKIP | High similarity or low value | Don't import |

## Troubleshooting

**If URL fetch fails:**
- Check URL is accessible
- Try raw file URL for GitHub
- Paste content directly as source_text

**If similarity seems wrong:**
- Provide available_skills_list for better detection
- Check if similar skills exist under different names
- Request manual similarity override

**If value score seems off:**
- Consider your team's specific context
- Adjust for domain-specific needs
- Request re-evaluation with different criteria

## Best Practices

1. **Evaluate before importing**: Always assess external prompts first
2. **Check multiple sources**: Compare similar prompts from different sources
3. **Consider maintenance**: High-quality prompts are easier to maintain
4. **Track adoptions**: Note which adopted prompts get actual use
5. **Re-evaluate periodically**: Prompts may become outdated or redundant

## Common Evaluation Patterns

### Pattern 1: The Duplicate
- High similarity (>80%)
- No unique features
- **Action**: SKIP, use existing

### Pattern 2: The Enhancement
- Medium similarity (40-70%)
- Some unique features
- **Action**: EXTRACT PARTS, merge

### Pattern 3: The Hidden Gem
- Low similarity (<40%)
- High value score (>35)
- **Action**: ADOPT

### Pattern 4: The Niche Special
- Very specific use case
- High quality but rare use
- **Action**: ADOPT WITH MODIFICATIONS (make more generic)

## Next Steps After Evaluation

1. **If ADOPT**: Use convert-prompt-to-skill or create-skill
2. **If EXTRACT**: Identify target skill and merge patterns
3. **If SKIP**: Document reason for future reference
4. **Track outcomes**: Monitor which adoptions prove valuable

## Expected Timeline

- **Simple evaluation**: 5-10 minutes
- **Complex prompt**: 15-20 minutes
- **Batch evaluation**: 5-10 minutes per prompt

