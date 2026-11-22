// Meta readiness scan: text sizes, safe zones (9:16), hook + CTA prominence.
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const dir = __dirname;
  const files = fs.readdirSync(dir).filter(f => /_(45|916)\.html$/.test(f)).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const report = [];
  for (const f of files) {
    const story = f.endsWith('_916.html');
    await page.setViewportSize({ width: 1080, height: story ? 1920 : 1350 });
    await page.goto('file://' + path.join(dir, f));
    await page.evaluate(() => document.fonts.ready);
    const r = await page.evaluate((story) => {
      const out = { small: [], unsafe: [], h1: 0, cta: null };
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      const seen = new Set();
      while (walker.nextNode()) {
        const n = walker.currentNode; const t = n.textContent.trim(); if (!t) continue;
        const el = n.parentElement; if (seen.has(el)) continue; seen.add(el);
        if (el.closest('svg')) continue;
        const cs = getComputedStyle(el); const fs = parseFloat(cs.fontSize);
        const range = document.createRange(); range.selectNodeContents(n); const b = range.getBoundingClientRect();
        if (b.width === 0) continue;
        if (fs < 18) out.small.push(`${fs}px "${t.slice(0, 40)}"`);
        if (story) {
          const bad = b.top < 1920 * 0.14 || b.bottom > 1920 * 0.80 || b.left < 1080 * 0.06 - 2 || b.right > 1080 * 0.94 + 2;
          if (bad) out.unsafe.push(`y${Math.round(b.top)}-${Math.round(b.bottom)} x${Math.round(b.left)}-${Math.round(b.right)} "${t.slice(0, 34)}"`);
        }
      }
      const h1 = document.querySelector('h1'); if (h1) out.h1 = parseFloat(getComputedStyle(h1).fontSize);
      const cta = document.querySelector('.btn, .chip');
      if (cta) { const b = cta.getBoundingClientRect(); out.cta = `${cta.className} ${Math.round(b.width)}x${Math.round(b.height)} @y${Math.round(b.top)}`; }
      return out;
    }, story);
    report.push({ f, ...r });
  }
  await browser.close();
  for (const r of report) {
    console.log(`\n${r.f}  h1=${r.h1}px  cta=${r.cta || 'NONE'}`);
    if (r.small.length) console.log('  small<18px:', r.small.length, '|', r.small.slice(0, 6).join(' | '));
    if (r.unsafe.length) console.log('  UNSAFE:', r.unsafe.length, '|', r.unsafe.slice(0, 5).join(' | '));
  }
})();
