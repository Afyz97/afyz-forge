#!/usr/bin/env python3
"""Read-only codebase inventory and heuristic leads; stdlib only, no project writes."""
from __future__ import annotations

import argparse
import collections
import json
import re
import subprocess
import sys
from pathlib import Path

CODE_EXTS = {
    '.py', '.php', '.js', '.jsx', '.mjs', '.cjs', '.ts', '.tsx', '.vue',
    '.go', '.rs', '.java', '.kt', '.kts', '.cs', '.rb', '.swift', '.dart',
    '.scala', '.sql', '.sh', '.bash', '.ps1', '.blade.php'
}
SKIP_DIRS = {
    '.git', 'node_modules', 'vendor', 'dist', 'build', 'coverage', '.next',
    '.nuxt', '.venv', 'venv', '__pycache__', '.pytest_cache', '.mypy_cache',
    '.cache', 'target', 'out', 'storage', '.idea', '.vscode'
}
PATTERNS = [
    ('delay-or-sleep', re.compile(r'\b(?:time\.sleep|Thread\.sleep|usleep|sleep\s*\(|setTimeout\s*\()', re.I)),
    ('retry-or-backoff', re.compile(r'\b(?:retry|backoff|max_retries|retryCount)\b', re.I)),
    ('disabled-test', re.compile(r'\b(?:pytest\.mark\.skip|test\.skip|describe\.skip|it\.skip|markTestSkipped|@Disabled|xit\s*\(|xdescribe\s*\()', re.I)),
    ('ignored-exception', re.compile(r'\b(?:except\s*\w*\s*:\s*pass\b|catch\s*\([^)]*\)\s*\{\s*\}|rescue\s*=>?\s*\w*\s*;?\s*end)')),
    ('global-state', re.compile(r'^\s*(?:global\s+\w+|(?:window|globalThis)\.\w+\s*=)', re.I)),
    ('conditional-special-case', re.compile(r'\b(?:if|else\s+if|elif)\b[^\n]{0,100}(?:===?|!==?|===)\s*[\'\"](?:[\w-]+)[\'\"]')),
]


def is_code_file(path: Path) -> bool:
    name = path.name.lower()
    return name.endswith('.blade.php') or path.suffix.lower() in CODE_EXTS


def paths(root: Path):
    try:
        result = subprocess.run(['git', '-C', str(root), 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True)
        candidates = [Path(raw.decode('utf-8', 'surrogateescape'))
                      for raw in result.stdout.split(b'\0') if raw]
    except (FileNotFoundError, subprocess.CalledProcessError):
        candidates = [p.relative_to(root) for p in root.rglob('*') if p.is_file()]
    for rel in candidates:
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if is_code_file(rel) and (root / rel).is_file() and not (root / rel).is_symlink():
            yield rel


def analyze(root: Path, top: int, max_signals: int, max_files: int):
    extension_counts = collections.Counter()
    dir_counts = collections.Counter()
    large = []
    signals = []
    signal_counts = collections.Counter()
    scanned = 0
    skipped_large = 0
    limits_hit = False

    for rel in paths(root):
        if scanned >= max_files:
            limits_hit = True
            break
        full = root / rel
        try:
            size = full.stat().st_size
            if size > 1_000_000:
                skipped_large += 1
                continue
            content = full.read_text(encoding='utf-8', errors='replace')
        except (OSError, UnicodeError):
            continue
        scanned += 1
        ext = '.blade.php' if rel.name.lower().endswith('.blade.php') else rel.suffix.lower()
        extension_counts[ext] += 1
        dir_counts[rel.parts[0] if len(rel.parts) > 1 else '(root)'] += 1
        count = len(content.splitlines())
        large.append((count, rel.as_posix()))
        # Signals are observations only; never automatically change code based on them.
        for no, line in enumerate(content.splitlines(), start=1):
            for label, regex in PATTERNS:
                if regex.search(line):
                    signal_counts[label] += 1
                    if len(signals) < max_signals:
                        signals.append({'kind': label, 'location': f'{rel.as_posix()}:{no}'})
    large.sort(reverse=True)
    return {
        'root': str(root),
        'files_scanned': scanned,
        'skipped_large_files': skipped_large,
        'max_files_reached': limits_hit,
        'languages_by_extension': dict(extension_counts.most_common()),
        'top_level_directories': dict(dir_counts.most_common(top)),
        'largest_files_by_lines': [{'lines': n, 'path': path} for n, path in large[:top]],
        'signal_totals': dict(signal_counts.most_common()),
        'signal_examples': signals[:max_signals],
        'disclaimer': 'Heuristic leads only; dynamic dispatch, dependency injection and runtime usage are not inferred. Inspect source before refactoring.'
    }


def render(report: dict) -> str:
    out = [f'# Read-only repository map: {report["root"]}',
           f'Files scanned: {report["files_scanned"]} (oversized skipped: {report["skipped_large_files"]}; file limit reached: {report["max_files_reached"]})',
           '', '## File types']
    out.extend(f'- `{k}`: {v}' for k, v in report['languages_by_extension'].items())
    out += ['', '## Top-level directories']
    out.extend(f'- `{k}`: {v}' for k, v in report['top_level_directories'].items())
    out += ['', '## Largest files (not automatically defects)']
    out.extend(f'- `{d["path"]}`: {d["lines"]} lines' for d in report['largest_files_by_lines'])
    out += ['', '## Heuristic leads - inspect before concluding']
    out.extend(f'- {k}: {v}' for k, v in report['signal_totals'].items())
    out += ['', '## Signal examples']
    out.extend(f'- `{d["location"]}`: {d["kind"]}' for d in report['signal_examples'])
    out += ['', f'**Caution:** {report["disclaimer"]}']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='.', help='repository directory')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown')
    parser.add_argument('--top', type=int, default=20)
    parser.add_argument('--max-signals', type=int, default=35)
    parser.add_argument('--max-files', type=int, default=10000)
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f'No such directory: {root}')
    report = analyze(root, max(1, args.top), max(0, args.max_signals), max(1, args.max_files))
    print(json.dumps(report, indent=2) if args.format == 'json' else render(report))


if __name__ == '__main__':
    main()
