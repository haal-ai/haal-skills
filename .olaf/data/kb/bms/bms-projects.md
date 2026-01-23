# BMS inside Specific Projects

## Summary
This documentation covers how to integrate and use BMS (Build Management System) within specific Amadeus projects, particularly the SBM (SBR Model) and SBR department. Understanding project-specific BMS configurations is essential when working with components that need to be BMS 2.0 compliant within these organizational contexts. Both projects follow similar patterns for migrating from BMS 1.x to BMS 2.0, using cascaded configuration files that provide standardized settings across all components while allowing customization when needed.

> This section provides detailed migration procedures and configuration details for making components BMS 2.0 compliant in SBM and SBR projects.

---

## Key Concepts
- **Project-Specific BMS**: BMS integration varies by project/department with custom configurations
- **SBM (SBR Model)**: A specific project requiring BMS 2.0 compliance (NOTE: Obsolete for versions >= 11, now owned by DEV-RDM-PNR-ASE-PIF)
- **SBR Department**: Departmental implementation with own BMS requirements
- **BMS 2.0 Compliance**: Components must meet specific standards to work within these projects
- **Cascaded Configuration**: Uses `include_conf` to reference shared configuration files at project level
- **`.bms/bmsrc` File**: Local component configuration file that includes project-level settings
- **SCM Integration**: Configuration files are version-controlled (CVS, Mercurial)
- **Pre/Post Scripts**: Scripts executed before and after unit tests for environment setup
- **Configuration Profiles**: Separate settings for dev and release modes (test plugins, valgrind, etc.)

---

## Usage

### Making Components BMS 2.0 Compliant - Minimal Procedure

Both SBM and SBR follow a similar minimal procedure:

**For SBM Components:**
```bash
# 1. Create .bms directory in component root
mkdir .bms

# 2. Create .bms/bmsrc with the following content
cat > .bms/bmsrc << EOF
[bms]
include_conf = /projects/sbmdelde/sbm/tools/bms/bmsrc
EOF

# 3. Commit the file
# (use your SCM: CVS, Mercurial, etc.)
```

**For SBR Components:**
```bash
# 1. Create .bms directory in component root
mkdir .bms

# 2. Create .bms/bmsrc with the following content
cat > .bms/bmsrc << EOF
[bms]
include_conf = /projects/sbrdelde/tools/bms/config/bmsrc
EOF

# 3. Commit the file
# (use your SCM: CVS, Mercurial, etc.)
```

---

## SBM Configuration Details

### Configuration Location
- **Path**: `/projects/sbmdelde/sbm/tools/bms/`
- **Files**: `bmsrc`, `sbmSetenv`, `preRegression.sh`

### Configuration Content
```ini
[test]
env_script = /projects/sbmdelde/sbm/tools/bms/sbmSetenv
pre_script = /projects/sbmdelde/sbm/tools/bms/preRegression.sh

[deliver]
user = sbmdelde
repository = /projects/sbmdelde/delivery

[profile_dev]
test.plugins = sbmunittest

[profile_rel]
test.plugins = sbmunittest, valgrind
```

**Key Settings:**
- **Environment Setup**: Sets SBM-specific environment (local database, sqlite file paths)
- **Default Delivery**: Uses `sbmdelde` account for deliveries to `/projects/sbmdelde/delivery`
- **Test Plugins**: Uses `sbmunittest` plugin by default, adds `valgrind` for release profile

### Important Notes
- **Obsolescence Warning**: SBM documentation is obsolete for versions >= 11
- **Ownership**: Ownership transferred to DEV-RDM-PNR-ASE-PIF team
- **Legacy Scripts**: `test/runRegression.sh` is obsolete with BMS 2.0 and can be removed when all developers migrate

---

## SBR Configuration Details

### Configuration Location
- **Path**: `/projects/sbrdelde/tools/bms/config/`
- **Files**: `bmsrc`, `sbrSetenv`, `preRegression.sh`

### Configuration Content
```ini
[test]
env_script = /projects/sbmdelde/delivery/sbm/tools/bms/sbmSetenv, /projects/sbrdelde/tools/bms/config/sbrSetenv
pre_script = /projects/sbrdelde/tools/bms/config/preRegression.sh

[deliver]
user = sbrdelde
repository = /projects/sbrdelde/delivery

[profile_dev]
test.plugins = sbmunittest

[profile_rel]
test.plugins = sbmunittest, valgrind
```

