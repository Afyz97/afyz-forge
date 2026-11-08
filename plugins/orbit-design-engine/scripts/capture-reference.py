#!/usr/bin/env python3
"""Opt-in screenshot helper for public reference UIs (requires: pip install playwright; playwright install chromium).

This does not bypass authentication or download proprietary source. Uses an interactive page to permit
manual navigation, then captures current view (dashboard and other views if user navigates).
"""
from __future__ import annotations
import argparse
from pathlib import Path

DEFAULT_URL = 'https://demo.codeandchill.store/kinlo/#/dashboard'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default=DEFAULT_URL)
    parser.add_argument('--output', default='.ai/uiux/orbit/reference/screenshots')
    parser.add_argument('--name', default='dashboard')
    parser.add_argument('--headed', action='store_true', help='Display browser for manual inspection before screenshot.')
    parser.add_argument('--pause', action='store_true', help='Press Enter to capture, useful for menus/modals.')
    args = parser.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit('Install Playwright first: pip install playwright && playwright install chromium') from exc
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    viewports = [('desktop', 1440, 900), ('laptop', 1024, 768), ('phone', 390, 844)]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not args.headed)
        for label, width, height in viewports:
            context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1)
            page = context.new_page()
            try:
                page.goto(args.url, wait_until='domcontentloaded', timeout=30000)
                page.wait_for_timeout(2000)  # allow SPA hydration; adjust after inspecting
                if args.pause:
                    input(f'Inspect {label} {width}x{height}, interact if necessary, press Enter to capture: ')
                target = out / f'{args.name}-{label}.png'
                page.screenshot(path=str(target), full_page=True, animations='disabled')
                print(f'Saved {target} ({page.url})')
            except Exception as exc:
                print(f'Failed {label}: {exc}')
            finally:
                context.close()
        browser.close()

if __name__ == '__main__':
    main()
