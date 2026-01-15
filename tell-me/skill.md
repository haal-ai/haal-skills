---
name: tell-me
description: Lightweight knowledge retrieval from existing artifacts with smart fallback to analysis
license: Apache-2.0
metadata:
  olaf_tags: [knowledge-retrieval, search, artifacts, onboarding]
  olaf_protocol: Act
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Tell Me - Knowledge Retrieval

## Purpose

Lightweight **search-first** knowledge retrieval that:
1. **Searches existing artifacts** in .olaf/data/context/ and .olaf/data/practices/
2. **Returns answers from found docs** - fast, no analysis needed
3. **Suggests running analysis** if no artifacts exist (onboard-me, analyze-contributor-risk, etc.)

## Input Parameters

You MUST request if not provided:
- **question**: string - User's question about the project/practices (REQUIRED)
- **repository_name**: string - Name of repository (OPTIONAL, default: auto-detect from workspace)

## User Interaction Protocol

You WILL use **Act** protocol.

## Process

### 0. Handle Missing Question

**If user invokes without a question** (`olaf tell me`):

Display persona-based question examples:
```markdown
I can help answer questions about this project. Here are some examples:

📚 **For Developers:**
- How do I build this project locally?
- How do I run the application?
- How do I run tests?
- What programming languages and frameworks are used?

🏗️ **For Architects:**
- What architectural pattern is used?
- What are the main components and their relationships?
- What external dependencies exist?

🚀 **For DevOps:**
- How is this application deployed?
- What is the CI/CD pipeline setup?
- What infrastructure is required?

🔒 **For Security:**
- How is authentication implemented?
- What security patterns are used?
- Are there any known vulnerabilities?

💼 **For Business/PM:**
- What is the business domain?
- What are the main features?

Just ask: `olaf tell me <your question>`
```

Then **exit** and wait for user to ask a specific question.

### 1. Search Existing Artifacts

**CRITICAL: Search in this EXACT order - stop at first match:**

```
Priority 1: .olaf/data/context/*/*/QUICKSTART-*.md           # ALL repo QUICKSTART guides
Priority 2: .olaf/data/kb/                                          # General knowledge base (BMS, OTF, etc.)
Priority 3: .olaf/data/practices/                                   # Team practices and standards
Priority 4: README.md, CONTRIBUTING.md                              # Root documentation
Priority 5: WEB FETCH (if technology detected)                      # Official docs from web-resources-kb-index.md
```

**Search Strategy**:
1. Extract keywords from question (case-insensitive)
2. **FIRST: List available repos** - Explore the .olaf/data/context/ directory structure to see all available repository documentation
3. **Persona detection**: Determine which QUICKSTART guide to prioritize based on question type:
   - Build/run/setup → QUICKSTART-*-DEVELOPER.md or QUICKSTART-OVERVIEW.md
   - Architecture/design → QUICKSTART-ARCHITECT.md
   - Testing → QUICKSTART-QA-ENGINEER.md
   - Business/features → QUICKSTART-BUSINESS-ANALYST.md
   - Documentation → QUICKSTART-DOCS-CONTRIBUTOR.md
