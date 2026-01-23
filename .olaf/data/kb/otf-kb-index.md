# OTF Knowledge Base Index

**Domain**: Open Transaction Framework (OTF) - Amadeus C++ Application Configuration  
**Last Updated**: 2025-11-24  
**Scope**: Runtime configuration, feature flags, environment management

---

## Overview

This knowledge base provides comprehensive documentation for working with OTF (Open Transaction Framework) variables in Amadeus C++ applications. OTF enables runtime configuration and feature toggles without requiring code recompilation.

## What is OTF?

**OTF (Open Transaction Framework)** is a C++ application server framework used at Amadeus that acts as a service broker, providing:
- Runtime configuration management
- Feature flag capabilities
- Environment-specific behavior control
- Gradual feature rollout mechanisms

## Knowledge Base Contents

### 📘 Core Documentation

#### [OTF Configuration Guide](./otf/otf-configuration-guide.md)
**Purpose**: Comprehensive reference for OTF variables  
**Topics**:
- OTF variables overview and key concepts
- Configuration structure (common and phase sections)
- C++ access patterns with PropertiesManager
- Variable naming conventions
- Common value types and formats
- Environment phases (LOCAL, UAT, PRD)
- Best practices and testing strategies
- Migration patterns
- Troubleshooting guide

**When to Use**: Reference for understanding OTF concepts, naming conventions, access patterns, and best practices.

---

#### [OTF Workflow](./otf/otf-workflow.md)
**Purpose**: Step-by-step implementation guide  
**Topics**:
- Complete workflow for creating OTF variables
- Requirements gathering checklist
- Locating component XML files
- Checking existing patterns
- Adding variables to XML
- Implementing C++ accessor code
- Testing strategies (unit and environment)
- Deployment and rollout strategy
- Common issues and solutions
- Quality checklist

**When to Use**: Follow when creating new OTF variables, implementing feature flags, or setting up environment-specific configurations.

---

## Quick Reference

### Common Use Cases

| Use Case | Relevant Documentation | Key Topics |
|----------|----------------------|------------|
| Create new feature flag | OTF Workflow | XML structure, accessor code, testing |
| Understand OTF concepts | OTF Configuration Guide | Architecture, naming, best practices |
| Implement migration toggle | Both guides | Migration patterns, gradual rollout |
| Fix OTF variable issues | OTF Configuration Guide (Troubleshooting) | Common errors, solutions |
| Environment-specific config | OTF Workflow (Step 4) | Phase sections, overrides |
| Write unit tests | OTF Workflow (Step 7) | Test patterns, mocking |

### Key Concepts at a Glance

- **Common Section**: Default values for all environments
- **Phase Section**: Environment-specific overrides (LOCAL, UAT, PRD)
- **PropertiesManager**: C++ singleton for accessing OTF variables
- **Feature Flags**: Runtime toggles (ENABLE_*, MIG_*, IS_*)
- **Gradual Rollout**: Progressive enablement across environments

### Naming Convention Quick Reference

```
ENABLE_*        - Regular feature toggles (e.g., ENABLE_CACHE)
MIG_*          - Migration-related features (e.g., MIG_ENABLE_LAYOVER)
IS_*           - State-based flags (e.g., IS_PRODUCTION)
MAX_*          - Numeric limits (e.g., MAX_RETRY_COUNT)
```

### Value Format Quick Reference

```
Boolean:  "Y"/"N" or "true"/"false"
Numeric:  "123", "3.14" (string representation)
String:   Any string value
```

## Related Skills

### create-otf-variable
**Skill ID**: `create-otf-variable`  
**Purpose**: Interactive guide for creating OTF variables  
**Usage**: `olaf create-otf-variable`  
**Features**:
- Gathers requirements interactively
- Locates component XML files
- Generates XML configuration
- Provides C++ accessor code
- Offers testing and deployment guidance

## Integration Points

### With BMS Knowledge Base
- Component XML files are managed by BMS
- Component versioning affects OTF variable availability
- Build processes include XML configuration validation

### With Shared Context
- Original prompt: `.olaf/your-repos/shared-context/.github/prompts/create-otfvar.prompt.md`
- Builder pattern for standardized variable creation

## Access Patterns

### Reading This Knowledge Base

**For Quick Answers**:
1. Use Quick Reference section above
2. Jump to specific topics in table of contents

**For Learning OTF**:
1. Start with OTF Configuration Guide
2. Review concepts and patterns
3. Follow OTF Workflow for implementation

**For Implementation**:
1. Use `create-otf-variable` skill for interactive guidance
2. Reference OTF Workflow for detailed steps
3. Consult OTF Configuration Guide for best practices

## Version Information

- **Framework**: OTF (Open Transaction Framework) - Amadeus
- **Language**: C++
- **Configuration Format**: XML
- **Access Method**: `toolbox::PropertiesManager`

## Updates and Contributions

This knowledge base is maintained as part of the OLAF framework. For updates or contributions:
- Ensure accuracy with current OTF implementation
- Follow documentation standards
- Test examples with actual OTF applications
- Update version information as needed

---

**Note**: This knowledge base focuses on OTF variable configuration and usage. For broader C++ development topics, component management, or build systems, see the BMS knowledge base.
