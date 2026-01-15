# Generate AI Agent Instructions - Tutorial

Learn how to create comprehensive instruction files for AI coding assistants across different platforms.

## Prerequisites

- OLAF framework installed
- Access to `generate-ai-agent-instructions` skill
- A codebase to analyze

## Basic Usage

### Scenario 1: Auto-Detect Platform

**Your Situation**: You have a project and want AI instructions generated automatically.

```bash
olaf generate ai agent instructions
```

**What Happens**:
1. Skill scans for existing AI instruction files (`.cursorrules`, `.github/copilot-instructions.md`, etc.)
2. Auto-detects which platform(s) you use
3. Analyzes your codebase structure
4. Proposes output location and content
5. Generates appropriate instruction file

**Example Output**:
```
Platform: Cursor (detected .cursorrules)
File: .cursorrules
Lines: 187
Sections: 7

Key Coverage:
✓ Architecture: NestJS microservice with PostgreSQL
✓ Workflows: npm run build, npm test, docker-compose up
✓ Patterns: 12 project-specific patterns documented
✓ Integration Points: 3 external APIs, Redis cache
```

---

### Scenario 2: Specify Target Platform

**Your Situation**: You want to create instructions for a specific platform.

```bash
olaf generate ai agent instructions
```

**When prompted**: Select platform or provide `--platform cursor`

**Supported Platforms**:
- `copilot` - GitHub Copilot (`.github/copilot-instructions.md`)
- `cursor` - Cursor (`.cursorrules`)
- `windsurf` - Windsurf (`.windsurfrules`)
- `cline` - Cline (`.clinerules`)
- `kiro` - Kiro (`.kiro/steering/`)
- `generic` - Platform-agnostic (`AGENTS.md`)

---

### Scenario 3: Merge Existing Instructions

**Your Situation**: You have existing `.github/copilot-instructions.md` and want to consolidate to `AGENTS.md`.

```bash
olaf generate ai agent instructions
```

**Prompt Response**:
```
I found existing AI instructions in .github/copilot-instructions.md. 
Would you like me to:
1. Merge content into AGENTS.md (recommended)
2. Update .github/copilot-instructions.md in place
3. Create new file without merging
4. Create both with synced content
```

Choose **1** to merge valuable guidance into platform-agnostic format.

**Result**:
- Preserves project-specific patterns from existing file
- Updates outdated sections with current codebase analysis
- Creates `AGENTS.md` with consolidated guidance

---

## Advanced Usage

### Scenario 4: Multi-Platform Projects

**Your Situation**: Team uses multiple AI tools (Copilot + Cursor).

**Approach**:
1. Generate generic `AGENTS.md` first:
   ```bash
   olaf generate ai agent instructions --platform generic
   ```

2. Create platform-specific symlinks or copies:
   ```bash
   # Cursor
   cp AGENTS.md .cursorrules
   
   # Copilot
   cp AGENTS.md .github/copilot-instructions.md
   ```

3. Maintain single source of truth (`AGENTS.md`)

---

### Scenario 5: Existing Project Onboarding

**Your Situation**: Large legacy codebase with complex patterns.

**Steps**:

1. **Run the skill**:
   ```bash
   olaf generate ai agent instructions
   ```

2. **Review analysis proposal**:
   ```
   Analysis Summary:
   - Detected Platform: None (will use generic)
   - Primary Language: Java
   - Frameworks: Spring Boot 3.2, Hibernate
   - Build Tool: Maven
   
   Proposed Output:
   - Create: AGENTS.md
   - Estimated size: 220 lines
   
   Sections to Include:
   1. Critical Rules (security, data handling)
   2. Repository Overview (microservices architecture)
   3. Architecture & Key Concepts (DDD patterns)
   4. File Structure (module organization)
   5. Development Workflows (Maven, Docker)
   6. Common Scenarios (adding endpoints, DB migrations)
   7. AI Guidelines (topic-specific guidance)
   ```

3. **Confirm or adjust**

4. **Review generated file** and provide feedback:
   ```
   Please review:
   1. Clarity: Are all sections clear?
   2. Completeness: Missing workflows?
   3. Accuracy: Commands correct?
   4. Specificity: Enough project-specific examples?
   ```