4. **Search ALL repos in context/**: Search for keywords across all documentation files in the .olaf/data/context/ directory (case-insensitive)
5. **Fallback search**: If keyword search fails, look for files matching patterns with keywords in their names
6. If found → Return answer and STOP
7. If not found → Search Priority 2 (KB)
8. Continue until match found or all locations searched
9. **If still not found** → Proceed to Web Fetch (Step 1.5)

**IMPORTANT**: Don't assume repo name - search across ALL repos in .olaf/data/context/ directory

### 1.5. Web Fetch Strategy (NEW)

**Trigger Conditions**:
- Local KB search (Priority 1-4) found NO relevant results
- Question mentions a recognizable technology (MongoDB, React, Docker, etc.)
- Question is about syntax, API, configuration, or "how to" for that technology

**Web Fetch Process**:

1. **Load Web Resources Index**:
   - Read `.olaf/data/kb/web-resources-kb-index.md`
   - Extract technology entries with URLs and keywords

2. **Technology Detection**:
   - Match question keywords against index keywords
   - Examples:
     * "mongodb" → MongoDB Official Docs
     * "react hooks" → React Official Docs
     * "docker compose" → Docker Official Docs
     * "kubernetes pods" → Kubernetes Official Docs
   
3. **URL Selection**:
   - **If in index**: Use official docs URL from web-resources-kb-index.md
   - **If NOT in index**: Infer URL using common patterns:
     * `https://docs.{technology}.com/`
     * `https://{technology}.io/docs/`
     * `https://www.{technology}.org/documentation/`

4. **Fetch Web Content**:
   - Retrieve web content from detected URL
   - Provide specific query based on user question
   - Example: User asks "how to create mongodb index" → fetch from MongoDB docs with query "create index"

5. **Multi-Fetch Strategy** (if needed):
   - Primary fetch: Main technology docs
   - Secondary fetch: Related technology or best practices
   - Example: "mongodb with nodejs" → Fetch MongoDB docs + Node.js driver docs

6. **Smart Query Formation**:
   - Extract core question from user input
   - Remove filler words ("how do I", "what is", "tell me about")
   - Focus on technical terms for better search results

**Web Fetch Decision Tree (Example)**:
```
EXAMPLE Question: "How do I create an index in MongoDB?"

1. Extract keywords: ["mongodb", "create", "index"]
2. Check web-resources-kb-index.md
3. Find match: MongoDB → https://www.mongodb.com/docs/
4. Form query: "create index"
5. Fetch: Retrieve web content using URL and query
6. Synthesize answer from fetched content
7. Cite source: "📚 Source: MongoDB Official Documentation"

Note: This same process applies to any detected technology (React, Docker, PostgreSQL, etc.)
```

**Example Technologies to Auto-Fetch**:
- **Databases**: MongoDB, PostgreSQL, MySQL, Redis, Elasticsearch
- **Frameworks**: React, Vue, Angular, Spring Boot, Django, Flask
- **DevOps**: Docker, Kubernetes, Terraform, GitHub Actions
- **Languages**: Python, TypeScript, Go, Java, Scala (when asking syntax/API questions)
- **Cloud**: AWS, Azure, GCP (for service-specific questions)

**DO NOT fetch for**:
- Questions about internal/Amadeus-specific tech (BMS, OTF) - these are in local KB
- Questions about the current project/repository
- General conceptual questions better answered by synthesis

### 2. Answer from Artifacts (If Found)

**If artifacts found (local KB or web fetch):**
- Extract relevant sections
- Synthesize answer from found content
- Cite sources with file paths or URLs
- Format as concise answer

**Output Format for Local Sources**:
```markdown
# {Question}

{Answer synthesized from artifacts}

---
📚 Sources:
- {file1} (lines {X}-{Y})
- {file2} (lines {X}-{Y})
```

**Output Format for Web Sources**:
```markdown
# {Question}

{Answer synthesized from web content}

---
🌐 Sources:
- {Technology} Official Documentation: {URL}
- {Additional source if multi-fetch}: {URL}

💡 Note: This information is from external documentation. For project-specific implementation, check local artifacts.
```

**Output Format for Hybrid (Local + Web)**:
```markdown
# {Question}

{Answer combining local context with web documentation}

---
📚 Local Sources:
- {local-file} (lines {X}-{Y})

🌐 External Sources:
- {Technology} Official Documentation: {URL}
```

### 3. Suggest Analysis (If Not Found)

**If no artifacts found:**
- Identify which analysis would answer the question
- Suggest specific skill to run

**Mapping Questions → Skills**:
- "How to build/run?" → `olaf onboard-me` (generates QUICKSTART-*.md in `.olaf/data/product/context/{repo-name}/`)
- "Who are contributors?" → `olaf analyze-contributor-risk` (generates report in `.olaf/data/product/{repo-name}/`)
- "What is AI impact?" → `olaf measure-ai-impact` (generates report in `.olaf/data/product/{repo-name}/`)
- "Architecture/tech stack?" → `olaf onboard-me` (generates QUICKSTART-ARCHITECT.md)
- "Testing approach?" → `olaf onboard-me` (generates QUICKSTART-QA-ENGINEER.md)
- "Business value/features?" → `olaf onboard-me` (generates QUICKSTART-BUSINESS-ANALYST.md)
- "Coding standards?" → Search `.olaf/data/practices/standards/` first, then suggest creating standards doc

**Output Format**:
```markdown
❌ No existing documentation found for: "{question}"

💡 Suggested Action:
Run `olaf onboard-me` to generate persona-specific quick start guides.

This will analyze your repository and create:
- QUICKSTART-OVERVIEW.md (guide selector)
- QUICKSTART-ARCHITECT.md (architecture and design)
- QUICKSTART-*-DEVELOPER.md (implementation guides)
- QUICKSTART-QA-ENGINEER.md (testing workflows)
- QUICKSTART-BUSINESS-ANALYST.md (features and value)
- QUICKSTART-DOCS-CONTRIBUTOR.md (documentation)

All guides in: .olaf/data/product/context/{repo-name}/
```
## Example Scenarios

### Example 1: Found in Existing Artifacts
```
User: olaf tell me how to build this project

Search: .olaf/data/product/context/my-repo/QUICKSTART-*.md
Found: QUICKSTART-BACKEND-DEVELOPER.md, Section "Build & Run"

Output:
# How to Build This Project

Prerequisites:
- Node.js 18+
- npm 9+

Build Steps:
1. npm install
2. npm run build
3. npm test

Verify: Check console for successful compilation

---
📚 Source: .olaf/data/product/context/my-repo/QUICKSTART-BACKEND-DEVELOPER.md (lines 18-28)
```

### Example 2: Not Found - Suggest Analysis
```
User: olaf tell me how to get started

Search: .olaf/data/product/context/my-repo/ → No QUICKSTART files found
Search: .olaf/data/kb/ → No results
Search: .olaf/data/practices/ → No results

Output:
❌ No existing documentation found for: "how to get started"

💡 Suggested Action:
Run `olaf onboard-me` to generate persona-specific quick start guides.

This will analyze your repository and create:
- QUICKSTART-OVERVIEW.md (guide selector)
- QUICKSTART-ARCHITECT.md (architecture and design)
- QUICKSTART-*-DEVELOPER.md (implementation guides)
- QUICKSTART-QA-ENGINEER.md (testing workflows)
- QUICKSTART-BUSINESS-ANALYST.md (features and value)
- QUICKSTART-DOCS-CONTRIBUTOR.md (documentation)

All guides in: .olaf/data/product/context/my-repo/
```

### Example 3: Found in Practices
```
User: olaf tell me about coding standards

Search: .olaf/data/practices/standards/
Found: universal-coding-standards.md, python-coding-standards.md

Output:
# Coding Standards

## Universal Standards
- Use meaningful variable names
- Follow DRY principle
- Write self-documenting code

## Python-Specific
- Follow PEP 8
- Use type hints
- Max line length: 120

---
📚 Sources:
- .olaf/data/practices/standards/universal-coding-standards.md
- .olaf/data/practices/standards/python-coding-standards.md
```

### Example 4: Web Fetch - MongoDB Question (NEW)
```
User: olaf tell me how to create an index in MongoDB

Search: Local KB → No MongoDB documentation found
Detect: Technology keyword "mongodb"
Load: .olaf/data/kb/web-resources-kb-index.md
Match: MongoDB → https://www.mongodb.com/docs/
Fetch: Retrieve web content using URL and query="create index"

Output:
# How to Create an Index in MongoDB

To create an index in MongoDB, use the `createIndex()` method:

```javascript
db.collection.createIndex({ fieldName: 1 })
```

For compound indexes:
```javascript
db.collection.createIndex({ field1: 1, field2: -1 })
```

Index types:
- Single field: Index on one field
- Compound: Index on multiple fields
- Multikey: Index on array fields
- Text: Index for text search

Performance tips:
- Create indexes on frequently queried fields
- Use compound indexes for multi-field queries
- Monitor index usage with explain()

---
🌐 Source: MongoDB Official Documentation
https://www.mongodb.com/docs/manual/indexes/

💡 Note: This information is from external documentation. For project-specific MongoDB usage, check local artifacts.
```

### Example 5: Multi-Fetch - Docker Compose (NEW)
```
User: olaf tell me how to use docker compose with mongodb

Search: Local KB → No Docker/MongoDB combo found
Detect: Technologies ["docker", "mongodb"]
Load: web-resources-kb-index.md
Match: Docker → https://docs.docker.com/ + MongoDB → https://www.mongodb.com/docs/
Fetch: Both sources with queries "docker compose" and "mongodb docker"

Output:
# Using Docker Compose with MongoDB

Create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

Run with:
```bash
docker-compose up -d
```

Connect from application:
```
mongodb://admin:password@localhost:27017
```

---
🌐 Sources:
- Docker Official Documentation: https://docs.docker.com/compose/
- MongoDB Official Documentation: https://www.mongodb.com/docs/

💡 Note: This information is from external documentation. For project-specific implementation, check local artifacts.
```

### Example 6: Internal Tech (BMS) - No Web Fetch
```
User: olaf tell me how to configure BMS dependencies

Search: .olaf/data/kb/bms/ → Found bms-kb-index.md, description-xml.md
NO WEB FETCH (internal Amadeus technology)

Output:
# How to Configure BMS Dependencies

Dependencies are defined in Description.xml using the <dependencies> element:

```xml
<dependencies>
    <dependency name="ComponentName" type="external"/>
    <dependency name="AnotherComponent" type="internal"/>
</dependencies>
```

Dependency types:
- **External**: Third-party or platform components
- **Internal**: Your own components within the same project

Version resolution:
- BMS automatically resolves compatible versions
- Uses binary compatibility checking
- Builds dependency graph

---
📚 Sources:
- .olaf/data/kb/bms/description-xml.md (lines 45-67)
- .olaf/data/kb/bms/bms-glossary.md (lines 23-28)
```
```
User: olaf tell me about coding standards

Search: .olaf/data/practices/standards/
Found: universal-coding-standards.md, python-coding-standards.md

Output:
# Coding Standards

## Universal Standards
- Use meaningful variable names
- Follow DRY principle
- Write self-documenting code

## Python-Specific
- Follow PEP 8
- Use type hints
- Max line length: 120

---
📚 Sources:
- .olaf/data/practices/standards/universal-coding-standards.md
- .olaf/data/practices/standards/python-coding-standards.md
```

## Success Criteria

- ✅ Searches existing artifacts before suggesting analysis
- ✅ Returns answers from found documentation
- ✅ **Intelligently fetches web content when local KB lacks info** (NEW)
- ✅ **Detects technology from question keywords** (NEW)
- ✅ **Uses web-resources-kb-index.md for URL mapping** (NEW)
- ✅ **Infers official docs URLs for unknown technologies** (NEW)
- ✅ **Distinguishes internal (BMS/OTF) vs external technologies** (NEW)
- ✅ Suggests appropriate skill if no docs found
- ✅ Cites sources for all answers (local files or web URLs)
- ✅ Fast response (no unnecessary analysis)

---

**Related Skills**: onboard-me, analyze-contributor-risk, measure-ai-impact
**Related KB**: web-resources-kb-index.md (official docs and repos)
**Replaces**: Complex FAQ routing system
### Task 2: Check Direct Question
- [ ] Direct question detection completed
- [ ] `has_direct_question` flag set correctly
- [ ] Conditional routing determined

### Task 3: Match FAQ (if direct question)
- [ ] FAQ index loaded from `kb/faq-index.md`
- [ ] Semantic matching performed
- [ ] Match confidence calculated
- [ ] If match found: `faq_match_found = true`, prompt identified
- [ ] If no match: proceed to KB search

### Task 4: Present Options (if no direct question)
- [ ] FAQ index loaded
- [ ] Questions grouped by persona
- [ ] Formatted list displayed to user
- [ ] User prompted to ask specific question

### Task 5: Search Knowledge Base (fallback)
- [ ] Product KB directory checked: `.olaf/data/product/*/kb/`
- [ ] Artifacts searched for relevant content
- [ ] Results ranked by relevance
- [ ] `kb_search_completed = true`
- [ ] `relevant_artifacts` populated

### Task 6: Generate Answer
- [ ] Answer generated from FAQ prompt OR KB artifacts
- [ ] Source files documented
- [ ] Answer formatted with proper markdown
- [ ] Source references included
- [ ] `answer_generated = true`

## FAQ Index Structure Reference

The FAQ index (`kb/faq-index.md`) has this structure:

```markdown
## [Persona] Questions

