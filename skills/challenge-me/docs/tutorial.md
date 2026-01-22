# Tutorial: challenge-me

## Introduction
Refine your ideas through structured challenge cycles with research-backed insights.

## Prerequisites
- A clear idea or concept to explore
- Your initial position or thoughts on the topic

## Step-by-Step Instructions

### Step 1: Invoke the Skill
```
@challenge-me
```

### Step 2: Provide Parameters
Answer the numbered questions:
1. Your idea/topic
2. Your current position
3. Challenge intensity (gentle/moderate/rigorous)
4. Research URLs (optional)
5. Focus areas (optional)
6. Save deliverables? (true/false)

### Step 3: Engage with Challenges
Each cycle presents:
- Numbered challenges (1, 2, 3, 4)
- Lettered clarifying questions (A, B, C, D)
- Research citations when applicable

Respond to refine your thinking.

### Step 4: Continue or End
After each cycle:
- Continue for another round
- Say "stop" to end without saving
- Say "save" to end and generate files

### Step 5: Review Deliverables
If saved, find files in:
`.olaf/work/staging/challenge-me/[session-id]/`

## Verification Checklist
- [ ] Session initialized with identifier
- [ ] Challenges match selected intensity
- [ ] Research sources cited properly
- [ ] Deliverables generated (if requested)

## Troubleshooting

### Challenges too harsh/soft
Adjust `challenge_intensity` parameter at session start.

### Missing research insights
Ensure provided URLs are accessible and relevant.

## Next Steps
- Review generated recommendations in `reco.md`
- Use insights to refine your implementation plan
