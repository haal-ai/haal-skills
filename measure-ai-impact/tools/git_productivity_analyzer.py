#!/usr/bin/env python3
"""
Git Productivity Analyzer - Quarterly Snapshots from Git History

Analyzes developer productivity and AI impact using pure Git data:
- Commit frequency (commits/day, commits/week)
- Commit size (LOC churn per commit)
- Code churn metrics (additions, deletions, net change)
- Contributor analysis (churn per contributor)
- Time-based patterns (active days, session duration)

Works with any Git repository - no GitHub/GitLab API needed.

Usage:
    # Generate all quarterly snapshots since 2024-Q1
    python git_productivity_analyzer.py snapshots --since 2024-01-01
    
    # Generate single quarter snapshot
    python git_productivity_analyzer.py snapshot --quarter 2024-Q4
    
    # Compare two quarters
    python git_productivity_analyzer.py compare 2024-Q1 2024-Q4
    
    # Generate full report with trends
    python git_productivity_analyzer.py report
"""

import json
import subprocess
import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import re

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Try to import radon for Halstead metrics (Python only)
try:
    from radon.complexity import cc_visit
    from radon.metrics import mi_visit, h_visit
    RADON_AVAILABLE = True
except ImportError:
    RADON_AVAILABLE = False
    logger.warning("radon library not available. Install with: pip install radon")
    logger.warning("Halstead/MI metrics will be unavailable for Python files.")

# Language file extensions mapping
LANGUAGE_EXTENSIONS = {
    'python': ['.py'],
    'java': ['.java'],
    'c': ['.c', '.h'],
    'cpp': ['.cpp', '.cc', '.cxx', '.hpp', '.hxx', '.h'],
    'csharp': ['.cs'],
    'javascript': ['.js', '.jsx'],
    'typescript': ['.ts', '.tsx'],
    'go': ['.go']
}


