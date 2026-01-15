# Built-in BMS Configuration (bmsrc)

## Summary
The `bmsrc` file is BMS's main configuration file that defines default options and behavior for all users. It controls plugins, repositories, build settings, testing, delivery, and various tool integrations. Users can override these defaults in their own `~/.bmsrc` or component-level `.bms/bmsrc` files. This is a comprehensive configuration template documenting every possible BMS option.

> This file serves as both the default configuration and complete documentation for all BMS settings, located at `/etc/bms/bmsrc` (new) or `…/bmslib/data/bmsrc` (legacy).

---

## Key Concepts
- **Hierarchical Configuration**: Built-in defaults < user `~/.bmsrc` < component `.bms/bmsrc`
- **Plugin Architecture**: BMS functionality divided into plugins (build, deps, test, deliver, clean, replicate, applicative)
- **Profiles**: Named setting groups (dev, rel, devpartial, etc.) invoked with `-p` flag
- **Repository Management**: Supports local, remote (NAS), and Artifactory repositories
- **Section-Based Structure**: Settings organized by plugin/feature (`[bms]`, `[build]`, `[test]`, etc.)
- **Variable Substitution**: Supports placeholders like `%u` (user), `%t` (tmpdir), `%c` (component), `%v` (version)

---

## Core Sections

### [bms] - General Settings
**Key options:**
- `plugins`: Default enabled plugins (build, deps, test, deliver, clean, replicate, applicative)
- `repositories`: List of artifact repositories (e.g., `ar://bms-release-public`)
- `local_tempfiles`: Generate temporary files locally (default: true)
- `tempdir`: Temporary folder location (default: `%t`)
- `profile`: Default profile to use (default: dev)
- `config`: Default BMS config to use
- `database_host`/`database_port`: Statistics database location
- `toolchain_path`: Toolchain location (default: `/opt/1A/toolchain`)

**Important flags:**
- `traceback`: Show Python stack traces on errors (default: false)
- `error_deprecate`: Treat deprecated components as errors (default: false)
- `stats_sample_rate`: Statistics push rate 0.0-1.0 (default: 1)
- `translate_nas_repositories`: Translate filesystem paths to Artifactory queries (default: false)

### [graph] - Dependency Graph
- `store_dependency_graph`: Cache dependency graph (default: false)
- `dependency_graph_folder`: Graph cache location (default: `/gctmp/%u/bms_graph`)

### [build] - Build System
**Build system:**
- `system`: Build system choice - makefile or scons (default: makefile)
- `silent`: Short compilation lines (default: true)
- `parallel`: Parallel compilation jobs (default: 5)
- `color`: Colored output (default: 1)
- `distribute`: Distributed build (default: false)

**Build profiles:**
- `debug`: Debug mode 0/1 (default: 1)
- `shared`: Shared/static libraries (default: 1)
- `arch`: Architecture 32/64 (default: 64)
- `compiler`: General compiler cxx/c (default: cxx)
- `compiler_c`: C sources compiler (default: cxx)
- `threads`: Multithread support (default: 1)

**Advanced:**
- `compilation_database_directory`: JSON compilation database path (default: `%d | .`)
- `headers`: Build headers standalone 0/1/both (default: 0)
- `dependencies`: Include deps headers in compilation database (default: 0)

### [test] - Testing
- `plugins`: Test plugins to run (default: unittest)
- `env_script`: Shell script sourced before test execution
- `pre_script`/`post_script`: Scripts before/after test execution
- `pre_post_once`: Run pre/post scripts once vs per test binary (default: false)
- `clean_log`: Clean logs before execution (default: false)
- `display_output`: Direct test output to stdout (default: false)

**Sub-plugins:**
- `[unittest]`: Basic unit test execution
- `[valgrind]`: Memory leak detection with options
- `[callgrind]`: Performance profiling with thresholds
- `[customtest]`: Custom test script execution

### [deliver] - Delivery
- `plugins`: Delivery-time plugins (default: deps, build, test, scm)
- `profiles`: Profiles to use (default: dev, rel)
- `repository`: Target BMS repository path
- `user`: Repository access user
- `excludes`: Patterns to exclude (default: CVS, .1DE, .hg)
- `force_tag`: Move existing tags (default: false)
- `patch_version_threshold`: High 4th digit threshold for patch versions (default: 1000)
- `push_tag`: Push tag to SCM (default: False)
- `dry_run`: Dry run mode (default: False)
- `exceptional_nas_delivery`: Allow NAS delivery (default: false, deprecated)

### [deps] - Dependency Management
- `check_missing_propagated_deps`: Check external dependency chains (default: true)
- `error_on_unneeded_dependencies`: Treat unneeded deps as errors (default: false)
- `error_on_circular_dependencies`: Treat circular deps as errors (default: true)
- `error_on_interface_implementation`: Check interface alignment (default: false)
- `raise_if_unittest_upgrade`: Error if unittest dep version differs from main (default: false)

### [replicate] - Replication
**Mode and behavior:**
- `mode`: auto/manual/off (default: auto)
- `replication_server`: Use external replication server (default: false)
- `replication_timeout`: Max wait time in seconds (default: 300.0)
- `replication_dir`: Replication directory (default: system-dependent)
- `parallel`: Parallel replication jobs (default: 10)

