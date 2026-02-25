---
name: clean-srt-transcript
description: Transform messy subtitle files into clean, readable transcripts by removing filler words, fixing grammar, and joining broken sentences while preserving the original conversational flow.
license: Apache-2.0
metadata:
  olaf_tags: [srt, subtitle, transcript, english, cleanup]
  argument-hint: "[path to .srt file] - clean SRT transcript to proper US English"
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

## What This Skill Does

This skill converts **subtitle files (.srt)** into **clean, readable transcripts** perfect for:

📝 **Documentation** - Turn video subtitles into clean text for manuals  
🎓 **Learning Materials** - Create readable transcripts from educational content  
💼 **Meeting Records** - Clean up recorded meeting subtitles  
📚 **Content Creation** - Extract clean text from video content for articles  

### Key Transformations:
- ✅ **Removes SRT metadata** (timestamps, sequence numbers)
- ✅ **Joins broken sentences** that span multiple subtitle blocks
- ✅ **Eliminates filler words** ("um", "uh", "you know", "like")
- ✅ **Fixes grammar errors** while preserving natural speech
- ✅ **Maintains conversational flow** and original meaning
- ✅ **Outputs clean text** ready for editing or publication

---

## Quick Start Example

**Input SRT file:**
```
1
00:01:23,456 --> 00:01:25,789
So, um, basically what we have here is,
you know, like, a really important feature.

2
00:01:26,012 --> 00:01:28,345
And it allows to create, like, multiple
documents at the same time.
```

**Output clean text:**
```
What we have here is a really important feature.
It allows you to create multiple documents at the same time.
```

---

## Input Parameters
You MUST request these parameters if not provided by the user:
- **srt_file**: string - Full path to the .srt subtitle file (REQUIRED)
- **output_file**: string - Full path for the cleaned text output (OPTIONAL — defaults to same directory/name as input with .txt extension)
- **target_language**: string - Target language variant (OPTIONAL — defaults to "US English")

## User Interaction
- You MUST ask for the SRT file path if not provided
- You MUST present the cleaned text to the user for review before saving
- You MUST ask for user approval before overwriting any existing file

---

## Common Use Cases

### 🎥 **Video Content Creators**
- **YouTube/TikTok scripts** - Clean up auto-generated subtitles for better readability
- **Tutorial transcripts** - Create written versions of video tutorials
- **Interview transcripts** - Clean up spoken interviews for articles

### 👥 **Business & Education**
- **Meeting minutes** - Transform recorded meeting subtitles into clean notes
- **Lecture transcripts** - Create readable versions of educational content
- **Training materials** - Convert video training to text documentation

### 📖 **Content Repurposing**
- **Blog posts** - Turn video content into written articles
- **Social media** - Extract quotes and key points from videos
- **Research notes** - Clean up interview or focus group transcripts

---

## Benefits Over Manual Cleaning

| Manual Cleaning | This Skill |
|-----------------|------------|
| ⏰ **Time-consuming** (hours per file) | ⚡ **Fast** (seconds per file) |
| 🤯 **Inconsistent** results | ✅ **Consistent** quality every time |
| 😫 **Tedious** filler word removal | 🎯 **Systematic** cleanup rules |
| 📝 **Error-prone** manual editing | 🛡️ **Reliable** automated process |
| 🔄 **Hard to maintain** flow | 💬 **Preserves** natural conversation |

---

## What Gets Cleaned Up

### ❌ **Removed Items:**
- SRT timestamps and sequence numbers
- Filler words: "um", "uh", "like", "you know"
- Leading "So" and "And" at sentence starts
- Stuttering and word repetitions
- Standalone filler lines ("Right.", "Uh.")

### ✅ **Fixed Issues:**
- Grammar errors and subject-verb agreement
- Missing articles and prepositions
- Broken sentences across subtitle blocks
- Inconsistent pronoun references
- Plural/singular mismatches

### 🎯 **Preserved Elements:**
- Original meaning and intent
- Conversational tone and flow
- Technical terms and proper nouns
- Speaker's unique voice patterns
- Content length and structure

## Process

### 1. Validation Phase
You MUST verify all requirements:
- Confirm the SRT file exists and is readable
- Confirm the file has `.srt` extension or valid SRT structure
- Determine output file path (use input path with `.txt` extension if not specified)

### 2. SRT Parsing Phase
You MUST read the full SRT file and extract text content:

**Strip SRT metadata:**
- Remove all sequence numbers (lines containing only digits like `1`, `2`, `3`)
- Remove all timestamp lines (lines matching pattern `HH:MM:SS,mmm --> HH:MM:SS,mmm`)
- Remove all blank separator lines
- Keep only the subtitle text lines

**Join multi-line sentences:**
- If a subtitle text spans multiple consecutive lines (no blank line between them), join them into a single sentence
- If a sentence is split across two consecutive subtitle blocks (e.g., block ends mid-sentence without punctuation and next block continues), join them into one sentence
- Use punctuation cues (period, question mark, exclamation mark) to detect sentence boundaries

### 3. Text Cleanup Phase
You MUST rephrase the extracted text to proper US English while preserving the original conversational flow and tempo:

**Remove filler words and hesitation marks:**
- Remove leading "So" at the start of sentences (e.g., "So I have one..." → "I have one...")
- Remove leading "And" at the start of sentences (e.g., "And basically..." → "Basically...")
- Remove "you know" interjections (e.g., "because, you know, it's..." → "because it's...")
- Remove "like" used as filler (e.g., "which means like basically" → "which basically means")
- Remove "basically" when redundant (keep if it adds meaning)
- Remove stuttering and repeated words (e.g., "the, the, the, the plan" → "the plan")
- Remove standalone filler lines like "Right." or "Uh." or "Um."

**Fix grammar and clarity:**
- Fix subject-verb agreement (e.g., "what that do" → "what that does")
- Fix missing articles and prepositions (e.g., "allows to create" → "allows you to create")
- Use consistent pronoun references (e.g., when referring to an AI tool, use "it" not "he/him")
- Fix plural/singular consistency (e.g., "that kind of things" → "that kind of thing")
- Correct obvious transcription errors

**Preserve the original flow:**
- You MUST NOT summarize, condense, or reduce the content
- You MUST NOT expand or add new content
- You MUST keep the same conversational tone and tempo
- You MUST keep the same approximate length — sentence count should remain similar
- You MUST preserve the speaker's intent and meaning exactly
- Vary repeated words where natural (e.g., alternate "presentation" with "deck", "slides")

### 4. Output Generation Phase
You MUST generate the output as a plain text file:
- One sentence per line where practical
- Blank lines between logical paragraph breaks
- UTF-8 encoding
- No SRT metadata, no timestamps, no sequence numbers

### 5. Review Phase
You WILL present the cleaned text to the user:
- Show the full cleaned text for review
- Highlight significant changes if any sentence meaning was altered
- Ask for user approval before saving

## Output Format
**Primary deliverable**: A clean `.txt` file containing the rephrased transcript text.

**OUTPUT LOCATION**: The output file WILL be saved to the `output_file` path. If not specified, it defaults to the same directory and filename as the input with a `.txt` extension.

## User Communication

### Progress Updates
- Confirmation when SRT file is read and parsed
- Number of subtitle blocks found
- Number of text lines extracted
- Draft presented for user review

### Completion Summary
- Summary of changes made (fillers removed, sentences joined, grammar fixes)
- Location of the saved output file
- Line count comparison (original subtitle lines vs cleaned text lines)

### Next Steps
You WILL suggest:
- Review the cleaned text and make any manual adjustments
- Use the text for captions, documentation, or further editing

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: You MUST NOT change the meaning of any sentence
- Rule 2: You MUST NOT summarize, condense, or reduce content length
- Rule 3: You MUST NOT expand or add content that was not in the original
- Rule 4: You MUST preserve the conversational tone — this is spoken language, not formal writing
- Rule 5: You MUST join sentences that were split across subtitle blocks into single coherent sentences
- Rule 6: You MUST remove ALL leading "So" and "And" filler words at sentence starts
- Rule 7: You MUST remove ALL "you know" interjections
- Rule 8: You MUST remove stuttering and word repetitions
- Rule 9: You MUST fix grammar errors while keeping natural speech patterns
- Rule 10: Output MUST be plain text with no SRT formatting artifacts

## Success Criteria
You WILL consider the task complete when:
- [ ] SRT file successfully read and parsed
- [ ] All SRT metadata (numbers, timestamps) stripped
- [ ] Multi-line sentences joined into single lines
- [ ] All filler words and hesitation marks removed
- [ ] Grammar corrected to proper US English
- [ ] Conversational flow and tempo preserved
- [ ] Content not summarized or expanded
- [ ] User reviewed and approved the output
- [ ] Clean text file saved to specified location

## Error Handling
You WILL handle these scenarios:
- **File not found**: Ask user to verify the file path
- **Invalid SRT format**: Inform user the file doesn't appear to be a valid SRT file, attempt best-effort parsing
- **Empty SRT file**: Inform user the file contains no subtitle text
- **Encoding issues**: Try UTF-8, then fall back to system default encoding
- **Output file exists**: Ask user before overwriting
- **User rejects draft**: Ask for specific feedback and regenerate the cleaned text

---

## 💡 Tips & Best Practices

### 📁 **File Organization**
- Keep original SRT files until you're satisfied with the cleaned version
- Use descriptive names: `interview-john-doe-2024.srt` → `interview-john-doe-2024.txt`
- Consider organizing by date, project, or speaker

### 🔍 **Quality Check**
After cleaning, review for:
- **Technical accuracy** - Are specialized terms correct?
- **Context preservation** - Does the meaning match the original?
- **Readability** - Is it easy to understand for your intended audience?

### 🚀 **Advanced Usage**
- **Batch processing**: Process multiple SRT files from the same video series
- **Content analysis**: Use cleaned text for keyword extraction or summarization
- **Translation prep**: Clean transcripts are better starting points for translation

### ⚠️ **Limitations to Note**
- **Heavy accents** may have transcription errors that need manual review
- **Technical jargon** might be misinterpreted - verify specialized terms
- **Multiple speakers** - Consider adding speaker identification if needed
- **Cultural context** - Some colloquialisms may need cultural adaptation

---

## 🎯 Success Stories

This skill is perfect for:
- **Academic researchers** cleaning interview transcripts
- **Content creators** repurposing video content
- **Business analysts** documenting meeting discussions
- **Educators** creating accessible learning materials
- **Journalists** preparing interview content for publication

**Result**: Professional-quality transcripts that save hours of manual editing while maintaining authentic voice and meaning!
