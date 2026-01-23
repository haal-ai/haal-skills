from __future__ import annotations

import json
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

    skills_dir = repo_root / 'skills'
    if not skills_dir.is_dir():
        return skills

    for child in sorted(skills_dir.iterdir(), key=lambda p: p.name.lower()):
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


def _parse_verified_skills(verified_skills_txt: str) -> list[tuple[str, str | None]]:
    items: list[tuple[str, str | None]] = []
    for raw_line in verified_skills_txt.splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue

        note: str | None = None
        if '(' in line and line.endswith(')'):
            before, after = line.split('(', 1)
            line = before.strip()
            note = after[:-1].strip()

        items.append((line, note))

    return items


def _parse_simple_list(list_txt: str) -> list[str]:
    items: list[str] = []
    for raw_line in list_txt.splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue
        items.append(line)
    return items


def _normalize_skill_id(raw: str) -> str:
    return raw.strip().lower().replace(' ', '-').replace('_', '-')


def _build_verified_skills_page(
    repo_root: Path,
    generated_root: Path,
    skills: list[SkillDocs],
) -> None:
    verified_path = repo_root / 'verified-skills.txt'
    if not verified_path.is_file():
        return

    skill_ids = {s.skill_id for s in skills}

    alias_map = _verified_alias_map()

    verified_items = _parse_verified_skills(verified_path.read_text(encoding='utf-8'))

    # De-dupe while preserving order
    seen: set[str] = set()
    deduped: list[tuple[str, str | None]] = []
    for raw, note in verified_items:
        key = raw.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append((raw, note))

    lines: list[str] = []
    lines.append('# Verified skills')
    lines.append('')
    lines.append('This page is generated from `verified-skills.txt` at build time.')
    lines.append('')

    missing: list[str] = []

    for raw, note in deduped:
        normalized = _normalize_skill_id(raw)
        canonical = alias_map.get(normalized, normalized)

        description_path = generated_root / canonical / 'description.md'
        tutorial_path = generated_root / canonical / 'tutorial.md'

        links: list[str] = []
        if description_path.is_file():
            links.append(f"[Description](./{canonical}/description.md)")
        if tutorial_path.is_file():
            links.append(f"[Tutorial](./{canonical}/tutorial.md)")

        note_part = f" — _{note}_" if note else ""

        if links:
            link_part = ' | '.join(links)
            display = canonical if canonical in skill_ids else raw
            lines.append(f"- **{display}** — {link_part}{note_part}")
        else:
            missing.append(raw)
            display = canonical if canonical != normalized else raw
            lines.append(f"- **{display}** — _Not found in docs site_{note_part}")

    if missing:
        lines.append('')
        lines.append('## Notes')
        lines.append('Some entries could not be linked because a published `docs/description.md` or `docs/tutorial.md` was not found for them.')
        lines.append('')

    (generated_root / 'verified.md').write_text('\n'.join(lines), encoding='utf-8')


def _verified_alias_map() -> dict[str, str]:
    # Common typos / aliases from verified-skills.txt
    return {
        'augment-unittest': 'augment-code-unit-test',
        'bootstrap-functionnal-spec-from-code': 'bootstrap-functional-spec-from-code',
        'deepen-tech-spec-developper': 'deepen-tech-spec-developer',
        'generat-commits-fron-changelog': 'generate-commits-from-changelog',
        'create-otf-varibale': 'create-otf-variable',
        'swicth-context': 'switch-context',
    }


def _docs_links_for_skill(generated_root: Path, skill_id: str) -> str:
    description_path = generated_root / skill_id / 'description.md'
    tutorial_path = generated_root / skill_id / 'tutorial.md'

    links: list[str] = []
    if description_path.is_file():
        links.append(f"[Description](./{skill_id}/description.md)")
    if tutorial_path.is_file():
        links.append(f"[Tutorial](./{skill_id}/tutorial.md)")

    return ' | '.join(links)


def _load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding='utf-8'))


