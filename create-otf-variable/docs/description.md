# create-otf-variable

## Overview

The `create-otf-variable` skill guides developers through creating OTF (Open Transaction Framework) variables with proper XML configuration and C++ accessor code. It provides an interactive workflow for adding feature flags and configuration parameters to Amadeus OTF applications.

## Purpose

This skill enables developers to:
- Create new OTF configuration variables with proper structure
- Generate C++ accessor code following best practices
- Configure environment-specific overrides (LOCAL, UAT, PRD)
- Implement safe feature flag rollout strategies
- Follow consistent naming conventions and patterns

## Key Features

- **Interactive Workflow**: Gathers requirements through guided questions
- **XML Configuration**: Generates proper component XML structure
- **C++ Code Generation**: Provides PropertiesManager accessor patterns
- **Environment Management**: Configures common and phase-specific values
- **Testing Guidance**: Includes unit test examples and deployment strategies
- **Best Practices**: Enforces naming conventions and safe defaults

## Usage

Invoke the skill to start the interactive workflow:

```
Execute create-otf-variable
```

Or provide initial context:

```
Execute create-otf-variable for: enable layover feature
```

## Parameters

The skill gathers parameters interactively:

| Parameter | Required | Description |
|-----------|----------|-------------|
| Variable Name | Yes | Identifier (e.g., `ENABLE_*`, `MIG_*`, `IS_*`) |
| Purpose | Yes | What the variable controls |
| Valid Values | Yes | e.g., `Y/N`, `true/false`, numeric |
| Default Value | Yes | Recommended: OFF (`N` or `false`) for safety |
| Environments | Yes | Which need overrides (LOCAL, UAT, PRD) |
| Component XML File | Yes | Path to the configuration file |

## Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    Gather Requirements                       │
│  • Variable name and purpose                                │
│  • Valid values and default                                 │
│  • Environment overrides needed                             │
│  • Component XML file location                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Locate Component XML                       │
│  • Search for *.component.xml files                         │
│  • Verify file structure                                    │
│  • Present options if multiple found                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Check Existing Patterns                     │
│  • Find existing variables in XML                           │
│  • Identify accessor patterns in C++ code                   │
│  • Match project conventions                                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Add Variable to XML                        │
│  • Add to <common> section with default                     │
│  • Add to <phase> sections for overrides                    │
│  • Maintain alphabetical order if applicable                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 Generate C++ Accessor Code                   │
│  • PropertiesManager patterns                               │
│  • Recommended accessor method                              │
│  • Usage examples                                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Provide Testing Guidance                    │
│  • Unit test examples                                       │
│  • Environment testing strategy                             │
│  • Gradual rollout recommendations                          │
└─────────────────────────────────────────────────────────────┘
```

## Output

The skill produces:

### XML Configuration
```xml
<!-- In <common> section -->
<variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>

<!-- In <phase name="LOCAL"> section -->
<variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature for migration"/>
```

### C++ Accessor Code
```cpp
// Basic pattern
bool isLayoverEnabled = toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
                        toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";

// Recommended accessor method
bool ConfigManager::isLayoverEnabled() {
    return toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
           toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";
}
```

### Unit Test Examples
```cpp
TEST(FeatureTest, WhenDisabled_UsesStandardLogic) {
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "N");
    ASSERT_FALSE(ConfigManager::isLayoverEnabled());
}
```

## Examples

### Feature Flag for Migration
```
User: "Add an OTF variable to enable layover feature"

Skill Response:
1. Suggests name: MIG_ENABLE_LAYOVER
2. Recommends values: Y/N
3. Sets default: N (safe)
4. Enables in LOCAL for development
5. Provides accessor code and tests
```

### Configuration Parameter
```
User: "Create a variable for max retry count"

Skill Response:
1. Suggests name: MAX_RETRY_COUNT
2. Recommends values: numeric (1-10)
3. Sets default: 3
4. Provides numeric accessor pattern
```

## Naming Conventions

| Prefix | Use Case |
|--------|----------|
| `ENABLE_*` | Feature flags |
| `MIG_*` | Migration-related features |
| `IS_*` | Boolean state indicators |
| `MAX_*` | Numeric limits |
| `DEFAULT_*` | Default values |

## Error Handling

| Scenario | Behavior |
|----------|----------|
| XML file not found | Helps locate correct component file |
| Syntax errors | Ensures proper XML structure |
| Naming conflicts | Searches for existing variables, suggests alternatives |
| Missing sections | Guides user to add required sections |

## Related Skills

- `get-bms-expertise` - BMS build system expertise
- `code-in-rust` - Alternative language patterns
- `tell-me` - Search OTF knowledge base
