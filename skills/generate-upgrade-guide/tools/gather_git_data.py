#!/usr/bin/env python3
"""
Gather git data between two tags on a given branch.

Outputs a structured Markdown file with:
- Commit log (hash, subject, body, author, date)
- Extracted Jira ticket references
- File change summary (git diff --stat)
- Detailed file change list (git diff --name-status)

Usage:
    python gather_git_data.py <start_tag> <end_tag> -o <output_file> [--branch <branch>] [--repo <path>]
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

JIRA_PATTERN = re.compile(r"[A-Z][A-Z0-9_]+-\d+")
SEPARATOR = "---GIT_RECORD_SEP---"
FIELD_SEP = "---GIT_FIELD_SEP---"


def run_git(args: list[str], cwd: str | None = None) -> str:
    """Run a git command and return stdout. Raises on failure."""
    cmd = ["git"] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=cwd,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        print(f"ERROR running: {' '.join(cmd)}", file=sys.stderr)
        print(result.stderr.strip(), file=sys.stderr)
        sys.exit(1)
    return result.stdout.strip()


def extract_jira_tickets(text: str) -> list[str]:
    """Extract unique Jira-style ticket references from text."""
    return sorted(set(JIRA_PATTERN.findall(text)))


# ---------------------------------------------------------------------------
# Data gathering
# ---------------------------------------------------------------------------

def gather_commits(start_tag: str, end_tag: str, cwd: str | None = None) -> list[dict]:
    """Return list of commit dicts between two tags."""
    fmt = FIELD_SEP.join(["%H", "%h", "%s", "%b", "%an", "%ae", "%ad"])
    raw = run_git(
        [
            "log",
            f"--pretty=format:{fmt}{SEPARATOR}",
            "--date=short",
            f"{start_tag}..{end_tag}",
        ],
        cwd=cwd,
    )
    if not raw:
        return []

    commits = []
    for block in raw.split(SEPARATOR):
        block = block.strip()
        if not block:
            continue
        parts = block.split(FIELD_SEP)
        if len(parts) < 6:
            continue
        commit = {
            "hash": parts[0].strip(),
            "short_hash": parts[1].strip(),
            "subject": parts[2].strip(),
            "body": parts[3].strip(),
            "author": parts[4].strip(),
            "email": parts[5].strip(),
            "date": parts[6].strip() if len(parts) > 6 else "",
        }
        full_message = f"{commit['subject']} {commit['body']}"
        commit["jira_tickets"] = extract_jira_tickets(full_message)
        commits.append(commit)
    return commits


def gather_diff_stat(start_tag: str, end_tag: str, cwd: str | None = None) -> str:
    """Return git diff --stat between two tags."""
    return run_git(["diff", "--stat", f"{start_tag}..{end_tag}"], cwd=cwd)


def gather_diff_name_status(start_tag: str, end_tag: str, cwd: str | None = None) -> str:
    """Return git diff --name-status between two tags."""
    return run_git(["diff", "--name-status", f"{start_tag}..{end_tag}"], cwd=cwd)


def gather_shortlog(start_tag: str, end_tag: str, cwd: str | None = None) -> str:
    """Return contributor summary."""
    return run_git(["shortlog", "-sn", f"{start_tag}..{end_tag}"], cwd=cwd)


def get_current_branch(cwd: str | None = None) -> str:
    """Return current branch name."""
    return run_git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd)


def validate_ref(ref: str, cwd: str | None = None) -> bool:
    """Check if a git ref (tag/branch) exists."""
    result = subprocess.run(
        ["git", "rev-parse", "--verify", ref],
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return result.returncode == 0


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def build_markdown(
    start_tag: str,
    end_tag: str,
    branch: str,
    commits: list[dict],
    diff_stat: str,
    diff_name_status: str,
    shortlog: str,
    all_jira_tickets: list[str],
) -> str:
    """Build the structured Markdown context file."""
    lines: list[str] = []

    lines.append(f"# Git Data: {start_tag} → {end_tag}")
    lines.append("")
    lines.append(f"- **Branch**: `{branch}`")
    lines.append(f"- **Start tag**: `{start_tag}`")
    lines.append(f"- **End tag**: `{end_tag}`")
    lines.append(f"- **Total commits**: {len(commits)}")
    lines.append(f"- **Jira tickets found**: {len(all_jira_tickets)}")
    lines.append("")

    # Jira tickets summary
    lines.append("## Jira Tickets Referenced")
    lines.append("")
    if all_jira_tickets:
        for ticket in all_jira_tickets:
            lines.append(f"- `{ticket}`")
    else:
        lines.append("_No Jira ticket references found in commit messages._")
    lines.append("")

    # Commits
    lines.append("## Commits")
    lines.append("")
    for c in commits:
        tickets_str = ", ".join(f"`{t}`" for t in c["jira_tickets"]) if c["jira_tickets"] else "_none_"
        lines.append(f"### `{c['short_hash']}` — {c['subject']}")
        lines.append("")
        lines.append(f"- **Author**: {c['author']} ({c['email']})")
        lines.append(f"- **Date**: {c['date']}")
        lines.append(f"- **Jira**: {tickets_str}")
        if c["body"]:
            lines.append(f"- **Body**:")
            for body_line in c["body"].splitlines():
                lines.append(f"  > {body_line}")
        lines.append("")

    # Contributor summary
    lines.append("## Contributors")
    lines.append("")
    lines.append("```")
    lines.append(shortlog if shortlog else "No contributors found.")
    lines.append("```")
    lines.append("")

    # File changes
    lines.append("## File Changes (name-status)")
    lines.append("")
    lines.append("```")
    lines.append(diff_name_status if diff_name_status else "No file changes.")
    lines.append("```")
    lines.append("")

    lines.append("## File Changes (stat)")
    lines.append("")
    lines.append("```")
    lines.append(diff_stat if diff_stat else "No file changes.")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gather git data between two tags and output structured Markdown."
    )
    parser.add_argument("start_tag", help="Starting git tag (e.g. v1.0.0)")
    parser.add_argument("end_tag", help="Ending git tag (e.g. v1.1.0)")
    parser.add_argument("-o", "--output", required=True, help="Output Markdown file path")
    parser.add_argument("--branch", default=None, help="Branch to use (default: current branch)")
    parser.add_argument("--repo", default=None, help="Path to git repository (default: current directory)")

    args = parser.parse_args()
    cwd = args.repo or os.getcwd()

    # Validate refs
    if not validate_ref(args.start_tag, cwd=cwd):
        print(f"ERROR: Tag '{args.start_tag}' not found in repository.", file=sys.stderr)
        sys.exit(1)
    if not validate_ref(args.end_tag, cwd=cwd):
        print(f"ERROR: Tag '{args.end_tag}' not found in repository.", file=sys.stderr)
        sys.exit(1)

    # Resolve branch
    branch = args.branch or get_current_branch(cwd=cwd)

    # If branch specified, check out (but don't force — just inform)
    if args.branch:
        current = get_current_branch(cwd=cwd)
        if current != args.branch:
            print(f"WARNING: Current branch is '{current}', not '{args.branch}'.", file=sys.stderr)
            print(f"         Tags are resolved in current repo state.", file=sys.stderr)

    # Gather data
    print(f"Gathering commits between {args.start_tag}..{args.end_tag} ...")
    commits = gather_commits(args.start_tag, args.end_tag, cwd=cwd)

    print(f"Gathering diff stats ...")
    diff_stat = gather_diff_stat(args.start_tag, args.end_tag, cwd=cwd)
    diff_name_status = gather_diff_name_status(args.start_tag, args.end_tag, cwd=cwd)

    print(f"Gathering contributor summary ...")
    shortlog = gather_shortlog(args.start_tag, args.end_tag, cwd=cwd)

    # Collect all Jira tickets
    all_tickets: set[str] = set()
    for c in commits:
        all_tickets.update(c["jira_tickets"])
    all_jira_tickets = sorted(all_tickets)

    # Build and write markdown
    md = build_markdown(
        start_tag=args.start_tag,
        end_tag=args.end_tag,
        branch=branch,
        commits=commits,
        diff_stat=diff_stat,
        diff_name_status=diff_name_status,
        shortlog=shortlog,
        all_jira_tickets=all_jira_tickets,
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")

    print(f"Git data written to: {out_path}")
    print(f"  Commits: {len(commits)}")
    print(f"  Jira tickets: {len(all_jira_tickets)}")

    # Write tickets list as separate file for the Jira script
    tickets_file = out_path.parent / "jira-tickets.txt"
    tickets_file.write_text("\n".join(all_jira_tickets), encoding="utf-8")
    print(f"  Jira ticket list: {tickets_file}")


if __name__ == "__main__":
    main()
