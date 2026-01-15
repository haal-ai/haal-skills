# OTF Variable Configuration Guide

## What is OTF?

**OTF (Open Transaction Framework)** is a C++ application server framework used at Amadeus that acts as a service broker. It enables runtime configuration of application behavior without requiring recompilation.

## OTF Variables Overview

OTF variables are configuration parameters that control:
- **Feature flags** - Enable/disable features across environments
- **Behavioral options** - Runtime behavior customization
- **Migration toggles** - Gradual feature rollout
- **Environment-specific settings** - Different values per environment (LOCAL, UAT, PRD)

## Key Concepts

### Configuration Structure

Variables are defined in component XML files (e.g., `your_component.component.xml`) with two main sections:

1. **Common Section** - Default values for all environments
2. **Phase Sections** - Environment-specific overrides

```xml
<common>
    <variable name="VARIABLE_NAME" value="DEFAULT_VALUE" control="off" description="Clear description"/>
</common>

<phase name="LOCAL">
    <variable name="VARIABLE_NAME" value="OVERRIDE_VALUE" control="off" description="Clear description"/>
</phase>
```

### C++ Access Pattern

Variables are accessed in C++ code via `toolbox::PropertiesManager::GetInstance()`:

```cpp
bool isFeatureEnabled = toolbox::PropertiesManager::GetInstance().isDefined("VARIABLE_NAME") &&
                        toolbox::PropertiesManager::GetInstance().getValue("VARIABLE_NAME") == "EXPECTED_VALUE";
```

## Variable Naming Conventions

Use clear, descriptive names with appropriate prefixes:

| Prefix | Purpose | Example |
|--------|---------|---------|
| `ENABLE_` | Regular feature toggles | `ENABLE_NEW_API` |
| `MIG_` | Migration-related features | `MIG_ENABLE_LAYOVER` |
| `IS_` | State-based feature flags | `IS_CACHE_ENABLED` |

**Best Practice**: Avoid redundancy like `ENABLE_IS_FEATURE_ENABLED`

## Common Value Types

| Type | Format | Examples |
|------|--------|----------|
| Boolean | `"Y"/"N"` or `"true"/"false"` | `"Y"`, `"false"` |
| Numeric | String representation | `"100"`, `"3.14"` |
| String | Any string value | `"production"`, `"v2"` |

## Environment Phases

Common environment phases in Amadeus OTF:

- **LOCAL** - Development environment
- **UAT** - User Acceptance Testing
- **PRD** - Production

## Best Practices

### 1. Default to OFF
Always set default value to OFF in common section for safety:
```xml
<common>
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature"/>
</common>
```

### 2. Enable in LOCAL First
Enable in LOCAL environment for development/testing:
```xml
<phase name="LOCAL">
    <variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature"/>
</phase>
```

### 3. Gradual Rollout Strategy

For production features:
1. Add variable with default OFF
2. Enable in LOCAL for development
3. Test thoroughly
4. Enable in UAT
5. Monitor and validate
6. Enable in PRD with monitoring

### 4. XML Formatting
- Maintain consistent indentation
- Place variables in alphabetical order when possible
- Include clear descriptions

### 5. Accessor Methods
Create reusable accessor methods for common patterns:

```cpp
// Good - Reusable method
bool ConfigManager::isLayoverEnabled() {
    return PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
           PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";
}

// Usage
if (ConfigManager::isLayoverEnabled()) {
    // Feature-specific implementation
}
```

## Migration Pattern

For migration features (variables prefixed with `MIG_`):

1. **Add OTF variable** with `MIG_` prefix
2. **Set default OFF** in common section
3. **Enable in LOCAL** for development
4. **Implement conditional logic**:
   ```cpp
   bool useMigrationFeature = ConfigManager::isMigrationFeatureEnabled();
   if (useMigrationFeature) {
       // New implementation
   } else {
       // Legacy implementation
   }
   ```
5. **Gradually enable** in higher environments
6. **Monitor** behavior in each environment
7. **Remove flag** once migration is complete

## Testing Strategy

### Unit Testing
Mock PropertiesManager values to test both ON and OFF states:

```cpp
// Test with feature OFF
MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "N");
assert(!ConfigManager::isLayoverEnabled());

// Test with feature ON
MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "Y");
assert(ConfigManager::isLayoverEnabled());
```

### Environment Testing
1. Verify default behavior (common section)
2. Test environment overrides
3. Validate feature behavior in each phase
4. Ensure backwards compatibility when OFF

## Common Patterns

### Boolean Feature Flag
```xml
<variable name="ENABLE_NEW_FEATURE" value="false" control="off" description="Enable new feature implementation"/>
```

```cpp
bool isEnabled = toolbox::PropertiesManager::GetInstance().isDefined("ENABLE_NEW_FEATURE") &&
                 toolbox::PropertiesManager::GetInstance().getValue("ENABLE_NEW_FEATURE") == "true";
```

### Y/N Migration Flag
```xml
<variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
```

```cpp
bool isLayoverEnabled = toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
                        toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";
```

### Numeric Configuration
```xml
<variable name="MAX_RETRY_COUNT" value="3" control="off" description="Maximum number of retry attempts"/>
```

```cpp
std::string retryStr = toolbox::PropertiesManager::GetInstance().getValue("MAX_RETRY_COUNT");
int maxRetries = std::stoi(retryStr);
```

## Troubleshooting

### Variable Not Found
**Issue**: Variable not recognized at runtime

**Solutions**:
1. Verify variable exists in correct component XML file
2. Check spelling matches exactly in XML and C++ code
3. Ensure component XML is loaded by OTF
4. Restart application after XML changes

### Wrong Value Returned
**Issue**: Getting unexpected value

**Solutions**:
1. Check phase-specific overrides
2. Verify environment phase name matches
3. Ensure no typos in value strings
4. Check for XML parsing errors in logs

### Performance Concerns
**Issue**: Frequent PropertiesManager calls impacting performance

**Solutions**:
1. Cache variable values at initialization
2. Use accessor methods instead of direct calls
3. Consider lazy initialization patterns
4. Profile to identify actual bottlenecks

## Related Concepts

- **Component XML** - Configuration files defining OTF components
- **PropertiesManager** - C++ singleton for accessing OTF variables
- **Feature Flags** - Runtime toggles for feature enablement
- **Environment Phases** - Deployment stages (LOCAL, UAT, PRD)
- **Migration Toggles** - Temporary flags for gradual feature rollout
