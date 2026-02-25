---
name: distill-docs-to-pptx
description: >
  Distill large or multiple markdown documentation files into a concise,
  professional PowerPoint presentation. Use when the user wants to present
  complex technical documentation without forcing the audience to read
  hundreds of lines of markdown. Not a comparison — a distillation.
license: MIT
compatibility: Requires Python 3.9+ and python-pptx package
metadata:
  author: olaf
  version: "1.0.0"
  tags: "pptx presentation documentation distill summarize slides"
---

# Distill Documentation to PPTX

## When to use this skill

Trigger phrases:
- "create a presentation from this documentation"
- "distill these docs into slides"
- "make a deck explaining this architecture"
- "summarize this design doc as a presentation"
- "I need slides to present this to the team"
- "turn this markdown into a PowerPoint"
- "people won't read all this — make slides"

## When NOT to use this skill

- If the user wants to compare items with numeric metrics, use
  `generate-comparison-pptx` instead.
- If the user wants a written summary (not slides), just summarize directly.

## Overview

This skill reads one or more markdown documentation files, extracts the
key concepts, and generates a professional dark-themed PPTX presentation
that communicates the essential information in 4-8 slides. The goal is
to save the audience from reading 200-800 lines of markdown while
retaining the critical content.

IMPORTANT: This "skill" is a **process/spec** that guides an agent (LLM) to:

- decide the slide set (count + structure)
- generate a dedicated `generate_pptx.py` for that presentation
- run it to produce a `.pptx`

The bundled `scripts/generate_pptx.py` is only a **starter template** and must remain generic.

## Prerequisites

```bash
pip install python-pptx
```

## Process

### Step 1 — Read and analyze the source documentation

Read all the markdown files the user points to. As you read, identify:

1. **Core purpose** — what is this thing and why does it exist?
2. **Key concepts** — the 3-6 most important ideas (architecture decisions,
   design patterns, workflows, components)
3. **Visual structures** — anything that maps well to diagrams, flows,
   grids, or cards (pipelines, phase lists, component inventories,
   decision trees)
4. **Numbers and facts** — concrete data points worth highlighting
   (counts, caps, limits, performance figures)
5. **Design principles** — recurring themes or explicit principles

### Step 2 — Plan the slide structure

Decide how many slides based on content density:

| Source size | Recommended slides | Rationale |
|-------------|-------------------|-----------|
| < 200 lines | 3-4 content slides | Light content, keep it tight |
| 200-500 lines | 4-5 content slides | Standard treatment |
| 500-1000 lines | 5-6 content slides | Rich content, needs space |
| 1000+ lines or multiple files | 6-8 content slides | Complex system, max density |

Always include (not counted above):
- Title slide (with intent, data source, AI-generated notice)

The first content slide should always be an **Executive Summary** that
gives the audience the key takeaway upfront.

**Slide type selection guide:**

| Content type | Best slide format |
|-------------|-------------------|
| Overview / what & why | 2-3 cards side by side (problem / solution / output) |
| Pipeline / workflow | Numbered phase boxes with arrows + detail cards below |
| Component inventory | Grid layout (3-4 columns × N rows) with colored dots |
| Quality / validation process | Side-by-side pass cards (what each pass does) |
| Configuration / injection | Cards for the chain + variable table |
| Metrics / operations | Feature cards + principle badges |
| Comparison data | Use `generate-comparison-pptx` skill instead |

### Step 3 — Generate the Python script

Create a Python script using the helper functions and design system
documented below (in the "Reference Script" section). All helpers must
be inlined in the generated script — no imports from external skill files.

IMPORTANT: The files under this skill folder are **templates**. They are **read-only**.
Do **NOT** edit or run:

- `c:\Users\ppaccaud\.agents\skills\distill-docs-to-pptx\scripts\generate_pptx.py`
- `c:\Users\ppaccaud\.agents\skills\distill-docs-to-pptx\scripts\template.pptx`

Instead, always generate a new presentation folder in the **repo workspace**:

```
<repo>/.olaf/work/presentations/<presentation-name>/
  generate_pptx.py
  template.pptx
  <presentation-name>.pptx
```

The bundled `generate_pptx.py` includes a runtime guard and will refuse to run unless it is located under `.olaf/work/presentations/<presentation-name>/`.

