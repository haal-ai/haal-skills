from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SkillDocs:
    skill_id: str
    description_src: Path | None
    tutorial_src: Path | None


def _is_skill_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    if path.name.startswith(('.', '_')):
        return False
    return (path / 'skill.md').is_file()


def _collect_skill_docs(repo_root: Path) -> list[SkillDocs]:
    skills: list[SkillDocs] = []

    for child in sorted(repo_root.iterdir(), key=lambda p: p.name.lower()):
        if not _is_skill_dir(child):
            continue

        docs_dir = child / 'docs'
        description = docs_dir / 'description.md'
        tutorial = docs_dir / 'tutorial.md'

        skills.append(
            SkillDocs(
                skill_id=child.name,
                description_src=description if description.is_file() else None,
                tutorial_src=tutorial if tutorial.is_file() else None,
            )
        )

    return skills


def _safe_copy(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def build_docs_site(repo_root: Path) -> None:
    docs_root = repo_root / 'docs'
    if not docs_root.is_dir():
        raise RuntimeError(f"Expected docs directory at: {docs_root}")

    generated_root = docs_root / 'skills'
    generated_root.mkdir(parents=True, exist_ok=True)

    skills = _collect_skill_docs(repo_root)

    # Copy per-skill docs
    for skill in skills:
        dest_dir = generated_root / skill.skill_id

        if skill.description_src is not None:
            _safe_copy(skill.description_src, dest_dir / 'description.md')

        if skill.tutorial_src is not None:
            _safe_copy(skill.tutorial_src, dest_dir / 'tutorial.md')

    # Generate skills index
    lines: list[str] = []
    lines.append('# Skills')
    lines.append('')
    lines.append('Browse skill documentation (generated from each `/<skill>/docs/` folder).')
    lines.append('')

    published = [
        s
        for s in skills
        if (s.description_src is not None) or (s.tutorial_src is not None)
    ]

    if not published:
        lines.append('No skill docs found.')
        lines.append('')
    else:
        for s in published:
            parts: list[str] = []
            if s.description_src is not None:
                parts.append(f"[Description](./{s.skill_id}/description.md)")
            if s.tutorial_src is not None:
                parts.append(f"[Tutorial](./{s.skill_id}/tutorial.md)")

            links = ' | '.join(parts)
            lines.append(f"- **{s.skill_id}** — {links}")

        lines.append('')
        lines.append(f"Total published skills: {len(published)}")
        lines.append('')

    (generated_root / 'index.md').write_text('\n'.join(lines), encoding='utf-8')


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    build_docs_site(repo_root)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
