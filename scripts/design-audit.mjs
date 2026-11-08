#!/usr/bin/env node
// design-audit.mjs — deterministic design smell auditor for the Ultimate Design Skills Suite.
//
// Scope & philosophy:
//   Taste cannot be linted. This tool ONLY flags mechanically-detectable smells and always
//   reports them as SIGNALS to investigate, never as verdicts. Every rule documents what it
//   detects, why, its false-positive risk, a severity, and a remediation. A human (or the
//   design-review skill) must confirm each finding in context — many flagged patterns are
//   legitimate when deliberately chosen.
//
// Usage:
//   node scripts/design-audit.mjs [path ...]     # defaults to current directory
//   node scripts/design-audit.mjs --json src/    # machine-readable output
//
// No dependencies. Node 16+. Scans .css/.scss/.html/.jsx/.tsx/.vue/.svelte/.astro files.

import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const asJson = args.includes('--json');
const targets = args.filter(a => !a.startsWith('--'));
const roots = targets.length ? targets : ['.'];

const EXT = new Set(['.css', '.scss', '.sass', '.less', '.html', '.htm', '.jsx', '.tsx', '.vue', '.svelte', '.astro']);
const IGNORE = new Set(['node_modules', '.git', 'dist', 'build', '.next', 'out', 'vendor', 'coverage', '.svelte-kit']);

