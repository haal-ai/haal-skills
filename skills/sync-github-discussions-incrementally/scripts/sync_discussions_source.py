#!/usr/bin/env python3

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class ExistingBlock:
    number: int
    content_hash: Optional[str]
    raw: str


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_gh_api_json(path: str) -> object:
    # Use utf-8 to avoid Windows cp1252 decode errors on rich content
    env = dict(os.environ)
    # If GITHUB_TOKEN is set (and possibly invalid), gh will prefer it over keyring auth.
    # Removing it forces gh to use the authenticated account from `gh auth login`.
    env.pop("GITHUB_TOKEN", None)
    result = subprocess.run(
        ["gh", "api", path],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"gh api failed for {path}")
    return json.loads(result.stdout)


def compute_discussion_hash(discussion: Dict, comments: List[Dict]) -> str:
    # Hash only the meaningful fields that indicate content change.
    payload = {
        "number": discussion.get("number"),
        "title": discussion.get("title"),
        "body": discussion.get("body"),
        "state": discussion.get("state"),
        "updated_at": discussion.get("updated_at"),
        "comments": [
            {
                "id": c.get("id"),
                "updated_at": c.get("updated_at"),
                "body": c.get("body"),
                "user": (c.get("user") or {}).get("login"),
            }
            for c in comments
        ],
    }
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def safe_md(text: str) -> str:
    # Keep markdown readable; normalize line endings.
    if text is None:
        return ""
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip()


def fetch_discussion_numbers(owner: str, repo: str) -> List[int]:
    # REST API paginates; use per_page=100 and loop.
    numbers: List[int] = []
    page = 1
    while True:
        path = f"repos/{owner}/{repo}/discussions?per_page=100&page={page}"
        data = run_gh_api_json(path)
        if not isinstance(data, list):
            raise RuntimeError(f"Unexpected response for {path}")
        if not data:
            break
        for d in data:
            n = d.get("number")
            if isinstance(n, int):
                numbers.append(n)
        if len(data) < 100:
            break
        page += 1

    # Keep stable ordering
    return sorted(set(numbers))


def fetch_discussion(owner: str, repo: str, number: int) -> Tuple[Dict, List[Dict]]:
    discussion = run_gh_api_json(f"repos/{owner}/{repo}/discussions/{number}")

    comments: List[Dict] = []
    page = 1
    while True:
        path = f"repos/{owner}/{repo}/discussions/{number}/comments?per_page=100&page={page}"
        page_data = run_gh_api_json(path)
        if not isinstance(page_data, list):
            raise RuntimeError(f"Unexpected response for {path}")
        if not page_data:
            break
        comments.extend(page_data)
        if len(page_data) < 100:
            break
        page += 1

    return discussion, comments


BLOCK_HEADER_RE = re.compile(r"^## Discussion #(\d+):.*$", re.MULTILINE)
HASH_RE = re.compile(r"^\*\*ContentHash:\*\*\s*([0-9a-f]{64})\s*$", re.MULTILINE)


def parse_existing_blocks(text: str) -> Dict[int, ExistingBlock]:
    # Blocks are delimited by H2 headers.
    matches = list(BLOCK_HEADER_RE.finditer(text))
    blocks: Dict[int, ExistingBlock] = {}
    for idx, m in enumerate(matches):
        start = m.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        raw = text[start:end].rstrip() + "\n"
        number = int(m.group(1))
        hash_match = HASH_RE.search(raw)
        content_hash = hash_match.group(1) if hash_match else None
        blocks[number] = ExistingBlock(number=number, content_hash=content_hash, raw=raw)
    return blocks


def upsert_updated_header(text: str, updated_iso: str) -> str:
    lines = text.splitlines()
    out: List[str] = []
    replaced = False
    for line in lines:
        if line.startswith("**Updated:**") and not replaced:
            out.append(f"**Updated:** {updated_iso}")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        # If no header exists, prepend a minimal header.
        return "\n".join(
            [
                "# GitHub Discussions Source",
                "",
                f"**Updated:** {updated_iso}",
                "",
            ]
            + out
        ).rstrip() + "\n"

    return "\n".join(out).rstrip() + "\n"