### Q: [Question text]
- **Documentation**: artifact-name.md
- **Prompt**: prompts/prompt-name.md
- **Gap Check**: ✅ / ⚠️ / ❌ conditions
- **Can Answer**: [what enables answering]
```

## Matching Algorithm

For Task 3 (Match FAQ):

1. **Load FAQ entries**: Parse `kb/faq-index.md`
2. **Extract questions**: Get all Q: entries
3. **Semantic matching**:
   - Compare user question to each FAQ question
   - Use keyword overlap + intent similarity
   - Calculate confidence score (0.0-1.0)
4. **Threshold**: Match if confidence > 0.7
5. **Return best match**: Highest scoring FAQ entry

## QUICKSTART Guide Search Algorithm

For Task 1 (Search QUICKSTART Guides):

1. **Locate guides**: Find `.olaf/data/product/context/{repo-name}/QUICKSTART-*.md`
2. **Persona detection**: Determine relevant guide based on question:
   - Build/run/setup → QUICKSTART-*-DEVELOPER.md, QUICKSTART-OVERVIEW.md
   - Architecture/design/tech stack → QUICKSTART-ARCHITECT.md
   - Testing/QA → QUICKSTART-QA-ENGINEER.md
   - Business/features/value → QUICKSTART-BUSINESS-ANALYST.md
   - Documentation → QUICKSTART-DOCS-CONTRIBUTOR.md
3. **Extract keywords**: From user question
4. **Search prioritized guides**: 
   - Start with persona-matched guide
   - Then search other QUICKSTART-*.md files
   - grep/search for keywords in guides
   - Rank by keyword density
5. **Return best match**: Most relevant section with context
6. **Load content**: Read relevant sections including Mermaid diagrams

## Answer Generation Strategies

### Strategy 1: FAQ-Matched Answer
- Load prompt from `matched_prompt`
- Execute prompt to generate answer
- Include artifact references
- Format as clean markdown

### Strategy 2: KB Search Answer
- Load `relevant_artifacts` content
- Synthesize answer from artifact sections
- Cite source files
- Format as clean markdown

### Strategy 3: Hybrid Answer
- Combine FAQ prompt with KB artifacts
- Use prompt as template
- Fill with artifact data
- Format with references

## Error Handling

### No Artifacts Found
```
⚠️ No onboarding artifacts found.

