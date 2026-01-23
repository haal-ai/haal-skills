#!/usr/bin/env python3
"""
GitHub PR Analyzer using GitHub CLI
Collects comprehensive PR data for code review analysis.

Usage:
    python gh-pr-analyzer.py --pr 123
    python gh-pr-analyzer.py --branch feature/my-branch
    python gh-pr-analyzer.py --latest-open
"""

import subprocess
import json
import sys
import argparse
from typing import Dict, Any, Optional, List
from datetime import datetime

class GitHubPRAnalyzer:
    def __init__(self):
        self._check_auth()
        self.repo_info = self._get_repo_info()
        
    def _check_auth(self):
        """Check GitHub CLI authentication status."""
        print("🔐 Checking GitHub CLI authentication...")
        output, code = self._run_gh_command(['auth', 'status'])
        if code != 0:
            print("❌ ERROR: GitHub CLI is not authenticated!")
            print("Please run: gh auth login")
            print("Then try again.")
            sys.exit(1)
        print("✅ GitHub CLI authentication verified")
        
    def _run_gh_command(self, cmd: List[str]) -> tuple[str, int]:
        """Run GitHub CLI command and return output and exit code."""
        try:
            result = subprocess.run(['gh'] + cmd, 
                                  capture_output=True, 
                                  encoding='utf-8',
                                  errors='replace',
                                  check=False)
            return result.stdout.strip(), result.returncode
        except FileNotFoundError:
            print("ERROR: GitHub CLI (gh) not found. Please install GitHub CLI.")
            sys.exit(1)
        except UnicodeDecodeError as e:
            print(f"WARNING: Unicode decode error: {e}")
            # Fallback: try with bytes and decode manually
            try:
                result = subprocess.run(['gh'] + cmd, 
                                      capture_output=True, 
                                      check=False)
                output = result.stdout.decode('utf-8', errors='replace')
                return output.strip(), result.returncode
            except Exception as fallback_error:
                print(f"ERROR: Failed to decode command output: {fallback_error}")
                return "", 1
            
    def _get_repo_info(self) -> Dict[str, Any]:
        """Get current repository information."""
        print("🔍 Getting repository information...")
        
        # Get repo name and owner
        output, code = self._run_gh_command(['repo', 'view', '--json', 'name,owner,defaultBranchRef'])
        if code != 0:
            print(f"ERROR: Failed to get repo info: {output}")
            sys.exit(1)
            
        repo_data = json.loads(output)
        
        # Get current branch
        try:
            git_result = subprocess.run(['git', 'branch', '--show-current'], 
                                       capture_output=True, 
                                       encoding='utf-8',
                                       errors='replace')
            current_branch = git_result.stdout.strip() if git_result.returncode == 0 else "unknown"
        except UnicodeDecodeError:
            current_branch = "unknown"
        
        return {
            'name': repo_data['name'],
            'owner': repo_data['owner']['login'],
            'default_branch': repo_data['defaultBranchRef']['name'],
            'current_branch': current_branch,
            'full_name': f"{repo_data['owner']['login']}/{repo_data['name']}"
        }
        
    def get_pr_by_number(self, pr_number: int, skip_diff: bool = False, files_filter: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
        """Get PR details by PR number.
        
        Args:
            pr_number: PR number to analyze
            skip_diff: If True, skip fetching the diff content (for metadata-only analysis)
            files_filter: If provided, only get diff for these specific files
        """
        print(f"🔍 Analyzing PR #{pr_number}...")
        
        # Get basic PR details first
        basic_fields = ['title', 'body', 'state', 'number', 'createdAt', 'updatedAt', 'baseRefName', 'headRefName', 'author']
        
        output, code = self._run_gh_command([
            'pr', 'view', str(pr_number), 
            '--json', ','.join(basic_fields)
        ])
        
        if code != 0:
            print(f"ERROR: Failed to get PR #{pr_number}: {output}")
            return None
            
        pr_data = json.loads(output)
        
        # Get additional fields separately to avoid API issues
        try:
            # Get mergeable status and merge commit
            merge_output, _ = self._run_gh_command([
                'pr', 'view', str(pr_number), '--json', 'mergeable,mergedAt,mergeCommit'
            ])
            if merge_output:
                merge_data = json.loads(merge_output)
                pr_data.update(merge_data)
        except:
            pass
            
        try:
            # Get statistics
            stats_output, _ = self._run_gh_command([
                'pr', 'view', str(pr_number), '--json', 'additions,deletions,changedFiles'
            ])
            if stats_output:
                stats_data = json.loads(stats_output)
                pr_data.update(stats_data)
        except:
            pass
        
        # Get changed files list (always needed for file detection)
        print(f"📁 Getting changed files for PR #{pr_number}...")
        files_output, files_code = self._run_gh_command([
            'pr', 'view', str(pr_number), 
            '--json', 'files'
        ])
        if files_code == 0:
            files_data = json.loads(files_output)
            pr_data['files'] = files_data.get('files', [])
        
        # Get PR diff (conditionally)
        if skip_diff:
            print(f"⏭️  Skipping diff fetch (metadata-only mode)")
            pr_data['diff'] = ""
        elif files_filter:
            # Get diff only for specified files
            print(f"📄 Getting filtered diff for {len(files_filter)} code files...")
            pr_data['diff'] = self._get_filtered_diff(pr_number, pr_data, files_filter)
        else:
            # Get full diff
            print(f"📄 Getting full diff for PR #{pr_number}...")
            pr_data['diff'] = self._get_diff(pr_number, pr_data)
        
        return pr_data
    
    def _get_diff(self, pr_number: int, pr_data: Dict[str, Any]) -> str:
        """Get diff for PR, with fallback to git show for merged PRs."""
        # Try gh pr diff first
        diff_output, diff_code = self._run_gh_command(['pr', 'diff', str(pr_number)])
        
        if diff_code == 0 and diff_output:
            return diff_output
        
        # Fallback to git show for merged PRs
        print(f"⚠️  gh pr diff failed, trying git show fallback...")
        
        # Check if we have merge commit from PR data
        merge_commit_data = pr_data.get('mergeCommit')
        if merge_commit_data and isinstance(merge_commit_data, dict):
            merge_commit = merge_commit_data.get('oid')
            
            if merge_commit:
                print(f"📦 Using git show for merge commit {merge_commit[:7]}...")
                try:
                    # For merge commits, use --first-parent to show actual changes
                    git_result = subprocess.run(
                        ['git', 'show', '--first-parent', '-m', merge_commit],
                        capture_output=True,
                        encoding='utf-8',
                        errors='replace'
                    )
                    
                    if git_result.returncode == 0 and git_result.stdout:
                        print(f"✅ Successfully retrieved diff from git")
                        return git_result.stdout
                    else:
                        print(f"⚠️  git show failed: {git_result.stderr}")
                except Exception as e:
                    print(f"⚠️  Error running git show: {e}")
        else:
            print(f"⚠️  No merge commit found (PR may not be merged)")
        
        return "Failed to get diff"
    
    def _get_filtered_diff(self, pr_number: int, pr_data: Dict[str, Any], files: List[str]) -> str:
        """Get diff content only for specified files."""
        # Get full diff with fallback support
        diff_output = self._get_diff(pr_number, pr_data)
        
        if diff_output == "Failed to get diff":
            return diff_output
        
        # Parse diff and filter for specified files
        filtered_chunks = []
        current_chunk = []
        current_file = None
        
        for line in diff_output.split('\n'):
            if line.startswith('diff --git'):
                # Save previous chunk if it matches filter
                if current_file and current_file in files:
                    filtered_chunks.extend(current_chunk)
                
                # Start new chunk
                current_chunk = [line]
                # Extract filename from: diff --git a/path/file.ts b/path/file.ts
                try:
                    current_file = line.split(' b/')[-1]
                except:
                    current_file = None
            else:
                current_chunk.append(line)
        
        # Don't forget last chunk
        if current_file and current_file in files:
            filtered_chunks.extend(current_chunk)
        
        return '\n'.join(filtered_chunks) if filtered_chunks else "No matching files in diff"
        
    def get_latest_pr_for_branch(self, branch: str) -> Optional[Dict[str, Any]]:
        """Get the latest PR for a specific branch."""
        print(f"🔍 Finding latest PR for branch '{branch}'...")
        
        # List PRs for the branch (head branch)
        output, code = self._run_gh_command([
            'pr', 'list', 
            '--head', branch,
            '--json', 'number,title,state,createdAt',
            '--limit', '1'
        ])
        
        if code != 0:
            print(f"ERROR: Failed to list PRs for branch '{branch}': {output}")
            return None
            
        prs = json.loads(output)
        if not prs:
            print(f"No PRs found for branch '{branch}'")
            return None
            
        latest_pr = prs[0]
        print(f"Found PR #{latest_pr['number']}: {latest_pr['title']}")
        
        return self.get_pr_by_number(latest_pr['number'])
        
    def get_latest_open_pr(self) -> Optional[Dict[str, Any]]:
        """Get the most recent open PR."""
        print("🔍 Finding latest open PR...")
        
        output, code = self._run_gh_command([
            'pr', 'list',
            '--state', 'open',
            '--json', 'number,title,createdAt',
            '--limit', '1'
        ])
        
        if code != 0:
            print(f"ERROR: Failed to list open PRs: {output}")
            return None
            
        prs = json.loads(output)
        if not prs:
            print("No open PRs found")
            return None
            
        latest_pr = prs[0]
        print(f"Found latest open PR #{latest_pr['number']}: {latest_pr['title']}")
        
        return self.get_pr_by_number(latest_pr['number'])
        
    def format_pr_analysis(self, pr_data: Dict[str, Any]) -> str:
        """Format PR data for analysis."""
        if not pr_data:
            return "No PR data available"
            
        # Header
        analysis = f"""
=== GitHub PR Analysis Report ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Repository: {self.repo_info['full_name']}

=== PR OVERVIEW ===
Number: #{pr_data['number']}
Title: {pr_data['title']}
State: {pr_data['state']}
Author: {pr_data['author']['login']} ({pr_data['author'].get('name', 'N/A')})
Created: {pr_data['createdAt']}
Updated: {pr_data['updatedAt']}

=== BRANCH INFO ===
Base Branch: {pr_data['baseRefName']} 
Head Branch: {pr_data['headRefName']}
Mergeable: {pr_data.get('mergeable', 'Unknown')}
Merged: {pr_data.get('merged', False)}
"""

        if pr_data.get('mergedAt'):
            analysis += f"Merged At: {pr_data['mergedAt']}\n"
            
        # Statistics
        analysis += f"""
=== CHANGE STATISTICS ===
Changed Files: {pr_data.get('changedFiles', 0)}
Additions: +{pr_data.get('additions', 0)}
Deletions: -{pr_data.get('deletions', 0)}
Commits: {len(pr_data.get('commits', []))}
"""

        # Description
        if pr_data.get('body'):
            analysis += f"""
=== DESCRIPTION ===
{pr_data['body']}
"""

        # Files changed
        if pr_data.get('files'):
            analysis += "\n=== CHANGED FILES ===\n"
            for file_info in pr_data['files']:
                additions = file_info.get('additions', 0)
                deletions = file_info.get('deletions', 0)
                analysis += f"📁 {file_info['path']} (+{additions}/-{deletions})\n"
                
        # Reviews
        if pr_data.get('reviews'):
            analysis += "\n=== REVIEWS ===\n"
            for review in pr_data['reviews']:
                analysis += f"👤 {review['author']['login']}: {review['state']} - {review.get('submittedAt', 'N/A')}\n"
                if review.get('body'):
                    analysis += f"   💬 {review['body'][:100]}...\n"
                    
        # Status checks
        if pr_data.get('statusCheckRollup'):
            analysis += "\n=== STATUS CHECKS ===\n"
            for context in pr_data['statusCheckRollup'].get('contexts', []):
                status = context.get('conclusion') or context.get('state', 'Unknown')
                analysis += f"✅ {context.get('context', 'Unknown')}: {status}\n"
                
        # Diff
        if pr_data.get('diff'):
            analysis += f"""
=== DIFF ===
{pr_data['diff']}
"""

        return analysis

def main():
    parser = argparse.ArgumentParser(description='GitHub PR Analyzer using GitHub CLI')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--pr', type=int, help='PR number to analyze')
    group.add_argument('--branch', help='Branch name to find latest PR for')
    group.add_argument('--latest-open', action='store_true', help='Get latest open PR')
    parser.add_argument('--output-dir', default='.olaf/work/staging/pr-reviews', help='Output directory for analysis files')
    parser.add_argument('--timestamp', help='Optional timestamp to use for output filenames (format: YYYYMMDD-HHMMSS)')
    parser.add_argument('--metadata-only', action='store_true', help='Skip diff fetching, only get PR metadata and file list')
    parser.add_argument('--diff-for-files', nargs='+', help='Get diff only for specified files (space-separated list)')
    parser.add_argument('--files-from', help='Read list of files from specified file (one file path per line)')
    
    args = parser.parse_args()
    
    analyzer = GitHubPRAnalyzer()
    
    print(f"🏛️  Repository: {analyzer.repo_info['full_name']}")
    print(f"🌿 Current Branch: {analyzer.repo_info['current_branch']}")
    print(f"🎯 Default Branch: {analyzer.repo_info['default_branch']}")
    print()
    
    pr_data = None
    skip_diff = args.metadata_only
    files_filter = args.diff_for_files
    
    # If --files-from specified, read file list
    if args.files_from:
        import os
        if os.path.exists(args.files_from) and os.path.getsize(args.files_from) > 0:
            print(f"📂 Reading file list from: {args.files_from}")
            with open(args.files_from, 'r', encoding='utf-8') as f:
                files_filter = [line.strip() for line in f if line.strip()]
            print(f"📝 Loaded {len(files_filter)} files for diff filtering")
        else:
            print(f"⚠️  File list not found or empty: {args.files_from}")
            print(f"⏭️  Skipping diff fetch (no code files to analyze)")
            skip_diff = True
    
    if args.pr:
        pr_data = analyzer.get_pr_by_number(args.pr, skip_diff=skip_diff, files_filter=files_filter)
    elif args.branch:
        pr_data = analyzer.get_latest_pr_for_branch(args.branch)
    elif args.latest_open:
        pr_data = analyzer.get_latest_open_pr()
        
    if pr_data:
        # Save PR info and diff to separate files
        import os
        import glob
        os.makedirs(args.output_dir, exist_ok=True)
        
        pr_num = pr_data['number']
        
        # Clean up any existing files for this PR number
        existing_files = glob.glob(os.path.join(args.output_dir, f'pr-{pr_num}-*'))
        for file_path in existing_files:
            try:
                os.remove(file_path)
                print(f"Removed existing file: {file_path}")
            except OSError as e:
                print(f"Warning: Could not remove {file_path}: {e}")
        
        # Accept externally-provided timestamp to keep filenames coherent with caller
        provided_ts = args.timestamp
        if provided_ts:
            # basic validation: expect YYYYMMDD-HHMM or YYYYMMDD-HHMMSS
            try:
                # try parsing with seconds first
                try:
                    datetime.strptime(provided_ts, '%Y%m%d-%H%M%S')
                    timestamp = provided_ts
                except ValueError:
                    # try without seconds
                    datetime.strptime(provided_ts, '%Y%m%d-%H%M')
                    timestamp = provided_ts
            except ValueError:
                print(f"WARNING: Provided timestamp '{provided_ts}' is not in expected format YYYYMMDD-HHMM or YYYYMMDD-HHMMSS. Falling back to current time.")
                timestamp = datetime.now().strftime('%Y%m%d-%H%M')
        else:
            timestamp = datetime.now().strftime('%Y%m%d-%H%M')
        
        # Save PR metadata (without diff)
        pr_info = pr_data.copy()
        diff_content = pr_info.pop('diff', '')
        
        info_file = os.path.join(args.output_dir, f'pr-{pr_num}-info-{timestamp}.json')
        with open(info_file, 'w', encoding='utf-8') as f:
            json.dump(pr_info, f, indent=2, ensure_ascii=False)
        
        # Save diff separately
        diff_file = os.path.join(args.output_dir, f'pr-{pr_num}-diff-{timestamp}.txt')
        with open(diff_file, 'w', encoding='utf-8') as f:
            f.write(diff_content)
        
        # If metadata-only mode, create code files list
        if args.metadata_only:
            code_extensions = {
                '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.go', '.rs',
                '.cpp', '.c', '.h', '.hpp', '.cs', '.rb', '.php', '.swift',
                '.kt', '.scala', '.sh', '.bash', '.ps1'
            }
            
            code_files = []
            if pr_info.get('files'):
                for file_info in pr_info['files']:
                    file_path = file_info.get('path', '')
                    # Check if file has code extension
                    if any(file_path.endswith(ext) for ext in code_extensions):
                        code_files.append(file_path)
            
            # Save code files list (empty if no code files)
            code_files_file = os.path.join(args.output_dir, f'pr-{pr_num}-code-files-{timestamp}.txt')
            with open(code_files_file, 'w', encoding='utf-8') as f:
                if code_files:
                    f.write('\n'.join(code_files))
                # else: leave empty file
            
            if code_files:
                print(f"📝 Code Files List: {code_files_file} ({len(code_files)} files)")
            else:
                print(f"📝 Code Files List: {code_files_file} (empty - no code files)")
        
        # Output only file locations
        print(f"\n✅ PR Analysis Complete for PR #{pr_num}")
        print(f"📄 PR Info: {info_file}")
        print(f"📄 Diff: {diff_file}")
    else:
        print("❌ No PR data found")
        sys.exit(1)

if __name__ == '__main__':
    main()