# Design Patterns Guidance

**Version**: 1.0  
**Purpose**: Guide AI in transforming EARS specifications into layered system designs

---

## Application Type Classification

**First Step**: Identify what type of application is being designed to select appropriate patterns.

### Application Types

1. **ETL / Data Pipeline**
   - Extract data from sources → Transform → Load to destination
   - Pattern: 3-5 layer data flow (extraction → validation → transformation → loading → monitoring)

2. **Frontend Application**
   - User interface with state management
   - Pattern: Component-based (UI components → state management → API integration → routing)

3. **Backend API**
   - REST/GraphQL service with business logic
   - Pattern: Request-response layers (routing → validation → business logic → data access → response)

4. **CLI Tool**
   - Command-line interface with operations
   - Pattern: Command-based (argument parsing → validation → execution → output formatting)

5. **Pure Data Analysis**
   - Analyze existing data and generate insights
   - Pattern: Data pipeline (collection → analysis → interpretation → reporting)

6. **Event-Driven System**
   - React to events and trigger actions
   - Pattern: Event handlers (listeners → processors → actions → state updates)

7. **Batch Processing**
   - Process large volumes periodically
   - Pattern: Job-based (scheduling → extraction → processing → aggregation → storage)

8. **Microservice**
   - Single-responsibility service in larger ecosystem
   - Pattern: Service layers (API → business logic → persistence → messaging)

---

## Core Design Principle: Layer Separation

**Fundamental Rule**: Separate concerns into distinct layers that build on each other sequentially.

### Why Layer?
- **Clarity**: Each layer has one clear responsibility
- **Testability**: Layers can be tested independently
- **Maintainability**: Changes isolated to specific layers
- **Debugging**: Easy to identify which layer has issues

---

## Pattern 1: ETL / Data Pipeline Architecture

**When to Use**: ETL systems, data analysis, repository scanners, reporting systems

**Application Types**: ETL, Pure Data Analysis, Batch Processing

### Layer Structure (5 Layers)

```
Layer 1: Data Collection
  ↓ Produces: Raw data files (JSON/CSV/structured)
Layer 2: Validation & Quality Check
  ↓ Produces: Validated data + gap reports
Layer 3: Interpretation & Artifact Generation
  ↓ Produces: Business-ready artifacts (reports/docs)
Layer 4: Indexing & Routing
  ↓ Produces: Query indexes and routing logic
Layer 5: Query & Retrieval
  ↓ Produces: User-facing answers/results
```

### Example: Onboarding System

**Layer 1**: Scan repository (Python scripts)
- Extract project structure, dependencies, Git activity
- Output: `raw-*.json` and `data-*.md`

**Layer 2**: Validate scanner outputs
- Check for missing data, verify correctness
- Output: `validated-data-*.md` + gap warnings

**Layer 3**: Generate documentation artifacts
- Create 21 docs answering persona questions
- Output: `artifact-*.md` (build guide, API reference, etc.)

**Layer 4**: Create FAQ index
- Map 60 questions → documentation artifacts
- Output: `persona-query-index.md`

**Layer 5**: Answer questions
- Route user question → appropriate artifact
- Output: Direct answers from generated docs

### Key Design Decisions
- **Python for Layer 1**: Fast, deterministic data extraction
- **AI for Layer 3**: Interpretation requires understanding context
- **Sequential processing**: Each layer depends on previous outputs
- **File-based handoff**: Clear interfaces between layers (JSON → Markdown → Indexed)

---

## Pattern 2: Request-Response Service Architecture

**When to Use**: Backend APIs, microservices, RESTful services

**Application Types**: Backend API, Microservice

### Layer Structure (3-4 Layers)

```
Layer 1: Input Validation & Parsing
  ↓ Produces: Validated request objects
Layer 2: Business Logic Processing
  ↓ Produces: Processed results
Layer 3: Response Formatting
  ↓ Produces: User-facing output
[Optional Layer 4: Persistence/State Management]
```

### Example: Code Analysis Tool

**Layer 1**: Parse code input, validate syntax
**Layer 2**: Run analysis (complexity, quality metrics)
**Layer 3**: Format results as report
**Layer 4**: Save analysis history (optional)

---

## Pattern 3: Workflow Orchestration Architecture

**When to Use**: Multi-phase processes, coordinated workflows, ESDI-like systems

**Application Types**: CLI Tool (complex operations), Event-Driven System

### Layer Structure (Chain-Based)

```
Coordinator (Master)
  ↓
Task 1: Initialize
  ↓
Task 2: Process A
  ↓
Decision Point → Branch
  ├→ Task 3a: Path A
  └→ Task 3b: Path B
  ↓
Task 4: Finalize
```

### Example: ESDI Workflow

**Coordinator**: `esdi-coordinator.md`
**Task Chain**:
1. Exploration (challenge-me)
2. Specification (transform-raw-spec)
3. Design (generate-design) ← You are here
4. Implementation Planning (generate-implementation-plan)

