# Evaluate Prompt for Adoption - Tutorial

This tutorial demonstrates how to evaluate external prompts for potential adoption into your OLAF framework.

## Prerequisites

- OLAF framework installed
- Internet connection (for fetching from URLs)
- Access to evaluate-prompt-for-adoption skill

## Tutorial Scenarios

### Scenario 1: Evaluate from GitHub URL

**Situation**: You found an interesting prompt in an awesome-chatgpt-prompts repository.

**Steps**:

1. **Invoke the skill with URL**:
   ```
   olaf evaluate prompt from https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts/linux-terminal.txt
   ```

2. **Skill fetches and analyzes**:
   ```
   Fetching prompt from URL...
   ✓ Retrieved 245 characters
   ✓ Detected prompt type: Interactive simulation
   
   Checking similarity to existing OLAF skills...
   ✓ Searched 96 skills
   ✓ Found 0 similar skills (0% overlap)
   
   Evaluating quality...
   ```

3. **Review the evaluation report**:
   ```
   ## Evaluation Report
   
   ### Source Information
   - URL: https://raw.githubusercontent.com/.../linux-terminal.txt
   - Description: Act as a Linux Terminal
   - Author: Community contribution
   
   ### Similarity Analysis
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
   - AI Necessity: Required (needs command understanding)
   - Value Score: 32/50 - GOOD
   
   ### Final Recommendation
   
   🎯 RECOMMENDATION: ADOPT WITH MODIFICATIONS
   
   Rationale: Unique capability not in OLAF. Good quality but needs
   parameterization and error handling. Value score indicates strong candidate.
   
   Modifications needed:
   1. Add shell_type parameter (bash/zsh/fish)
   2. Add error handling section
   3. Structure as proper OLAF skill
   
   Estimated effort: Medium (2-3 hours)
   ```

4. **Skill asks for next step**:
   ```
   Would you like me to proceed with ADOPT WITH MODIFICATIONS?
   
   I can:
   a) Create OLAF-native version with create-skill
   b) Import as-is then improve with convert-prompt
   c) Skip for now
   ```

5. **You decide**:
   ```
   Option a - create OLAF-native version
   ```

6. **Result**: Skill creates improved version

### Scenario 2: Evaluate from Direct Paste

**Situation**: Your colleague shared a prompt via Slack that they found useful.

**Steps**:

1. **Copy the prompt text**

2. **Invoke with pasted content**:
   ```
   olaf evaluate this prompt:
   
   [paste content]
   You are an expert code reviewer. Review the provided code for:
   1. Security vulnerabilities
   2. Performance issues
   3. Code style violations
   4. Best practice adherence
   Provide specific, actionable feedback.
   ```

3. **Skill analyzes without fetching**:
   ```
   Analyzing provided prompt text...
   ✓ Extracted 87 characters
   ✓ Detected type: Code review assistant
   
   Checking similarity to existing OLAF skills...
   ✓ Found 2 similar skills:
     - review-code (75% overlap)
     - review-diff (45% overlap)
   
   Evaluating quality and unique features...
   ```

4. **Review report focusing on similarity**:
   ```
   ### Similarity Analysis
   - Similar OLAF Skills:
     • review-code (75% overlap) - Already has security, performance checks
     • review-diff (45% overlap) - Focuses on git diffs
   
   - Unique Features in External Prompt:
     • "Best practice adherence" explicitly mentioned
     • Numbered checklist approach
   
   - Similarity Verdict: HIGH (75%) - Mostly duplicate ⚠️
   
   ### Final Recommendation
   
   🎯 RECOMMENDATION: EXTRACT PARTS
   
   Rationale: High overlap with existing review-code skill. However,
   the explicit "best practice adherence" callout and numbered
   checklist format could enhance our existing skill.
   
   Parts worth extracting:
   1. Best practice adherence check (add to review-code)
   2. Numbered checklist format (improve output structure)
   
   Integration approach: Enhance review-code skill with these elements
   ```

5. **Next steps provided**:
   ```
   Recommended action:
   1. Open skills/review-code/prompts/review-code.md
   2. Add "Best practice adherence" to objectives
   3. Update output format to use numbered checklist
   
   Would you like me to make these enhancements now?
   ```

### Scenario 3: Low-Value Prompt Rejection

**Situation**: You see a very specific prompt that seems narrow.

**Steps**:

1. **Invoke evaluation**:
   ```
   olaf evaluate prompt: https://example.com/my-very-specific-prompt
   ```

2. **Skill fetches and evaluates**:
   ```
   Fetching prompt...
   ✓ Retrieved content
   
   Prompt description: "Generate TypeScript interfaces for AWS Lambda
   handlers that process S3 events triggered by CloudWatch using CDK"
   
   Analyzing...
   ```

3. **Report shows low scores**:
   ```
   ### Quality Assessment
   | Dimension | Rating | Notes |
   |-----------|--------|-------|
   | Clarity | Clear | Well-defined but narrow |
   | Genericity | Too Narrow | ❌ Very specific stack |
   | Parameterizability | Hardcoded | Locked to AWS/TypeScript |
   | LLM Independence | Agnostic | Works across LLMs |
   | Structure | Acceptable | Basic structure |
   
   ### Persona & Use Cases
   - Target Personas: AWS developers using TypeScript + CDK
   - Primary Use Case: Specific S3→Lambda→CloudWatch setup
   - Frequency: Rare (only when setting up this exact pattern)
   
   ### Value-Add Analysis
   - Frequency × Specificity: LOW VALUE ⭐ (very narrow + rare)
   - AI Necessity: Optional (code generator could handle)
   - Value Score: 14/50 - LOW
   
   ### Final Recommendation
   
   🎯 RECOMMENDATION: SKIP
   
   Rationale: Too specific to one tech stack combination. Rare use case.
   Could be replaced with code generator or CDK construct. Low reuse
   potential across team. Not generic enough for OLAF library.
   
   Alternative: Use general create-typescript-interfaces skill and
   adapt output for specific AWS needs.
   ```

