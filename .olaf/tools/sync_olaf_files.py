#!/usr/bin/env python3
"""
File synchronization script for OLAF skills repository.

This script manages file synchronization between:
- Source: ~/.codeium/windsurf/skills
- Destination: Current repository where script is launched

Configuration is stored in ~/.codeium/windsurf/skills/.olaf/local-file.json
"""

import json
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Set


def get_config_path() -> Path:
    """Get path to the configuration file."""
    home = Path.home()
    return home / ".codeium/windsurf/skills/.olaf/local-file.json"


def get_source_base() -> Path:
    """Get the source base directory."""
    home = Path.home()
    return home / ".codeium/windsurf/skills"


def initialize_config(config_path: Path, source_base: Path) -> None:
    """Initialize the configuration file with default values."""
    config = {
        "files_to_prune": [],
        "files_to_force_replace": [],
        "folders_to_copy_from": [
            str(source_base / ".olaf/data"),
            str(source_base / ".olaf/work"),
            str(source_base / ".olaf/tools"),
            str(source_base / ".windsurf/rules"),
            str(source_base / ".windsurf/workflows")
        ]
    }
    
    # Ensure parent directory exists
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Initialized config at {config_path}")
    print(f"📁 Source base: {source_base}")


def load_config(config_path: Path) -> Dict:
    """Load configuration from JSON file."""
    if not config_path.exists():
        print(f"❌ Config file not found: {config_path}")
        print("Initializing new config...")
        source_base = get_source_base()
        initialize_config(config_path, source_base)
    
    with open(config_path, 'r') as f:
        return json.load(f)


def get_destination_base() -> Path:
    """Get the destination base directory (current repository)."""
    return Path.cwd()


def collect_files_to_copy(source_folders: List[str], prune_files: List[str], 
                         force_replace_files: List[str], source_base: Path) -> Set[Path]:
    """Collect all files from source folders, excluding specified ones."""
    files_to_copy = set()
    prune_set = set(Path(f) for f in prune_files)
    force_replace_set = set(Path(f) for f in force_replace_files)
    
    for folder_str in source_folders:
        folder = Path(folder_str)
        if not folder.exists():
            print(f"⚠️  Source folder not found: {folder}")
            continue
        
        # Walk through all files in the folder
        for file_path in folder.rglob('*'):
            if file_path.is_file():
                # Get relative path from the SOURCE BASE (not from the folder)
                rel_path = file_path.relative_to(source_base)
                
                # Skip if in prune list
                if rel_path in prune_set:
                    print(f"🗑️  Pruning: {rel_path}")
                    continue
                
                files_to_copy.add((file_path, rel_path, rel_path in force_replace_set))
    
    return files_to_copy


def prune_files_at_destination(prune_files: List[str], dest_base: Path) -> None:
    """Delete files from destination if they exist."""
    for file_str in prune_files:
        file_path = dest_base / file_str
        if file_path.exists():
            if file_path.is_file():
                file_path.unlink()
                print(f"🗑️  Deleted file: {file_path}")
            elif file_path.is_dir():
                shutil.rmtree(file_path)
                print(f"🗑️  Deleted directory: {file_path}")
        else:
            print(f"ℹ️  File not found for pruning: {file_path}")


def copy_files_to_destination(files_to_copy: Set[tuple], dest_base: Path) -> None:
    """Copy files from source to destination."""
    for source_file, rel_path, force_replace in files_to_copy:
        dest_file = dest_base / rel_path
        
        # Check if file already exists
        if dest_file.exists():
            if force_replace:
                print(f"🔄 Force replacing: {rel_path}")
            else:
                print(f"⏭️  Skipping (exists): {rel_path}")
                continue
        
        # Create parent directories if needed
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy the file
        shutil.copy2(source_file, dest_file)
        print(f"📁 Copied: {rel_path}")


def update_git_exclude(dest_base: Path) -> None:
    """Update .git/info/exclude to exclude OLAF files."""
    git_info_dir = dest_base / ".git" / "info"
    exclude_file = git_info_dir / "exclude"
    
    # Ensure .git/info directory exists
    git_info_dir.mkdir(parents=True, exist_ok=True)
    
    # Exclusions to add
    exclusions = [
        "olaf-*",
        "my-skills-*",
        ".olaf/work/",
        ".olaf/data/context/"
    ]
    
    # Read existing exclusions
    existing_exclusions = set()
    if exclude_file.exists():
        with open(exclude_file, 'r') as f:
            existing_exclusions = set(line.strip() for line in f if line.strip() and not line.startswith('#'))
    
    # Add new exclusions that don't already exist
    new_exclusions = [ex for ex in exclusions if ex not in existing_exclusions]
    
    if new_exclusions:
        with open(exclude_file, 'a') as f:
            f.write("\n# OLAF sync exclusions\n")
            for exclusion in new_exclusions:
                f.write(f"{exclusion}\n")
        print(f"📝 Added {len(new_exclusions)} exclusions to .git/info/exclude")
    else:
        print("ℹ️  No new exclusions needed for .git/info/exclude")


def main():
    """Main execution function."""
    print("🚀 OLAF File Synchronization Script")
    print("=" * 50)
    
    # Get paths
    config_path = get_config_path()
    source_base = get_source_base()
    dest_base = get_destination_base()
    
    print(f"📂 Config: {config_path}")
    print(f"📂 Source: {source_base}")
    print(f"📂 Destination: {dest_base}")
    print()
    
    # Load configuration
    try:
        config = load_config(config_path)
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        sys.exit(1)
    
    # Extract configuration
    prune_files = config.get("files_to_prune", [])
    force_replace_files = config.get(
        "files_to_force_replace",
        config.get("files_to_not_replace", []),
    )
    source_folders = config.get("folders_to_copy_from", [])
    
    print(f"📋 Configuration loaded:")
    print(f"   - Files to prune: {len(prune_files)}")
    print(f"   - Files to force replace: {len(force_replace_files)}")
    print(f"   - Source folders: {len(source_folders)}")
    print()
    
    # Step 1: Prune files at destination
    print("🗑️  Step 1: Pruning files...")
    prune_files_at_destination(prune_files, dest_base)
    print()
    
    # Step 2: Collect files to copy
    print("📦 Step 2: Collecting files to copy...")
    files_to_copy = collect_files_to_copy(source_folders, prune_files, force_replace_files, source_base)
    print(f"   Found {len(files_to_copy)} files to copy")
    print()
    
    # Step 3: Copy files to destination
    print("📁 Step 3: Copying files...")
    copy_files_to_destination(files_to_copy, dest_base)
    print()
    
    # Step 4: Update .git/info/exclude
    print("📝 Step 4: Updating .git/info/exclude...")
    update_git_exclude(dest_base)
    print()
    
    print("✅ Synchronization completed successfully!")


if __name__ == "__main__":
    main()
