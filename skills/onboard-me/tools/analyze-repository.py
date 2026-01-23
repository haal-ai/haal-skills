#!/usr/bin/env python3
"""
Repository Analyzer - Extract Facts for AI Onboarding Guide Generation

Outputs a single JSON file with repository facts that AI uses to generate
persona-focused onboarding guides dynamically.

Design: Python extracts data → AI generates guides
"""

import os
import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional
from collections import defaultdict

class RepositoryAnalyzer:
    """Extract repository facts without generating guides"""
    
    LANGUAGE_EXTENSIONS = {
        'Go': ['.go'],
        'Python': ['.py', '.pyx', '.pyi'],
        'Java': ['.java'],
        'Scala': ['.scala', '.sc'],
        'Kotlin': ['.kt', '.kts'],
        'JavaScript': ['.js', '.mjs', '.cjs'],
        'TypeScript': ['.ts', '.tsx'],
        'C#': ['.cs'],
        'C++': ['.cpp', '.cc', '.cxx', '.hpp'],
        'Rust': ['.rs'],
        'Ruby': ['.rb'],
        'Shell': ['.sh', '.bash', '.zsh', '.ps1'],
    }
    
    EXCLUDE_DIRS = {
        '.git', 'node_modules', 'vendor', '__pycache__', 'venv', '.venv',
        'dist', 'build', 'target', 'bin', 'obj', '.next', '.cache',
        'coverage', 'tmp', 'logs', '.idea', 'site', '_site'
    }
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.repo_name = self.repo_path.name
        self.files_by_language: Dict[str, List[Path]] = defaultdict(list)
        
    def analyze(self) -> Dict:
        """Extract all facts needed for AI guide generation"""
        print("[*] Analyzing repository...")
        print(f"    Path   : {self.repo_path}")
        print("    Phase 1/5: Scanning files and languages...")

        self._scan_files()

        print("    Phase 2/5: Computing language statistics...")
        languages = self._get_language_stats()

        print("    Phase 3/5: Detecting frameworks and build tools...")
        frameworks = self._detect_frameworks()
        build_tools = self._detect_build_tools()

        print("    Phase 4/5: Extracting commands and entry points...")
        commands = self._extract_commands()
        entry_points = self._find_entry_points()

        print("    Phase 5/5: Detecting key files and architecture hints...")
        key_files = self._identify_key_files()
        architecture = self._detect_architecture_hints()

        return {
            'metadata': {
                'repo_name': self.repo_name,
                'repo_path': str(self.repo_path),
                'total_files': sum(len(files) for files in self.files_by_language.values()),
                'analyzed_at': str(Path.cwd())
            },
            'languages': languages,
            'frameworks': frameworks,
            'build_tools': build_tools,
            'project_type': self._infer_project_type(),
            'commands': commands,
            'entry_points': entry_points,
            'key_files': key_files,
            'architecture': architecture
        }
    
    def _scan_files(self):
        """Scan all files and categorize by language"""
        for root, dirs, files in os.walk(self.repo_path):
            dirs[:] = [
                d for d in dirs 
                if d not in self.EXCLUDE_DIRS and (
                    not d.startswith('.') or d in ['.olaf', '.github']
                )
            ]
            
            for file in files:
                file_path = Path(root) / file
                rel_path = file_path.relative_to(self.repo_path)
                
                ext = file_path.suffix.lower()
                for lang, extensions in self.LANGUAGE_EXTENSIONS.items():
                    if ext in extensions:
                        self.files_by_language[lang].append(rel_path)
                        break
    
    def _count_loc(self, files: List[Path]) -> int:
        """Count lines of code"""
        total = 0
        for file_path in files:
            try:
                full_path = self.repo_path / file_path
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    total += sum(1 for line in f if line.strip())
            except:
                pass
        return total
    
    def _get_language_stats(self) -> List[Dict]:
        """Get statistics for each language"""
        total_loc = sum(self._count_loc(files) for files in self.files_by_language.values())
        
        results = []
        for lang, files in sorted(self.files_by_language.items(), key=lambda x: len(x[1]), reverse=True):
            if not files:
                continue
            
            loc = self._count_loc(files)
            version = self._detect_version(lang)
            
            results.append({
                'name': lang,
                'files': len(files),
                'loc': loc,
                'percentage': round(loc / max(total_loc, 1) * 100, 1),
                'version': version
            })
        
        return results
    
    def _detect_version(self, lang: str) -> Optional[str]:
        """Detect language version"""
        if lang == 'Go':
            for go_mod in self.repo_path.rglob('go.mod'):
                try:
                    content = go_mod.read_text(encoding='utf-8')
                    match = re.search(r'go (\d+\.\d+)', content)
                    if match:
                        return match.group(1)
                except:
                    pass
        
        elif lang == 'TypeScript':
            for pkg_json in self.repo_path.rglob('package.json'):
                try:
                    data = json.loads(pkg_json.read_text(encoding='utf-8'))
                    deps = {**data.get('devDependencies', {}), **data.get('dependencies', {})}
                    if 'typescript' in deps:
                        return deps['typescript'].strip('^~')
                except:
                    pass
        
        elif lang == 'Python':
            for file in ['.python-version', 'runtime.txt']:
                path = self.repo_path / file
                if path.exists():
                    try:
                        return path.read_text().strip().replace('python-', '')
                    except:
                        pass
        
        elif lang == 'Java':
            pom = self.repo_path / 'pom.xml'
            if pom.exists():
                try:
                    content = pom.read_text(encoding='utf-8')
                    match = re.search(r'<java\.version>(\d+)</java\.version>', content)
                    if match:
                        return match.group(1)
                except:
                    pass
        
        return None
    
    def _detect_frameworks(self) -> List[str]:
        """Detect frameworks and libraries"""
        frameworks = set()
        
        # Node.js/TypeScript frameworks
        for pkg_json in self.repo_path.rglob('package.json'):
            try:
                data = json.loads(pkg_json.read_text(encoding='utf-8'))
                deps = {**data.get('devDependencies', {}), **data.get('dependencies', {})}
                
                if 'react' in deps:
                    frameworks.add('React')
                if 'vue' in deps:
                    frameworks.add('Vue')
                if 'angular' in deps or '@angular/core' in deps:
                    frameworks.add('Angular')
                if 'next' in deps:
                    frameworks.add('Next.js')
                if 'express' in deps:
                    frameworks.add('Express')
                if 'fastify' in deps:
                    frameworks.add('Fastify')
                if 'vite' in deps:
                    frameworks.add('Vite')
                if 'webpack' in deps:
                    frameworks.add('Webpack')
                if 'mocha' in deps:
                    frameworks.add('Mocha')
                if 'jest' in deps:
                    frameworks.add('Jest')
                if 'vscode' in data.get('engines', {}):
                    frameworks.add('VS Code Extension')
            except:
                pass
        
        # Python frameworks
        for req_file in ['requirements.txt', 'pyproject.toml', 'setup.py']:
            path = self.repo_path / req_file
            if path.exists():
                try:
                    content = path.read_text(encoding='utf-8').lower()
                    if 'django' in content:
                        frameworks.add('Django')
                    if 'flask' in content:
                        frameworks.add('Flask')
                    if 'fastapi' in content:
                        frameworks.add('FastAPI')
                    if 'pytest' in content:
                        frameworks.add('pytest')
                    if 'boto3' in content:
                        frameworks.add('AWS SDK (boto3)')
                except:
                    pass
        
        # Go frameworks
        for go_mod in self.repo_path.rglob('go.mod'):
            try:
                content = go_mod.read_text(encoding='utf-8')
                if 'gin-gonic' in content:
                    frameworks.add('Gin')
                if 'fiber' in content:
                    frameworks.add('Fiber')
                if 'bubbletea' in content:
                    frameworks.add('Bubble Tea (TUI)')
            except:
                pass
        
        # Scala frameworks
        for build_sbt in self.repo_path.rglob('build.sbt'):
            try:
                content = build_sbt.read_text(encoding='utf-8').lower()
                if 'spark' in content:
                    frameworks.add('Apache Spark')
                if 'akka' in content:
                    frameworks.add('Akka')
                if 'play' in content:
                    frameworks.add('Play Framework')
                if 'scalatra' in content:
                    frameworks.add('Scalatra')
            except:
                pass
        
        return sorted(list(frameworks))
    
    def _detect_build_tools(self) -> List[str]:
        """Detect build tools"""
        tools = set()
        
        if (self.repo_path / 'package.json').exists():
            tools.add('npm')
        if (self.repo_path / 'go.mod').exists():
            tools.add('go modules')
        if (self.repo_path / 'pom.xml').exists():
            tools.add('Maven')
        if (self.repo_path / 'build.gradle').exists() or (self.repo_path / 'build.gradle.kts').exists():
            tools.add('Gradle')
        if (self.repo_path / 'build.sbt').exists():
            tools.add('SBT')
        if (self.repo_path / 'Cargo.toml').exists():
            tools.add('Cargo')
        if (self.repo_path / 'Makefile').exists():
            tools.add('Make')
        if (self.repo_path / 'Dockerfile').exists():
            tools.add('Docker')
        if list(self.repo_path.glob('*.csproj')):
            tools.add('dotnet')
        
        return sorted(list(tools))
    
    def _infer_project_type(self) -> str:
        """Infer project type from structure"""
        frameworks = self._detect_frameworks()
        
        if 'VS Code Extension' in frameworks:
            return 'vscode-extension'
        if 'Next.js' in frameworks:
            return 'web-app'
        if 'React' in frameworks or 'Vue' in frameworks:
            return 'frontend-app'
        if 'FastAPI' in frameworks or 'Django' in frameworks or 'Express' in frameworks:
            return 'backend-api'
        if 'Bubble Tea (TUI)' in frameworks:
            return 'cli-tool'
        if (self.repo_path / 'setup.py').exists() or (self.repo_path / 'pyproject.toml').exists():
            return 'library'
        if (self.repo_path / 'Dockerfile').exists() and 'kubernetes' in str(self.repo_path).lower():
            return 'microservices'
        
        return 'monorepo' if len(self._get_language_stats()) > 3 else 'application'
    
    def _extract_commands(self) -> Dict[str, List[str]]:
        """Extract common commands from config files"""
        commands = {
            'install': [],
            'build': [],
            'test': [],
            'run': [],
            'lint': []
        }
        
        # From package.json (search all subdirectories)
        for pkg_json in self.repo_path.rglob('package.json'):
            try:
                data = json.loads(pkg_json.read_text(encoding='utf-8'))
                scripts = data.get('scripts', {})
                
                # Only add from the first package.json found (usually root or main component)
                if not commands['install']:
                    commands['install'].append('npm install')
                
                if 'build' in scripts and 'npm run build' not in commands['build']:
                    commands['build'].append('npm run build')
                if 'compile' in scripts and 'npm run compile' not in commands['build']:
                    commands['build'].append('npm run compile')
                if 'test' in scripts and 'npm test' not in commands['test']:
                    commands['test'].append('npm test')
                if 'test:unit' in scripts and 'npm run test:unit' not in commands['test']:
                    commands['test'].append('npm run test:unit')
                if 'start' in scripts and 'npm start' not in commands['run']:
                    commands['run'].append('npm start')
                if 'dev' in scripts and 'npm run dev' not in commands['run']:
                    commands['run'].append('npm run dev')
                if 'lint' in scripts and 'npm run lint' not in commands['lint']:
                    commands['lint'].append('npm run lint')
                
                # Break after first package.json to avoid duplicates
                break
            except:
                pass
        
        # From Makefile
        makefile = self.repo_path / 'Makefile'
        if makefile.exists():
            try:
                content = makefile.read_text(encoding='utf-8')
                for target in ['build', 'test', 'run', 'install']:
                    if re.search(rf'^{target}:', content, re.MULTILINE):
                        commands[target].append(f'make {target}')
            except:
                pass
        
        # Python
        if (self.repo_path / 'requirements.txt').exists():
            commands['install'].append('pip install -r requirements.txt')
        if (self.repo_path / 'setup.py').exists():
            commands['install'].append('pip install -e .')
        
        # Go
        if (self.repo_path / 'go.mod').exists():
            commands['install'].append('go mod download')
            commands['build'].append('go build ./...')
            commands['test'].append('go test ./...')
        
        # Docker
        if (self.repo_path / 'Dockerfile').exists():
            commands['build'].append('docker build -t app .')
            commands['run'].append('docker run -p 8080:8080 app')
        
        return {k: v for k, v in commands.items() if v}
    
    def _find_entry_points(self) -> Dict[str, List[str]]:
        """Find entry point files"""
        entry_points = defaultdict(list)
        
        # Common entry points
        common_entries = [
            ('main.py', 'Python'),
            ('app.py', 'Python'),
            ('__main__.py', 'Python'),
            ('main.go', 'Go'),
            ('index.js', 'JavaScript'),
            ('index.ts', 'TypeScript'),
            ('App.tsx', 'TypeScript'),
            ('extension.ts', 'TypeScript'),
            ('server.js', 'JavaScript'),
            ('Application.java', 'Java'),
            ('Main.java', 'Java'),
        ]
        
        for entry_file, lang in common_entries:
            for match in self.repo_path.rglob(entry_file):
                rel_path = match.relative_to(self.repo_path)
                entry_points[lang].append(str(rel_path))
        
        return dict(entry_points)
    
    def _identify_key_files(self) -> Dict[str, str]:
        """Identify key documentation and config files"""
        key_files = {}
        
        important_files = [
            'README.md', 'CONTRIBUTING.md', 'ARCHITECTURE.md', 'DESIGN.md',
            'package.json', 'go.mod', 'pom.xml', 'requirements.txt',
            'Dockerfile', 'docker-compose.yml', '.github/workflows'
        ]
        
        for file_name in important_files:
            path = self.repo_path / file_name
            if path.exists():
                key_files[file_name] = str(path.relative_to(self.repo_path))
        
        return key_files
    
    def _detect_architecture_hints(self) -> Dict:
        """Detect architecture patterns and structure"""
        hints = {
            'has_api_layer': False,
            'has_service_layer': False,
            'has_tests': False,
            'is_monorepo': False,
            'main_directories': []
        }
        
        # Check for common architecture patterns
        for root, dirs, _ in os.walk(self.repo_path):
            rel_root = Path(root).relative_to(self.repo_path)
            
            if rel_root == Path('.'):
                hints['main_directories'] = [d for d in dirs if not d.startswith('.')]
            
            dir_name = Path(root).name.lower()
            if dir_name in ['api', 'routes', 'controllers']:
                hints['has_api_layer'] = True
            if dir_name in ['services', 'service', 'business']:
                hints['has_service_layer'] = True
            if dir_name in ['test', 'tests', '__tests__']:
                hints['has_tests'] = True
        
        # Monorepo detection
        hints['is_monorepo'] = len(self._get_language_stats()) > 3
        
        return hints


def main():
    parser = argparse.ArgumentParser(description='Analyze repository for onboarding guide generation')
    parser.add_argument('repo_path', help='Path to repository')
    parser.add_argument('--output', default='.', help='Output directory for JSON')
    
    args = parser.parse_args()
    
    analyzer = RepositoryAnalyzer(args.repo_path)
    data = analyzer.analyze()
    
    # Write JSON
    output_path = Path(args.output) / 'repository-analysis.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n[OK] Analysis complete: {output_path}")
    print(f"     Languages: {', '.join(l['name'] for l in data['languages'][:5])}")
    print(f"     Project type: {data['project_type']}")
    print(f"     Frameworks: {', '.join(data['frameworks'][:5])}")


if __name__ == '__main__':
    main()