def _build_competencies_page(
    repo_root: Path,
    generated_root: Path,
) -> None:
    competencies_dir = repo_root / 'competencies'
    if not competencies_dir.is_dir():
        return

    items: list[tuple[str, str | None, list[str]]] = []

    for path in sorted(competencies_dir.glob('*.json'), key=lambda p: p.name.lower()):
        try:
            data = _load_json(path)
        except Exception:
            continue

        if not isinstance(data, dict):
            continue

        name = data.get('name')
        if not isinstance(name, str) or not name.strip():
            name = path.stem

        description = data.get('description')
        if not isinstance(description, str) or not description.strip():
            description = None

        skills_raw = data.get('skills')
        skills: list[str] = []
        if isinstance(skills_raw, list):
            for s in skills_raw:
                if isinstance(s, str) and s.strip():
                    skills.append(s.strip())

        items.append((name, description, skills))

    if not items:
        return

    lines: list[str] = []
    lines.append('# Competencies')
    lines.append('')
    lines.append('This page is generated from `competencies/*.json` at build time.')
    lines.append('')

    # Index
    lines.append('## List')
    lines.append('')
    for name, _desc, skills in items:
        lines.append(f"- [{name}](#{name}) — {len(skills)} skill(s)")
    lines.append('')

    for name, description, skills in items:
        lines.append(f"## {name}")
        lines.append('')
        if description:
            lines.append(description)
            lines.append('')

        if not skills:
            lines.append('_No skills listed._')
            lines.append('')
            continue

        for skill_id in skills:
            links = _docs_links_for_skill(generated_root, skill_id)
            if links:
                lines.append(f"- **{skill_id}** — {links}")
            else:
                lines.append(f"- **{skill_id}**")
        lines.append('')

    (repo_root / 'docs' / 'competencies.md').write_text('\n'.join(lines), encoding='utf-8')


def _build_collections_page(
    repo_root: Path,
) -> None:
    manifest_path = repo_root / 'collection-manifest.json'
    if not manifest_path.is_file():
        return

    try:
        data = _load_json(manifest_path)
    except Exception:
        return

    if not isinstance(data, dict):
        return

    preferred_order = ['starter', 'basic', 'techie', 'full', 'all']
    remaining = sorted([k for k in data.keys() if k not in preferred_order], key=str.lower)
    ordered = [k for k in preferred_order if k in data] + remaining

    lines: list[str] = []
    lines.append('# Collections')
    lines.append('')
    lines.append('This page is generated from `collection-manifest.json` at build time.')
    lines.append('')

    for collection_name in ordered:
        comps_raw = data.get(collection_name)
        competencies: list[str] = []
        if isinstance(comps_raw, list):
            for c in comps_raw:
                if isinstance(c, str) and c.strip():
                    competencies.append(c.strip())

        lines.append(f"## {collection_name}")
        lines.append('')

        if not competencies:
            lines.append('_No competencies listed._')
            lines.append('')
            continue

        lines.append('Competencies:')
        lines.append('')
        for comp in competencies:
            lines.append(f"- [{comp}](competencies.md#{comp})")
        lines.append('')

    (repo_root / 'docs' / 'collections.md').write_text('\n'.join(lines), encoding='utf-8')


