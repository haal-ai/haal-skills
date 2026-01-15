---
task_id: "apply-test-learning"
task_name: "Apply and Test Learning"
dependencies: ["context.synthesized_knowledge"]
conditions: []
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

# Apply and Test Learning

## Input Context
**Required Context Variables**: 
- `context.synthesized_knowledge`: Organized knowledge by topic
- `context.learning_goals`: Original learning goals
- `context.application_context`: User's application context
- `context.success_criteria`: Success criteria for learning
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Create Practical Applications and Validate Understanding

1. **Create Practical Applications of New Knowledge**:
   - Identify real-world use cases for learned concepts
   - Design examples relevant to user's application context
   - Create code snippets, workflows, or procedures (if applicable)
   - Develop step-by-step implementation guides
   - Consider different scenarios or edge cases

2. **Test Understanding Through Exercises**:
   - Create comprehension check questions
   - Design small exercises or challenges
   - Propose mini-projects or experiments
   - Suggest ways to practice new skills
   - Identify opportunities to apply knowledge immediately

3. **Document Key Insights and Actionable Takeaways**:
   - Extract most important lessons learned
   - List actionable next steps
   - Identify common pitfalls to avoid
   - Note best practices or recommended approaches
   - Highlight prerequisites for successful application

4. **Validate Against Success Criteria**:
   - Check each success criterion from learning goals
   - Assess whether learning objectives were met
   - Identify any gaps or areas needing more study
   - Rate confidence level for each learning goal

5. **Create Application Summary**:
   ```markdown
   **Practical Applications**:
   
   Use Cases:
   - [Use case 1]: [description]
   - [Use case 2]: [description]
   
   Implementation Examples:
   - [Example 1]
   - [Example 2]
   
   Understanding Validation:
   ✓ [Criterion 1]: Achieved
   ✓ [Criterion 2]: Achieved
   ⚠ [Criterion 3]: Partially achieved
   
   Actionable Takeaways:
   - [Takeaway 1]
   - [Takeaway 2]
   ```

## Output Requirements

**State Updates**:
- `context.practical_applications`: Array of use cases and examples
- `context.understanding_validation`: Success criteria assessment
- `context.actionable_takeaways`: Key insights and next steps
- `context.knowledge_gaps`: Remaining areas for future learning
- `task_status.apply-test-learning`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- All application and validation results will be included in learning report
