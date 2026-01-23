# Get BMS Expertise

Load the BMS expert persona with comprehensive knowledge of Amadeus' enterprise-scale C/C++ build system.

## Purpose

This skill transforms the AI into a Senior BMS Specialist with:
- 10+ years of BMS experience
- Deep knowledge of component-based architecture
- Binary compatibility expertise
- Build/test/delivery workflow mastery
- Problem-solving methodology for common BMS scenarios

## Usage

```bash
olaf get-bms-expertise
```

After activation, ask BMS-related questions naturally:
- "How do I fix a binary incompatibility error?"
- "What's the difference between external and internal dependencies?"
- "How do I optimize parallel builds in a forest workspace?"
- "My component delivery is failing, what should I check?"

## What This Skill Provides

### Embedded Expertise

- **Behavioral Guidelines**: Problem-solving approach, communication style, quality standards
- **Command Reference**: Essential BMS commands for build, test, deliver, deps, configuration
- **Troubleshooting Scenarios**: Dependency issues, build problems, delivery failures, forest management
- **Knowledge Snippets**: Description.xml patterns, version management rules, plugin architecture

### Knowledge Base Integration

For detailed technical information, the skill references:
- `.olaf/data/kb/bms-kb-index.md` - Routing index to 18 BMS documentation files
- Can use `tell-me` skill to search specific topics

## Example Session

```
User: olaf get-bms-expertise

AI: ✅ BMS Expert Mode Activated

I'm now operating as a Senior BMS Specialist with expertise in:
- Component-based C/C++ architecture
- Binary compatibility management  
- Build/test/delivery workflows
- Dependency resolution and Forest workspaces

How can I assist you with BMS today?

User: My build is failing with "undefined reference" errors

AI: [Diagnoses as link error, checks Description.xml sources, suggests solutions...]
```

## Benefits

- **Fast activation**: Single command loads complete BMS expertise
- **Consistent guidance**: Follows BMS best practices and axioms
- **Structured problem-solving**: Applies 5-step diagnostic methodology
- **Safety-focused**: Always warns about binary compatibility risks
- **Knowledge-backed**: Can reference detailed docs when needed

## Integration

Works seamlessly with:
- `tell-me` skill - Search BMS knowledge base
- BMS documentation in `.olaf/data/kb/bms/`
- BMS knowledge base index for topic routing
