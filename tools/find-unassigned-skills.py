#!/usr/bin/env python3
"""
Find skills that are not assigned to any competency.

This script:
1. Lists all skill directories in skills/
2. Reads all competency JSON files
3. Identifies skills not referenced in any competency
4. Outputs the list of unassigned skills
"""

import json
import os
from pathlib import Path


def get_all_skills(skills_dir="skills"):
    """Get all skill directory names."""
    # Get the parent directory (project root) from tools/
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    skills_path = project_root / skills_dir
    if not skills_path.exists():
        print(f"Error: {skills_dir} directory not found")
        return []
    
    skills = []
    for item in skills_path.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            # Check if it has a skill.md file
            if (item / "skill.md").exists():
                skills.append(item.name)
    
    return sorted(skills)


def get_competency_skills(competencies_dir="competencies"):
    """Get all skills referenced in competency files."""
    # Get the parent directory (project root) from tools/
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    competencies_path = project_root / competencies_dir
    if not competencies_path.exists():
        print(f"Error: {competencies_dir} directory not found")
        return set(), {}
    
    all_assigned_skills = set()
    competency_map = {}  # skill -> list of competencies
    
    for comp_file in competencies_path.glob("*.json"):
        try:
            with open(comp_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                comp_name = data.get('name', comp_file.stem)
                skills = data.get('skills', [])
                
                for skill in skills:
                    all_assigned_skills.add(skill)
                    if skill not in competency_map:
                        competency_map[skill] = []
                    competency_map[skill].append(comp_name)
        except Exception as e:
            print(f"Warning: Could not read {comp_file}: {e}")
    
    return all_assigned_skills, competency_map


def main():
    print("Finding unassigned skills...\n")
    
    # Get all skills
    all_skills = get_all_skills()
    print(f"Total skills found: {len(all_skills)}")
    
    # Get skills assigned to competencies
    assigned_skills, competency_map = get_competency_skills()
    print(f"Skills assigned to competencies: {len(assigned_skills)}")
    
    # Find unassigned skills
    unassigned = sorted(set(all_skills) - assigned_skills)
    
    print(f"\n{'='*60}")
    print(f"UNASSIGNED SKILLS: {len(unassigned)}")
    print(f"{'='*60}\n")
    
    if unassigned:
        for skill in unassigned:
            print(f"  - {skill}")
    else:
        print("  All skills are assigned to at least one competency!")
    
    # Also check for skills in competencies that don't exist
    print(f"\n{'='*60}")
    print("VALIDATION: Skills in competencies that don't exist")
    print(f"{'='*60}\n")
    
    missing_skills = sorted(assigned_skills - set(all_skills))
    if missing_skills:
        for skill in missing_skills:
            comps = competency_map.get(skill, [])
            print(f"  - {skill} (in: {', '.join(comps)})")
    else:
        print("  All competency references are valid!")
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total skills: {len(all_skills)}")
    print(f"Assigned skills: {len(assigned_skills)}")
    print(f"Unassigned skills: {len(unassigned)}")
    print(f"Invalid references: {len(missing_skills)}")


if __name__ == "__main__":
    main()
