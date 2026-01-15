#!/usr/bin/env python3
"""
OLAF Competency Manager
Handles create, edit, delete, and validate operations for OLAF competencies.
Competencies are collections/packs of skills (not file containers).
"""

import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

class CompetencyManager:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.skills_dir = self.script_dir.parent.parent
        self.core_dir = self.skills_dir.parent
        self.competencies_dir = self.core_dir / "competencies"
        
    def run(self, operation: str, competency_name: Optional[str] = None, pack: Optional[str] = None):
        """Main entry point"""
        print(f"\n{'='*60}")
        print(f"  OLAF Competency Manager - {operation.upper()}")
        print(f"{'='*60}\n")
        
        if operation == "create":
            self.create_competency(competency_name, pack)
        elif operation == "edit":
            self.edit_competency(competency_name)
        elif operation == "delete":
            self.delete_competency(competency_name)
        elif operation == "validate":
            self.validate_competency(competency_name)
        else:
            print(f"❌ Unknown operation: {operation}")
            sys.exit(1)
    
    def create_competency(self, name: Optional[str], pack: Optional[str]):
        """Create a new competency (skill collection)"""
        if not name:
            name = input("Competency name (kebab-case): ").strip()
        
        if not self._validate_name(name):
            print("❌ Invalid name. Use kebab-case (e.g., 'data-analysis')")
            sys.exit(1)
        
        comp_dir = self.competencies_dir / name
        
        if comp_dir.exists():
            print(f"❌ Competency already exists: {comp_dir}")
            print("   Use 'edit' operation to modify it.")
            sys.exit(1)
        
        description = input("Brief description: ").strip()
        
        print("\n📋 List skills to include (comma-separated, e.g., 'review-code,analyze-complexity')")
        print("   Leave empty to create empty competency and add skills later:")
        skills_input = input("Skills: ").strip()
        skill_ids = [s.strip() for s in skills_input.split(',') if s.strip()] if skills_input else []
        
        print(f"\n📁 PROPOSED COMPETENCY:")
        print(f"   Name: {name}")
        print(f"   Type: Skill Collection")
        print(f"   Skills: {len(skill_ids)} skill(s)")
        if skill_ids:
            for skill in skill_ids:
                print(f"      - {skill}")
        print(f"   Location: {comp_dir}/competency-manifest.json")
        
        confirm = input("\nProceed? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("❌ Cancelled")
            sys.exit(0)
        
        print("\n📝 Creating competency...")
        comp_dir.mkdir(parents=True, exist_ok=True)
        
        manifest = {
            "metadata": {
                "id": name,
                "name": name.replace('-', ' ').title() + " Competency Package",
                "shortDescription": description,
                "description": description,
                "version": "1.0.0",
                "objectives": [f"Provide {name} capabilities"],
                "tags": [name],
                "author": "OLAF Framework",
                "status": "experimental",
                "exposure": "export",
                "created": datetime.now().isoformat()[:10],
                "updated": datetime.now().isoformat()[:10],
                "maintenance": {
                    "team": name,
                    "primary_maintainer": "OLAF Framework",
                    "created_by": "manage-competencies skill"
                },
                "technical_requirements": {
                    "recommended_llm": "GPT-4 or equivalent",
                    "tool_dependency": "None",
                    "platform_limitations": "Cross-platform compatible"
                }
            },
            "bom": {
                "competencies": skill_ids,
                "entry_points": [
                    {"id": sid, "manifest": f"skills/{sid}/skill-manifest.json"}
                    for sid in skill_ids
                ]
            }
        }
        
        manifest_file = comp_dir / "competency-manifest.json"
        manifest_file.write_text(json.dumps(manifest, indent=2))
        
        print(f"\n✅ COMPETENCY CREATED: {name}")
        print(f"   Location: {comp_dir}")
        print(f"   Manifest: {manifest_file}")
        print(f"   Skills: {len(skill_ids)}")
        print(f"\nNext steps:")
        print(f"   1. Validate: python {__file__} --operation validate --name {name}")
        print(f"   2. Add more skills: python {__file__} --operation edit --name {name}")
    
    def edit_competency(self, name: Optional[str]):
        """Edit an existing competency (add/remove skills)"""
        while True:
            # Competency selection
            if not name:
                available = self._list_competencies()
                print(f"\nAvailable competencies:")
                for i, comp in enumerate(available, 1):
                    print(f"   {i}. {comp}")
                print(f"   0. Exit")
                
                choice = input("\nSelect competency (number or name, 0 to exit): ").strip()
                
                if choice == "0":
                    print("\n✅ Done")
                    return
                
                if choice.isdigit():
                    idx = int(choice)
                    if idx < 1 or idx > len(available):
                        print("❌ Invalid choice")
                        continue
                    name = available[idx - 1]
                else:
                    name = choice
            
            comp_path = self._find_competency(name)
            if not comp_path:
                print(f"❌ Competency not found: {name}")
                name = None
                continue
            
            manifest_file = comp_path / "competency-manifest.json"
            if not manifest_file.exists():
                print(f"❌ Manifest not found: {manifest_file}")
                name = None
                continue
            
            # Load manifest
            manifest = json.loads(manifest_file.read_text())
            bom = manifest.get("bom", {})
            
            # Get skills from competencies array OR extract from entry_points
            current_skills = bom.get("competencies", [])
            if not current_skills and "entry_points" in bom:
                # Extract skill IDs from entry_points if competencies is empty
                current_skills = [ep["id"] for ep in bom["entry_points"] if "id" in ep]
            
            # Display current state
            print(f"\n📝 EDITING: {name}")
            print(f"   Location: {comp_path}")
            print(f"\n📋 Current skills ({len(current_skills)}):")
            if current_skills:
                for skill in current_skills:
                    print(f"      - {skill}")
            else:
                print(f"      (empty)")
            
            # Action menu
            print(f"\nWhat would you like to do?")
            print(f"   1. Add skills")
            print(f"   2. Remove skills")
            print(f"   3. List all available skills")
            print(f"   4. Select different competency")
            print(f"   0. Exit")
            
            choice = input("\nChoice (0-4): ").strip()
            
            if choice == "0":
                print("\n✅ Done")
                return
            
            if choice == "4":
                name = None
                continue
            
            if choice == "1":
                # Add skills
                available_skills = self._list_available_skills()
                print(f"\n📚 Available skills ({len(available_skills)}):")
                for i, skill in enumerate(available_skills, 1):
                    marker = "✓" if skill in current_skills else " "
                    print(f"   {i:2d}. [{marker}] {skill}")
                
                print("\nEnter skill IDs or numbers (comma-separated, e.g., '1,3,5' or 'review-code,analyze-complexity'):")
                print("Type 'back' to return to menu")
                new_skills = input("Skills: ").strip()
                
                if not new_skills or new_skills.lower() == 'back':
                    continue
                
                # Parse input - could be numbers or skill IDs
                skill_ids = []
                for item in new_skills.split(','):
                    item = item.strip()
                    if item.isdigit():
                        idx = int(item)
                        if 1 <= idx <= len(available_skills):
                            skill_ids.append(available_skills[idx - 1])
                        else:
                            print(f"⚠️  Skipping invalid number: {item}")
                    else:
                        skill_ids.append(item)
                
                added = []
                for skill_id in skill_ids:
                    if skill_id not in current_skills:
                        current_skills.append(skill_id)
                        added.append(skill_id)
                
                if added:
                    # Update both competencies array and entry_points
                    manifest["bom"]["competencies"] = current_skills
                    manifest["bom"]["entry_points"] = [
                        {"id": sid, "manifest": f"skills/{sid}/skill-manifest.json"}
                        for sid in current_skills
                    ]
                    manifest["metadata"]["updated"] = datetime.now().isoformat()[:10]
                    
                    manifest_file.write_text(json.dumps(manifest, indent=2))
                    print(f"\n✅ Added {len(added)} skill(s):")
                    for s in added:
                        print(f"   + {s}")
                else:
                    print("\n⚠️  No new skills added (all already present)")
            
            elif choice == "2":
                # Remove skills
                if not current_skills:
                    print("\n⚠️  No skills to remove")
                    continue
                
                print(f"\n📋 Current skills in this competency:")
                for i, skill in enumerate(current_skills, 1):
                    print(f"   {i}. {skill}")
                
                print("\nEnter skill IDs or numbers to remove (comma-separated, e.g., '1,3' or 'review-code'):")
                print("Type 'back' to return to menu")
                remove_skills = input("Skills: ").strip()
                
                if not remove_skills or remove_skills.lower() == 'back':
                    continue
                
                # Parse input - could be numbers or skill IDs
                skill_ids = []
                for item in remove_skills.split(','):
                    item = item.strip()
                    if item.isdigit():
                        idx = int(item)
                        if 1 <= idx <= len(current_skills):
                            skill_ids.append(current_skills[idx - 1])
                        else:
                            print(f"⚠️  Skipping invalid number: {item}")
                    else:
                        skill_ids.append(item)
                
                removed = []
                for skill_id in skill_ids:
                    if skill_id in current_skills:
                        current_skills.remove(skill_id)
                        removed.append(skill_id)
                
                if removed:
                    # Update both competencies array and entry_points
                    manifest["bom"]["competencies"] = current_skills
                    manifest["bom"]["entry_points"] = [
                        {"id": sid, "manifest": f"skills/{sid}/skill-manifest.json"}
                        for sid in current_skills
                    ]
                    manifest["metadata"]["updated"] = datetime.now().isoformat()[:10]
                    
                    manifest_file.write_text(json.dumps(manifest, indent=2))
                    print(f"\n✅ Removed {len(removed)} skill(s):")
                    for s in removed:
                        print(f"   - {s}")
                else:
                    print("\n⚠️  No skills removed")
            
            elif choice == "3":
                # List available skills
                print("\n📚 Available skills:")
                available_skills = self._list_available_skills()
                for skill in sorted(available_skills):
                    marker = "✓" if skill in current_skills else " "
                    print(f"   [{marker}] {skill}")
                input("\nPress Enter to continue...")
            
            else:
                print("\n⚠️  Invalid choice")
    
    def delete_competency(self, name: Optional[str]):
        """Delete a competency"""
        if not name:
            name = input("Competency name to delete: ").strip()
        
        comp_path = self._find_competency(name)
        if not comp_path:
            print(f"❌ Competency not found: {name}")
            sys.exit(1)
        
        print(f"\n🔍 Checking dependencies...")
        dependents = self._find_dependents(name)
        if dependents:
            print(f"\n⚠️  WARNING: This competency is used by:")
            for dep in dependents:
                print(f"   - {dep}")
            print(f"\nDeleting it may break these competencies!")
        
        print(f"\n🗑️  DELETION PLAN:")
        print(f"   Will delete: {comp_path}")
        
        confirm = input(f"\nType competency name '{name}' to confirm: ").strip()
        if confirm != name:
            print("❌ Cancelled")
            sys.exit(0)
        
        import shutil
        shutil.rmtree(comp_path)
        
        print(f"\n✅ DELETED: {name}")
    
    def validate_competency(self, name: Optional[str]):
        """Validate competency manifest and skill references"""
        if not name:
            name = input("Competency name to validate: ").strip()
        
        comp_path = self._find_competency(name)
        if not comp_path:
            print(f"❌ Competency not found: {name}")
            sys.exit(1)
        
        print(f"\n🔍 VALIDATING: {name}")
        print(f"   Location: {comp_path}\n")
        
        errors = []
        warnings = []
        repairs = []
        
        manifest_file = comp_path / "competency-manifest.json"
        if not manifest_file.exists():
            errors.append("Missing competency-manifest.json")
            print("❌ VALIDATION FAILED:")
            for err in errors:
                print(f"   • {err}")
            sys.exit(1)
        
        try:
            manifest = json.loads(manifest_file.read_text())
            modified = False
            
            if "metadata" not in manifest:
                errors.append("Missing 'metadata' section")
            else:
                meta = manifest["metadata"]
                required_meta = ["id", "name", "description", "version", "status"]
                for field in required_meta:
                    if field not in meta:
                        errors.append(f"Metadata missing field: {field}")
            
            if "bom" not in manifest:
                errors.append("Missing 'bom' section")
            else:
                bom = manifest["bom"]
                
                # Check for sync issues between competencies and entry_points
                competencies_list = bom.get("competencies", [])
                entry_points_list = bom.get("entry_points", [])
                entry_point_ids = [ep["id"] for ep in entry_points_list if "id" in ep]
                
                # REPAIR: Detect and fix mismatched arrays
                if not competencies_list and entry_point_ids:
                    # competencies is empty but entry_points has skills
                    warnings.append(f"Found {len(entry_point_ids)} skills in entry_points but competencies array is empty")
                    repairs.append(f"Rebuilding competencies array from entry_points ({len(entry_point_ids)} skills)")
                    manifest["bom"]["competencies"] = entry_point_ids
                    modified = True
                
                elif competencies_list and not entry_points_list:
                    # entry_points is empty but competencies has skills
                    warnings.append(f"Found {len(competencies_list)} skills in competencies but entry_points array is empty")
                    repairs.append(f"Rebuilding entry_points from competencies ({len(competencies_list)} skills)")
                    manifest["bom"]["entry_points"] = [
                        {"id": sid, "manifest": f"skills/{sid}/skill-manifest.json"}
                        for sid in competencies_list
                    ]
                    modified = True
                
                elif set(competencies_list) != set(entry_point_ids):
                    # Arrays exist but don't match
                    comp_only = set(competencies_list) - set(entry_point_ids)
                    ep_only = set(entry_point_ids) - set(competencies_list)
                    
                    if comp_only:
                        warnings.append(f"Skills in competencies but not entry_points: {', '.join(comp_only)}")
                    if ep_only:
                        warnings.append(f"Skills in entry_points but not competencies: {', '.join(ep_only)}")
                    
                    # Merge both lists (union)
                    merged_skills = sorted(set(competencies_list) | set(entry_point_ids))
                    repairs.append(f"Synchronizing arrays: merging to {len(merged_skills)} unique skills")
                    manifest["bom"]["competencies"] = merged_skills
                    manifest["bom"]["entry_points"] = [
                        {"id": sid, "manifest": f"skills/{sid}/skill-manifest.json"}
                        for sid in merged_skills
                    ]
                    modified = True
                
                # Get final skill list for validation
                skill_ids = manifest["bom"].get("competencies", [])
                
                if not skill_ids:
                    warnings.append("No skills defined in this competency")
                else:
                    print(f"📋 Validating {len(skill_ids)} skill references...")
                    
                    # Check which skills actually exist
                    valid_skills = []
                    invalid_skills = []
                    
                    for skill_id in skill_ids:
                        skill_path = self.skills_dir / skill_id
                        if not skill_path.exists():
                            invalid_skills.append(skill_id)
                            errors.append(f"Referenced skill not found: {skill_id}")
                        else:
                            valid_skills.append(skill_id)
                            print(f"   ✓ {skill_id}")
                    
                    # AUTO-REPAIR: Remove non-existent skills
                    if invalid_skills:
                        print(f"\n❌ Found {len(invalid_skills)} non-existent skill(s):")
                        for skill_id in invalid_skills:
                            print(f"   ✗ {skill_id}")
                        
                        confirm = input(f"\nAuto-remove these {len(invalid_skills)} invalid skills? (yes/no): ").strip().lower()
                        if confirm == "yes":
                            repairs.append(f"Removed {len(invalid_skills)} non-existent skills: {', '.join(invalid_skills)}")
                            manifest["bom"]["competencies"] = valid_skills
                            manifest["bom"]["entry_points"] = [
                                {"id": sid, "manifest": f"skills/{sid}/skill-manifest.json"}
                                for sid in valid_skills
                            ]
                            modified = True
                            # Clear errors for removed skills
                            errors = [e for e in errors if not any(skill in e for skill in invalid_skills)]
            
            # Save repairs if any were made
            if modified:
                manifest["metadata"]["updated"] = datetime.now().isoformat()[:10]
                manifest_file.write_text(json.dumps(manifest, indent=2))
                
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON in manifest: {e}")
        
        print()
        
        if repairs:
            print("🔧 AUTO-REPAIRS APPLIED:")
            for repair in repairs:
                print(f"   ✓ {repair}")
            print()
        
        if errors:
            print("❌ VALIDATION FAILED:")
            for err in errors:
                print(f"   • {err}")
        else:
            print("✅ VALIDATION PASSED")
        
        if warnings:
            print("\n⚠️  WARNINGS:")
            for warn in warnings:
                print(f"   • {warn}")
    
    # Helper methods
    def _validate_name(self, name: str) -> bool:
        """Validate kebab-case name"""
        return name.replace('-', '').replace('_', '').isalnum() and '-' in name
    
    def _list_available_skills(self) -> List[str]:
        """List all available skills"""
        if not self.skills_dir.exists():
            return []
        skills = []
        for skill_dir in self.skills_dir.iterdir():
            if skill_dir.is_dir() and (skill_dir / "skill-manifest.json").exists():
                skills.append(skill_dir.name)
        return sorted(skills)
    
    def _list_competencies(self) -> List[str]:
        """List all competencies"""
        if not self.competencies_dir.exists():
            return []
        competencies = []
        for comp_dir in self.competencies_dir.iterdir():
            if comp_dir.is_dir():
                competencies.append(comp_dir.name)
        return sorted(competencies)
    
    def _find_competency(self, name: str) -> Optional[Path]:
        """Find competency path by name"""
        comp_path = self.competencies_dir / name
        if comp_path.exists() and comp_path.is_dir():
            return comp_path
        return None
    
    def _find_dependents(self, name: str) -> List[str]:
        """Find competencies that depend on this one"""
        dependents = []
        for comp_dir in self.competencies_dir.iterdir():
            if comp_dir.is_dir() and comp_dir.name != name:
                deps_file = comp_dir / "dependencies.json"
                if deps_file.exists():
                    try:
                        deps = json.loads(deps_file.read_text())
                        if name in str(deps):
                            dependents.append(comp_dir.name)
                    except:
                        pass
        return dependents

def main():
    parser = argparse.ArgumentParser(description="OLAF Competency Manager")
    parser.add_argument("--operation", choices=["create", "edit", "delete", "validate"],
                       required=True, help="Operation to perform")
    parser.add_argument("--name", help="Competency name")
    parser.add_argument("--pack", help="Pack name (for create)")
    
    args = parser.parse_args()
    
    manager = CompetencyManager()
    manager.run(args.operation, args.name, args.pack)

if __name__ == "__main__":
    main()
