# Tutorial: create-otf-variable

## Introduction

This tutorial guides you through using the `create-otf-variable` skill to add configuration variables to Amadeus OTF applications. You'll learn how to create feature flags with proper XML configuration and C++ accessor code.

## Prerequisites

Before starting, ensure you have:
- Access to an OTF application codebase
- Knowledge of which component XML file to modify
- Understanding of the feature you want to control
- Familiarity with C++ and XML basics

## Step-by-Step Instructions

### Step 1: Start the Skill

Invoke the skill to begin the interactive workflow:

```
Execute create-otf-variable
```

Or provide initial context:

```
Execute create-otf-variable for: enable new pricing algorithm
```

### Step 2: Provide Variable Requirements

The skill will ask for details. Provide:

**Variable Name**:
- Use descriptive names with proper prefixes
- Examples: `MIG_ENABLE_LAYOVER`, `ENABLE_NEW_PRICING`, `IS_DEBUG_MODE`

**Purpose**:
- Clearly describe what the variable controls
- Example: "Enable the new layover calculation feature for migration"

**Valid Values**:
- Boolean: `Y/N` or `true/false`
- Numeric: specific range like `1-10`
- String: enumerated values

**Default Value**:
- Recommend OFF (`N` or `false`) for safety
- New features should be disabled by default

**Environments**:
- LOCAL: Development environment
- UAT: User acceptance testing
- PRD: Production

### Step 3: Locate the Component XML File

The skill will help find your configuration file:

```
Searching for *.component.xml files...

Found:
1. src/pricing/pricing.component.xml
2. src/booking/booking.component.xml

Which file should I update?
```

Select the appropriate file for your feature.

### Step 4: Review Existing Patterns

The skill checks your codebase for:
- Existing variable naming conventions
- Current accessor patterns in C++ code
- XML structure and formatting style

This ensures consistency with your project.

### Step 5: Add XML Configuration

The skill adds the variable to your XML file:

**In the `<common>` section** (default for all environments):
```xml
<common>
    <!-- Existing variables... -->
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
</common>
```

**In environment-specific `<phase>` sections**:
```xml
<phase name="LOCAL">
    <!-- Enable for development -->
    <variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature for migration"/>
</phase>

<phase name="UAT">
    <!-- Keep disabled until ready for testing -->
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
</phase>

<phase name="PRD">
    <!-- Keep disabled until rollout -->
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
</phase>
```

### Step 6: Implement C++ Accessor Code

The skill provides accessor code patterns:

**Basic inline check**:
```cpp
bool isLayoverEnabled = toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
                        toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";

if (isLayoverEnabled) {
    // New implementation
} else {
    // Legacy implementation
}
```

**Recommended: Dedicated accessor method**:
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

// Usage in your code
if (ConfigManager::isLayoverEnabled()) {
    // New layover calculation
    calculateLayoverNew();
} else {
    // Legacy calculation
    calculateLayoverLegacy();
}
```

### Step 7: Add Unit Tests

Implement tests for both states:

```cpp
#include <gtest/gtest.h>
#include "ConfigManager.h"
#include "MockPropertiesManager.h"

TEST(LayoverFeatureTest, WhenDisabled_UsesLegacyLogic) {
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "N");
    
    ASSERT_FALSE(ConfigManager::isLayoverEnabled());
    // Verify legacy behavior
}

TEST(LayoverFeatureTest, WhenEnabled_UsesNewLogic) {
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "Y");
    
    ASSERT_TRUE(ConfigManager::isLayoverEnabled());
    // Verify new behavior
}

TEST(LayoverFeatureTest, WhenUndefined_DefaultsToDisabled) {
    MockPropertiesManager::clearValue("MIG_ENABLE_LAYOVER");
    
    ASSERT_FALSE(ConfigManager::isLayoverEnabled());
}
```

### Step 8: Plan Deployment Strategy

Follow the gradual rollout approach:

1. **Deploy with default OFF**: Ship code with feature disabled
2. **Enable in LOCAL**: Verify feature works in development
3. **Enable in UAT**: Test with production-like data
4. **Monitor metrics**: Watch for issues
5. **Enable in PRD**: Gradual rollout (canary/percentage)
6. **Full rollout**: After validation
7. **Remove flag**: Clean up after migration complete

## Verification Checklist

After creating the variable, verify:

- [ ] Variable added to `<common>` section with safe default
- [ ] Environment overrides configured correctly
- [ ] Description is clear and accurate
- [ ] C++ accessor code compiles without errors
- [ ] Unit tests pass for both enabled and disabled states
- [ ] XML formatting matches project style
- [ ] Variable name follows project conventions

## Troubleshooting

### XML File Not Found

**Symptom**: Skill can't locate component XML

**Solution**:
1. Search workspace for `*.component.xml`
2. Check if file is in a different location
3. Verify file naming convention

### Accessor Code Doesn't Compile

**Symptom**: C++ errors when using PropertiesManager

**Solution**:
1. Verify include paths for toolbox headers
2. Check PropertiesManager namespace
3. Review existing accessor patterns in codebase

### Variable Not Taking Effect

**Symptom**: Feature doesn't respond to variable changes

**Solution**:
1. Verify variable name matches exactly (case-sensitive)
2. Check `isDefined()` call is present
3. Confirm correct phase is being used
4. Restart application to reload configuration

### Tests Fail Intermittently

**Symptom**: Unit tests pass sometimes, fail others

**Solution**:
1. Ensure mock is properly reset between tests
2. Check for static state issues
3. Verify test isolation

## Next Steps

After creating your OTF variable:

- **Test locally**: Verify feature works with variable enabled
- **Code review**: Have team review XML and accessor code
- **Document**: Add variable to feature documentation
- **Monitor**: Set up metrics for feature usage
- **Plan cleanup**: Schedule flag removal after migration

## Tips for Success

1. **Use safe defaults**: Always default to OFF for new features
2. **Be descriptive**: Clear variable names and descriptions
3. **Test both paths**: Verify behavior when enabled AND disabled
4. **Plan for removal**: Feature flags are temporary
5. **Monitor rollout**: Watch metrics during gradual enablement
6. **Keep it simple**: One variable per feature when possible