### Key Design Decisions
- **Review gates**: User approval between phases
- **State management**: Track phase completion
- **File-based handoff**: Each phase outputs file for next

---

## Pattern 4: Component-Based Frontend Architecture

**When to Use**: Frontend applications, UI-heavy systems

**Application Types**: Frontend Application

### Layer Structure (Component-Based)

```
Presentation Layer (UI Components)
  ↓ Triggers: User interactions
State Management Layer
  ↓ Produces: Application state updates
API Integration Layer
  ↓ Produces: Data from backend
Routing & Navigation Layer
  ↓ Produces: View transitions
```

### Example: React/Vue Application

**Presentation**: Components render UI based on state
**State Management**: Redux/Vuex manages application state
**API Integration**: Axios/Fetch calls to backend services
**Routing**: React Router/Vue Router handles navigation

---

## Pattern 5: Iterative Refinement Architecture

**When to Use**: System that improves output through cycles, quality improvement loops

**Application Types**: Code analysis tools, optimization systems

### Layer Structure (Cyclic)

```
Initial Input
  ↓
Cycle Start:
  ├→ Analysis
  ├→ Refinement
  ├→ Validation
  └→ Exit condition check?
      ├→ Yes: Output final
      └→ No: Loop back
```

---

## Design Template Structure

For any system design, include:

### 1. Architecture Overview
- ASCII diagram showing layers/components
- Data flow arrows
- Input/output at each boundary

### 2. Layer Definitions
For each layer:
- **Purpose**: What responsibility does it have?
- **Input**: What does it consume?
- **Processing**: What does it do?
- **Output**: What does it produce?
- **Technology**: Python script vs AI prompt vs other
- **Execution Time**: Estimated duration

### 3. Interface Contracts
- File formats between layers
- Required fields in data structures
- Error handling strategy

### 4. Task Breakdown
Map layers → executable tasks:
- Task ID and name
- Dependencies (which tasks must complete first)
- Execution time estimate
- Implementation approach (AI/Script/Manual)
- Note: Executable commands generated in Phase 4, not design phase

### 5. Quality Gates
- Validation checkpoints
- Gap detection strategy
- User review points (if interactive)

---

## Multi-Language Support Principle

When designing systems that process code/projects:

**Design Principle**: Language-agnostic core + language-specific adapters

```
Core Layer (Language-Agnostic)
  ↓
Adapter Layer (Language-Specific)
  ├→ TypeScript analyzer
  ├→ Python analyzer
  ├→ Java analyzer
  └→ Generic fallback
```

**Example**: Complexity analyzer
- Core: Define "complexity" metrics
- Adapters: Use radon (Python), complexity-report (JS), PMD (Java)
- Aggregation: Combine results into unified report

---

## Decision Checklist

When creating a design, answer:

1. **What are the natural boundaries?** (Where does one concern end and another begin?)
2. **What is the primary data flow?** (One-way pipeline vs request-response vs cyclic?)
3. **Which parts need AI interpretation?** (vs deterministic processing)
4. **What are the handoff formats?** (JSON, Markdown, API calls, etc.)
5. **Where are the validation points?** (Quality gates, error detection)
6. **What is user-visible?** (vs internal intermediate outputs)
7. **Is it synchronous or asynchronous?** (Sequential vs parallel execution)

---

## Anti-Patterns to Avoid

❌ **Monolithic Layer**: One layer doing everything
- Fix: Split into focused layers with clear responsibilities

❌ **Unclear Handoffs**: Layer outputs undefined format
- Fix: Specify exact file formats and required fields

❌ **Skip Validation**: Assume upstream data is perfect
- Fix: Add validation layer to catch gaps/errors early

❌ **Premature Optimization**: Complex design for simple problem
- Fix: Start with minimal layers, add only when needed

❌ **Language-Specific Core**: Hardcode to one language
- Fix: Use adapter pattern for multi-language support

---

## Complexity Thresholds (Industry Reality)

When designing analysis systems, use realistic thresholds:

### Halstead Metrics (Filter for genuinely problematic code)
- **Difficulty > 30**: Truly unmaintainable (industry: 10-25 is normal)
- **Effort > 15,000**: Extreme mental load

### Cyclomatic Complexity (Language-Specific)
| Language | Acceptable | Monitor | Refactor Needed |
|----------|-----------|---------|-----------------|
| TypeScript/JS | 1-20 | 21-30 | > 30 |
| Python | 1-10 | 11-20 | > 20 |
| Java/C# | 1-20 | 21-40 | > 40 |
| Go/Rust | 1-15 | 16-25 | > 25 |

**Philosophy**: Flag real problems, not nitpick normal code.

---

## Summary

**Good design**:
- Clear layer boundaries
- One responsibility per layer
- Explicit data contracts
- Validation checkpoints
- Realistic complexity thresholds
- Language-agnostic where possible

**Use this guidance** to transform EARS specifications into structured, maintainable architectures.
