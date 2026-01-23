# BMS Frequently Asked Questions

## Summary
This document covers common issues, errors, and solutions encountered when working with BMS (Build Management System) version 2.5.4.492. It provides troubleshooting guidance for build errors, delivery problems, dependency resolution, forest configurations, generators, configuration issues, replication, and XML validation. Use this reference when diagnosing BMS-related problems or helping developers resolve build and delivery issues.

---

## Key Topics

### Build Issues
- **Missing class definitions** - Link-time errors for undefined references
- **Permission denied errors** - File access issues during builds
- **Configuration checking** - Validating BMS settings
- **CMK installation problems** - Environment variable conflicts

### Delivery & Deployment
- **Identifying component owners** - Finding who delivered a component
- **Delivery vs standard builds** - Understanding compilation differences
- **Incomplete deliveries** - Missing folders or files in delivered components
- **SSH authentication failures** - Too many private keys causing connection drops
- **Description.xml errors** - XML validation against XSD schema

### Dependencies
- **Version resolution failures** - Missing or conflicting dependency versions
- **Forest constraints** - Version mismatches between forest and external contexts
- **Versioner configuration** - Proper setup of dependency versioners

### Generators
- **Generator debugging** - Investigating failed code generation
- **Log analysis** - Finding generator output in bms.log
- **Manual reproduction** - Testing generators locally

### Configuration & Environment
- **BMS configuration validation** - Checking settings with `bms -s`
- **Repository setup** - Proper use of `+=` vs `=` operators
- **Environment variables** - GREP_OPTIONS conflicts

### Replication & Storage
- **Disk space management** - Cleaning old replication data
- **Manual cleanup procedures** - SSH access and file removal

### XML & Schema Validation
- **Namespace identifiers** - Understanding URIs vs URLs
- **XSD file locations** - Current locations for schema files
- **Schema validation** - Different XSD files for forest vs non-forest contexts

---

## Build FAQ

### Missing Class Definition (Link Error)

**Issue:** Undefined reference error during linking, e.g., `undefined reference to 'sbr::[...]::DbServiceVisitor::getRequiresBlobFiltering() const'`

**Cause:** Function declaration found at compile time (header exists) but definition (function body) not found at link time. The corresponding `.cpp` file was not compiled.

**Solution:** 
- Verify the `.cpp` file exists
- Check that it's included in the source file list in `Description.xml`
- Ensure the file is being compiled

---

### Permission Denied Error

**Issue:** `OSError: [Errno 13] Permission denied: './bmstmp'`

**Solution:** Configure BMS to use local temporary files by adding to your BMS configuration:

```ini
[BMS]
local_tempfiles = 1
```

**Reference:** BMS-2155 ticket

---

## Delivery FAQ

### How to Know Who Delivered a BMS Component

**Method 1 - Check Description.xml:**
```bash
grep -i contactpoint Description.xml
```
Output example: `<contactPoint>DEV-RDM-TKE-TKD-FOP</contactPoint>`

**Method 2 - Check delivery.log:**
Look for `delivery.log` file delivered with the component.

**Method 3 - Check compilation metadata:**
```bash
strings lib/Linux2-6_64/MultiThread/Debug/g++_3_4_2/libMdwFkproxy.so | grep -i compiled
```
Output example: `Compiled on Fri Mar 19 19:50:37 MET 2010 by lcapanac`

Note: Compilation metadata is added by `mdw::CFC`

---

### Difference Between Delivery Build and Standard Build

BMS executes the same commands but with different profiles and configurations. A `bms build` may succeed while delivery fails.

**Debugging approach:**
Enable compilation logs by creating `.bms/bmsrc`:

```ini
[build]
silent = 0
```

Since the deliver plugin calls the build plugin, this option will be checked and all logs will be available for comparison.

---

### Incomplete Delivery (Missing Folders/Files)

**Cause:** Delivery controlled by two sections in `Description.xml`:
- `<publicIncludes>` - Public header files
- `<delivery>` - Additional files to deliver

**Common mistake:** Using `recursive="true"` on root directory causes previously delivered folders to be removed.

**Example problem:**
```xml
<delivery>
    <dir name="." filters="*.xml" recursive="true" />  <!-- PROBLEM -->
    <dir name="include" filters="*.h *.i" recursive="true" />
</delivery>
```

The root directory delivery removes the `include` directory that was already delivered.

**Solution:** Set `recursive="false"` explicitly:
```xml
<delivery>
    <dir name="." filters="*.xml" recursive="false" />  <!-- FIXED -->
</delivery>
```

