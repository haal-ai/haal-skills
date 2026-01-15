# Manage Competencies

Complete competency lifecycle management for OLAF framework.

## Overview

This skill provides comprehensive management of OLAF competencies including:
- **Create** - Generate new competencies with proper structure
- **Edit** - Modify existing competencies safely
- **Delete** - Remove competencies with dependency checking
- **Validate** - Verify competency structure and integrity

## Features

- Interactive Python script for all operations
- Automatic structure generation
- Manifest validation
- Dependency checking
- Standards compliance verification

## Usage

Invoke the skill and specify your intent:
- "create competency pdf-analysis"
- "edit competency code-review"
- "delete competency old-tool"
- "validate competency developer-tools"

The skill will call the Python script with appropriate parameters and guide you through the process.

## Architecture

- **Prompt**: Routes request and calls Python script
- **Script**: Handles all CRUD operations interactively
- **Validation**: Ensures OLAF standards compliance
