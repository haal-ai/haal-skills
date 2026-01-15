# BMS Configuration

## Summary
BMS (Build Management System) uses cascaded configuration files (bmsrc files) to control build behavior, avoiding repetitive command-line options. Configuration files are read in a specific order where later files override earlier settings. This system supports team-wide configuration management, user-specific settings, and component-specific configurations through a hierarchical structure.

> **Use Case:** Essential for setting up BMS repositories, build profiles, parallel compilation, and environment-specific behaviors without repeatedly specifying command-line flags.

---

## Key Concepts

- **Cascaded Configuration**: BMS reads multiple bmsrc files in sequence (built-in → site → system → user → forest → component → command-line)
- **Profiles**: Named configuration sets (e.g., `dev`, `rel`, `devg4`, `relg4`) for different build scenarios
- **Configuration Scopes**: System-level (`/etc/bms/bmsrc.d/`), user-level (`~/.bmsrc`), forest-level, component-level
- **Include Directive**: `include_conf` allows reusing configuration files (local paths or URLs)
- **Override Operators**: `=` (set), `+=` (append), `=+` (prepend), `-=` (remove), `delete` (unset)
- **Repository Types**: Local filesystem paths and remote Artifactory repositories (`ar://repo-id` or `https://...`)

---

## Configuration File Loading Order

BMS reads configuration files in this strict sequence (skipping non-existent files):

1. **Built-in bmsrc** - Default BMS settings (part of distribution)
2. **Site bmsrc** - `~app-bms-admin/bms-shared/site.bmsrc`
3. **System bmsrc** - `/etc/bms/bmsrc.d/*.bmsrc` (sorted alphabetically)
4. **User bmsrc** - `$HOME/.bmsrc`
5. **Forest bmsrc** - `FOREST_ROOT/.bms/bmsrc` (if in Forest mode)
6. **Component bmsrc** - `DESCRIPTION_ROOT/.bms/bmsrc` and `DESCRIPTION_ROOT/bmsrc`
7. **Command-line override** - Files specified with `--bmsrc-cascade`

**Note:** Files specified via `include_conf` are processed before the file containing them, regardless of where the directive appears.

---

## Configuration File Syntax

```bash
# Comments start with '#'

# Include other configuration files (processed first, regardless of position)
include_conf = /path/to/other.bmsrc

# Global BMS options section
[bms]
repositories = /projects/repo1, /projects/repo2, ar://bms-release-public
profile = dev

# Plugin-specific section
[build]
parallel = 3
debug = 1
color = 1

# Profile section (named configuration sets)
[profile_dev]
bms.local_tempfiles = 1
build.debug = 1
build.parallel = 3
test.plugins = unittest

# Another profile
[profile_rel]
build.debug = 0
test.plugins = unittest, valgrind
```

### Syntax Rules

- **Assignments**: Use `=` operator (no quotes needed for strings)
- **Booleans**: `0` = false, `1` = true
- **Lists**: Comma-separated values (leading whitespace trimmed)
- **Durations**: `<number> <unit>` (e.g., `1 hour`, `42 days`, `53 years`)
- **Append/Prepend**: `+=` appends, `=+` prepends (commas auto-added for lists)
- **Delete**: `delete variable_name` removes a setting

---

## Essential Global Options

### User-Friendly Options

**repositories**
```bash
[bms]
repositories = ar://bms-release-public, /projects/mwdeldev, /projects/delivery
```
- **Required**: List of BMS repositories to search for dependencies
- **Recommendation**: Place `ar://bms-release-public` first
- Supports local paths and Artifactory URLs

**repositories_sort**
```bash
[bms]
repositories_sort = keep_user_order
```
- Controls repository search order
- Values: `keep_user_order` (recommended), `force_nas_first`, `force_artifactory_first`
- Legacy behavior reordered repositories; new behavior respects list order

**profile**
```bash
[bms]
profile = dev
```
- Default configuration profile to use
- Avoids needing `-p profile_name` on command line
- Default: `dev`

