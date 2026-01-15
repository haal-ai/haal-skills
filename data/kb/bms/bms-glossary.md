# BMS Glossary

## Summary
Core terminology and concepts used throughout the BMS (Build Management System) ecosystem. This glossary defines component relationships, dependency types, and key architectural patterns. Essential reference for understanding BMS documentation, Description.xml files, and dependency management workflows.

> **When to use:** Reference this when encountering BMS-specific terminology in documentation, error messages, or when working with component dependencies and Forest configurations.

---

## Key Concepts

### Component Architecture
- **Component** - A library or binary in BMS (note: historically confused with "Description" in older docs)
- **Description/Description directory** - Directory tree containing Description.xml at top level; can contain 1-2 components: `<componentPack>` (required) and optionally `<unitTestPack>`
- **Description.xml** - XML file defining component name, version, dependencies, and source code; primary BMS input file

### Dependency Types by Exposure
- **External dependency** - Dependency exposed in component's public API (e.g., public header includes file from D); transitively affects all dependents
- **Internal dependency** - Dependency NOT exposed in public API; isolated to component implementation
- **Direct dependency** - Component A includes a file from component D directly
- **Indirect dependency** - Component A depends on D through another dependency, but doesn't directly include D's files

### Dependency Types by Source
- **Delivered dependency** - Dependency on a delivered version (default convention)
- **Local dependency** - Dependency on non-delivered version; must be explicitly specified

### Graph Terminology
- **Dependency graph** - Complete dependency hierarchy for a component
- **ROOT component** - No other component depends on it (top of graph)
- **LEAF component** - Has no dependencies on other components (bottom of graph)
- **Note:** A component can be both ROOT and LEAF simultaneously (standalone component)

### Other Key Terms
- **Binary compatibility** - Two component versions are binary compatible if dependents can upgrade without code changes or recompilation
- **Time to market** - Duration to design, code, test, and activate new features/bugfixes in production

---

## Usage

### Understanding Component Relationships
When analyzing BMS components, identify:
1. **Direct vs Indirect** - Which headers are directly included?
2. **External vs Internal** - Are dependencies exposed in public API?
3. **ROOT vs LEAF** - Position in dependency hierarchy?

```bash
# Example: Viewing component dependencies
A -> B -> C
 \-> D -> E

# Analysis:
# - A is ROOT (nothing depends on it)
# - C and E are LEAF (no dependencies)
# - B and D are intermediate nodes
# - If A's public header includes B, then B is external dependency
```

### Common Scenarios

**External Dependency Example:**
```cpp
// In component A's public header (A/public/api.h)
#include <D/public/types.h>  // D is now external dependency

// Any component depending on A will also depend on D
```

**Internal Dependency Example:**
```cpp
// In component A's private source (A/src/impl.cpp)
#include <D/public/util.h>   // D is internal dependency

// Components depending on A don't need D
```

### Important Notes

1. **Naming Confusion:** "Description" and "component" were historically mixed up in BMS nomenclature. For delivered components, they effectively mean the same thing (only componentPack survives).

2. **Default Convention:** All dependencies are delivered dependencies unless explicitly marked as local.

3. **Version Reference:** This glossary corresponds to BMS 2.5.4.492 documentation.

---

## Related Documentation
- Description.xml specification: See BMS documentation section
- Local Components: Reference `<localcomponents>` configuration
- Forest configuration: For managing dependency graphs
