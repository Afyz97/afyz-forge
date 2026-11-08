#!/usr/bin/env python3
"""Orbit Design Engine v8 installer for Claude Code and Codex.

Standard-library only. Updates the package's owned files and marked instructions.
Optional --migrate-kinlo cleans only SHA-verified, unmodified v4 skill folders.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
START = '<!-- ORBIT-DESIGN-AUTO-APPLY:START -->'
END = '<!-- ORBIT-DESIGN-AUTO-APPLY:END -->'
LEGACY_START = '<!-- KINLO-UIUX-AUTO-APPLY:START -->'
LEGACY_END = '<!-- KINLO-UIUX-AUTO-APPLY:END -->'


def copy_owned(src: Path, dst: Path, upgrade: bool, output: list[str]) -> None:
    if not src.exists(): raise FileNotFoundError(src)
    if dst.exists() and not upgrade:
        output.append(f'SKIPPED existing (use --upgrade): {dst}')
        return
    if dst.exists():
        # Do not delete custom files: update only those supplied by the package.
        for file in src.rglob('*'):
            if file.is_file():
                out = dst / file.relative_to(src)
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, out)
    else:
        shutil.copytree(src, dst)
    output.append(f'INSTALLED: {dst}')


def _remove_marked(text: str, start: str, end: str) -> str:
    if start not in text or end not in text: return text
    i=text.find(start)
    j=text.find(end,i)
    if j<0:return text
    j += len(end)
    # Keep unrelated instructions before and after, trim only surrounding padding.
    return text[:i].rstrip() + ('\n\n' if text[:i].strip() and text[j:].strip() else '') + text[j:].lstrip('\n')


def apply_rule(path: Path, rule: str, out: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    initial=path.read_text(encoding='utf8') if path.exists() else ''
    clean=_remove_marked(initial,START,END)
    clean=_remove_marked(clean,LEGACY_START,LEGACY_END)
    block=f'{START}\n{rule}\n{END}'
    updated=clean.rstrip() + ('\n\n' if clean.strip() else '') + block + '\n'
    if updated!=initial:
        path.write_text(updated,encoding='utf8')
        out.append(f'UPDATED agent instructions: {path}')
    else:out.append(f'UNCHANGED agent instructions: {path}')


def migrate_pristine_legacy(base: Path, target: str, out: list[str]) -> None:
    fingerprints=json.loads((SOURCE/'legacy'/'v4-pristine-skill-checksums.json').read_text(encoding='utf8'))
    parents=[]
    if target in ('both','claude'): parents.append(base/'.claude'/'skills')
    if target in ('both','codex'): parents.append(base/'.agents'/'skills')
    for parent in parents:
        for old_name,expected in fingerprints.items():
            old=parent/old_name
            if not old.exists():continue
            file=old/'SKILL.md'
            if (old.is_dir() and file.is_file() and
                sorted(p.relative_to(old).as_posix() for p in old.rglob('*') if p.is_file())==['SKILL.md'] and
                hashlib.sha256(file.read_bytes()).hexdigest()==expected):
                shutil.rmtree(old)
                out.append(f'RETIRED untouched legacy skill: {old}')
            else:
                out.append(f'KEPT modified legacy skill (manual review): {old}')
    legacy_ref=base/'.ai'/'uiux'/'kinlo'
    if legacy_ref.exists():out.append(f'KEPT legacy reference archive (manual removal if desired): {legacy_ref}')
    old_nested=base/'.claude'/'skills'/'kinlo-design-system'
    if old_nested.exists():out.append(f'KEPT older nested legacy skills (manual review): {old_nested}')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project',default='.',help='Project root (for --scope project).')
    parser.add_argument('--scope',choices=['project','user'],default='project')
    parser.add_argument('--target',choices=['both','claude','codex'],default='both')
    parser.add_argument('--upgrade',action='store_true',help='Refresh package-owned files.')
    parser.add_argument('--no-rules',action='store_true',help='Only install skills/resources.')
    parser.add_argument('--migrate-kinlo',action='store_true',help='Retire SHA-verified, unmodified v4 legacy skill folders; preserve modified files.')
    args=parser.parse_args()
    base=Path(args.project).expanduser().resolve() if args.scope=='project' else Path.home()
    base.mkdir(parents=True,exist_ok=True)
    shared=base/'.ai'/'uiux'/'orbit'
    out=[]
    for folder in ('references','assets','examples','scripts'):
        destination=shared if folder=='references' else shared/folder
        copy_owned(SOURCE/folder,destination,args.upgrade,out)
    if args.target in ('both','claude'):
        for skill in sorted((SOURCE/'skills').iterdir()):
            if skill.is_dir():copy_owned(skill,base/'.claude'/'skills'/skill.name,args.upgrade,out)
    if args.target in ('both','codex'):
        for skill in sorted((SOURCE/'skills').iterdir()):
            if skill.is_dir():copy_owned(skill,base/'.agents'/'skills'/skill.name,args.upgrade,out)
    if not args.no_rules:
        docs='~/.ai/uiux/orbit/AUTO-APPLY.md' if args.scope=='user' else '.ai/uiux/orbit/AUTO-APPLY.md'
        rule=(f'For every visible UI/frontend change, read `{docs}` before implementing. '
              'Use the Orbit Design Engine modular skills (`orbit-ui-director` for broad UI work, '
              '`orbit-ui-motion` and component-specific skills for behaviour (including `orbit-ui-workspace-navigation` and `orbit-ui-metric-choreography` for workspaces, and `orbit-ui-auth-forms` plus `orbit-ui-diagonal-wipe` for animated login/registration), and `orbit-ui-visual-qa`/`orbit-ui-motion-qa` for verification). '
              "ALWAYS preserve the host system's configured colours and every organization/user theme variant; never define or copy a palette or hardcode colour values. "
              'Inspect actual project theme tokens first and read THEME-INHERITANCE.md; motion and reference geometry must use the existing theme. '
              'Choose the operational app-motion or cinematic storytelling route appropriate to the task. '
              'Follow project knowledge in `.ai/agents/` and preserve business logic, performance and accessibility. '
              'Do not load UI skills for backend-only tasks. Agent routing instructions do not guarantee automatic invocation.')
        if args.target in ('both','claude'):
            apply_rule(base/'.claude'/'CLAUDE.md' if args.scope=='user' else base/'CLAUDE.md',rule,out)
        if args.target in ('both','codex'):
            apply_rule(base/'.codex'/'AGENTS.md' if args.scope=='user' else base/'AGENTS.md',rule,out)
    if args.migrate_kinlo:
        migrate_pristine_legacy(base,args.target,out)
    elif (base/'.ai'/'uiux'/'kinlo').exists():
        out.append('OLD plugin detected: add --migrate-kinlo to retire verified unmodified v4 skills; reference archive will remain intact.')
    print('\n'.join(out))
    print('\nOrbit Design Engine installed. Restart/reload your agents if needed; check skills are discoverable.')

if __name__=='__main__': main()
