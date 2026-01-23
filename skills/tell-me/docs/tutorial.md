# Tutorial: tell-me

## Introduction
Get quick answers about your project by searching existing documentation and knowledge bases.

## Prerequisites
- Ideally, run `onboard-me` first to generate QUICKSTART guides
- Or have existing documentation in `.olaf/data/`

## Step-by-Step Instructions

### Step 1: Ask a Question
```
@tell-me how do I build this project?
```

### Step 2: Review the Answer
The skill searches local artifacts and returns:
- Synthesized answer from found documentation
- Source file citations with line numbers

### Step 3: Follow Up
Ask additional questions or run suggested skills if documentation is missing.

## Example Questions by Role

**Developers:**
- How do I build this project locally?
- How do I run tests?
- What frameworks are used?

**Architects:**
- What architectural pattern is used?
- What are the main components?

**DevOps:**
- How is this deployed?
- What's the CI/CD setup?

## Verification Checklist
- [ ] Question was understood correctly
- [ ] Sources are cited in the answer
- [ ] Answer addresses your question

## Troubleshooting

### "No documentation found"
Run `@onboard-me` to generate QUICKSTART guides for your repository.

### Answer from wrong repository
Specify the repository name explicitly in your question.

### Technology question not answered
The skill will attempt to fetch from official documentation. If that fails, search manually.

## Next Steps
- Generate missing docs with `onboard-me`
- Use `search-and-learn` for deeper research
- Create custom KB entries for frequently asked questions
