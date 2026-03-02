# HAAL Installer Architecture & Registry Design

## Executive Summary

The HAAL (Human-Assisted AI Learning) system implements a sophisticated modular installation architecture that enables granular selection and deployment of AI skills across multiple coding platforms. This document explains the core concepts of competencies, collections, registry format, and superseding capabilities that make HAAL uniquely suited for enterprise AI skill management.

## Table of Contents

1. [Installer Overview](#installer-overview)
2. [Competency Model](#competency-model)
3. [Collection Framework](#collection-framework)
4. [Registry Architecture](#registry-architecture)
5. [Superseding Mechanisms](#superseding-mechanisms)
6. [Multi-Platform Support](#multi-platform-support)
7. [Enterprise Benefits](#enterprise-benefits)
8. [Technical Implementation](#technical-implementation)

## Installer Overview

### Supported Platforms
- **Windsurf** - Modern AI coding environment
- **Claude** - Anthropic's AI assistant
- **GitHub Copilot** - Microsoft's AI coding partner
- **Kiro** - Enterprise AI development platform

### Installation Components

| Component | Description | Location |
|-----------|-------------|----------|
| **Skills** | AI agent prompts for specific tasks | Platform-specific directories |
| **Powers** | Kiro-specific capabilities with steering files | Kiro platform |
| **Tools** | Helper scripts and utilities | `.olaf/tools/` |
| **Data** | Knowledge base and context files | `.olaf/data/` |

### Installation Methods

```bash
# Quick install (all platforms)
curl -fsSL https://haal-ai.github.io/haal-skills/setup-haal.sh | bash

# Selective installation
bash setup-haal.sh --competency developer --platform claude,github
bash setup-haal.sh --collection techie --platform windsurf
```

## Competency Model

### What is a Competency?

A competency is a JSON-defined collection of related skills for a specific role or capability. Each competency contains:

- **Metadata**: Name, description, version information
- **Skills**: Array of skill identifiers for the competency
- **Powers**: Platform-specific capabilities (primarily for Kiro)

### Competency Structure

```json
{
  "name": "developer",
  "description": "Developer: code review, analysis, refactoring, and quality improvement",
  "skills": [
    "analyze-function-complexity",
    "assess-code-quality-principles",
    "review-code",
    "review-diff",
    "review-github-pr"
  ],
  "powers": [
    "code-in-go",
    "code-in-rust",
    "code-microservice-in-quarkus"
  ]
}
```

### Available Competencies

| Competency | Skills Count | Focus Area |
|------------|--------------|------------|
| `developer` | 27 | Core development skills |
| `architect` | 15+ | System design and architecture |
| `api-producers` | 10+ | API development and design |
| `api-consumers` | 8+ | API integration and consumption |
| `git-assistant` | 5+ | Git workflow automation |
| `session-manager` | 3+ | Development session management |
| `prompt-engineer` | 8+ | Prompt optimization |
| `technical-writer` | 6+ | Documentation skills |
| `base-skills` | 12+ | Fundamental reusable skills |
| `business-analyst` | 5+ | Business analysis |
| `project-manager` | 8+ | Project management |
| `researcher` | 4+ | Research and learning |
| `specification` | 6+ | Technical specifications |

## Collection Framework

### What is a Collection?

Collections are predefined groupings of competencies designed for different user profiles and use cases. They provide a convenient way to install related competencies together.

### Collection Hierarchy

| Collection | Competencies | Target User | Size |
|------------|--------------|-------------|------|
| **starter** | 3 | Beginners getting started | Small |
| **basic** | 4 | Regular developers | Small-Medium |
| **techie** | 7 | Technical specialists | Medium |
| **full** | 10 | Comprehensive development | Large |
| **all** | 15 | Complete skill library | Complete |

### Collection Composition

**starter**: `developer`, `git-assistant`, `session-manager`
**basic**: starter + `base-skills`
**techie**: `developer`, `architect`, `api-producers`, `api-consumers`, `specification`, `git-assistant`, `prompt-engineer`
**full**: techie + `session-manager`, `technical-writer`, `base-skills`
**all**: full + business roles (`business-analyst`, `project-manager`, `researcher`)

## Registry Architecture

### Task Registry Design

The task registry implements a centralized, reusable task system that eliminates duplication across skills and enables modular composition.

### Registry Schema

```json
{
  "$schema": "../../../schemas/task-registry.schema.json",
  "version": "1.0.0",
  "description": "Centralized registry of reusable tasks across OLAF skills",
  "last_updated": "2025-11-24",
  "tasks": [...],
  "categories": {...}
}
```

### Task Structure

Each task in the registry contains:

| Field | Description | Example |
|-------|-------------|---------|
| `id` | Unique identifier | "retrieve-timestamp" |
| `name` | Human-readable name | "Environment Information Retrieval" |
| `description` | Detailed functionality | "Retrieves current timestamp and environment details" |
| `category` | Task classification | "environment", "git", "github", "analysis" |
| `tags` | Search and filtering keywords | ["timestamp", "environment", "initialization"] |
| `current_location` | File path to implementation | "skills/common/tasks/retrieve-timestamp.md" |
| `used_in_skills` | Which skills use this task | ["review-github-pr", "convert-skill-to-chain"] |
| `dependencies` | Required tools, templates, state | Tools, templates, state variables |
| `outputs` | Produced state variables and files | State variables, created files |
| `reusability_score` | 1-10 scale of reusability | 10 (highly reusable) |
| `notes` | Implementation guidance | "Highly reusable for any skill requiring timestamp" |

### Task Categories

- **environment** - System information and environment detection
- **github** - GitHub API interactions and data extraction
- **analysis** - Data analysis and report preparation
- **cleanup** - Temporary file cleanup and resource management
- **user-interaction** - User input and selection handling
- **filesystem** - File operations (backup, copy, move)
- **validation** - Prerequisites and requirement validation
- **learning** - Learning workflow specific tasks
- **research** - Information gathering and search operations
- **reporting** - Report generation and documentation
- **git** - Git operations and repository management

### Reusability Benefits

**Highly Reusable Tasks (Score 8-10):**
- `retrieve-timestamp` - Used in 5+ skills
- `backup-file` - Universal file backup utility
- `cleanup-extraction-files` - Standard cleanup pattern
- `perform-safety-checks` - Pre-commit validation

**Moderately Reusable Tasks (Score 5-7):**
- `extract-pr-data` - GitHub PR data extraction
- `generate-commit-message` - Commit message generation
- `analyze-git-status` - Git status analysis

## Superseding Mechanisms

### Registry Evolution

The system supports multiple mechanisms for registry superseding and evolution:

#### 1. Version Management
- Semantic versioning in registry files
- `last_updated` timestamps for change tracking
- Backward compatibility maintenance
- Migration paths between versions

#### 2. Source Override
```bash
# Use different branch or fork
bash setup-haal.sh --seed "your-org/your-repo:branch"
```

#### 3. Platform-Specific Registries
- Base registry + platform-specific extensions
- Custom skills per AI platform
- Platform-optimized task implementations

#### 4. Clean Installation
```bash
# Remove existing before installing
bash setup-haal.sh --clean
```

#### 5. Custom Registry Paths
- Enterprise-specific registry locations
- Private registry hosting
- Air-gapped environment support

### Superseding Hierarchy

1. **Base Registry** - Core HAAL registry
2. **Platform Extensions** - Platform-specific additions
3. **Enterprise Overrides** - Custom enterprise registry
4. **Local Overrides** - User-specific customizations

## Multi-Platform Support

### Platform-Specific Adaptations

Each supported platform receives optimized implementations:

#### GitHub Copilot
- Copilot-specific prompt formatting
- GitHub integration optimizations
- Enterprise GitHub features

#### Claude
- Claude-optimized prompt structures
- Long-context handling
- Multi-modal capabilities

#### Windsurf
- Windsurf-specific integrations
- IDE plugin compatibility
- Real-time collaboration features

#### Kiro
- Enterprise-grade security
- Advanced steering capabilities
- Custom workflow integration

### Cross-Platform Consistency

- **Unified Skill Library** - Same core skills across all platforms
- **Platform Optimizations** - Platform-specific enhancements
- **Consistent API** - Uniform skill invocation patterns
- **Shared Registry** - Common task registry across platforms

## Enterprise Benefits

### 1. Granular Control
- **Skill-Level Selection** - Install only needed competencies
- **Role-Based Collections** - Predefined sets for different roles
- **Platform Targeting** - Deploy to specific platforms only
- **Progressive Adoption** - Start small, expand as needed

### 2. Centralized Management
- **Single Registry** - Unified task and skill management
- **Version Control** - Track and manage skill versions
- **Dependency Management** - Automatic dependency resolution
- **Quality Assurance** - Centralized testing and validation

### 3. Customization & Extension
- **Custom Competencies** - Create role-specific skill collections
- **Private Registries** - Host custom skill libraries
- **Fork-and-Extend** - Customize base skills for specific needs
- **Integration Capabilities** - Connect with internal systems

### 4. Scalability
- **Modular Architecture** - Add new skills without affecting existing ones
- **Reusable Tasks** - Build complex skills from reusable components
- **Efficient Updates** - Update individual skills without full reinstall
- **Multi-Tenant Support** - Support multiple teams/organizations

### 5. Governance & Compliance
- **Skill Auditing** - Track which skills are installed where
- **Access Control** - Control who can install which competencies
- **Usage Monitoring** - Monitor skill usage and effectiveness
- **Compliance Support** - Meet regulatory requirements for AI tools

## Technical Implementation

### Installation Process

1. **Download Phase**
   - Fetch HAAL package from specified source
   - Validate package integrity
   - Extract to temporary location

2. **Analysis Phase**
   - Read competency/collection requirements
   - Resolve dependencies from registry
   - Plan installation strategy

3. **Installation Phase**
   - Copy skills to platform directories
   - Install powers to Kiro (if applicable)
   - Sync tools and data to `.olaf` directories
   - Update platform-specific configurations

4. **Validation Phase**
   - Verify installation completeness
   - Test skill functionality
   - Generate installation report

### File Structure

```
.olaf/
├── tools/                 # Helper scripts
│   ├── setup-haal.sh
│   └── install-opencode.sh
├── data/                  # Knowledge base
│   ├── practices/
│   ├── kb/
│   └── web-resources-kb-index.md
└── work/                  # Working directory
    └── staging/           # Temporary files

competencies/              # Competency definitions
├── developer.json
├── architect.json
└── ...

skills/                    # Skill implementations
├── common/
├── review-code/
├── git-add-commit/
└── ...

collection-manifest.json  # Collection definitions
task-registry.json        # Central task registry
```

### Configuration Management

- **Platform Detection** - Automatic platform identification
- **Environment Validation** - Prerequisite checking
- **Conflict Resolution** - Handle version conflicts
- **Rollback Capability** - Undo failed installations

## Usage Examples

### Individual Developer Setup
```bash
# Install basic development skills
curl -fsSL https://haal-ai.github.io/haal-skills/setup-haal.sh | bash

# Later add specific competencies
bash .olaf/tools/setup-haal.sh --competency architect --competency api-producers
```

### Team Deployment
```bash
# Deploy to entire team with specific collection
bash setup-haal.sh --collection techie --platform github,claude

# Use enterprise registry
bash setup-haal.sh --seed "company/haal-skills:enterprise" --collection full
```

### Platform-Specific Installation
```bash
# Install only to Claude
bash setup-haal.sh --competency developer --platform claude

# Install to multiple platforms
bash setup-haal.sh --collection basic --platform github,windsurf,claude
```

## Future Enhancements

### Planned Features
1. **Graphical Installer** - Web-based installation interface
2. **Skill Marketplace** - Community-contributed skills
3. **Usage Analytics** - Skill usage tracking and optimization
4. **Auto-Updates** - Automatic skill updates and patches
5. **Integration Hub** - Connect with external tools and services

### Extension Points
1. **Custom Task Types** - New task categories and implementations
2. **Platform Plugins** - Support for new AI platforms
3. **Enterprise Connectors** - Integration with enterprise systems
4. **Compliance Modules** - Industry-specific compliance features

## Conclusion

The HAAL installer architecture represents a sophisticated approach to AI skill management that addresses the complex needs of modern development teams. By combining modular competencies, reusable task registries, and flexible superseding mechanisms, it provides a foundation for scalable, customizable, and governable AI assistance across multiple platforms.

The design enables organizations to:
- Start small and scale gradually
- Customize skills for specific needs
- Maintain control over AI tool deployment
- Ensure consistency across development environments
- Adapt to evolving AI capabilities and platforms

This architecture positions HAAL as a comprehensive solution for enterprise AI skill management, supporting both individual developers and large organizations in their AI-assisted development journey.
