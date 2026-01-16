#!/usr/bin/env python3
"""
Simple command-line executor for OLAF skills via STRAF
Usage: python run_skill.py --prompt path/to/skill.md --context "key=value, key2=value2"
"""

import argparse
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# Import execution queue
try:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "agentic" / "common"))
    from execution_queue import ExecutionQueue
except ImportError:
    ExecutionQueue = None


def main():
    parser = argparse.ArgumentParser(description='Execute OLAF skill via STRAF')
    parser.add_argument('--prompt', required=True, help='Path to skill prompt file')
    parser.add_argument('--context', required=True, help='Context parameters as "key=value, key2=value2"')
    
    args = parser.parse_args()
    
    # Set AWS region
    if 'AWS_DEFAULT_REGION' not in os.environ:
        os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
    
    # Find project root
    project_root = Path.cwd()
    while project_root != project_root.parent:
        if (project_root / ".olaf").exists():
            break
        project_root = project_root.parent
    
    # Parse context string into dict
    context_params = {}
    for pair in args.context.split(','):
        pair = pair.strip()
        if '=' in pair:
            key, value = pair.split('=', 1)
            context_params[key.strip()] = value.strip()
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3]
    
    # Build command for olaf_strands_agent
    command = [
        sys.executable,
        str(project_root / ".olaf/core/agentic/straf/olaf_strands_agent.py"),
        "--prompt", str(args.prompt),
        "--context", args.context,
        "--tool-mode", "full",
        "--aws-profile", "bedrock",
        "--timeout", "2400",
        "--timestamp", timestamp,
        "--project-root", str(project_root),
        "--no-confirm"
    ]
    
    # Use queue if available
    if ExecutionQueue:
        queue = ExecutionQueue(max_concurrent=3, project_root=project_root)
        
        # Generate description
        skill_name = Path(args.prompt).stem
        description = f"{skill_name}"
        for key in ['learning_objective', 'topic', 'module', 'file']:
            if key in context_params:
                description += f" - {context_params[key]}"
                break
        
        # Enqueue
        result = queue.enqueue_execution(
            command=command,
            description=description,
            parameters=context_params
        )
        
        if result['status'] == 'queued':
            print(f"⏳ Queued: {result['position']}/{result['queue_size']}")
        else:
            print(f"✅ Spawned: PID {result.get('pid')}")
    else:
        # No queue - spawn directly
        process = subprocess.Popen(command, cwd=project_root)
        print(f"✅ Spawned: PID {process.pid}")
    
    print(f"📊 Timestamp: {timestamp}")


if __name__ == '__main__':
    main()
