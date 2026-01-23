# Description.xml

## Summary
The `Description.xml` file is the core configuration file for BMS components. It defines component metadata, dependencies, build instructions, and delivery specifications. Every BMS component requires this XML file at the root of its directory tree. It serves as the single source of truth for component identification, version management, dependency resolution, and build/delivery processes.

> **Key Use Case:**  
> When creating a new BMS component or modifying existing component structure, the Description.xml must be updated to reflect changes in dependencies, build configuration, or public API.

---

## Key Concepts

- **componentPack**: The main component defined in Description.xml with the same name as the file
- **unitTestPack**: Optional test executable component automatically marked for testing (name = componentPack + "UnitTest")
- **Test Executables**: Special components for unit testing, either standalone or unitTestPack
- **Dependencies**: External (headers required by clients) vs Internal (headers not exposed to clients)
- **Versioners/Packs**: Components that specify dependency versions without creating dependencies
- **Public Includes**: Header files defining the component's public API (must follow namespace convention)
- **Configs**: Component flavors/variants (typically just "main" config)
- **Namespacing**: Component names use `::` separator (e.g., `mdw::Toolbox`)
- **Version Format**: 4 integers separated by `.` or `-` (e.g., `1-2-0-3`)

---

## XML Structure

### Root Element: `<componentDescription>`
```xml
<componentDescription version="1.0"
    xmlns="http://gcnet/documentation/bms/metadata/1-0/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://gcnet/documentation/bms/metadata/1-0/
    https://bms.cloud.rnd.amadeus.net/bmsdoc/users/_static/Description.xsd">
```

**Main sections:**
- `<properties>`: General component information (name, version, public API)
- `<componentPack>`: Build and dependency details for main component
- `<unitTestPack>`: Optional test executable component

---

## Properties Section

### Basic Attributes
```xml
<properties name="obe::utils" version="1-5-0-0" type="dependency">
    <abstract>Component description and purpose</abstract>
    <contactPoint>DEV-TEAM-CODE (email@example.com)</contactPoint>
    <configs>
        <config name="main" default="true"/>
    </configs>
</properties>
```

**Key attributes:**
- `name`: Component identifier with namespace (e.g., `foo::bar`)
- `version`: 4-part version number
- `type`: `dependency` (default) or `pack` (versioner-only components)
- `private`: Set to `true` to hide from delivered Descriptions (default: `false`)
- `abstract`: Human-readable description
- `contactPoint`: Team responsible (Chorus code/Aproach group + emails)

### Public Includes
```xml
<publicIncludes>
    <dir name="include" filters="*.hpp"/>
    <dir name="include2" filters="*.hpp *.i" excludes="foobar.hpp"/>
</publicIncludes>
```

**Critical convention:** Public includes should mirror component name  
Example: `foo::bar` → headers in `include/foo/bar/`

**Attributes:**
- `name`: Directory path relative to Description.xml
- `filters`: Space-separated shell patterns for files to include
- `excludes`: Space-separated patterns to exclude
- Always recursive within specified directories

---

## Dependencies

### Direct Dependencies
```xml
<componentPack>
    <dependencies>
        <dependenciesForConfig configs="main">
            <dependency type="external" name="foo::bar" version="1-0-0-0"/>
            <dependency type="internal" name="mdw::Boost" version="1-33-1-2"/>
        </dependenciesForConfig>
    </dependencies>
</componentPack>
```

**Dependency types:**
- **`external`**: Dependency headers are #included by your public headers (transitive to clients)
- **`internal`**: Dependency headers used only in implementation (not exposed to clients)

### Versioners (Packs)
```xml
<versioner name="mdw::Pack" version="1-7-0-2"/>
<dependency type="external" name="mdw::Toolbox"/>  <!-- version from versioner -->
<dependency type="external" name="mdw::Boost" version="1-33-1-1"/>  <!-- explicit version -->
```

**Purpose:** Specify dependency versions without creating dependency relationships  
**Common packs:** `mdw::Pack`, `sbm::Pack`, `ngi::Pack`

### Local Dependencies (Legacy - Use Forests Instead)
```xml
<dependency type="internal" name="mdw::IDSC" version="local" path="../mdw_idsc"/>
```

**⚠️ Warning:** Prefer using Forests over local dependencies for multi-component development

---

## Build Section

### Library Component
```xml
<build>
    <buildForConfig configs="main">
        <library name="utils" customizedName="false" deliver="true">
            <sources>
                <dir name="src" recursive="true" filters="*.cpp *.c"/>
            </sources>
            <flags>
                <cppFlags>-DPRIVATE_FLAG=1</cppFlags>
                <cxxFlags>-std=c++17</cxxFlags>
                <ldFlags>-z PRIVATE_KEYWORD</ldFlags>
            </flags>
        </library>
        
        <includes>
            <dir name="src" recursive="true" filters="*.h *.hpp"/>
        </includes>
        
        <!-- Public flags inherited by clients -->
        <flags>
            <cppFlags>-DPUBLIC_FLAG=1</cppFlags>
            <ldFlags>-z PUBLIC_KEYWORD</ldFlags>
        </flags>
        
        <systemLib>pthread</systemLib>
    </buildForConfig>
</build>
```

