# bmslib - The BMS Python API

## Summary
The BMS Python API (`bmslib`) provides programmatic access to BMS functionality for reading/writing Description.xml files, validating components, accessing the dependency engine, and extending BMS through a plugin framework. This eliminates the need for command-line wrappers and enables native Python-based BMS extensions.

> **Use when:** Automating BMS tasks, building custom tooling around BMS, accessing Description.xml programmatically, or creating BMS plugins for team-specific workflows.

---

## Key Concepts
- **Two main APIs**: Client API (`bmslib.api`) for Description.xml manipulation and a dependencies engine API
- **Plugin framework**: Extend BMS natively without complex wrapper scripts
- **Environment setup**: Requires proper Python environment with all dependencies
- **API stability**: Only `bmslib.api` is officially supported; internal structures may change
- **Python 2/3 support**: Multiple Python versions supported via different entry points

---

## Python Environment Setup

### Recommended Approaches (Clean Way)
BMS library requires a properly configured Python environment. Three supported methods:

1. **OS Package** - Ubuntu bionic (18.04) packages available, more OS support planned
2. **virtualenv** - Create isolated Python environment with controlled dependencies
3. **conda** - Use conda environment management

**Advantages:**
- Full control over dependencies
- Can add/upgrade packages as needed
- Stable, predictable environment

**Example project:** [example-program-using-bmslib](https://rndwww.nce.amadeus.net/git/projects/BMS/repos/example-program-using-bmslib/browse)

### Reusing BMS's virtualenv
Alternative approach using BMS's bundled virtualenv on development servers:

```bash
# Source the environment
source /opt/devsup/bms/setenv

# Or use in shebang
#!/usr/bin/env bms-python      # Auto-detect Python version
#!/usr/bin/env bms-python2     # Force Python 2
#!/usr/bin/env bms-python3     # Force Python 3
```

**Limitations:**
- No write access to environment
- Cannot add/upgrade dependencies
- BMS dependency upgrades may break your scripts

**Legacy approach (deprecated):** Adding `/opt/devsup/bms/latest` to PYTHONPATH and calling `bmslib.set_environment()` - unreliable due to evolving dependencies.

---

## API Usage

### Basic Setup for Advanced Features
```python
import bmslib
bmslib.set_environment()
```

### API Modules
- **`bmslib.api`** - Main client API (stable, officially supported)
- **`bmslib.description`** - Description.xml manipulation API

**Key classes/components:**
- `Description` - Parse/manipulate Description.xml
- `Component`, `DescriptionComponent` - Component representations
- `Dependency` - Dependency management
- `BuildTarget`, `BinaryTarget`, `LibraryTarget` - Build target types
- `Generator`, `Versioner`, `PythonPackage` - Various component types

---

## Version Management & Compatibility

### Dependency Version Strategy
- **User responsibility**: Upgrade your code when BMS dependencies change
- **BMS team commitment**: Ensure BMS itself works with new dependency versions
- **No compatibility guarantees**: BMS cannot maintain compatibility for all user scripts
- **Recommendation**: Use your own virtualenv/conda environment with pinned versions

### API Stability Warning
⚠️ **Only `bmslib.api` is officially stable**

- Python's open nature allows access to any internal structure
- BMS developers may refactor internals without notice
- Accessing undocumented attributes (e.g., `vers_cache` on Description objects) is **unsupported**
- Use common sense - stick to documented API surface

**Alternative:** Contribute features directly to BMS with automated tests to ensure future compatibility during refactoring.

---

## Known Programs Using bmslib

**Note:** BMS team is NOT responsible for these tools.

- **CMK** - Component Management Kit ([Bitbucket](https://rndwww.nce.amadeus.net/git/projects/CMK/repos/cmk4/browse), [Docs](https://static.forge.amadeus.net/packs-tooling-documentation/cmk/index.html))
- **hgtools** - Mercurial tools ([Bitbucket](https://rndwww.nce.amadeus.net/git/projects/DCSI/repos/hgtools/browse))
- **bmslite/bmslite2/bmslite_ID** - Self-service check-in scripts (`/remote/intdeliv/sscdelde/script/`)
- **CLion BMS plugin** - IDE integration
- **MdwPackageEnvelope** - SSP package envelope tool ([Bitbucket](https://rndwww.nce.amadeus.net/git/projects/SSPC/repos/mdwpackageenvelope/browse))
- **bms-bridge** - Bridge tool ([Confluence](https://rndwww.nce.amadeus.net/confluence/x/mndNK), [Bitbucket](https://rndwww.nce.amadeus.net/git/users/semonet/repos/bms-bridge/browse))

See [BMS-2556](https://amadeus.atlassian.net/l/cp/yLMF1YUB) for comprehensive list.

---

## Best Practices

1. **Use official API** - Stick to `bmslib.api` for stability
2. **Control your environment** - Prefer virtualenv/conda over reusing BMS's environment
3. **Pin dependency versions** - Avoid breakage from BMS dependency upgrades
4. **Test compatibility** - Validate your code when upgrading BMS versions
5. **Contribute upstream** - Submit features to BMS with tests for guaranteed compatibility

---

## References

- **Main API Documentation:** `bmslib.api` module
- **Description.xml API:** `bmslib.description` module
- **BMS Version:** 2.5.4.492
- **Support:** [R&D Support Portal - BMS / Support](http://rndwww.nce.amadeus.net/rndrequest/RND_request.jsp?topic=10030&subtopic=100302)
- **Feature Requests:** [R&D Support Portal - BMS / New Feature](http://rndwww.nce.amadeus.net/rndrequest/RND_request.jsp?topic=10030&subtopic=100304)
