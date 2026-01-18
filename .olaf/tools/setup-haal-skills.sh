#!/usr/bin/env bash
set -euo pipefail

REPO_PATH=""
SKILLS_REPO_URL="https://github.com/haal-ai/haal-skills"
SKILLS_BRANCH="main"
CLONE_DEPTH="1"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-path)
      REPO_PATH="${2:-}"; shift 2;;
    --skills-repo-url)
      SKILLS_REPO_URL="${2:-}"; shift 2;;
    --skills-branch)
      SKILLS_BRANCH="${2:-}"; shift 2;;
    --clone-depth)
      CLONE_DEPTH="${2:-}"; shift 2;;
    -h|--help)
      echo "Usage: $0 [--repo-path PATH] [--skills-repo-url URL] [--skills-branch BRANCH] [--clone-depth N]";
      exit 0;;
    *)
      echo "Unknown argument: $1"; exit 2;;
  esac
done

require_command() {
  local name="$1"
  command -v "$name" >/dev/null 2>&1 || { echo "Required command '$name' was not found on PATH."; exit 1; }
}

normalize_git_remote_url() {
  local u="$1"
  u="$(echo "$u" | tr -d '\r' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
  while [[ "$u" == */ ]]; do u="${u%/}"; done
  echo "$u"
}

resolve_repo_root() {
  if [[ -n "$REPO_PATH" ]]; then
    (cd "$REPO_PATH" && pwd -P)
    return
  fi

  if git_root=$(git rev-parse --show-toplevel 2>/dev/null); then
    if [[ -n "$git_root" ]]; then
      echo "$git_root"
      return
    fi
  fi

  pwd -P
}

require_command git

PYTHON_BIN=""
if command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
else
  echo "Required command 'python' or 'python3' was not found on PATH."; exit 1
fi

REPO_ROOT="$(resolve_repo_root)"
WINDSURF_SKILLS_PATH="$HOME/.codeium/windsurf/skills"
SYNC_SCRIPT="$WINDSURF_SKILLS_PATH/.olaf/tools/sync_olaf_files.py"

echo "=== HAAL Skills Setup ==="
echo "Repo:   $REPO_ROOT"
echo "Skills: $WINDSURF_SKILLS_PATH"
echo "Depth:  $CLONE_DEPTH"

if [[ ! -d "$REPO_ROOT/.git" ]]; then
  echo "Target path is not a git repository: $REPO_ROOT"; exit 1
fi

mkdir -p "$(dirname "$WINDSURF_SKILLS_PATH")"

if [[ -d "$WINDSURF_SKILLS_PATH/.git" ]]; then
  (
    cd "$WINDSURF_SKILLS_PATH"
    remote="$(git remote get-url origin 2>/dev/null || true)"
    remote_norm="$(normalize_git_remote_url "$remote")"
    expected_norm="$(normalize_git_remote_url "$SKILLS_REPO_URL")"
    if [[ "$remote_norm" != "$expected_norm" ]]; then
      echo "Existing skills folder has unexpected git remote: '$remote' (expected '$SKILLS_REPO_URL')."; exit 1
    fi

    echo "Updating existing haal-skills checkout..."
    if [[ "$CLONE_DEPTH" != "0" ]]; then
      git fetch --depth "$CLONE_DEPTH" origin "$SKILLS_BRANCH"
    else
      git fetch origin
    fi
    git checkout "$SKILLS_BRANCH" >/dev/null
    git reset --hard "origin/$SKILLS_BRANCH" >/dev/null
  )
else
  if [[ ! -d "$WINDSURF_SKILLS_PATH" ]]; then
    echo "Creating skills folder: $WINDSURF_SKILLS_PATH"
    mkdir -p "$WINDSURF_SKILLS_PATH"
  else
    if [[ -n "$(ls -A "$WINDSURF_SKILLS_PATH" 2>/dev/null || true)" ]]; then
      item_count="$(ls -A "$WINDSURF_SKILLS_PATH" 2>/dev/null | wc -l | tr -d ' ')"
      echo "Cannot install into '$WINDSURF_SKILLS_PATH' because it exists, is not a git repo, and is not empty (contains $item_count items)."; exit 1
    fi
  fi

  echo "Cloning haal-skills into $WINDSURF_SKILLS_PATH ..."
  if [[ "$CLONE_DEPTH" != "0" ]]; then
    git clone --depth "$CLONE_DEPTH" --branch "$SKILLS_BRANCH" --single-branch "$SKILLS_REPO_URL" "$WINDSURF_SKILLS_PATH"
  else
    git clone --branch "$SKILLS_BRANCH" "$SKILLS_REPO_URL" "$WINDSURF_SKILLS_PATH"
  fi
fi

if [[ ! -f "$SYNC_SCRIPT" ]]; then
  echo "Sync script not found: $SYNC_SCRIPT"; exit 1
fi

echo "Running OLAF sync script..."
(
  cd "$REPO_ROOT"
  "$PYTHON_BIN" "$SYNC_SCRIPT"
)

env_validation_file="$REPO_ROOT/.windsurf/workflows/environment-validation.md"
olaf_data_dir="$REPO_ROOT/.olaf/data"

echo "Verification:"
if [[ -f "$env_validation_file" ]]; then echo "- environment-validation.md: true"; else echo "- environment-validation.md: false"; fi
if [[ -d "$olaf_data_dir" ]]; then echo "- .olaf/data exists: true"; else echo "- .olaf/data exists: false"; fi

if [[ -d "$olaf_data_dir" ]]; then
  file_count="$(find "$olaf_data_dir" -type f 2>/dev/null | wc -l | tr -d ' ')"
  echo "- .olaf/data file count: $file_count"
fi

echo "=== Done ==="
