/*
 * Ten Fixes DOM probe — measures the RENDERED page (computed styles + boxes).
 * Covers what static lint can't: real left edges (02), real contrast on real
 * backgrounds (06), rendered icon sizes (07), surfaces (08).
 *
 * Run it:
 *   - DevTools console: paste, then `tenFixesProbe('.weather-card')`
 *   - Playwright: await page.addScriptTag({ path }); await page.evaluate(() => tenFixesProbe('main'))
 *   - Or: node playwright_probe.mjs URL SELECTOR (see SKILL.md)
 * Returns a JSON-able object; print with JSON.stringify(result, null, 2).
 */
function tenFixesProbe(rootSelector = 'body', opts = {}) {
  const root = document.querySelector(rootSelector);
  if (!root) return { error: `No element for ${rootSelector}` };
  const tol = opts.edgeTolerance ?? 2;

  const parseRGB = (s) => {
    const m = s && s.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1];
  };
  const lum = ([r, g, b]) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const over = (top, bottom) => [0, 1, 2].map((i) => top[i] * top[3] + bottom[i] * (1 - top[3])).concat(1);
  const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };

  // Effective background: composite ancestors' background-colors; note gradients/images.
  const bgOf = (el) => {
    const layers = []; let gradient = false;
    for (let n = el; n; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') gradient = true;
      const c = parseRGB(cs.backgroundColor);
      if (c && c[3] > 0) { layers.push(c); if (c[3] === 1) break; }
    }
    let acc = [255, 255, 255, 1];
    for (let i = layers.length - 1; i >= 0; i--) acc = over(layers[i], acc);
    return { color: acc, gradient };
  };

  // Left edge of the rendered glyphs (not the block box, which spans the full width).
  const textLeft = (el) => { const n = [...el.childNodes].find((c) => c.nodeType === 3 && c.textContent.trim());
    const r = document.createRange(); r.selectNodeContents(n); return Math.round(r.getBoundingClientRect().left); };
  const isTextEl = (el) => [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
  const visible = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity > 0; };

  const all = [root, ...root.querySelectorAll('*')].filter(visible);
  const textEls = all.filter(isTextEl);
  const icons = all.filter((el) => el.tagName.toLowerCase() === 'svg' ||
    (el.tagName === 'IMG' && el.getBoundingClientRect().width <= 64) ||
    (el.tagName === 'I' && /icon|fa-|bi-|ri-|material/.test(el.className)));

  const fontSizes = {}, weights = {}, families = {}, hues = {}, decor = { uppercase: 0, italic: 0, underline: 0, tracking: 0 };
  const lowContrast = []; const spacing = {};
  for (const el of textEls) {
    const cs = getComputedStyle(el);
    const fs = Math.round(parseFloat(cs.fontSize));
    fontSizes[fs] = (fontSizes[fs] || 0) + 1;
    weights[cs.fontWeight] = (weights[cs.fontWeight] || 0) + 1;
    families[cs.fontFamily.split(',')[0].trim()] = 1;
    if (cs.textTransform === 'uppercase') decor.uppercase++;
    if (cs.fontStyle === 'italic') decor.italic++;
    if (cs.textDecorationLine.includes('underline') && el.tagName !== 'A') decor.underline++;
    if (parseFloat(cs.letterSpacing) / fs >= 0.05) decor.tracking++;
    const fg = parseRGB(cs.color); const opacity = +cs.opacity;
    const { color: bg, gradient } = bgOf(el);
    const eff = over([...fg.slice(0, 3), fg[3] * opacity], bg);
    const r = ratio(eff, bg);
    const large = fs >= 24 || (fs >= 18.66 && +cs.fontWeight >= 700);
    if (r < (large ? 3 : 4.5)) lowContrast.push({ text: el.textContent.trim().slice(0, 30), ratio: +r.toFixed(2), color: cs.color, bg: `rgb(${bg.slice(0, 3).map(Math.round)})`, gradientBehind: gradient });
    const [R, G, B] = fg; const mx = Math.max(R, G, B), mn = Math.min(R, G, B);
    const sat = mx === 0 ? 0 : (mx - mn) / mx;
    if (sat > 0.2 && mx > 40) {
      let h = 0; const d = mx - mn;
      if (d) h = mx === R ? ((G - B) / d) % 6 : mx === G ? (B - R) / d + 2 : (R - G) / d + 4;
      const bucket = Math.round(((h * 60 + 360) % 360) / 30) * 30;
      hues[bucket] = (hues[bucket] || 0) + 1;
    }
  }
  for (const el of all) {
    const cs = getComputedStyle(el);
    for (const p of ['marginTop', 'marginBottom', 'paddingTop', 'paddingLeft', 'rowGap', 'columnGap']) {
      const v = Math.round(parseFloat(cs[p]));
      if (v > 0) spacing[v] = (spacing[v] || 0) + 1;
    }
  }

  // Tabular containers (rows of columns) legitimately have several edges (Rule 02 exception).
  const isTabular = (el) => { const cs = getComputedStyle(el);
    if (cs.display.includes('grid')) return cs.gridTemplateColumns.trim().split(/\s+/).length > 1;
    if (cs.display.includes('flex')) return cs.flexDirection.startsWith('row') && el.children.length >= 3;
    return false; };

  // Left edge of a row: a surface (card) aligns by its box; anything else by its first glyph.
  const hasSurface = (el) => { const cs = getComputedStyle(el); const bg = parseRGB(cs.backgroundColor);
    return (bg && bg[3] > 0) || cs.backgroundImage !== 'none' || parseFloat(cs.borderLeftWidth) > 0; };
  const firstGlyphLeft = (el) => { const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT,
      { acceptNode: (n) => n.textContent.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP });
    const n = w.nextNode(); if (!n) return null; const r = document.createRange(); r.selectNodeContents(n);
    return Math.round(r.getBoundingClientRect().left); };
  const rowLeft = (el) => hasSurface(el) ? Math.round(el.getBoundingClientRect().left) : firstGlyphLeft(el);

  // Stacks = non-tabular containers with >= 3 visible child rows; count distinct row edges.
  const centred = (el) => { const cs = getComputedStyle(el);
    return cs.textAlign === 'center' || cs.justifyItems === 'center' || (cs.display.includes('flex') && cs.alignItems === 'center' && cs.flexDirection.startsWith('column')); };
  const containers = all.filter((el) => !isTabular(el) && !centred(el) && [...el.children].filter(visible).length >= 3)
    .map((el) => {
      const edges = [];
      for (const kid of [...el.children].filter(visible)) {
        const x = rowLeft(kid); if (x == null) continue;
        if (!edges.some((e) => Math.abs(e - x) <= tol)) edges.push(x);
      }
      return { el: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : ''),
               rows: el.children.length, leftEdges: edges.sort((x, y) => x - y) };
    })
    .sort((x, y) => y.leftEdges.length - x.leftEdges.length).slice(0, 12);
  const stackEdges = containers.map((c) => c.leftEdges.length);

  const iconSizes = {};
  for (const i of icons) { const r = i.getBoundingClientRect(); const k = `${Math.round(r.width)}x${Math.round(r.height)}`; iconSizes[k] = (iconSizes[k] || 0) + 1; }
  const sizes = Object.keys(fontSizes).map(Number).sort((a, b) => a - b);
  const body = +Object.entries(fontSizes).sort((a, b) => b[1] - a[1])[0]?.[0];
  const hero = sizes[sizes.length - 1];
  const surfaces = all.filter((el) => { const cs = getComputedStyle(el); const bg = parseRGB(cs.backgroundColor);
    const r = el.getBoundingClientRect();
    return r.height >= 24 && bg && bg[3] > 0 && ((bg[3] < 1) || parseFloat(cs.borderRadius) >= 8); }).length;

  return {
    root: rootSelector,
    r01_hierarchy: { hero, body, ratio: +(hero / body).toFixed(2), distinctSizes: sizes },
    r02_alignment: { maxEdgesInAStack: stackEdges.length ? Math.max(...stackEdges) : 0, containers },
    r03_spacing: { distinctValues: Object.keys(spacing).map(Number).sort((a, b) => a - b), offGrid: Object.keys(spacing).map(Number).filter((v) => v % 4 && v > 2) },
    r04_textStyle: { decorations: decor, families: Object.keys(families), weights: Object.keys(weights) },
    r05_colour: { textHueBuckets: hues, hueCount: Object.keys(hues).length },
    r06_contrast: { failing: lowContrast.sort((a, b) => a.ratio - b.ratio).slice(0, 20) },
    r07_icons: { count: icons.length, renderedSizes: iconSizes },
    r08_grouping: { surfaces },
    note: 'Rules 09 and 10 need human/visual judgement; use a screenshot.',
  };
}
if (typeof module !== 'undefined') module.exports = { tenFixesProbe };
