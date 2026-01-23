# BMS Advanced Concepts

## Summary
This document covers advanced BMS (Build Management System) concepts for experienced users working with complex component architectures, delivery systems, and optimization techniques. These features address performance optimization (aggregated components), artifact management, configuration variations, code generation, dependency patterns, forest organization, build customization, snapshots, toolchain management, and version filtering.

> **Context**: When working on large-scale Amadeus projects, these advanced features help manage complexity, reduce startup times, control delivery artifacts, handle platform differences, and maintain flexible dependency graphs without sacrificing modularity.

---

## Key Concepts

### 1. **Aggregated Components**
- **Purpose**: Combine multiple BMS components into a single library to reduce startup time and library count
- **Partial Mode**: Components built with `partial=1` produce `.ro` (relocatable object) files instead of shared libraries
- **Aggregated Dependencies**: Dependencies marked with `mode="aggregated"` are embedded into the parent library
- **Delivery Optimization**: Only the aggregated pack needs delivery; aggregated dependencies propagate their headers and transitive dependencies
- **Graph Resolution**: Aggregated dependencies cannot be binary-compatible upgraded; version freezing prevents conflicts

### 2. **Artifact Repository (AR)**
- **Artifacts**: Atomic replication units (Description, headers, libraries, binaries, etc., config, docs, test support, user files)
- **Lazy Replication**: BMS retrieves only required artifacts from Artifactory on-demand
- **Nickname System**: Single-character IDs for artifacts (D=description, I=include, L=lib, B=bin, E=etc, O=doc, T=test, U=user)
- **Server Configuration**: `[ar]` section controls artifactory server, credentials, and retry behavior
- **Priority Order**: Stand-alone > local FS > remote FS > AR repositories

### 3. **BMS Configs (Component Flavours)**
- **Configuration**: Set of parameters (dependencies, build options) characterizing a component build
- **Valid Uses**: Different library names, compile flags, OS-specific implementations
- **Invalid Uses**: Platform differences, threading modes, debug/release, compiler differences
- **Exponential Problem**: n configs in one component forces n configs in all clients (combinatorial explosion)
- **Alternative**: Prefer Interface/Implementation pattern over configs when possible

### 4. **Code Generators**
- **Supported**: `mdw::GrammarGenerator`, `mdw::ABRGenerator`, `mdw::XDSC`
- **Configuration**: Defined in `Description.xml` with `<generator>` tag specifying name, version, config file
- **Output Directory**: Must be dedicated (non-committed) as BMS cleans it on rebuild
- **Generator Path**: `generator.path=` line in config file tells BMS where files are generated
- **Binary Requirement**: Generator must accept config file path as parameter

### 5. **Forest of Forests**
- **Problem**: Need to work on components from multiple forests simultaneously without fake deliveries
- **Not Implemented**: BMS explicitly does not support forest-of-forest dependencies
- **Workaround**: Copy components to your forest, replicate constraints, use include_conf for shared bmsrc settings
- **Validation Issue**: Validating one forest through another's tests provides only partial validation

### 6. **Interface and Implementations**
- **Interface Component**: Publishes headers with `interface="true"`, defines no library
- **Implementation Component**: Uses `provide="interface_name"` to specify which API it implements
- **Benefits**: Avoid configuration explosion, swap implementations at dependency resolution time
- **Multiple Implementations**: Multiple components can provide same interface (e.g., sqlite vs oracle backends)

### 7. **Makefiles**
- **Structure**: Main Makefile includes settings.mk (BMS-generated) + CFC's Makefile.inc + build.mk
- **Generated Variables**: All prefixed with `BMS_`, defined in `settings.mk`
- **No Customization**: BMS philosophy hides build system; use plugins instead of modifying makefiles
- **Debugging**: Use `gmake -s eval VAR='$(AMD_DEBUG)'` or `gmake -np > output.log` for troubleshooting

### 8. **Snapshots** (Future Feature)
- **Definition**: Delivered but unreleased components for testing/CI
- **Uniqueness**: Snapshots replace previous snapshots; no version-specific snapshot dependencies
- **Promotion**: Can be promoted to delivered component after validation
- **Restrictions**: Delivered components cannot depend on snapshots; automatic replication on updates
- **Identified By**: `snapshot="###"` attribute in properties tag

### 9. **Toolchain**
- **Purpose**: Low-level libraries/binaries for kernel interface, breaking distribution dependency
- **Location**: `/opt/1A/toolchain`
- **Profile Selection**: Auto-generated profiles like `dev_x86_64-2.6.16-v1`
- **Build Packs**: Enhanced toolsets (make, zlib, ccache) built with toolchain for reproducibility
- **Library Path**: Changes to `lib/<toolchain_name>/<Debug|Release>/`