5. **Iterate if needed**

---

## Understanding the Output

### What's Included

**Critical Rules** - Project-specific do's and don'ts:
```markdown
## 🚨 CRITICAL RULES FOR AI BEHAVIOR
- Never modify database migration files directly
- All API changes require OpenAPI spec updates
- Authentication uses OAuth2 - don't suggest Basic Auth
```

**Architecture Explanation** - The "why" behind decisions:
```markdown
## Understanding the Architecture
Microservices architecture with event-driven communication.
Each service owns its database (no shared DB).
WHY: Enables independent scaling and deployment.
```

**File Structure** - Where things go and why:
```markdown
### `/services/`
Purpose: Individual microservice implementations
Conventions: Each service in own directory with Dockerfile
Key Files:
- `auth-service/` - JWT token management
- `user-service/` - User CRUD operations
```

**Development Workflows** - Actual commands:
```markdown
### Building the Project
```bash
mvn clean install -DskipTests
docker-compose build
```
```

**Common Scenarios** - Step-by-step with file references:
```markdown
### Adding New REST Endpoint
1. Create controller in `src/main/java/controllers/`
2. Add service method in `src/main/java/services/`
3. Update OpenAPI spec in `api/openapi.yml`
4. Write integration test in `src/test/java/integration/`
```

**AI Guidelines** - Topic-specific guidance:
```markdown
### When Users Ask About:
**Database**: PostgreSQL with Flyway migrations in `db/migrations/`. 
Never modify existing migrations - create new ones.
```

---

## Best Practices

### 1. Keep It Current
Re-run when major changes occur:
- New framework or library adoption
- Architecture refactoring
- New deployment process
- Changed conventions

### 2. Be Specific
Good ✅:
```markdown
**Error Handling**: Custom exceptions in `src/errors/`, 
centralized handler in `middleware/error.handler.ts`
```

Bad ❌:
```markdown
**Error Handling**: Use try-catch blocks and handle errors properly
```

### 3. Reference Real Files
Good ✅:
```markdown
**Logging**: Winston logger configured in `src/utils/logger.ts`
```

Bad ❌:
```markdown
**Logging**: Use a logging library for better debugging
```

### 4. Explain Why
Good ✅:
```markdown
**Monorepo Structure**: Uses Nx for build optimization and dependency graph.
WHY: Enables shared libraries and atomic commits across services.
```

Bad ❌:
```markdown
**Monorepo Structure**: Code organized in monorepo
```

---

## Comparison with `onboard-me`

| Aspect | `generate-ai-agent-instructions` | `onboard-me` |
|--------|----------------------------------|--------------|
| **Audience** | AI coding assistants | Human developers |
| **Output** | `AGENTS.md` (150-250 lines) | `repo-guide.md` (300-1500 lines) |
| **Focus** | Patterns, conventions, "why" | Setup, build, test commands |
| **Depth** | Single comprehensive pass | Progressive (quick/standard/deep) |
| **Content** | AI-optimized guidance | Human-readable documentation |

**Use Both**: Generate `repo-guide.md` for humans, `AGENTS.md` for AI agents.

---

## Troubleshooting

### Issue: Generic Output
**Symptom**: Instructions contain generic advice, not project-specific guidance.

**Solution**: 
- Ensure codebase has clear patterns (not just getting started)
- Provide feedback requesting more specific examples
- Reference specific files you want documented

### Issue: Wrong Platform Detected
**Symptom**: Skill chooses wrong platform.

**Solution**:
- Use `--platform` parameter to specify explicitly
- Remove old platform files if migrating

### Issue: Missing Critical Info
**Symptom**: Important workflows or patterns not documented.

**Solution**:
- Provide feedback listing missing items
- Skill will iterate and add sections
- Consider if pattern is discoverable in code

---

## Related Skills

- **`onboard-me`** - Generate human-focused repository guide
- **`evaluate-prompt-for-adoption`** - Assess external prompts for quality
- **`convert-prompt`** - Modernize prompts to OLAF standards
- **`import-prompt-unchanged`** - Import prompts as-is
