# Tutorial: create-prompt

## Introduction
Create a well-structured OLAF prompt file from your informal idea.

## Prerequisites
- Clear idea of what you want the prompt to accomplish
- Write access to `.olaf/staging/generated-prompts/`

## Step-by-Step Instructions

### Step 1: Invoke the Skill
```
@create-prompt
```

### Step 2: Provide Your Request
Answer the numbered questions:
1. What should the prompt do? (required)
2. Who will use it?
3. What context should it assume?
4. Any constraints?
5. Suggested name?
6. Tags?

### Step 3: Review the Rewritten Version
The skill rewrites your request into clear English. Respond:
- **yes** - Accept and continue
- **no** - Cancel
- **edit** - Request changes

### Step 4: Review Generated Prompt
Full prompt content is displayed. Respond:
- **yes** - Save the file
- **no** - Cancel
- **edit** - Request modifications

### Step 5: Confirm Save Location
File saves to `.olaf/staging/generated-prompts/{timestamp}-{name}.md`

## Verification Checklist
- [ ] Request was rewritten clearly
- [ ] Generated prompt follows template structure
- [ ] File saved with correct naming convention
- [ ] Tags and metadata are appropriate

## Troubleshooting

### Prompt doesn't capture intent
Use the "edit" option to refine the rewritten version before generation.

### File save fails
Check write permissions on `.olaf/staging/generated-prompts/`

## Next Steps
- Test your prompt in a conversation
- Use `evaluate-prompt-for-adoption` to assess quality
- Convert to a skill with `convert-prompt-to-skill`