def render_block(
    owner: str,
    repo: str,
    discussion: Dict,
    comments: List[Dict],
    status: str,
    content_hash: str,
) -> str:
    number = discussion.get("number")
    title = discussion.get("title") or ""
    url = discussion.get("html_url") or ""
    created_at = discussion.get("created_at") or ""
    updated_at = discussion.get("updated_at") or ""
    author = (discussion.get("user") or {}).get("login") or ""
    category = ((discussion.get("category") or {}) or {}).get("name") or ""
    state = discussion.get("state") or ""

    lines: List[str] = []
    lines.append(f"## Discussion #{number}: {title}")
    lines.append("")
    lines.append(f"**Status:** {status}")
    lines.append(f"**ContentHash:** {content_hash}")
    lines.append(f"**URL:** {url}")
    lines.append(f"**Created:** {created_at}")
    lines.append(f"**Updated:** {updated_at}")
    lines.append(f"**Author:** {author}")
    lines.append(f"**Category:** {category}")
    lines.append(f"**State:** {state}")
    lines.append("")
    lines.append("### Original Post")
    lines.append("")
    lines.append(safe_md(discussion.get("body") or ""))
    lines.append("")
    lines.append("### Comments")
    lines.append("")

    if not comments:
        lines.append("(No comments)")
    else:
        # Keep chronological order by created_at then id.
        sorted_comments = sorted(
            comments,
            key=lambda c: (c.get("created_at") or "", c.get("id") or 0),
        )
        for idx, c in enumerate(sorted_comments, start=1):
            c_author = (c.get("user") or {}).get("login") or ""
            c_created = c.get("created_at") or ""
            c_updated = c.get("updated_at") or ""
            lines.append(f"#### Comment {idx} — {c_author}")
            lines.append("")
            lines.append(f"**Created:** {c_created}")
            lines.append(f"**Updated:** {c_updated}")
            lines.append("")
            lines.append(safe_md(c.get("body") or ""))
            lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()

    owner = args.owner
    repo = args.repo

    out_dir = Path("discussion-summaries")
    out_dir.mkdir(exist_ok=True)

    source_path = out_dir / f"{repo}-discussions-source.md"

    existing_text = ""
    existing_blocks: Dict[int, ExistingBlock] = {}
    if source_path.exists():
        existing_text = source_path.read_text(encoding="utf-8")
        existing_blocks = parse_existing_blocks(existing_text)

    fetched_at_iso = utc_now_iso()

    numbers = fetch_discussion_numbers(owner, repo)

    header = "\n".join(
        [
            f"# GitHub Discussions Source — {owner}/{repo}",
            "",
            f"**Updated:** {fetched_at_iso}",
            "",
            "This file is generated from GitHub Discussions. Each discussion is marked as NEW/UPDATED/UNCHANGED based on content hash.",
            "",
            "---",
            "",
        ]
    )

    blocks_out: List[str] = []
    for number in numbers:
        discussion, comments = fetch_discussion(owner, repo, number)
        content_hash = compute_discussion_hash(discussion, comments)

        prior = existing_blocks.get(number)
        if prior and prior.content_hash == content_hash:
            # Preserve unchanged blocks verbatim.
            # Only transition NEW/UPDATED -> UNCHANGED once, to avoid rewriting on every run.
            if re.search(r"^\*\*Status:\*\*\s*UNCHANGED\s*$", prior.raw, flags=re.MULTILINE):
                blocks_out.append(prior.raw.rstrip() + "\n")
            else:
                raw = re.sub(
                    r"^\*\*Status:\*\*\s*(NEW|UPDATED)\s*$",
                    "**Status:** UNCHANGED",
                    prior.raw,
                    flags=re.MULTILINE,
                )
                blocks_out.append(raw.rstrip() + "\n")
            continue

        status = "NEW" if prior is None else "UPDATED"
        blocks_out.append(
            render_block(
                owner=owner,
                repo=repo,
                discussion=discussion,
                comments=comments,
                status=status,
                content_hash=content_hash,
            )
        )

    final_text = header + "\n".join(blocks_out).rstrip() + "\n"

    # If there was an existing file and it contained extra preamble, we intentionally replace it.
    source_path.write_text(final_text, encoding="utf-8")

    print(str(source_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