// Each rule: id, description(what), why, falsePositive, severity, remediation, scan(content)->[{line, evidence}]
const RULES = [
  {
    id: 'shadow-stack',
    what: 'Elements with 3+ box-shadow layers (shadow soup / neumorphism/clay overuse).',
    why: 'Stacked soft shadows accumulate into muddy depth, hurt performance, and flatten hierarchy.',
    falsePositive: 'Neumorphism/claymorphism legitimately use paired/triple shadows on a FEW focal elements.',
    severity: 'medium',
    remediation: 'Cap the count; reserve multi-shadow depth for focal elements; animate transform, not box-shadow.',
    scan: (c) => matchDecl(c, /box-shadow\s*:\s*([^;{}]+)[;}]/gi, (m) => {
      const layers = splitTopLevel(m[1]).length;
      return layers >= 3 ? `box-shadow has ${layers} layers` : null;
    }),
  },
  {
    id: 'backdrop-filter-density',
    what: 'Many backdrop-filter uses in one file (glass-on-everything).',
    why: 'backdrop-filter is one of the most expensive CSS effects; overuse causes jank and contrast chaos.',
    falsePositive: 'A design may legitimately use glass on a couple of floating layers.',
    severity: 'medium',
    remediation: 'Limit glass to the floating control layer; ensure solid + reduced-transparency fallbacks.',
    scan: (c) => {
      const hits = [...c.matchAll(/backdrop-filter\s*:/gi)];
      if (hits.length >= 4) return [{ line: lineOf(c, hits[0].index), evidence: `${hits.length} backdrop-filter declarations in file` }];
      return [];
    },
  },
  {
    id: 'backdrop-filter-fallback-missing',
    what: 'backdrop-filter used with no @supports / prefers-reduced-transparency fallback in the file.',
    why: 'Without a fallback, unsupported browsers and Reduce Transparency users get unreadable or broken surfaces.',
    falsePositive: 'Fallback may live in a shared stylesheet not scanned here.',
    severity: 'high',
    remediation: 'Add @supports not (backdrop-filter: blur(1px)) and prefers-reduced-transparency solid fallbacks.',
    scan: (c) => {
      if (!/backdrop-filter\s*:/i.test(c)) return [];
      const hasSupports = /@supports[^{]*backdrop-filter/i.test(c);
      const hasReduced = /prefers-reduced-transparency/i.test(c);
      if (hasSupports || hasReduced) return [];
      const idx = c.search(/backdrop-filter\s*:/i);
      return [{ line: lineOf(c, idx), evidence: 'backdrop-filter present; no @supports or prefers-reduced-transparency fallback found in file' }];
    },
  },
  {
    id: 'reduced-motion-missing',
    what: 'File defines animations/transitions but no prefers-reduced-motion handling.',
    why: 'Motion without a reduced-motion path can trigger discomfort and fails WCAG 2.3.3 expectations.',
    falsePositive: 'Global reduced-motion reset may live in a base stylesheet not scanned here.',
    severity: 'medium',
    remediation: 'Add a @media (prefers-reduced-motion: reduce) block that reduces travel while preserving feedback.',
    scan: (c) => {
      const hasMotion = /@keyframes|animation\s*:|animation-name\s*:|transition\s*:\s*[^;]*\d/i.test(c);
      const hasRM = /prefers-reduced-motion/i.test(c);
      if (hasMotion && !hasRM) return [{ line: 1, evidence: 'animations/transitions present; no prefers-reduced-motion block in file' }];
      return [];
    },
  },
  {
    id: 'focus-removed',
    what: 'outline:none / outline:0 without an accompanying :focus-visible style nearby.',
    why: 'Removing focus outlines without replacement destroys keyboard accessibility (WCAG 2.4.7).',
    falsePositive: 'A replacement focus style may be defined elsewhere; only flags when none is found in file.',
    severity: 'high',
    remediation: 'Provide a visible :focus-visible indicator (>=2px, >=3:1 contrast) wherever you remove the default.',
    scan: (c) => {
      const hits = [...c.matchAll(/outline\s*:\s*(none|0)\b/gi)];
      if (!hits.length) return [];
      const hasFocusVisible = /:focus-visible|focus-visible:/i.test(c);
      if (hasFocusVisible) return [];
      return hits.slice(0, 3).map(h => ({ line: lineOf(c, h.index), evidence: 'outline removed with no :focus-visible replacement in file' }));
    },
  },
  {
    id: 'radius-repetition',
    what: 'A single border-radius value repeated heavily (everything equally rounded).',
    why: 'Uniform rounding on everything is a common template tell and can flatten hierarchy.',
    falsePositive: 'A tokenized radius reused via a variable is GOOD; this only flags repeated literal px values.',
    severity: 'low',
    remediation: 'Use a small radius scale via tokens; vary radius by element role; avoid one literal value everywhere.',
    scan: (c) => {
      const counts = {};
      for (const m of c.matchAll(/border-radius\s*:\s*(\d{1,3})px/gi)) {
        const v = m[1]; (counts[v] ??= []).push(m.index);
      }
      const out = [];
      for (const [v, idxs] of Object.entries(counts)) {
        if (idxs.length >= 8) out.push({ line: lineOf(c, idxs[0]), evidence: `border-radius: ${v}px appears ${idxs.length} times (literal, not tokenized)` });
      }
      return out;
    },
  },
  {
    id: 'important-spiral',
    what: 'Many !important declarations (specificity escape hatch overused).',
    why: 'A pile of !important signals a broken cascade and unmaintainable overrides.',
    falsePositive: 'A few !important in utility/reset layers can be legitimate.',
    severity: 'medium',
    remediation: 'Fix specificity/token layering instead; reserve !important for genuine utility overrides.',
    scan: (c) => {
      const hits = [...c.matchAll(/!important/gi)];
      if (hits.length >= 8) return [{ line: lineOf(c, hits[0].index), evidence: `${hits.length} !important declarations in file` }];
      return [];
    },
  },
  {
    id: 'zindex-escalation',
    what: 'Very large or arbitrary z-index values (9999+, 99999).',
    why: 'Arbitrary z-index escalation is a symptom of an unmanaged stacking system.',
    falsePositive: 'Some libraries legitimately use high z-index; confirm against a defined scale.',
    severity: 'low',
    remediation: 'Define a z-index scale as tokens (e.g. dropdown/sticky/modal/toast) and reference it.',
    scan: (c) => matchAllLines(c, /z-index\s*:\s*(\d{4,})/gi, (m) => Number(m[1]) >= 9999 ? `z-index: ${m[1]}` : null),
  },
  {
    id: 'purple-blue-gradient',
    what: 'The stereotypical purple→blue diagonal gradient (AI-default hero gradient).',
    why: 'This specific gradient is a strong "generic AI output" tell when used without brand reason.',
    falsePositive: 'Perfectly fine if these hues are the actual brand colors and the gradient is intentional.',
    severity: 'low',
    remediation: 'Tie gradient hues to real brand colors; reserve a hero gradient for one intentional moment.',
    scan: (c) => matchAllLines(c, /linear-gradient\([^)]*(#[678][0-9a-f]{5}|#[678][0-9a-f]{2}(?![0-9a-f])|\b(?:violet|purple|indigo)\b)/gi, () => 'possible purple/violet gradient — verify it is brand-driven'),
  },
  {
    id: 'gradient-text',
    what: 'Gradient text via background-clip:text.',
    why: 'Gradient headings often reduce contrast/legibility and read as templated.',
    falsePositive: 'One deliberate accent heading with verified contrast can be fine.',
    severity: 'low',
    remediation: 'Prefer solid high-contrast type; if used, verify contrast and limit to one accent.',
    scan: (c) => matchAllLines(c, /-webkit-background-clip\s*:\s*text|background-clip\s*:\s*text/gi, () => 'background-clip:text (gradient text) — verify contrast & intent'),
  },
  {
    id: 'tiny-tap-target',
    what: 'Explicit width/height below 24px on things that look interactive.',
    why: 'Targets under 24×24 CSS px fail WCAG 2.5.8; under ~44px are hard on touch.',
    falsePositive: 'Not everything with a small size is a target (icons inside larger hit areas, decorative elements).',
    severity: 'medium',
    remediation: 'Ensure interactive targets are >=24px (prefer >=44px touch), padding the hit area if the glyph is small.',
    scan: (c) => matchAllLines(c, /(?:min-)?(?:width|height)\s*:\s*(\d{1,2})px/gi, (m) => Number(m[1]) > 0 && Number(m[1]) < 24 ? `dimension ${m[1]}px (<24px) — confirm it is not an interactive target` : null),
  },
];

// ---------- helpers ----------
function splitTopLevel(s) {
  // split a shorthand value list on top-level commas (ignore commas inside parens)
  const parts = []; let depth = 0, cur = '';
  for (const ch of s) {
    if (ch === '(') depth++; if (ch === ')') depth--;
    if (ch === ',' && depth === 0) { parts.push(cur); cur = ''; } else cur += ch;
  }
  if (cur.trim()) parts.push(cur);
  return parts.map(p => p.trim()).filter(Boolean);
}
function lineOf(content, index) { return content.slice(0, index).split('\n').length; }
function matchDecl(content, re, fn) {
  const out = [];
  for (const m of content.matchAll(re)) {
    const ev = fn(m); if (ev) out.push({ line: lineOf(content, m.index), evidence: ev });
  }
  return out;
}
function matchAllLines(content, re, fn) {
  const out = [];
  for (const m of content.matchAll(re)) {
    const ev = fn(m); if (ev) out.push({ line: lineOf(content, m.index), evidence: ev });
  }
  return out;
}
function walk(dir, acc) {
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return acc; }
  for (const e of entries) {
    if (e.name.startsWith('.') && e.name !== '.') { if (IGNORE.has(e.name)) continue; }
    if (IGNORE.has(e.name)) continue;
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walk(full, acc);
    else if (EXT.has(path.extname(e.name).toLowerCase())) acc.push(full);
  }
  return acc;
}

// ---------- run ----------
const files = [];
for (const r of roots) {
  try {
    const st = fs.statSync(r);
    if (st.isDirectory()) walk(r, files);
    else if (EXT.has(path.extname(r).toLowerCase())) files.push(r);
  } catch { /* ignore missing */ }
}

const findings = [];
for (const file of files) {
  let content;
  try { content = fs.readFileSync(file, 'utf8'); } catch { continue; }
  for (const rule of RULES) {
    for (const hit of rule.scan(content)) {
      findings.push({ rule: rule.id, severity: rule.severity, file, line: hit.line, evidence: hit.evidence, remediation: rule.remediation });
    }
  }
}

const order = { high: 0, medium: 1, low: 2 };
findings.sort((a, b) => order[a.severity] - order[b.severity] || a.file.localeCompare(b.file) || a.line - b.line);

if (asJson) {
  console.log(JSON.stringify({ filesScanned: files.length, findingCount: findings.length, findings }, null, 2));
} else {
  console.log(`\nDesign audit — ${files.length} file(s) scanned, ${findings.length} signal(s).`);
  console.log('These are SIGNALS to investigate, not verdicts. Confirm each in context.\n');
  const byRule = {};
  for (const f of findings) (byRule[f.rule] ??= []).push(f);
  for (const rule of RULES) {
    const fs2 = byRule[rule.id]; if (!fs2 || !fs2.length) continue;
    console.log(`[${rule.severity.toUpperCase()}] ${rule.id} — ${rule.what}`);
    console.log(`   why: ${rule.why}`);
    console.log(`   false-positive risk: ${rule.falsePositive}`);
    console.log(`   fix: ${rule.remediation}`);
    for (const f of fs2.slice(0, 20)) console.log(`   • ${f.file}:${f.line} — ${f.evidence}`);
    if (fs2.length > 20) console.log(`   … and ${fs2.length - 20} more`);
    console.log('');
  }
  if (!findings.length) console.log('No mechanical smells detected. (Taste still requires human/design-review judgment.)\n');
}
process.exit(0);
