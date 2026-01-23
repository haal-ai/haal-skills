# BMS Forest

## Summary
BMS Forest is a workspace feature that enables multi-component development by describing a project workspace containing one or more checked-out BMS components. It allows BMS to understand which components are actively being developed and manage their dependencies locally without requiring version numbers or BMS repositories for inter-component references. This streamlines local development, mass compilation/delivery, and software migrations (e.g., new MDW or SBM packs).

> Forest enables developers to work on multiple interdependent components simultaneously, perform operations (build, clean, deliver) across the entire forest while respecting dependency order, and avoid redelivery during development cycles.

---

## Key Concepts

- **Forest.xml** - Central metadata file describing the workspace, listing components being worked on, constraints, and build flags
- **Local Dependencies** - Components within the forest reference each other without version numbers; BMS uses the Forest.xml to resolve paths
- **Constraints** - Forest-level specification of dependency/versioner versions and compilation flags applied to all components
- **Auto-discovery** - Components with `version="local"` are automatically considered part of the forest without explicit Forest.xml listing
- **Component vs Forest Level** - BMS automatically detects whether to operate on a single component or the entire forest based on directory context
- **ROOT Components** - Top-level components with no forest dependencies; LEAF components are dependencies with no forest dependents
- **Topological Sort** - Operations respect dependency ordering (LEAF to ROOT for builds)
- **Forest Delivery** - All components delivered together with automatic Description.xml patching to include explicit versions

---

## Forest.xml Structure

### Basic Properties
```xml
<?xml version="1.0" encoding="UTF-8"?>
<forestDescription xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://gcnet/documentation/bms/metadata/1-0/Forest.xsd">
    
    <properties name="basic::Forest" version="1-0-0-0">
        <abstract>Description of the forest project</abstract>
        <contactPoint>TEAM-CODE, email@amadeus.com</contactPoint>
    </properties>
</forestDescription>
```

### Components List
```xml
<components>
    <component name="foo" />
    <component name="bar" path="/custom/path/to/bar" />
    <component name="nil" version="1-0-0-0" />
    <component name="baz" activated="false" /> <!-- Excluded from forest -->
</components>
```

**Default Path Resolution**: Component `foo::bar` defaults to path `foo/bar` relative to Forest.xml

### Constraints
```xml
<constraints>
    <!-- Versioner constraints -->
    <component name="mdw::Pack" version="1-8-0-0" type="strong" />
    <component name="sbm::Pack" version="9-0-0-0" />
    
    <!-- Frozen components (not modified by BMS) -->
    <component name="sbr::Toolbox" version="5-0-0-0" />
    
    <!-- Build flags for all components -->
    <build>
        <library>
            <flags>
               <cppFlags>-DFOO -DBAR</cppFlags>
               <ldFlags append="true">-g</ldFlags>
            </flags>
        </library>
     </build>
</constraints>
```

---

## Dependency Resolution

### Inside Forest (No Version Specified)
```xml
<!-- In component's Description.xml -->
<dependencies>
    <dependenciesForConfig configs="main">
        <versioner name="mdw::Pack" />  <!-- Resolved from Forest constraints -->
        <dependency type="internal" name="bar" />  <!-- Local forest component -->
        <dependency type="external" name="mdw::Tracer" />  <!-- Resolved via versioner -->
    </dependenciesForConfig>
</dependencies>
```

**Resolution Algorithm**:
1. Search in Forest.xml `<components>` list (use local path)
2. Search in Forest.xml `<constraints>` (use BMS repository)
3. Search in component's versioners
4. Error if not found

### Outside Forest (Version Specified)
```xml
<!-- Explicit version = resolved via BMS repositories, not forest -->
<dependency type="external" name="mdw::Boost" version="1-33-1-2" />
```

### Auto-discovery Mode
```xml
<!-- In Description.xml -->
<dependency type="internal" name="bom::base" version="local" />
<!-- OR with custom path -->
<dependency type="internal" name="bom::base" version="local" path="../bom/base" />
```

Components marked with `version="local"` are auto-discovered and added to the forest without Forest.xml modification.

---

## Usage

