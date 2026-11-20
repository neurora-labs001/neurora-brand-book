// Render a looping MP4 for each ad: steps the paused CSS animation frame by frame.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { execSync } = require('child_process');
(async () => {
  const dir = __dirname; const only = process.argv[2]; const fps = 30, secs = parseFloat(process.argv[3] || '7');
  const files = fs.readdirSync(dir).filter(f => /_(45|916)\.html$/.test(f) && f.includes(only)).sort();
  const browser = await chromium.launch(); const page = await browser.newPage({ deviceScaleFactor: 1 });
  fs.mkdirSync(path.join(dir, 'video'), { recursive: true });
  for (const f of files) {
    const h = f.endsWith('_45.html') ? 1350 : 1920; await page.setViewportSize({ width: 1080, height: h });
    await page.goto('file://' + path.join(dir, f)); await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => document.body.classList.add('anim')); await page.waitForTimeout(50);
    const tmp = fs.mkdtempSync(path.join(dir, 'frames-'));
    for (let i = 0; i < fps * secs; i++) {
      await page.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), (i / fps) * 1000);
      await page.screenshot({ path: path.join(tmp, String(i).padStart(4, '0') + '.png') });
    }
    const out = path.join(dir, 'video', f.replace('.html', '.mp4'));
    execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i ${tmp}/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart ${out}`);
    fs.rmSync(tmp, { recursive: true }); console.log(out);
  }
  await browser.close();
})();