Mandatory script structure:

1. **Copy the bundled template** (`scripts/template.pptx`) into the output
   folder and set `TEMPLATE_PATH = Path(__file__).resolve().parent / "template.pptx"`
2. **Use layout helpers** for every slide:
   - Title slide: `prs.slides.add_slide(get_cover_layout(prs))` and
     populate placeholders (idx 0 = title, idx 13 = subtitle, idx 18 = footer)
   - Content slides: `prs.slides.add_slide(get_content_layout(prs))` and
     call `header(slide, title, subtitle)` which uses the placeholder
   - Sources/closing: `prs.slides.add_slide(get_closing_layout(prs))`
3. **Never use `prs.slide_layouts[N]`** — always use `get_*_layout()` helpers
4. **Never use `RGBColor(...)`** — always use `_apply_theme_color()` with
   `MSO_THEME_COLOR` constants
5. **Never use `Presentation()`** without the template — always use
   `Presentation(str(TEMPLATE_PATH))`

Key rules for distillation slides:

1. **One idea per slide** — if you're cramming two stories, split
2. **Cards over paragraphs** — use `card()` helper for grouped info
3. **Badges for inventories** — colored rounded rects in grids
4. **Phase flows** — numbered boxes with arrows for pipelines
5. **Insight boxes** — every content slide MUST end with a one-sentence
   takeaway in a tinted rect: `rect(slide, x, y, w, 0.55, ACCENT_*, -0.7, text=..., fc_theme=ACCENT_*)`
6. **Font sizes**: titles 28pt, card titles 16pt, body 13-14pt, minimum 11pt
7. **Max 6 bullet points per card** — beyond that, split or summarize

### Step 3.5 — Pre-run checklist

Before running the script, verify ALL of these:

- [ ] `TEMPLATE_PATH` points to the bundled `template.pptx` (NOT `None`)
- [ ] `template.pptx` has been copied to the output folder
- [ ] Title slide uses `get_cover_layout(prs)` and populates placeholders
- [ ] All content slides use `get_title_only_layout(prs)` + `header()`
- [ ] Sources slide uses `get_closing_layout(prs)`
- [ ] No `prs.slide_layouts[N]` anywhere in the script
- [ ] No `RGBColor(...)` anywhere in the script
- [ ] No `Presentation()` without the template path
- [ ] Every content slide has an insight box at the bottom
- [ ] All text uses `MSO_THEME_COLOR` (no hardcoded colors)

### Step 4 — Run the script

**IMPORTANT: Use simple, single commands only.**  
Do not use complex PowerShell blocks, nested logic, or multi-line scripts. Execute one command at a time to avoid permission prompts and failures.

Preferred pattern:
```bash
# 1. Change directory
cd "<path-to-presentation-folder>"

# 2. Run the Python script
python generate_pptx.py
```

The script must be executed from:

```
<repo>/.olaf/work/presentations/<presentation-name>/generate_pptx.py
```

By convention (and by default in the template), the PPTX output is:

```
<repo>/.olaf/work/presentations/<presentation-name>/<presentation-name>.pptx
```

Then open:
```bash
# Windows
Start-Process "<path-to-pptx>"
# macOS
open "<path-to-pptx>"
# Linux
xdg-open "<path-to-pptx>"
```

## Design System — Theme-Aware

All colors use PowerPoint theme slots (`MSO_THEME_COLOR`) instead of
hardcoded RGB values. This means the user can switch the theme in
PowerPoint (Design tab → Themes) and all colors adapt automatically,
making it easy to match any company's branding.

```python
from pptx.enum.dml import MSO_THEME_COLOR

# Semantic mapping:
# Slide background     → DARK_1
# Card background      → DARK_1 with brightness +0.15
# Primary text         → LIGHT_1
# Body text            → LIGHT_1 with brightness -0.25
# Subtitle/muted text  → LIGHT_2
# Primary accent       → ACCENT_1 (blue in default theme)
# Positive accent      → ACCENT_2 (green)
# AI/validation accent → ACCENT_3 (purple)
# Warning accent       → ACCENT_4 (orange)
# Danger accent        → ACCENT_5 (red)
# Info accent          → ACCENT_6 (teal)
```