Run: olaf onboard me
```

### Ambiguous Question
```
I found multiple possible matches for your question:

1. How do I build this project locally?
2. How do I run the application?

Which one do you mean? (or ask differently)
```

### No Match Found
```
I couldn't find an exact match in the FAQ, but I searched 
the knowledge base and found information in:

- build-and-run.md
- technology-stack.md

[synthesized answer here]
```

## Integration with Onboard-Me

This skill depends on `onboard-me` skill having run first:

- **Onboard-me** generates: `.olaf/data/product/context/{repo-name}/QUICKSTART-*.md`
  - QUICKSTART-OVERVIEW.md (role selector)
  - QUICKSTART-ARCHITECT.md (system architecture)
  - QUICKSTART-*-DEVELOPER.md (development guides)
  - QUICKSTART-QA-ENGINEER.md (testing)
  - QUICKSTART-BUSINESS-ANALYST.md (business value)
  - QUICKSTART-DOCS-CONTRIBUTOR.md (documentation)
- **Tell-me** reads: QUICKSTART guides to answer questions
- **Fallback**: If no QUICKSTART guides exist, prompt user to run onboard-me

## Example Interactions

### Example 1: Direct Question Match
```
User: olaf tell me how to build this project
System: [Executes chain]
  ✓ Task 1: Parsed question
  ✓ Task 2: Direct question detected
  ✓ Task 3: Searched QUICKSTART guides
  ✓ Task 6: Generated answer from QUICKSTART-BACKEND-DEVELOPER.md

