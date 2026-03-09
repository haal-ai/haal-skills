#!/usr/bin/env python3
"""
Gather Jira issue details for a list of ticket IDs.

Reads ticket IDs from a file (one per line) or from command-line arguments,
queries the Jira REST API, and outputs a structured Markdown file.

Authentication:
    Set environment variables:
        JIRA_BASE_URL   - e.g. https://yourcompany.atlassian.net
        JIRA_USER       - e.g. user@company.com
        JIRA_API_TOKEN  - API token (Jira Cloud) or password (Jira Server)

    For Jira Server with personal access token:
        JIRA_PAT        - Personal access token (used instead of user+token)

Usage:
    python gather_jira_data.py -f jira-tickets.txt -o jira-data.md
    python gather_jira_data.py PROJ-101 PROJ-102 -o jira-data.md
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import base64


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

def get_jira_config() -> dict:
    """Read Jira connection settings from environment variables."""
    base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
    if not base_url:
        return {}

    config = {"base_url": base_url}

    pat = os.environ.get("JIRA_PAT", "")
    if pat:
        config["auth_header"] = f"Bearer {pat}"
    else:
        user = os.environ.get("JIRA_USER", "")
        token = os.environ.get("JIRA_API_TOKEN", "")
        if user and token:
            cred = base64.b64encode(f"{user}:{token}".encode()).decode()
            config["auth_header"] = f"Basic {cred}"

    return config


# ---------------------------------------------------------------------------
# Jira API
# ---------------------------------------------------------------------------

def fetch_issue(ticket_id: str, config: dict) -> dict | None:
    """Fetch a single Jira issue. Returns parsed JSON or None on failure."""
    url = f"{config['base_url']}/rest/api/2/issue/{ticket_id}"
    req = Request(url)
    req.add_header("Accept", "application/json")
    if "auth_header" in config:
        req.add_header("Authorization", config["auth_header"])

    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        print(f"  WARNING: HTTP {e.code} fetching {ticket_id}: {e.reason}", file=sys.stderr)
        return None
    except URLError as e:
        print(f"  WARNING: Network error fetching {ticket_id}: {e.reason}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  WARNING: Unexpected error fetching {ticket_id}: {e}", file=sys.stderr)
        return None


def extract_issue_data(raw: dict) -> dict:
    """Extract relevant fields from a Jira API response."""
    fields = raw.get("fields", {})

    issue_type = fields.get("issuetype", {})
    status = fields.get("status", {})
    priority = fields.get("priority", {})
    assignee = fields.get("assignee", {})
    reporter = fields.get("reporter", {})
    resolution = fields.get("resolution", {})
    components = fields.get("components", [])
    labels = fields.get("labels", [])
    fix_versions = fields.get("fixVersions", [])

    return {
        "key": raw.get("key", ""),
        "summary": fields.get("summary", ""),
        "description": fields.get("description", "") or "",
        "type": issue_type.get("name", "") if issue_type else "",
        "status": status.get("name", "") if status else "",
        "priority": priority.get("name", "") if priority else "",
        "assignee": assignee.get("displayName", "") if assignee else "Unassigned",
        "reporter": reporter.get("displayName", "") if reporter else "",
        "resolution": resolution.get("name", "") if resolution else "Unresolved",
        "components": [c.get("name", "") for c in components],
        "labels": labels,
        "fix_versions": [v.get("name", "") for v in fix_versions],
        "created": fields.get("created", ""),
        "updated": fields.get("updated", ""),
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def truncate_description(desc: str, max_lines: int = 20) -> str:
    """Truncate long descriptions for readability."""
    lines = desc.splitlines()
    if len(lines) <= max_lines:
        return desc
    return "\n".join(lines[:max_lines]) + f"\n\n_... (truncated, {len(lines) - max_lines} more lines)_"


def build_markdown(tickets: list[str], issues: dict[str, dict], failed: list[str]) -> str:
    """Build structured Markdown from Jira issue data."""
    lines: list[str] = []

    lines.append("# Jira Issue Details")
    lines.append("")
    lines.append(f"- **Tickets requested**: {len(tickets)}")
    lines.append(f"- **Successfully fetched**: {len(issues)}")
    lines.append(f"- **Failed/not found**: {len(failed)}")
    lines.append("")

    if failed:
        lines.append("## Tickets Not Found")
        lines.append("")
        for t in failed:
            lines.append(f"- `{t}` — could not be retrieved")
        lines.append("")

    # Summary table
    if issues:
        lines.append("## Issue Summary")
        lines.append("")
        lines.append("| Ticket | Type | Status | Priority | Summary |")
        lines.append("|--------|------|--------|----------|---------|")
        for key in tickets:
            if key in issues:
                i = issues[key]
                lines.append(f"| `{i['key']}` | {i['type']} | {i['status']} | {i['priority']} | {i['summary']} |")
        lines.append("")

    # Detailed issues
    if issues:
        lines.append("## Issue Details")
        lines.append("")
        for key in tickets:
            if key not in issues:
                continue
            i = issues[key]
            lines.append(f"### `{i['key']}` — {i['summary']}")
            lines.append("")
            lines.append(f"- **Type**: {i['type']}")
            lines.append(f"- **Status**: {i['status']}")
            lines.append(f"- **Priority**: {i['priority']}")
            lines.append(f"- **Assignee**: {i['assignee']}")
            lines.append(f"- **Reporter**: {i['reporter']}")
            lines.append(f"- **Resolution**: {i['resolution']}")
            if i["components"]:
                lines.append(f"- **Components**: {', '.join(i['components'])}")
            if i["labels"]:
                lines.append(f"- **Labels**: {', '.join(i['labels'])}")
            if i["fix_versions"]:
                lines.append(f"- **Fix Versions**: {', '.join(i['fix_versions'])}")
            lines.append(f"- **Created**: {i['created']}")
            lines.append(f"- **Updated**: {i['updated']}")
            if i["description"]:
                lines.append("")
                lines.append("**Description:**")
                lines.append("")
                lines.append(truncate_description(i["description"]))
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gather Jira issue details and output structured Markdown."
    )
    parser.add_argument("tickets", nargs="*", help="Jira ticket IDs (e.g. PROJ-101 PROJ-102)")
    parser.add_argument("-f", "--file", help="File containing ticket IDs, one per line")
    parser.add_argument("-o", "--output", required=True, help="Output Markdown file path")

    args = parser.parse_args()

    # Collect ticket IDs
    tickets: list[str] = []
    if args.file:
        path = Path(args.file)
        if path.is_file():
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    tickets.append(line)
        else:
            print(f"WARNING: Ticket file not found: {args.file}", file=sys.stderr)

    tickets.extend(args.tickets)
    tickets = list(dict.fromkeys(tickets))  # deduplicate preserving order

    if not tickets:
        print("No Jira tickets to fetch.", file=sys.stderr)
        # Write empty report
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            "# Jira Issue Details\n\n_No Jira ticket references were found in the commit messages._\n",
            encoding="utf-8",
        )
        print(f"Empty Jira report written to: {out_path}")
        return

    # Check Jira config
    config = get_jira_config()
    if not config:
        print("WARNING: JIRA_BASE_URL not set. Cannot fetch Jira data.", file=sys.stderr)
        print("         Set JIRA_BASE_URL, and either JIRA_PAT or JIRA_USER+JIRA_API_TOKEN.", file=sys.stderr)
        # Write report with tickets listed but no details
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Jira Issue Details",
            "",
            "**WARNING: Jira API not configured. Ticket details could not be fetched.**",
            "",
            "Set the following environment variables to enable Jira integration:",
            "- `JIRA_BASE_URL` — e.g. `https://yourcompany.atlassian.net`",
            "- `JIRA_PAT` — Personal access token (or use `JIRA_USER` + `JIRA_API_TOKEN`)",
            "",
            "## Tickets Found in Commits",
            "",
        ]
        for t in tickets:
            lines.append(f"- `{t}`")
        lines.append("")
        out_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Jira report (no API) written to: {out_path}")
        return

    # Fetch issues
    print(f"Fetching {len(tickets)} Jira issues from {config['base_url']} ...")
    issues: dict[str, dict] = {}
    failed: list[str] = []

    for ticket in tickets:
        print(f"  Fetching {ticket} ...")
        raw = fetch_issue(ticket, config)
        if raw:
            issues[ticket] = extract_issue_data(raw)
        else:
            failed.append(ticket)

    # Build and write markdown
    md = build_markdown(tickets, issues, failed)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")

    print(f"Jira data written to: {out_path}")
    print(f"  Fetched: {len(issues)}")
    print(f"  Failed: {len(failed)}")


if __name__ == "__main__":
    main()
