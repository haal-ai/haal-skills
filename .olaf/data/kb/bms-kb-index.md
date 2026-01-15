# BMS Knowledge Base Index

This index helps route questions about Amadeus BMS (Build Management System) to the appropriate documentation files.

## About BMS

BMS is Amadeus' enterprise-scale C/C++ build infrastructure serving 1,500+ developers with 2,000,000 weekly build executions. It provides component-based architecture, binary compatibility management, and automated build/test/delivery pipelines.

## Documentation Navigation

### Foundational Concepts and Terminology

**Core BMS architecture, component-based design, binary compatibility strategy, and enterprise-scale metrics**
→ `bms/principles-and-introduction.md`

**Complete BMS terminology (components, dependencies, ROOT/LEAF, versioners, and graph concepts)**
→ `bms/bms-glossary.md`

**Static vs shared libraries, dynamic linking, binary compatibility fundamentals, and SONAME resolution**
→ `bms/unix-concepts.md`

### Practical Guides and Tutorials

**BMS installation across platforms, version channels (alpha/beta/stable), OS packages, and environment selection**
→ `bms/installation-guide.md`

**Daily workflow commands (build/test/deliver), component structure, configuration hierarchy, and basic usage patterns**
→ `bms/tutorial.md`

**Cascaded bmsrc configuration system, profiles, repository setup, include directives, and override operators**
→ `bms/configuration.md`

### Component Development and Structure

**Complete Description.xml schema (properties, dependencies, build targets, public includes, and delivery specifications)**
→ `bms/description-xml.md`

**Multi-component workspace management, Forest.xml structure, constraint propagation, auto-discovery, and topological operations**
→ `bms/forest.md`

**Project-specific BMS configurations (SBM, SBR), cascaded bmsrc integration, and migration procedures**
→ `bms/bms-projects.md`

### Advanced Features and Optimization

**Aggregated components, artifact repository, BMS configs, code generators, interface/implementation patterns, and snapshots**
→ `bms/advanced.md`

**Complete plugin reference (build, test, deliver, deps, replicate, clean, static analysis) with usage and configuration**
→ `bms/plugins.md`

**Dependency graph construction, version resolution algorithm, binary compatibility checking, and conflict detection**
→ `bms/algorithms.md`

**Optimization strategies for forest.parallel vs build.parallel, memory constraints, and build performance tuning**
→ `bms/parallel-tuning.md`

### Troubleshooting and Support

**Common errors and solutions (build failures, delivery issues, dependency conflicts, generator problems, and XML validation)**
→ `bms/bms-faq.md`

**BMS version management, backward/forward compatibility, change request process, support channels, and contribution guidelines**
→ `bms/management.md`

### Configuration References

**Built-in bmsrc defaults and comprehensive option reference for all plugins, profiles, and system configurations**
→ `bms/bmsrc-configuration.md`

**System-level configuration for environment-specific settings (devservers, DevBox, CI), replication dirs, and ccache**
→ `bms/bmsrc-system-scope.md`

### APIs and Programmatic Access

**Python API for Description.xml manipulation, component automation, plugin development, and environment setup**
→ `bms/bmslib-python-api.md`

## Quick Reference

### Common Questions → Documentation

| Question Type | Documentation File |
|--------------|-------------------|
| How do I build a component? | `tutorial.md` |
| How do I configure dependencies? | `description-xml.md` |
| What are external vs internal dependencies? | `bms-glossary.md` |
| How do I set up a forest workspace? | `forest.md` |
| How do I optimize build performance? | `parallel-tuning.md` |
| Build failed, what do I check? | `bms-faq.md` |
| How do I use the test plugins? | `plugins.md` |
| What is binary compatibility? | `principles-and-introduction.md` |
| How do I configure repositories? | `configuration.md` |
| How do I use aggregated components? | `advanced.md` |

## Essential Commands

```bash
# Core workflow
bms build              # Compile componentPack
bms build -t           # Build unitTestPack
bms test               # Run unit tests
bms deliver            # Full delivery pipeline

# Dependency management
bms deps               # View dependency graph
bms deps --unpack      # Show aggregated dependencies
bms replicate          # Cache dependencies locally

# Configuration
bms -s                 # Show configuration
bms -p <profile>       # Use specific profile

# Forest operations
bms --use-forest build # Force forest mode
bms --no-forest build  # Disable forest mode
```

## Version Information

Current BMS Version: 2.5.4.492
Documentation Last Updated: 2025-11

## Support Channels

1. R&D Request Portal (topic: BMS)
2. BMS admin: NCE-BMS-Admin@amadeus.com
3. BMS "sheriff" (support rotation)

## File Locations

All BMS documentation files are located in:
`.olaf/data/kb/bms/`

Or in the source repository:
`.olaf/your-repos/shared-context/.github/context/dev/bms/`