Answer:
# Building This Project

Prerequisites:
- Node.js 18+
- npm 9+

Build steps:
1. Install dependencies: `npm install`
2. Build: `npm run build`
3. Run tests: `npm test`

Verify: Check console for successful compilation

Source: QUICKSTART-BACKEND-DEVELOPER.md (Section: Build & Run)
```

### Example 2: No Direct Question
```
User: olaf tell me
System: [Executes chain]
  ✓ Task 1: Parsed (empty question)
  ✓ Task 2: No direct question
  ✓ Task 4: Presenting options

I can answer questions about this project:

📚 For Developers:
• How do I build this project locally?
• How do I run the application?
• What programming languages are used?

🏗️ For Architects:
• What architectural pattern is used?
• How is this system designed?

Just ask me any question!
```

### Example 3: Architecture Question
```
User: olaf tell me about the system architecture
System: [Executes chain]
  ✓ Task 1: Parsed question
  ✓ Task 2: Direct question detected (architecture-related)
  ✓ Task 3: Searched QUICKSTART-ARCHITECT.md
  ✓ Task 6: Generated answer with architecture diagram

Answer:
# System Architecture

High-level architecture:
[Mermaid diagram showing components]

Key components:
- VS Code Extension (TypeScript)
- OLAF Framework Core (Python)
- CLI Tools (Go)

Technology decisions:
- TypeScript for VS Code API integration
- Python for AI agent flexibility
- Go for performance-critical tools

Source: QUICKSTART-ARCHITECT.md (Section: Understand the Architecture)
```

## Notes

- **Chain-based execution**: Sequential task flow with conditional routing
- **FAQ-first approach**: Try to match known questions before KB search
- **Fallback mechanism**: KB search if no FAQ match
- **Interactive mode**: Can present options if no specific question
- **Depends on onboard-me**: Requires artifacts to exist
- **No file creation**: Read-only skill, returns answers only