4. **Clear guidance**:
   ```
   This prompt is not recommended for adoption.
   
   If you frequently need AWS/TypeScript/CDK work, consider instead:
   1. Creating a generic "generate-aws-cdk-constructs" skill
   2. Parameterizing for different AWS services
   3. Making it reusable beyond S3→Lambda pattern
   ```

### Scenario 4: Excellent High-Value Find

**Situation**: You discover a prompt that looks perfect.

**Steps**:

1. **Evaluate**:
   ```
   olaf evaluate https://github.com/awesome/prompts/api-design-reviewer.md
   ```

2. **Report shows high scores**:
   ```
   ### Quality Assessment
   | Dimension | Rating | Notes |
   |-----------|--------|-------|
   | Clarity | Clear | ✅ Excellent structure |
   | Genericity | Generic | ✅ Works for any API |
   | Parameterizability | High | ✅ REST/GraphQL/gRPC support |
   | LLM Independence | Agnostic | ✅ Standard patterns |
   | Structure | Well-Structured | ✅ Comprehensive flow |
   
   ### Value-Add Analysis
   - Frequency × Specificity: HIGH VALUE ⭐⭐⭐ (generic + frequent)
   - AI Necessity: Required (needs design judgment)
   - Value Score: 45/50 - EXCELLENT
   
   ### Final Recommendation
   
   🎯 RECOMMENDATION: ADOPT
   
   Rationale: Exceptional quality across all dimensions. Fills gap in
   OLAF (no API design review skill currently). High reuse potential.
   Frequent use case. Well-structured and parameterized. No modifications
   needed.
   
   Suggested skill name: review-api-design
   Suggested competency: code-quality or api-development
   Priority: HIGH
   ```

3. **Immediate adoption**:
   ```
   Would you like me to import this excellent prompt now?
   
   I recommend: import-prompt-unchanged (it's already perfect)
   ```

4. **You confirm**:
   ```
   Yes, import it
   ```

5. **Skill proceeds**:
   ```
   ✓ Importing via import-prompt-unchanged...
   ✓ Created skill: review-api-design
   ✓ Added to api-development competency
   ✓ Ready to use!
   
   Try it: olaf review-api-design
   ```

## Understanding the Value Score

The value score formula combines multiple factors:

```
Value Score = (Frequency × 3) + (Genericity × 2) + (AI_Necessity × 3) + (Quality × 2)
```

**Example calculation**:

For "Linux Terminal" prompt:
- Frequency: 3/5 (weekly) → 3 × 3 = 9 points
- Genericity: 3/5 (domain-specific) → 3 × 2 = 6 points
- AI_Necessity: 5/5 (requires understanding) → 5 × 3 = 15 points
- Quality: 4/5 (acceptable) → 4 × 2 = 8 points

**Total**: 9 + 6 + 15 + 8 = **38/50 (GOOD)**

## Decision Matrix

Use this to quickly interpret recommendations:

| Recommendation | Similarity | Value Score | Action |
|----------------|------------|-------------|--------|
| ADOPT | <40% | 40-50 | Import as-is or with minor tweaks |
| ADOPT WITH MODIFICATIONS | <60% | 30-39 | Improve then import |
| EXTRACT PARTS | 40-80% | 20-29 | Merge into existing skill |
| SKIP | >80% or <20% | <20 | Don't import |

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
- Good quality across dimensions
- **Action**: ADOPT

### Pattern 4: The Niche Special
- Very specific use case
- High quality but rare use
- **Action**: ADOPT WITH MODIFICATIONS (make more generic)

### Pattern 5: The Almost-There
- Good concept, poor execution
- Low quality scores
- **Action**: ADOPT WITH MODIFICATIONS or rebuild with create-skill

## Tips for Effective Evaluation

### Before Evaluation
1. **Quick scan**: Read the prompt briefly first
2. **Check source**: Is it from reputable source?
3. **Check license**: Can you legally use it?

### During Evaluation
1. **Trust the metrics**: Don't override scores without good reason
2. **Consider context**: Your team's needs may differ from general assessment
3. **Look for patterns**: Does it teach you something valuable even if you skip it?

### After Evaluation
1. **Act on recommendation**: Don't just evaluate, execute
2. **Track outcomes**: Note which adopted prompts get used
3. **Iterate**: Re-evaluate periodically

## Next Steps

After completing this tutorial:

1. **Find prompts**: Browse GitHub awesome lists, blogs, registries
2. **Evaluate systematically**: Use this skill for all external prompts
3. **Build curated library**: Only adopt high-value prompts
4. **Share evaluations**: Help team make informed decisions
5. **Measure value**: Track which adopted prompts get actual use

## Related Skills

- `import-prompt-unchanged` - Import evaluated prompts as-is
- `convert-prompt` - Modernize adopted prompts to OLAF standards
- `create-skill` - Build OLAF-native version of adopted prompts
- `validate-prompt-value` - Re-evaluate existing OLAF prompts
