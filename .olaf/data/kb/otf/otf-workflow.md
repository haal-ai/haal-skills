# OTF Variable Creation Workflow

## Step-by-Step Guide

This guide walks through the complete process of adding a new OTF variable to your Amadeus C++ component.

## Prerequisites

- Access to component XML file (e.g., `component.component.xml`)
- Understanding of the feature being controlled
- Knowledge of target environments

## Step 1: Gather Requirements

Before creating the variable, collect:

### Required Information
- **Variable Name** - Identifier (e.g., `MIG_ENABLE_LAYOVER`)
- **Purpose** - What does this variable control?
- **Valid Values** - What values are acceptable?
- **Default Value** - Safe default (usually OFF: `N` or `false`)
- **Environment Overrides** - Which environments need different values?
- **Component XML File** - Path to configuration file

### Optional Context
- Is this for a migration? (use `MIG_` prefix)
- Existing accessor patterns in your project?
- Related features or dependencies?

## Step 2: Locate Component XML File

### Finding Your XML File

**Option 1: Known Location**
If you know the component name:
```
your-project/config/your_component.component.xml
```

**Option 2: Search**
Use VS Code search or command line:
```bash
# Find component XML files
find . -name "*.component.xml"

# Or use grep to find specific component
grep -r "component name=" . --include="*.xml"
```

### Verify Structure
Open the XML file and identify:
- `<common>` section - Default values
- `<phase name="...">` sections - Environment overrides

## Step 3: Check Existing Patterns

### Review Existing Variables
Look for similar variables in the XML:

```xml
<common>
    <variable name="ENABLE_FEATURE_X" value="false" control="off" description="Enable Feature X"/>
    <variable name="MIG_ENABLE_FEATURE_Y" value="N" control="off" description="Migration flag for Feature Y"/>
</common>
```

**Identify**:
- Naming conventions used
- Value format (`Y/N` vs `true/false`)
- Description style
- Indentation and formatting

### Check C++ Accessor Patterns

Search for existing PropertiesManager usage:

```bash
# Find accessor patterns
grep -r "PropertiesManager::GetInstance()" . --include="*.cpp" --include="*.h"
```

**Look for**:
- Dedicated accessor classes (e.g., `ConfigManager`, `FeatureFlags`)
- Common patterns and helper methods
- Naming conventions for accessor methods

## Step 4: Add Variable to XML

### Add to Common Section

1. **Locate `<common>` section**
2. **Add variable** (maintain alphabetical order if used):

```xml
<common>
    <!-- Existing variables... -->
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
    <!-- More variables... -->
</common>
```

### Add Environment Overrides

For each environment needing different values:

```xml
<phase name="LOCAL">
    <variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature for migration"/>
</phase>
```

**Common Phases**:
- `LOCAL` - Development (often enabled for testing)
- `UAT` - User acceptance testing
- `PRD` - Production (enable after validation)

### Complete Example

```xml
<component name="your_component">
    <common>
        <variable name="ENABLE_CACHE" value="true" control="off" description="Enable response caching"/>
        <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
    </common>
    
    <phase name="LOCAL">
        <variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature for migration"/>
    </phase>
    
    <phase name="UAT">
        <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
    </phase>
    
    <phase name="PRD">
        <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
    </phase>
</component>
```

## Step 5: Implement C++ Accessor Code

### Basic Pattern

**Direct Access**:
```cpp
bool isLayoverEnabled = toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
                        toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";
```

### Recommended: Accessor Method

**Create reusable method**:

```cpp
// In ConfigManager.h or similar
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
    // Layover-specific logic
} else {
    // Standard logic
}
```

### Accessor Naming Conventions

| Variable Type | Method Name Pattern | Example |
|---------------|---------------------|---------|
| `ENABLE_*` | `is*Enabled()` | `isCacheEnabled()` |
| `MIG_ENABLE_*` | `is*Enabled()` | `isLayoverEnabled()` |
| `IS_*` | `is*()` | `isProduction()` |
| Numeric | `get*()` | `getMaxRetries()` |

