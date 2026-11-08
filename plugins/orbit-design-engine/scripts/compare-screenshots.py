#!/usr/bin/env python3
"""Create side-by-side evidence image from two actual captures (requires Pillow).

Does not assign a fabricated similarity score. Review composition and details manually.
"""
from __future__ import annotations
import argparse
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('reference')
    p.add_argument('implementation')
    p.add_argument('--output', default='orbit-ui-visual-comparison.png')
    args = p.parse_args()
    try:
        from PIL import Image, ImageOps, ImageDraw
    except ImportError as exc:
        raise SystemExit('Install Pillow first: pip install pillow') from exc
    first = Image.open(args.reference).convert('RGB')
    second = Image.open(args.implementation).convert('RGB')
    width = max(first.width, second.width)
    first = ImageOps.pad(first, (width, max(first.height, second.height)), color='#e9edf2', centering=(0.5,0))
    second = ImageOps.pad(second, (width, max(first.height, second.height)), color='#e9edf2', centering=(0.5,0))
    gap = 20
    canvas = Image.new('RGB', (width*2 + gap*3, first.height + 60), '#ecf0f4')
    canvas.paste(first, (gap,45))
    canvas.paste(second, (width+gap*2,45))
    d = ImageDraw.Draw(canvas)
    d.text((gap,17), 'Reference (observed)', fill='#182536')
    d.text((width+gap*2,17), 'Implementation (observed)', fill='#182536')
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(path)
    print(f'Side-by-side comparison: {path}')

if __name__ == '__main__':
    main()