**Important:** In most cases, the `<delivery>` section is not needed. BMS always delivers:
- `Description.xml`
- Public headers
- Compiled libraries

Use `<delivery>` only for special cases like documentation.

---

### SSH Authentication Failure - Too Many Keys

**Issue:** `too many authentication failure` error without password prompt

**Cause:** Too many private keys in SSH configuration. Each key is tried; if max attempts ≤ number of keys, connection drops before password prompt.

Example problematic config (`~/.ssh/config`):
```
IdentityFile ~/.ssh/advoncal.priv
IdentityFile ~/.ssh/id_dsa
IdentityFile ~/.ssh/iiponcal
IdentityFile ~/.ssh/resoncal
IdentityFile ~/.ssh/intiip
IdentityFile ~/.ssh/deviip
```

**Solution:** Remove unnecessary private keys and use proper public-key authentication methods.

---

### DescriptionError - XML Structure Validation

**Issue:** XML validation errors when running `bms deps -k` or `bms deliver`

**Cause:** BMS validates `Description.xml` against XSD schema. Different schemas apply:
- **In a Forest:** Some fields (like versioner versions) may be omitted
- **Outside a Forest:** All required fields must be present

**XSD Files:**
- [XSD used when in a forest](Description_weak.xsd)
- [XSD used when not in a forest](Description.xsd)

---

## Dependencies FAQ

### No Version Found for Dependency

**Issue:** Warning that a version for a dependency could not be computed

**Cause:** Versioner only loads direct dependencies, not the complete graph. If dependency is not direct, version cannot be resolved.

**Example problem:**
```xml
<versioner name="addElemInBF::plugins::BasePlugin"/>
<dependency type="internal" name="mdw::OTF"/>
```
Only valid if `mdw::OTF` is a **direct** dependency of `addElemInBF::plugins::BasePlugin`.

**Solution:** Add intermediate versioner:
```xml
<versioner name="addElemInBF::plugins::BasePlugin"/>
<versioner name="mdw::Pack"/>
<dependency type="internal" name="mdw::OTF"/>
```

The version resolution chain: `BasePlugin` → `Pack` → `OTF`

---

### Version Found Outside Forest But Not Inside

**Issue:** Component has version outside forest but no version inside forest after applying constraints

**Example error:**
```
BmsError: Component package::Bom, dependency of sbm::element::Package, has version 3-2-0-0 
outside of forest (versioned by tkd::Pack 11-0-1-0 main), but no version inside forest.
```

**Cause:** Forest constraints upgrade versioner to a version that no longer provides the required dependency.

**Workaround:** Add constraint or strong versioner to force dependency version (may result in inclusion in applicative tarball if not in ulam pack).

**Proper fix:** Upgrade component dependencies to match forest constraints.

---

## Forest FAQ

### Forest of Forests

**Status:** Not supported

**Reference:** See BMS documentation on "Forest of forests" for details.

---

## Generator FAQ

### How Does a Specific Generator Work?

Generators are not managed by BMS - they're provided by external teams.

**Finding contact:**
- Check `Description.xml` for `<contactPoint>`
- Check `delivery.log`
- Use `strings` command on compiled libraries

---

### Investigating Generator Failures

**Scenario 1 - Generator not called:**

If no log like `Generating code with mdw::GrammarGenerator (full logs in bms.log)...` appears, generator wasn't run.

**Cause:** BMS assumes generator already succeeded (e.g., failed previously with exit code 0 but created output folder).

**Solution:** Force rebuild with `bms clean`

**Scenario 2 - Generator failed:**

Check `bms.log` for generator output. If no logs found, generator failed silently.

**Manual reproduction steps:**
1. Copy generator to temporary directory
2. Run `bms build --links` in the copy
3. Add `<component>/links/Linux2-6_64/MultiThread/Release/g++_4_3_2` (or equivalent) to `LD_LIBRARY_PATH`
4. Manually run the command from the error message
5. Contact generator team to add logging for the scenario

---

## Generic FAQ

### Checking BMS Configuration

**Command:** `bms -s` (run from root of Description or forest)

**Purpose:** Display current configuration and verify changes are applied

**Example workflow:**

Create configuration:
```ini
# .bms/bmsrc
[bms]
repositories += ~mwdeldev
[deliver]
profiles = devg4
```

Verify with `bms -s`:
```ini
[bms]
local_tempfiles = 1
profile = dev
repositories = /data/mwrep/rev, ..., ~mwdeldev
...
[deliver]
excludes = CVS, .1DE, .hg
repository = 
profiles = devg4
```

**Common mistake:** Using `=` instead of `+=` for repositories (replaces entire list instead of appending)

