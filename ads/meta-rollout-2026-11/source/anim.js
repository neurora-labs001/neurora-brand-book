// Render looping MP4s. Ads with built-in motion (Signal draw / comet) use it; all others get the generic motion system.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { execSync } = require('child_process');
const GENERIC_CSS = `
@keyframes g-up{from{opacity:0;translate:0 28px}to{opacity:1;translate:0 0}}
@keyframes g-pop{from{opacity:0;scale:.86}to{opacity:1;scale:1}}
@keyframes g-draw{to{stroke-dashoffset:0}}
@keyframes g-kb{from{object-view-box:inset(0% 0% 0% 0%)}to{object-view-box:inset(5% 4% 3% 4%)}}
@keyframes g-pulse{0%,100%{scale:1}45%{scale:1.06}}
@keyframes g-dot{0%,100%{scale:1}50%{scale:1.4}}
@keyframes g-bounce{0%,100%{translate:0 0;rotate:0deg}25%{translate:0 -16px;rotate:-10deg}50%{translate:0 0;rotate:8deg}70%{translate:0 -6px;rotate:-3deg}}`;
function generic() {
  const st = document.createElement('style'); st.textContent = window.__GCSS; document.head.appendChild(st);
  const set = (el, anim) => { el.style.animation = el.style.animation ? el.style.animation + ',' + anim : anim; };
  const wrap = document.querySelector('.wrap');
  let items = [];
  for (const c of wrap.children) { if (c.classList.contains('grow')) items.push(...c.children); else items.push(c); }
  const delayOf = new Map(); const done = new Set();
  items.forEach((el, i) => { const d = 0.05 + i * 0.24; delayOf.set(el, d); set(el, `g-up 1.1s cubic-bezier(.2,.7,.2,1) ${d}s backwards`); done.add(el); });
  const baseDelay = el => { let n = el; while (n && !delayOf.has(n)) n = n.parentElement; return n ? delayOf.get(n) : 0.3; };
  // staggered groups: flex/grid containers with >=3 similar children
  for (const e of wrap.querySelectorAll('*')) {
    const cs = getComputedStyle(e); if (!/flex|grid/.test(cs.display)) continue;
    const kids = [...e.children].filter(k => k.getBoundingClientRect().height > 40 && !done.has(k));
    if (kids.length < 3) continue;
    const tag = kids[0].tagName; if (kids.filter(k => k.tagName === tag).length < 3) continue;
    const b = baseDelay(e) + 0.7;
    kids.forEach((k, j) => { set(k, `g-pop 1s cubic-bezier(.2,.8,.3,1.15) ${b + j * 0.3}s backwards`); done.add(k); });
  }
  // stroked SVG paths draw in
  for (const p of wrap.querySelectorAll('svg path')) {
    const s = getComputedStyle(p); if (s.stroke === 'none' || s.fill !== 'none' || (s.strokeDasharray && s.strokeDasharray !== 'none')) continue;
    if (p.getTotalLength() < 40) continue;
    p.setAttribute('pathLength', '1'); p.style.strokeDasharray = '1'; p.style.strokeDashoffset = '1';
    set(p, `g-draw 2.8s cubic-bezier(.45,0,.2,1) ${baseDelay(p) + 0.5}s forwards`);
  }
  // Ken Burns on photos
  for (const im of wrap.querySelectorAll('img')) {
    const s = getComputedStyle(im); const r = im.getBoundingClientRect();
    if (s.objectFit === 'cover' && r.width > 250 && r.height > 150) set(im, 'g-kb 11s linear both');
  }
  // living details
  document.querySelectorAll('.dot, .dots i').forEach((d, i) => set(d, `g-dot 3.6s ease-in-out ${2 + (i % 4) * 0.45}s infinite`));
  document.querySelectorAll('.btn').forEach(b => { b.style.transformOrigin = 'center'; set(b, 'g-pulse 1.6s ease-in-out 6.2s 1'); set(b, 'g-pulse 1.6s ease-in-out 9.2s 1'); });
  document.querySelectorAll('.emo, .qbadge .q').forEach(e => { e.style.display = 'inline-block'; set(e, 'g-bounce 2.8s ease-in-out 2s infinite'); });
  document.querySelectorAll('body > svg path').forEach(p => { p.setAttribute('pathLength', '1'); p.style.strokeDasharray = '1'; p.style.strokeDashoffset = '1'; set(p, 'g-draw 3s cubic-bezier(.45,0,.2,1) 1.4s forwards'); });
}
(async () => {
  const dir = __dirname; const only = process.argv[2] || ''; const secs = parseFloat(process.argv[3] || '11'); const fps = 30;
  const shots = process.argv[4] ? process.argv[4].split(',').map(Number) : null;   // preview mode: list of seconds
  const files = fs.readdirSync(dir).filter(f => /_(45|916)\.html$/.test(f) && f.includes(only)).sort();
  const browser = await chromium.launch(); const page = await browser.newPage({ deviceScaleFactor: 1 });
  fs.mkdirSync(path.join(dir, 'video'), { recursive: true });
  for (const f of files) {
    const h = f.endsWith('_45.html') ? 1350 : 1920; await page.setViewportSize({ width: 1080, height: h });
    await page.goto('file://' + path.join(dir, f)); await page.evaluate(() => document.fonts.ready);
    const builtIn = await page.evaluate(() => !!document.querySelector('.sig-b, .comet, .builtin'));
    await page.evaluate(() => window.__measure && window.__measure());
    if (!builtIn) await page.evaluate(css => { window.__GCSS = css; }, GENERIC_CSS);
    await page.evaluate(gen => { document.body.classList.add('anim'); if (gen) generic(); document.getAnimations().forEach(a => a.pause()); }, !builtIn);
    const step = async t => page.evaluate(t => { document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }); document.body.offsetHeight; return new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); }, t * 1000);
    if (shots) {
      for (const t of shots) { await step(t); await page.screenshot({ path: path.join(dir, 'out', `_pv_${f.replace('.html', '')}_${t}.jpg`), type: 'jpeg', quality: 80 }); }
      console.log('preview', f, builtIn ? 'built-in' : 'generic'); continue;
    }
    const tmp = fs.mkdtempSync(path.join(dir, 'frames-'));
    for (let i = 0; i < fps * secs; i++) { await step(i / fps); await page.screenshot({ path: path.join(tmp, String(i).padStart(4, '0') + '.jpg'), type: 'jpeg', quality: 93 }); }
    const out = path.join(dir, 'video', f.replace('.html', '.mp4'));
    execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i ${tmp}/%04d.jpg -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart ${out}`);
    fs.rmSync(tmp, { recursive: true }); console.log(out);
  }
  await browser.close();
})();