**Key Settings:**
- **Environment Setup**: Sets SBR environment (SSH local databases, connection parameters) and inherits SBM settings
- **Default Delivery**: Uses `sbrdelde` account for deliveries to `/projects/sbrdelde/delivery`
- **Test Plugins**: Uses `sbmunittest` plugin by default, adds `valgrind` for release profile

### Advanced Component Configuration Example

For components requiring custom scripts (e.g., `sbr::dbServices::Retrieve`):

```ini
[bms]
include_conf = /projects/sbrdelde/tools/bms/config/bmsrc

[test]
post_script = postRegression.sh
pre_script = /projects/sbrdelde/tools/bms/config/preRegression.sh, preRegression.sh
env_script = /projects/sbmdelde/delivery/sbm/tools/bms/sbmSetenv, /projects/sbrdelde/tools/bms/config/sbrSetenv, testEnv
pre_post_once = 1
```

**Key Features:**
- **Script Chaining**: Multiple pre-scripts executed in order (shared config first, then component-specific)
- **Custom Environment**: Component-specific `testEnv` file for local variables (e.g., `AMDORA_XMLDBFILE`)
- **Pre/Post Once**: `pre_post_once = 1` ensures scripts run once regardless of number of test plugins
- **XML DB Tools**: Common pattern uses XML DB dump tool for database state management in unit tests

### Component-Specific Pre-Script Example

```bash
#!/bin/sh
# preRegression.sh - Called before running unit tests

# Get the test path
script_dir=`cd \`dirname $0\`; pwd`

# Dump database state before tests
echo '* Dumping ACTIVATION_PARAMETERS state...'
/projects/sbrdelde/tools/regression/xmldbdump/TableExporter.py \
  -o $script_dir/ACTIVATION_PARAMETERS.backup \
  -u ${AMDORA_IDX_COM_SCHEMA} \
  -p amadeus \
  -d $AMDORA_SERVICE \
  ACTIVATION_PARAMETERS > /dev/null
```

---

## Migration Considerations

### Transition Period (BMS 1.x to 2.0)
When migrating, modify `runRegression.sh` to support both versions:

```bash
#!/bin/sh
# !! DO NOT UPDATE ANYMORE THIS FILE !!
# Only kept for backward compatibility with BMS 1.x

script_dir=`cd \`dirname $0\`; pwd`

# Source environment
. /projects/sbmdelde/delivery/sbm/tools/bms/sbmSetenv
. /projects/sbrdelde/tools/bms/config/sbrSetenv
. $script_dir/testEnv

# Pre-regression scripts
. /projects/sbrdelde/tools/bms/config/preRegression.sh
. $script_dir/preRegression.sh

# Run standard unit test script
/projects/sbmdelde/sbm/tools/stdTest.sh --directory $script_dir "$@"
rc=$?

# Post-regression scripts
. $script_dir/postRegression.sh

exit $rc
```

### Modifying Project Configurations

**Warning**: Project-level configurations affect many components and developers.

**Process for Modifications:**
1. Test changes in your own component first
2. Propose to SBM committee or SBR team leader
3. Log as appropriate user (`sbmdelde` or `sbrdelde`)
4. Commit with Mercurial: `hg commit -u ${your name}`
5. Update documentation accordingly

**Version Control:**
- All configuration files managed by Mercurial
- Enables rollback if issues arise
- Maintains modification history

---

## When to Consult This

- Integrating BMS into SBM or SBR projects
- Migrating components from BMS 1.x to BMS 2.0
- Making components compliant with project standards
- Understanding project-specific BMS configurations
- Setting up custom pre/post scripts or environment variables
- Troubleshooting unit test execution in project context

---

## Related Documentation

- **Configuration**: Cascaded Configuration Files, Configuration Profiles
- **Plugins**: Test plugin, Deliver plugin, sbmunittest plugin, valgrind plugin
- **Tutorial**: General BMS 2.0 tutorial before starting
- **Support**: nce-bms-admin@amadeus.com for BMS questions
- **Version**: BMS 2.5.4.492
