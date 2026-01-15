# Measure AI Impact

## Overview
Measure the impact of AI-assisted development on code quality and team productivity.

## Quick Start

### Detect AI in Specific Files
```
@olaf measure-ai-impact mode:file-analysis files:["src/auth.py", "src/validator.py"]
```

### Track Quarterly Productivity
```
@olaf measure-ai-impact mode:quarterly-trends since:"2024-01-01"
```

### Create Baseline Snapshot
```
@olaf measure-ai-impact mode:snapshot name:"baseline-pre-ai"
```

## Capabilities

- **File-Level AI Detection**: Identify AI-assisted code improvements via Halstead metrics
- **Quarterly Trend Analysis**: Track team productivity patterns over time
- **Baseline Comparison**: Create snapshots for accurate before/after measurement

## Documentation

- **[Full Description](docs/description.md)** - Complete skill documentation
- **[Tutorial](docs/tutorial.md)** - Step-by-step examples
- **[Skill Manifest](skill-manifest.json)** - Technical metadata

## Output

Reports saved to: `olaf-data/ai-impact/`

## Requirements

- Python 3.10+
- Git repository
- Radon library (optional): `pip install radon`

---

**Version**: 1.0.0 | **Protocol**: Act | **Status**: Active
