#!/usr/bin/env python3
"""Read-only Git co-change signals from history (not proof of architectural coupling)."""
from __future__ import annotations

import argparse
import collections
import subprocess
from pathlib import Path

CODE_EXTS = {'.php', '.js', '.jsx', '.ts', '.tsx', '.py', '.go', '.java', '.rs', '.cs', '.rb', '.vue', '.sql', '.kt', '.swift', '.dart'}
SKIP = ('vendor/', 'node_modules/', 'dist/', 'build/', 'coverage/', 'storage/', 'generated/', '.ai/')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='.')
    parser.add_argument('--commits', type=int, default=200)
    parser.add_argument('--min-count', type=int, default=3)
    parser.add_argument('--top', type=int, default=30)
    parser.add_argument('--max-files-per-commit', type=int, default=40)
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    cmd = ['git', '-C', str(root), '-c', 'core.quotePath=false', 'log', '--no-merges',
           '--name-only', '--no-renames', f'-n{max(1,args.commits)}', '--format=__CODEWEAVE_COMMIT__%H %P']
    try:
        data = subprocess.run(cmd, capture_output=True, text=True, check=True, encoding='utf-8', errors='replace').stdout
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        parser.error(f'Cannot inspect Git history for {root}: {e}')
    changes = []
    current = None
    ignored_root = 0
    for line in data.splitlines():
        line = line.strip()
        if line.startswith('__CODEWEAVE_COMMIT__'):
            if current is not None:
                changes.append(current)
            parts = line.removeprefix('__CODEWEAVE_COMMIT__').split()
            # Root commits commonly add every file at once: not co-change evidence.
            if len(parts) < 2:
                current = None
                ignored_root += 1
            else:
                current = set()
        elif line and current is not None:
            if not line.startswith(SKIP) and Path(line).suffix.lower() in CODE_EXTS:
                current.add(line)
    if current is not None:
        changes.append(current)

    pair_counts = collections.Counter()
    file_counts = collections.Counter()
    used = 0
    skipped = 0
    for paths in changes:
        if not paths or len(paths) > max(2, args.max_files_per_commit):
            skipped += 1
            continue
        used += 1
        names = sorted(paths)
        file_counts.update(names)
        for i, left in enumerate(names):
            for right in names[i + 1:]:
                pair_counts[(left, right)] += 1
    rows = []
    for (left, right), co in pair_counts.items():
        if co < max(1, args.min_count):
            continue
        # Relative support helps rank pairs; cross-feature release commits still create noise.
        support = co / max(file_counts[left], file_counts[right])
        rows.append((co, support, left, right))
    rows.sort(reverse=True)
    print(f'# Git co-change leads: {root}')
    print(f'Commits read: {len(changes) + ignored_root}; sampled: {used}; excluded root: {ignored_root}; excluded empty/mass: {skipped}')
    print('Pairs are **investigation leads** only. Corroborate with actual ownership, imports, and domain requirements.\n')
    print('| Co-changes | Support | File A | File B |')
    print('| ---: | ---: | --- | --- |')
    for co, support, left, right in rows[:max(1, args.top)]:
        # No backslash inside the f-string expression: that is a SyntaxError before Python 3.12.
        left, right = left.replace('|', '\\|'), right.replace('|', '\\|')
        print(f'| {co} | {support:.0%} | `{left}` | `{right}` |')
    if not rows:
        print('| - | - | No pairs met the threshold | - |')


if __name__ == '__main__':
    main()