### 10. **Version Filters**
- **Syntax**: Comparison (`> 16-0-12-4`), logical operators (`and`, `or`, `not`), wildcards (`16-0-*`), ranges (`16-0-12-4;16-0-42-60`)
- **Operators**: `<`, `>`, `<=`, `>=`, `!=`, `=`
- **Usage**: Constraints, versioners, dependencies, generators in Forest.xml or Description.xml
- **No Parentheses**: Logical precedence is `and` before `or`

---

## Usage

### Aggregated Components

**Building Aggregated Dependencies:**

```bash
# In aggregated dependency's .bms/bmsrc
[build]
partial = 1
[deliver]
dry_run = 1
```

**Defining Aggregated Pack:**

```xml
<dependenciesForConfig configs="main">
    <versioner name="mdw::Pack"/>
    <dependency name="sbm::element::Address" version="5-1-0-2" type="external" mode="aggregated" />
    <dependency name="sbm::element::Air" version="9-0-0-3" mode="aggregated" />
    <dependency name="sbm::BasicUtils" version="6-0-0-6" type="external" />
</dependenciesForConfig>
```

**Display Aggregated Dependencies:**

```bash
# Hide aggregated dependencies (default)
bms deps

# Show all aggregated dependencies
bms deps --unpack
```

### Artifact Repository

**Configure AR Access:**

```bash
# In ~/.bmsrc or .bms/bmsrc
[ar]
system = artifactory
server = https://repository.rnd.amadeus.net
searchlogin = bmslocaldevuser
searchpass = bmslocaldevuser
# Or use password command
searchpass = command:pass show amadeus/artifactory-api-key
retries = 3
```

**Deliver with Custom Artifact Assignment:**

```xml
<delivery>
    <dir name="jar" recursive="true" artifact="lib"/>
    <dir name="src" recursive="true" artifact="user"/>
    <scm type="hg" repository="~intscs/MyRepo"/>
</delivery>
```

**Replicate from AR:**

```bash
# Forced replication with artifact detail
bms replicate -f

# Output shows artifact IDs:
# D IL    mdw::Toolbox    11-0-0-5
# (D=description, I=include, L=lib replicated)
```

### BMS Configs

**Define Configurations:**

```xml
<properties name="mdw::RFD" version="5-2-0-5">
    <configs>
        <config name="sqlite" default="true"/>
        <config name="ora"/>
    </configs>
</properties>

<componentPack>
<dependencies>
    <dependenciesForConfig configs="sqlite">
        <dependency type="external" name="mdw::SQL::sqlite" version="9-4-2-0"/>
    </dependenciesForConfig>
    
    <dependenciesForConfig configs="ora">
        <dependency type="external" name="mdw::SQL::oracle" version="9-4-2-0"/>
    </dependenciesForConfig>
</dependencies>
</componentPack>
```

### Code Generators

**Standard Generator Usage:**

```xml
<generator name="mdw::GrammarGenerator" version="4-1-1-7" configfile="etc/edi.conf"/>
<generator name="mdw::ABRGenerator" version="2-3-0-0" configfile="etc/abr.conf"/>
<generator name="mdw::XDSC" version="1-6-0-45" configfile="etc/xdsc.conf"/>
```

**Silent Code Cleanup:**

```bash
# In .bmsrc
[clean]
interactive_clean_generated_code = 0
```

### Interface/Implementation

**Interface Definition:**

```xml
<properties name="bms::name::api" version="13-0-0-0" interface="true">
    <publicIncludes>
        <dir name="include" filters="*.h" />
    </publicIncludes>
</properties>
```

**Implementation Definition:**

```xml
<properties name="bms::name::impl1" version="13-0-0-0" provide="bms::name::api">
    <library in="impl1">
        <sources>
            <dir name="src" filters="*.cpp"/>
        </sources>
    </library>
</properties>
```

### Toolchain

**Select Toolchain Profile:**

```bash
# View toolchain profile
bms -p dev_x86_64-2.6.16-v1 -s

# Profile shows:
# [profile_dev_x86_64-2.6.16-v1]
# inherits_from = devg4
# build.compiler_path = /opt/1A/toolchain/x86_64-2.6.16-v1
# bms.toolchain_path = /opt/1A/toolchain
# bms.toolchain_name = x86_64-2.6.16-v1
```

