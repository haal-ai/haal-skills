# Generate Design Skill

## Overview

Transforms EARS (Easy Approach to Requirements Syntax) specifications into structured, layered system designs using proven architecture patterns.

## What It Does

- ✅ Identifies application type (ETL, Frontend, Backend API, CLI, etc.)
- ✅ Selects appropriate architecture pattern
- ✅ Designs 3-5 layer systems with clear boundaries
- ✅ Creates task breakdown with execution estimates
- ✅ Generates comprehensive design documentation

## Master-Chain Pattern

This skill uses the master-chain pattern with 5 sequential tasks:

```
Task 0: Analyze EARS Specification
  ↓
Task 1: Identify Application Type
  ↓
Task 2: Design Layer Architecture
  ↓
Task 3: Create Task Breakdown
  ↓
Task 4: Generate Design Document
```

## Application Types Supported

1. **ETL / Data Pipeline** - Extract, transform, load systems
2. **Frontend Application** - UI with state management
3. **Backend API** - REST/GraphQL services
4. **CLI Tool** - Command-line interfaces
5. **Pure Data Analysis** - Repository scanners, analyzers
6. **Event-Driven** - Reactive systems
7. **Batch Processing** - Scheduled jobs
8. **Microservice** - Domain-specific services

## Architecture Patterns

**Pattern 1**: ETL / Data Pipeline (5 layers)
- Data Collection → Validation → Interpretation → Indexing → Querying

**Pattern 2**: Request-Response Service (3-4 layers)
- Routing → Validation → Business Logic → Data Access

**Pattern 3**: Workflow Orchestration (chain-based)
- Sequential phases with decision gates

**Pattern 4**: Component-Based Frontend (4 layers)
- UI Components → State Management → API Integration → Routing

**Pattern 5**: Iterative Refinement (cyclic)
- Analysis → Refinement → Validation (loop)

## Usage

```bash
# Called from ESDI Phase 3
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "skills/generate-design/prompts/generate-design.md" \
  --context "specification_file=./specification.md,output_file=./design.md" \
  --tool-mode standard \
  --aws-profile bedrock
```

## Input

**Required**:
- `specification_file`: Path to EARS specification
- `output_file`: Where to save design document

**Optional**:
- `system_type`: Hint about application type (auto-detected if not provided)

## Output

**Primary**: `design.md` - Complete system design document

**Contents**:
- Architecture diagram (ASCII)
- Layer definitions with responsibilities
- Interface contracts between layers
- Task breakdown with implementation approach (conceptual)
- Technology stack justification
- Execution timeline and critical path

## Protocol: Propose-Act

1. Analyzes specification
2. Identifies application type
3. **Proposes architecture** → User approves
4. Generates final design document

## Knowledge Base

- `kb/design-patterns-guidance.md` - Architecture patterns library
- `templates/design-document-template.md` - Output structure

## Example Output

```markdown
# Repository Scanner Design

Application Type: Pure Data Analysis
Pattern: ETL / Data Pipeline
Layers: 5

Layer 1: Data Collection (Python) - Extract project metadata
Layer 2: Validation (AI) - Verify data quality
Layer 3: Artifact Generation (AI) - Create documentation
Layer 4: Indexing (Python) - Map questions to artifacts
Layer 5: Query (AI) - Answer user questions

Tasks: 12
Execution Time: ~6 minutes
```

## Integration

Part of ESDI workflow:
- **Phase 1**: challenge-me (exploration)
- **Phase 2**: transform-raw-spec (specification)
- **Phase 3**: generate-design ← This skill
- **Phase 4**: generate-implementation-plan
