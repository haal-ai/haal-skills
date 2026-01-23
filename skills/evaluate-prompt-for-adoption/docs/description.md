# Evaluate Prompt for Adoption

## Overview

Evaluate Prompt for Adoption systematically assesses external prompts from GitHub, awesome lists, registries, or the web to determine if they're worth adopting into your OLAF framework. It provides a structured evaluation framework with quality scoring and actionable recommendations.

## Purpose

Before importing every interesting prompt you find, you need to evaluate whether it adds value, duplicates existing capabilities, meets quality standards, and is worth the maintenance burden. This skill provides a comprehensive evaluation framework to make informed adoption decisions.

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
- Overlap percentage calculation (0-100%)
- Unique feature identification
- Optional check against user's available skills list
- Merge vs adopt decision support

**Similarity Verdicts:**
- **HIGH (>80%)**: Already have this, skip unless significantly better
- **MEDIUM (40-80%)**: Partial overlap, extract unique parts
- **LOW (<40%)**: New capability, evaluate for adoption

### 3. Multi-Dimensional Quality Assessment

**Clarity Assessment:**
- Clear objective stated?
- Well-structured sections?
- Unambiguous instructions?
- Examples provided?
- Expected outputs defined?

**Genericity Assessment:**
- Applicable to multiple use cases?
- Not too narrow/specific?
- Reusable across projects/teams?
- Domain-agnostic or valuable niche?

**Parameterizability Assessment:**
- Can be parameterized (inputs/outputs)?
- Supports configuration/options?
- Flexible for different contexts?

**LLM Independence Assessment:**
- Works across different LLMs?
- Not tied to specific agent framework?
- No vendor-specific syntax?
- Uses standard prompt patterns?

**Structure Quality Assessment:**
- Logical flow/sequence?
- Proper sections (input, process, output)?
- Error handling included?
- Validation steps defined?
- Clear success criteria?

### 4. Persona & Use Case Analysis
Identifies target users:
- Developer personas (junior, senior, architect, lead)
- Domain experts (data scientist, designer, analyst)
- Roles (individual contributor, team lead, manager)
- Expertise levels (beginner, intermediate, advanced)
- Use case frequency (daily, weekly, monthly, rare)

### 5. Value-Add Estimation

**Frequency × Specificity Matrix:**
```
         │ High Frequency        │ Low Frequency
─────────┼──────────────────────┼─────────────────
Generic  │ HIGH VALUE ⭐⭐⭐     │ MEDIUM VALUE ⭐⭐
         │ (everyday tool)      │ (useful helper)
─────────┼──────────────────────┼─────────────────
Specific │ MEDIUM VALUE ⭐⭐     │ LOW VALUE ⭐
         │ (niche but frequent) │ (very situational)
```

**AI Necessity Assessment:**
- ✅ Required - Needs reasoning/creativity/judgment
- ⚠️ Beneficial - AI helps but script could work
- ❌ Optional - Better as script/tool/automation

**Value Score (0-50 points):**
- 40-50: **EXCELLENT** - Adopt immediately
- 30-39: **GOOD** - Strong candidate
- 20-29: **MODERATE** - Consider with improvements
- 10-19: **LOW** - Skip or extract specific parts
- 0-9: **POOR** - Not worth adopting

### 6. Actionable Recommendations

Clear recommendations with rationale:
- **ADOPT** - Import as-is or with minor tweaks
- **ADOPT WITH MODIFICATIONS** - Needs improvements first
- **EXTRACT PARTS** - Take specific patterns, not whole prompt
- **SKIP** - Not valuable or duplicative

## Usage

**Command**: `evaluate prompt for adoption`

**Protocol**: Act

**When to Use**: Use this skill before importing any external prompt, when exploring awesome lists or registries, after seeing interesting blog post prompts, when team members suggest new prompts, or during periodic prompt library audits.

## Parameters

### Required Inputs (one of):
- **source_url**: URL to the prompt (GitHub, gist, registry, webpage)
- **source_text**: Direct paste of prompt content

### Optional Inputs
- **source_description**: Brief description of what the prompt does
- **available_skills_list**: List of skills the user currently has available (improves duplicate detection)

### Context Requirements
- Internet access for URL fetching
- Access to existing OLAF skills for similarity checking
- Semantic search capability

## Output

**Deliverables**:
- Comprehensive evaluation report
- Source information and metadata
- Similarity analysis with overlap percentages
- Quality assessment across 5 dimensions
- Persona and use case analysis
- Value-add score (0-50)
- Final recommendation with rationale
- Concrete next steps

**Format**: Structured markdown report with tables and clear sections

## Examples

### Example 1: GitHub Awesome List Discovery

**Input**:
```
source_url: https://github.com/awesome/prompts/blob/main/code-reviewer.md
```

**Output**:
```
## Evaluation Report

### Similarity Analysis
- Similar OLAF Skills: review-code (60% overlap)
- Unique Features: Specific review criteria checklist
- Similarity Verdict: MEDIUM

### Quality Assessment
| Dimension | Rating |
|-----------|--------|
| Clarity | Clear |
| Genericity | Generic |
| Parameterizability | Moderate |
| LLM Independence | Agnostic |
| Structure | Acceptable |

### Value Score: 38/50 (GOOD)

### Recommendation: ADOPT WITH MODIFICATIONS
Extract unique review criteria, merge into existing review-code skill
```

### Example 2: Low-Value Prompt Rejection

**Input**:
```
source_url: https://example.com/very-specific-prompt
```

**Output**:
```
### Quality Assessment
| Dimension | Rating |
|-----------|--------|
| Genericity | Too Narrow |
| Parameterizability | Hardcoded |

### Value Score: 14/50 (LOW)

### Recommendation: SKIP
Too specific to one tech stack. Low reuse potential.
```

### Example 3: Excellent Find

**Input**:
```
source_url: https://github.com/awesome/prompts/api-design-reviewer.md
```

**Output**:
```
### Quality Assessment
All dimensions: Clear/Generic/High/Agnostic/Well-Structured

### Value Score: 45/50 (EXCELLENT)

### Recommendation: ADOPT
Exceptional quality. Fills gap in OLAF. High reuse potential.
Suggested skill name: review-api-design
Priority: HIGH
```

## Related Skills

- **convert-prompt-to-skill**: Package adopted prompts into OLAF skills
- **create-skill**: Build OLAF-native version of adopted prompts
- **check-prompt-compliance**: Validate prompts against OLAF standards

## Tips & Best Practices

1. **Always evaluate first**: Never import prompts without evaluation
2. **Check similarity**: Avoid duplicating existing capabilities
3. **Trust the metrics**: Don't override scores without good reason
4. **Consider context**: Your team's needs may differ from general assessment
5. **Look for patterns**: Even skipped prompts may teach valuable techniques
6. **Act on recommendations**: Don't just evaluate, execute
7. **Track outcomes**: Note which adopted prompts get actual use

## Limitations

- Requires internet access for URL fetching
- Similarity detection depends on semantic search quality
- Cannot validate runtime behavior, only static content
- Quality assessment is based on OLAF conventions
- Value estimation is subjective and context-dependent
- Cannot automatically detect licensing issues
- Batch evaluation of large collections may be time-consuming

