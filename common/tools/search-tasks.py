#!/usr/bin/env python3
"""
Task Registry Helper
Easy search and discovery of reusable tasks in OLAF framework
"""

import json
import sys
from pathlib import Path

# Path to registry
REGISTRY_PATH = Path(__file__).parent.parent / "kb" / "task-registry.json"

# Output file for task search results
OUTPUT_FILE = Path(__file__).parent.parent.parent.parent.parent / "work" / "staging" / "temporary" / "task-search-results.json"


def load_registry():
    """Load the task registry"""
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def search_by_category(registry, category):
    """Find all tasks in a category"""
    return [
        task for task in registry['tasks']
        if task['category'] == category
    ]


def search_by_tag(registry, tag):
    """Find all tasks with a specific tag"""
    return [
        task for task in registry['tasks']
        if tag.lower() in [t.lower() for t in task.get('tags', [])]
    ]


def search_by_reusability(registry, min_score=8):
    """Find highly reusable tasks"""
    return [
        task for task in registry['tasks']
        if task.get('reusability_score', 0) >= min_score
    ]


def search_by_keyword(registry, keyword):
    """Search task names and descriptions for keyword"""
    keyword_lower = keyword.lower()
    return [
        task for task in registry['tasks']
        if keyword_lower in task['name'].lower() 
        or keyword_lower in task['description'].lower()
    ]


def print_task_summary(task):
    """Print a formatted task summary"""
    print(f"\n{'='*60}")
    print(f"ID: {task['id']}")
    print(f"Name: {task['name']}")
    print(f"Category: {task['category']}")
    print(f"Reusability: {task.get('reusability_score', 'N/A')}/10")
    print(f"Location: {task['current_location']}")
    print(f"Used in: {', '.join(task['used_in_skills'])}")
    print(f"\nDescription: {task['description']}")
    
    if task['dependencies']['tools']:
        print(f"\nTools Required:")
        for tool in task['dependencies']['tools']:
            print(f"  - {tool['name']}: {tool.get('description', 'N/A')}")
    
    if task['dependencies']['state_variables']:
        print(f"\nInput Variables: {', '.join(task['dependencies']['state_variables'])}")
    
    if task['outputs']['state_variables']:
        print(f"Output Variables: {', '.join(task['outputs']['state_variables'])}")


def save_results_to_file(results, search_type, search_param=None):
    """Save search results to JSON file"""
    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    output_data = {
        "search_type": search_type,
        "search_parameter": search_param,
        "result_count": len(results),
        "tasks": results
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Results saved to: {OUTPUT_FILE}")
    return OUTPUT_FILE


def main():
    """Main CLI interface"""
    if len(sys.argv) < 2:
        print("Task Registry Search Tool")
        print("\nUsage:")
        print("  python search-tasks.py category <category_name>")
        print("  python search-tasks.py tag <tag_name>")
        print("  python search-tasks.py keyword <search_term>")
        print("  python search-tasks.py reusable [min_score]")
        print("  python search-tasks.py list")
        print("\nCategories: environment, github, analysis, cleanup, user-interaction")
        sys.exit(1)
    
    registry = load_registry()
    command = sys.argv[1].lower()
    
    results = []
    
    if command == 'category' and len(sys.argv) > 2:
        results = search_by_category(registry, sys.argv[2])
        print(f"\n🔍 Tasks in category '{sys.argv[2]}':")
    
    elif command == 'tag' and len(sys.argv) > 2:
        results = search_by_tag(registry, sys.argv[2])
        print(f"\n🏷️  Tasks tagged with '{sys.argv[2]}':")
    
    elif command == 'keyword' and len(sys.argv) > 2:
        results = search_by_keyword(registry, sys.argv[2])
        print(f"\n🔎 Tasks matching '{sys.argv[2]}':")
    
    elif command == 'reusable':
        min_score = int(sys.argv[2]) if len(sys.argv) > 2 else 8
        results = search_by_reusability(registry, min_score)
        print(f"\n⭐ Highly reusable tasks (score >= {min_score}):")
    
    elif command == 'list':
        results = registry['tasks']
        print(f"\n📋 All registered tasks ({len(results)}):")
    
    else:
        print("❌ Invalid command. Use --help for usage info.")
        sys.exit(1)
    
    if not results:
        print("  No tasks found.")
    else:
        for task in results:
            print_task_summary(task)
    
    print(f"\n{'='*60}\n")
    print(f"Total: {len(results)} task(s) found")
    
    # Save results to file
    save_results_to_file(results, command, sys.argv[2] if len(sys.argv) > 2 else None)


if __name__ == '__main__':
    main()