**local_tempfiles**
```bash
[bms]
local_tempfiles = 1
```
- Places temporary files (`.o`, `.so`, logs) in local filesystem (`/gctmp`) instead of NAS
- Default: `1` (enabled for speed/disk space)

**tempdir**
```bash
[bms]
tempdir = /custom/tmp/%u
```
- Custom temporary directory (requires `local_tempfiles = 1`)
- `%u` = username, `%t` = TMPDIR

**config**
```bash
[bms]
config = ora
```
- Default BMS config/flavor to use for components

**plugins**
```bash
[bms]
plugins = build, deps, test, deliver, clean, replicate
```
- List of active BMS plugins
- Default: build, deps, test, deliver, clean, replicate

**include_conf**
```bash
[bms]
include_conf = /team/shared.bmsrc, https://bitbucket.example.com/my.bmsrc
```
- Include other bmsrc files (local or URL)
- Supports http/https with authentication (`.netrc`, environment variables)
- Recursive/nested includes supported
- **Always processed before current file settings**

**validate_remote_config_tls**
```bash
[bms]
validate_remote_config_tls = true
```
- Verify TLS certificates when including remote bmsrc files
- Default: `true`

**translate_nas_repositories**
```bash
[bms]
translate_nas_repositories = true
```
- Auto-translate NAS repositories to Artifactory-friendly syntax
- Adds `ar://bms-nas` to repository list
- Enables remote/cloud access to NAS components via nas-ar-adapter

**fail_on_nonazure_nas_cache**
```bash
[bms]
fail_on_nonazure_nas_cache = false
```
- Fail if cache repositories (ccache, replication) are on non-Azure NAS
- Relevant for Azure-based build machines
- Default: `false`

---

## Numeric Expressions in Settings

Settings like `[build] parallel` support dynamic expressions:

```bash
[build]
parallel = cpu_count
max_load = cpu_count

[forest]
parallel = 3

[build]
# Avoid OOM: each compile uses ~4GB, 3 forest parallel jobs
parallel = memtotal / (4 * 1024 * 1024) / 3

# Or use minimum of memory-based and CPU-based
parallel = min(memtotal / (4 * 1024 * 1024) / 3, cpu_count)
```

**Available Symbols:**
- `cpu_count` - Number of CPU cores (may be fractional in containers)
- `memtotal` - Total system memory (KB)
- `memavailable` - Available memory for BMS (KB)
- `min(a, b, ...)` - Minimum value function

---

## Profiles (Named Configuration Sets)

Profiles group related settings for different scenarios (dev, release, testing, etc.):

```bash
# Define profile
[profile_dev]
bms.local_tempfiles = 1
bms.config = ora
build.debug = 1
build.parallel = 3
test.plugins = unittest

[profile_rel]
build.debug = 0
build.parallel = 8
test.plugins = unittest, valgrind

# Profile inheritance
[profile_myprofile]
inherits_from = relg4
build.debug = 1
```

**Usage:**
```bash
# Use profile via command line
bms -p dev build

# Or set default in bmsrc
[bms]
profile = dev
```

**Built-in Profiles:**
- `dev` - Debug build with unit tests
- `rel` - Release build with unit tests + valgrind
- `devg4` - Debug build with GCC 4.x
- `relg4` - Release build with GCC 4.x

---

## Configuration Management Best Practices

### Team/Project Configuration

**Recommended Approach:**
- Create team/project-level bmsrc file
- Store in shared location (Bitbucket, shared filesystem)
- Include from component-level or forest-level bmsrc

```bash
# Component's .bms/bmsrc
[bms]
include_conf = https://bitbucket.example.com/myteam/team.bmsrc
```

**Benefits:**
- Single source of truth for team BMS policies
- Consistent behavior across all developers
- Easy updates without modifying individual user configs

### Configuration Scope Recommendations

| Scope | Location | Use For |
|-------|----------|---------|
| System | `/etc/bms/bmsrc.d/` | System-specific settings (replication_dir, ccache) |
| User | `~/.bmsrc` | Personal preferences, user-specific paths |
| Forest | `FOREST_ROOT/.bms/bmsrc` | Forest-wide settings |
| Component | `DESCRIPTION_ROOT/.bms/bmsrc` | Component-specific configurations |

