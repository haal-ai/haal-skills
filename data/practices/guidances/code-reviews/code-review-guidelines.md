# Code Review Practice Guidelines

## Purpose
Establish systematic approaches for providing constructive, effective code reviews that improve code quality while maintaining positive team dynamics.

## Core Principles

### 1. Focus on Code, Not Person
- ❌ "You didn't handle errors properly"
- ✅ "This function could benefit from error handling for the network call"

### 2. Be Specific and Actionable
- ❌ "This looks messy"
- ✅ "Consider extracting this 50-line function into smaller, single-purpose functions"

### 3. Explain the Why
- ❌ "Use const instead of let"
- ✅ "Using const here prevents accidental reassignment and makes the intent clearer"

## Review Focus Areas

### 1. **Functionality & Logic**
- Does the code solve the intended problem?
- Are edge cases handled appropriately?
- Is the logic clear and correct?

**Example Feedback:**
```
"The validation logic looks good, but what happens if the email field is undefined? 
Consider adding a check: if (!email?.trim()) return false;"
```

### 2. **Code Quality & Maintainability**
- Is the code readable and well-structured?
- Are functions/classes appropriately sized?
- Is naming descriptive and consistent?

**Example Feedback:**
```
"The function name 'processData' is quite generic. Something like 'validateUserInput' 
or 'sanitizeFormData' would better describe what this function does."
```

### 3. **Performance & Efficiency**
- Are there obvious performance issues?
- Is the solution appropriately efficient?
- Are resources managed properly?

**Example Feedback:**
```
"This loop creates a new array on each iteration. Consider using Array.reduce() 
or pre-allocating the array to improve performance for large datasets."
```

### 4. **Security & Safety**
- Are inputs properly validated?
- Are security best practices followed?
- Are potential vulnerabilities addressed?

**Example Feedback:**
```
"Direct string interpolation in SQL queries can lead to injection attacks. 
Consider using parameterized queries or an ORM instead."
```

## Constructive Feedback Techniques

### 1. **Suggest, Don't Demand**
- ❌ "Change this to use async/await"
- ✅ "Consider using async/await here for better readability"
- ✅ "What do you think about using async/await instead of .then()?"

### 2. **Ask Questions to Guide Discovery**
- "How do you think this might behave with an empty array?"
- "What would happen if the API returns a 500 error here?"
- "Have you considered how this scales with larger datasets?"

### 3. **Provide Context and Alternatives**
```
"While this approach works, using the built-in Array.find() method might be 
more readable and performant:

const user = users.find(u => u.id === targetId);

This also handles the case where no match is found more gracefully."
```

### 4. **Acknowledge Good Work**
- "Nice use of the factory pattern here!"
- "Great error handling - this makes debugging much easier"
- "I like how you've made this function pure and testable"

## Review Process Protocol

### 1. **Preparation Phase**
- Understand the context and requirements
- Review related documentation or tickets
- Check if there are existing patterns to follow

### 2. **Review Phase**
- Read through the entire change first for context
- Focus on one aspect at a time (logic, then style, then performance)
- Use inline comments for specific issues
- Use general comments for overall feedback

### 3. **Feedback Phase**
- Prioritize feedback (critical vs. nice-to-have)
- Group related comments together
- Provide examples or links to documentation when helpful

### 4. **Follow-up Phase**
- Be available for questions and clarification
- Re-review changes promptly
- Acknowledge when concerns are addressed

## Feedback Categories and Examples

### Critical Issues (Must Fix)
```
"⚠️ CRITICAL: This creates a SQL injection vulnerability. 
The user input needs to be sanitized before being used in the query."
```

### Important Improvements (Should Fix)
```
"💡 IMPROVEMENT: This function has multiple responsibilities. 
Consider splitting it into 'validateInput' and 'saveToDatabase' functions."
```

### Suggestions (Nice to Have)
```
"✨ SUGGESTION: You might find the destructuring assignment syntax 
cleaner here: const { name, email } = user;"
```

### Questions (For Understanding)
```
"❓ QUESTION: I'm curious about the choice to use setTimeout here. 
Is this for debouncing user input?"
```

## Common Review Patterns

### 1. **The Compliment Sandwich**
1. Start with something positive
2. Provide constructive feedback
3. End with encouragement

Example:
```
"Great job implementing the user authentication flow! The token validation 
logic is solid. One thing to consider is adding rate limiting to prevent 
brute force attacks. Overall, this is a solid foundation that we can build on."
```

### 2. **The Teaching Moment**
```
"I noticed you're manually formatting dates. JavaScript has a built-in 
Intl.DateTimeFormat API that handles localization automatically:

const formatter = new Intl.DateTimeFormat('en-US');
const formattedDate = formatter.format(new Date());

This approach is more robust for international users."
```

### 3. **The Alternative Approach**
```
"This works well! Another approach you might consider is using a Map 
instead of an object for the cache, since Maps have better performance 
for frequent additions and deletions."
```

## Team Dynamics and Culture

### 1. **Respond Positively to Feedback**
- Thank reviewers for their time and insights
- Ask clarifying questions when feedback is unclear
- Explain your reasoning when you disagree respectfully

### 2. **Create Psychological Safety**
- Encourage questions and learning
- Share your own mistakes and learning experiences
- Focus on continuous improvement, not perfection

### 3. **Balance Speed and Quality**
- Prioritize critical issues for immediate fixes
- Create follow-up tickets for non-critical improvements
- Distinguish between personal preference and best practices

## Tools and Automation

### 1. **Use Linters and Formatters**
- Automate style and formatting issues
- Focus human review time on logic and architecture
- Ensure consistent code style across the team

### 2. **Leverage CI/CD Checks**
- Automated testing should catch functional issues
- Security scanners can identify common vulnerabilities
- Performance profiling can highlight efficiency issues

### 3. **Code Review Checklists**
Create team-specific checklists for common review areas:
- [ ] Functions have clear, descriptive names
- [ ] Error cases are handled appropriately
- [ ] Tests cover the new functionality
- [ ] Documentation is updated if needed
- [ ] No obvious security vulnerabilities
- [ ] Performance implications are considered

## Learning and Growth

### 1. **Use Reviews as Learning Opportunities**
- Explain the reasoning behind suggestions
- Share relevant articles or documentation
- Discuss trade-offs and alternative approaches

### 2. **Review Your Own Reviews**
- Periodically assess if your feedback is helpful
- Ask team members for feedback on your review style
- Adjust approach based on team preferences and culture

### 3. **Stay Current with Best Practices**
- Regularly update review criteria based on new learnings
- Incorporate lessons from production issues
- Share interesting staging with the team

## Measuring Review Effectiveness

### Positive Indicators
- Decreased bugs in production
- Improved code readability and maintainability
- Increased knowledge sharing across the team
- Faster onboarding of new team members

### Warning Signs
- Reviews become contentious or personal
- Developers avoid requesting reviews
- Review feedback is consistently ignored
- Review process significantly slows down development

Remember: The goal of code review is to improve code quality, share knowledge, and build better software together. Every review is an opportunity to learn and teach.