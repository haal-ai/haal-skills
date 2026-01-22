#!/usr/bin/env python3
"""
Spawn JSDoc Generator

Wrapper script to execute jsdoc-gen command in spawn/background mode.
This ensures the command runs from the correct directory and doesn't block.

⚠️ WARNING: This tool MODIFIES SOURCE CODE by adding JSDoc comments!
Git branch creation is enabled by default for safety.

Usage:
    python spawn-jsdoc-generator.py --repo <repo_path> --output <output_path> [--no-branch]
"""

import sys
import subprocess
import os
import argparse
import json
import uuid
from pathlib import Path
from datetime import datetime


def get_process_lock_file(workspace_path):
    """Get path to process tracking file."""
    locks_dir = os.path.join(workspace_path, '.olaf', 'work', 'straf-locks')
    os.makedirs(locks_dir, exist_ok=True)
    return os.path.join(locks_dir, 'jsdoc-generation-processes.json')


def read_process_registry(lock_file):
    """Read existing process registry."""
    if os.path.exists(lock_file):
        try:
            with open(lock_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'processes': []}
    return {'processes': []}


def write_process_registry(lock_file, registry):
    """Write process registry to file."""
    with open(lock_file, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def register_process(workspace_path, repo_path, output_path, output_mode, process_id=None):
    """Register a new spawned process."""
    lock_file = get_process_lock_file(workspace_path)
    registry = read_process_registry(lock_file)
    
    # Generate process name from repo path
    repo_name = os.path.basename(repo_path)
    process_name = f"jsdoc-gen-{repo_name}"
    
    # Create process entry
    process_entry = {
        'id': str(uuid.uuid4()),
        'name': process_name,
        'repo': repo_path,
        'output': output_path,
        'mode': output_mode,
        'status': 'running',
        'started_at': datetime.now().isoformat(),
        'pid': process_id,
        'log_file': os.path.join(output_path, 'jsdoc-generation.log') if output_mode == 'copy-to-folder' else os.path.join(repo_path, '.jsdoc-generation.log')
    }
    
    registry['processes'].append(process_entry)
    write_process_registry(lock_file, registry)
    
    return process_entry


def main():
    parser = argparse.ArgumentParser(description='Spawn JSDoc inline documentation generation')
    parser.add_argument('--repo', required=True, help='Repository folder for analysis')
    parser.add_argument('--output', required=True, help='Output directory for documented files')
    parser.add_argument('--workspace', required=True, help='Workspace root directory')
    parser.add_argument('--no-branch', action='store_true', help='Skip git branch creation (NOT RECOMMENDED)')
    
    args = parser.parse_args()
    
    # Resolve paths
    repo_path = os.path.abspath(args.repo)
    output_path = os.path.abspath(args.output)
    workspace_path = os.path.abspath(args.workspace)
    
    # Determine output mode
    if repo_path == output_path:
        output_mode = "in-place"
    else:
        output_mode = "copy-to-folder"
    
    # Validate repo folder exists
    if not os.path.exists(repo_path):
        print(f"❌ Error: Repository folder does not exist: {repo_path}")
        sys.exit(1)
    
    if not os.path.isdir(repo_path):
        print(f"❌ Error: Repository path is not a directory: {repo_path}")
        sys.exit(1)
    
    # Create output directory if it doesn't exist (for copy mode)
    if output_mode == "copy-to-folder":
        try:
            os.makedirs(output_path, exist_ok=True)
        except Exception as e:
            print(f"❌ Error: Cannot create output folder: {output_path}")
            print(f"   Reason: {e}")
            sys.exit(1)
    
    # Determine straf-cli path
    cli_dir = os.path.join(workspace_path, '.olaf', 'core', 'agentic', 'straf-cli')
    cli_script = os.path.join(cli_dir, 'cli.py')
    
    # Validate straf-cli exists
    if not os.path.exists(cli_script):
        print(f"❌ Error: straf-cli not found")
        print(f"   Expected at: {cli_script}")
        sys.exit(1)
    
    # Display execution info
    print("=" * 80)
    print("JSDOC INLINE DOCUMENTATION GENERATION (Spawn Mode)")
    print("=" * 80)
    print(f"Repository:     {repo_path}")
    print(f"Output Mode:    {output_mode}")
    print(f"Output Folder:  {output_path}")
    print(f"CLI Directory:  {cli_dir}")
    print(f"Git Branch:     {'Enabled (default)' if not args.no_branch else 'DISABLED (⚠️ NOT RECOMMENDED)'}")
    print(f"Mode:           Asynchronous (background process)")
    print("=" * 80)
    print()
    
    if output_mode == "in-place":
        print("⚠️  CRITICAL WARNINGS:")
        print("  ⚠️  IN-PLACE MODE: Source files will be MODIFIED directly!")
        print("  ⚠️  .js and .ts files will have JSDoc comments added")
        if not args.no_branch:
            print("  ✅ Git branch creation: ENABLED (recommended)")
        else:
            print("  ⚠️  Git branch creation: DISABLED (NOT RECOMMENDED!)")
            print("  ⚠️  Changes will be made to current branch!")
        print()
    else:
        print("ℹ️  COPY MODE:")
        print("  ℹ️  Original source files will NOT be modified")
        print(f"  ℹ️  Documented copies will be saved to: {output_path}")
        print()
    
    print("JSDoc Standards to be Applied:")
    print("  ✓ Comprehensive @param descriptions with types")
    print("  ✓ Detailed @returns documentation with types")
    print("  ✓ @throws for error conditions")
    print("  ✓ @example with usage examples")
    print("  ✓ @remarks for implementation context")
    print("  ✓ @see for related references")
    print()
    print("Target Quality: commit-d02da43 JSDoc standards")
    print("=" * 80)
    print()
    
    # Build command - use CREATE_NEW_PROCESS_GROUP on Windows for true spawn
    python_exe = sys.executable
    
    # Command to execute
    cmd = [
        python_exe,
        'cli.py',
        'jsdoc-gen',
        '--repo', repo_path
    ]
    
    # Add output if different from repo (copy mode)
    if output_mode == "copy-to-folder":
        cmd.extend(['--output', output_path])
    
    # Add --no-branch flag if specified
    if args.no_branch:
        cmd.append('--no-branch')
    
    print("🚀 Starting JSDoc generation in background...")
    print(f"   Command: {' '.join(cmd)}")
    print()
    
    # Create log file for output
    if output_mode == "copy-to-folder":
        log_file_path = os.path.join(output_path, 'jsdoc-generation.log')
    else:
        log_file_path = os.path.join(repo_path, '.jsdoc-generation.log')
    
    # Spawn the process in background - completely detached from VS Code
    try:
        if sys.platform == 'win32':
            # Windows: Use subprocess with complete detachment
            # Create a batch file to run the process independently
            if output_mode == "copy-to-folder":
                batch_file = os.path.join(output_path, 'run_jsdoc_generation.bat')
            else:
                batch_file = os.path.join(repo_path, '.run_jsdoc_generation.bat')
            
            with open(batch_file, 'w') as f:
                f.write('@echo off\n')
                f.write(f'cd /d "{cli_dir}"\n')
                # Run with low priority to minimize system impact
                cmd_str = ' '.join(f'"{arg}"' if ' ' in arg else arg for arg in cmd)
                f.write(f'start /LOW /B {cmd_str} > "{log_file_path}" 2>&1\n')
            
            # Use START command to launch completely independent process
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            CREATE_NO_WINDOW = 0x08000000
            
            # Execute batch file with START to completely detach
            subprocess.Popen(
                ['cmd', '/c', 'start', '/min', batch_file],
                creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW,
                close_fds=True
            )
            
            # Register process
            process_entry = register_process(workspace_path, repo_path, output_path, output_mode)
            
            print(f"✅ Process spawned successfully (independent of VS Code)")
            print(f"   Process ID: {process_entry['id']}")
            print(f"   Process Name: {process_entry['name']}")
            print(f"   Priority: LOW (minimal system impact)")
            print(f"   Log file: {log_file_path}")
        else:
            # Unix: Use nohup and nice for low priority
            log_file = open(log_file_path, 'w')
            
            # Prepend 'nice -n 19' for lowest priority
            nice_cmd = ['nice', '-n', '19'] + cmd
            
            process = subprocess.Popen(
                nice_cmd,
                cwd=cli_dir,
                start_new_session=True,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL,
                close_fds=True
            )
            
            # Register process with PID
            process_entry = register_process(workspace_path, repo_path, output_path, output_mode, process.pid)
            
            print(f"✅ Process spawned successfully (PID: {process.pid})")
            print(f"   Process ID: {process_entry['id']}")
            print(f"   Process Name: {process_entry['name']}")
            print(f"   Priority: LOW (nice 19 - minimal system impact)")
            print(f"   Log file: {log_file_path}")
        
        print()
        print("You can continue working. The process will:")
        print("  1. Analyze repository structure (scan .js and .ts files)")
        print("  2. Generate JSDoc comments for each file (parallel processing)")
        print(f"  3. Save documented files to: {output_path}")
        print("  4. Log progress and results")
        print()
        print("Estimated time:")
        print("  - Small codebase (<100 files): ~5-10 minutes")
        print("  - Medium codebase (100-500 files): ~10-30 minutes")
        print("  - Large codebase (500+ files): ~30-60 minutes")
        print()
        print("⚠️  Process is running OUTSIDE VS Code at LOW priority")
        print("   - Minimal CPU/memory impact on Copilot and VS Code")
        print(f"   - Monitor progress: {log_file_path}")
        print(f"   - Process registry: {get_process_lock_file(workspace_path)}")
        print()
        
        if output_mode == "in-place":
            print("🔍 Review changes after completion:")
            print("   git diff  # See all JSDoc additions")
            print("   git status  # Check modified files")
            print()
            print("To commit changes:")
            print("   git add .")
            print('   git commit -m "docs: add comprehensive JSDoc comments"')
        else:
            print("When complete, documented files will be available at:")
            print(f"  {output_path}/")
            print("  # Copy desired files back to repo if needed")
        print()
        
    except Exception as e:
        print(f"❌ Error spawning process: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