---

## Advanced Options

**blacklisted_repo_components**
```bash
[bms]
blacklisted_repo_components = /repo/path component_name 1-2-3-4
```
- Exclude specific component versions from dependency resolution
- Useful for automated partial pack rebuilds

**cfc_default_version**
```bash
[bms]
cfc_default_version = 2-8-0-705
```
- Default version of `mdw::CFC` if not explicitly declared
- Toolchained packs should provide explicit version

**plugin_path**
```bash
[bms]
plugin_path = /custom/plugins
```
- Additional directories for BMS plugin modules

**error_deprecate**
```bash
[bms]
error_deprecate = 1
```
- Treat deprecated dependency usage as error instead of warning

**rsync_binary**
```bash
[bms]
rsync_binary = /nastools/scs/rsync/3.0.6/bin/rsync
```
- Specify rsync binary for deliver/replicate/doc plugins

**tips**
```bash
[bms]
tips = 0
```
- Disable random BMS tips after commands

**traceback**
```bash
[bms]
traceback = 1
```
- Enable Python stack traces on errors by default

---

## Graph Cache Options

```bash
[graph]
store_dependency_graph = true
dependency_graph_folder = /gctmp/%u/bms_graph
```

**store_dependency_graph**
- Cache dependency graph between BMS calls
- Skips interface/implementation checks on subsequent runs
- **Recommendation**: Enable locally, disable for delivery
- Default: `false`

**dependency_graph_folder**
- Custom location for graph cache
- Default: `/gctmp/%u/bms_graph` (`%u` = username)

---

## Examples

### Minimal User Configuration

```bash
# ~/.bmsrc
[bms]
repositories = ar://bms-release-public
profile = dev
```

### Team Configuration with Remote Include

```bash
# Component .bms/bmsrc
[bms]
include_conf = https://bitbucket.company.com/myteam/shared.bmsrc

# Override team settings for this component
[build]
parallel = 4
```

### Multi-Repository Setup

```bash
[bms]
repositories = ar://bms-release-public, /projects/mwdeldev, /projects/sbmdelde/delivery
repositories_sort = keep_user_order
translate_nas_repositories = true
```

### Profile with Inheritance

```bash
[profile_mydev]
inherits_from = dev
build.parallel = min(cpu_count, 8)
build.cppflags += -DCUSTOM_FLAG
```

### URL Include with Authentication

```bash
[bms]
include_conf = https://bitbucket.example.com/git/projects/MYPROJ/repos/myrepo/raw/my.bmsrc?at=refs/heads/mybranch
```

Authentication methods (in order of precedence):
1. Environment: `BMS_CONFIG_AUTH_LOGIN`, `BMS_CONFIG_AUTH_PASSWORD`
2. `~/.netrc`
3. `~/.git-credentials`
4. Default: bmslocaldevuser account

---

## BMS 1.x Compatibility

Legacy syntax still supported for migration:

```bash
# BMS 1.x style (compatible with both 1.x and 2.x)
bms.options = -R /projects/mwdeldev -R /projects/sbmdelde
```

**Migration Note:** If using both BMS 1.x and 2.x, continue using `bms.options = -R ...` syntax for repositories.

---

## Common Patterns

### Development Setup

```bash
[bms]
repositories = ar://bms-release-public
profile = dev
local_tempfiles = 1

[profile_dev]
build.debug = 1
build.parallel = min(cpu_count, 4)
build.color = 1
test.plugins = unittest
```

### Production/Release Setup

```bash
[bms]
repositories = ar://bms-release-public, ar://bms-production
profile = rel

[profile_rel]
build.debug = 0
build.parallel = min(memtotal / (4 * 1024 * 1024) / 3, cpu_count)
test.plugins = unittest, valgrind
```

### Cloud/Remote Development

```bash
[bms]
repositories = ar://bms-release-public
translate_nas_repositories = true
fail_on_nonazure_nas_cache = true
local_tempfiles = 1
```
