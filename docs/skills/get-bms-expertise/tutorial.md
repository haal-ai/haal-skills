# Get BMS Expertise - Tutorial

Learn how to use the BMS expert persona to solve build system problems.

## Step 1: Activate BMS Expertise

```bash
olaf get-bms-expertise
```

You'll see confirmation:
```
✅ BMS Expert Mode Activated

I'm now operating as a Senior BMS Specialist...
```

## Step 2: Ask BMS Questions

The AI now thinks like a BMS expert. Ask questions naturally:

### Example 1: Build Issues

```
User: My component won't compile, I'm getting link errors

AI: Let me help diagnose this link error using the BMS problem-solving approach.

1. Context First: What type of component are you building (library/binary)?
2. Check Description.xml: Are all .cpp files listed in <sources>?
3. Verify dependencies: Run `bms deps` to check your dependency graph

[Provides structured troubleshooting steps...]
```

### Example 2: Dependency Management

```
User: Should I use external or internal dependency for this library?

AI: This depends on whether the library is part of your component's public API.

External dependencies:
- Transitively visible to components that depend on you
- Use when: Library types appear in your public headers
- Example: <dependency type="external" name="mdw::Toolbox"/>

Internal dependencies:
- Hidden from clients
- Use when: Library only used in .cpp files
- Example: <dependency type="internal" name="mdw::Boost"/>

[Provides XML examples and best practices...]
```

### Example 3: Performance Optimization

```
User: My forest builds are slow, how can I optimize?

AI: Let's optimize your forest build performance:

1. Check current parallelism: `bms -s | grep parallel`
2. Balance forest.parallel vs build.parallel
3. Consider memory constraints

[Provides specific tuning recommendations...]
```

## Step 3: Deep Dive with Knowledge Base

For detailed documentation:

```
User: I need the complete list of test plugins and their options

AI: For comprehensive plugin documentation, use:

`olaf tell me about BMS plugins`

This will retrieve the complete plugin reference from the knowledge base,
covering all 27+ plugins with configuration options.

Or I can provide a quick overview of the main plugins:
- build: Compilation with profiles
- test: Orchestrates unittest, valgrind, callgrind, cppcheck
- deliver: Full delivery pipeline
[...]
```

## Step 4: Get Configuration Examples

Ask for specific configurations:

```
User: Show me how to configure a development profile with ccache

AI: Here's a bmsrc configuration for a dev profile with ccache:

```bmsrc
[default]
profile = dev

[dev]
build.ccache = true
build.parallel = 8
test.plugins = unittest,valgrind

[repositories]
[0] = ar://bms-release-public
```

[Explains each setting...]
```

## Common Use Cases

### 1. Troubleshooting Build Failures
- Link errors → Check sources in Description.xml
- Compilation errors → Analyze cppFlags, cxxFlags
- Generator failures → Examine bms.log

### 2. Managing Dependencies
- Binary incompatibility → Manual version specification
- Missing dependencies → Check repositories config
- Circular dependencies → Architectural refactoring

### 3. Delivery Issues
- Version conflicts → Version bump strategy
- Test failures → Review test/logs/
- SCM tagging → Verify uncommitted changes

### 4. Forest Workspace
- Setup multi-component workspace
- Resolve constraint conflicts
- Execute forest-level operations

## Tips

✅ **Be specific**: "My unittest plugin fails" vs "Tests don't work"  
✅ **Provide context**: Component type, BMS version, error messages  
✅ **Ask for examples**: "Show me an example Description.xml for..."  
✅ **Request validation**: "How do I verify this configuration?"  

## Exit Expertise Mode

Simply start a new conversation or use another skill. The persona is session-specific.

## Need More Help?

- Detailed docs: `olaf tell me about BMS <topic>`
- Full documentation: `.olaf/data/kb/bms/`
- Escalate to BMS team: NCE-BMS-Admin@amadeus.com