**Avoid redundancy**: Use `isLayoverEnabled()` NOT `isEnableLayoverEnabled()`

## Step 6: Usage in Code

### Conditional Feature Implementation

```cpp
void processRequest(const Request& request) {
    if (ConfigManager::isLayoverEnabled()) {
        // New implementation with layover support
        processWithLayover(request);
    } else {
        // Legacy implementation
        processStandard(request);
    }
}
```

### Feature Flag Pattern

```cpp
class FeatureProcessor {
private:
    bool layoverEnabled_;
    
public:
    FeatureProcessor() {
        // Cache at initialization
        layoverEnabled_ = ConfigManager::isLayoverEnabled();
    }
    
    void process() {
        if (layoverEnabled_) {
            // Feature-specific logic
        }
    }
};
```

## Step 7: Testing

### Unit Tests

Test both enabled and disabled states:

```cpp
TEST(LayoverTest, WhenDisabled_UsesStandardLogic) {
    // Setup: Mock OTF variable to N
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "N");
    
    // Execute
    auto result = processRequest(testRequest);
    
    // Verify standard behavior
    ASSERT_EQ(result.type, StandardResult);
}

TEST(LayoverTest, WhenEnabled_UsesLayoverLogic) {
    // Setup: Mock OTF variable to Y
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "Y");
    
    // Execute
    auto result = processRequest(testRequest);
    
    // Verify layover behavior
    ASSERT_EQ(result.type, LayoverResult);
}
```

### Environment Testing

1. **LOCAL**: Verify feature works when enabled
2. **UAT**: Test with production-like data
3. **PRD**: Monitor after controlled rollout

## Step 8: Deployment Strategy

### Gradual Rollout

1. **Deploy code** with feature OFF by default
2. **Enable in LOCAL** - Developer testing
3. **Enable in UAT** - QA validation
4. **Monitor metrics** - Performance, errors
5. **Enable in PRD** - Gradual rollout (canary, percentage)
6. **Full rollout** - After validation
7. **Cleanup** - Remove flag after migration complete

### Monitoring

Track key metrics:
- Feature usage rates
- Error rates when enabled vs disabled
- Performance impact
- User feedback

## Common Issues and Solutions

### Issue: Variable Not Recognized

**Symptoms**: Runtime error or default behavior always used

**Solutions**:
1. Verify XML file is loaded by component
2. Check variable name spelling (case-sensitive)
3. Restart application to reload configuration
4. Check OTF logs for parsing errors

### Issue: Override Not Applied

**Symptoms**: Getting common value instead of phase override

**Solutions**:
1. Verify phase name matches environment (case-sensitive)
2. Check phase section is properly closed
3. Ensure override comes AFTER common section
4. Validate XML syntax

### Issue: Performance Degradation

**Symptoms**: Slow response times after adding variable checks

**Solutions**:
1. Cache variable value at initialization
2. Avoid repeated PropertiesManager calls in loops
3. Use accessor methods for cleaner code
4. Profile to identify actual bottleneck

## Best Practices Checklist

Before finalizing:

- ✅ Variable name follows naming conventions
- ✅ Default value is safe (typically OFF)
- ✅ Clear description provided in XML
- ✅ Environment overrides configured correctly
- ✅ Accessor method created (not inline checks)
- ✅ Unit tests cover both enabled/disabled states
- ✅ Deployment plan includes gradual rollout
- ✅ Monitoring strategy defined
- ✅ XML formatting matches project style

## Next Steps

After creating your OTF variable:

1. **Code Review** - Get team feedback on implementation
2. **Documentation** - Update component documentation
3. **Deployment** - Follow gradual rollout plan
4. **Monitoring** - Track metrics in each environment
5. **Cleanup** - Plan for flag removal after migration
