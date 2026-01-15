# Tutorial: Create OTF Variable

Learn how to use the `create-otf-variable` skill to add runtime configuration to your Amadeus C++ application.

## Quick Start

```
olaf create-otf-variable
```

The skill will guide you through an interactive workflow to create a new OTF variable.

## Example Walkthrough

### Scenario: Adding a Layover Feature Toggle

Let's create an OTF variable to enable a new layover feature in a migration scenario.

#### Step 1: Invoke the Skill

```
User: olaf create-otf-variable
```

#### Step 2: Provide Requirements

The skill will prompt you for information:

```
Assistant: I'll help you create a new OTF variable. Let me gather the details:

- Variable name (suggestion: ENABLE_*, MIG_*, IS_*):
- Purpose/Description:
- Expected values (Y/N, true/false, numeric, etc.):
- Default value (recommend OFF for safety):
- Environments to override (LOCAL, UAT, PRD):
- Component XML file path or name:
```

**Your Response**:
```
User: Variable name: MIG_ENABLE_LAYOVER
Purpose: Enable layover feature for migration
Values: Y/N
Default: N
Enable in LOCAL for development
Component: booking_component.component.xml
```

#### Step 3: XML Update

The skill will:
1. Locate your component XML file
2. Check existing variable patterns
3. Add the variable to the XML:

```xml
<common>
    <variable name="MIG_ENABLE_LAYOVER" value="N" control="off" description="Enable layover feature for migration"/>
</common>

<phase name="LOCAL">
    <variable name="MIG_ENABLE_LAYOVER" value="Y" control="off" description="Enable layover feature for migration"/>
</phase>
```

#### Step 4: C++ Accessor Code

The skill provides ready-to-use accessor code:

```cpp
// Recommended: Create accessor method
bool ConfigManager::isLayoverEnabled() {
    return toolbox::PropertiesManager::GetInstance().isDefined("MIG_ENABLE_LAYOVER") &&
           toolbox::PropertiesManager::GetInstance().getValue("MIG_ENABLE_LAYOVER") == "Y";
}

// Usage in your code
if (ConfigManager::isLayoverEnabled()) {
    // New layover implementation
    processWithLayover(request);
} else {
    // Legacy implementation
    processStandard(request);
}
```

#### Step 5: Testing Guidance

The skill provides unit test examples:

```cpp
TEST(LayoverTest, WhenDisabled_UsesStandardLogic) {
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "N");
    ASSERT_FALSE(ConfigManager::isLayoverEnabled());
    // Test standard behavior
}

TEST(LayoverTest, WhenEnabled_UsesLayoverLogic) {
    MockPropertiesManager::setValue("MIG_ENABLE_LAYOVER", "Y");
    ASSERT_TRUE(ConfigManager::isLayoverEnabled());
    // Test layover behavior
}
```

#### Step 6: Deployment Strategy

The skill recommends a rollout plan:
1. ✅ Deploy with default OFF (N)
2. ✅ Test in LOCAL (enabled)
3. ✅ Validate in UAT
4. ✅ Monitor metrics
5. ✅ Enable in PRD gradually
6. ✅ Full rollout after validation

## Common Usage Patterns

### Pattern 1: Simple Feature Flag

```
User: olaf create-otf-variable

Create a feature flag for the new caching system:
- Name: ENABLE_CACHE
- Values: true/false
- Default: false
- Enable in LOCAL
```

**Result**:
```xml
<variable name="ENABLE_CACHE" value="false" control="off" description="Enable response caching"/>
```

```cpp
bool isCacheEnabled = toolbox::PropertiesManager::GetInstance().isDefined("ENABLE_CACHE") &&
                      toolbox::PropertiesManager::GetInstance().getValue("ENABLE_CACHE") == "true";
```

### Pattern 2: Numeric Configuration

```
User: olaf create-otf-variable

Add retry count configuration:
- Name: MAX_RETRY_COUNT
- Values: numeric string
- Default: 3
- Override in PRD: 5
```

