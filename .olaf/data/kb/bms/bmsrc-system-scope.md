# BMS System Scope Configuration

## Summary
The BMS "system" scope is a configuration layer introduced in early 2024 to handle system-specific settings that differ across development environments (devservers, DevBox containers, CI systems). This scope sits at the lowest priority in the configuration hierarchy, allowing system administrators to define environment-specific defaults without interfering with user, forest, or description-level configurations. It addresses the need for system-dependent settings like replication directories and cache paths that should not be duplicated across project-specific files.

> **Use Case**: When the same project needs different system configurations (e.g., `/remote/tmp/my_replication_dir` on devservers vs `/data/mwrep/res` on DevBox containers), the system scope provides a centralized location for these settings.

---

## Key Concepts

- **Configuration Hierarchy** (lowest to highest priority):
  1. System scope (lowest) - system-wide defaults
  2. User scope (`~/.bmsrc`) - user preferences
  3. Forest scope - forest-specific settings
  4. Description scope (highest) - project-specific overrides

- **System-Specific Settings** - Settings that vary by environment type (devservers, DevBox, CI):
  - `replicate.replication_dir` - Where replication data is stored
  - `replicate.shared` - Shared replication configuration
  - `replicate.use_ssh` - SSH usage for replication
  - `ccache.cache_dir` - Compiler cache directory
  - `ccache.default_max_size` - Cache size limits
  - `ccache.permissions` - Cache file permissions

- **Devserver Owners File** - `/etc/bms/bmsrc.d/50-bmsrc-owners.bmsrc`
  - Location for devserver-specific settings on legacy OBE servers (SLES12 VMs)
  - Write permissions granted on request to devserver owners
  - Prevents inappropriate Forest-level configuration pollution

- **Responsibility** - Only system-specific settings should go in this scope, not project or user preferences

---

## Usage

### Configuration File Location
```bash
# System scope configuration location (legacy OBE servers)
/etc/bms/bmsrc.d/50-bmsrc-owners.bmsrc
```

### Common System-Specific Settings
```ini
# Example system scope configuration for devservers
[replicate]
replication_dir = /remote/tmp/my_replication_dir
shared = true
use_ssh = false

[ccache]
cache_dir = /remote/ccache
default_max_size = 50G
permissions = 0755
```

### Requesting Access
To obtain write permissions for the system scope file on your devserver:

1. Submit a request via **R&D Support Portal**
2. Provide:
   - List of devservers (hostnames)
   - List of UNIX usernames (not email addresses or full names)
3. Request will be validated against YAC devserver ownership records

---

## Best Practices

- **Migration**: Move devserver-specific settings from Forest bmsrc to system scope
- **Scope Appropriateness**: Verify settings are truly system-dependent, not project-specific
- **Environment Awareness**: Different systems require different paths:
  - Devservers (…rndobe…): `/remote/tmp/*`
  - DevBox containers: `/data/mwrep/*`
  - CI workflows: `/remote/tmp/weekly/*`

---

## Related Topics
- BMS Configuration Hierarchy
- Forest Configuration
- Replication Settings
- CCache Configuration
