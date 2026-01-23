# Tutorial: get-bms-expertise

## Introduction

This tutorial guides you through using the `get-bms-expertise` skill to access expert-level guidance on Amadeus BMS (Build Management System). You'll learn how to activate the expert persona and get help with common BMS challenges.

## Prerequisites

Before starting, you should have:
- Basic familiarity with C/C++ build systems
- Access to a BMS-managed codebase (optional, for hands-on practice)
- Understanding of component-based architecture concepts

## Step-by-Step Instructions

### Step 1: Activate BMS Expert Mode

Invoke the skill to activate the expert persona:

```
Execute get-bms-expertise
```

You'll receive confirmation:

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

### Step 2: Ask Your BMS Question

Once activated, ask any BMS-related question. The expert will provide detailed, actionable guidance.

**Example questions:**
- "How do I add an external dependency to my component?"
- "Why am I getting binary incompatibility errors?"
- "How do I set up a forest workspace?"
- "What's the best way to optimize my build times?"

### Step 3: Follow the Diagnostic Process

For troubleshooting questions, the expert follows a systematic methodology:

1. **Context First**: Understanding your component type and structure
2. **Version Awareness**: Checking BMS version and channel
3. **Configuration Analysis**: Reviewing bmsrc cascade
4. **Error Diagnosis**: Examining error messages and logs
5. **Incremental Solutions**: Starting simple, escalating as needed

### Step 4: Apply Recommendations

The expert provides:
- Specific Description.xml snippets
- Exact bmsrc configurations
- Validation commands to verify changes
- Warnings about compatibility risks

### Step 5: Validate Changes

After applying recommendations, use validation commands:

```bash
# Check configuration
bms -s

# View dependency graph
bms deps

# Build and test
bms build
bms test
```

## Common Use Cases

### Adding Dependencies

**Question**: "How do I add an external dependency?"

**Expert Response**:
```xml
<!-- External dependency (transitively visible) -->
<dependency type="external" name="mdw::Toolbox" version="11-0-0-5"/>

<!-- Internal dependency (hidden from clients) -->
<dependency type="internal" name="mdw::Boost"/>
```

### Resolving Version Conflicts

**Question**: "I'm getting version conflicts in my dependencies"

**Expert Response**:
1. Run `bms deps` to visualize the dependency graph
2. Identify conflicting versions
3. Use versioner or explicit version specification
4. Validate with `bms deps --unpack`

### Optimizing Build Performance

**Question**: "My builds are taking too long"

**Expert Response**:
1. Check parallel build settings: `build.parallel`
2. Review dependency graph for unnecessary dependencies
3. Consider local replication: `bms replicate`
4. Tune based on available memory

### Setting Up Forest Workspaces

**Question**: "How do I work with multiple components?"

**Expert Response**:
1. Create Forest.xml with component constraints
2. Use `bms --use-forest build` for forest mode
3. Manage local dependencies with `version="local"`

## Verification Checklist

After getting expert guidance, verify:

- [ ] Recommendations are specific to your BMS version
- [ ] Description.xml changes follow proper syntax
- [ ] Validation commands confirm expected behavior
- [ ] Binary compatibility rules are respected
- [ ] Changes work across required environments

## Troubleshooting

### Expert Doesn't Understand Context

**Symptom**: Responses seem generic or off-target

**Solution**:
1. Provide more context about your component
2. Share relevant Description.xml snippets
3. Include error messages verbatim
4. Specify your BMS version

### Recommendations Don't Work

**Symptom**: Applied changes cause new errors

**Solution**:
1. Verify BMS version compatibility
2. Check for typos in configuration
3. Review the complete error message
4. Ask for alternative approaches

### Need More Detailed Information

**Symptom**: Need deeper technical details

**Solution**:
1. Ask the expert to reference the knowledge base
2. Use `tell-me` skill for specific BMS topics
3. Request links to BMS documentation sections

### Complex Architectural Questions

**Symptom**: Question requires BMS admin input

**Solution**:
The expert will recommend escalation to:
1. R&D Request Portal (topic: BMS)
2. BMS admin mailing list
3. Current BMS support "sheriff"

## Next Steps

After using the BMS expert:

- **Apply recommendations**: Implement suggested changes
- **Validate thoroughly**: Test in all required environments
- **Document decisions**: Record architectural choices
- **Share knowledge**: Help team members with similar issues

## Tips for Success

1. **Be specific**: Include component names, versions, and error messages
2. **Share context**: Describe your forest structure and dependencies
3. **Ask follow-ups**: Clarify any unclear recommendations
4. **Validate incrementally**: Test changes step by step
5. **Note version-specific behavior**: BMS behavior varies by version

## Essential Commands Reference

```bash
# Core workflow
bms build              # Compile componentPack
bms build -t           # Build unitTestPack
bms test               # Run unit tests
bms deliver            # Full delivery pipeline

# Dependency management
bms deps               # View dependency graph
bms deps --unpack      # Show aggregated dependencies
bms replicate          # Cache dependencies locally

# Configuration
bms -s                 # Show configuration
bms -p <profile>       # Use specific profile

# Forest operations
bms --use-forest build # Force forest mode
bms --no-forest build  # Disable forest mode
```