**Build Pack Configuration:**

```bash
# In .bmsrc - use specific buildpack
[bms]
buildpack_name = default

# Disable buildpack (not recommended)
buildpack_name =
```

### Version Filters

**In Forest.xml:**

```xml
<constraints>
    <!-- Latest 16-0-0-* version -->
    <component name="mdw::Pack" version="16-0-0-*" type="strong" />
    
    <!-- Range -->
    <component name="foo::bar" version="16-0-12-4;16-0-42-60" type="strong" />
    
    <!-- Complex expression -->
    <component name="baz::qux" version=">= 16-0-0-0 and < 16-1-0-0 or >= 18-0-0-0 and < 18-1-0-0" type="strong" />
</constraints>
```

**In Description.xml:**

```xml
<dependenciesForConfig configs="main">
    <versioner name="mdw::Pack" version="16-0-0-*" type="strong"/>
    <dependency type="external" name="foo::bar" version="16-*"/>
    <generator name="my::GrammarGenerator" version="16-*" configfile="etc/my.conf"/>
</dependenciesForConfig>
```

---

## Common Patterns

### Aggregated Component Best Practices
- Use aggregation to reduce library count for startup performance
- Build aggregated dependencies with `partial=1` and `dry_run=1`
- Only deliver the top-level aggregated pack
- Use `bms deps --unpack` to troubleshoot aggregation issues
- Remember: aggregated dependencies freeze versions (no binary-compatible upgrades)

### Artifact Management
- Lazy replication minimizes AR bandwidth usage
- Use artifact assignment in `<delivery>` section for custom files
- Check replicated artifacts with `bms replicate -f` output
- Configure AR credentials once in `~/.bmsrc`

### Configuration vs Interface/Implementation
- **Use Configs** when: Managing OS-specific builds, different compile flags
- **Use Interface/Implementation** when: Swapping backends, optional features, avoiding config explosion
- **Avoid Configs** for: Debug/release, threading, compiler differences (BMS handles these)

### Code Generator Integration
- Always specify version for reproducibility (or use versioners)
- Dedicate output directory (will be cleaned on rebuild)
- Set `interactive_clean_generated_code = 0` for automation
- Generator paths in config are relative to component root (except XDSC: relative to config file)

### Version Filter Strategies
- Wildcard (`16-0-*`) for latest patch in minor version
- Range (`16-0-12-4;16-0-42-60`) for known-good version range
- Complex expressions for multi-version support across major releases
- Remember: `and` has higher precedence than `or`

---

## Troubleshooting

### Aggregated Components Issues
- **Problem**: Linking fails with undefined symbols
  - **Cause**: Aggregated dependency not built in partial mode
  - **Solution**: Check `.bms/bmsrc` has `partial=1` in aggregated dependencies

- **Problem**: Version conflict with aggregated dependency
  - **Cause**: Same component aggregated in multiple places with different versions
  - **Solution**: Use `bms deps --unpack` to identify conflicts; unify versions

### Artifact Repository Issues
- **Problem**: Component not found in AR
  - **Cause**: Not delivered to AR, or credentials incorrect
  - **Solution**: Check `[ar]` configuration; verify delivery repository setting

- **Problem**: Slow replication from AR
  - **Cause**: Network latency, AR server congestion
  - **Solution**: Use local repositories when possible; check `[ar] retries` setting

### Configuration Problems
- **Problem**: Exponential configuration growth
  - **Cause**: Multiple dependencies with different configs
  - **Solution**: Refactor to use Interface/Implementation pattern

- **Problem**: Config not found in Forest.xml
  - **Cause**: Client didn't specify config for dependency
  - **Solution**: Review Forest.xml constraints; ensure config consistency

### Toolchain Issues
- **Problem**: Binary incompatibility with system libraries
  - **Cause**: Wrong toolchain selected or missing toolchain
  - **Solution**: Verify `/opt/1A/toolchain/<name>` exists; check profile selection

- **Problem**: Build fails with toolchain profile
  - **Cause**: Buildpack incompatibility
  - **Solution**: Check buildpack version; try `buildpack_name = ` to disable

---

## References

- **Related Topics**: Component Management, Forest Structure, Dependency Resolution, Delivery Process
- **BMS Documentation**: Unix Concepts, Description.xml, Forest.xml, BMS Plugins
- **Alternative Approaches**: Consider Interface/Implementation before using BMS Configs
- **Performance**: Aggregated components primarily for reducing startup time in large applications
- **Artifact Repository**: Introduced in BMS 2.5.0 for centralized component delivery
