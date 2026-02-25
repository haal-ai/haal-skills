# clean-srt-transcript

## Overview
Reads an SRT subtitle file (e.g., from ClipChamp, OBS, or any video editor), extracts the spoken text, and rewrites it in proper US English. Removes filler words, hesitation marks, stuttering, and fixes grammar — while preserving the original conversational flow and tempo.

## What It Does
1. **Parses SRT** — Strips sequence numbers, timestamps, and blank lines
2. **Joins split sentences** — Reconnects sentences broken across subtitle blocks
3. **Removes fillers** — Eliminates "So", "And", "you know", "like", stuttering, and standalone filler lines
4. **Fixes grammar** — Corrects subject-verb agreement, pronouns, articles, and plurals
5. **Preserves flow** — Keeps the same length, tone, and conversational rhythm — no summarizing or expanding

## When to Use
- You recorded a video/screencast and need clean captions or a transcript
- You have auto-generated subtitles that need language cleanup
- You want to turn spoken narration into readable text without losing the speaker's voice

## Input
- Path to an `.srt` file

## Output
- A clean `.txt` file with proper US English text, one sentence per line

## Example Usage
```
Clean this SRT file: C:\Users\me\Downloads\recording.srt
```
