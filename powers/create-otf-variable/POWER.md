---
name: "create-otf-variable"
displayName: "Create OTF Variable"
description: "Guide developers through creating OTF (Open Transaction Framework) variables with proper XML configuration and C++ accessor code for Amadeus applications"
keywords: ["otf", "amadeus", "feature-flags", "xml", "cpp", "configuration"]
author: "Haal AI"
---

# Create OTF Variable

## Overview

This power guides developers through creating OTF (Open Transaction Framework) variables for Amadeus C++ applications. OTF variables are configuration parameters that enable runtime control of features without recompilation.

**Key capabilities:**
- Interactive workflow for gathering requirements
- XML configuration generation for component files
- C++ accessor code patterns using PropertiesManager
- Environment-specific overrides (LOCAL, UAT, PRD)
- Testing guidance and deployment strategies

## Background: OTF Variables

**OTF (Open Transaction Framework)** is a C++ application server framework at Amadeus that acts as a service broker. OTF variables are configuration parameters defined in component XML files.

**Key concepts:**
- Variables defined in `*.component.xml` files
- `<common>` section = default values for all environments
- `<phase>` sections = environment-specific overrides (LOCAL, UAT, PRD)
- Accessed via `toolbox::PropertiesManager::GetInstance()` in C++
- Enable gradual feature rollout and A/B testing

## Workflow

### Step 1: Gather Requirements

Collect the following information:

| Parameter | Required | Description |
|-----------|----------|-------------|
| Variable Name | Yes | Identifier with proper prefix (`ENABLE_*`, `MIG_*`, `IS_*`) |
| Purpose | Yes | What the variable controls |
| Valid Values | Yes | `Y/N`, `true/false`, numeric, or string |
| Default Value | Yes | Recommended: OFF (`N` or `false`) for safety |
| Environments | Yes | Which need overrides (LOCAL, UAT, PRD) |
| Component XML File | Yes | Path to the configuration file |

**Naming conventions:**
| Prefix | Use Case |
|--------|----------|
| `ENABLE_*` | Feature flags |
| `MIG_*` | Migration-related features |
| `IS_*` | Boolean state indicators |
| `MAX_*` | Numeric limits |

### Step 2: Locate Component XML

Search for `*.component.xml` files in the workspace:
```bash
# Find component XML files
find . -name "*.component.xml"
```

### Step 3: Check Existing Patterns

Before making changes:
1. Find existing variables in XML to match style
2. Identify accessor patterns in C++ code
3. Search for `PropertiesManager::GetInstance()` usage

### Step 4: Add XML Configuration

**In `<common>` section (default for all environments):**
```xml
<variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
```

**In environment `<phase>` sections:**
```xml
<phase name="LOCAL">
    <variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature for migration"/>
</phase>

<phase name="UAT">
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
</phase>

<phase name="PRD">
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
</phase>
```

### Step 5: Generate C++ Accessor Code

**Basic inline check:**
```cpp
bool isLayoverEnabled = toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
                        toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";

if (isLayoverEnabled) {
    // New implementation
} else {
    // Legacy implementation
}
```

**Recommended: Dedicated accessor method:**
```cpp
// In ConfigManager.h
class ConfigManager {
public:
    static bool isLayoverEnabled();
};

// In ConfigManager.cpp
bool ConfigManager::isLayoverEnabled() {
    return toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
           toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";
}

// Usage
if (ConfigManager::isLayoverEnabled()) {
    calculateLayoverNew();
} else {
    calculateLayoverLegacy();
}
```

**For true/false flags:**
```cpp
bool isEnabled = toolbox::PropertiesManager::GetInstance().isDefined("ENABLE_FEATURE") &&
                 toolbox::PropertiesManager::GetInstance().getValue("ENABLE_FEATURE") == "true";
```

**Accessor naming:**
- `isFeatureEnabled()` - For simple feature flags
- `isFeatureApplicable()` - For complex conditional features
- Avoid redundancy: `isLayoverEnabled()` NOT `isEnableLayoverEnabled()`

### Step 6: Add Unit Tests

```cpp
#include <gtest/gtest.h>
#include "ConfigManager.h"
#include "MockPropertiesManager.h"

TEST(LayoverFeatureTest, WhenDisabled_UsesLegacyLogic) {
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "N");
    ASSERT_FALSE(ConfigManager::isLayoverEnabled());
}

TEST(LayoverFeatureTest, WhenEnabled_UsesNewLogic) {
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "Y");
    ASSERT_TRUE(ConfigManager::isLayoverEnabled());
}

TEST(LayoverFeatureTest, WhenUndefined_DefaultsToDisabled) {
    MockPropertiesManager::clearValue("MIG_ENABLE_LAYOVER");
    ASSERT_FALSE(ConfigManager::isLayoverEnabled());
}
```

### Step 7: Deployment Strategy

**Gradual rollout:**
1. Deploy with default OFF
2. Enable in LOCAL for development
3. Enable in UAT for QA testing
4. Monitor metrics
5. Enable in PRD (canary/percentage rollout)
6. Full rollout after validation
7. Remove flag after migration complete

## Best Practices

- **Safe defaults**: Always default to OFF for new features
- **Clear descriptions**: Document purpose in XML description attribute
- **Test both paths**: Verify behavior when enabled AND disabled
- **Plan for removal**: Feature flags are temporary
- **Alphabetical order**: Maintain within sections if project follows this
- **Match project style**: Follow existing XML formatting

## Troubleshooting

### XML File Not Found
- Search workspace for `*.component.xml`
- Check if file is in a different location
- Verify file naming convention

### Variable Not Taking Effect
- Verify variable name matches exactly (case-sensitive)
- Check `isDefined()` call is present
- Confirm correct phase is being used
- Restart application to reload configuration

### Accessor Code Doesn't Compile
- Verify include paths for toolbox headers
- Check PropertiesManager namespace
- Review existing accessor patterns in codebase

## Quality Checklist

Before completing:
- [ ] Variable added to XML with proper structure
- [ ] Clear description in XML
- [ ] Safe default value (typically OFF)
- [ ] Environment overrides configured
- [ ] Accessor code provided
- [ ] Naming follows conventions
- [ ] Testing guidance included
- [ ] XML formatting matches project style
