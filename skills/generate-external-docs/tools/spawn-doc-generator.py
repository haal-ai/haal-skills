#!/usr/bin/env python3
"""
Spawn Documentation Generator

Wrapper script to execute doc-external command in spawn/background mode.
This ensures the command runs from the correct directory and doesn't block.

Usage:
    python spawn-doc-generator.py --root <root_path> --output <output_path>
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
    return os.path.join(locks_dir, 'doc-generation-processes.json')


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


def register_process(workspace_path, root_path, output_path, process_id=None):
    """Register a new spawned process."""
    lock_file = get_process_lock_file(workspace_path)
    registry = read_process_registry(lock_file)
    
    # Generate process name from root path
    root_name = os.path.basename(root_path)
    process_name = f"doc-gen-{root_name}"
    
    # Create process entry
    process_entry = {
        'id': str(uuid.uuid4()),
        'name': process_name,
        'root': root_path,
        'output': output_path,
        'status': 'running',
        'started_at': datetime.now().isoformat(),
        'pid': process_id,
        'log_file': os.path.join(output_path, 'generation.log')
    }
    
    registry['processes'].append(process_entry)
    write_process_registry(lock_file, registry)
    
    return process_entry


def main():
    parser = argparse.ArgumentParser(description='Spawn external documentation generation')
    parser.add_argument('--root', required=True, help='Root folder for analysis')
    parser.add_argument('--output', required=True, help='Output directory for documentation')
    parser.add_argument('--workspace', required=True, help='Workspace root directory')
    
    args = parser.parse_args()
    
    # Resolve paths
    root_path = os.path.abspath(args.root)
    output_path = os.path.abspath(args.output)
    # Normalize: enforce plural 'documentations' segment under product/
    output_path = output_path.replace(os.sep + 'product' + os.sep + 'documentation' + os.sep,
                                      os.sep + 'product' + os.sep + 'documentations' + os.sep)
    output_path = output_path.replace('/product/documentation/', '/product/documentations/')
    workspace_path = os.path.abspath(args.workspace)
    
    # Validate root folder exists
    if not os.path.exists(root_path):
        print(f"❌ Error: Root folder does not exist: {root_path}")
        sys.exit(1)
    
    if not os.path.isdir(root_path):
        print(f"❌ Error: Root path is not a directory: {root_path}")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
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
    print("EXTERNAL DOCUMENTATION GENERATION (Spawn Mode)")
    print("=" * 80)
    print(f"Root Folder:    {root_path}")
    print(f"Output Folder:  {output_path}")
    print(f"CLI Directory:  {cli_dir}")
    print(f"Mode:           Asynchronous (background process)")
    print("=" * 80)
    print()
    print("Documentation Files to Generate:")
    print("  ✓ index.md - Project overview")
    print("  ✓ architecture.md - Technical architecture + Mermaid diagrams")
    print("  ✓ control-flow.md - Process flows + Mermaid diagrams")
    print("  ✓ use-cases.md - Functional use cases")
    print("  ✓ mkdocs.yml - MkDocs configuration")
    print("  ✓ VALIDATION_REPORT.md - Quality validation")
    print("=" * 80)
    print()
    
    # Build command - use CREATE_NEW_PROCESS_GROUP on Windows for true spawn
    python_exe = sys.executable
    
    # Command to execute
    cmd = [
        python_exe,
        'cli.py',
        'doc-external',
        '--root', root_path,
        '--output', output_path,
        '--no-branch'
    ]
    
    print("🚀 Starting documentation generation in background...")
    print(f"   Command: {' '.join(cmd)}")
    print()
    
    # Create log file for output
    log_file_path = os.path.join(output_path, 'generation.log')
    
    # Spawn the process in background - completely detached from VS Code
    try:
        if sys.platform == 'win32':
            # Windows: Use subprocess with complete detachment
            # Create a batch file to run the process independently
            batch_file = os.path.join(output_path, 'run_generation.bat')
            
            with open(batch_file, 'w') as f:
                f.write('@echo off\n')
                f.write(f'cd /d "{cli_dir}"\n')
                # Run with low priority to minimize system impact
                f.write(f'start /LOW /B "{python_exe}" cli.py doc-external --root "{root_path}" --output "{output_path}" --no-branch > "{log_file_path}" 2>&1\n')
            
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
            process_entry = register_process(workspace_path, root_path, output_path)
            
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
            process_entry = register_process(workspace_path, root_path, output_path, process.pid)
            
            print(f"✅ Process spawned successfully (PID: {process.pid})")
            print(f"   Process ID: {process_entry['id']}")
            print(f"   Process Name: {process_entry['name']}")
            print(f"   Priority: LOW (nice 19 - minimal system impact)")
            print(f"   Log file: {log_file_path}")
        print()
        print("You can continue working. The process will:")
        print("  1. Analyze repository structure")
        print("  2. Generate documentation files (parallel)")
        print("  3. Validate documentation quality")
        print(f"  4. Save files to: {output_path}")
        print()
        print("Estimated time: 5-15 minutes (depending on codebase size)")
        print()
        print("⚠️  Process is running OUTSIDE VS Code at LOW priority")
        print("   - Minimal CPU/memory impact on Copilot and VS Code")
        print(f"   - Monitor progress: {log_file_path}")
        print(f"   - Process registry: {get_process_lock_file(workspace_path)}")
        print()
        print("When complete, files will be available at:")
        print(f"  {os.path.join(output_path, 'content', 'index.md')}")
        print(f"  {os.path.join(output_path, 'content', 'architecture.md')}")
        print(f"  {os.path.join(output_path, 'content', 'control-flow.md')}")
        print(f"  {os.path.join(output_path, 'content', 'use-cases.md')}")
        print(f"  {os.path.join(output_path, 'mkdocs.yml')}")
        print()
        print("To preview documentation:")
        print(f"  cd {output_path}")
        print("  mkdocs serve")
        print("  # Then open http://localhost:8000")
        print()
        
    except Exception as e:
        print(f"❌ Error spawning process: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
