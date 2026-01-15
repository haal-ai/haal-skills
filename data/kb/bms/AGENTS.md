# BMS Context Documentation for AI Agents

## Purpose

This directory contains comprehensive BMS (Build Management System) documentation specifically formatted for AI agent consumption. The content is designed to provide the **bms-expert chatmode** with detailed, structured knowledge about Amadeus' enterprise-scale C/C++ build infrastructure.

## Source

All documentation files in this directory were generated from the official BMS documentation:

**Source URL**: https://bms.cloud.rnd.amadeus.net/bmsdoc/users/contents.html

**BMS Version**: 2.5.4.492 (as of documentation extraction)

## Target Audience

### Primary Consumer
- **bms-expert.chatmode.md** - AI chatmode specializing in BMS expertise for Amadeus developers

### Human Readers
While optimized for AI consumption, these documents are also valuable for:
- Developers learning BMS concepts
- Build engineers troubleshooting issues
- Architects designing component structures
- Documentation maintainers updating AI knowledge bases

## Documentation Structure

The documentation is organized into thematic areas:

### Foundational Concepts (3 files)
- `principles-and-introduction.md` - Core architecture and design principles
- `bms-glossary.md` - Complete terminology reference
- `unix-concepts.md` - Library fundamentals and binary compatibility

### Practical Guides (3 files)
- `installation-guide.md` - Installation and version management
- `tutorial.md` - Daily workflow and essential commands
- `configuration.md` - Configuration system and bmsrc files

### Component Development (3 files)
- `description-xml.md` - Complete Description.xml specification
- `forest.md` - Multi-component workspace management
- `bms-projects.md` - Project-specific configurations (SBM, SBR)

### Advanced Topics (4 files)
- `advanced.md` - Aggregated components, artifacts, generators
- `plugins.md` - Complete plugin reference (27+ plugins)
- `algorithms.md` - Dependency resolution algorithms
- `parallel-tuning.md` - Build performance optimization

### Configuration References (2 files)
- `bmsrc-configuration.md` - Built-in configuration options
- `bmsrc-system-scope.md` - System-level configuration

### Troubleshooting & Support (2 files)
- `bms-faq.md` - Common issues and solutions
- `management.md` - Version management and support processes

### APIs (1 file)
- `bmslib-python-api.md` - Python API for programmatic access

**Total**: 18 documentation files covering all aspects of BMS

## AI Integration Pattern

### How the bms-expert Chatmode Uses This Content

The **bms-expert.chatmode.md** file includes all 18 documentation files via `include` directives:

```markdown
include: '.github/context/dev/bms/principles-and-introduction.md'
include: '.github/context/dev/bms/bms-glossary.md'
# ... (all 18 files)
```

### Context Loading Strategy

The AI agent:
1. **Lazy loads** documentation based on user questions
2. **Indexes summaries** from each file's opening sections
3. **Retrieves full content** when detailed information is needed
4. **Cross-references** between files for comprehensive answers

### Example Usage Flow

```
User: "How do I fix a binary incompatibility error?"
  ↓
AI checks: bms-glossary.md (terminology)
  ↓
AI loads: algorithms.md (version resolution)
  ↓
AI references: bms-faq.md (troubleshooting steps)
  ↓
AI provides: Complete solution with config examples
```

## Content Format

### Document Structure
Each markdown file follows this pattern:

```markdown
# Topic Title

## Summary
Brief overview of the topic and when to use it

## Key Concepts
- Bulleted list of core ideas
- Critical terminology
- Important patterns

## Usage
Practical examples, commands, and configurations

## Related Topics
Cross-references to other documentation files
```

### Optimizations for AI Consumption
- **Summaries first** - Each file starts with a concise summary
- **Key concepts** - Highlighted terminology and patterns
- **Practical examples** - Concrete code snippets and commands
- **Contextual notes** - When to use specific features
- **Version awareness** - Notes on version-specific behavior

## Maintenance

### Updating Documentation

When BMS documentation changes:

1. **Extract updated content** from https://bms.cloud.rnd.amadeus.net/bmsdoc/users/
2. **Preserve structure** - Maintain the Summary → Key Concepts → Usage pattern
3. **Update version references** - Note the BMS version in each file
4. **Test AI integration** - Verify bms-expert chatmode can access updates
5. **Update this file** - Reflect any structural changes

### Version Tracking

- **Current BMS Version**: 2.5.4.492
- **Documentation Source**: Official BMS user documentation
- **Last Updated**: October 2025
- **Update Frequency**: As needed when significant BMS changes occur

### Quality Criteria

Documentation updates should:
- ✅ Maintain consistent formatting across all files
- ✅ Include practical examples for complex concepts
- ✅ Cross-reference related topics
- ✅ Highlight version-specific behavior
- ✅ Provide clear summaries for AI indexing
- ✅ Use exact BMS terminology from glossary

## Related Documentation

### Other AI Context Directories
- `.github/context/dev/` - Parent directory for development context
- `.github/context/architecture/` - System architecture documentation
- `.github/context/` - Root context directory for all domains

### BMS Chatmode
- `.github/chatmodes/bms-expert.chatmode.md` - AI persona that consumes this content

### Official BMS Resources
- **User Documentation**: https://bms.cloud.rnd.amadeus.net/bmsdoc/users/
- **Code Documentation**: https://bms.cloud.rnd.amadeus.net/bmsdoc/code/
- **R&D Request Portal**: http://rndwww.nce.amadeus.net/rndrequest/ (topic: BMS)

## Usage Statistics

### Scope and Scale
- **Users**: 1,500+ Amadeus C++ developers
- **Executions**: 2,000,000 BMS operations per week
- **Components**: Thousands of BMS-managed components
- **Repositories**: Multiple Artifactory and filesystem repositories

### AI Agent Impact
By providing comprehensive, structured documentation:
- **Reduces support burden** on BMS team
- **Improves developer productivity** with instant, accurate answers
- **Ensures consistency** in BMS best practices across teams
- **Enables self-service** troubleshooting and learning

## Contributing

### Adding New Content

When adding new BMS documentation:

1. **Follow the established structure** (Summary → Key Concepts → Usage)
2. **Use consistent formatting** matching existing files
3. **Add include directive** to `bms-expert.chatmode.md`
4. **Update this AGENTS.md** to reflect new content
5. **Test AI responses** with sample questions

### Reporting Issues

If you find:
- **Outdated information** - Check against current BMS version
- **Missing topics** - Identify gaps in coverage
- **Unclear content** - Suggest improvements for AI consumption
- **Broken cross-references** - Fix links between files

Contact the shared-context repository maintainers or submit a pull request.

---

**Last Updated**: October 2025  
**Documentation Version**: BMS 2.5.4.492  
**Maintained By**: Shared Context Repository Team  
**For Questions**: See `.github/context/AGENTS.md` or repository CONTRIBUTING.md
