# get-bms-expertise

## Overview

The `get-bms-expertise` skill activates a BMS (Build Management System) expert persona with deep knowledge of Amadeus' enterprise-scale C/C++ build infrastructure. It transforms the AI agent into a senior specialist capable of troubleshooting, advising, and guiding developers through complex build system challenges.

## Purpose

This skill enables developers to:
- Get expert-level guidance on BMS configuration and troubleshooting
- Understand component-based C/C++ architecture patterns
- Resolve dependency conflicts and binary compatibility issues
- Navigate forest workspaces and delivery pipelines
- Follow best practices for build system management

## Key Features

- **Expert Persona Activation**: Transforms agent into a senior BMS specialist
- **Deep Technical Knowledge**: Covers Description.xml, dependencies, versioning, and plugins
- **Troubleshooting Methodology**: Systematic diagnostic approach for build issues
- **Best Practices Guidance**: Enforces binary compatibility and quality standards
- **Command Reference**: Quick access to essential BMS commands

## Usage

Invoke the skill to activate BMS expert mode:

```
Execute get-bms-expertise
```

The agent will confirm activation and await your BMS-related questions.

## Parameters

This skill does not require parameters. It activates a persona that responds to subsequent BMS-related queries.

## Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│                   Activate BMS Expert Persona                │
│  • Load BMS knowledge and terminology                       │
│  • Set communication style to precise technical language    │
│  • Enable diagnostic methodology                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Confirm Activation                         │
│  • Display expertise areas                                  │
│  • Indicate readiness for BMS questions                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Await User Questions                       │
│  • Respond to BMS troubleshooting requests                  │
│  • Provide configuration guidance                           │
│  • Explain best practices and patterns                      │
└─────────────────────────────────────────────────────────────┘
```

## Output

Upon activation, the skill outputs:

```
✅ BMS Expert Mode Activated

I'm now operating as a Senior BMS Specialist with expertise in:
- Component-based C/C++ architecture
- Binary compatibility management  
- Build/test/delivery workflows
- Dependency resolution and Forest workspaces

I'm ready to help with BMS questions, troubleshooting, and best practices.

How can I assist you with BMS today?
```

## Expertise Areas

### BMS Architecture & Principles
- Component-based design (1 component = 1 library/binary)
- Binary compatibility optimization
- Description.xml configuration mastery
- Dependency resolution algorithms
- Forest workspace management

### Technical Domains
- Build system: Makefile generation, parallel compilation, toolchains
- Testing: unittest, valgrind, callgrind, cppcheck, coverage
- Delivery: Automated verification, SCM tagging, Artifactory
- Configuration: Cascaded bmsrc files, profiles (dev/rel)
- Versioning: 4-part versioning (A-B-C-D), compatibility rules

### Platform Knowledge
- Operating systems: RHEL, Fedora, Ubuntu, Debian
- Repository systems: Local filesystem, NAS, Artifactory
- SCM integration: Git, Mercurial, CVS

## Examples

### Troubleshooting Dependency Issues
```
User: "I'm getting binary incompatibility errors when building my component"

BMS Expert: [Provides systematic diagnosis]
1. Check version conflicts in Description.xml
2. Review dependency graph with `bms deps`
3. Verify binary compatibility rules (A-B-C-D versioning)
4. Guide manual version specification if needed
```

### Configuration Guidance
```
User: "How do I set up a new component with external dependencies?"

BMS Expert: [Provides Description.xml patterns]
- External dependency syntax
- Internal vs external classification
- Version specification best practices
```

### Build Optimization
```
User: "My builds are slow, how can I optimize?"

BMS Expert: [Provides tuning recommendations]
- Parallel build configuration
- Dependency graph optimization
- Replication strategies
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Non-BMS question | Redirects to appropriate resources |
| Unknown BMS feature | References knowledge base or escalates |
| Complex architectural decision | Recommends BMS admin consultation |

## Related Skills

- `tell-me` - Search BMS knowledge base for specific topics
- `code-in-rust` - C/C++ alternative language expertise
- `code-in-go` - Systems programming guidance