Accent colors assigned by topic/section (not by compared items):
- ACCENT_1 for primary/structural concepts
- ACCENT_2 for positive/output/quality
- ACCENT_3 for validation/AI passes
- ACCENT_4 for warnings/configuration
- ACCENT_5 for problems/constraints
- ACCENT_6 for processing/operations

CRITICAL: Never use `RGBColor(...)` for slide content. Always use
`_apply_theme_color(color_format, MSO_THEME_COLOR.XXX, brightness)`
so colors follow the theme. Use `brightness` (-1.0 to 1.0) for
lighter/darker variants of the same theme slot.

Note: It's fine if the Python script imports helper types it doesn't end up using,
but the **generated** presentation content must never rely on hardcoded RGB values.

## Layout Resolution

Slide layouts are resolved **by name** from the template, not by hardcoded
index. This avoids breakage when the template's layout order changes.

Three layout roles:

| Role | Purpose | Name patterns (tried in order) |
|---------|----------------------------------------------|------------------------------------------------|
| cover | Title/cover slide (first slide) | `"cover slide"`, `"cover"`, `"title slide"` |
| title-only | Body slides with title placeholder only (REQUIRED for all non-cover slides) | `"title only"`, `"title-only"` |
| content | Body slides with title + content area (optional fallback in other templates) | `"title, subtitle and content"`, `"title and content"` |
| closing | Final/outro slide (sources, thank you) | `"closing"`, `"end"`, `"thank"` |

The resolver does a case-insensitive substring match against layout names.
If no match is found, it falls back to a layout index (0 for cover/closing,
1 for content).

CRITICAL rules for layout usage:

1. **Title slide** → use `get_cover_layout(prs)` and populate its
   placeholders (idx 0 = Title, others are template-specific)
2. **All non-cover slides** → use `get_title_only_layout(prs)` and call `header()`
   which populates the title placeholder automatically
3. **Never hardcode layout indices** like `prs.slide_layouts[6]` — always
   use the `get_*_layout()` helpers
4. **Always use placeholders for titles** — the `header()` helper finds
   placeholder idx 0 and sets its text, falling back to a floating text
   box only if no placeholder exists

If the template does not contain a matching **Title Only** layout, the
generator script fails fast with a clear error to prevent silent layout drift.

## Helper Functions

The reference script provides:

- `_find_layout(prs, name_patterns, fallback_index)` — find layout by name pattern
- `get_cover_layout(prs)` — get the cover/title slide layout
- `get_content_layout(prs)` — get the content slide layout
- `get_closing_layout(prs)` — get the closing/outro slide layout
- `set_bg(slide)` — **no-op**: background must be inherited from the template/layout.
- `txt(slide, l, t, w, h, text, sz, theme_color, brightness, bold, align)` — text box; theme_color=None means inherit
- `rect(slide, l, t, w, h, fill_theme, fill_brightness, text, ...)` — rounded rect; fc_theme=None means inherit
- `header(slide, title, subtitle)` — set title via placeholder (fallback to text box)
- `card(slide, l, t, w, h, title, lines, accent_theme, tsz, bsz)` — info card with accent bar
- `_apply_theme_color(color_format, theme_color, brightness)` — apply theme color to any element

All helpers are documented in the "Reference Script" section below.

## Text Grouping Rule

When multiple text lines belong together (e.g., bullet points in a card,
description lines, profile text), they MUST be rendered as paragraphs
within a single text frame — NOT as separate `txt()` calls. This produces
one editable text block in PowerPoint instead of many independent floating
text fields.

Pattern to follow:
```python
body_box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
tf = body_box.text_frame
tf.word_wrap = True
for i, line in enumerate(lines):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.text = line
    p.font.size = Pt(14)
    # Don't set font color — let it inherit from the theme
    p.font.name = "Segoe UI"
    p.space_after = Pt(4)
```

Use separate `txt()` only for truly independent text elements (titles,
subtitles, insight boxes) that are positioned in different areas of the
slide.

## Theme Color Inheritance Rule

To ensure presentations adapt when the user switches the PowerPoint theme
(Design tab), text and shape colors follow this rule:

- `None` / omit the color parameter = **inherit from theme** (auto-adapts
  to light or dark backgrounds). Use this for all body text, subtitles,
  axis labels, data labels, and any text that should be readable on any
  background.
