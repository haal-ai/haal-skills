# onboard-me

## Overview

The `onboard-me` skill generates persona-focused 30-minute productivity guides from repository analysis. It automatically detects the technology stack, identifies relevant developer personas, and creates tailored quickstart guides for each role.

## Purpose

This skill enables teams to:
- Automatically generate onboarding documentation for any repository
- Create role-specific guides that get developers productive in 30 minutes
- Maintain consistent onboarding quality across projects
- Reduce time spent on manual documentation creation

## Key Features

- **Automatic Repository Analysis**: Scans codebase to detect languages, frameworks, and architecture
- **Persona Detection**: Identifies 3-6 relevant developer roles based on tech stack
- **Tailored Guides**: Generates role-specific quickstart documentation
- **Mermaid Diagrams**: Includes architecture and workflow visualizations
- **Actionable Content**: Every command is copy-pasteable, every step is concrete

## Usage

Invoke the skill by pointing it at a repository:

```
Execute onboard-me for repository: /path/to/repo
```

The skill will:
1. Run the repository analyzer tool
2. Detect applicable personas
3. Generate quickstart guides for each persona
4. Create an overview file linking all guides

## Parameters

This skill operates on the target repository path and generates output based on automatic analysis. No additional parameters are required.

## Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│                   Run Repository Analyzer                    │
│  • Execute analyze-repository.py on target repo             │
│  • Generate repository-analysis.json                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Detect Personas                         │
│  • Analyze languages, frameworks, project type              │
│  • Apply persona detection rules                            │
│  • Select 3-6 relevant personas                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Generate Persona Guides                    │
│  For each detected persona:                                 │
│  • Create QUICKSTART-<PERSONA>.md                           │
│  • Include setup, build, code understanding, first change   │
│  • Add relevant Mermaid diagrams                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Create Overview File                      │
│  • Generate QUICKSTART-OVERVIEW.md                          │
│  • Link all persona guides                                  │
│  • Include repo snapshot and general setup                  │
└─────────────────────────────────────────────────────────────┘
```

## Output

The skill generates files in `.olaf/data/product/context/<repo-name>/`:

| File | Description |
|------|-------------|
| `QUICKSTART-OVERVIEW.md` | Summary with links to all persona guides |
| `QUICKSTART-FRONTEND-DEVELOPER.md` | Guide for frontend developers |
| `QUICKSTART-BACKEND-DEVELOPER.md` | Guide for backend developers |
| `QUICKSTART-ARCHITECT.md` | System overview and architecture guide |
| `QUICKSTART-QA-ENGINEER.md` | Testing and quality assurance guide |
| `QUICKSTART-DEVOPS-ENGINEER.md` | Infrastructure and deployment guide |
| `QUICKSTART-BUSINESS-ANALYST.md` | Non-technical system overview |
| `QUICKSTART-DOCS-CONTRIBUTOR.md` | Documentation contribution guide |

*Note: Only guides for detected personas are generated.*

## Persona Detection Rules

| Persona | Detection Criteria |
|---------|-------------------|
| Frontend Developer | TypeScript/JavaScript + React/Vue/Angular/Next.js |
| Backend Developer | Python + FastAPI/Django/Flask OR Go with API frameworks |
| Mobile Developer | Kotlin OR Swift OR react-native |
| VS Code Extension Developer | VS Code Extension in frameworks |
| CLI Tool Developer | project_type == cli-tool OR Bubble Tea (TUI) |
| DevOps Engineer | Docker OR Kubernetes OR Terraform |
| Data Engineer | Python + pandas/numpy/tensorflow OR Apache Spark |
| QA Engineer | Always if architecture.has_tests == true |
| Architect | Always included |
| Business Analyst | Always included |
| Docs Contributor | Always included |

## Examples

### Basic Usage
```
Execute onboard-me for repository: ./my-project
```

### Output Structure
```
.olaf/data/product/context/my-project/
├── QUICKSTART-OVERVIEW.md
├── QUICKSTART-FRONTEND-DEVELOPER.md
├── QUICKSTART-BACKEND-DEVELOPER.md
├── QUICKSTART-ARCHITECT.md
├── QUICKSTART-QA-ENGINEER.md
└── QUICKSTART-DOCS-CONTRIBUTOR.md
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Repository path not found | Reports error with path |
| Analysis tool fails | Reports specific error from analyzer |
| No personas detected | Falls back to Architect, Business Analyst, Docs Contributor |
| Existing guides found | Regenerates in-place (overwrites) |

## Related Skills

- `generate-step-by-step-tutorial` - Creates detailed tutorials for specific workflows
- `create-skill-description` - Generates skill documentation
- `tell-me` - Searches knowledge base for specific topics
