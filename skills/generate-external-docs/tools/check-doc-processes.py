#!/usr/bin/env python3
"""
Check Documentation Generation Processes

Utility to check status of spawned documentation generation processes.
Updates process status based on log file completion markers.

Usage:
    python check-doc-processes.py [--workspace <path>]
"""

import sys
import os
import json
import argparse
from pathlib import Path
from datetime import datetime


def get_process_lock_file(workspace_path):
    """Get path to process tracking file."""
    locks_dir = os.path.join(workspace_path, '.olaf', 'work', 'straf-locks')
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


def check_process_completion(process):
    """Check if process has completed by examining log file."""
    log_file = process.get('log_file')
    
    if not log_file or not os.path.exists(log_file):
        return None
    
    try:
        # Read last 50 lines of log file
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            last_lines = ''.join(lines[-50:])
            
            # Check for completion markers
            if '[OK] External documentation generated successfully!' in last_lines:
                return 'completed'
            elif 'ERROR' in last_lines or 'FAILED' in last_lines:
                return 'failed'
            else:
                return 'running'
    except:
        return None


def update_process_status(workspace_path):
    """Update status of all processes based on log files."""
    lock_file = get_process_lock_file(workspace_path)
    
    if not os.path.exists(lock_file):
        return {'processes': []}
    
    registry = read_process_registry(lock_file)
    updated = False
    
    for process in registry['processes']:
        if process.get('status') == 'running':
            new_status = check_process_completion(process)
            if new_status and new_status != 'running':
                process['status'] = new_status
                process['completed_at'] = datetime.now().isoformat()
                updated = True
    
    if updated:
        write_process_registry(lock_file, registry)
    
    return registry


def display_processes(registry):
    """Display process status in human-readable format."""
    processes = registry.get('processes', [])
    
    if not processes:
        print("No documentation generation processes found.")
        return
    
    print("=" * 100)
    print("DOCUMENTATION GENERATION PROCESSES")
    print("=" * 100)
    print()
    
    for idx, proc in enumerate(processes, 1):
        status_emoji = {
            'running': '🔄',
            'completed': '✅',
            'failed': '❌'
        }.get(proc.get('status', 'unknown'), '❓')
        
        print(f"{idx}. {status_emoji} {proc.get('name', 'unknown')}")
        print(f"   ID: {proc.get('id', 'N/A')}")
        print(f"   Status: {proc.get('status', 'unknown').upper()}")
        print(f"   Root: {proc.get('root', 'N/A')}")
        print(f"   Output: {proc.get('output', 'N/A')}")
        print(f"   Started: {proc.get('started_at', 'N/A')}")
        
        if proc.get('completed_at'):
            print(f"   Completed: {proc.get('completed_at', 'N/A')}")
        
        if proc.get('pid'):
            print(f"   PID: {proc.get('pid')}")
        
        log_file = proc.get('log_file')
        if log_file:
            log_exists = "✓" if os.path.exists(log_file) else "✗"
            print(f"   Log: {log_file} [{log_exists}]")
        
        print()
    
    # Summary
    running = sum(1 for p in processes if p.get('status') == 'running')
    completed = sum(1 for p in processes if p.get('status') == 'completed')
    failed = sum(1 for p in processes if p.get('status') == 'failed')
    
    print("-" * 100)
    print(f"Summary: {len(processes)} total | {running} running | {completed} completed | {failed} failed")
    print("-" * 100)


def main():
    parser = argparse.ArgumentParser(description='Check documentation generation processes')
    parser.add_argument('--workspace', help='Workspace root directory', default=os.getcwd())
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    workspace_path = os.path.abspath(args.workspace)
    
    # Update process status
    registry = update_process_status(workspace_path)
    
    if args.json:
        print(json.dumps(registry, indent=2))
    else:
        display_processes(registry)


if __name__ == '__main__':
    main()