- Explicit `MSO_THEME_COLOR.ACCENT_*` = use only on **accent-colored
  elements**: card title text, text inside colored shapes, insight box
  text, item badges. These are intentionally colored and should stay
  colored regardless of theme.

Never set `LIGHT_1` or `LIGHT_2` explicitly on text — these are white/gray
in dark themes but invisible on white backgrounds. Let PowerPoint handle
the text color through theme inheritance.

## Distillation Principles

1. **Audience-first**: The reader of the slides is NOT the author of the
   docs. Strip implementation details, keep concepts and decisions.
2. **Visual hierarchy**: Use cards, badges, and color to create scannable
   slides. No walls of text.
3. **Evidence preservation**: If the source doc has concrete numbers
   (line caps, token limits, retry counts), keep them — they build trust.
4. **Flow over detail**: Show the pipeline/workflow shape first, then
   drill into individual phases only if they're interesting.
5. **Insight boxes**: Every data-heavy slide should end with a one-line
   "so what?" takeaway in a tinted box.

## Slide Count & Content Density (authoritative)

The number of slides is decided during **script generation** (Step 3), not at runtime.
The template script is only an example.

Rules:

- Always keep **one idea per slide**
- If a card needs more than **6 bullets**, split into a new slide
- Prefer **shapes** (cards/flows/grids) over charts unless the docs contain real numeric series
- If the source docs are large or multi-file, increase slide count rather than shrinking font sizes

## Title Slide Requirements

Every presentation must include on the title slide:
- Clear statement of intent (what is this about)
- Data source reference (which doc(s) this was distilled from)
- "AI-generated presentation" notice with verification note

## Sources & References Slide

If the source documentation contains URLs or citations, extract them into
the `SOURCES` list in the generated script:

```python
SOURCES = [
    ("Kiro PBT documentation", "https://kiro.dev/docs/specs/correctness/"),
    ("Hypothesis library", "https://hypothesis.readthedocs.io/"),
]
```

A "Sources & References" slide is auto-generated at the end with clickable
hyperlinks. Each source shows the label as a blue underlined link, followed
by the URL in muted text. If `SOURCES` is empty, the slide is skipped.

When distilling markdown docs, scan for `[label](url)` patterns and extract
them into the SOURCES list.

## Template Support

CRITICAL: The generated script MUST ALWAYS use the bundled template.
A template is bundled with this skill at `scripts/template.pptx` (relative
to the skill folder). This template provides the dark theme, branded slide
masters, and proper layout placeholders that make presentations look
professional.

```python
# MANDATORY — always resolve to the bundled template
TEMPLATE_PATH = Path(__file__).resolve().parent / "template.pptx"
```

When generating the Python script, you MUST:
1. **Copy `template.pptx`** from the skill's `scripts/` folder into the
   output presentation folder (next to `generate_pptx.py`)
2. **Set `TEMPLATE_PATH`** to resolve relative to the script's location:
   `Path(__file__).resolve().parent / "template.pptx"`
3. **Never set `TEMPLATE_PATH = None`** — this produces an ugly blank
   presentation with no theme, no dark background, and no branded layouts

The presentation inherits the template's theme, slide master, and color
scheme. The user can then switch the theme in PowerPoint (Design tab)
and all colors adapt automatically.

The script should gracefully fall back to a blank presentation ONLY if
the template file is missing at runtime (e.g., deleted by the user).

## Document Properties

The script sets PowerPoint document properties (File → Info):
- Title: from the `TITLE` constant
- Subject: from the `INTENT` constant
- Comments: skill attribution

## Output Location

Both output files (the generator script and the PPTX) MUST be saved under:

```
.olaf/work/presentations/<presentation-name>/
```

The `<presentation-name>` folder is derived from the context — typically
the topic or source document name, in kebab-case.

Examples:
- Distilling `docs/architecture.md` → save to
  `.olaf/work/presentations/architecture/generate_pptx.py` and
  `.olaf/work/presentations/architecture/architecture.pptx`
- Distilling `agentic/straf-cli/docs/documentor-architecture.md` → save to
  `.olaf/work/presentations/documentor-architecture/generate_pptx.py` and
  `.olaf/work/presentations/documentor-architecture/documentor-architecture.pptx`

If the user explicitly requests a different location, use that instead.

Naming convention:
- Script: `generate_pptx.py` (inside the presentation folder)
- PPTX: `<presentation-name>.pptx`

