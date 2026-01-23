# Tutorial: Review Document for Jargon

## Basic Usage

Provide your document content and ask for a jargon review:

```
Review this document for jargon:

{{DOCUMENT}}
We need to punt on the Q3 deliverables and circle back after we've 
moved the goalposts on our OKRs. Let's get boots on the ground and 
find some low-hanging fruit before we boil the ocean.
```

## Example Output

### Jargon Found

| Original | Category | Issue | Suggested Replacement |
|----------|----------|-------|----------------------|
| punt | Sports | American football term for delaying | postpone, delay |
| circle back | Corporate | Vague business speak | revisit, discuss again |
| moved the goalposts | Sports | Changed success criteria | adjusted our targets |
| OKRs | Acronym | Undefined | objectives and key results (OKRs) |
| boots on the ground | Military | Physical presence metaphor | people working directly on this |
| low-hanging fruit | Corporate | Easy wins metaphor | quick wins, easy tasks |
| boil the ocean | Corporate | Attempting too much | take on too much |

### Revised Document

We need to **postpone** the Q3 deliverables and **revisit this** after we've 
**adjusted our targets** on our **objectives and key results (OKRs)**. Let's get 
**people working directly on this** and find some **quick wins** before we 
**take on too much**.

## Tips

- For technical documents, specify if certain jargon should be preserved
- Mention your target audience for better suggestions
- Use with style guides for consistent terminology
