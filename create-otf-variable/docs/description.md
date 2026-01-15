# Create OTF Variable

**Skill ID**: `create-otf-variable`  
**Version**: 1.0.0  
**Status**: Experimental

## Overview

The `create-otf-variable` skill guides developers through adding OTF (Open Transaction Framework) variables to Amadeus C++ applications, ensuring proper XML configuration, environment-specific settings, and C++ accessor code following best practices.

## What is OTF?

**OTF (Open Transaction Framework)** is a C++ application server framework used at Amadeus that acts as a service broker, enabling runtime configuration of application behavior without requiring recompilation.

## What This Skill Does

This skill provides interactive guidance for:

1. **Gathering Requirements**
   - Variable naming (with convention suggestions)
   - Purpose and valid values
   - Default values and environment overrides

2. **XML Configuration**
   - Locating component XML files
   - Adding variables to `<common>` section
   - Setting environment-specific overrides in `<phase>` sections

3. **C++ Implementation**
   - Generating PropertiesManager accessor code
   - Creating reusable accessor methods
   - Following naming conventions

4. **Testing & Deployment**
   - Unit testing strategies
   - Gradual rollout recommendations
   - Environment-specific validation

## Use Cases

### Feature Flags
Create runtime toggles for new features:
```xml
<variable name="ENABLE_NEW_API" value="false" control="off" description="Enable new API implementation"/>
```

### Migration Toggles
Gradual rollout of migration features:
```xml
<variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
```

### Environment-Specific Configuration
Different behavior per environment:
```xml
<common>
    <variable name="MAX_RETRY_COUNT" value="3" control="off" description="Maximum retry attempts"/>
</common>
<phase name="PRD">
    <variable name="MAX_RETRY_COUNT" value="5" control="off" description="Maximum retry attempts"/>
</phase>
```

## Key Features

✅ **Interactive workflow** - Step-by-step guidance with prompts for required information  
✅ **Pattern detection** - Analyzes existing variables to match project conventions  
✅ **Best practices** - Enforces naming conventions and safe defaults  
✅ **Code generation** - Provides ready-to-use C++ accessor code  
✅ **Testing guidance** - Unit test examples and deployment strategies  
✅ **Environment management** - Proper phase-specific overrides  

## What You'll Need

- Component XML file path (or component name to search)
- Variable purpose and expected values
- Target environments for the feature
- Understanding of the feature being controlled

## Benefits

- **Reduces errors** in XML configuration
- **Standardizes** feature flag implementation across teams
- **Accelerates development** with ready-to-use code patterns
- **Ensures best practices** for gradual rollout and testing
- **Maintains consistency** with existing project patterns

## Related Skills

- `get-bms-expertise` - BMS build system expertise for component management
- General C++ development and XML editing skills

## Knowledge Base

This skill references:
- **OTF Configuration Guide** - Comprehensive overview of OTF variables
- **OTF Workflow** - Step-by-step implementation guide

## Who Should Use This

- Amadeus C++ developers working with OTF applications
- Teams implementing feature flags and runtime configuration
- Developers performing gradual feature migrations
- Anyone needing environment-specific application behavior

## Limitations

- Specific to Amadeus OTF framework and C++ applications
- Requires access to component XML files
- Assumes familiarity with C++ and basic XML structure
- Does not handle complex multi-component dependencies

## Example Output

The skill will help you create:

**XML Configuration**:
```xml
<common>
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature"/>
</common>
<phase name="LOCAL">
    <variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature"/>
</phase>
```

**C++ Accessor**:
```cpp
bool ConfigManager::isLayoverEnabled() {
    return toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
           toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";
}
```

**Usage**:
```cpp
if (ConfigManager::isLayoverEnabled()) {
    // New implementation
} else {
    // Legacy implementation
}
```
