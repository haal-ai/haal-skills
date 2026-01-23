# Unix Concepts for BMS

## Summary
This document covers fundamental Unix concepts essential for understanding BMS's binary compatibility system. It explains the difference between static and shared libraries, how dynamic linking works, and the critical concept of binary compatibility in version management. This knowledge is foundational for BMS users who need to understand library dependencies, version compatibility, and compilation workflows.

> This section is introductory material for fully understanding binary compatibility, one of BMS's key concepts. Most content references the [Program Library HOWTO](http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html).

---

## Key Concepts

### Libraries
- **Object Files (`.o`)**: Compiled source files containing symbols (classes, functions, variables)
- **Static Libraries (`.a`)**: Collection of object files aggregated together
  - Symbols are embedded directly into the final binary at link time
  - No runtime dependency on the library file
  - Less flexible but potentially faster
- **Shared Libraries (`.so`)**: Dynamic libraries loaded at runtime
  - Binaries maintain virtual links to libraries
  - Libraries resolved at execution time by the OS
  - Default delivery method within Amadeus
  - More flexible, enables binary compatibility

### Binary Compatibility
- **Definition**: A program linked to a former library version continues running with newer versions without recompilation
- **Critical for**: Reducing compilation time across large codebases
- **Version Format**: `A-B-C-D` (e.g., `1-2-0-1`)
  - `A` changes: Not compatible, clients need code changes
  - `B` changes: Source compatible only, clients must recompile (new features)
  - `C` changes: Source compatible only, clients must recompile (non-bin-comp changes)
  - `D` changes: **Binary compatible**, no recompilation or relink needed

### Dynamic Linking
- **Name Resolution**: Finding symbols at runtime from loaded libraries
- **LD_LIBRARY_PATH**: Colon-separated list of directories searched for `.so` files
- **SONAME**: Shared object name (3-digit version) used for dynamic linking
- **ldd**: Command to show dynamic library dependencies
- **Forward Compatibility**: Upgrading versions is safe, downgrading is not

---

## Usage

### Creating Static Libraries

```bash
# Compile source to object file
gcc -c a.c

# List symbols in object file
nm a.o

# Create static library from object file
ar rcs liba.a a.o

# Link binary with static library
gcc b.c -L. -la -o mybin
```

### Creating Shared Libraries

```bash
# Create shared library from object file
gcc -shared -o liba.so a.o

# View symbols in shared library
nm liba.so

# Link binary with shared library
gcc b.o -L. -la -o mybin

# Check dynamic library dependencies
ldd mybin
```

### Inspecting Binary Dependencies

```bash
# View SONAME and dependencies
readelf --dynamic liba.so

# List undefined symbols (needs runtime resolution)
nm mybin | grep U

# List defined symbols
nm mybin | grep T
```

---

## Binary Compatibility Rules

### Binary-Compatible Changes (bump D only)
- Adding new functions or classes
- Adding new symbols (functions, classes, global variables)
- Changes to private/implementation code only
- **No changes to public headers**

### Non-Binary-Compatible Changes (bump B or C)
- Changing order of class/struct attributes
- Adding/removing class/struct members
- Adding/removing virtual functions
- Changing function signatures (public/protected)
- Removing public/protected symbols
- Any size changes to public classes/structs

### Warning
⚠️ **Incorrectly marking incompatible changes as binary-compatible is dangerous**
- May cause segmentation faults
- Can lead to silent memory corruption
- Errors may only appear when specific code paths execute
- When in doubt, bump in a non-binary-compatible way

---

## Advanced Topics

### Additional Symbol Resolution Mechanisms
- **LD_PRELOAD**: Override symbols by preloading a library (limited use in Amadeus)
- **dlopen()**: Open arbitrary libraries during execution (used by Job Framework)

### OTF Behavior
- Amadeus OTF resolves all symbols at load time
- Catches obvious errors early
- Some incompatibilities (e.g., class size changes) may not be detected until code execution

---

## Best Practices

1. **When bumping version numbers**: Be certain about binary compatibility
2. **Default rule**: No change to public includes = binary compatible
3. **If clients need to adapt**: Bump in non-binary-compatible way
4. **Forward compatibility**: Always design for upgrades, not downgrades
5. **Ask for help**: When uncertain, consult others or bump conservatively
6. **Symbol versioning**: Use SONAME (3-digit) for dynamic linking to allow patch updates

---

## Related Concepts
- **Source Compatibility**: Code compiles without changes
- **Binary Compatibility**: Code runs without recompilation
- **Functional Compatibility**: Not guaranteed by either above; behavior may differ
- **SONAME**: Shared library naming with 3-digit version enabling transparent patch updates
