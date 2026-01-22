# Prompt Engineering Best Practices

This guide provides specific prompt engineering techniques for optimal results in your applications.

## Success Criteria for This Document
This principles document is effective when:
- Each principle follows the structure it teaches
- Examples demonstrate the principles in action
- No duplicate or contradictory content exists
- Numbering is sequential and logical
- Formatting is consistent throughout

---

## Core Principles

### 1. Use Imperative Language
Always use commanding, action-oriented language for clarity and consistency:

**Effective patterns:**
- "You WILL" - for required actions
- "You MUST" - for critical requirements  
- "You NEVER" - for prohibited actions
- "MANDATORY" - for non-negotiable requirements
- "CRITICAL" - for extremely important instructions

**Example: Task Instructions**
```text
Less effective: Please analyze the code and make improvements

More effective: You WILL analyze the code structure and identify three specific improvement opportunities. You MUST provide concrete examples for each recommendation.
```

### 2. Be Explicit with Instructions and Success Criteria
Always define what constitutes successful completion and provide clear, measurable outcomes:

**Effective patterns:**
- Define exact requirements upfront
- Specify success metrics
- Include validation steps
- Provide concrete examples

**Example: Creating an analytics dashboard**
```text
Less effective: Create an analytics dashboard

More effective: You WILL create an analytics dashboard that includes:
- Real-time data visualization
- Interactive filtering capabilities
- Export functionality
- Mobile-responsive design

Success criteria: Dashboard loads in under 3 seconds and displays data correctly on all screen sizes.
```

### 3. Add Context to Improve Performance
Providing context or motivation behind your instructions helps models better understand your goals and deliver more targeted responses.

**Effective patterns:**
- Explain WHY requirements matter
- Provide background context
- Connect instructions to business outcomes
- Include motivation for specific behaviors

**Example: Task Instructions**
```text
Less effective: Please analyze the code and make improvements

More effective: You WILL analyze the code structure and identify three specific improvement opportunities. You MUST provide concrete examples for each recommendation. This analysis is critical because the code will be deployed to production next week and needs to meet our performance standards.
```

### 4. Structure with Clear Separators (OpenAI 2024)
Put instructions at the beginning of prompts and use clear separators to distinguish instructions from context.

**Effective patterns:**
- Use `###` or `"""` to separate instructions from context
- Place instructions BEFORE the context/data
- Use XML-style tags for complex prompts
- Maintain visual hierarchy

**Example:**
```text
Summarize the text below as a bullet point list of the most important points.

Text: """{text input here}"""
```

**Example with XML markup:**
```text
<!-- <validation_phase> -->
You WILL first validate all input parameters
<!-- </validation_phase> -->

<!-- <execution_phase> -->  
You WILL then execute the core logic
<!-- </execution_phase> -->
```

### 5. Tool Usage Explicitness (Anthropic 2024)
Modern models need explicit direction about when to use tools vs just suggesting changes.

**Effective patterns:**
- Use `<default_to_action>` tags for proactive behavior
- Use `<do_not_act_before_instructions>` for cautious behavior
- Be explicit about implementing vs suggesting
- Define tool usage triggers

**For proactive behavior:**
```text
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is unclear, infer the most useful likely action and proceed, using tools to discover any missing details instead of guessing.
</default_to_action>
```

**For cautious behavior:**
```text
<do_not_act_before_instructions>
You MUST NOT jump into implementation or change files unless clearly instructed to make changes. When the user's intent is ambiguous, default to providing information, doing research, and providing recommendations rather than taking action.
</do_not_act_before_instructions>
```

### 6. Progressive Specificity (Prompt Generation)
Start with the smallest set of instructions that can work, then add specificity only when the model output misses your intent.

**Rationale:** When you're designing prompts (not training models), the lever you have is *instruction clarity*, not fine-tuning. Use examples sparingly and only to lock down format or edge cases.

**Effective patterns (escalation order):**
1. **Clarify the goal**: State the desired outcome unambiguously
2. **Constrain the output**: Add length, structure, and formatting requirements
3. **Add acceptance checks**: Add explicit success criteria / validation checklist
4. **Add examples only if needed**: Provide one example of the exact format you want (avoid adding extra behavior)
5. **Add negative examples only if needed**: Show what NOT to do *and* what to do instead