def _build_skills_catalog_page(
    repo_root: Path,
    generated_root: Path,
    skills: list[SkillDocs],
) -> None:
    stable_path = repo_root / 'stable.txt'
    stable_items: list[str] = []
    if stable_path.is_file():
        stable_items = _parse_simple_list(stable_path.read_text(encoding='utf-8'))

    verified_path = repo_root / 'verified-skills.txt'
    verified_items: list[tuple[str, str | None]] = []
    if verified_path.is_file():
        verified_items = _parse_verified_skills(
            verified_path.read_text(encoding='utf-8')
        )

    alias_map = _verified_alias_map()

    stable_canonical: list[str] = []
    stable_set: set[str] = set()
    for raw in stable_items:
        normalized = _normalize_skill_id(raw)
        canonical = alias_map.get(normalized, normalized)
        if canonical in stable_set:
            continue
        stable_set.add(canonical)
        stable_canonical.append(canonical)

    curated_canonical: list[str] = []
    curated_set: set[str] = set()
    for raw, _note in verified_items:
        normalized = _normalize_skill_id(raw)
        canonical = alias_map.get(normalized, normalized)
        if canonical in curated_set:
            continue
        curated_set.add(canonical)
        curated_canonical.append(canonical)

    skill_ids = sorted({s.skill_id for s in skills}, key=lambda s: s.lower())
    skill_id_set = set(skill_ids)

    stable_present = sorted([s for s in skill_ids if s in stable_set], key=str.lower)
    curated_present = sorted(
        [s for s in skill_ids if (s in curated_set) and (s not in stable_set)],
        key=str.lower,
    )
    to_be_curated = sorted(
        [s for s in skill_ids if (s not in curated_set) and (s not in stable_set)],
        key=str.lower,
    )

    stable_missing = sorted([s for s in stable_canonical if s not in skill_id_set], key=str.lower)
    curated_missing = sorted(
        [s for s in curated_canonical if (s not in skill_id_set) and (s not in stable_set)],
        key=str.lower,
    )
    listed_but_missing = sorted(set(stable_missing + curated_missing), key=str.lower)

    lines: list[str] = []
    lines.append('# Skills catalog')
    lines.append('')
    lines.append('All skills are grouped into: **Stable**, **Curated**, **To be curated**, and **Listed but missing**.')
    lines.append('')

    # 1 - Stable
    lines.append('## Stable')
    lines.append('')
    if not stable_present:
        lines.append('_No stable skills yet._')
        lines.append('')
    else:
        for skill_id in stable_present:
            links = _docs_links_for_skill(generated_root, skill_id)
            lines.append(f"- **{skill_id}** — {links or '_No published docs yet_'}")
        lines.append('')

    # 2 - Curated
    lines.append('## Curated')
    lines.append('')
    if not curated_present:
        lines.append('_No curated skills listed yet._')
        lines.append('')
    else:
        for skill_id in curated_present:
            links = _docs_links_for_skill(generated_root, skill_id)
            lines.append(f"- **{skill_id}** — {links or '_No published docs yet_'}")
        lines.append('')

    # 3 - To be curated
    lines.append('## To be curated')
    lines.append('')
    if not to_be_curated:
        lines.append('_No skills awaiting curation._')
        lines.append('')
    else:
        for skill_id in to_be_curated:
            links = _docs_links_for_skill(generated_root, skill_id)
            lines.append(f"- **{skill_id}** — {links or '_No published docs yet_'}")
        lines.append('')

    # 4 - Listed but missing (in verified-skills.txt but no skill folder)
    lines.append('## Listed but missing')
    lines.append('')
    if not listed_but_missing:
        lines.append('_No missing entries in stable.txt or verified-skills.txt._')
        lines.append('')
    else:
        for skill_id in listed_but_missing:
            sources: list[str] = []
            if skill_id in stable_missing:
                sources.append('stable.txt')
            if skill_id in curated_missing:
                sources.append('verified-skills.txt')
            source_note = f" ({', '.join(sources)})" if sources else ''
            lines.append(f"- **{skill_id}** — _Listed but no matching skill folder found_{source_note}")
        lines.append('')

    (generated_root / 'catalog.md').write_text('\n'.join(lines), encoding='utf-8')


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

    # Generate verified skills page from verified-skills.txt (if present)
    _build_verified_skills_page(repo_root, generated_root, skills)

    # Generate skills catalog page (Stable / Curated / To be curated)
    _build_skills_catalog_page(repo_root, generated_root, skills)

    # Generate collections/competencies pages
    _build_collections_page(repo_root)
    _build_competencies_page(repo_root, generated_root)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    build_docs_site(repo_root)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
