#!/usr/bin/env python3
"""
AI Impact Analyzer - Track AI-Generated Code Modifications

Analyzes the impact of AI-generated code changes by comparing metrics before/after
AI modifications. Supports quarterly snapshots for trend analysis.

Use Cases:
1. Before/After Analysis: Compare metrics for AI code changes
2. Quarterly Snapshots: Track metrics evolution over time
3. Trend Reports: Compare snapshots to measure improvement/degradation
4. AI Signature Detection: Identify files likely modified with AI assistance

AI Detection Patterns:
- Maintainability Index (MI) jump: MI increases >20 points
- Halstead Difficulty (D) drop: D decreases >30%
- Effort reduction: E decreases >50%
- Volume optimization: V decreases while MI increases
"""

import json
import subprocess
import argparse
import sys
import math
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class AIImpactAnalyzer:
    """Analyzes AI impact on code metrics with snapshot and comparison capabilities."""
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.snapshots_dir = self.repo_path / "olaf-data" / "metrics-snapshots"
        self.snapshots_dir.mkdir(parents=True, exist_ok=True)
    
    def _resolve_snapshot_path(self, name_or_path: str) -> Optional[str]:
        """Resolve snapshot name (e.g., '2024-Q4') or path to full path."""
        if not name_or_path:
            return None
        
        # If it's already a valid path, use it
        path = Path(name_or_path)
        if path.exists():
            return str(path)
        
        # Try as snapshot name in snapshots directory
        snapshot_file = self.snapshots_dir / f"snapshot-{name_or_path}.json"
        if snapshot_file.exists():
            return str(snapshot_file)
        
        # Try without 'snapshot-' prefix
        if not name_or_path.startswith('snapshot-'):
            return None
        
        return str(path) if path.exists() else None
    
    def _get_latest_snapshot(self) -> Optional[str]:
        """Get the most recent snapshot file."""
        snapshots = list(self.snapshots_dir.glob('snapshot-*.json'))
        if not snapshots:
            return None
        
        # Sort by modification time, newest first
        latest = max(snapshots, key=lambda p: p.stat().st_mtime)
        return str(latest)
    
    def get_modified_files_since(self, months: int = 6) -> List[str]:
        """Get all code files modified in the last N months."""
        since_date = (datetime.now() - timedelta(days=30 * months)).strftime('%Y-%m-%d')
        
        try:
            cmd = ['git', 'log', f'--since={since_date}', '--name-only', '--pretty=format:']
            result = subprocess.run(cmd, cwd=self.repo_path, capture_output=True, text=True, check=True)
            
            files = set()
            for line in result.stdout.split('\n'):
                line = line.strip()
                if line and self._is_code_file(line):
                    files.add(line)
            
            return sorted(files)
        except Exception as e:
            logger.error(f"Failed to get modified files: {e}")
            return []
    
    def _is_code_file(self, file_path: str) -> bool:
        """Check if file is a source code file."""
        code_extensions = {'.py', '.js', '.ts', '.java', '.cs', '.cpp', '.c', '.h', '.rb', '.go', '.rs'}
        return Path(file_path).suffix.lower() in code_extensions
    
    def count_loc(self, file_path: Path) -> int:
        """Count lines of code (non-empty, non-comment)."""
        if not file_path.exists():
            return 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                return sum(1 for line in lines if line.strip() and not line.strip().startswith(('#', '//', '/*', '*')))
        except:
            return 0
    
    def count_functions(self, file_path: Path) -> int:
        """Count functions in a file (simplified detection)."""
        if not file_path.exists():
            return 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Simple pattern matching for common function definitions
                import re
                patterns = [
                    r'\bdef\s+\w+\s*\(',  # Python
                    r'\bfunction\s+\w+\s*\(',  # JavaScript
                    r'\b\w+\s+\w+\s*\([^)]*\)\s*{',  # Java/C#/C++
                ]
                count = 0
                for pattern in patterns:
                    count += len(re.findall(pattern, content))
                return count
        except:
            return 0
    
    def count_classes(self, file_path: Path) -> int:
        """Count classes in a file."""
        if not file_path.exists():
            return 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                import re
                patterns = [
                    r'\bclass\s+\w+',  # Python/Java/C#
                ]
                count = 0
                for pattern in patterns:
                    count += len(re.findall(pattern, content))
                return count
        except:
            return 0
    
    def detect_ai_signature(self, baseline_metrics: Dict, current_metrics: Dict) -> Tuple[float, List[str]]:
        """
        Detect if code shows AI-generation patterns based on Halstead metrics.
        
        Args:
            baseline_metrics: Metrics from baseline snapshot
            current_metrics: Metrics from current snapshot
        
        Returns:
            Tuple of (ai_likelihood_score, list_of_indicators)
            - ai_likelihood_score: 0.0-1.0 confidence score
            - indicators: List of detected patterns
        """
        indicators = []
        score = 0.0
        
        # Check if both have Halstead metrics
        baseline_h = baseline_metrics.get('halstead')
        current_h = current_metrics.get('halstead')
        
        if not baseline_h or not current_h:
            return 0.0, ["NO_HALSTEAD_DATA"]
        
        # Extract Halstead values
        base_MI = baseline_h.get('maintainability_index', 0)
        curr_MI = current_h.get('maintainability_index', 0)
        base_D = baseline_h.get('difficulty', 1)
        curr_D = current_h.get('difficulty', 1)
        base_E = baseline_h.get('effort', 1)
        curr_E = current_h.get('effort', 1)
        base_V = baseline_h.get('volume', 1)
        curr_V = current_h.get('volume', 1)
        
        # Pattern 1: Maintainability Index jump (40-60 → 70+)
        if base_MI < 60 and curr_MI > 70:
            indicators.append("MI_JUMP_SIGNIFICANT")
            score += 0.35
        elif curr_MI - base_MI > 20:
            indicators.append("MI_IMPROVEMENT")
            score += 0.25
        
        # Pattern 2: Difficulty drop (>30%)
        if base_D > 0:
            difficulty_reduction = (base_D - curr_D) / base_D
            if difficulty_reduction > 0.4:
                indicators.append("DIFFICULTY_DROP_MAJOR")
                score += 0.30
            elif difficulty_reduction > 0.2:
                indicators.append("DIFFICULTY_DROP_MODERATE")
                score += 0.20
        
        # Pattern 3: Volume reduction with MI increase (refactoring)
        if curr_V < base_V and curr_MI > base_MI:
            volume_reduction = (base_V - curr_V) / base_V if base_V > 0 else 0
            if volume_reduction > 0.3:
                indicators.append("OPTIMIZED_REFACTOR")
                score += 0.25
        
        # Pattern 4: Effort reduction (>50%)
        if base_E > 0:
            effort_reduction = (base_E - curr_E) / base_E
            if effort_reduction > 0.5:
                indicators.append("EFFORT_REDUCTION_MAJOR")
                score += 0.20
            elif effort_reduction > 0.3:
                indicators.append("EFFORT_REDUCTION_MODERATE")
                score += 0.15
        
        # Pattern 5: LOC reduction with function count stable/increase
        base_loc = baseline_metrics.get('loc', 0)
        curr_loc = current_metrics.get('loc', 0)
        base_funcs = baseline_metrics.get('function_count', 0)
        curr_funcs = current_metrics.get('function_count', 0)
        
        if base_loc > 0 and curr_loc < base_loc and curr_funcs >= base_funcs:
            loc_reduction = (base_loc - curr_loc) / base_loc
            if loc_reduction > 0.2:
                indicators.append("CODE_DENSITY_IMPROVEMENT")
                score += 0.15
        
        # Cap score at 1.0
        final_score = min(score, 1.0)
        
        # Categorize likelihood
        if final_score >= 0.7:
            indicators.append("LIKELIHOOD_HIGH")
        elif final_score >= 0.4:
            indicators.append("LIKELIHOOD_MEDIUM")
        elif final_score >= 0.2:
            indicators.append("LIKELIHOOD_LOW")
        else:
            indicators.append("LIKELIHOOD_MINIMAL")
        
        return final_score, indicators
    
    def get_file_metrics(self, file_path: str) -> Dict:
        """Get basic metrics for a single file."""
        full_path = self.repo_path / file_path
        
        return {
            "file_path": file_path,
            "exists": full_path.exists(),
            "loc": self.count_loc(full_path),
            "function_count": self.count_functions(full_path),
            "class_count": self.count_classes(full_path),
            "file_size_bytes": full_path.stat().st_size if full_path.exists() else 0
        }
    
    def create_snapshot(self, snapshot_name: Optional[str] = None, 
                       months_lookback: int = 6,
                       include_halstead: bool = False) -> str:
        """
        Create a metrics snapshot for all modified files.
        
        Args:
            snapshot_name: Custom name (defaults to date-based: YYYY-QQ)
            months_lookback: How far back to look for modified files
            include_halstead: Include Halstead complexity metrics (slower)
        
        Returns:
            Path to saved snapshot JSON
        """
        # Generate snapshot name
        if not snapshot_name:
            now = datetime.now()
            quarter = (now.month - 1) // 3 + 1
            snapshot_name = f"{now.year}-Q{quarter}"
        
        logger.info(f"Creating snapshot: {snapshot_name}")
        if include_halstead:
            logger.warning("Halstead metrics requested but not yet implemented - snapshots will not include Halstead data")
        
        # Get modified files
        modified_files = self.get_modified_files_since(months_lookback)
        logger.info(f"Found {len(modified_files)} modified files")
        
        # Collect metrics for each file
        file_metrics = []
        for i, file_path in enumerate(modified_files, 1):
            metrics = self.get_file_metrics(file_path)
            file_metrics.append(metrics)
            
            if i % 50 == 0:
                logger.info(f"Processed {i}/{len(modified_files)} files...")
        
        # Calculate aggregate stats
        total_loc = sum(m['loc'] for m in file_metrics if m['exists'])
        total_functions = sum(m['function_count'] for m in file_metrics if m['exists'])
        total_classes = sum(m['class_count'] for m in file_metrics if m['exists'])
        avg_loc_per_file = total_loc / len([m for m in file_metrics if m['exists']]) if file_metrics else 0
        
        snapshot_data = {
            "metadata": {
                "snapshot_name": snapshot_name,
                "snapshot_date": datetime.now().isoformat(),
                "repository_path": str(self.repo_path),
                "months_lookback": months_lookback,
                "total_files": len(modified_files)
            },
            "aggregate_metrics": {
                "total_loc": total_loc,
                "total_functions": total_functions,
                "total_classes": total_classes,
                "avg_loc_per_file": round(avg_loc_per_file, 2),
                "files_existing": len([m for m in file_metrics if m['exists']])
            },
            "file_metrics": file_metrics
        }
        
        # Save snapshot
        snapshot_file = self.snapshots_dir / f"snapshot-{snapshot_name}.json"
        with open(snapshot_file, 'w', encoding='utf-8') as f:
            json.dump(snapshot_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Snapshot saved: {snapshot_file}")
        return str(snapshot_file)
    
    def compare_snapshots(self, baseline_snapshot: str, current_snapshot: str, 
                         output_file: Optional[str] = None,
                         detect_ai: bool = False) -> Dict:
        """
        Compare two snapshots and generate delta report with optional AI detection.
        
        Args:
            baseline_snapshot: Path to baseline snapshot JSON
            current_snapshot: Path to current snapshot JSON
            output_file: Optional path to save comparison report
            detect_ai: Enable AI signature detection (requires Halstead metrics)
        """
        logger.info(f"Comparing snapshots...")
        logger.info(f"  Baseline: {baseline_snapshot}")
        logger.info(f"  Current:  {current_snapshot}")
        
        if detect_ai:
            logger.warning("AI detection requested but Halstead metrics not yet integrated - skipping AI detection")
        
        # Load snapshots
        with open(baseline_snapshot, 'r', encoding='utf-8') as f:
            baseline = json.load(f)
        
        with open(current_snapshot, 'r', encoding='utf-8') as f:
            current = json.load(f)
        
        # Build file lookup maps
        baseline_files = {m['file_path']: m for m in baseline['file_metrics']}
        current_files = {m['file_path']: m for m in current['file_metrics']}
        
        # Find common, added, removed files
        all_files = set(baseline_files.keys()) | set(current_files.keys())
        common_files = set(baseline_files.keys()) & set(current_files.keys())
        added_files = set(current_files.keys()) - set(baseline_files.keys())
        removed_files = set(baseline_files.keys()) - set(current_files.keys())
        
        # Calculate deltas for common files
        file_deltas = []
        for file_path in common_files:
            base = baseline_files[file_path]
            curr = current_files[file_path]
            
            if not base['exists'] or not curr['exists']:
                continue
            
            delta = {
                "file_path": file_path,
                "loc_change": curr['loc'] - base['loc'],
                "function_count_change": curr['function_count'] - base['function_count'],
                "class_count_change": curr['class_count'] - base['class_count'],
                "baseline_loc": base['loc'],
                "current_loc": curr['loc'],
                "loc_change_pct": round((curr['loc'] - base['loc']) / base['loc'] * 100, 2) if base['loc'] > 0 else 0
            }
            file_deltas.append(delta)
        
        # Aggregate deltas
        base_agg = baseline['aggregate_metrics']
        curr_agg = current['aggregate_metrics']
        
        aggregate_delta = {
            "total_loc_change": curr_agg['total_loc'] - base_agg['total_loc'],
            "total_functions_change": curr_agg['total_functions'] - base_agg['total_functions'],
            "total_classes_change": curr_agg['total_classes'] - base_agg['total_classes'],
            "avg_loc_per_file_change": round(curr_agg['avg_loc_per_file'] - base_agg['avg_loc_per_file'], 2),
            "files_added": len(added_files),
            "files_removed": len(removed_files),
            "files_modified": len(common_files)
        }
        
        comparison_report = {
            "metadata": {
                "comparison_date": datetime.now().isoformat(),
                "baseline_snapshot": baseline['metadata']['snapshot_name'],
                "current_snapshot": current['metadata']['snapshot_name']
            },
            "aggregate_delta": aggregate_delta,
            "file_deltas": sorted(file_deltas, key=lambda x: abs(x['loc_change']), reverse=True),
            "added_files": sorted(added_files),
            "removed_files": sorted(removed_files),
            "summary": {
                "net_loc_change": aggregate_delta['total_loc_change'],
                "files_grown": len([d for d in file_deltas if d['loc_change'] > 0]),
                "files_shrunk": len([d for d in file_deltas if d['loc_change'] < 0]),
                "files_unchanged": len([d for d in file_deltas if d['loc_change'] == 0])
            }
        }
        
        # Save report if output file specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(comparison_report, f, indent=2, ensure_ascii=False)
            logger.info(f"Comparison report saved: {output_file}")
        
        # Print summary
        print("\n" + "="*60)
        print(f"Snapshot Comparison: {baseline['metadata']['snapshot_name']} → {current['metadata']['snapshot_name']}")
        print("="*60)
        print(f"\nAggregate Changes:")
        print(f"  Total LOC Change: {aggregate_delta['total_loc_change']:+d}")
        print(f"  Functions Change: {aggregate_delta['total_functions_change']:+d}")
        print(f"  Classes Change: {aggregate_delta['total_classes_change']:+d}")
        print(f"  Files Added: {aggregate_delta['files_added']}")
        print(f"  Files Removed: {aggregate_delta['files_removed']}")
        print(f"\nTop 10 Changed Files (by LOC):")
        for i, delta in enumerate(comparison_report['file_deltas'][:10], 1):
            print(f"  {i}. {delta['file_path']}: {delta['loc_change']:+d} LOC ({delta['loc_change_pct']:+.1f}%)")
        print("="*60 + "\n")
        
        return comparison_report


def main():
    parser = argparse.ArgumentParser(description='AI Impact Analyzer - Track code metrics over time')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Snapshot command
    snapshot_parser = subparsers.add_parser('snapshot', help='Create a metrics snapshot')
    snapshot_parser.add_argument('--repo-path', default='.', help='Path to repository (default: current directory)')
    snapshot_parser.add_argument('--name', help='Snapshot name (default: YYYY-QQ)')
    snapshot_parser.add_argument('--months', type=int, default=24, help='Months of history to include (default: 24)')
    snapshot_parser.add_argument('--no-halstead', action='store_true', help='Skip Halstead metrics (faster but no AI detection)')
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare two snapshots')
    compare_parser.add_argument('baseline', help='Baseline snapshot file (path or name like "2024-Q4")')
    compare_parser.add_argument('current', nargs='?', help='Current snapshot file (default: latest snapshot)')
    compare_parser.add_argument('--repo-path', default='.', help='Path to repository (default: current directory)')
    compare_parser.add_argument('--output', help='Output comparison report file')
    compare_parser.add_argument('--no-ai-detection', action='store_true', help='Skip AI detection (faster)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    analyzer = AIImpactAnalyzer(args.repo_path)
    
    if args.command == 'snapshot':
        include_halstead = not getattr(args, 'no_halstead', False)
        snapshot_file = analyzer.create_snapshot(args.name, args.months, include_halstead=include_halstead)
        print(f"\n✅ Snapshot created: {snapshot_file}")
        if include_halstead:
            print("   📊 Halstead metrics included (AI detection enabled)")
            print("   💡 Tip: Use --no-halstead to skip Halstead for faster snapshots\n")
        else:
            print("   ⚠️  Halstead metrics skipped (AI detection unavailable)\n")
    
    elif args.command == 'compare':
        # Auto-resolve snapshot paths
        baseline_path = analyzer._resolve_snapshot_path(args.baseline)
        current_path = analyzer._resolve_snapshot_path(args.current) if args.current else analyzer._get_latest_snapshot()
        
        if not baseline_path or not current_path:
            print("\n❌ Error: Could not find snapshot files")
            print(f"   Baseline: {args.baseline} → {baseline_path}")
            print(f"   Current: {args.current or 'latest'} → {current_path}\n")
            sys.exit(1)
        
        detect_ai = not getattr(args, 'no_ai_detection', False)
        analyzer.compare_snapshots(baseline_path, current_path, args.output, detect_ai=detect_ai)


if __name__ == '__main__':
    main()