**Access control:**
- `user`: Replication user account (default: system-dependent)
- `ssh_key`: Private SSH key path (default: system-dependent)
- `use_ssh`: Enable SSH for replication (default: true)
- `shared`: World-writable replicated files (default: false)

**Repository management:**
- `repositories_sort`: keep_user_order/force_nas_first/force_artifactory_first (default: keep_user_order)
- `replicate_ar_artifacts_only`: Only replicate Artifactory artifacts (default: false)
- `trusted_replica`: Trust replication dir without remote checks (default: false)
- `exhaustive`: Replicate for offline work (default: false)

### [scm] - Source Control
- `system`: SCM type - cvs/hg/git/guess (default: guess)
- `tag`: Component tag format (default: `%c_DELIVERY_%v`)
- `tag_forest`: Forest tag format (default: `DELIVERY_FOREST_%f`)
- `retry_number`: SCM command retries (default: 10)
- `retry_interval`: Retry interval seconds (default: 30)
- `types`: Tagging types - component/forest (default: component)

### [ccache] - Compiler Cache
- `mode`: on/off
- `cache_dir`: Cache directory (default: `/mwrep/ccache`)
- `display_build_statistics`: Show ccache stats (default: false)
- `log_stats_in_json_file`: JSON statistics log (default: false)

### [ar] - Artifactory Repository
- `system`: Repository system (default: artifactory)
- `server`: Artifactory URL (default: `https://repository.rnd.amadeus.net`)
- `searchlogin`/`searchpass`: Search API credentials
- `default_delivery_repository`: Default delivery target
- `retries`: Retry count on errors (default: 3)

---

## Profiles

### Built-in Profiles
BMS profiles group related settings for different build scenarios, invoked via `bms -p <profile>`:

**Development profiles:**
- `profile_dev`: Debug build with unittest (default)
- `profile_devg4`: Dev with GCC 4.3.2
- `profile_devpartial`: Debug partial build

**Release profiles:**
- `profile_rel`: Release build with unittest, valgrind, abidiff
- `profile_relg4`: Release with GCC 4.3.2
- `profile_relpartial`: Release partial build

**Profile syntax:**
```ini
[profile_name]
plugin_name.setting = value
```

### Common Profile Patterns
```bash
# Use development profile (debug build)
bms -p dev build

# Use release profile (optimized + full testing)
bms -p rel deliver

# Custom profile in user bmsrc
[profile_myprofile]
build.debug = 1
build.parallel = 10
test.plugins = unittest, customtest
```

---

## Usage

### Configuration Hierarchy
BMS loads configuration in order (later overrides earlier):
1. Built-in `/etc/bms/bmsrc`
2. User `~/.bmsrc`
3. Component `.bms/bmsrc`

### Include Directive
```ini
[bms]
# Include settings from another file
include_conf = /path/to/other/bmsrc
# Relative paths are relative to current bmsrc
include_conf = ../shared-config.bmsrc
```

### Common Customizations

**User-level customization (`~/.bmsrc`):**
```ini
[bms]
profile = dev

[build]
parallel = 16
silent = false
compilation_database_directory = %d | .

[replicate]
mode = auto
replication_dir = /my/local/cache
```

**Component-level customization (`.bms/bmsrc`):**
```ini
[build]
# Component needs special compiler flags
compiler = c

[test]
# Custom test environment setup
env_script = setup_test_db.sh
pre_script = populate_data.py
post_script = cleanup.sh
```

### Variable Substitutions
- `%u`: Current user
- `%t`: Temporary directory (TMPDIR)
- `%c`: Component name
- `%v`: Component version
- `%p`: Profile name
- `%d`: BMS default path
- `%f`: Forest name
- `%h`: Hostname

### Critical Settings for Performance
```ini
[build]
parallel = 10                    # Adjust to CPU cores
distribute = true                # Enable distributed build if available

[ccache]
mode = on                        # Enable compiler cache
cache_dir = /fast/local/ccache   # Use fast local storage

[replicate]
mode = auto                      # Auto-replicate dependencies
trusted_replica = true           # Skip remote checks if no patches
repositories_sort = keep_user_order  # Respect repository priority
```

### Artifactory-First Configuration
Modern recommended setup prioritizing Artifactory over NAS:
```ini
[bms]
repositories = ar://bms-release-public

[replicate]
repositories_sort = keep_user_order  # Don't reorder repositories
replicate_ar_artifacts_only = false  # Replicate everything
```

---

## Important Notes
- **Dangerous options clearly marked**: Many settings include warnings not to change unless you know what you're doing
- **BMS 1.x compatibility**: Some settings exist for backward compatibility (e.g., `break_binary_compatibility_for_bms_1`)
- **NAS deprecation**: On-premise NAS delivery being phased out, will error after 31/05/2025
- **Azure considerations**: Special settings for Azure devbox environments (NAS performance warnings)
- **Patch versions**: 4th digit ≥1000 indicates patch/hotfix versions excluded from normal compatibility searches
- **Symbolic link options**: `symbolic_functions_link` improves library loading performance (default: true)
