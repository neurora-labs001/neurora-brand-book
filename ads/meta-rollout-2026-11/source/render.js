// Render every *_45.html / *_916.html in this folder to PNG (1080x1350 / 1080x1920).
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const dir = __dirname; const only = process.argv[2];
  const files = fs.readdirSync(dir).filter(f => /_(45|916)\.html$/.test(f) && (!only || f.includes(only))).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  for (const f of files) {
    const h = f.endsWith('_45.html') ? 1350 : 1920;
    await page.setViewportSize({ width: 1080, height: h });
    await page.goto('file://' + path.join(dir, f));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const overflow = await page.evaluate(() => { const w = document.querySelector('.wrap'); return w ? w.scrollHeight - w.clientHeight : 0; });
    await page.screenshot({ path: path.join(dir, 'out', f.replace('.html', '.png')) });
    console.log(f, overflow > 2 ? `OVERFLOW ${overflow}px` : 'ok');
  }
  await browser.close();
})();
