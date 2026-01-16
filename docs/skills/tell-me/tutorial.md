# Tell Me: Step-by-Step Tutorial

**How to Execute the "Tell Me" Skill for Quick Knowledge Retrieval**

This tutorial shows how to get instant answers about your project from existing documentation.

## Prerequisites

- OLAF framework installed and loaded
- `onboard-me` skill executed (recommended for best results)
- OR existing documentation in `.olaf/data/practices/` folder

## Step-by-Step Instructions

### Step 1: Invoke the Tell Me Skill
Start the knowledge retrieval process

**User Action:**
Type one of these commands:
```bash
olaf tell me [your question]
olaf ask about [topic]
olaf info about [subject]
```

**Example:**
```bash
olaf tell me how to build this project
```

**OLAF Response:**
OLAF will search existing documentation for answers

### Step 2: OLAF Searches Documentation
**What OLAF Does:**
- Searches `.olaf/data/product/{repo}/` for project-specific docs
- Searches `.olaf/data/practices/` for team practices
- Searches root docs (README.md, CONTRIBUTING.md)
- Ranks results by relevance

**You Should See:** Search in progress message (if configured)

### Step 3: Results Returned
**Scenario A: Documentation Found**

**What OLAF Does:**
- Extracts relevant sections from found documents
- Synthesizes a comprehensive answer
- Includes source citations with file paths and line numbers

**Example Output:**
```markdown
# How to Build This Project

Prerequisites:
- Node.js 18+
- npm 9+

Build Steps:
1. Install dependencies: npm install
2. Build the project: npm run build
3. Run tests: npm test

Development Mode:
- npm run dev (starts development server on port 3000)

---
📚 Sources:
- .olaf/data/product/my-repo/repo-guide.md (lines 45-62)
- .olaf/data/product/my-repo/development-setup.md (lines 12-18)
```

**Scenario B: No Documentation Found**

**What OLAF Does:**
- Reports that no documentation exists for the topic
- Suggests the appropriate skill to generate the documentation

**Example Output:**
```markdown
❌ No existing documentation found for: "contributor risk analysis"

💡 Suggested Action:
Run `olaf analyze-contributor-risk` to generate this information.

This skill will:
- Analyze git commit history
- Identify key contributors
- Assess knowledge concentration
- Generate risk mitigation recommendations
```

### Step 4: Browse Available Documentation (Optional)
**User Action:**
Type `olaf tell me` without a question

**What OLAF Does:**
- Lists all available documentation topics
- Groups by category (Development, Architecture, Operations, etc.)
- Shows what questions can be answered

**Example Output:**
```markdown
📚 Available Documentation

🔨 For Developers:
• How do I build this project locally?
• How do I run the application?
• What are the coding standards?
• How do I run tests?

🏗️ For Architects:
• What architectural pattern is used?
• What are the key components?

📊 For Managers:
• What is the AI impact analysis?
• What are the contributor risks?
```

## Verification Checklist

✅ **Answer is relevant to your question**
✅ **Sources are cited with file paths**
✅ **Information comes from YOUR repository**
✅ **Suggested skills are actionable (if no docs found)**

## Troubleshooting

### Issue: "No artifacts found"
**Cause:** No documentation has been generated yet

**Solution:** 
```bash
olaf onboard-me
```
This will generate comprehensive project documentation.

### Issue: "Low relevance results"
**Cause:** Question may be too vague or use different terminology

**Solutions:**
- Rephrase your question with more specific terms
- Try broader keywords
- Browse available docs: `olaf tell me`
- Check if topic requires analysis: try suggested skill

### Issue: "Answer is incomplete"
**Cause:** Documentation may not cover all aspects of your question

**Solutions:**
- Ask more specific sub-questions
- Check source files directly for more detail
- Run suggested analysis skill to generate comprehensive docs
- Contribute missing information to documentation

### Issue: "Wrong topic returned"
**Cause:** Keywords matched different documentation

**Solutions:**
- Use more specific terminology
- Include context: "tell me about [topic] in [area]"
- Exclude unrelated terms: "tell me about builds, not deployments"

## Common Use Cases

### 1. Onboarding New Developers
**Question:** "How do I get started with this project?"

**Expected Flow:**
1. Tell me searches for setup guides
2. Returns build instructions, prerequisites, first-run steps
3. Cites development setup documentation

### 2. Checking Team Practices
**Question:** "What are our git commit message standards?"

**Expected Flow:**
1. Tell me searches practices folder
2. Returns git guidelines from `.olaf/data/practices/git-guidelines.md`
3. Shows commit message format and examples

### 3. Understanding Architecture
**Question:** "What design patterns are used in this codebase?"

**Expected Flow:**
1. Tell me searches architecture documentation
2. Returns patterns from `.olaf/data/product/{repo}/architecture-overview.md`
3. Cites specific sections with line numbers

### 4. Pre-Analysis Check
**Question:** "What metrics do we have on AI usage?"

**Expected Flow (No Docs):**
1. Tell me searches and finds no documentation
2. Suggests: "Run `olaf measure-ai-impact`"
3. Explains what the skill will generate

## Advanced Usage

### Scoped Searches
```bash
# Search only in specific area
olaf tell me about error handling in the API layer

# Search for specific file types
olaf tell me about configuration files
```

### Follow-up Questions
```bash
# Initial question
olaf tell me how to deploy

# Follow-up based on answer
olaf tell me more about production deployment prerequisites
```

### Cross-Referencing
```bash
# Ask about related topics
olaf tell me about testing strategy
olaf tell me about code coverage requirements
```

## Key Learning Points

1. **Documentation-First**: Always searches existing docs before suggesting analysis
2. **Source Citations**: Every answer includes file references for verification
3. **Smart Fallback**: Suggests the right skill when documentation is missing
4. **Repository-Specific**: Only answers from YOUR project's documentation
5. **Fast & Lightweight**: No heavy analysis, just quick retrieval

## Integration with Other Skills

### With onboard-me
```bash
# First: Generate documentation
olaf onboard-me

# Then: Ask questions about the project
olaf tell me how to build this project
```

### With Analysis Skills
```bash
# Check if analysis exists
olaf tell me about contributor risk

# If not, run suggested skill
olaf analyze-contributor-risk

# Then ask again
olaf tell me about contributor risk
```

## Expected Timeline

- **Total execution time:** 5-30 seconds
- **Search time:** 2-10 seconds (depends on documentation size)
- **Answer synthesis:** 3-20 seconds (depends on answer complexity)
- **User action required:** Initial question only (no interactive prompts)

## Next Steps to Try

1. **Explore Available Docs**: Run `olaf tell me` to see what's available
2. **Ask Common Questions**: Build process, coding standards, architecture
3. **Generate Missing Docs**: Run `olaf onboard-me` if few results
4. **Use Daily**: Make it your first stop for project questions
5. **Contribute**: Add to `.olaf/data/practices/` for team-wide knowledge

## Best Practices

✅ **Do:**
- Ask specific, clear questions
- Use natural language
- Check sources for more detail
- Run suggested skills when docs missing
- Use for quick reference during coding

❌ **Don't:**
- Expect generic programming knowledge (repository-specific only)
- Ask questions requiring new analysis without running suggested skill
- Ignore source citations (verify information)
- Skip running `onboard-me` first

## Success Indicators

You're using tell-me effectively when:
- Getting instant answers to project questions
- Saving time by not searching through files manually
- Finding accurate information with source citations
- Knowing which skill to run when documentation is missing
- Onboarding new team members faster with documentation access
