#!/usr/bin/env python3
"""
Environment Information Generator
Creates an environment info file in staging directory with current datetime, OS, and shell information.
"""

import os
import platform
import glob
from datetime import datetime
from pathlib import Path

def get_shell_info():
    """Detect the current shell being used."""
    # Try to get from environment variables
    shell_env = os.environ.get('SHELL', '')
    if shell_env:
        return Path(shell_env).name
    
    # Windows specific detection
    if platform.system() == 'Windows':
        # Check for PowerShell
        if os.environ.get('PSModulePath'):
            ps_version = os.environ.get('PSVersionTable', '')
            if 'Core' in ps_version:
                return 'pwsh'  # PowerShell Core
            else:
                return 'powershell'  # Windows PowerShell
        
        # Check for Command Prompt
        comspec = os.environ.get('COMSPEC', '')
        if 'cmd.exe' in comspec.lower():
            return 'cmd'
    
    # Unix-like systems
    parent_process = os.getppid()
    try:
        import psutil
        parent = psutil.Process(parent_process)
        return parent.name()
    except (ImportError, Exception):
        # Fallback: try to read from /proc (Linux)
        try:
            with open(f'/proc/{parent_process}/comm', 'r') as f:
                return f.read().strip()
        except (FileNotFoundError, PermissionError):
            pass
    
    # Final fallback
    return 'unknown'

def main():
    # Get the staging directory path
    script_dir = Path(__file__).parent
    staging_dir = script_dir.parent.parent.parent.parent / "work" / "staging"
    
    # Ensure staging directory exists
    staging_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate current timestamp
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Gather environment information
    env_info = {
        'timestamp': current_time,
        'datetime_iso': datetime.now().isoformat(),
        'os': platform.system(),
        'os_version': platform.release(),
        'architecture': platform.machine(),
        'shell': get_shell_info(),
        'python_version': platform.python_version(),
        'hostname': platform.node(),
        'user': os.environ.get('USER', os.environ.get('USERNAME', 'unknown'))
    }
    
    # Define the environment file
    env_file = staging_dir / "olaf-env.txt"
    
    # Remove previous environment files
    previous_files = glob.glob(str(staging_dir / "olaf-env.txt"))
    for file_path in previous_files:
        try:
            os.remove(file_path)
            print(f"Removed previous environment file: {file_path}")
        except OSError as e:
            print(f"Warning: Could not remove {file_path}: {e}")
    
    # Create the new environment file
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write("# OLAF Environment Information\n")
            f.write(f"# Generated: {env_info['datetime_iso']}\n\n")
            
            for key, value in env_info.items():
                f.write(f"{key}={value}\n")
        
        print(f"Created environment file: {env_file}")
        print(f"Current timestamp: {current_time}")
        print(f"Operating System: {env_info['os']} {env_info['os_version']}")
        print(f"Architecture: {env_info['architecture']}")
        print(f"Shell: {env_info['shell']}")
        print(f"Python: {env_info['python_version']}")
        print(f"User: {env_info['user']} @ {env_info['hostname']}")
        
        return env_info
    except OSError as e:
        print(f"Error creating environment file: {e}")
        return None

if __name__ == "__main__":
    main()