**Example escalation (prompt spec):**
```text
# Minimal
You WILL generate a skill prompt for the user's request.

# Add constraints (format + structure)
You WILL generate a skill prompt in Markdown.
You MUST include sections: Input Parameters, Process, Success Criteria, Error Handling.

# Add acceptance checks
Success criteria: the prompt contains all required sections and references external files instead of embedding them.

# Add an example only to lock the format
Example section header format:
## Input Parameters
1. **param**: type - description
```

### 7. Include Comprehensive Error Handling
Always anticipate and address potential issues with clear guidance.

**Effective patterns:**
- List specific error scenarios
- Provide recovery steps
- Offer alternative approaches
- Include validation checkpoints

**Example:**
```text
## Error Handling
You WILL handle these scenarios:
- **Missing Parameters**: Request specific missing items from user
- **Invalid Input**: Provide clear error message and correction guidance
- **Tool Failures**: Offer alternative approaches or manual steps
- **Validation Failures**: Stop process and request user guidance
```

### 8. Maintain Consistency and Formatting
Apply uniform structure and formatting throughout your prompts.

**Effective patterns:**
- Use consistent headings and levels
- Apply uniform command formatting
- Standardize parameter descriptions
- Use consistent language tone
- Apply template structure exactly

**Validation checklist:**
- [ ] All imperative language follows "You WILL/MUST/NEVER" patterns
- [ ] Every instruction has clear success criteria
- [ ] Context and motivation are provided
- [ ] Separators are used consistently
- [ ] Tool usage is explicitly defined
- [ ] Complexity progresses appropriately
- [ ] Error handling is comprehensive
- [ ] Formatting is uniform throughout

---

## Quick Reference

| Principle | Key Pattern | Example |
|-----------|-------------|---------|
| Imperative Language | "You WILL/MUST/NEVER" | You WILL analyze the code |
| Explicit Criteria | Define success metrics | Loads in under 3 seconds |
| Context | Explain WHY | Critical for production deployment |
| Structure | Use separators | Text: """content""" |
| Tool Usage | Action tags | `<default_to_action>` |
| Progressive | Escalate specificity | Start minimal, then add constraints/examples |
| Error Handling | List scenarios | Missing parameters: request from user |
| Consistency | Uniform format | Same structure throughout |

### 3. Add Context to Improve Performance

Always explain WHY instructions matter:

**Example: Formatting preferences**
```text
Less effective: NEVER use ellipses

More effective: You MUST avoid ellipses because your response will be read aloud by a text-to-speech engine, and ellipses cannot be properly pronounced by TTS systems.
```

### 4. Structure with XML-Style Markup

Use XML-style tags for complex prompts to improve organization:

```text
<!-- <validation_phase> -->
You WILL first validate all input parameters
<!-- </validation_phase> -->

<!-- <execution_phase> -->  
You WILL then execute the core logic
<!-- </execution_phase> -->

<!-- <output_phase> -->
You WILL generate outputs in the specified format
<!-- </output_phase> -->
```

### 5. Include Validation and Error Handling

Always anticipate and address potential issues:

```text
## Error Handling
You WILL handle these scenarios:
- **Missing Parameters**: Request specific missing items from user
- **Invalid Input**: Provide clear error message and correction guidance
- **Tool Failures**: Offer alternative approaches or manual steps
- **Validation Failures**: Stop process and request user guidance
```

### 6. Clarity and Specificity

Every instruction should be specific and measurable:
- Define exact formats and expected outputs
- Provide concrete examples
- Specify success metrics
- Include validation steps
- Document assumptions
- List dependencies

### 7. Progressive Disclosure

Organize information from high-level to detailed:
- Start with overview and purpose
- Present required parameters clearly
- Detail execution steps
- Include error scenarios
- Provide next steps guidance

### 8. Consistency and Formatting

Maintain consistent formatting throughout:
- Use consistent headings and levels
- Apply uniform command formatting
- Standardize parameter descriptions
- Use consistent language tone
- Apply template structure exactly