**Result**:
```xml
<common>
    <variable name="MAX_RETRY_COUNT" value="3" control="off" description="Maximum retry attempts"/>
</common>
<phase name="PRD">
    <variable name="MAX_RETRY_COUNT" value="5" control="off" description="Maximum retry attempts"/>
</phase>
```

```cpp
std::string retryStr = toolbox::PropertiesManager::GetInstance().getValue("MAX_RETRY_COUNT");
int maxRetries = std::stoi(retryStr);
```

### Pattern 3: Migration Flag

```
User: olaf create-otf-variable

Migration flag for new API:
- Name: MIG_ENABLE_NEW_API
- Values: Y/N
- Default: N
- Enable in LOCAL and UAT
```

**Result**:
```xml
<common>
    <variable name="MIG_ENABLE_NEW_API" value="N" control="off" description="Enable new API implementation"/>
</common>
<phase name="LOCAL">
    <variable name="MIG_ENABLE_NEW_API" value="Y" control="off" description="Enable new API implementation"/>
</phase>
<phase name="UAT">
    <variable name="MIG_ENABLE_NEW_API" value="Y" control="off" description="Enable new API implementation"/>
</phase>
```

## Tips & Best Practices

### Naming Conventions

✅ **Good**:
- `ENABLE_CACHE` - Clear feature toggle
- `MIG_ENABLE_LAYOVER` - Migration prefix
- `IS_PRODUCTION` - State flag
- `MAX_RETRY_COUNT` - Descriptive configuration

❌ **Avoid**:
- `ENABLE_IS_FEATURE_ENABLED` - Redundant
- `flag1` - Not descriptive
- `enableCache` - Wrong case convention
- `CACHE` - Unclear purpose

### Default Values

✅ **Safe Defaults**:
- Feature flags: `"N"` or `"false"` (OFF by default)
- Retry counts: Conservative values (e.g., `"3"`)
- Timeouts: Safe/tested values

❌ **Risky Defaults**:
- Feature enabled by default without testing
- Aggressive retry/timeout values
- Production-only configurations

### Environment Strategy

**Recommended Rollout**:
1. LOCAL - Always enable for development
2. UAT - Enable after initial validation
3. PRD - Enable gradually with monitoring

**Avoid**:
- Enabling in PRD before LOCAL/UAT testing
- Same value across all environments (no override benefit)
- Too many environment-specific overrides (complexity)

## Troubleshooting

### Variable Not Recognized

**Problem**: Runtime error or feature not working

**Solutions**:
1. Verify XML file is loaded by component
2. Check variable name spelling (case-sensitive)
3. Restart application to reload configuration
4. Check OTF logs for XML parsing errors

### Override Not Applied

**Problem**: Getting common value instead of phase override

**Solutions**:
1. Verify phase name matches environment exactly
2. Check XML syntax (properly closed tags)
3. Ensure phase section comes after common section
4. Restart application after XML changes

### Accessor Always Returns False

**Problem**: Feature flag always disabled

**Solutions**:
1. Verify `isDefined()` check passes
2. Check exact value comparison (case-sensitive)
3. Ensure XML has correct value
4. Debug PropertiesManager call to see actual value

## Next Steps

After creating your OTF variable:

1. **Review the code** with your team
2. **Write unit tests** for both enabled/disabled states
3. **Test in LOCAL** environment first
4. **Document** the feature flag in your component docs
5. **Monitor** behavior in each environment
6. **Plan cleanup** after migration is complete

## Related Resources

- OTF Configuration Guide - Comprehensive reference
- OTF Workflow - Detailed step-by-step guide
- Component XML documentation - Project-specific structure

## Need Help?

- Check existing variables in your component XML for patterns
- Review C++ code for existing PropertiesManager usage
- Consult team for project-specific conventions
- Use `olaf get-bms-expertise` for component-level questions