---

### Issue During CMK Install

**Issue:** `[ERROR] Invalid library name: 30:SONAMElibicui18n.so.50`

**Cause:** `GREP_OPTIONS` environment variable interferes with BMS library name parsing

**Solution:** Check and unset `GREP_OPTIONS` if configured in your shell environment

---

## Replication FAQ

### Replication Folder is Full

**Solution:** Manual cleanup via SSH

**Steps:**

1. Get replication configuration:
```bash
bms -s | grep -A 13 '\[replicate\]' | egrep "^user|^ssh_key|^replication_dir"
```

Example output:
```
ssh_key = /projects/intres/intres_key
replication_dir = /data/mwrep/res
user = intres
```

2. SSH to replication server:
```bash
ssh -i /projects/intres/intres_key intres@$HOST
```

3. Clean old components (unused in last 10 days):
```bash
find /data/mwrep -maxdepth 6 -name Description.xml -atime +10 | sed -e 's:/[^/]*$::' | xargs rm -rf
```

4. Or clean everything:
```bash
rm -rf /data/mwrep/res
```

---

## XML FAQ

### Understanding XML Namespaces, URIs and URLs

**Key concept:** XML namespaces use URIs as identifiers (Uniform Resource **Identifiers**), not URLs for downloading.

**Example namespace identifier:**
```xml
xmlns="http://gcnet/documentation/bms/metadata/1-0/"
```

This is a **string identifier only**, not meant to be accessed over the network. Like a type in programming, it's difficult to change once written.

**Schema location:** XML documents may link to XSD files via `schemaLocation`:
```xml
schemaLocation="NAMESPACE1 XSD_URL1 NAMESPACE2 XSD_URL2..."
```

The schemaLocation provides pairs of (namespace, XSD URL) for validation.

---

### Downloading a Namespace Identifier Fails

**Issue:** Attempting to download BMS namespace identifiers fails

**Examples of identifiers (not URLs):**
```xml
xmlns="http://gcnet/documentation/bms/metadata/1-0/"
schemaLocation="http://obe.nce.amadeus.net/bms/metadata/1-0/ XSD_URL"
```

**Important:** These are identifiers, not downloadable URLs. Trying to access them in a browser will fail - this is expected and harmless.

**Historical note:** These identifiers reference decommissioned Amadeus servers (gcnet, obe.nce.amadeus.net).

---

### The Link to the XSD Does Not Work

**Issue:** XML validation software fails to download XSD files

**Decommissioned URLs (do not work):**
- `http://obe.nce.amadeus.net/bms/metadata/1-0/Description.xsd`
- `http://gcnet/documentation/bms/metadata/1-0/Description.xsd`

**Solution:** Update XSD_URLs (not namespaces) to current locations (see next section)

---

### Where Can I Find the XSD Files?

**Current locations:**
- Forest XSD: `https://bms.cloud.rnd.amadeus.net/bmsdoc/users/_static/Forest.xsd`
- Description XSD: `https://bms.cloud.rnd.amadeus.net/bmsdoc/users/_static/Description.xsd`
- Description (weak) XSD: `https://bms.cloud.rnd.amadeus.net/bmsdoc/users/_static/Description_weak.xsd`

**Usage:** For validation or XML editor assistance

---

## Common Commands Reference

### Diagnostic Commands
```bash
# Check BMS configuration
bms -s

# Find who delivered a component
grep -i contactpoint Description.xml
strings <library.so> | grep -i compiled

# Check replication settings
bms -s | grep -A 13 '\[replicate\]'
```

### Build Commands
```bash
# Clean build (force generator re-run)
bms clean

# Build with symlinks
bms build --links

# Enable verbose output (in .bms/bmsrc)
[build]
silent = 0
```

### Dependency Commands
```bash
# Check dependencies with keep-going
bms deps -k
```

---

## Configuration File Examples

### Enable Local Temp Files
```ini
# .bms/bmsrc
[BMS]
local_tempfiles = 1
```

### Add Repository (append)
```ini
# .bms/bmsrc
[bms]
repositories += ~mwdeldev
```

### Set Delivery Profile
```ini
# .bms/bmsrc
[deliver]
profiles = devg4
```

### Enable Build Logs
```ini
# .bms/bmsrc
[build]
silent = 0
```

---

## Support Contacts

**BMS Team:** nce-bms-admin@amadeus.com

**Issue Tracking:**
- Support: R&D Support Portal → BMS / Support
- Feature Requests: R&D Support Portal → BMS / New Feature

**Current Version:** BMS 2.5.4.492
