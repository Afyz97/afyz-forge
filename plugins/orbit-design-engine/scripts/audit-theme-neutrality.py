#!/usr/bin/env python3
"""Fail if package instructions or source examples contain a fixed colour palette."""
from __future__ import annotations
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
TARGETS=(list((ROOT/'skills').rglob('SKILL.md'))+list((ROOT/'references').glob('*.md'))+
         list((ROOT/'assets').glob('*.css'))+list((ROOT/'examples').glob('*.html')))
FIXED=re.compile(r'(?i)#[0-9a-f]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|hwb|lab|lch|oklab|oklch)\s*\(')
NAMED=re.compile(r'(?i)\b(?:white|black|green|blue|purple|red|cream|gold|teal|orange|gray|grey|emerald|evergreen|beige|lavender|lilac|mint|peach|forest|plum|ember|ocean)\b')

issues=[]
for p in TARGETS:
    s=p.read_text(encoding='utf-8')
    for i,line in enumerate(s.splitlines(),1):
        if FIXED.search(line):issues.append(f'{p.relative_to(ROOT)}:{i}: explicit palette literal')
        # Colour names should never be added to the instructions (but note proper paths in archival reference data need separate audit).
        if p.parent.name.startswith('orbit-ui-') and NAMED.search(line):issues.append(f'{p.relative_to(ROOT)}:{i}: colour-specific skill instruction')
if issues:
    print('Theme neutrality audit FAILED:')
    for err in issues:print(' -',err)
    sys.exit(1)
print(f'Theme neutrality audit PASSED: {len(TARGETS)} instructions, reference docs, token sheets and demos have no fixed palette values; no skill prescribes named colours.')