class GitProductivityAnalyzer:
    """Analyzes Git repository productivity metrics from commit history."""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        self.snapshots_dir = self.repo_path / "olaf-data" / "git-snapshots"
        self.snapshots_dir.mkdir(parents=True, exist_ok=True)
        
        # Verify it's a git repo
        if not (self.repo_path / ".git").exists():
            raise ValueError(f"Not a git repository: {self.repo_path}")
    
    def _run_git(self, args: List[str]) -> str:
        """Run git command and return output."""
        cmd = ['git'] + args
        try:
            result = subprocess.run(
                cmd, 
                cwd=self.repo_path, 
                capture_output=True, 
                text=True, 
                check=True,
                encoding='utf-8',
                errors='replace'
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logger.error(f"Git command failed: {' '.join(cmd)}")
            logger.error(f"Error: {e.stderr}")
            raise
    
    def get_quarter_dates(self, quarter_str: str) -> Tuple[datetime, datetime]:
        """Convert 'YYYY-QN' to start/end dates."""
        match = re.match(r'(\d{4})-Q([1-4])', quarter_str)
        if not match:
            raise ValueError(f"Invalid quarter format: {quarter_str}. Use YYYY-QN (e.g., 2024-Q1)")
        
        year = int(match.group(1))
        quarter = int(match.group(2))
        
        # Quarter start months: Q1=1, Q2=4, Q3=7, Q4=10
        start_month = (quarter - 1) * 3 + 1
        start_date = datetime(year, start_month, 1)
        
        # End date is start of next quarter minus 1 day
        if quarter == 4:
            end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            end_date = datetime(year, start_month + 3, 1) - timedelta(days=1)
        
        return start_date, end_date
    
    def generate_quarters_since(self, since_date: str) -> List[str]:
        """Generate list of quarters from since_date to now."""
        start = datetime.strptime(since_date, '%Y-%m-%d')
        now = datetime.now()
        
        quarters = []
        current = start
        
        while current <= now:
            quarter = (current.month - 1) // 3 + 1
            quarter_str = f"{current.year}-Q{quarter}"
            quarters.append(quarter_str)
            
            # Move to next quarter
            if quarter == 4:
                current = datetime(current.year + 1, 1, 1)
            else:
                current = datetime(current.year, quarter * 3 + 1, 1)
        
        return list(dict.fromkeys(quarters))  # Remove duplicates, preserve order
    
    def get_commits_in_range(self, start_date: datetime, end_date: datetime, 
                            all_branches: bool = True) -> List[Dict]:
        """Get all commits in date range with detailed stats."""
        # Format: %H|%an|%ae|%at|%s
        # Hash|Author Name|Author Email|Timestamp|Subject
        format_str = '%H|%an|%ae|%at|%s'
        
        args = [
            'log',
            f'--since={start_date.isoformat()}',
            f'--until={end_date.isoformat()}',
            f'--format={format_str}',
            '--numstat',
            '--no-merges'
        ]
        
        if all_branches:
            args.append('--all')
        
        output = self._run_git(args)
        
        commits = []
        current_commit = None
        
        for line in output.split('\n'):
            if not line.strip():
                continue
            
            # Commit header line
            if '|' in line and len(line.split('|')) == 5:
                if current_commit:
                    commits.append(current_commit)
                
                parts = line.split('|')
                current_commit = {
                    'hash': parts[0],
                    'author_name': parts[1],
                    'author_email': parts[2],
                    'timestamp': int(parts[3]),
                    'date': datetime.fromtimestamp(int(parts[3])).isoformat(),
                    'subject': parts[4],
                    'files_changed': [],
                    'additions': 0,
                    'deletions': 0,
                    'total_churn': 0,
                    'net_churn': 0,
                    'file_count': 0
                }
            
            # File stat line (additions, deletions, filename)
            elif current_commit and '\t' in line:
                parts = line.split('\t')
                if len(parts) >= 3:
                    try:
                        adds = int(parts[0]) if parts[0] != '-' else 0
                        dels = int(parts[1]) if parts[1] != '-' else 0
                        filename = parts[2]
                        
                        current_commit['files_changed'].append({
                            'file': filename,
                            'additions': adds,
                            'deletions': dels
                        })
                        current_commit['additions'] += adds
                        current_commit['deletions'] += dels
                    except ValueError:
                        pass
        
        # Add last commit
        if current_commit:
            commits.append(current_commit)
        
        # Calculate derived metrics
        for commit in commits:
            commit['total_churn'] = commit['additions'] + commit['deletions']
            commit['net_churn'] = commit['additions'] - commit['deletions']
            commit['file_count'] = len(commit['files_changed'])
        
        return commits
    
    def calculate_halstead_metrics(self, file_path: Path) -> Optional[Dict]:
        """Calculate Halstead metrics for Python files using radon."""
        if not RADON_AVAILABLE:
            return None
        
        if not file_path.exists() or file_path.suffix != '.py':
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
            
            if not code.strip():
                return None
            
            # Halstead metrics
            h_metrics = h_visit(code)
            
            # Maintainability Index
            mi = mi_visit(code, multi=True)
            
            # Cyclomatic Complexity
            cc_results = cc_visit(code)
            avg_complexity = sum(item.complexity for item in cc_results) / len(cc_results) if cc_results else 0
            
            return {
                'maintainability_index': mi if isinstance(mi, (int, float)) else (mi.mi if hasattr(mi, 'mi') else 0),
                'halstead_volume': h_metrics.total.volume if h_metrics and h_metrics.total else 0,
                'halstead_difficulty': h_metrics.total.difficulty if h_metrics and h_metrics.total else 0,
                'halstead_effort': h_metrics.total.effort if h_metrics and h_metrics.total else 0,
                'avg_cyclomatic_complexity': round(avg_complexity, 2),
                'total_functions': len(cc_results)
            }
        except Exception as e:
            logger.debug(f"Failed to calculate Halstead for {file_path}: {e}")
            return None
    
    def calculate_quality_at_commit(self, commit_hash: str) -> Optional[Dict]:
        """Calculate quality metrics for code at a specific commit.
        
        Supports: Python, Java, C/C++, C#, JavaScript/TypeScript, Go
        Uses git show to get file contents at that commit without modifying working directory.
        """
        logger.info(f"Calculating quality metrics at commit {commit_hash[:8]}...")
        
        try:
            # Get list of all source files at this commit
            file_list = self._run_git(['ls-tree', '-r', '--name-only', commit_hash])
            all_files = [f.strip() for f in file_list.split('\n') if f.strip()]
            
            # Filter for supported languages
            source_files = []
            for file_path in all_files:
                for lang, extensions in LANGUAGE_EXTENSIONS.items():
                    if any(file_path.endswith(ext) for ext in extensions):
                        source_files.append((file_path, lang))
                        break
            
            # Exclude common non-source paths
            source_files = [(f, lang) for f, lang in source_files if not any(
                part in f for part in ['.venv/', 'venv/', 'node_modules/', '__pycache__/', 
                                      'site-packages/', '.git/', 'target/', 'build/', 'dist/',
                                      'vendor/', '.gradle/', 'bin/', 'obj/']
            )]
            
            if not source_files:
                logger.info(f"No source files found at commit {commit_hash[:8]}")
                return None
            
            # Metrics accumulators
            all_metrics = {
                'loc': [],
                'complexity': [],
                'comment_density': [],
                'avg_method_length': []
            }
            
            language_stats = defaultdict(int)
            
            # Analyze up to 1000 files maximum for comprehensive coverage
            analysis_limit = min(1000, len(source_files))
            total_files = len(source_files)
            coverage_pct = (analysis_limit / total_files * 100) if total_files > 0 else 0
            logger.info(f"Analyzing {analysis_limit}/{total_files} source files ({coverage_pct:.1f}% coverage) at commit {commit_hash[:8]}...")
            
            # Stratified sampling: take files evenly distributed across the repository
            if len(source_files) > analysis_limit:
                step = len(source_files) / analysis_limit
                sampled_files = [source_files[int(i * step)] for i in range(analysis_limit)]
            else:
                sampled_files = source_files
            
            for file_path, lang in sampled_files:
                try:
                    # Get file content at this commit
                    code = self._run_git(['show', f'{commit_hash}:{file_path}'])
                    
                    if not code.strip():
                        continue
                    
                    # Calculate language-agnostic metrics
                    metrics = self._analyze_code_quality(code, lang)
                    if metrics:
                        all_metrics['loc'].append(metrics['loc'])
                        all_metrics['complexity'].append(metrics['complexity'])
                        all_metrics['comment_density'].append(metrics['comment_density'])
                        all_metrics['avg_method_length'].append(metrics['avg_method_length'])
                        language_stats[lang] += 1
                
                except Exception as e:
                    logger.debug(f"Failed to analyze {file_path} at {commit_hash[:8]}: {e}")
                    continue
            
            if all_metrics['loc']:
                result = {
                    'avg_lines_of_code': round(sum(all_metrics['loc']) / len(all_metrics['loc']), 2),
                    'avg_complexity_per_file': round(sum(all_metrics['complexity']) / len(all_metrics['complexity']), 2),
                    'avg_comment_density': round(sum(all_metrics['comment_density']) / len(all_metrics['comment_density']), 2),
                    'avg_method_length': round(sum(all_metrics['avg_method_length']) / len(all_metrics['avg_method_length']), 2),
                    'files_analyzed': len(all_metrics['loc']),
                    'languages': dict(language_stats)
                }
                logger.info(f"Quality metrics calculated for {len(all_metrics['loc'])} files at {commit_hash[:8]} - Languages: {dict(language_stats)}")
                return result
            
            return None
        
        except Exception as e:
            logger.error(f"Failed to calculate quality at commit {commit_hash[:8]}: {e}")
            return None
    
    def _analyze_code_quality(self, code: str, language: str) -> Optional[Dict]:
        """Analyze code quality metrics for any supported language.
        
        Returns language-agnostic metrics:
        - loc: Lines of code (excluding blanks and comments)
        - complexity: Estimated cyclomatic complexity
        - comment_density: Ratio of comment lines to total lines
        - avg_method_length: Average lines per function/method
        """
        try:
            lines = code.split('\n')
            total_lines = len(lines)
            
            # Count blank lines
            blank_lines = sum(1 for line in lines if not line.strip())
            
            # Count comment lines (language-specific patterns)
            comment_patterns = {
                'python': [r'^\s*#', r'^\s*"""', r"^\s*'''"],
                'java': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
                'c': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
                'cpp': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
                'csharp': [r'^\s*//', r'^\s*/\*', r'^\s*\*', r'^\s*///'],
                'javascript': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
                'typescript': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
                'go': [r'^\s*//', r'^\s*/\*', r'^\s*\*']
            }
            
            patterns = comment_patterns.get(language, [r'^\s*//'])
            comment_lines = 0
            for line in lines:
                if any(re.match(pattern, line) for pattern in patterns):
                    comment_lines += 1
            
            # Lines of code (excluding blanks and comments)
            loc = total_lines - blank_lines - comment_lines
            
            # Comment density (percentage)
            comment_density = (comment_lines / total_lines * 100) if total_lines > 0 else 0
            
            # Estimate cyclomatic complexity by counting decision points
            complexity_patterns = {
                'python': [r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\band\b', r'\bor\b', r'\belif\b', r'\bexcept\b'],
                'java': [r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\bcase\b', r'\bcatch\b', r'\b&&\b', r'\b\|\|\b', r'\?'],
                'c': [r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\bcase\b', r'\b&&\b', r'\b\|\|\b', r'\?'],
                'cpp': [r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\bcase\b', r'\bcatch\b', r'\b&&\b', r'\b\|\|\b', r'\?'],
                'csharp': [r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\bcase\b', r'\bcatch\b', r'\b&&\b', r'\b\|\|\b', r'\?'],
                'javascript': [r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\bcase\b', r'\bcatch\b', r'\b&&\b', r'\b\|\|\b', r'\?'],
                'typescript': [r'\bif\b', r'\bfor\b', r'\bwhile\b', r'\bcase\b', r'\bcatch\b', r'\b&&\b', r'\b\|\|\b', r'\?'],
                'go': [r'\bif\b', r'\bfor\b', r'\bswitch\b', r'\bcase\b', r'\b&&\b', r'\b\|\|\b']
            }
            
            complexity = 1  # Base complexity
            patterns = complexity_patterns.get(language, [r'\bif\b', r'\bfor\b', r'\bwhile\b'])
            for pattern in patterns:
                complexity += len(re.findall(pattern, code))
            
            # Count methods/functions to estimate average length
            method_patterns = {
                'python': r'^\s*def\s+\w+',
                'java': r'^\s*(public|private|protected|static|\s)*\s+\w+\s+\w+\s*\(',
                'c': r'^\s*\w+\s+\w+\s*\([^)]*\)\s*\{',
                'cpp': r'^\s*\w+\s+\w+\s*\([^)]*\)\s*\{',
                'csharp': r'^\s*(public|private|protected|static|\s)*\s+\w+\s+\w+\s*\(',
                'javascript': r'^\s*(function\s+\w+|const\s+\w+\s*=\s*\([^)]*\)\s*=>|\w+\s*:\s*function)',
                'typescript': r'^\s*(function\s+\w+|const\s+\w+\s*=\s*\([^)]*\)\s*=>|\w+\s*:\s*function)',
                'go': r'^\s*func\s+\w+'
            }
            
            pattern = method_patterns.get(language, r'^\s*def\s+\w+')
            method_count = len(re.findall(pattern, code, re.MULTILINE))
            avg_method_length = (loc / method_count) if method_count > 0 else loc
            
            return {
                'loc': max(0, loc),
                'complexity': max(1, complexity),
                'comment_density': round(comment_density, 2),
                'avg_method_length': round(avg_method_length, 2)
            }
        
        except Exception as e:
            logger.debug(f"Failed to analyze code quality: {e}")
            return None
    
    def analyze_commits(self, commits: List[Dict], calculate_quality: bool = False) -> Dict:
        """Analyze commit patterns and generate metrics.
        
        Args:
            commits: List of commit dictionaries
            calculate_quality: If True, calculate Halstead/quality metrics for Python files
        """
        if not commits:
            return self._empty_analysis()
        
        # Group by contributor
        by_contributor = defaultdict(list)
        for commit in commits:
            by_contributor[commit['author_email']].append(commit)
        
        # Group by date
        by_date = defaultdict(list)
        for commit in commits:
            date = datetime.fromtimestamp(commit['timestamp']).date()
            by_date[date].append(commit)
        
        # Calculate metrics
        total_commits = len(commits)
        total_additions = sum(c['additions'] for c in commits)
        total_deletions = sum(c['deletions'] for c in commits)
        total_churn = sum(c['total_churn'] for c in commits)
        net_churn = total_additions - total_deletions
        
        # Time-based metrics
        dates = sorted(by_date.keys())
        date_range_days = (dates[-1] - dates[0]).days + 1 if dates else 1
        active_days = len(dates)
        
        # Commit frequency
        commits_per_day = total_commits / max(date_range_days, 1)
        commits_per_active_day = total_commits / max(active_days, 1)
        commits_per_week = commits_per_day * 7
        
        # Commit size metrics
        avg_churn_per_commit = total_churn / total_commits if total_commits else 0
        avg_files_per_commit = sum(c['file_count'] for c in commits) / total_commits if total_commits else 0
        avg_additions_per_commit = total_additions / total_commits if total_commits else 0
        avg_deletions_per_commit = total_deletions / total_commits if total_commits else 0
        
        # Rework ratio (deletions/additions - high = lots of rework)
        rework_ratio = total_deletions / total_additions if total_additions > 0 else 0
        
        # Contributor metrics
        contributor_stats = []
        for email, contributor_commits in by_contributor.items():
            name = contributor_commits[0]['author_name']
            contrib_additions = sum(c['additions'] for c in contributor_commits)
            contrib_deletions = sum(c['deletions'] for c in contributor_commits)
            contrib_churn = sum(c['total_churn'] for c in contributor_commits)
            
            contributor_stats.append({
                'email': email,
                'name': name,
                'commit_count': len(contributor_commits),
                'additions': contrib_additions,
                'deletions': contrib_deletions,
                'total_churn': contrib_churn,
                'net_churn': contrib_additions - contrib_deletions,
                'avg_churn_per_commit': contrib_churn / len(contributor_commits),
                'commit_percentage': (len(contributor_commits) / total_commits * 100)
            })
        
        # Sort contributors by commit count
        contributor_stats.sort(key=lambda x: x['commit_count'], reverse=True)
        
        # Commit size distribution
        small_commits = len([c for c in commits if c['total_churn'] < 50])
        medium_commits = len([c for c in commits if 50 <= c['total_churn'] < 200])
        large_commits = len([c for c in commits if 200 <= c['total_churn'] < 1000])
        huge_commits = len([c for c in commits if c['total_churn'] >= 1000])
        
        # Calculate quality metrics if requested
        quality_metrics = None
        if calculate_quality and RADON_AVAILABLE:
            # Get the last commit hash in the date range to analyze code at that point
            if commits:
                last_commit_hash = commits[-1]['hash']
                quality_metrics = self.calculate_quality_at_commit(last_commit_hash)
        
        result = {
            'commit_metrics': {
                'total_commits': total_commits,
                'commits_per_day': round(commits_per_day, 2),
                'commits_per_active_day': round(commits_per_active_day, 2),
                'commits_per_week': round(commits_per_week, 2),
                'active_days': active_days,
                'total_days_in_range': date_range_days
            },
            'churn_metrics': {
                'total_additions': total_additions,
                'total_deletions': total_deletions,
                'total_churn': total_churn,
                'net_churn': net_churn,
                'avg_churn_per_commit': round(avg_churn_per_commit, 2),
                'avg_additions_per_commit': round(avg_additions_per_commit, 2),
                'avg_deletions_per_commit': round(avg_deletions_per_commit, 2),
                'avg_files_per_commit': round(avg_files_per_commit, 2),
                'rework_ratio': round(rework_ratio, 3)
            },
            'commit_size_distribution': {
                'small_commits_under_50': small_commits,
                'medium_commits_50_200': medium_commits,
                'large_commits_200_1000': large_commits,
                'huge_commits_over_1000': huge_commits
            },
            'contributor_metrics': {
                'total_contributors': len(by_contributor),
                'contributors': contributor_stats,
                'churn_per_contributor': round(total_churn / len(by_contributor), 2) if by_contributor else 0
            }
        }
        
        if quality_metrics:
            result['quality_metrics'] = quality_metrics
        
        return result
    
    def _empty_analysis(self) -> Dict:
        """Return empty analysis structure."""
        return {
            'commit_metrics': {
                'total_commits': 0,
                'commits_per_day': 0,
                'commits_per_active_day': 0,
                'commits_per_week': 0,
                'active_days': 0,
                'total_days_in_range': 0
            },
            'churn_metrics': {
                'total_additions': 0,
                'total_deletions': 0,
                'total_churn': 0,
                'net_churn': 0,
                'avg_churn_per_commit': 0,
                'avg_additions_per_commit': 0,
                'avg_deletions_per_commit': 0,
                'avg_files_per_commit': 0,
                'rework_ratio': 0
            },
            'commit_size_distribution': {
                'small_commits_under_50': 0,
                'medium_commits_50_200': 0,
                'large_commits_200_1000': 0,
                'huge_commits_over_1000': 0
            },
            'contributor_metrics': {
                'total_contributors': 0,
                'contributors': [],
                'churn_per_contributor': 0
            }
        }
    
    def create_snapshot(self, quarter: str, all_branches: bool = True, include_quality: bool = False) -> str:
        """Create snapshot for a specific quarter.
        
        Args:
            quarter: Quarter string (YYYY-QN)
            all_branches: Include all branches or just current
            include_quality: Calculate Halstead/quality metrics (slower, requires radon)
        """
        logger.info(f"Creating snapshot for {quarter}...")
        if include_quality and not RADON_AVAILABLE:
            logger.warning("Quality metrics requested but radon not available. Install with: pip install radon")
            include_quality = False
        
        start_date, end_date = self.get_quarter_dates(quarter)
        
        # Get commits
        commits = self.get_commits_in_range(start_date, end_date, all_branches)
        
        # Analyze
        analysis = self.analyze_commits(commits, calculate_quality=include_quality)
        
        # Build snapshot
        snapshot = {
            'metadata': {
                'quarter': quarter,
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat(),
                'snapshot_created': datetime.now().isoformat(),
                'repository_path': str(self.repo_path),
                'all_branches': all_branches
            },
            'analysis': analysis,
            'raw_commit_count': len(commits)
        }
        
        # Save
        snapshot_file = self.snapshots_dir / f"snapshot-{quarter}.json"
        with open(snapshot_file, 'w', encoding='utf-8') as f:
            json.dump(snapshot, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✅ Snapshot saved: {snapshot_file}")
        logger.info(f"   Commits: {len(commits)}, Contributors: {analysis['contributor_metrics']['total_contributors']}")
        
        return str(snapshot_file)
    
    def create_snapshots_since(self, since_date: str, all_branches: bool = True, include_quality: bool = False) -> List[str]:
        """Create snapshots for all quarters since given date.
        
        Args:
            since_date: Start date (YYYY-MM-DD)
            all_branches: Include all branches or just current
            include_quality: Calculate Halstead/quality metrics (slower, requires radon)
        """
        quarters = self.generate_quarters_since(since_date)
        
        logger.info(f"Generating {len(quarters)} quarterly snapshots: {', '.join(quarters)}")
        if include_quality:
            logger.info("Quality metrics enabled (slower but includes MI, Halstead, CC)")
        
        snapshot_files = []
        for quarter in quarters:
            try:
                snapshot_file = self.create_snapshot(quarter, all_branches, include_quality)
                snapshot_files.append(snapshot_file)
            except Exception as e:
                logger.error(f"Failed to create snapshot for {quarter}: {e}")
        
        return snapshot_files
    
    def compare_quarters(self, q1: str, q2: str) -> Dict:
        """Compare two quarterly snapshots."""
        # Load snapshots
        file1 = self.snapshots_dir / f"snapshot-{q1}.json"
        file2 = self.snapshots_dir / f"snapshot-{q2}.json"
        
        if not file1.exists() or not file2.exists():
            raise FileNotFoundError(f"Missing snapshot files for {q1} or {q2}")
        
        with open(file1, 'r') as f:
            snap1 = json.load(f)
        with open(file2, 'r') as f:
            snap2 = json.load(f)
        
        a1 = snap1['analysis']
        a2 = snap2['analysis']
        
        # Calculate deltas
        comparison = {
            'metadata': {
                'baseline_quarter': q1,
                'current_quarter': q2,
                'comparison_date': datetime.now().isoformat()
            },
            'commit_metrics_delta': {
                'commits_change': a2['commit_metrics']['total_commits'] - a1['commit_metrics']['total_commits'],
                'commits_per_day_change': round(a2['commit_metrics']['commits_per_day'] - a1['commit_metrics']['commits_per_day'], 2),
                'commits_per_week_change': round(a2['commit_metrics']['commits_per_week'] - a1['commit_metrics']['commits_per_week'], 2),
                'active_days_change': a2['commit_metrics']['active_days'] - a1['commit_metrics']['active_days']
            },
            'churn_metrics_delta': {
                'total_churn_change': a2['churn_metrics']['total_churn'] - a1['churn_metrics']['total_churn'],
                'avg_churn_per_commit_change': round(a2['churn_metrics']['avg_churn_per_commit'] - a1['churn_metrics']['avg_churn_per_commit'], 2),
                'rework_ratio_change': round(a2['churn_metrics']['rework_ratio'] - a1['churn_metrics']['rework_ratio'], 3),
                'net_churn_change': a2['churn_metrics']['net_churn'] - a1['churn_metrics']['net_churn']
            },
            'contributor_metrics_delta': {
                'contributors_change': a2['contributor_metrics']['total_contributors'] - a1['contributor_metrics']['total_contributors'],
                'churn_per_contributor_change': round(a2['contributor_metrics']['churn_per_contributor'] - a1['contributor_metrics']['churn_per_contributor'], 2)
            }
        }
        
        return comparison
    
    def print_snapshot_summary(self, quarter: str):
        """Print formatted summary of a snapshot."""
        file = self.snapshots_dir / f"snapshot-{quarter}.json"
        
        if not file.exists():
            print(f"❌ Snapshot not found: {quarter}")
            return
        
        with open(file, 'r') as f:
            snapshot = json.load(f)
        
        a = snapshot['analysis']
        
        print(f"\n{'='*70}")
        print(f"📊 Git Productivity Snapshot: {quarter}")
        print(f"{'='*70}")
        
        print(f"\n📝 COMMIT METRICS")
        print(f"   Total Commits: {a['commit_metrics']['total_commits']}")
        print(f"   Commits/Day: {a['commit_metrics']['commits_per_day']:.2f}")
        print(f"   Commits/Week: {a['commit_metrics']['commits_per_week']:.2f}")
        print(f"   Active Days: {a['commit_metrics']['active_days']}/{a['commit_metrics']['total_days_in_range']}")
        
        print(f"\n📈 CHURN METRICS")
        print(f"   Total Additions: {a['churn_metrics']['total_additions']:,}")
        print(f"   Total Deletions: {a['churn_metrics']['total_deletions']:,}")
        print(f"   Net Change: {a['churn_metrics']['net_churn']:+,}")
        print(f"   Avg Churn/Commit: {a['churn_metrics']['avg_churn_per_commit']:.2f} lines")
        print(f"   Rework Ratio: {a['churn_metrics']['rework_ratio']:.3f}")
        
        print(f"\n📦 COMMIT SIZE DISTRIBUTION")
        print(f"   Small (<50 lines): {a['commit_size_distribution']['small_commits_under_50']}")
        print(f"   Medium (50-200): {a['commit_size_distribution']['medium_commits_50_200']}")
        print(f"   Large (200-1000): {a['commit_size_distribution']['large_commits_200_1000']}")
        print(f"   Huge (>1000): {a['commit_size_distribution']['huge_commits_over_1000']}")
        
        print(f"\n👥 CONTRIBUTOR METRICS")
        print(f"   Total Contributors: {a['contributor_metrics']['total_contributors']}")
        print(f"   Churn/Contributor: {a['contributor_metrics']['churn_per_contributor']:.2f}")
        
        print(f"\n   Top 5 Contributors:")
        for i, c in enumerate(a['contributor_metrics']['contributors'][:5], 1):
            print(f"      {i}. {c['name']} ({c['email']})")
            print(f"         Commits: {c['commit_count']} ({c['commit_percentage']:.1f}%)")
            print(f"         Churn: {c['total_churn']:,} lines (avg {c['avg_churn_per_commit']:.0f}/commit)")
        
        print(f"{'='*70}\n")
    
    def print_trend_report(self):
        """Print comprehensive trend report across all snapshots."""
        snapshot_files = sorted(self.snapshots_dir.glob('snapshot-*.json'))
        
        if not snapshot_files:
            print("\n❌ No snapshots found. Generate snapshots first with 'snapshots' command.\n")
            return
        
        print("\n" + "="*110)
        print("📊 GIT PRODUCTIVITY TREND REPORT - QUARTERLY OVERVIEW")
        print("="*110)
        print(f"Repository: {self.repo_path.name}")
        print(f"Snapshots Directory: {self.snapshots_dir}")
        print("="*110)
        
        # Table header
        print(f"\n{'Quarter':<12} {'Commits':<10} {'Contributors':<15} {'Total Churn':<15} {'Avg/Commit':<12} {'Rework':<10} {'Commits/Week':<12}")
        print("-"*110)
        
        # Load all snapshots and collect data
        all_data = []
        total_commits = 0
        total_churn = 0
        all_contributors = set()
        
        for snapshot_file in snapshot_files:
            with open(snapshot_file, 'r') as f:
                data = json.load(f)
            
            quarter = data['metadata']['quarter']
            cm = data['analysis']['commit_metrics']
            chm = data['analysis']['churn_metrics']
            contrib = data['analysis']['contributor_metrics']
            
            # Print row
            print(f"{quarter:<12} {cm['total_commits']:<10} {contrib['total_contributors']:<15} "
                  f"{chm['total_churn']:<15,} {chm['avg_churn_per_commit']:<12.1f} "
                  f"{chm['rework_ratio']:<10.3f} {cm['commits_per_week']:<12.1f}")
            
            # Accumulate totals
            total_commits += cm['total_commits']
            total_churn += chm['total_churn']
            for c in contrib['contributors']:
                all_contributors.add(c['email'])
            
            all_data.append(data)
        
        print("-"*110)
        
        # Overall summary
        print(f"\n📈 OVERALL TOTALS:")
        print(f"   Total Commits: {total_commits:,}")
        print(f"   Unique Contributors: {len(all_contributors)}")
        print(f"   Total Churn: {total_churn:,} lines")
        if total_commits > 0:
            print(f"   Avg Churn/Commit: {total_churn/total_commits:.1f} lines")
        
        # Trend analysis
        if len(all_data) >= 2:
            first = all_data[0]['analysis']
            last = all_data[-1]['analysis']
            
            print(f"\n📊 TREND ANALYSIS ({all_data[0]['metadata']['quarter']} → {all_data[-1]['metadata']['quarter']}):")
            
            commits_change = last['commit_metrics']['total_commits'] - first['commit_metrics']['total_commits']
            commits_per_week_change = last['commit_metrics']['commits_per_week'] - first['commit_metrics']['commits_per_week']
            churn_per_commit_change = last['churn_metrics']['avg_churn_per_commit'] - first['churn_metrics']['avg_churn_per_commit']
            rework_change = last['churn_metrics']['rework_ratio'] - first['churn_metrics']['rework_ratio']
            
            print(f"   Commits per Quarter: {commits_change:+d}")
            print(f"   Commits per Week: {commits_per_week_change:+.2f}")
            print(f"   Avg Churn per Commit: {churn_per_commit_change:+.1f} lines")
            print(f"   Rework Ratio: {rework_change:+.3f}")
            
            # AI Impact indicators
            print(f"\n🤖 AI IMPACT INDICATORS:")
            positive_indicators = []
            negative_indicators = []
            
            if commits_per_week_change > 0.5:
                positive_indicators.append("✅ Increased commit frequency (faster iteration)")
            elif commits_per_week_change < -0.5:
                negative_indicators.append("⚠️  Decreased commit frequency")
            
            if churn_per_commit_change < -20:
                positive_indicators.append("✅ Smaller commits (better granularity)")
            elif churn_per_commit_change > 50:
                negative_indicators.append("⚠️  Larger commits (possible code bloat)")
            
            if rework_change < -0.05:
                positive_indicators.append("✅ Reduced rework ratio (less thrashing)")
            elif rework_change > 0.1:
                negative_indicators.append("⚠️  Increased rework ratio (more code churn)")
            
            # Calculate average commit size distribution trend
            first_small_pct = first['commit_size_distribution']['small_commits_under_50'] / max(first['commit_metrics']['total_commits'], 1) * 100
            last_small_pct = last['commit_size_distribution']['small_commits_under_50'] / max(last['commit_metrics']['total_commits'], 1) * 100
            
            if last_small_pct > first_small_pct + 10:
                positive_indicators.append("✅ More small commits (focused changes)")
            
            if positive_indicators:
                for indicator in positive_indicators:
                    print(f"   {indicator}")
            
            if negative_indicators:
                for indicator in negative_indicators:
                    print(f"   {indicator}")
            
            if not positive_indicators and not negative_indicators:
                print("   ℹ️  No significant trends detected")
        
        # Top contributors across all time
        contributor_totals = defaultdict(lambda: {'name': '', 'commits': 0, 'churn': 0})
        for data in all_data:
            for c in data['analysis']['contributor_metrics']['contributors']:
                email = c['email']
                contributor_totals[email]['name'] = c['name']
                contributor_totals[email]['commits'] += c['commit_count']
                contributor_totals[email]['churn'] += c['total_churn']
        
        top_contributors = sorted(contributor_totals.items(), key=lambda x: x[1]['commits'], reverse=True)[:10]
        
        print(f"\n👥 TOP 10 CONTRIBUTORS (ALL TIME):")
        for i, (email, stats) in enumerate(top_contributors, 1):
            avg_churn = stats['churn'] / stats['commits'] if stats['commits'] > 0 else 0
            pct = stats['commits'] / total_commits * 100 if total_commits > 0 else 0
            print(f"   {i:2d}. {stats['name']:<30} - {stats['commits']:4d} commits ({pct:5.1f}%), {stats['churn']:7,} churn (avg {avg_churn:.0f}/commit)")
        
        # Quality Metrics Trend (if available)
        quality_data = [(d['metadata']['quarter'], d['analysis'].get('quality_metrics')) for d in all_data]
        quality_data = [(q, qm) for q, qm in quality_data if qm is not None]
        
        if quality_data:
            print("\n" + "="*110)
            print("📊 CODE QUALITY METRICS TREND (Multi-Language Analysis)")
            print("="*110)
            print(f"\n{'Quarter':<12} {'Avg LOC':<12} {'Complexity':<12} {'Comments%':<12} {'Method Len':<12} {'Files':<10} {'Languages':<30}")
            print("-"*110)
            
            for quarter, qm in quality_data:
                langs = ', '.join(f"{k}:{v}" for k, v in qm.get('languages', {}).items())
                print(f"{quarter:<12} {qm['avg_lines_of_code']:<12.1f} "
                      f"{qm['avg_complexity_per_file']:<12.1f} "
                      f"{qm['avg_comment_density']:<12.1f} "
                      f"{qm['avg_method_length']:<12.1f} "
                      f"{qm['files_analyzed']:<10} "
                      f"{langs[:30]:<30}")
            
            print("-"*110)
            
            # Quality trend analysis
            if len(quality_data) >= 2:
                first_q, first_qm = quality_data[0]
                last_q, last_qm = quality_data[-1]
                
                loc_change = last_qm['avg_lines_of_code'] - first_qm['avg_lines_of_code']
                comp_change = last_qm['avg_complexity_per_file'] - first_qm['avg_complexity_per_file']
                comment_change = last_qm['avg_comment_density'] - first_qm['avg_comment_density']
                method_change = last_qm['avg_method_length'] - first_qm['avg_method_length']
                
                print(f"\n🔬 QUALITY TREND ANALYSIS ({first_q} → {last_q}):")
                print(f"   Avg Lines of Code: {loc_change:+.1f} ({'⚠️ Growing files' if loc_change > 50 else '✅ Stable' if abs(loc_change) <= 50 else '✅ Shrinking files'})")
                print(f"   Complexity per File: {comp_change:+.1f} ({'⚠️ Increasing complexity' if comp_change > 10 else '✅ Decreasing complexity' if comp_change < -10 else '➡️ Stable'})")
                print(f"   Comment Density: {comment_change:+.1f}% ({'✅ More documented' if comment_change > 2 else '⚠️ Less documented' if comment_change < -2 else '➡️ Stable'})")
                print(f"   Avg Method Length: {method_change:+.1f} lines ({'⚠️ Longer methods' if method_change > 5 else '✅ Shorter methods' if method_change < -5 else '➡️ Stable'})")
                
                # Overall quality assessment
                print(f"\n🎯 OVERALL CODE QUALITY:")
                quality_score = 0
                
                # Positive indicators (smaller files, lower complexity, better docs, shorter methods)
                if loc_change < -5: quality_score += 1
                elif loc_change < 5: quality_score += 0.5  # Stable is good
                
                if comp_change < -2: quality_score += 1
                elif comp_change < 2: quality_score += 0.5  # Stable is good
                
                if comment_change > 1: quality_score += 1
                elif comment_change > -1: quality_score += 0.5  # Stable is acceptable
                
                if method_change < -2: quality_score += 1
                elif method_change < 2: quality_score += 0.5  # Stable is good
                
                if quality_score >= 3.5:
                    print(f"   ✅ EXCELLENT - Code quality significantly improving (score: {quality_score:.1f}/4)")
                elif quality_score >= 2.5:
                    print(f"   ✅ GOOD - Code quality trending positively (score: {quality_score:.1f}/4)")
                elif quality_score >= 1.5:
                    print(f"   ➡️ STABLE - Code quality maintained well (score: {quality_score:.1f}/4)")
                else:
                    print(f"   ⚠️ CONCERNING - Code quality may be declining (score: {quality_score:.1f}/4)")
        
        print("\n" + "="*110 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Git Productivity Analyzer - Quarterly snapshots from Git history',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all quarterly snapshots since 2024
  python git_productivity_analyzer.py snapshots --since 2024-01-01
  
  # Generate single quarter
  python git_productivity_analyzer.py snapshot --quarter 2024-Q4
  
  # Compare two quarters
  python git_productivity_analyzer.py compare 2024-Q1 2024-Q4
  
  # Show summary of quarter
  python git_productivity_analyzer.py show 2024-Q3
        """
    )
    
    parser.add_argument('--repo-path', default='.', help='Path to Git repository (default: current dir)')
    parser.add_argument('--current-branch-only', action='store_true', help='Only analyze current branch (default: all branches)')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Snapshots command (plural - generate multiple)
    snapshots_parser = subparsers.add_parser('snapshots', help='Generate snapshots for all quarters since date')
    snapshots_parser.add_argument('--since', default='2024-01-01', help='Start date (YYYY-MM-DD, default: 2024-01-01)')
    snapshots_parser.add_argument('--with-quality', action='store_true', help='Include Halstead/MI/CC metrics (slower, requires radon)')
    
    # Snapshot command (singular - generate one)
    snapshot_parser = subparsers.add_parser('snapshot', help='Generate snapshot for specific quarter')
    snapshot_parser.add_argument('--quarter', required=True, help='Quarter (YYYY-QN, e.g., 2024-Q1)')
    snapshot_parser.add_argument('--with-quality', action='store_true', help='Include Halstead/MI/CC metrics (slower, requires radon)')
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare two quarters')
    compare_parser.add_argument('baseline', help='Baseline quarter (YYYY-QN)')
    compare_parser.add_argument('current', help='Current quarter (YYYY-QN)')
    
    # Show command
    show_parser = subparsers.add_parser('show', help='Show snapshot summary')
    show_parser.add_argument('quarter', help='Quarter to show (YYYY-QN)')
    
    # Report command (trend report across all snapshots)
    report_parser = subparsers.add_parser('report', help='Generate comprehensive trend report across all snapshots')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        analyzer = GitProductivityAnalyzer(args.repo_path)
        all_branches = not args.current_branch_only
        
        if args.command == 'snapshots':
            include_quality = getattr(args, 'with_quality', False)
            snapshot_files = analyzer.create_snapshots_since(args.since, all_branches, include_quality)
            print(f"\n✅ Generated {len(snapshot_files)} snapshots")
            print(f"   Output directory: {analyzer.snapshots_dir}")
            if include_quality:
                print(f"   📊 Quality metrics included (MI, Halstead, CC)")
        
        elif args.command == 'snapshot':
            include_quality = getattr(args, 'with_quality', False)
            snapshot_file = analyzer.create_snapshot(args.quarter, all_branches, include_quality)
            analyzer.print_snapshot_summary(args.quarter)
        
        elif args.command == 'compare':
            comparison = analyzer.compare_quarters(args.baseline, args.current)
            
            print(f"\n{'='*70}")
            print(f"📊 Quarter Comparison: {args.baseline} → {args.current}")
            print(f"{'='*70}")
            
            d = comparison['commit_metrics_delta']
            print(f"\n📝 COMMIT CHANGES")
            print(f"   Total Commits: {d['commits_change']:+d}")
            print(f"   Commits/Day: {d['commits_per_day_change']:+.2f}")
            print(f"   Commits/Week: {d['commits_per_week_change']:+.2f}")
            
            d = comparison['churn_metrics_delta']
            print(f"\n📈 CHURN CHANGES")
            print(f"   Total Churn: {d['total_churn_change']:+,}")
            print(f"   Avg Churn/Commit: {d['avg_churn_per_commit_change']:+.2f}")
            print(f"   Rework Ratio: {d['rework_ratio_change']:+.3f}")
            print(f"   Net Churn: {d['net_churn_change']:+,}")
            
            d = comparison['contributor_metrics_delta']
            print(f"\n👥 CONTRIBUTOR CHANGES")
            print(f"   Contributors: {d['contributors_change']:+d}")
            print(f"   Churn/Contributor: {d['churn_per_contributor_change']:+.2f}")
            print(f"{'='*70}\n")
        
        elif args.command == 'show':
            analyzer.print_snapshot_summary(args.quarter)
        
        elif args.command == 'report':
            analyzer.print_trend_report()
    
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
