#!/usr/bin/env python3
"""
Check whether an upgrade guide is applicable to the current target.

Compares the guide's expected start version against the target's actual version
using multiple detection strategies:
  1. Git tag on current HEAD (exact or closest)
  2. Version files (package.json, pom.xml, setup.py, pyproject.toml, version.txt, etc.)
  3. Git describe --tags

Outputs a structured JSON report with:
  - detected_version: what version the target appears to be at
  - expected_version: what the upgrade guide expects (start_tag)
  - target_version: what the upgrade guide upgrades to (end_tag)
  - is_applicable: boolean
  - detection_method: how the version was determined
  - details: human-readable explanation

Usage:
    python check_version_applicability.py <start_tag> <end_tag> [--repo <path>] [-o <output_file>]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Version detection strategies
# ---------------------------------------------------------------------------

def run_cmd(args: list[str], cwd: str | None = None) -> str | None:
    """Run a command, return stdout or None on failure."""
    try:
        result = subprocess.run(
            args, capture_output=True, text=True, cwd=cwd,
            encoding="utf-8", errors="replace", timeout=15,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def normalize_version(version: str) -> str:
    """Strip leading 'v' or 'V' for comparison."""
    return re.sub(r"^[vV]", "", version.strip())


def detect_from_git_tag_on_head(cwd: str | None = None) -> tuple[str | None, str]:
    """Check if HEAD is exactly at a tag."""
    result = run_cmd(["git", "describe", "--tags", "--exact-match", "HEAD"], cwd=cwd)
    if result:
        return result, "git tag (exact match on HEAD)"
    return None, ""


def detect_from_git_describe(cwd: str | None = None) -> tuple[str | None, str]:
    """Use git describe to find closest tag."""
    result = run_cmd(["git", "describe", "--tags", "--abbrev=0", "HEAD"], cwd=cwd)
    if result:
        return result, "git describe (closest tag)"
    return None, ""


def detect_from_package_json(cwd: str | None = None) -> tuple[str | None, str]:
    """Read version from package.json."""
    path = Path(cwd or ".") / "package.json"
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            version = data.get("version")
            if version:
                return str(version), "package.json"
        except Exception:
            pass
    return None, ""


def detect_from_pom_xml(cwd: str | None = None) -> tuple[str | None, str]:
    """Read version from pom.xml (simple regex, no XML parser needed)."""
    path = Path(cwd or ".") / "pom.xml"
    if path.is_file():
        try:
            content = path.read_text(encoding="utf-8")
            # Match first <version> outside of <parent>
            # Simple approach: find all <version> tags, take the first one after <artifactId>
            match = re.search(r"<version>\s*([^<]+?)\s*</version>", content)
            if match:
                return match.group(1), "pom.xml"
        except Exception:
            pass
    return None, ""


def detect_from_pyproject_toml(cwd: str | None = None) -> tuple[str | None, str]:
    """Read version from pyproject.toml."""
    path = Path(cwd or ".") / "pyproject.toml"
    if path.is_file():
        try:
            content = path.read_text(encoding="utf-8")
            match = re.search(r'^version\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
            if match:
                return match.group(1), "pyproject.toml"
        except Exception:
            pass
    return None, ""


def detect_from_setup_py(cwd: str | None = None) -> tuple[str | None, str]:
    """Read version from setup.py."""
    path = Path(cwd or ".") / "setup.py"
    if path.is_file():
        try:
            content = path.read_text(encoding="utf-8")
            match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
            if match:
                return match.group(1), "setup.py"
        except Exception:
            pass
    return None, ""


def detect_from_version_file(cwd: str | None = None) -> tuple[str | None, str]:
    """Read version from VERSION or version.txt."""
    base = Path(cwd or ".")
    for name in ("VERSION", "version.txt", "VERSION.txt"):
        path = base / name
        if path.is_file():
            try:
                content = path.read_text(encoding="utf-8").strip()
                if content and len(content) < 50:
                    return content, name
            except Exception:
                pass
    return None, ""


def detect_from_gradle(cwd: str | None = None) -> tuple[str | None, str]:
    """Read version from build.gradle or build.gradle.kts."""
    base = Path(cwd or ".")
    for name in ("build.gradle", "build.gradle.kts"):
        path = base / name
        if path.is_file():
            try:
                content = path.read_text(encoding="utf-8")
                match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    return match.group(1), name
            except Exception:
                pass
    return None, ""


DETECTORS = [
    detect_from_git_tag_on_head,
    detect_from_git_describe,
    detect_from_package_json,
    detect_from_pom_xml,
    detect_from_pyproject_toml,
    detect_from_setup_py,
    detect_from_version_file,
    detect_from_gradle,
]


def detect_version(cwd: str | None = None) -> tuple[str | None, str]:
    """Try all detection strategies in order. Return first match."""
    for detector in DETECTORS:
        version, method = detector(cwd=cwd)
        if version:
            return version, method
    return None, "none"


# ---------------------------------------------------------------------------
# Applicability check
# ---------------------------------------------------------------------------

def versions_match(detected: str, expected: str) -> bool:
    """Check if detected version matches the expected start_tag."""
    d = normalize_version(detected)
    e = normalize_version(expected)
    # Exact match
    if d == e:
        return True
    # Prefix match (e.g., 1.0.0 matches 1.0.0-SNAPSHOT)
    if d.startswith(e) or e.startswith(d):
        return True
    return False


def is_version_between(detected: str, start: str, end: str) -> str:
    """Determine if detected version is before start, at start, between, at end, or after end.
    Returns a descriptive string."""
    d = normalize_version(detected)
    s = normalize_version(start)
    e = normalize_version(end)

    if d == s:
        return "at_start"
    if d == e:
        return "at_end"

    # Simple numeric comparison for semver-like strings
    def to_tuple(v: str) -> tuple:
        parts = re.split(r"[.\-]", v)
        result = []
        for p in parts:
            try:
                result.append(int(p))
            except ValueError:
                result.append(p)
        return tuple(result)

    try:
        dt, st, et = to_tuple(d), to_tuple(s), to_tuple(e)
        if dt < st:
            return "before_start"
        if dt > et:
            return "after_end"
        return "between"
    except Exception:
        return "unknown"


def build_report(
    start_tag: str,
    end_tag: str,
    detected_version: str | None,
    detection_method: str,
) -> dict:
    """Build the applicability report."""
    if detected_version is None:
        return {
            "detected_version": None,
            "expected_version": start_tag,
            "target_version": end_tag,
            "is_applicable": False,
            "detection_method": "none",
            "position": "unknown",
            "details": (
                f"Could not detect current version of the target. "
                f"The upgrade guide expects the target to be at version '{start_tag}'. "
                f"Please verify manually that you are at version '{start_tag}' before proceeding."
            ),
            "recommendation": "MANUAL_CHECK_REQUIRED",
        }

    matches = versions_match(detected_version, start_tag)
    position = is_version_between(detected_version, start_tag, end_tag)

    if matches or position == "at_start":
        details = (
            f"Target is at version '{detected_version}' (detected via {detection_method}). "
            f"This matches the upgrade guide's expected start version '{start_tag}'. "
            f"The upgrade guide is APPLICABLE."
        )
        recommendation = "PROCEED"
    elif position == "at_end":
        details = (
            f"Target is already at version '{detected_version}' (detected via {detection_method}). "
            f"This matches the upgrade guide's target version '{end_tag}'. "
            f"The upgrade has ALREADY BEEN APPLIED."
        )
        recommendation = "ALREADY_UPGRADED"
    elif position == "before_start":
        details = (
            f"Target is at version '{detected_version}' (detected via {detection_method}), "
            f"which is BEFORE the guide's expected start version '{start_tag}'. "
            f"You need to first upgrade to '{start_tag}' before applying this guide."
        )
        recommendation = "UPGRADE_TO_START_FIRST"
    elif position == "after_end":
        details = (
            f"Target is at version '{detected_version}' (detected via {detection_method}), "
            f"which is AFTER the guide's target version '{end_tag}'. "
            f"This upgrade guide is NOT applicable — the target is already past '{end_tag}'."
        )
        recommendation = "NOT_APPLICABLE_PAST_TARGET"
    elif position == "between":
        details = (
            f"Target is at version '{detected_version}' (detected via {detection_method}), "
            f"which is between '{start_tag}' and '{end_tag}'. "
            f"The upgrade may have been PARTIALLY APPLIED. Review carefully before proceeding."
        )
        recommendation = "PARTIAL_UPGRADE_REVIEW"
    else:
        details = (
            f"Target is at version '{detected_version}' (detected via {detection_method}). "
            f"Could not determine relationship to guide versions '{start_tag}' → '{end_tag}'. "
            f"Please verify manually."
        )
        recommendation = "MANUAL_CHECK_REQUIRED"

    return {
        "detected_version": detected_version,
        "expected_version": start_tag,
        "target_version": end_tag,
        "is_applicable": matches or position == "at_start",
        "detection_method": detection_method,
        "position": position,
        "details": details,
        "recommendation": recommendation,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check if an upgrade guide is applicable to the current target."
    )
    parser.add_argument("start_tag", help="Expected start version from the upgrade guide")
    parser.add_argument("end_tag", help="Target version from the upgrade guide")
    parser.add_argument("--repo", default=None, help="Path to target repository (default: cwd)")
    parser.add_argument("-o", "--output", default=None, help="Output JSON report file (optional)")

    args = parser.parse_args()
    cwd = args.repo or os.getcwd()

    print(f"Checking version applicability for upgrade {args.start_tag} → {args.end_tag} ...")
    print(f"  Target repository: {cwd}")

    detected_version, method = detect_version(cwd=cwd)
    if detected_version:
        print(f"  Detected version: {detected_version} (via {method})")
    else:
        print(f"  WARNING: Could not detect current version.")

    report = build_report(args.start_tag, args.end_tag, detected_version, method)

    print(f"\n  Applicable: {report['is_applicable']}")
    print(f"  Recommendation: {report['recommendation']}")
    print(f"  Details: {report['details']}")

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"\n  Report written to: {out_path}")

    # Exit code: 0 = applicable, 1 = not applicable, 2 = unknown
    if report["is_applicable"]:
        sys.exit(0)
    elif report["recommendation"] == "MANUAL_CHECK_REQUIRED":
        sys.exit(2)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
