# BMS Algorithms

## Summary
BMS uses graph-based algorithms to manage component dependencies and resolve version conflicts. The system constructs a directed acyclic graph (DAG) by recursively reading `Description.xml` files to discover dependencies. Key functionality includes distinguishing between internal and external dependencies, automatic version resolution for binary-compatible versions, and handling of dependency conflicts.

> This section is critical when troubleshooting dependency issues, understanding how BMS selects component versions, or resolving binary incompatibility errors.

---

## Key Concepts

- **Dependency Graph**: A directed acyclic graph (DAG) where nodes are components (name + version) and edges represent "depends on" relationships
- **Edge Data**: Metadata on graph edges indicating whether dependency is internal/external and linkage mode (linked/aggregated)
- **External Dependency**: A dependency whose public API is transitively exposed through the component's public API (e.g., component A's public headers include component B's public headers)
- **Internal Dependency**: Any dependency that is not external (used internally but not exposed in public API)
- **Binary Compatibility**: Versions differing only in the 4th number are considered binary compatible
- **Version Resolution**: BMS automatically selects the highest binary-compatible version when multiple versions exist

---

## Dependency Graph Construction

BMS builds the dependency graph through a recursive process:

1. Reads the component's `Description.xml` file
2. Discovers dependencies listed in the file
3. Uses `[bms] repositories` to locate each dependency
4. Reads each dependency's `Description.xml` recursively
5. Continues until all transitive dependencies are discovered

Each node in the graph contains:
- Component name
- Component version

Each edge contains:
- Dependency type (internal/external)
- Link mode (linked/aggregated)

---

## Version Selection Algorithm

When BMS encounters multiple versions of the same component (e.g., `mdw::Toolbox`):

```
1. Collect all versions encountered in the dependency graph
2. Check if all versions are binary compatible (differ only in 4th number)
3. If binary compatible:
   - Select the highest version
   - Discard other versions
4. If NOT binary compatible:
   - Raise error (cannot auto-resolve)
   - Developer must manually choose the version
```

**Example Scenarios**:
- `1.2.3.4` and `1.2.3.5` → BMS selects `1.2.3.5` (binary compatible)
- `1.2.3.4` and `1.2.4.0` → BMS raises error (binary incompatible)

---

## Internal vs External Dependencies

**External Dependency Criteria**:
- Component A depends on component B
- **AND** A's public headers include B's public headers
- Result: B is an external dependency of A

**Internal Dependency**:
- All other dependencies that don't meet external criteria
- Used by component but not exposed in public API

This distinction affects:
- Transitive dependency resolution
- Build system linking behavior
- Component visibility in downstream projects

---

## Related Concepts

- **Forest Mode**: See [Forest](forest.md) documentation for differences between forest and no-forest modes
- **Aggregated Components**: See advanced documentation for link mode details
- **Versioners**: Pluggable versioning system - see [Versioner plugin](versioner.md) documentation

---

## Common Issues

**Binary Incompatibility Error**:
```
Error: Multiple incompatible versions of component found
  mdw::Toolbox: 1.2.3.0, 1.3.0.0
Action: Manually specify version in Description.xml
```

**Resolution**: Developer must update `Description.xml` to explicitly specify which version to use, ensuring all dependents use compatible versions.
