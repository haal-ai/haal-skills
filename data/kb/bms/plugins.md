# BMS Plugins Reference

## Summary
BMS (Build Management System) plugins are modular extensions that provide specific functionality for building, testing, delivering, and managing C/C++ components at Amadeus. Each plugin focuses on a particular aspect of the development workflow, from compilation and dependency management to static analysis and deployment. Plugins can be invoked directly via `bms <plugin-name>` or configured to run automatically during key workflows like delivery. Understanding plugins is essential for effectively using BMS in component development, testing, and release processes.

---

## Key Concepts

- **Plugin Architecture** - BMS uses a plugin-based system where each plugin is a self-contained module providing specific functionality
- **Delivery Plugins** - Special plugins that run during `bms deliver` to ensure components are production-ready (configured via `[deliver] plugins` in bmsrc)
- **Test Sub-Plugins** - Plugins invoked by the `test` plugin to run different types of tests (unittest, valgrind, cppcheck, etc.)
- **Configuration Profiles** - Plugins respect profiles (dev, rel) which control build variants and test execution (e.g., `bms -p rel test`)
- **Component vs UnitTestPack** - Most plugins can target either the main componentPack or the unitTestPack component using `-c` or `-t` flags
- **Plugin Chaining** - Multiple plugins work together in sequences (e.g., `deps` → `build` → `test` → `deliver`)
- **Automatic Invocation** - Some plugins run automatically (e.g., `replicate` during build, `scm` during deliver)

---

## Plugin Categories

### Core Build & Compilation
- `build` - Compile components with profiles
- `clean` - Remove build artifacts
- `deps` - Manage dependencies

### Testing & Quality
- `test` - Orchestrate test execution
- `unittest`, `valgrind`, `callgrind` - Test sub-plugins
- `cppcheck`, `codedupe`, `fortify` - Static analysis
- `gcov` - Code coverage

### Delivery & Release
- `deliver` - Production release workflow
- `scm` - Source control integration
- `bump` - Version management
- `ar_promote`, `ar_deprecate` - Artifactory operations

### Utilities
- `run` - Execute binaries
- `replicate` - Cache components locally
- `env`, `showconfig` - Environment inspection

---

## Individual Plugin Reference

Below are detailed summaries and usage examples for each BMS plugin.

---

## abidiff

### Plugin Summary
Checks binary compatibility between library versions using libabigail's abidiff tool. Detects ABI changes that could break binary compatibility.

### Usage
```bash
# Build component first
bms build

# Run abidiff test
bms test -t abidiff
# or directly
bms abidiff
```

---

## applicative

### Plugin Summary
**EXPERIMENTAL** - Manages applicative packs for BMS components. Creates hard links and tarballs for application deployment.

### Usage
```bash
# Display pack information
bms applicative --info

# Update applicative pack
bms applicative --update

# Create tarball
bms applicative --create-tarball
```

---

## ar_deprecate

### Plugin Summary
Deprecates BMS components in Artifactory. Can mark components as BLACKLISTED to prevent production usage.

### Usage
```bash
# Deprecate current component
bms ar_deprecate

# Deprecate with message
bms ar_deprecate -m "Deprecated due to security issue"

# Undeprecate
bms ar_deprecate --undeprecate
```

---

## ar_promote

### Plugin Summary
Promotes BMS components from one Artifactory repository to another (e.g., from staging to bms-production).

### Usage
```bash
# Promote to production (default)
bms ar_promote

# Promote to specific target
bms ar_promote -t bms-production -s bms-staging
```

---

## build

### Plugin Summary
Core plugin for compiling BMS components. Abstracts underlying build system (Makefiles) and handles parallel compilation, profiles, and dependencies.

### Usage
```bash
# Build with default dev profile (debug, multithread, shared, 64-bit)
bms build

# Build in release mode
bms -p rel build

# Build all profiles (like delivery does)
bms build -A
```

---

## clean

### Plugin Summary
Removes files produced by BMS: compilation results, test logs, and temporary files. Handles both symlinks and files in /gctmp.

### Usage
```bash
# Clean everything
bms clean

# Clean only componentPack
bms clean -c

# Clean only unitTestPack
bms clean -t

# Clean specific plugins
bms clean -p build -p test
```

---

## deliver

### Plugin Summary
Orchestrates the complete delivery process: validates code, builds in debug and release, runs tests, publishes to repository. Ensures components are production-ready.

### Usage
```bash
# Deliver component (runs all checks, builds, tests)
bms deliver

# Deliver specific component in forest
bms deliver --comp mycomp

# Customize delivery plugins in bmsrc
[deliver]
plugins = deps build test scm deliver
```

---

## deps

### Plugin Summary
Displays and verifies component dependency graph. Shows internal (private), external (public), and indirect dependencies. Essential for understanding component relationships.

