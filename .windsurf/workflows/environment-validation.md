---
description: Environment validation workflow for OLAF setup
---

# Environment Validation Workflow

Validate the development environment before proceeding with OLAF workflows. Run the following terminal commands and provide a clear report.

## Step 1: Detect Terminal and OS

Run these commands to detect the environment:

**For Windows:**
```bash
echo $SHELL
echo $PSModulePath
echo $TERM
echo $OS
echo $WINDIR
uname -a
```

**For macOS/Linux:**
```bash
echo $SHELL
echo $TERM
uname -a
```

## Step 2: Check Git Installation

```bash
git --version
which git
```

## Step 3: Check Python Installation

```bash
python --version
python3 --version
py --version
which python
which python3
which py
```

## Step 4: Check OLAF Repository

```bash
ls -la ~/.olaf
ls -la ~/.olaf/.git
```

## Required Output Format

Provide a structured report using this format:

```
🔍 OLAF Environment Validation
==================================================
💻 Terminal detected: [terminal_name]
🖥️  Operating System: [os_name] [version]

📦 Git Status: ✅ OK/❌ FAILED
   [git_version_info]

🐍 Python Status: ✅ OK/❌ FAILED  
   [python_version_info]

📁 OLAF Repo Status: ✅ OK/❌ FAILED
   [olaf_repo_info]

🎉 All checks passed! Environment is ready for OLAF workflows.
```

## Success Criteria

Environment is ready when:
- ✅ Git is installed and accessible
- ✅ Python is installed and accessible  
- ✅ ~/.olaf directory exists

## Error Handling

If any check fails:
- Explain what failed and why
- Suggest how to fix it
- Provide specific commands to resolve the issue

**Execute all the commands above and provide the validation report.**
