# List Competencies Tutorial

## Quick Start

To see all available OLAF competencies and skills:
```
list competencies
```

or

```
show competencies
```

## Understanding the Output

When you run this command, you'll see a formatted list like:

```
Available OLAF Competencies:

1. Assess GenAI Initiative Idea
   Path: assess-genai-initiative-idea.md
   Protocol: Propose-Act
   
2. Find Expert Contact
   Path: find-expert-contact.md
   Protocol: Propose-Act
   
3. OLAF Help Me
   Path: help-me-olaf.md
   Protocol: Act
   
4. Report My Daily
   Path: report-my-daily.md
   Protocol: Propose-Act
   
5. Should I Use AI
   Path: should-i-use-ai.md
   Protocol: Propose-Act

... (and more)
```

## Understanding Protocols

Each competency uses a specific interaction protocol:

### Act
Direct execution without confirmation.
**Example**: `time-retrieval` - Just gives you the timestamp

### Propose-Act
Proposes a plan, then executes automatically.
**Example**: `assess-genai-initiative-idea` - Shows research plan, then executes

### Propose-Confirm-Act
Proposes a plan, waits for confirmation, then executes.
**Example**: `prepare-conversation-handover` - Shows what will be saved, waits for approval

## Common Usage Scenarios

### Scenario 1: Discovering What's Available

**You**: "I need to do something with git, but I'm not sure what's available."

**Action**: 
```
list competencies
```

**Result**: You see all competencies, including git-related ones like:
- Git Assistant competencies
- Stash management
- Version control operations

### Scenario 2: Finding the Right Tool

**You**: "I want to save my work before switching tasks."

**Action**: 
```
list competencies
```

**Look for**: "stash-work-session" in the results

**Then use**: 
```
stash work
```

### Scenario 3: Learning OLAF Capabilities

**You**: "What can OLAF do for project management?"

**Action**:
```
list competencies
```

**Filter mentally** or ask: "Show me project management competencies"

**Result**: See items like:
- Report my daily
- Prepare conversation handover
- Store conversation record

## Filtering and Narrowing

If the list is too long, you can:

### Ask for specific categories:
```
list competencies for project management
```

### Ask for specific tags:
```
show me git competencies
```

### Ask for specific status:
```
list proven competencies only
```

## After Listing - Next Steps

Once you see the list:

### 1. Select and Execute
```
Use competency: assess-genai-initiative-idea
```

### 2. Learn More About One
```
Tell me more about the "stash-work-session" competency
```

### 3. Filter Further
```
Show me only the competencies with "Act" protocol
```

## Understanding the Index

The list comes from the OLAF competency index, which includes:

- **Skills** from `skills/`
- **Legacy competencies** from `core/competencies/`
- **Metadata** including status, exposure, and protocol

## Reading the Metadata

Each competency shows:

**Title**: Human-readable name  
**Path**: File location relative to skill/competency folder  
**Protocol**: Interaction pattern (Act, Propose-Act, Propose-Confirm-Act)  
**Status** (if shown): proven, experimental, deprecated  
**Exposure** (if shown): kernel, internal, external

### Status Meanings:
- **proven**: Battle-tested, reliable
- **experimental**: New, may change
- **deprecated**: Being phased out

### Exposure Meanings:
- **kernel**: Core OLAF functionality
- **internal**: For OLAF framework use
- **external**: User-facing capabilities

## Tips for Effective Discovery

### ✅ Do's

- **Browse regularly**: Periodically review to discover new capabilities
- **Read descriptions**: Understand what each competency does
- **Check protocols**: Know whether you'll need to confirm actions
- **Use filters**: Narrow down by category, tag, or status

### ❌ Don'ts

- **Don't overwhelm**: If list is long, use filters
- **Don't guess**: If unsure, ask for more details about a competency
- **Don't ignore protocols**: Understanding protocols prevents surprises

## Common Questions During Listing

The skill may ask clarifying questions:

**Q**: "Are you looking for a specific type of task?"  
**A**: "Yes, I need something for documentation" or "No, just browsing"

**Q**: "What area are you interested in?"  
**A**: "Git operations" or "Project management" or "Just show me everything"

## Integration with Other Skills

After discovering competencies, you can:

1. **Execute directly**: `use competency: [name]`
2. **Get help**: `olaf help me` - For guided selection
3. **Read details**: Request full documentation for a competency

## Example Workflow

**Step 1**: List all competencies
```
list competencies
```

**Step 2**: Review the list and find interesting ones
```
Hmm, "assess-genai-initiative-idea" looks useful...
```

**Step 3**: Ask for more details
```
Tell me more about assess-genai-initiative-idea
```

**Step 4**: Execute the competency
```
assess genai initiative
```

## Advanced Usage

### Combining with Search

```
list competencies | grep "stash"
```

(Conceptually - shows how to think about filtering)

### Regular Review

Set a reminder to:
- Review new competencies monthly
- Check for deprecated items
- Learn about experimental features

### Custom Organization

You can mentally organize competencies by:
- **Purpose**: Project management, code analysis, utilities
- **Protocol**: Quick actions (Act) vs. interactive (Propose-Confirm-Act)
- **Frequency**: Daily use vs. occasional

## Troubleshooting

**Q**: The list is too long!  
**A**: Ask for filtering by category, tag, or use case

**Q**: I don't see a competency I need  
**A**: Check if it exists in skills or competencies folders manually, or request creation

**Q**: What does a protocol mean?  
**A**: Ask "Explain OLAF interaction protocols" for detailed information

**Q**: Can I add my own competencies to the list?  
**A**: Yes! Create a skill following the OLAF skill structure

## Related Skills

- `help-me-olaf`: Guided assistance in choosing the right competency
- `use-skill`: Execute a specific skill by name
- `query-competency-index`: Low-level access to the index file

## Command Aliases

All of these work the same:
- `list competencies`
- `list competency`
- `show competencies`
- `list olaf commands`
- `competency list`

Choose whichever feels natural!
