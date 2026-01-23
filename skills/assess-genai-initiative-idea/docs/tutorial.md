# Tutorial: assess-genai-initiative-idea

## Introduction

This tutorial guides you through using the `assess-genai-initiative-idea` skill to conduct a comprehensive evaluation of a GenAI solution proposal. By the end, you'll have a structured assessment document with research findings and actionable recommendations.

## Prerequisites

Before starting, ensure you have:

- [ ] A clear GenAI use case or problem domain to assess
- [ ] Access to web search capabilities for the research phase
- [ ] Time to complete the 10-question questionnaire thoughtfully
- [ ] Stakeholder context information (optional but recommended)

## Step-by-Step Instructions

### Step 1: Define Your Assessment Scope

Start by clearly articulating the GenAI initiative you want to assess.

**Action:** Prepare a concise description of your GenAI use case.

**Example:**
```
assessment_scope: "Automated document summarization for legal contracts"
```

**Tips:**
- Be specific about the problem domain
- Avoid vague descriptions like "use AI to improve things"
- Include the target application area

### Step 2: Invoke the Skill

Trigger the assessment workflow with your parameters.

**Action:** Provide the required parameters to start the assessment.

```
Skill: assess-genai-initiative-idea
Parameters:
  - assessment_scope: "Automated document summarization for legal contracts"
  - stakeholder_context: "Legal team, 200+ contracts reviewed monthly"
  - timeline_constraints: "6 months to pilot"
```

**Expected Response:** The skill will confirm readiness and begin the questionnaire phase.

### Step 3: Complete the Questionnaire

Answer all 10 structured questions thoroughly.

**Core Problem Analysis (Questions 1-4):**

1. **What is the core problem or opportunity?**
   - Describe the specific pain point GenAI should address
   
2. **Why is solving this important now?**
   - Explain urgency and impact if not addressed
   
3. **Describe your current process**
   - Detail existing workflow for this need
   
4. **Where do you see GenAI providing value?**
   - Identify specific automation opportunities

**User and Impact Analysis (Questions 5-8):**

5. **Who are the main users?**
   - Describe daily tasks and pain points
   
6. **What outcomes do you expect?**
   - Define specific improvements
   
7. **What solutions have you tried?**
   - List manual, digital, or AI alternatives
   
8. **Why didn't previous solutions work?**
   - Explain gaps in existing approaches

**Business and Technical Constraints (Questions 9-10):**

9. **What are the expected business benefits?**
   - Include funding needs and target market
   
10. **Are there constraints to consider?**
    - Data, compliance, or integration requirements

**Tips:**
- Provide detailed, specific answers
- Avoid generic responses that could apply to any project
- Include quantifiable metrics where possible

### Step 4: Review and Sign Off

The skill will analyze your responses and present them for review.

**Action:** Review the generated data file and confirm accuracy.

**What to Check:**
- All responses captured correctly
- No critical information missing
- Initiative name is appropriate (3 words max)

**If Issues Found:**
- The skill will rate issues as Critical, Important, or Suggestion
- Address Critical issues before proceeding to research
- Important issues can be noted for later consideration

### Step 5: Research Phase

The skill conducts web research across multiple platforms.

**Platforms Searched:**
- GitHub repositories
- Medium articles
- Reddit discussions
- Industry publications
- Academic papers

**Action:** Wait for research completion (minimum 5 sources).

**Expected Output:**
- Similar initiatives and implementations
- Alternative approaches to consider
- Common challenges and pitfalls

### Step 6: Challenge and Justify

The skill will challenge your proposal with alternatives.

**Action:** Provide justification for rejecting suggested alternatives.

**Example Challenge:**
```
Alternative Found: "Pre-built contract analysis API from LegalTech vendor"
Question: Why not use this existing solution instead of building custom?
```

**Your Response:**
```
Justification: "Existing solutions don't support our specific contract 
templates and require data to leave our secure environment, which 
violates compliance requirements."
```

### Step 7: Review Final Assessment

Receive the comprehensive assessment document.

**Location:** `[staging_dir]/genai-assessments/[initiative_name]-data.md`

**Document Sections:**
1. Initiative Overview
2. Questionnaire Responses
3. Alternatives and Challenges
4. Implementation Challenges
5. Conclusion and Recommendations

**Action:** Review recommendations and determine next steps.

## Verification Checklist

After completing the assessment, verify:

- [ ] All 10 questionnaire questions answered completely
- [ ] Initiative name generated and data file created
- [ ] User review and sign-off obtained for responses
- [ ] Response quality analysis completed with issue ratings
- [ ] Web research conducted across minimum 5 sources
- [ ] Alternatives and challenges documented comprehensively
- [ ] Implementation challenges identified and analyzed
- [ ] Alternative approaches proposed and user justification obtained
- [ ] Final recommendations provided with actionable next steps
- [ ] Complete assessment document delivered with all chapters

## Troubleshooting

### Issue: Questionnaire Responses Flagged as Generic

**Symptom:** Skill requests more specific information repeatedly.

**Solution:**
- Add concrete numbers and metrics
- Include specific examples from your organization
- Reference actual pain points experienced by users

### Issue: Web Search Returns Limited Results

**Symptom:** Research phase finds fewer than 5 sources.

**Solution:**
- Broaden search terms
- Try alternative phrasings of your use case
- Consider adjacent problem domains

### Issue: Critical Gaps Identified

**Symptom:** Skill stops and requests clarification.

**Solution:**
- Address the specific gap identified
- Consult with stakeholders if needed
- Provide additional context or constraints

### Issue: Unable to Justify Rejecting Alternatives

**Symptom:** Proposed alternatives seem viable.

**Solution:**
- Consider if the alternative might actually be better
- Document specific requirements the alternative doesn't meet
- Discuss with stakeholders before proceeding

## Next Steps

After completing the assessment:

1. **Share with Stakeholders:** Distribute the assessment document to decision-makers
2. **Create Decision Record:** Use `create-decision-record` skill to document the final decision
3. **Plan Implementation:** If proceeding, use findings to inform project planning
4. **Address Challenges:** Create mitigation plans for identified implementation challenges
5. **Monitor Alternatives:** Keep track of alternative solutions for future consideration