**Library naming:**
- `customizedName="false"`: `scs::bms::comp` + `name="lib1"` → `libScsBmsLib1.so`
- `customizedName="true"`: `name="comp1"` → `libcomp1.so`

**Flags:**
- **Private flags** (in `<library>`/`<binary>`): Used only when building this component
- **Public flags** (in `<buildForConfig>`): Inherited by client components
- ⚠️ Avoid changing warnings in public flags (impacts all clients)

### Binary Component
```xml
<binary name="myapp" customizedName="true">
    <sources>
        <dir name="src" recursive="true" filters="*.cpp"/>
    </sources>
    <buildPath>$(GLB_BUILD_BIN_DIR)</buildPath>
    <systemLib>dl</systemLib>
    <linkMode mode="dynamic">
        <specialMode>
            <component name="mdw::xxx" mode="static"/>
            <component name="mdw::yyy" mode="none"/>
        </specialMode>
    </linkMode>
</binary>
```

**Link modes:**
- `dynamic`: Shared library linking
- `static`: Static library linking  
- `none`: Component not built by BMS (e.g., shell scripts)

**Special mode:** Override link mode for specific dependencies

---

## Delivery Section

```xml
<delivery>
    <dir name="src" recursive="true" filters="*.cpp" artifact="user"/>
    <dir name="jar" recursive="true" filters="*.jar" artifact="lib"/>
    <dir name="etc" recursive="false"/>
</delivery>
```

**Auto-delivered:** Description.xml, libraries/binaries, public includes  
**Artifact types:** Groups files for optimized download from Artifact Repository

---

## Suppressions Section

```xml
<suppressions>
    <plugin name="valgrind"/>
    <plugin name="cppcheck" files="cppcheck.suppr cppcheck2.suppr"/>
</suppressions>
```

**Purpose:** Specify suppression files for test analysis tools  
**Location:** Files must be in `suppressions/` folder  
**Default:** If no `files` attribute, looks for `<plugin_name>.suppr`

---

## unitTestPack Component

```xml
<unitTestPack>
    <dependencies>
        <dependenciesForConfig configs="main">
            <versioner name="mdw::Pack" version="1-7-0-2"/>
            <dependency type="internal" name="obe::utils" version="local" path="."/>
            <dependency type="internal" name="mdw::CppUnit"/>
        </dependenciesForConfig>
    </dependencies>
    <build>
        <buildForConfig configs="main">
            <binary name="test">
                <sources>
                    <dir name="test" recursive="true" filters="*.cpp"/>
                </sources>
                <linkMode mode="dynamic"/>
            </binary>
        </buildForConfig>
    </build>
</unitTestPack>
```

**Characteristics:**
- Automatically marked as test executable
- Name = componentPack name + "UnitTest"
- Not delivered
- Cannot be used as dependency by other components
- Tests companion componentPack component

**Alternative:** Mark componentPack with `standalone-test-executable="true"` for test executables testing multiple components

---

## Validation

**Schema validation:**
- Standard mode: `Description.xsd`
- Forest mode: `Description_weak.xsd` (relaxed versioner requirements)

**Contact point validation:**
- Checked during `bms deliver` unless `skip_poc_validation` option set
- Must be valid Chorus code or Aproach assignee group

---

## Best Practices

1. **Public API Organization:**
   - Keep public includes minimal (only essential API)
   - Follow namespace convention: `foo::bar` → `include/foo/bar/`
   - Avoid exposing implementation details in public headers

2. **Dependencies:**
   - Mark dependencies correctly (external vs internal) for proper transitivity
   - Use versioners to centralize version management
   - Prefer Forests over local dependencies for multi-component work

3. **Flags:**
   - Use private flags for component-specific compilation needs
   - Minimize public flags to avoid impacting clients
   - Never modify warnings via public flags

4. **Testing:**
   - Include unitTestPack for quality assurance
   - Unit tests detect errors early (shift-left)
   - Tests serve as usage examples for clients

5. **Naming:**
   - Use descriptive component names with proper namespacing
   - Follow library naming conventions (customizedName usage)

6. **Version Management:**
   - Use 4-part versioning consistently
   - Only use `technicalVersion` when absolutely necessary
   - Update versions appropriately for binary compatibility

---

## Common Commands

```bash
# Validate Description.xml against schema
xmllint --schema Description.xsd Description.xml

# Build component with BMS
bms build

# Deliver component to repository
bms deliver

# Run unit tests
bms test

# Work with multiple related components (use Forest)
bms forest create
```

---

## Related Documentation

- **Algorithms**: Dependency resolution and version selection
- **Forest**: Multi-component development workflow
- **BMS Configs**: Component flavors/variants (advanced)
- **Interface and Implementations**: Interface/implementation pattern
- **Artifact Repository**: Delivery optimization and artifact management
