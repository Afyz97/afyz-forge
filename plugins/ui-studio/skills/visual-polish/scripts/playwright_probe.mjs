#!/usr/bin/env node
// Usage: node playwright_probe.mjs <url-or-file> [selector=body] [out=ten-fixes] [--mobile]
// Writes <out>.png (screenshot of the selector) and <out>.json (dom_probe result).
// Needs: npm i -D playwright && npx playwright install chromium
import { chromium, devices } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const [, , target, selector = 'body', out = 'ten-fixes', ...flags] = process.argv;
if (!target) { console.error('usage: node playwright_probe.mjs <url-or-file> [selector] [out] [--mobile]'); process.exit(2); }
const url = /^https?:|^file:/.test(target) ? target : pathToFileURL(path.resolve(target)).href;
const here = path.dirname(fileURLToPath(import.meta.url));

const browser = await chromium.launch();
const ctx = await browser.newContext(flags.includes('--mobile') ? devices['iPhone 13'] : { viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();
await page.emulateMedia({ reducedMotion: 'reduce' });
await page.goto(url, { waitUntil: 'networkidle' });
await page.addScriptTag({ path: path.join(here, 'dom_probe.js') });
const result = await page.evaluate((sel) => tenFixesProbe(sel), selector);
const el = await page.$(selector);
await (el ?? page).screenshot({ path: `${out}.png` });
fs.writeFileSync(`${out}.json`, JSON.stringify(result, null, 2));
console.log(JSON.stringify(result, null, 2));
await browser.close();
