# tell-me

## Overview
Lightweight knowledge retrieval from existing artifacts with smart fallback to web fetch and analysis suggestions.

## Purpose
Quickly answer questions by searching local documentation first, fetching from official docs when needed, and suggesting analysis skills when no information exists.

## Key Features
- Search-first approach across local artifacts
- Persona-based QUICKSTART guide detection
- Smart web fetch for technology questions
- Suggests appropriate analysis skills when needed
- Cites all sources (local and web)

## Usage
```
@tell-me <your question>
```
Or invoke without a question to see example queries.

## Parameters
| Parameter | Required | Description |
|-----------|----------|-------------|
| question | Yes | Your question about the project |
| repository_name | No | Target repo (auto-detected) |

## Process Flow
1. Parses question and extracts keywords
2. Searches in priority order:
   - QUICKSTART guides in `.olaf/data/context/`
   - Knowledge base in `.olaf/data/kb/`
   - Practices in `.olaf/data/practices/`
   - Root documentation (README, CONTRIBUTING)
3. If not found, attempts web fetch for recognized technologies
4. If still not found, suggests appropriate analysis skill

## Output
- Answer synthesized from found sources
- Source citations (file paths or URLs)
- Suggestions for generating missing documentation

## Error Handling
| Scenario | Resolution |
|----------|------------|
| No question provided | Shows example questions by persona |
| No artifacts found | Suggests running onboard-me |
| Technology not in index | Infers official docs URL |

## Related Skills
- `onboard-me` - Generate QUICKSTART guides
- `search-and-learn` - Deep research capability
- `research-and-report` - Comprehensive research reports