### Usage
```bash
# Show all dependencies
bms deps

# Find path to specific dependency
bms deps --path-to osp::Boost 1-39-0-1

# Verify dependency graph
bms deps --check
```

---

## replicate

### Plugin Summary
Copies remote delivered components to local replication directory for faster access. Handles HTTP downloads from Artifactory and lazy artifact replication.

### Usage
```bash
# Replicate dependencies (usually automatic)
bms replicate

# Force re-replication
bms replicate --force

# Check replication status
bms replicate --check
```

---

## run

### Plugin Summary
Simple way to execute binary from componentPack. Sets up LD_LIBRARY_PATH and environment. Alternative to `bms test` for non-test binaries.

### Usage
```bash
# Run binary in current Description
bms run

# Run binary with options
bms run --options "--flag1 --flag2=value"

# Run specific component
bms run --comp my::comp 1-0-0-0
```

---

## scm

### Plugin Summary
Manages Source Control Management integration. Checks code is committed, prevents duplicate tags, tags code at delivery. Supports Git, Mercurial, CVS.

### Usage
```bash
# Show SCM info
bms scm

# Create/update ignore file (.gitignore)
bms scm --ignore

# Used automatically during delivery
bms deliver
```

---

## test

### Plugin Summary
Runs test sub-plugins (unittest, valgrind, callgrind, cppcheck, etc.). Delegates to specialized test tools, logs output per sub-plugin.

### Usage
```bash
# Run default tests (dev profile: unittest)
bms test

# Run release tests (rel profile: unittest + valgrind)
bms -p rel test

# Run specific test sub-plugin
bms test -t valgrind
```

---

## unittest

### Plugin Summary
Most basic test sub-plugin. Directly runs test executable without instrumentation. Default test for dev profile.

### Usage
```bash
# Run via test plugin
bms test

# With output display
bms test --display-output
```

---

## valgrind

### Plugin Summary
Runs test executable through Valgrind's memory checker (Memcheck). Detects memory leaks, invalid access, uninitialized values. Default for rel profile.

### Usage
```bash
# Run via test plugin in release mode
bms -p rel test

# Direct invocation
bms test -t valgrind

# Custom suppressions in Description.xml
<suppressions>
    <plugin name="valgrind" files="valgrind.suppr"/>
</suppressions>
```

---

## bump

### Plugin Summary
Intelligently increases component version based on binary compatibility checks. Uses abidiff to determine if change is patch (4th digit) or minor (3rd digit). Propagates version changes to clients.

### Usage
```bash
# Build first, then bump
bms build
bms bump

# Bump specific component
bms bump --comp mycomp

# Force version (skip compatibility check)
bms bump --force-version 1-0-1-0
```

---

## More Plugin Summaries

### ccache
Speeds up recompilation by caching previous compilations. Transparent build acceleration.

### callgrind  
Profiles test executable using Valgrind's Callgrind tool. Generates performance data for optimization.

### changelog_plugin
Generates changelogs from SCM commit messages between versions.

### clients
Finds and displays which components depend on current component. Used by bump plugin.

### cmakelists
Generates CMakeLists.txt files for CMake-based builds (alternative to Makefiles).

### codedupe
Detects code duplication using PMD's Copy Paste Detector (CPD).

### cppcheck
Static analysis tool for C/C++ code. Detects bugs, undefined behavior, dangerous constructs.

### customtest
Runs custom test scripts defined in Description.xml. Flexible test framework.

### ddd
Runs test executable under DDD (Data Display Debugger) for visual debugging.

### dependency_updator
Updates dependency versions in Forest.xml to latest compatible versions.

### doc
Generates documentation from source code (Doxygen integration).

### env
Displays and manages BMS environment variables.

### fortify
Static security analysis using Fortify SCA. Detects security vulnerabilities.

### gcov
Code coverage analysis using GCC's gcov tool.

### gdb
Runs test executable under GDB debugger for interactive debugging.

### gdbserver
Runs test executable under gdbserver for remote debugging.

### generate-bazel-files
Generates Bazel BUILD files from Description.xml for Bazel build system.

### graphml
Generates GraphML visualization of component dependencies.

### pack_deps
Analyzes and visualizes pack-level dependencies.

### pack_finder
Finds which pack provides a specific component.

### prepare_cmk
Prepares CMake build configuration.

### prepare_release
Prepares components for release (version checks, changelog generation).

### python
Support for Python components and tests.

### sbmunittest
Legacy Amadeus-specific unit test framework.

### showconfig
Displays current BMS configuration settings and their sources.

### sonar_configure
Configures SonarQube integration for code quality analysis.

### sqlite_cache
Caches build and test data in SQLite for performance.

### versioner
Manages version numbers and version file generation.

### writeyourown
Template and guide for creating custom BMS plugins.

---
