# BMS Installation Guide

## Summary
This guide explains how to install and select BMS (Build Management System) versions across different platforms and environments. It covers version channels (alpha, beta, stable, previous), installation methods (clean OS packages vs virtualenv-based), and platform-specific considerations for RHEL, Ubuntu, Debian, Fedora, and SLES12.

> BMS is distributed through multiple channels with different stability levels, and installation methods vary based on the operating system. Modern "clean" OS packages are preferred over legacy virtualenv-based installations.

---

## Key Concepts

### Version Channels
- **alpha** (formerly "nightly") - Latest from master branch, used by BMS developers and OTF builds, reasonably stable
- **beta** (formerly "future") - Recommended for most users, solid enough to become stable soon, helps detect bugs early
- **stable** (formerly "latest") - Rock-solid, fire-tested version for maximum stability
- **previous** - Fallback version, seldom modified (may be deprecated)

### Package Types
- **Clean OS packages** - Proper integration with OS package manager (RHEL, Fedora, Ubuntu, Debian)
- **Virtualenv-based packages** - Legacy installation under `/opt` (SLES12 only, planned for deprecation)

### BMS Package Variants
- `amadeus-bms` - Command-line tool
- `python3-amadeus-bms` - Python library for scripts (e.g., CMK)
- `amadeus-bms-user-doc` - HTML user documentation
- `amadeus-bms-code-doc` - HTML code documentation for contributors
- `amadeus-bms-opt-py3` - Compatibility symlinks for `/opt` (legacy scripts only)

---

## Usage

### Installing BMS on Modern OS (RHEL, Fedora, Ubuntu, Debian)

Setup OBE tools repository (one-time):
```bash
curl -fsSL "https://repository.rnd.amadeus.net/artifactory/obe-tools-rpm/install.sh" | bash
```

This automatically provides access to the **stable** BMS channel.

### Adding Beta Channel (Recommended)

**For Debian/Ubuntu:**
Create `/etc/apt/sources.list.d/deb-bms-bullseye-beta.sources`:
```
Types: deb
URIs: https://repository.rnd.amadeus.net/deb-bms/
Suites: bullseye-beta
Components: main
Trusted: yes
```

**For RHEL/Fedora:**
Create `/etc/yum.repos.d/amadeus-obe-tools-el-beta.repo`:
```
[bms-el$releasever-beta]
name = BMS-beta for el$releasever
baseurl = https://repository.rnd.amadeus.net/rpm-bms/el$releasever/beta/
enabled = 1
gpgcheck = 0
gpgkey = https://repository.rnd.amadeus.net/api/gpg/key/public
```

Or install the channel package:
```bash
# For RHEL/Fedora
zypper install -y amadeus-bms-beta-channel
zypper update -y
```

### Selecting BMS Version on Development Servers

Set in `~/.zshenv.user` (don't export):
```bash
BMS_ENABLE_DEFAULT_FLAVOR=beta     # Recommended
BMS_ENABLE_DEFAULT_FLAVOR=alpha    # Latest development
BMS_ENABLE_DEFAULT_FLAVOR=stable   # Most stable
BMS_ENABLE_DEFAULT_FLAVOR=2.5.4.42 # Specific version
```

Restart shell after changes.

### Installing on SLES12 (Legacy Virtualenv Method)

Setup repository:
```bash
curl -fsSL "https://repository.rnd.amadeus.net/artifactory/obe-tools-rpm/install.sh" | bash
```

For beta channel, create `/etc/yum.repos.d/bms-sles12-beta.repo`:
```
[Artifactory]
name=Artifactory
baseurl=https://repository.rnd.amadeus.net/artifactory/rpm-bms/sles12/beta
enabled=1
gpgcheck=0
```

Or install channel package:
```bash
zypper install -y amadeus-bms-beta-channel
zypper update -y
```

### Jenkins Integration (Beta Channel)

Add to Jenkinsfile:
```groovy
boolean useBmsBeta = true

if (useBmsBeta) {
    sh(label: "Install BMS-beta", script: '''#!/bin/bash
die () { echo "$*"; exit 1; }
pr () { echo "+ $*"; "$@"; }
if ((UID != 0)); then
    die "must run as root"
fi
pr zypper install -y amadeus-bms-beta-channel || exit 1
pr zypper update -y || exit 1
''')
}
```

### SWBv2 Workflow Configuration

Add to `workbench.yaml`:
```yaml
channel_packages:
  - amadeus-bms-beta-channel
```

---

## Platform Support

### Supported OS with Clean Packages (Recommended)
- RHEL
- Fedora  
- Ubuntu
- Debian

### Supported OS with Virtualenv Packages (Legacy)
- SLES12 (installation under `/opt/devsup/bms/`, ~300MB, planned for deprecation)

### Deprecated
- Python 2 support (removed October 2021)
- `/nastools/scs` and `~intsts` scripts (may be removed anytime)
- SLES11 legacy PYT pack

---

## Important Notes

- **Beta is recommended** for most users - helps detect bugs before they reach stable
- **Clean OS packages** are preferred - only ~5MB vs ~300MB for virtualenv or ~1GB for Conda
- **Version 2.5.4.492** is current as of documentation date
- **Four channels** are the only officially supported versions (plus master branch)
- **SLES12 virtualenv packages** will be discontinued when SLES12 is decommissioned
