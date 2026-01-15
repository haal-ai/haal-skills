#!/usr/bin/env python3
# ============================================================================
# OLAF Competency Collection Selector
# ============================================================================
# Purpose: Allow end-users to select a competency collection (or create custom)
#          and generate the query-competency-index.md file
#
# Usage: python select_collection.py [--collection developer] [--custom] [--list]
#
# ============================================================================

import json
import argparse
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

class CollectionSelector:
    # Constants for maintainability
    TIMESTAMP_FORMAT = "%Y%m%d-%H%M"
    INDEX_FILENAME = "query-competency-index.md"
    COLLECTIONS_FILENAME = "competency-collections.json"
    CONDENSED_FILENAME = "olaf-framework-condensed.md"
    MANIFEST_FILENAME = "competency-manifest.json"
    
    # Pattern extraction constants
    MAPPINGS_START_MARKER = "## Mappings\n\n["
    MAPPINGS_END_MARKER = "]\n\nend-of-competency-index"
    COMPETENCIES_START_MARKER = "<!-- OLAF_COMPETENCIES_START -->\n"
    COMPETENCIES_END_MARKER = "\n<!-- OLAF_COMPETENCIES_END -->"
    
    # Menu constants
    MIN_MENU_CHOICE = 1
    MAX_ALIASES_DISPLAY = 3
    
    def __init__(self, execution_mode=2, *, local_root: str | None = None):
        self.script_dir = Path(__file__).parent

        # Support running from either:
        # - <repo>/skills/<skill>/scripts (workspace root layout)
        # - tools/ (workspace root) OR ~/.olaf/tools (global install)
        if self.script_dir.name == "tools":
            # tools/ (workspace root) OR ~/.olaf/tools (global install)
            self.repo_root = self.script_dir.parent
            self.core_dir = self.repo_root
        elif self.script_dir.parent.parent.name == "skills":
            # <repo>/skills/<skill>/scripts (workspace root layout)
            self.repo_root = self.script_dir.parents[3]
            self.core_dir = self.repo_root
        else:
            # Best-effort fallback
            self.repo_root = self.script_dir.parents[1]
            self.core_dir = self.repo_root
        
        # Global paths (user-wide)
        home_dir = Path.home()
        self.global_olaf_dir = home_dir / ".olaf"
        self.global_core_dir = self.global_olaf_dir
        self.global_collections_file = self.global_core_dir / "reference" / self.COLLECTIONS_FILENAME
        self.global_competencies_dir = self.global_core_dir / "competencies"

        # Local paths (project-specific)
        self.local_root = Path(local_root).resolve() if local_root else None
        self.project_root = self.local_root
        self.local_olaf_dir = (self.local_root / ".olaf") if self.local_root else self.repo_root
        self.local_core_dir = self.local_root if self.local_root else self.core_dir
        self.local_competencies_dir = self.local_core_dir / "competencies"

        # Prefer local competency-collections.json; fallback to legacy local-competency-collections.json
        local_ref = self.local_core_dir / "reference"
        preferred_local_collections = local_ref / self.COLLECTIONS_FILENAME
        legacy_local_collections = local_ref / "local-competency-collections.json"
        self.local_collections_file = (
            preferred_local_collections if preferred_local_collections.exists() else legacy_local_collections
        )
        
        # Collections are always read from the project-local manifest.
        # This file also defines which competencies are local vs global.
        self.collections_file = self.local_collections_file
        
        # Output index to local project's reference directory
        self.index_output = self.local_core_dir / "reference" / self.INDEX_FILENAME
        self.execution_mode = execution_mode  # Configurable auto_execution_mode
        
    def _handle_error(self, message: str, exit_code: int = 1):
        """Consistent error handling with exit"""
        print(f"❌ {message}")
        sys.exit(exit_code)
    
    def show_logo(self):
        print("\n" + "="*60)
        print("  OLAF Skill Collection Selector v1.0")
        print("  Generate personalized skill index")
        print("="*60 + "\n")
    
    def load_collections(self) -> Dict:
        """Load collections from JSON file"""
        try:
            with open(self.collections_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            self._handle_error(f"Collections file not found: {self.collections_file}")
        except json.JSONDecodeError:
            self._handle_error(f"Invalid JSON in: {self.collections_file}")
    
    def load_hybrid_collections(self) -> Dict:
        """Load and merge global and local collections"""
        # Load global collections
        global_collections = {"collections": [], "metadata": {}}
        try:
            with open(self.global_collections_file, 'r') as f:
                global_collections = json.load(f)
            print(f"✓ Loaded {len(global_collections.get('collections', []))} global collections")
        except FileNotFoundError:
            print(f"⚠️  Global collections file not found: {self.global_collections_file}")
        except json.JSONDecodeError:
            print(f"⚠️  Invalid JSON in global collections file: {self.global_collections_file}")
        
        # Load local collections
        local_collections = {"collections": [], "metadata": {}}
        try:
            with open(self.local_collections_file, 'r') as f:
                local_collections = json.load(f)
            print(f"✓ Loaded {len(local_collections.get('collections', []))} local collections")
        except FileNotFoundError:
            print(f"ℹ️  No local collections file found (project-specific collections only)")
        except json.JSONDecodeError:
            print(f"⚠️  Invalid JSON in local collections file: {self.local_collections_file}")
        
        # Merge collections
        merged = {
            "version": "1.1.0",
            "metadata": {
                **global_collections.get("metadata", {}),
                "local_collections_count": len(local_collections.get("collections", [])),
                "global_collections_count": len(global_collections.get("collections", [])),
                "last_merged": datetime.now().isoformat()
            },
            "collections": []
        }
        
        # Add global collections first
        for collection in global_collections.get("collections", []):
            collection["scope"] = "global"
            merged["collections"].append(collection)
        
        # Add local collections (override if same ID)
        local_ids = set()
        for collection in local_collections.get("collections", []):
            collection["scope"] = "local"
            merged["collections"].append(collection)
            local_ids.add(collection["id"])
        
        print(f"✓ Merged collections: {len(merged['collections'])} total")
        return merged

    def _get_competency_locations(self, collections: Dict) -> dict[str, str]:
        loc = collections.get("competency_locations")
        if isinstance(loc, dict):
            out: dict[str, str] = {}
            for k, v in loc.items():
                if isinstance(k, str) and isinstance(v, str):
                    out[k] = v
            return out
        return {}

    def _competency_declared_location(self, competency_id: str, locations: dict[str, str]) -> str:
        return locations.get(competency_id) or locations.get("default") or "global"
    
    def clean_invalid_competencies(self, collections: Dict) -> Dict:
        """Remove competencies that don't exist in their declared location (global/local)."""
        locations = self._get_competency_locations(collections)

        for collection in collections.get('collections', []):
            current_comps = collection.get('competencies', [])
            valid: list[str] = []
            removed_msgs: list[str] = []

            for comp_id in current_comps:
                declared = self._competency_declared_location(comp_id, locations)

                global_manifest = self.global_competencies_dir / comp_id / self.MANIFEST_FILENAME
                local_manifest = self.local_competencies_dir / comp_id / self.MANIFEST_FILENAME

                global_exists = global_manifest.exists()
                local_exists = local_manifest.exists()

                if declared == "local":
                    if local_exists:
                        valid.append(comp_id)
                    else:
                        note = "missing"
                        if global_exists:
                            note = "exists globally but declared local"
                        removed_msgs.append(f"{comp_id} ({note})")
                else:  # global (default)
                    if global_exists:
                        valid.append(comp_id)
                    else:
                        note = "missing"
                        if local_exists:
                            note = "exists locally but declared global"
                        removed_msgs.append(f"{comp_id} ({note})")

            if removed_msgs:
                print(f"[CLEAN] {collection.get('id')}: Removing competencies: {', '.join(removed_msgs)}")
                collection['competencies'] = valid

        return collections
    
    def _get_timestamp(self) -> str:
        """Get formatted timestamp for consistency"""
        return datetime.now().strftime(self.TIMESTAMP_FORMAT)
    
    def show_execution_mode_info(self):
        """Display information about execution modes"""
        modes = {
            0: "Manual - User confirmation required for each step",
            1: "Safe - Automatic execution with safety checks (recommended)",
            2: "Normal - Balanced automatic execution",
            3: "Turbo - Maximum automation (experimental)"
        }
        
        print(f"🚀 Execution Mode: {self.execution_mode} - {modes.get(self.execution_mode, 'Unknown')}")
        print("   Modes: 0=Manual | 1=Safe | 2=Normal | 3=Turbo")
    
    def load_manifest(self, skill_id: str) -> Dict:
        """Load competency manifest from either global or local competencies."""
        candidates = [
            self.global_competencies_dir / skill_id / self.MANIFEST_FILENAME,
            self.local_competencies_dir / skill_id / self.MANIFEST_FILENAME,
        ]

        for manifest_path in candidates:
            try:
                if not manifest_path.exists():
                    continue
                with open(manifest_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                continue

        print(f"⚠️  Manifest not found or invalid for: {skill_id}")
        return None
    
    def show_collections(self, collections: Dict):
        """Display all available collections"""
        print("📋 Available Collections:")
        print("-" * 60)
        
        for i, collection in enumerate(collections['collections'], 1):
            skill_count = len(collection.get('competencies', []))
            scope = collection.get('scope', 'unknown')
            scope_icon = "🌍" if scope == "global" else "🏠" if scope == "local" else "❓"
            print(f"\n  [{i}] {collection['name']} {scope_icon}")
            print(f"      ID: {collection['id']}")
            print(f"      Scope: {scope}")
            print(f"      Description: {collection['description']}")
            print(f"      Skills: {skill_count}")
            for skill in collection.get('competencies', []):
                print(f"         • {skill}")
        print()
    
    def show_menu(self, collections: Dict) -> str:
        """Interactive menu to select collection"""
        options = [c['id'] for c in collections['collections']] + ["custom"]
        
        print("🎯 Select Collection:")
        print("-" * 60)
        
        for i, option in enumerate(options, 1):
            if option == "custom":
                print(f"  [{i}] Create Custom Selection")
            else:
                coll = next(c for c in collections['collections'] if c['id'] == option)
                print(f"  [{i}] {coll['name']}")
        
        print()
        while True:
            try:
                choice = int(input(f"Enter number (1-{len(options)}): "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                print("❌ Invalid selection")
            except ValueError:
                print("❌ Please enter a number")
    
    def get_available_competencies(self) -> List[Dict]:
        """Get all available competencies from both global and local directories"""
        competencies = []
        
        # Load global competencies
        if self.global_competencies_dir.exists():
            for comp_dir in self.global_competencies_dir.iterdir():
                if comp_dir.is_dir():
                    manifest_path = comp_dir / "competency-manifest.json"
                    if manifest_path.exists():
                        try:
                            comp_data = json.load(open(manifest_path, 'r'))
                            comp_data['scope'] = 'global'
                            competencies.append(comp_data)
                        except (json.JSONDecodeError, KeyError):
                            continue
        
        # Load local competencies
        if self.local_competencies_dir.exists():
            for comp_dir in self.local_competencies_dir.iterdir():
                if comp_dir.is_dir():
                    manifest_path = comp_dir / "competency-manifest.json"
                    if manifest_path.exists():
                        try:
                            comp_data = json.load(open(manifest_path, 'r'))
                            comp_data['scope'] = 'local'
                            competencies.append(comp_data)
                        except (json.JSONDecodeError, KeyError):
                            continue
        
        return sorted(competencies, key=lambda x: x['metadata']['id'])
    
    def select_competencies_interactive(self, collections: Dict) -> List[str]:
        """Allow user to select competencies"""
        competencies = self.get_available_competencies()
        
        self._display_competency_menu(competencies)
        selected = self._get_user_selections(competencies)
        
        if not selected:
            selected = self._get_default_selections(collections)
        
        return list(set(selected))
    
    def _display_competency_menu(self, competencies: List[Dict]):
        """Display available competencies in a formatted menu"""
        print("\n🎯 Select competencies for custom collection:")
        print("-" * 60)
        
        for i, comp in enumerate(competencies, 1):
            print(f"  [{i}] {comp['metadata']['id']}")
            print(f"      {comp['metadata']['name']}")
        print()
    
    def _get_user_selections(self, competencies: List[Dict]) -> List[str]:
        """Get and validate user selections from input"""
        selected = []
        while True:
            try:
                choices = input("Enter numbers separated by commas (e.g., 1,3,5): ").strip()
                if not choices:
                    break
                
                indices = self._parse_user_choices(choices)
                selected = self._validate_indices(indices, competencies)
                break
            except ValueError:
                print("Please enter valid numbers")
        
        return selected
    
    def _parse_user_choices(self, choices: str) -> List[int]:
        """Parse user input into list of indices"""
        return [int(x.strip()) - 1 for x in choices.split(',')]
    
    def _validate_indices(self, indices: List[int], competencies: List[Dict]) -> List[str]:
        """Validate indices and return selected competency IDs"""
        selected = []
        for idx in indices:
            if 0 <= idx < len(competencies):
                selected.append(competencies[idx]['metadata']['id'])
            else:
                print(f"Invalid index: {idx + 1}")
        return selected
    
    def _get_default_selections(self, collections: Dict) -> List[str]:
        """Get default selections when user provides no input"""
        core_coll = next((c for c in collections['collections'] if c['id'] == 'core'), None)
        return list(core_coll['competencies']) if core_coll else []
    
    def build_index_entry(self, entry_point: Any, competency_id: str) -> str:
        """Build a single index entry"""
        # Handle both dict and string entry_point formats
        if isinstance(entry_point, str):
            # Simple file path string - default to global
            file_path = f"{competency_id}/{entry_point}"
            return f'  [[], "~/.olaf/skills/{file_path}", "Act"]'
        
        # Dictionary format with metadata
        aliases = entry_point.get('aliases', [])
        file_path = f"{competency_id}/{entry_point.get('file', '')}"
        protocol = entry_point.get('protocol', 'Act')
        location = entry_point.get('location', 'global')  # Default to global
        
        # Add memory map ID prefix
        if location == 'local':
            file_path = f"skills/{file_path}"
        else:
            file_path = f"~/.olaf/skills/{file_path}"
        
        # Format: [["alias1", "alias2", ...], "path/to/file.md", "Protocol"]
        aliases_str = ', '.join(f'"{a}"' for a in aliases)
        return f'  [{{{aliases_str}}}, "{file_path}", "{protocol}"]'
    
    def _validate_kernel_competencies(self, kernel_competencies: List[str]) -> List[str]:
        """Validate and filter kernel competencies, removing invalid ones"""
        available_competencies = self.get_available_competencies()
        available_ids = [c['metadata']['id'] for c in available_competencies]
        
        valid_kernels = [comp for comp in kernel_competencies if comp in available_ids]
        invalid_kernels = [comp for comp in kernel_competencies if comp not in available_ids]
        
        if invalid_kernels:
            print(f"⚠️  Removing invalid kernel competencies: {', '.join(invalid_kernels)}")
            print(f"✅ Valid kernel competencies: {', '.join(valid_kernels)}")
            
        if not valid_kernels:
            self._handle_error("No valid kernel competencies after filtering")
            
        return valid_kernels

    def generate_index(self, selected_competencies: List[str], collection_name: str) -> str:
        """Generate the skill index from competency manifests"""
        print("\n🔧 Generating index from selected competencies...")
        
        # Deduplicate entries by skill_id (aligns with generated /olaf-* commands).
        # If the same skill_id appears in multiple competencies, keep a single mapping and merge aliases.
        entries: dict[str, tuple[str, str, set[str]]] = {}
        legacy_entries: list[str] = []
        duplicates_removed = 0
        timestamp = self._get_timestamp()
        
        for competency_id in selected_competencies:
            manifest = self.load_manifest(competency_id)
            
            if not manifest:
                print(f"  ⚠️  Skipping (no manifest): {competency_id}")
                continue
            
            print(f"  ✓ Processing: {competency_id}")
            
            # New BOM-based structure: competency manifest references skill manifests
            bom = manifest.get('bom', {})
            entry_points = bom.get('entry_points', [])
            
            if not entry_points:
                # Fallback to legacy entry_points at root level (deprecated)
                entry_points = manifest.get('entry_points', [])
                if entry_points:
                    print(f"  ⚠️  Using legacy entry_points format for {competency_id}")
                    for entry_point in entry_points:
                        entry = self.build_index_entry(entry_point, competency_id)
                        legacy_entries.append(entry)
                continue
            
            # Process BOM entry_points: each references a skill manifest
            for ep in entry_points:
                skill_id = ep.get('id')
                skill_manifest_path = ep.get('manifest', '')
                skill_location = ep.get('location', 'global')  # Default to global
                
                if not skill_manifest_path:
                    print(f"  ⚠️  No manifest path for entry point {skill_id}")
                    continue
                
                # The manifest path in competency is relative to core
                rel = skill_manifest_path.lstrip('/')

                # Prefer the location specified by the entry point
                preferred_core = self.local_core_dir if skill_location == 'local' else self.global_core_dir
                fallbacks = [preferred_core / rel]
                if preferred_core != self.global_core_dir:
                    fallbacks.append(self.global_core_dir / rel)
                if preferred_core != self.local_core_dir:
                    fallbacks.append(self.local_core_dir / rel)

                skill_manifest_file = None
                for cand in fallbacks:
                    if cand.exists():
                        skill_manifest_file = cand
                        break
                if not skill_manifest_file:
                    print(f"  ⚠️  Could not find skill manifest {skill_manifest_path}")
                    continue
                
                try:
                    with open(skill_manifest_file, 'r') as f:
                        skill_manifest = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    print(f"  ⚠️  Could not load skill manifest {skill_manifest_path}: {e}")
                    continue
                
                # Extract data from skill manifest
                metadata = skill_manifest.get('metadata', {})
                skill_bom = skill_manifest.get('bom', {})
                
                protocol = metadata.get('protocol', 'Act')
                aliases = metadata.get('aliases', [])
                prompts = skill_bom.get('prompts', [])
                
                if not prompts:
                    print(f"  ⚠️  No prompts defined in skill manifest {skill_id}")
                    continue
                
                # Use first prompt
                first_prompt = prompts[0]
                prompt_path = first_prompt.get('path', '').lstrip('/')
                
                # Build final path: skills/{skill-id}/{prompt-path}
                skill_dir = Path(skill_manifest_path).parent  # e.g., skills/review-code
                full_path = f"{skill_dir}/{prompt_path}"
                
                # Add memory map ID prefix based on skill_location
                if skill_location == 'local':
                    full_path = f"skills/{full_path}"
                else:  # global or any other value defaults to global
                    full_path = f"~/.olaf/skills/{full_path}"
                
                # Deduplicate by skill_id and merge aliases
                if not skill_id:
                    skill_id = f"{full_path}|{protocol}"

                if skill_id in entries:
                    duplicates_removed += 1
                    prev_path, prev_protocol, prev_aliases = entries[skill_id]
                    prev_aliases.update(aliases)
                    entries[skill_id] = (prev_path, prev_protocol, prev_aliases)
                else:
                    entries[skill_id] = (full_path, protocol, set(aliases))


        
        index_entries: list[str] = []
        for _, (full_path, protocol, aliases_set) in entries.items():
            aliases_str = ', '.join(f'"{a}"' for a in sorted(aliases_set))
            index_entries.append(f'  [{{{aliases_str}}}, "{full_path}", "{protocol}"]')

        index_entries.extend(legacy_entries)

        if duplicates_removed:
            print(f"ℹ️  Deduplicated mappings: removed {duplicates_removed} duplicate entries")

        # Build the markdown content
        content = f"""<olaf-query-competency-index>
# Skill Index

**Last Updated:** {timestamp} CEDT
**Collection:** {collection_name}
**Generated By:** select_collection.py

## How to Use This Index

If requested for a skill, iterate through the mappings below.
For each mapping, check if the user request matches the patterns.
Use the first matching mapping with its file and protocol.

## Collection Information

- **Name:** {collection_name}
- **Skills Included:** {', '.join(selected_competencies)}
- **Total Entry Points:** {len(index_entries)}

## Mappings

[
{chr(10).join(index_entries)}
]

end-of-competency-index
</olaf-query-competency-index>
"""
        return content
    
    def save_index(self, content: str):
        """Save generated index to file"""
        try:
            self.index_output.parent.mkdir(parents=True, exist_ok=True)
            with open(self.index_output, 'w') as f:
                f.write(content)
            print(f"\n✅ Index generated successfully!")
            print(f"   Output: {self.index_output}")
        except Exception as e:
            self._handle_error(f"Error saving index: {e}")
    
    def save_active_collection(self, collection_id: str):
        """Update the active_collection field in collections JSON file"""
        try:
            with open(self.collections_file, 'r') as f:
                collections = json.load(f)
            
            # Update the active_collection in metadata
            if 'metadata' not in collections:
                collections['metadata'] = {}
            
            collections['metadata']['active_collection'] = collection_id
            collections['metadata']['lastUpdated'] = datetime.now().isoformat()
            
            # Write back to file
            with open(self.collections_file, 'w') as f:
                json.dump(collections, f, indent=2)
            
            print(f"✅ Active collection updated: {collection_id}")
        except Exception as e:
            print(f"⚠️  Warning: Could not update active collection in JSON: {e}")
    
    def extract_patterns_from_index(self, content: str) -> List[str]:
        """Extract competency patterns from index content for condensed framework (compressed format without aliases)"""
        mappings_section = self._extract_mappings_section(content)
        if not mappings_section:
            return []
        
        return self._parse_mapping_lines(mappings_section)
    
    def _extract_mappings_section(self, content: str) -> str:
        """Extract the mappings section from index content"""
        start_marker = "## Mappings\n\n["
        end_marker = "]\n\nend-of-competency-index"
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        
        if start_idx == -1 or end_idx == -1:
            print("⚠️  Could not extract patterns from index")
            return ""
        
        # Extract mapping entries (skip opening '[' from marker)
        return content[start_idx + len(start_marker):end_idx]
    
    def _parse_mapping_lines(self, mappings_section: str) -> List[str]:
        """Parse individual mapping lines into patterns"""
        patterns = []
        lines = mappings_section.strip().split('\n')
        
        for line in lines:
            pattern = self._parse_single_mapping_line(line.strip())
            if pattern:
                patterns.append(pattern)
        
        return patterns
    
    def _parse_single_mapping_line(self, line: str) -> str:
        """Parse a single mapping line into a pattern"""
        if not line:
            return ""
        
        # Clean up line formatting
        line = self._clean_mapping_line(line)
        if not line:
            return ""
        
        try:
            # Extract components: aliases, file_path, protocol
            aliases = self._extract_aliases_from_line(line)
            file_path = self._extract_file_path_from_line(line)
            protocol = self._extract_protocol_from_line(line)
            
            if not all([aliases, file_path, protocol]):
                return ""
            
            # Build pattern: →path|Protocol (compressed format - no aliases for condensed framework)
            return '→' + file_path + '|' + protocol
            
        except Exception as e:
            print(f"⚠️  Error parsing line: {line} ({e})")
            return ""
    
    def _clean_mapping_line(self, line: str) -> str:
        """Clean and normalize a mapping line"""
        # Remove leading/trailing brackets
        if line.startswith('['):
            line = line[1:]
        if line.endswith(']'):
            line = line[:-1]
        
        return line.strip()
    
    def _extract_aliases_from_line(self, line: str) -> List[str]:
        """Extract aliases from a mapping line"""
        aliases_start = line.find('{')
        aliases_end = line.find('}')
        if aliases_start == -1 or aliases_end == -1:
            return []
        
        aliases_str = line[aliases_start+1:aliases_end]
        return [a.strip().strip('"') for a in aliases_str.split(',')]
    
    def _extract_file_path_from_line(self, line: str) -> str:
        """Extract file path from a mapping line (handles both old and new formats)"""
        aliases_end = line.find('}')
        if aliases_end == -1:
            return ""
        
        file_start = line.find('"', aliases_end)
        file_end = line.find('"', file_start + 1)
        if file_start == -1 or file_end == -1:
            return ""
        
        file_path = line[file_start+1:file_end]
        
        # Handle [id:...] prefix - remove it for condensed framework
        if file_path.startswith('[id:'):
            id_end = file_path.find(']')
            if id_end != -1:
                file_path = file_path[id_end+1:]  # Remove [id:...] prefix
        
        return file_path
    
    def _extract_protocol_from_line(self, line: str) -> str:
        """Extract protocol from a mapping line (handles both old and new formats)"""
        # Find the last comma that separates file path from protocol
        # This works for both: [{"aliases"}, "file.md", "Act"] and [{"aliases"}, "[id:...]file.md", "Act"]
        protocol_start = line.rfind(',')
        if protocol_start == -1:
            return ""
        
        return line[protocol_start+1:].strip().strip('"')
    
    def _merge_with_kernels(self, kernel_competencies: List[str], selected_competencies: List[str]) -> List[str]:
        """Merge kernel competencies with selected ones, avoiding duplicates"""
        return list(dict.fromkeys(kernel_competencies + selected_competencies))

    def update_condensed_framework(self, index_content: str, collection_name: str):
        """Update condensed framework - skip competency patterns generation as requested"""
        print(f"✅ Condensed framework update skipped (as configured)")
        print(f"   Competency patterns section will not be modified")
        print(f"   Collection: {collection_name}")
        return True
    
    def sync_olaf_commands(self, selected_competencies: List[str]):
        """Synchronize /olaf-* command files for selected competencies"""
        print("\n🔧 Synchronizing /olaf-* commands...")

        if not self.project_root:
            print("⚠️  No project root provided; skipping /olaf-* command generation")
            return
        
        # Build map: skill_id -> core/skills/<skill-id>/prompts/<main>.md (from skill manifest)
        competency_map = {}
        for comp_id in selected_competencies:
            manifest = self.load_manifest(comp_id)
            if not manifest:
                continue
            bom = manifest.get('bom', {})
            entry_points = bom.get('entry_points', [])
            if not entry_points:
                # Legacy fallback (root-level entry_points)
                entry_points = manifest.get('entry_points', [])
            for ep in entry_points:
                skill_id = ep.get('id')
                skill_manifest_rel = ep.get('manifest')
                if not skill_id or not skill_manifest_rel:
                    continue
                
                # Check if skill exists in global directory first
                global_skills_dir = Path.home() / ".olaf" / "skills"
                local_skills_dir = self.core_dir / "skills"
                
                # Build the full manifest path for both locations
                global_manifest_path = global_skills_dir / skill_id / "skill-manifest.json"
                local_manifest_path = local_skills_dir / skill_id / "skill-manifest.json"
                
                # Determine if skill is global or local
                if global_manifest_path.exists():
                    skill_location = "global"
                    skill_manifest_file = global_manifest_path
                    skill_dir = f"skills/{skill_id}"
                elif local_manifest_path.exists():
                    skill_location = "local"
                    skill_manifest_file = local_manifest_path
                    skill_dir = f"skills/{skill_id}"
                else:
                    print(f"  ⚠️  Could not find skill manifest for {skill_id}")
                    continue
                
                try:
                    with open(skill_manifest_file, 'r', encoding='utf-8') as f:
                        skill_manifest = json.load(f)
                except Exception as e:
                    print(f"  ⚠️  Could not read skill manifest for {skill_id}: {e}")
                    continue
                    
                prompts = skill_manifest.get('bom', {}).get('prompts', [])
                if not prompts:
                    print(f"  ⚠️  No prompts in skill manifest for {skill_id}")
                    continue
                    
                first_prompt = prompts[0]
                prompt_path = first_prompt.get('path', '').lstrip('/')  # e.g., prompts/main.md
                
                # Build path based on location
                if skill_location == "global":
                    full_path = f"~/.olaf/{skill_dir}/{prompt_path}"
                else:  # local
                    full_path = f"./{skill_dir}/{prompt_path}"
                    
                competency_map[skill_id] = full_path
        
        competency_names = set(competency_map.keys())
        
        # Sync both .github/prompts and .windsurf/workflows under the project root
        github_prompts_dir = self.project_root / ".github" / "prompts"
        windsurf_workflows_dir = self.project_root / ".windsurf" / "workflows"

        github_prompts_dir.mkdir(parents=True, exist_ok=True)
        windsurf_workflows_dir.mkdir(parents=True, exist_ok=True)
        
        stats = {
            'created': 0,
            'deleted': 0,
            'kept': 0
        }
        
        for target_dir, extension in [(github_prompts_dir, '.prompt.md'), (windsurf_workflows_dir, '.md')]:
            if not target_dir.exists():
                print(f"⚠️  Directory not found: {target_dir}")
                continue
            
            dir_stats = self._sync_directory_commands(target_dir, competency_names, competency_map, extension)
            stats['created'] += dir_stats['created']
            stats['deleted'] += dir_stats['deleted']
            stats['kept'] += dir_stats['kept']
        
        print(f"✅ Command sync complete!")
        print(f"   Created: {stats['created']}")
        print(f"   Deleted: {stats['deleted']}")
        print(f"   Kept: {stats['kept']}")
    
    def _sync_directory_commands(self, target_dir: Path, competency_names: set, competency_map: dict, extension: str) -> Dict[str, int]:
        """Sync commands in a specific directory by deleting all and recreating"""
        stats = {'created': 0, 'deleted': 0, 'kept': 0}
        
        # Delete ALL existing olaf-* files first
        existing_files = list(target_dir.glob(f"olaf-*{extension}"))
        for file in existing_files:
            file.unlink()
            stats['deleted'] += 1
        
        if stats['deleted'] > 0:
            print(f"   🗑️  Deleted {stats['deleted']} existing files")
        
        # Recreate files for all competencies in selection
        for comp_name in competency_names:
            file_path = competency_map.get(comp_name)
            self._create_command_file(target_dir, comp_name, file_path, extension)
            stats['created'] += 1
        
        return stats
    
    def _create_command_file(self, target_dir: Path, competency_name: str, comp_file_path: str, extension: str):
        """Create a command file for a competency"""
        file_path = target_dir / f"olaf-{competency_name}{extension}"
        
        if not comp_file_path:
            print(f"⚠️  Could not find competency file path for: {competency_name}")
            return
        
        # comp_file_path now comes as either:
        # - "~/.olaf/skills/xxx/skill.md" (global)
        # - "./skills/xxx/skill.md" (local)
        # No conversion needed - use as-is
        
        # Determine content based on extension
        if extension == '.prompt.md':
            # GitHub Copilot format
            content = f"\nolaf Execute the `{comp_file_path}` skill.\n"
        else:
            # Windsurf format - with auto_execution_mode for seamless execution
            description = competency_name.replace('-', ' ')
            # Use configurable auto_execution_mode 
            execution_mode = getattr(self, 'execution_mode', 1)
            content = f"---\ndescription: {description}\nauto_execution_mode: {execution_mode}\n---\n\nolaf Execute the `{comp_file_path}` skill.\n"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"   ✨ Created: {file_path.name}")

    def generate_git_exclude(self):
        """Generate .git/info/exclude file to keep OLAF workflows out of git while visible to Windsurf"""
        print("ℹ️  Skipping .git/info/exclude generation (handled by installer)")
        return True

    def run(self, collection_name: str = None, custom: bool = False, list_only: bool = False, output_path: str = None, reinit: bool = False):
        """Main execution - orchestrates the collection selection process"""
        self.show_logo()
        
        collections = self._initialize_collections()
        if output_path:
            self.index_output = Path(output_path)
        
        if list_only:
            self.show_collections(collections)
            return
        
        # Handle reinit mode - regenerate /olaf-* commands from active collection
        if reinit:
            self._handle_reinit(collections)
            return
        
        kernel_competencies = self._prepare_kernel_competencies(collections)
        selected_competencies, selected_id = self._determine_selection(
            collections, kernel_competencies, collection_name, custom
        )
        
        self._generate_and_save_outputs(selected_competencies, selected_id)
        print("\n✨ Done! Your competency index is ready to use.\n")
    
    def _initialize_collections(self) -> Dict:
        """Initialize and clean collections from the local manifest only"""
        collections = self.load_collections()
        print("✓ Collections loaded (local)")
        return self.clean_invalid_competencies(collections)
    
    def _prepare_kernel_competencies(self, collections: Dict) -> List[str]:
        """Extract and validate kernel competencies from core collection"""
        core_collection = next((c for c in collections['collections'] if c['id'] == 'core'), None)
        kernel_competencies = core_collection['competencies'] if core_collection else []
        valid_kernels = self._validate_kernel_competencies(kernel_competencies)
        
        # Update core collection in memory
        if core_collection:
            core_collection['competencies'] = valid_kernels
        
        return valid_kernels
    
    def _determine_selection(self, collections: Dict, kernel_competencies: List[str], 
                           collection_name: str, custom: bool) -> tuple[List[str], str]:
        """Determine which competencies to select based on user input"""
        if collection_name and not custom:
            return self._select_named_collection(collections, kernel_competencies, collection_name)
        elif custom:
            return self._select_custom_collection(collections, kernel_competencies)
        else:
            return self._select_interactive_collection(collections, kernel_competencies)
    
    def _select_named_collection(self, collections: Dict, kernel_competencies: List[str], 
                               collection_name: str) -> tuple[List[str], str]:
        """Select a specific collection by name"""
        coll = next((c for c in collections['collections'] if c['id'] == collection_name), None)
        if not coll:
            self._handle_error(f"Collection not found: {collection_name}")
        
        selected_competencies = self._merge_with_kernels(kernel_competencies, coll['competencies'])
        return selected_competencies, collection_name
    
    def _select_custom_collection(self, collections: Dict, kernel_competencies: List[str]) -> tuple[List[str], str]:
        """Handle custom collection selection"""
        selected_competencies = self.select_competencies_interactive(collections)
        selected_competencies = self._merge_with_kernels(kernel_competencies, selected_competencies)
        selected_id = f"custom-{self._get_timestamp()}"
        
        print(f"\n💡 Tip: Your custom selection is temporary (ID: {selected_id})")
        print("   To create a permanent collection, use: python scripts/olaf-structure-management/create_collection.py")
        
        return selected_competencies, selected_id
    
    def _select_interactive_collection(self, collections: Dict, kernel_competencies: List[str]) -> tuple[List[str], str]:
        """Handle interactive menu selection"""
        selected_id = self.show_menu(collections)
        if selected_id == "custom":
            return self._select_custom_collection(collections, kernel_competencies)
        else:
            coll = next(c for c in collections['collections'] if c['id'] == selected_id)
            selected_competencies = self._merge_with_kernels(kernel_competencies, coll['competencies'])
            return selected_competencies, selected_id
    
    def _generate_and_save_outputs(self, selected_competencies: List[str], selected_id: str):
        """Generate index and save all outputs"""
        index_content = self.generate_index(selected_competencies, selected_id)
        self.save_index(index_content)
        self.save_active_collection(selected_id)
        self.update_condensed_framework(index_content, selected_id)
        self.sync_olaf_commands(selected_competencies)
        self.generate_git_exclude()
    
    def _handle_reinit(self, collections: Dict):
        """Handle reinit mode - regenerate /olaf-* commands from active collection"""
        print("\n🔄 Reinitializing /olaf-* commands from active collection...\n")
        
        # Show execution mode info
        self.show_execution_mode_info()
        print()
        
        # Get active collection from metadata
        active_collection_id = collections.get('metadata', {}).get('active_collection')
        if not active_collection_id:
            self._handle_error("No active collection found. Run the script normally first to select a collection.")
        
        # Find the collection
        collection = next((c for c in collections['collections'] if c['id'] == active_collection_id), None)
        if not collection:
            self._handle_error(f"Active collection '{active_collection_id}' not found in collections.")
        
        print(f"📦 Active Collection: {collection['name']}")
        print(f"   Competencies: {', '.join(collection['competencies'])}\n")
        
        # Regenerate /olaf-* commands
        self.sync_olaf_commands(collection['competencies'])
        
        # Generate git exclude file
        self.generate_git_exclude()
        
        print("\n✨ Reinitialization complete! /olaf-* commands regenerated.\n")


def main():
    # Source of truth is .olaf/tools/select-collection.py
    # Delegate to it so both entry points behave identically.
    here = Path(__file__).resolve()
    olaf_root = here.parents[4]  # .../.olaf
    tools_script = olaf_root / "tools" / "select-collection.py"

    if not tools_script.exists():
        raise SystemExit(f"❌ Missing tools selector: {tools_script}")

    cmd = [sys.executable, str(tools_script), *sys.argv[1:]]
    raise SystemExit(subprocess.call(cmd))


if __name__ == '__main__':
    main()