### Forest Detection
BMS automatically searches for `Forest.xml` upward from current directory. If found, forest mode is activated.

```bash
# Directory structure
Forest.xml
├── foo/
│   └── Description.xml
└── bar/
    └── Description.xml

# Commands in foo/ directory operate on component foo (Description level)
cd foo
bms build  # Builds foo and its local dependencies

# Commands at forest root operate on entire forest
cd ..
bms build  # Builds all components (topological order: LEAF→ROOT)
```

### Manual Forest Control
```bash
# Force forest mode (even inside component directory)
bms --use-forest build

# Disable forest mode
bms --no-forest build

# Specify custom Forest.xml location
bms --forest-xml /path/to/Forest.xml build
```

### Forest Build
```bash
# At forest level: builds all components
bms build

# Build with error handling
bms --on-error=stop build           # Stop on first error
bms --on-error=best_effort build    # Skip failed components (default)
bms --on-error=ignore build         # Continue despite errors

# Parallel builds
bms build  # Uses [forest] parallel setting from bmsrc
```

### Forest Deliver
```bash
# Delivers all forest components in dependency order
bms deliver

# Delivery process:
# 1. Check which components need delivery
# 2. Run version upgrade plugin (if activated)
# 3. Perform source management and dependency checks
# 4. Build all components
# 5. Run all tests
# 6. Tag source, publish to repository, send release notes
```

**Important**: Delivered Description.xml files are automatically patched with:
- Explicit versions for all dependencies (replaces `version="local"` or missing versions)
- Constraint versions from Forest.xml
- No forest reference required for delivered components

### Follow Dependencies
```bash
# At component level, build only this component (not deps)
cd foo
bms --no-follow-deps build

# At component level, build with dependencies (default)
cd foo
bms build  # or bms --follow-deps build
```

### Configuration Options (bmsrc)
```ini
[forest]
# Forest detection
use_forest = true          # Force forest mode
forest_xml = /path/to/Forest.xml

# Dependency handling
follow_deps = true         # Follow local dependencies

# Error handling
on_error = best_effort     # stop | best_effort | ignore

# Versioning
use_forest_version = false # Use Forest.xml version for all components
allow_components_versioned_at_forest_level = true

# Performance
parallel = cpu_count * 1.2 # Parallel component processing

# Path simplification
prefix = root              # For components like root::Toto, avoid root/Toto paths
```

### Examples

**Simple Components Listing**:
```xml
<!-- Forest.xml -->
<components>
    <component name="foo" />
    <component name="bar" />
</components>

<!-- foo's Description.xml -->
<dependency type="internal" name="bar" />
<!-- BMS uses local bar from forest, not repository -->
```

**With Constraints**:
```xml
<!-- Forest.xml -->
<constraints>
    <component name="mdw::Pack" version="1-8-0-0" />
</constraints>

<!-- Component's Description.xml -->
<versioner name="mdw::Pack" />
<!-- BMS uses mdw::Pack 1-8-0-0 from forest constraint -->
```

**Auto-discovery**:
```xml
<!-- Forest.xml -->
<components>
    <component name="foo" />  <!-- Only ROOT listed -->
</components>

<!-- foo's Description.xml -->
<dependency type="internal" name="bom::base" version="local"/>
<!-- bom::base auto-discovered, doesn't need Forest.xml listing -->
```

---

## Common Commands

```bash
# Build entire forest
bms build

# Build with parallel processing
bms build  # Uses [forest] parallel from config

# Deliver entire forest
bms deliver

# Check dependencies across forest
bms deps --follow-deps

# Force operation at forest level (even in component dir)
bms --use-forest <command>

# Disable forest (even with Forest.xml present)
bms --no-forest <command>

# Set forest version override
bms --forest-version=2-0-0-0 deliver
```

---

## Key Constraints

- **No Forest-of-Forests** - Nested forests are not supported
- **Delivery Requirement** - All components must have explicit versions at delivery time; `version="local"` is replaced
- **Binary Compatibility** - Component versioning rules still apply within the forest
- **Auto-detection** - Forest.xml searched upward in directory tree from current location
- **Frozen Components** - Components in constraints (not in components list) are read-only from BMS repository
