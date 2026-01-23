# BMS Tutorial

## Summary
This tutorial provides practical guidance for working with BMS (Build Management System) in daily development workflows. It covers essential command-line operations, component creation, dependency management, and configuration. The tutorial is designed for developers who need to build, test, and deliver BMS components without deep diving into underlying architecture.

> **Core Use Case:**  
> Developers working with BMS-managed projects need to understand three primary commands (`build`, `test`, `deliver`) and how to configure BMS through repositories, profiles, and configuration files (bmsrc).

---

## Key Concepts

### Three Essential Commands
- **`bms build`** - Compiles componentPack and optionally unitTestPack
- **`bms test`** - Runs test executables with various test sub-plugins (unittest, valgrind, callgrind)
- **`bms deliver`** - Publishes components to BMS repositories after verification and testing

### Component Structure
- **componentPack** - The main library/binary component with public API (headers) and private implementation
- **unitTestPack** - Optional test binary component
- **Description.xml** - Single file describing component name, version, dependencies, and structure

### Configuration Hierarchy
BMS reads configuration files (bmsrc) in order of precedence:
1. Built-in defaults
2. Site-wide (`~app-bms-admin/bms-shared/site.bmsrc`)
3. System-level (`/etc/bms/bmsrc.d/*.bmsrc`)
4. User-level (`~/.bmsrc`) - most common for personal settings
5. Forest-level (`FOREST_ROOT/.bms/bmsrc`)
6. Component-level (`DESCRIPTION_ROOT/.bms/bmsrc`)

### Profiles
- Switch configurations on-the-fly (e.g., debug vs release, compiler versions)
- **dev** profile - non-optimized, suitable for development
- **rel** profile - optimized, suitable for production
- Applied via `-p` flag: `bms -p shared_release build`

### BMS Repositories
- Centralized storage locations for delivered components
- Components stored as: `<repository>/<name>/<version>/`
- Example: `/projects/galaxyfaraway/foo/bar/1-0-0-0/`
- Search order: replication_dir → local/NAS repos → Artifactory repos

### Automatic Replication
- BMS automatically replicates dependencies locally to speed up builds
- Unpacks tarballs and copies from remote NAS to local disk
- Triggered automatically by `bms build` or `bms deps`
- Explicit command: `bms replicate`

---

## Usage

### Basic Command Syntax
```bash
# General syntax
bms <global-options> <pluginname> <plugin-options>

# Get help
bms -h                    # Show global options and plugin list
bms <pluginname> --help   # Show plugin-specific help
```

### Building Components
```bash
bms build       # Build componentPack only
bms build -t    # Build unitTestPack (tests)
bms build -b    # Build both componentPack and unitTestPack
bms clean       # Clean all build artifacts

# With profile
bms -p rel build    # Build in release mode
```

**Build Behavior:**
- Generates Makefiles automatically (don't use make directly!)
- Incremental builds - only recompiles changed files
- Regenerates Makefiles when Description.xml changes
- Build artifacts stored in `bmstmp/` (often symlink to `/gctmp/<username>/`)

### Testing Components
```bash
bms test                # Run with default plugins (usually unittest)
bms test -t valgrind    # Run with specific test plugin
bms -p rel test         # Run in release mode (runs unittest + valgrind)
```

**Test Sub-Plugins:**
- **unittest** - Executes test binary, success if return code is 0
- **valgrind** - Memory leak detection
- **callgrind** - Performance profiling

**Test Results:**
- Logs stored in `test/logs/<profile>/<plugin>/`
- Examples: `test/logs/dev/unittest/`, `test/logs/dev/valgrind/`

### Delivering Components
```bash
bms deliver    # Complete delivery workflow
```

**Delivery Process (automated):**
1. Verify componentPack and unitTestPack dependencies
2. Check component not already delivered
3. Verify code committed to SCM (git/hg)
4. Build in both debug and release modes
5. Run tests with dev and rel profiles
6. Tag source code in SCM
7. Copy component to BMS repository via ssh/rsync

**Failure Handling:**
- Atomic delivery - component not "half delivered" if any step fails
- SCM tags not applied if copy fails
- Clear error messages indicate corrective actions

### Dependency Management
```bash
bms deps    # Display and verify dependency graph
```

### Working with Profiles
```bash
# Use specific profile for any command
bms -p <profile_name> build
bms -p <profile_name> test
bms -p <profile_name> deliver

# Common profiles
bms -p dev build      # Non-optimized build
bms -p rel build      # Optimized build
```

---

## Component Organization

### Standard Directory Structure
```
MyComponent/
├── Description.xml         # Component metadata and configuration
├── include/                # Public API (headers)
├── src/                    # Private implementation (headers + cpp)
├── test/
│   └── src/                # Test implementation
└── bmstmp/                 # Build artifacts (often symlink)
```

### Description.xml
Single file containing:
- Component name and version
- Dependency list (name/version pairs)
- Public API specification (include directories)
- Private code specification (src directories)
- Build configuration

### Forest Mode
- Workspace containing multiple components
- Central `Forest.xml` file describes workspace
- BMS commands run at Forest level target all components
- Example: `cd forest_root && bms build` builds all components

---

## Configuration Files (bmsrc)

### Common User Configuration (`~/.bmsrc`)
```ini
# Global BMS options
[bms]
repositories = /projects/mwdeldev, /projects/sbmdelde/delivery
include_conf = /path/to/shared/team-bmsrc  # Include team settings

# Build plugin configuration
[build]
parallel = 3    # Use 3 parallel jobs
color = 1       # Colorize make/gcc output

# Test plugin configuration
[test]
# Plugin-specific settings
```

### Configuration File Include
```ini
[bms]
include_conf = /path/to/other/bmsrc

# Behaves like C #include - loads other file first
# Then applies settings from this file (override)
```

### Override with Command-Line
```bash
# Use specific bmsrc file (disables user/Forest/Description bmsrc)
bms --bmsrc /path/to/custom.bmsrc build

# Chain multiple bmsrc files
bms --bmsrc-cascade file1.bmsrc --bmsrc-cascade file2.bmsrc build
```

---

## Important Notes

### Context Awareness
- BMS detects target component by current working directory
- Must be in directory with `Description.xml` or subdirectory
- Forest mode: run from `Forest.xml` directory to target all components

### Automatic Behavior
- Makefile generation - automatic and transparent
- Dependency replication - automatic on build/deps commands
- Build optimization - incremental compilation by default

### Best Practices
- Never edit generated Makefiles directly - use `bms build`
- Use profiles to switch build configurations
- Leverage Forest mode for multi-component workspaces
- Store team settings in shared bmsrc files via `include_conf`
- Use replication for faster builds from remote repositories

### Common Workflows
```bash
# Daily development cycle
bms build           # Compile changes
bms build -t        # Build tests
bms test            # Run tests
bms deliver         # Publish when ready

# Cross-platform development
bms -p gcc10_dev build       # Build with GCC 10
bms -p clang_release build   # Build with Clang in release

# Troubleshooting
bms deps            # Check dependency issues
bms clean           # Clean and rebuild
bms replicate       # Force dependency replication
```

---

## Related Documentation
- **Unix Concepts** - Previous topic covering UNIX fundamentals for BMS
- **Configuration** - Next topic with detailed bmsrc configuration reference
- **Plugins** - Complete reference for all BMS plugins (build, test, deliver, etc.)
- **Description.xml** - Full specification for component description files
- **Installation Guide** - BMS setup and installation procedures