## Output

1. A Python script (saved alongside the source docs for reproducibility)
2. A `.pptx` file with native editable shapes and text (no images)

## Example: Architecture doc → 6 slides

Source: `documentor-architecture.md` (759 lines, 14 sections)

| Slide | Title | Content |
|-------|-------|---------|
| Title | Documentor | Intent + tech badges + AI notice |
| 1 | Executive Summary | Problem / Solution / Output cards + principles |
| 2 | The 11-Phase Pipeline | Phase flow boxes + design decision cards |
| 3 | 12 Technology Profiles | Grid of profiles + fallback chain explanation |
| 4 | 3-Pass Quality System | Validation / Verification / Fix cards |
| 5 | Agent Context Injection | Injection chain + variables + model config |
| 6 | Bulk Execution & Metrics | Features + tracking + logging + principles |


## Reference Script — Complete Helper Library

The following is the complete reference implementation. When generating a
script for the user, copy the helpers you need and replace the DATA SECTION
with content extracted from the user's documentation. The script must be
fully self-contained — no imports from external skill files.

```python
#!/usr/bin/env python3
"""
Documentation Distillation PPTX Generator
==========================================
Generates a professional PowerPoint presentation that distills large markdown
documentation into concise, visual slides.

THEME-AWARE: All colors use PowerPoint theme slots so the user can switch
the theme in PowerPoint and all colors adapt automatically.

LAYOUT-AWARE: Slide layouts are resolved by name from the template, not by
hardcoded index. Titles are populated via the layout's built-in placeholders.

Requirements: pip install python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pathlib import Path


# ── Theme color semantic names ──
ACCENT_PRIMARY   = MSO_THEME_COLOR.ACCENT_1   # Blue / structural
ACCENT_POSITIVE  = MSO_THEME_COLOR.ACCENT_2   # Green / output / quality
ACCENT_AI        = MSO_THEME_COLOR.ACCENT_3   # Purple / validation
ACCENT_WARNING   = MSO_THEME_COLOR.ACCENT_4   # Orange / config
ACCENT_DANGER    = MSO_THEME_COLOR.ACCENT_5   # Red / problems
ACCENT_INFO      = MSO_THEME_COLOR.ACCENT_6   # Teal / processing


# ── Layout resolution ──
# Layouts are resolved by name (case-insensitive substring match).
# Customize these patterns if your template uses different naming.
LAYOUT_COVER_NAMES = ["cover", "title slide"]
LAYOUT_CONTENT_NAMES = ["title, subtitle and content", "title and content", "title only"]
LAYOUT_CLOSING_NAMES = ["closing", "end", "thank"]


def _find_layout(prs, name_patterns, fallback_index=0):
    """Find a slide layout by name pattern (case-insensitive substring match).
    Tries each pattern in order and returns the first matching layout.
    Falls back to the given index if no name matches.
    """
    for pattern in name_patterns:
        for layout in prs.slide_layouts:
            if pattern.lower() in layout.name.lower():
                return layout
    if fallback_index < len(prs.slide_layouts):
        return prs.slide_layouts[fallback_index]
    return prs.slide_layouts[0]


def get_cover_layout(prs):
    """Get the cover/title slide layout."""
    return _find_layout(prs, LAYOUT_COVER_NAMES, fallback_index=0)


def get_content_layout(prs):
    """Get the content slide layout (title + content area)."""
    return _find_layout(prs, LAYOUT_CONTENT_NAMES, fallback_index=1)


def get_closing_layout(prs):
    """Get the closing/outro slide layout."""
    return _find_layout(prs, LAYOUT_CLOSING_NAMES, fallback_index=0)


# ── Helpers ──

def _apply_theme_color(color_format, theme_color, brightness=0.0):
    """Apply a theme color with optional brightness adjustment."""
    color_format.theme_color = theme_color
    if brightness != 0.0:
        color_format.brightness = brightness


def set_bg(slide):
    """No-op: let the slide inherit its background from the slide master/layout."""
    pass


def txt(slide, l, t, w, h, text, sz=14, theme_color=MSO_THEME_COLOR.LIGHT_1,
        brightness=0.0, bold=False, align=PP_ALIGN.LEFT):
    """Add a positioned text box."""
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(sz)
    if theme_color is not None:
        _apply_theme_color(p.font.color, theme_color, brightness)
    p.font.bold = bold
    p.font.name = "Segoe UI"
    p.alignment = align
    return box


def rect(slide, l, t, w, h, fill_theme, fill_brightness=0.0,
         text="", sz=14, fc_theme=MSO_THEME_COLOR.LIGHT_1, fc_brightness=0.0,
         bold=False):
    """Add a rounded rectangle."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                   Inches(l), Inches(t), Inches(w), Inches(h))
    shape.fill.solid()
    _apply_theme_color(shape.fill.fore_color, fill_theme, fill_brightness)
    shape.line.fill.background()
    if text:
        tf = shape.text_frame
        tf.word_wrap = True
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(sz)
        if fc_theme is not None:
            _apply_theme_color(p.font.color, fc_theme, fc_brightness)
        p.font.bold = bold
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return shape


def header(slide, title, subtitle=""):
    """Set the slide title via the layout's title placeholder.
    Falls back to a floating text box if no title placeholder exists.
    Subtitle is always a floating text box positioned below the title.
    """
    set_bg(slide)
    # Try to use the layout's title placeholder (idx 0)
    title_set = False
    if slide.placeholders:
        for ph in slide.placeholders:
            if ph.placeholder_format.idx == 0:  # Title placeholder
                ph.text = title
                title_set = True
                break
    if not title_set:
        txt(slide, 0.5, 0.3, 12, 0.6, title, sz=28, bold=True)
    if subtitle:
        txt(slide, 0.5, 0.85, 12, 0.4, subtitle, sz=14)


def card(slide, l, t, w, h, title, lines, accent_theme, tsz=16, bsz=14):
    """Add an info card with accent top border and bullet lines."""
    bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(l), Inches(t), Inches(w), Inches(h))
    bg.fill.background()
    bg.line.width = Pt(1.5)
    _apply_theme_color(bg.line.color, accent_theme)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(l + 0.05), Inches(t + 0.05),
                                 Inches(w - 0.1), Inches(0.06))
    bar.fill.solid()
    _apply_theme_color(bar.fill.fore_color, accent_theme)
    bar.line.fill.background()
    txt(slide, l + 0.15, t + 0.18, w - 0.3, 0.35, title,
        sz=tsz, theme_color=accent_theme, bold=True)
    body_box = slide.shapes.add_textbox(
        Inches(l + 0.15), Inches(t + 0.55),
        Inches(w - 0.3), Inches(h - 0.7))
    tf = body_box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(bsz)
        _apply_theme_color(p.font.color, MSO_THEME_COLOR.LIGHT_1, -0.25)
        p.font.name = "Segoe UI"
        p.space_after = Pt(4)


def phase_flow(slide, phases, y_top=1.5):
    """Draw a horizontal flow of numbered phase boxes with arrows."""
    x = 0.3
    for num, name, desc, clr in phases:
        rect(slide, x, y_top, 1.1, 0.5, clr, text=num, sz=16, bold=True)
        txt(slide, x, y_top + 0.55, 1.1, 0.35, name,
            sz=11, bold=True, align=PP_ALIGN.CENTER)
        txt(slide, x, y_top + 0.9, 1.1, 0.6, desc,
            sz=9, align=PP_ALIGN.CENTER)
        if num != phases[-1][0]:
            txt(slide, x + 1.05, y_top + 0.05, 0.15, 0.4, "→",
                sz=16, align=PP_ALIGN.CENTER)
        x += 1.18


def grid_items(slide, items, y_start=1.5, cols=4):
    """Draw a grid of labeled items with colored accent dots.

    Each cell uses a dark-tinted accent fill so text remains readable on
    both light and dark themes.  Name and subtitle are grouped into a
    single text frame for easy editing in PowerPoint.
    """
    col_w = 3.0
    row_h = 0.9
    for i, (name, sub, clr) in enumerate(items):
        col = i % cols
        row = i // cols
        x = 0.5 + col * 3.2
        y = y_start + row * 1.1
        rect(slide, x, y, col_w, row_h, clr, 0.15)
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                                      Inches(x + 0.12), Inches(y + 0.18),
                                      Inches(0.22), Inches(0.22))
        dot.fill.solid()
        _apply_theme_color(dot.fill.fore_color, clr)
        dot.line.fill.background()
        body = slide.shapes.add_textbox(
            Inches(x + 0.45), Inches(y + 0.1),
            Inches(col_w - 0.6), Inches(row_h - 0.2))
        tf = body.text_frame
        tf.word_wrap = True
        p_name = tf.paragraphs[0]
        p_name.text = name
        p_name.font.size = Pt(14)
        p_name.font.bold = True
        p_name.font.name = "Segoe UI"
        _apply_theme_color(p_name.font.color, MSO_THEME_COLOR.LIGHT_1)
        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(12)
        p_sub.font.name = "Segoe UI"
        _apply_theme_color(p_sub.font.color, MSO_THEME_COLOR.LIGHT_1, -0.25)
        p_sub.space_before = Pt(2)


def badge_row(slide, badges, y=5.0):
    """Draw a horizontal row of principle/feature badges."""
    n = len(badges)
    total_w = n * 2.1
    x = (13.333 - total_w) / 2
    for label, desc, clr in badges:
        rect(slide, x, y, 2.0, 0.45, clr, text=label, sz=10, bold=True)
        txt(slide, x, y + 0.5, 2.0, 0.35, desc, sz=10,
            align=PP_ALIGN.CENTER)
        x += 2.1


def build_sources_slide(prs, sources):
    """Final slide: Sources & References with clickable hyperlinks."""
    if not sources:
        return
    slide = prs.slides.add_slide(get_closing_layout(prs))
    header(slide, "Sources & References")
    body = slide.shapes.add_textbox(
        Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.5))
    tf = body.text_frame
    tf.word_wrap = True
    for i, (label, url) in enumerate(sources):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        run_bullet = p.add_run()
        run_bullet.text = "• "
        run_bullet.font.size = Pt(14)
        _apply_theme_color(run_bullet.font.color, MSO_THEME_COLOR.LIGHT_1, -0.25)
        run_bullet.font.name = "Segoe UI"
        run_link = p.add_run()
        run_link.text = label
        run_link.font.size = Pt(14)
        run_link.font.name = "Segoe UI"
        _apply_theme_color(run_link.font.color, MSO_THEME_COLOR.HYPERLINK)
        run_link.font.underline = True
        run_link.hyperlink.address = url
        run_url = p.add_run()
        run_url.text = f"  ({url})"
        run_url.font.size = Pt(10)
        run_url.font.name = "Segoe UI"
        _apply_theme_color(run_url.font.color, MSO_THEME_COLOR.LIGHT_2)


# ── DATA SECTION — replace with content from your docs ──

TITLE = "System Name"
INTENT = "One-sentence description"
SOURCE = "Data: distilled from system-architecture.md"
AI_NOTICE = "AI-generated presentation — content verified by author"
SOURCES = []
TEMPLATE_PATH = Path(__file__).resolve().parent / "template.pptx"  # MANDATORY
OUTPUT_PATH = Path("distilled-overview.pptx")


# ── MAIN ──

def main():
    if TEMPLATE_PATH and Path(TEMPLATE_PATH).exists():
        prs = Presentation(str(TEMPLATE_PATH))
    else:
        prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # ── Title slide ──
    slide = prs.slides.add_slide(get_cover_layout(prs))
    set_bg(slide)
    for ph in slide.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:   ph.text = TITLE
        elif idx == 13: ph.text = INTENT
        elif idx == 18: ph.text = f"{SOURCE}\n{AI_NOTICE}"

    # ── Content slides ──
    # slide = prs.slides.add_slide(get_title_only_layout(prs))
    # header(slide, "Slide Title")
    # card(slide, 0.5, 1.4, 5.8, 2.8, "Card Title", ["line1", "line2"], ACCENT_PRIMARY)
    # rect(slide, 1.5, 4.5, 10.3, 0.55, ACCENT_PRIMARY, -0.7,
    #      text="Insight takeaway", sz=14, fc_theme=ACCENT_POSITIVE)

    # ── Sources slide ──
    build_sources_slide(prs, SOURCES)

    prs.core_properties.title = TITLE
    prs.core_properties.subject = INTENT
    prs.core_properties.comments = "Generated by distill-docs-to-pptx skill"
    prs.save(str(OUTPUT_PATH))
    print(f"✅ Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
```
