#!/usr/bin/env python3
"""Round 2: cleaner Neurora Meta ads. One message per ad, Meta safe zones, colourful frosted board."""
import os
from gen import S, A, svg_logo, signal_bridge, signal_inline, o_mark, dial_svg

ROOT = os.path.dirname(os.path.abspath(__file__))

CSS = """
@font-face{font-family:Manrope;src:url(fonts/Manrope-VariableFont_wght.ttf) format('truetype');font-weight:200 800}
@font-face{font-family:'EB Garamond';font-style:italic;src:url(fonts/EBGaramond-Italic.woff2) format('woff2')}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:var(--H);overflow:hidden}
body{font-family:Manrope,sans-serif;color:#0D1B33;background:#F1EEE8;-webkit-font-smoothing:antialiased;position:relative}
/* colourful mood field: all four glows, the ad's state glow strongest */
body::before{content:"";position:absolute;inset:0;z-index:0;background:
 radial-gradient(560px 520px at 100% 0%, color-mix(in srgb,var(--g) 55%,transparent),transparent 72%),
 radial-gradient(520px 480px at 0% 100%, rgba(246,174,142,.32),transparent 72%),
 radial-gradient(520px 480px at 100% 100%, rgba(163,204,240,.30),transparent 72%),
 radial-gradient(480px 440px at 0% 30%, rgba(138,211,189,.22),transparent 72%)}
.wrap{position:relative;z-index:1;height:100%;display:flex;flex-direction:column;padding:var(--pad)}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:34px}
.dots{display:inline-flex;gap:9px;align-items:center}
.dots i{width:13px;height:13px;border-radius:50%;display:block}
.slogan{font-size:22px;font-weight:300;letter-spacing:-.01em;color:rgba(13,27,51,.7)}
.slogan b{font-family:'EB Garamond';font-style:italic;font-weight:400;color:var(--c);font-size:26px}
.eyebrow{font-size:20px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--c)}
.eyebrow.grey{color:rgba(13,27,51,.55)}
h1{font-weight:300;letter-spacing:-.045em;line-height:1.02;font-size:88px}
h1 .acc{color:var(--c);display:block}
.lead{font-size:26px;line-height:1.45;color:rgba(13,27,51,.7)}
.board{background:linear-gradient(150deg,rgba(255,255,255,.82),rgba(255,255,255,.58));border:1px solid rgba(255,255,255,.95);border-radius:32px;
 box-shadow:0 30px 60px -40px rgba(13,27,51,.35),0 2px 6px -4px rgba(13,27,51,.1);backdrop-filter:blur(16px);position:relative;overflow:hidden}
.board.glow::before{content:"";position:absolute;inset:0;z-index:0;background:
 radial-gradient(380px 300px at 92% 6%, color-mix(in srgb,var(--g) 50%,transparent),transparent 70%),
 radial-gradient(360px 300px at 4% 100%, rgba(246,174,142,.28),transparent 70%),
 radial-gradient(320px 260px at 60% 110%, rgba(163,204,240,.28),transparent 70%)}
.board > *{position:relative;z-index:1}
.dot{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--c);box-shadow:0 0 0 5px color-mix(in srgb,var(--g) 45%,transparent),0 0 16px 3px color-mix(in srgb,var(--g) 80%,transparent);vertical-align:middle}
.lbl{font-size:18px;font-weight:600;letter-spacing:.18em;text-transform:uppercase}
.it{font-family:'EB Garamond';font-style:italic;font-weight:400}
.chip{display:flex;align-items:center;gap:20px;background:#fff;border-radius:24px;padding:14px 26px 14px 14px;box-shadow:0 14px 34px -24px rgba(13,27,51,.4)}
.chip img{width:88px;height:88px;object-fit:cover;border-radius:16px}
.chip .t{font-size:26px;font-weight:600;letter-spacing:-.01em}
.chip .s{font-size:19px;color:rgba(13,27,51,.55);margin-top:4px}
.chip .arr{margin-left:auto;font-size:36px;color:var(--c);font-weight:300}
.btn{display:inline-flex;align-items:center;gap:16px;background:#0D1B33;color:#F6F3EC;border-radius:999px;padding:28px 46px;font-size:28px;font-weight:600;min-height:96px}
.grow{flex:1 1 0;min-height:0}
/* video-only motion: active when the renderer adds body.anim */
body.anim .sig-b,body.anim .band-b{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 2.4s cubic-bezier(.45,0,.2,1) .7s forwards}
body.anim .sig-a,body.anim .band-a{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 2.6s cubic-bezier(.3,0,.2,1) 3.4s forwards}
body.anim .sig-o,body.anim .band-o{transform-box:fill-box;transform-origin:center;animation:opop 1s cubic-bezier(.3,1.5,.5,1) 3s both,obreathe 3.8s ease-in-out 4.1s infinite}
body.anim .sig-end{transform-box:fill-box;transform-origin:center;animation:opop .9s cubic-bezier(.3,1.5,.5,1) 5.9s both,obreathe 3.8s ease-in-out 6.8s infinite}
body.anim .sig-start{animation:fadein .7s ease .3s both}
body.anim .qbadge{animation:qfloat 5.5s ease-in-out infinite}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes opop{0%{transform:scale(0);opacity:0}100%{transform:scale(1);opacity:1}}
@keyframes obreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
@keyframes fadein{from{opacity:0}to{opacity:1}}
@keyframes qfloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
.qbadge{display:inline-flex;align-items:center;gap:12px;background:#0D1B33;color:#F6F3EC;border-radius:999px;padding:10px 14px 10px 28px;font-size:22px;font-weight:600;letter-spacing:.16em;
 box-shadow:0 0 0 7px color-mix(in srgb,var(--g) 40%,transparent),0 16px 30px -16px rgba(13,27,51,.55)}
.qbadge .q{font-family:'Noto Color Emoji';font-size:34px;letter-spacing:0;line-height:1;display:inline-block;transform:rotate(14deg);
 background:#F6F3EC;border-radius:50%;width:46px;height:46px;display:grid;place-items:center;box-shadow:0 0 18px 2px color-mix(in srgb,var(--g) 90%,transparent);
 animation:qwig 3.7s ease-in-out infinite;animation-play-state:paused}
@keyframes qwig{0%,100%{transform:rotate(14deg) scale(1);box-shadow:0 0 18px 2px color-mix(in srgb,var(--g) 90%,transparent)}
 12%{transform:rotate(-12deg) scale(1.12)}24%{transform:rotate(18deg) scale(1.08)}36%{transform:rotate(-6deg) scale(1.04)}
 48%{transform:rotate(14deg) scale(1);box-shadow:0 0 30px 8px color-mix(in srgb,var(--g) 100%,transparent)}}
.wrap > *{flex-shrink:0}
.wrap > .grow{flex-shrink:1}
.center{text-align:center}
"""

DOTS = "<span class='dots'>" + "".join(f"<i style='background:{S[s]['c']}'></i>" for s in ("activate", "focus", "calm", "sleep")) + "</span>"

def band(st):
    from gen import gesture_before, gesture_after
    c = S[st]; y = 60
    d1 = "M 60 %d" % y + gesture_before(st, 60, 430, y); d2 = "M 482 %d" % y + gesture_after(st, 482, 1020, y)
    dots = "".join("<circle cx='%d' cy='150' r='8' fill='%s'/>" % (60 + i * 30, S[k]['c']) for i, k in enumerate(("activate", "focus", "calm", "sleep")))
    return ("<svg style='position:absolute;left:0;bottom:120px;z-index:0;opacity:.55' width='1080' height='190' viewBox='0 0 1080 190'>"
            "<path class='band-b' pathLength='1' d='%s' fill='none' stroke='%s' stroke-opacity='.5' stroke-width='3' stroke-linecap='round'/>"
            "<path class='band-a' pathLength='1' d='%s' fill='none' stroke='%s' stroke-width='4' stroke-linecap='round'/><g class='band-o'>%s</g>%s</svg>") % (d1, c['c'], d2, c['c'], o_mark(456, y, st, 20), dots)

def page(title, st, fmt, body, css=""):
    c = S[st]
    H = 1350 if fmt == "45" else 1920
    pad = "64px 72px 60px" if fmt == "45" else "274px 78px 400px"   # 9:16: keep clear of Reels/Stories UI
    v = f"--H:{H}px;--pad:{pad};--c:{c['c']};--g:{c['g']};--soft:{c['soft']};"
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>:root{{{v}}}{CSS}{css}</style></head>"
            f"<body class='f{fmt}'>{band(st) if fmt == '916' else ''}<div class='wrap'>{body}</div></body></html>")

def top(st, right="slogan", dark=False):
    col = "#F6F3EC" if dark else "#0D1B33"
    r = {"slogan": "<div class='slogan'>Choose the <b>moment.</b></div>", "dots": DOTS, "": ""}.get(right, right)
    return f"<div class='top'>{svg_logo('lockup', col, h=44)}{r}</div>"

def headline(eyebrow, a, b=None, size=88, center=False, grey=True):
    acc = f"<span class='acc'>{b}</span>" if b else ""
    return (f"<div class='{'center' if center else ''}'><div class='eyebrow {'grey' if grey else ''}'>{eyebrow}</div>"
            f"<h1 style='margin-top:16px;font-size:{size}px'>{a}{acc}</h1></div>")

def chip(img, t, s):
    return f"<div class='chip'><img src='{A}{img}'><div><div class='t'>{t}</div><div class='s'>{s}</div></div><div class='arr'>→</div></div>"

# ---------- 01-03 Vorher / Nachher ----------
BA = [
 dict(key="01-sleep-vorher-nachher", st="sleep", eyebrow="<span class='qbadge'>Sieht dein Abend so aus<span class='q'>❓</span></span>", a="Der Körper liegt.", b="Der Kopf nicht.",
      off_t="Licht aus. Gedanken noch an.", off=[("22:50", "Licht aus. Und plötzlich fällt dir alles ein, was morgen ansteht."), ("23:40", "Du drehst das Kissen um und rechnest, wie viele Stunden noch bleiben.")],
      on_t="Licht aus. Der Tag ist vorbei.", on=[("22:16", "Ein Sprühstoß aufs Kissen, Roll-On aufs Handgelenk."), ("22:17", "Dein Signal: Der Tag ist vorbei.")],
      why="Dir fehlt keine Müdigkeit. Dir fehlt ein Ende für den Tag.", img="nr-set-sleep-hero.webp", line="sbox", ct="Dein Abend-Signal holen", cs="SLEEP Komplett-Set · €89"),
 dict(key="02-calm-vorher-nachher", st="calm", eyebrow="<span class='qbadge'>Sieht dein Feierabend so aus<span class='q'>❓</span></span>", a="Du bist zu Hause.", b="Aber nicht ganz da.",
      off_t="Zu Hause. Kopf noch im Meeting.", off=[("18:40", "Auf dem Heimweg spielst du das Meeting noch einmal durch."), ("19:30", "Am Tisch nickst du, hörst aber nur halb zu.")],
      on_t="Laptop zu. Kopf frei.", on=[("18:06", "Roll-On aufs Handgelenk. Ein Atemzug."), ("18:07", "Dein Signal: Ab jetzt ist Feierabend.")],
      why="Dir fehlt kein Feierabend. Dir fehlt ein Schlusspunkt.", img="nr-set-calm-hero_d9e1c46a-abd5-4b2b-b375-fb6d6ae9d035.webp", line="box", ct="Dein Feierabend-Signal holen", cs="CALM Komplett-Set · €89"),
 dict(key="03-focus-vorher-nachher", st="focus", eyebrow="<span class='qbadge'>Sieht dein Nachmittag so aus<span class='q'>❓</span></span>", a="Du bist beschäftigt.", b="Aber nicht bei der Sache.",
      off_t="Viel beschäftigt. Wenig geschafft.", off=[("14:55", "Zwölf Tabs offen. Keiner davon fertig."), ("15:10", "Dritter Kaffee. Oder doch der Riegel aus der Schublade.")],
      on_t="Eine Aufgabe. Ganz bei der Sache.", on=[("14:56", "Roll-On aufs Handgelenk. Ein Atemzug."), ("14:57", "Dein Signal zum Abtauchen.")],
      why="Dir fehlt keine Konzentration. Dir fehlt ein klarer Neustart.", img="nr-set-focus-hero_651397b1-0fd3-4ca6-a8b7-f7041f0dc4a8.webp", line="box", ct="Dein Fokus-Signal holen", cs="FOCUS Komplett-Set · €89"),
]

def product_line(st, kind, ct, cs, fmt):
    """Frosted board with the product line (four states, the ad's state highlighted) and the CTA."""
    tall = fmt == "916"; ih = 150 if tall else 172
    fmt_name = "Textilspray" if kind == "sbox" else "Roll-On"
    tiles = ""
    for s in ("activate", "focus", "calm", "sleep"):
        on = s == st; c = S[s]
        tiles += (f"<div style='flex:1;background:#fff;border-radius:20px;padding:12px 8px 14px;text-align:center;"
                  + (f"box-shadow:0 0 0 2.5px {c['c']},0 18px 34px -18px color-mix(in srgb,{c['c']} 70%,transparent)" if on else "box-shadow:0 12px 26px -22px rgba(13,27,51,.5)")
                  + f"'><img src='{A}nr-{kind}-{s}-cut.png' style='display:block;height:{ih}px;margin:0 auto;filter:drop-shadow(0 10px 10px rgba(13,27,51,.18))'>"
                  f"<div style='display:flex;align-items:center;justify-content:center;gap:9px;margin-top:12px'>"
                  f"<span class='dot' style='--c:{c['c']};--g:{c['g']};width:10px;height:10px'></span>"
                  f"<span class='lbl' style='font-size:18px;color:{c['c']}'>{c['name']}</span></div></div>")
    return (f"<div class='board glow' style='padding:{'24px 24px 24px' if tall else '18px 20px 20px'};margin-top:{18 if tall else 14}px'>"
            f"<div style='display:flex;align-items:baseline;justify-content:space-between;gap:16px;margin-bottom:{16 if tall else 12}px'>"
            f"<div style='font-size:{27 if tall else 25}px;font-weight:600;letter-spacing:-.01em'>{ct} <span style='color:var(--c)'>→</span></div>"
            f"<div style='font-size:{20 if tall else 19}px;color:rgba(13,27,51,.6)'>{fmt_name}-Reihe · {cs}</div></div>"
            f"<div style='display:flex;gap:12px'>{tiles}</div></div>")

def ad_ba(d, fmt):
    st = d["st"]; tall = fmt == "916"
    rp = "11px" if tall else "12px"
    rows = lambda rs, on: "".join(
        f"<div style='display:grid;grid-template-columns:66px 1fr;gap:8px;padding:{rp} 0;border-top:1px solid rgba(13,27,51,.07);font-size:{22 if tall else 21.5}px;line-height:1.36'>"
        f"<span style='font-size:19px;font-weight:600;letter-spacing:.04em;padding-top:2px;color:{'var(--c)' if on else 'rgba(13,27,51,.5)'}'>{t}</span>"
        f"<span style='color:{'#0D1B33' if on else 'rgba(13,27,51,.7)'}'>{x}</span></div>" for t, x in rs)
    card = lambda on: (
        f"<div style='border-radius:26px;padding:{'22px 22px 6px' if tall else '20px 22px 6px'};{'background:var(--soft);border:1px solid color-mix(in srgb,var(--c) 14%,transparent)' if on else 'background:rgba(242,241,238,.9);border:1px solid rgba(13,27,51,.06)'}'>"
        + (f"<div class='lbl' style='color:var(--c)'><span class='dot' style='width:10px;height:10px;margin-right:12px'></span>Mit {S[st]['name']}</div>" if on else
           "<div class='lbl' style='color:rgba(13,27,51,.5)'>⦸&nbsp; Ohne Signal</div>")
        + f"<div style='font-size:28px;font-weight:300;letter-spacing:-.035em;line-height:1.12;margin:12px 0 10px;color:{'var(--c)' if on else 'rgba(13,27,51,.8)'}'>{d['on_t'] if on else d['off_t']}</div>"
        + rows(d["on"] if on else d["off"], on) + "</div>")
    body = (top(st) + "<div class='grow'></div>"
            + headline(d["eyebrow"], d["a"], d["b"], 84 if tall else 80, center=True, grey=False)
            + f"<div style='margin:{'14px' if tall else '6px'} -10px -4px'>{signal_bridge(st, 980, drop=72 if tall else 70, lx=245, rx=740)}</div>"
            + f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:14px'>{card(False)}{card(True)}</div>"
            + f"<div style='background:#121B33;color:#F6F3EC;border-radius:22px;padding:{'18px 24px' if tall else '16px 24px'};margin-top:14px'>"
              f"<div class='lbl' style='font-size:18px;color:var(--g)'>Der eigentliche Grund</div>"
              f"<div style='font-size:{28 if tall else 26}px;font-weight:300;letter-spacing:-.02em;line-height:1.2;margin-top:6px'>{d['why']}</div></div>"
            + product_line(st, d["line"], d["ct"], d["cs"], fmt) + "<div class='grow'></div>")
    return page(d["key"], st, fmt, body)

# ---------- 01-03 VIDEO layout: full-width stage (Ohne -> Mit) + product slider ----------
VID_CSS = """
.stage{position:relative;overflow:hidden}
.stage .vcard{position:absolute;top:0;height:100%;border-radius:28px;overflow:hidden}
.stage .vcard .in{position:absolute;top:0;width:var(--sw);height:100%;padding:26px 30px 12px}
.stage .off{left:0;width:100%;background:rgba(242,241,238,.95);border:1px solid rgba(13,27,51,.07)}
.stage .on{right:0;width:0;background:var(--soft);border:1px solid color-mix(in srgb,var(--c) 18%,transparent);box-shadow:0 24px 50px -36px color-mix(in srgb,var(--c) 70%,transparent)}
.vrow{display:grid;grid-template-columns:104px 1fr;gap:12px;padding:16px 0 0;border-top:1px solid rgba(13,27,51,.07);font-size:35px;line-height:1.3;letter-spacing:-.01em}
.vlbl{font-size:28px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;display:flex;align-items:center}
.vtit{font-size:56px;font-weight:400;letter-spacing:-.035em;line-height:1.08;margin:14px 0 16px}
.offt{color:rgba(13,27,51,.72)} .offt b{font-weight:700;color:#0D1B33}
.ont{color:#0D1B33} .ont b{font-weight:700;color:var(--c)}
.vrow .t{font-size:27px;font-weight:700;letter-spacing:.03em;padding-top:5px}
.slider{overflow:hidden;border-radius:20px}
.slider .strip{display:flex;gap:14px;width:max-content;transform:translateX(var(--from))}
body.anim .bh{animation:bhup .75s cubic-bezier(.65,0,.3,1) 1.75s both}
body.anim .hh{animation:hhup .75s cubic-bezier(.65,0,.3,1) 3.85s both}
body.anim .stage{overflow:visible}
body.anim .stage .off{animation:offin .8s cubic-bezier(.2,.8,.2,1) 4.45s both,offsq 1.8s cubic-bezier(.6,0,.3,1) 7.2s both}
body.anim .stage .on{animation:onin 1.8s cubic-bezier(.6,0,.3,1) 7.2s both}
body.anim .sig-start{animation:fadein .5s ease 4.75s both}
body.anim .sig-b{animation:draw 2.2s cubic-bezier(.45,0,.2,1) 4.85s forwards}
body.anim .sig-o{animation:opop .8s cubic-bezier(.3,1.5,.5,1) 6.95s both,obreathe 3.8s ease-in-out 7.8s infinite}
body.anim .sig-a{animation:draw 1.9s cubic-bezier(.3,0,.2,1) 7.1s forwards}
body.anim .sig-end{animation:opop .7s cubic-bezier(.3,1.5,.5,1) 8.95s both,obreathe 3.8s ease-in-out 9.7s infinite}
body.anim .col{animation:colup .9s cubic-bezier(.65,0,.3,1) 9.4s both}
body.anim .slider{animation:slin .9s cubic-bezier(.2,.8,.2,1) 9.5s both}
body.anim .slider .strip{animation:slide 4s linear 9.5s both}
@keyframes bhup{from{transform:translateY(var(--dyb)) scale(1.5)}to{transform:none}}
@keyframes hhup{from{transform:translateY(var(--dyh)) scale(1.12)}to{transform:none}}
@keyframes offin{from{transform:translateX(-115%)}to{transform:none}}
@keyframes colup{from{transform:translateY(var(--dyc))}to{transform:none}}
@keyframes slin{from{opacity:0;transform:translateY(70px)}to{opacity:1;transform:none}}
@keyframes offsq{from{width:100%;opacity:1}to{width:0%;opacity:.35}}
@keyframes onin{0%{width:0%;opacity:0}8%{opacity:1}100%{width:100%;opacity:1}}
@keyframes slide{from{transform:translateX(var(--from))}to{transform:translateX(0)}}
.w{display:inline-block}
.qbadge.w{display:inline-flex}
.qbadge .q.w{display:grid}
body.anim .w{animation:wpop .42s cubic-bezier(.2,.9,.3,1.25) both}
body.anim .qbadge.w{animation:wpop .5s cubic-bezier(.2,.9,.3,1.2) both}
body.anim .qbadge .q.w{animation:wpop .5s cubic-bezier(.2,.9,.3,1.3) both,qwig 3.7s ease-in-out 3s infinite}
@keyframes wpop{from{opacity:0;transform:translateY(14px) scale(.85)}to{opacity:1;transform:none}}
"""

MEASURE_JS = """<script>
window.__measure = function () {
  const H = innerHeight, sl = document.querySelector('.slider');
  const sh = sl.getBoundingClientRect().height + parseFloat(getComputedStyle(sl).marginTop);
  const dyc = sh / 2, mid = r => (r.top + r.bottom) / 2;
  const col = document.querySelector('.col'), bh = document.querySelector('.bh'), hh = document.querySelector('.hh');
  col.style.setProperty('--dyc', dyc + 'px');
  bh.style.setProperty('--dyb', (H / 2 - (mid(bh.getBoundingClientRect()) + dyc)) + 'px');
  hh.style.setProperty('--dyh', (H / 2 - (mid(hh.getBoundingClientRect()) + dyc)) + 'px');
};
</script>"""

def _words(text, t0, step, cls="w"):
    out = []; t = t0
    for w in text.split(" "):
        out.append(f"<span class='{cls}' style='animation-delay:{t:.2f}s'>{w}</span>"); t += step
    return " ".join(out), t

def typed_headline(d, size):
    import re
    q = re.sub(r"<[^>]+>", "", d["eyebrow"]).replace("❓", "").strip()
    bw, t = _words(q, 0.35, 0.24)
    badge = (f"<span class='qbadge w' style='animation-delay:0.15s'>{bw}<span class='q w' style='animation-delay:{t:.2f}s'>❓</span></span>")
    a_w, t2 = _words(d["a"], t + 0.45, 0.27)
    b_w, t3 = _words(d["b"], t2 + 0.1, 0.28)
    return (f"<div class='center'><div class='eyebrow bh'>{badge}</div>"
            f"<h1 class='hh' style='margin-top:16px;font-size:{size}px'>{a_w}<span class='acc'>{b_w}</span></h1></div>")

VROWS = {
 "01-sleep-vorher-nachher": (("22:50", "Licht aus. Und plötzlich <b>fällt dir alles ein</b>, was morgen ansteht."),
                             ("22:16", "<b>Ein Sprühstoß</b> aufs Kissen, <b>Roll-On</b> aufs Handgelenk.")),
 "02-calm-vorher-nachher":  (("18:40", "Auf dem Heimweg spielst du <b>das Meeting</b> noch einmal durch."),
                             ("18:06", "<b>Roll-On</b> aufs Handgelenk. <b>Ein Atemzug.</b>")),
 "03-focus-vorher-nachher": (("14:55", "<b>Zwölf Tabs offen.</b> Keiner davon fertig."),
                             ("14:56", "<b>Roll-On</b> aufs Handgelenk. <b>Ein Atemzug.</b>")),
}

def ad_ba_video(d, fmt):
    st = d["st"]; tall = fmt == "916"; c = S[st]
    SW = 924 if tall else 936; ih = 214 if tall else 190; tw = 236
    vo, vn = VROWS[d["key"]]
    row = lambda r, on: (f"<div class='vrow'><span class='t' style='color:{'var(--c)' if on else 'rgba(13,27,51,.5)'}'>{r[0]}</span>"
                         f"<span class='{'on' if on else 'off'}t'>{r[1]}</span></div>")
    off = (f"<div class='vcard off'><div class='in' style='left:0'>"
           "<div class='vlbl' style='color:rgba(13,27,51,.55)'>⦸&nbsp; Ohne Signal</div>"
           f"<div class='vtit' style='color:rgba(13,27,51,.85)'>{d['off_t']}</div>"
           + row(vo, False) + "</div></div>")
    on = (f"<div class='vcard on'><div class='in' style='left:0'>"
          f"<div class='vlbl' style='color:var(--c)'><span class='dot' style='width:15px;height:15px;margin-right:16px'></span>Mit {c['name']}</div>"
          f"<div class='vtit' style='color:var(--c)'>{d['on_t']}</div>"
          + row(vn, True) + "</div></div>")
    stage_h = 330 if tall else 312
    stage = f"<div class='stage' style='height:{stage_h}px;--sw:{SW}px'>{off}{on}</div>"
    # product slider: Textilspray line + Roll-On line, the ad's state highlighted in both
    def tile(kind, s_):
        cc = S[s_]; hi = s_ == st
        return (f"<div style='flex:none;width:{tw}px;background:#fff;border-radius:20px;padding:12px 8px 14px;text-align:center;"
                + (f"box-shadow:inset 0 0 0 2.5px {cc['c']},0 18px 30px -20px color-mix(in srgb,{cc['c']} 70%,transparent)" if hi else "box-shadow:0 12px 24px -22px rgba(13,27,51,.5)")
                + f"'><img src='{A}nr-{kind}-{s_}-cut.png' style='display:block;height:{ih}px;margin:0 auto;filter:drop-shadow(0 10px 10px rgba(13,27,51,.18))'>"
                f"<div style='display:flex;align-items:center;justify-content:center;gap:9px;margin-top:10px'>"
                f"<span class='dot' style='--c:{cc['c']};--g:{cc['g']};width:11px;height:11px'></span>"
                f"<span class='lbl' style='font-size:19px;color:{cc['c']}'>{cc['name']}</span></div>"
                f"<div style='font-size:18px;color:rgba(13,27,51,.55);margin-top:4px'>{'Textilspray' if kind == 'sbox' else 'Roll-On'}</div></div>")
    order = ("activate", "focus", "calm", "sleep")
    strip = "".join(tile("sbox", s_) for s_ in order) + "".join(tile("box", s_) for s_ in order)
    shift = int(2.5 * (tw + 14))
    bleed = 78 if tall else 72
    slider = (f"<div class='slider' style='margin:{30 if tall else 22}px -{bleed}px 0;border-radius:0;padding:14px 0 24px'>"
              f"<div class='strip' style='--from:-{shift}px'>{strip}</div></div>")
    body = (top(st, "") + "<div class='grow'></div>"
            + "<div class='col'>" + typed_headline(d, 88 if tall else 82)
            + f"<div style='margin:{'14px' if tall else '8px'} -10px -4px'>{signal_bridge(st, 980, drop=72 if tall else 66, lx=245, rx=740)}</div>"
            + stage + slider + "</div><div class='grow'></div>" + MEASURE_JS)
    return page(d["key"], st, fmt, body, VID_CSS + 'body > svg{display:none}')

# ---------- 04 Founder ----------
def ad_founder(fmt):
    st = "activate"; tall = fmt == "916"
    ih = 750 if tall else 680
    play = ("<div style='position:absolute;right:26px;bottom:26px;display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.9);"
            "border-radius:999px;padding:10px 20px 10px 10px;box-shadow:0 14px 30px -18px rgba(13,27,51,.5)'>"
            "<span style='width:44px;height:44px;border-radius:50%;background:#0D1B33;display:grid;place-items:center'>"
            "<svg width='16' height='18' viewBox='0 0 16 18'><path d='M2 1.5v15l13-7.5z' fill='#F6F3EC'/></svg></span>"
            "<span class='lbl' style='color:#0D1B33'>Philip über das Ritual</span></div>")
    body = (top(st, "dots") + "<div class='grow'></div>"
      + f"<div class='board glow' style='padding:12px'><div style='position:relative'>"
        f"<img src='{A}nr-founder-ritual-3c-poster.jpg' style='display:block;width:100%;height:{ih}px;object-fit:cover;object-position:50% 78%;border-radius:22px'>"
        f"{play}</div></div>"
      + f"<div class='it' style='font-size:120px;line-height:.6;color:var(--c);height:52px;margin-top:30px'>“</div>"
      + f"<div style='font-size:{54 if tall else 50}px;font-weight:300;letter-spacing:-.04em;line-height:1.12'>Duft begleitet uns jeden Tag, meist unbewusst. Mit Neurora Labs machen wir ihn zu einem <span style='color:var(--c)'>bewussten Werkzeug</span>.</div>"
      + "<div style='display:flex;align-items:center;justify-content:space-between;gap:20px;margin-top:28px'>"
        f"<div style='display:flex;align-items:center;gap:14px'><div style='width:46px;height:46px;border-radius:10px;background:#0D1B33;display:grid;place-items:center'>{svg_logo('mono', '#F6F3EC', h=22)}</div>"
        "<div class='lbl' style='color:rgba(13,27,51,.6);font-size:18px;line-height:1.5'>Philip Huber<br>Founder &amp; CEO</div></div>"
        "<div class='btn'>Philip erklärt das Ritual&nbsp; →</div></div>"
      + "<div class='grow'></div>")
    return page("Founder", st, fmt, body)

# ---------- 05 Mission (navy, product centre) ----------
def ad_mission(fmt):
    st = "sleep"
    css = "body{background:#0B1630}body::before{background:radial-gradient(700px 620px at 100% 0%,rgba(78,61,152,.6),transparent 70%),radial-gradient(620px 520px at 0% 100%,rgba(181,71,31,.2),transparent 70%)}"
    body = (top(st, "<div class='slogan' style='color:rgba(246,243,236,.7)'>Choose the <b style='color:#C5B0F3'>moment.</b></div>", dark=True)
      + "<h1 style='font-size:84px;color:#F6F3EC'>Auf Wissenschaft gebaut.<span class='acc' style='color:rgba(246,243,236,.5)'>Damit deine Stimmung dir gehört.</span></h1>"
      + "<div class='grow' style='display:flex;align-items:center;padding:34px 0'>"
      f"<div style='width:100%;border-radius:32px;overflow:hidden;box-shadow:0 40px 80px -40px rgba(0,0,0,.6);border:1px solid rgba(255,255,255,.12)'>"
      f"<img src='{A}nr-set-sleep-hero.webp' style='display:block;width:100%;height:520px;object-fit:cover;object-position:50% 58%'></div></div>"
      + f"<div class='lbl' style='font-size:18px;color:rgba(246,243,236,.65)'><span class='dot' style='--c:#B5471F;--g:#F6AE8E;width:9px;height:9px;margin-right:12px'></span>Mission</div>"
      f"<div style='font-size:38px;font-weight:300;letter-spacing:-.03em;line-height:1.2;color:#F6F3EC;margin-top:14px'>Wir übersetzen olfaktorische Wissenschaft in Werkzeuge für deinen Alltag.</div>")
    return page("Mission", st, fmt, body, css)

# ---------- 06 Ein Atemzug (CALM, Philip video) ----------
def ad_atemzug(fmt):
    st = "calm"
    times = [("07:00", "activate"), ("09:30", "focus"), ("18:30", "calm"), ("22:00", "sleep")]
    tabs = "".join(
        f"<div style='flex:1;text-align:center;padding:14px 0 12px;border-radius:18px;{'background:#fff;box-shadow:0 10px 26px -18px rgba(13,27,51,.4);' if s=='calm' else ''}'>"
        f"<span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:10px;height:10px;{'' if s=='calm' else 'box-shadow:none;'}'></span>"
        f"<div style='font-size:21px;font-weight:600;margin-top:6px'>{t}</div><div class='lbl' style='font-size:19px;color:{S[s]['c']};margin-top:3px'>{S[s]['name']}</div></div>" for t, s in times)
    body = (top(st)
      + "<div class='eyebrow grey'>Rituale</div>"
      + "<h1 style='font-size:110px;margin-top:10px'>Ein Atemzug.</h1>"
      + "<div style='font-size:52px;font-weight:300;letter-spacing:-.04em;line-height:1.08;color:#4E3D98;margin-top:6px'>Jeden Tag im selben Moment.</div>"
      + "<p class='lead' style='margin-top:20px'>Ein Duft, den du jeden Tag im selben Moment auflegst, wird zu deinem Signal für genau diesen Moment.</p>"
      + "<div class='grow' style='min-height:24px'></div>"
      + f"<div style='position:relative;border-radius:32px;overflow:hidden;border:8px solid rgba(255,255,255,.75);box-shadow:0 30px 60px -36px rgba(13,27,51,.45)'>"
        f"<img src='{A}nr-founder-ritual-3c-poster.jpg' style='display:block;width:100%;height:600px;object-fit:cover;object-position:50% 68%'>"
        f"<div style='position:absolute;right:30px;top:30px;width:96px;height:96px;border-radius:50%;background:#fff;display:grid;place-items:center;box-shadow:0 0 0 12px rgba(163,204,240,.5)'><div style='width:0;height:0;border-left:22px solid #0D1B33;border-top:14px solid transparent;border-bottom:14px solid transparent;margin-left:6px'></div></div>"
        f"<div style='position:absolute;left:0;right:0;bottom:0;padding:16px'><div class='board' style='padding:8px'><div style='display:flex;gap:4px'>{tabs}</div></div></div></div>"
      + "<div style='font-size:19px;color:rgba(13,27,51,.55);margin-top:14px'>Philip, Gründer von Neurora, über sein Ritual am Feierabend.</div>"
      + "<div style='margin-top:24px'><div class='btn'>Finde dein Ritual&nbsp; →</div></div>")
    return page("Ein Atemzug", st, fmt, body)

# ---------- 07 Wo hakt dein Tag ----------
def ad_quiz_tiles(fmt):
    st = "sleep"
    items = [("activate", "07:00", "Morgens schwer in Gang?"), ("focus", "09:30", "Nachmittagstief um 15 Uhr?"),
             ("calm", "18:30", "Kopf noch im Meeting?"), ("sleep", "22:00", "Im Bett und noch hellwach?")]
    cards = "".join(
        f"<div style='background:linear-gradient(120deg,#fff 55%,color-mix(in srgb,{S[s]['g']} 28%,#fff));border-radius:26px;padding:28px 30px;box-shadow:0 14px 34px -26px rgba(13,27,51,.35);display:flex;align-items:center;gap:22px'>"
        f"<div style='flex:1'><div class='lbl' style='font-size:18px;color:{S[s]['c']}'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:10px;height:10px;margin-right:12px'></span>{t} · {S[s]['name']}</div>"
        f"<div style='font-size:36px;font-weight:300;letter-spacing:-.03em;margin-top:12px'>{h}</div></div>"
        f"<div style='width:44px;height:44px;border-radius:50%;border:1.5px solid rgba(13,27,51,.15);flex:none'></div></div>" for s, t, h in items)
    body = (top(st, "dots")
      + headline("Kennst du das?", "Wo hakt", "dein Tag?", 112)
      + "<div class='grow' style='min-height:30px'></div>"
      + f"<div style='display:flex;flex-direction:column;gap:14px'>{cards}</div>"
      + "<div style='display:flex;justify-content:space-between;align-items:center;margin-top:28px'>"
        "<div style='font-size:23px;color:rgba(13,27,51,.65);max-width:440px;line-height:1.35'>Tipp an, was du kennst.</div>"
        "<div class='btn'>Ritual finden →</div></div>")
    return page("Wo hakt dein Tag", st, fmt, body)

# ---------- 08 Ein Duft wird zum Signal ----------
def ad_signal_steps(fmt):
    st = "sleep"
    steps = [("01", "Der Moment", "nr-rituale-schritt-1-moment.jpg"), ("02", "Der Duft", "nr-rituale-schritt-2-duft.jpg"),
             ("03", "Der Atemzug", "nr-rituale-schritt-3-atemzug-v2.jpg"), ("04", "Das Signal", "nr-rituale-schritt-4-signal.jpg")]
    cards = "".join(
        f"<div class='board' style='padding:10px 10px 18px;border-radius:26px'><img src='{A}{img}' style='display:block;width:100%;height:220px;object-fit:cover;border-radius:18px'>"
        f"<div style='display:flex;align-items:baseline;gap:14px;padding:12px 12px 0'><span class='it' style='font-size:38px'>{n}</span><span style='font-size:27px;font-weight:400;letter-spacing:-.02em'>{t}</span></div></div>" for n, t, img in steps)
    body = (top(st)
      + headline("Warum Rituale", "Ein Duft wird zum Signal.", "Durch Wiederholung.", 78)
      + "<div class='grow' style='min-height:24px'></div>"
      + f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:14px'>{cards}</div>"
      + "<div style='background:#0F1A35;border-radius:28px;padding:30px 32px;color:#F6F3EC;margin-top:16px'>"
        "<div style='font-size:32px;font-weight:300;letter-spacing:-.025em;line-height:1.22'>„Der angenehme Duft wird zum Signal. Und durch die Routine lerne ich, dass der Feierabend jetzt anfangen kann.“</div>"
        "<div style='font-size:19px;color:rgba(246,243,236,.6);margin-top:14px'>Philip, Gründer von Neurora</div></div>"
      + "<div style='margin-top:24px'><div class='btn'>Dein Ritual starten&nbsp; →</div></div>")
    return page("Duft wird Signal", st, fmt, body)

# ---------- 09 Vier Momente ----------
def ad_vier_momente(fmt):
    st = "sleep"
    m = [("activate", "07:00", "Dein Start."), ("focus", "09:30", "Dein Fokus-Block."), ("calm", "18:30", "Dein Feierabend."), ("sleep", "22:00", "Dein Licht aus.")]
    cards = "".join(
        f"<div style='border-radius:30px;padding:28px 26px 30px;background:linear-gradient(160deg,rgba(255,255,255,.94) 35%,color-mix(in srgb,{S[s]['g']} 34%,#fff));box-shadow:0 18px 40px -30px rgba(13,27,51,.35);border:1px solid rgba(255,255,255,.95);display:flex;flex-direction:column'>"
        f"<div style='display:flex;justify-content:space-between;align-items:center'><span class='it' style='font-size:44px;color:{S[s]['c']}'>{t}</span>"
        f"<span class='lbl' style='font-size:18px;color:{S[s]['c']};background:#fff;border-radius:999px;padding:9px 14px'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:9px;height:9px;box-shadow:none;margin-right:8px'></span>{S[s]['name']}</span></div>"
        f"<div class='grow' style='min-height:20px'></div><div style='margin:0 0 18px'>{signal_inline(s, 410, 54, 0.36)}</div>"
        f"<div style='font-size:46px;font-weight:300;letter-spacing:-.045em;line-height:1.05'>{h}</div></div>" for s, t, h in m)
    body = (top(st, "dots")
      + headline("Dein Tag in vier Ritualen", "Vier Momente.", "Ein Duft für jeden.", 92)
      + "<p class='lead' style='margin-top:18px'>Fang mit einem Moment an. Die anderen kommen dazu, wenn du willst.</p>"
      + f"<div style='display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:14px;margin-top:34px;flex:1'>{cards}</div>"
      + "<div style='margin-top:24px'><div class='btn'>Wähle deinen Moment&nbsp; →</div></div>")
    return page("Vier Momente", st, fmt, body)

# ---------- 10 Die ersten 30 Tage ----------
def ad_30(fmt):
    st = "sleep"
    steps = [("Tag 1", "Wähle einen Moment.", "nr-rituale-66-tag-1.jpg"), ("Woche 1", "Gleicher Duft, gleicher Moment.", "nr-rituale-66-woche-1.jpg"),
             ("Woche 4", "Der Duft läuft mit.", "nr-rituale-66-woche-4.jpg"), ("Ab Tag 30", "Dein Signal. Auf Abruf.", "nr-rituale-66-tag-66.jpg")]
    o = ("<svg width='30' height='30' viewBox='0 0 30 30'><circle cx='15' cy='15' r='14' fill='#C5B0F3' opacity='.35'/>"
         "<path d='M 11.5 5.6 A 10 10 0 1 0 18.5 5.6' fill='none' stroke='#4E3D98' stroke-width='2.5' stroke-linecap='round'/><circle cx='15' cy='15' r='4.5' fill='#C5B0F3'/></svg>")
    ring = "<span style='width:24px;height:24px;border-radius:50%;border:2.5px solid #0D1B33;display:inline-block'></span>"
    cards = "".join(
        f"<div><div style='display:flex;align-items:center;gap:12px'>{o if i == 3 else ring}<span class='it' style='font-size:34px'>{l}</span></div>"
        f"<div style='font-size:27px;font-weight:400;letter-spacing:-.02em;margin:8px 0 14px'>{t}</div>"
        f"<img src='{A}{img}' style='display:block;width:100%;height:230px;object-fit:cover;border-radius:22px'></div>" for i, (l, t, img) in enumerate(steps))
    body = (top(st)
      + headline("Dein Plan", "Die ersten 30 Tage.", "Ein Moment nach dem anderen.", 80)
      + "<div class='grow' style='min-height:24px'></div>"
      + f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:30px 24px'>{cards}</div>"
      + "<div style='margin-top:26px;font-size:22px;color:rgba(13,27,51,.7)'><b style='color:#0D1B33;font-weight:600'>Einen Tag ausgelassen?</b> Macht nichts. Mach am nächsten Tag einfach weiter.</div>"
      + "<div style='margin-top:24px'><div class='btn'>30 Tage testen&nbsp; →</div></div>")
    return page("Die ersten 30 Tage", st, fmt, body)

# ---------- 11 FOCUS Angebot ----------
def ad_offer(fmt):
    st = "focus"
    check = "<span style='width:30px;height:30px;border-radius:50%;background:#1F4A3D;display:grid;place-items:center;flex:none'><svg width='15' height='15' viewBox='0 0 16 16'><path d='M3 8.5l3.2 3L13 4.8' stroke='#fff' stroke-width='2.2' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg></span>"
    items = [("Roll-On · 10 ml", "€29"), ("Textilspray · 30 ml", "€39"), ("Raumdiffuser · 125 ml", "€49")]
    rows = "".join(f"<div style='display:flex;gap:16px;align-items:center;padding:14px 0;border-top:1px solid rgba(13,27,51,.08);font-size:24px'>{check}<span style='flex:1'>FOCUS {a}</span><span style='color:rgba(13,27,51,.6)'>{b}</span></div>" for a, b in items)
    body = (top(st)
      + headline("Dein Angebot", "Alles für deinen", "Fokus-Block.", 80, grey=False)
      + "<div class='board' style='margin-top:30px;flex:1;display:flex;flex-direction:column'>"
      f"<div style='position:relative'><img src='{A}nr-set-focus-hero_651397b1-0fd3-4ca6-a8b7-f7041f0dc4a8.webp' style='display:block;width:100%;height:360px;object-fit:cover;object-position:50% 62%'>"
      "<div style='position:absolute;right:24px;bottom:22px;width:130px;height:130px;border-radius:50%;background:rgba(255,255,255,.94);display:grid;place-items:center;text-align:center'><div><div style='font-size:42px;font-weight:300;color:var(--c);line-height:1'>30</div><div class='lbl' style='font-size:18px;margin-top:4px'>Tage testen</div></div></div></div>"
      f"<div style='padding:20px 34px 30px;display:flex;flex-direction:column;flex:1'>{rows}"
      "<div style='display:flex;justify-content:space-between;align-items:flex-end;margin-top:14px;padding-top:16px;border-top:1.5px solid #0D1B33'><div style='font-size:21px;color:rgba(13,27,51,.6)'>Gesamtwert <s>€122,99</s></div>"
      "<div style='font-size:72px;font-weight:300;color:var(--c);line-height:1'>€89</div></div>"
      "<div style='background:#E3F1EA;border-radius:18px;padding:16px 20px;margin-top:16px;font-size:20px'>+ Roll-On deiner Wahl gratis dazu (Wert 29 €)</div>"
      "<div class='grow'></div><div class='btn' style='justify-content:center;margin-top:18px'>Fokus-Set in den Warenkorb · €89</div></div></div>")
    return page("FOCUS Angebot", st, fmt, body)

# ---------- 12 Kompass ----------
def ad_kompass(fmt):
    st = "focus"
    mol = "".join(f"<span style='display:inline-flex;align-items:center;gap:12px;background:#fff;border-radius:999px;padding:8px 22px 8px 8px;box-shadow:0 8px 22px -14px rgba(13,27,51,.35);font-size:22px'>"
                  f"<span style='width:44px;height:44px;border-radius:50%;background:#1F4A3D;color:#fff;display:grid;place-items:center;font-size:19px;font-weight:600;box-shadow:0 0 0 5px rgba(138,211,189,.35)'>{n}</span>{t}</span>"
                  for n, t in [("08", "1,8-Cineol"), ("09", "Kampfer"), ("10", "Verbenon")])
    body = (top(st, "dots")
      + "<div class='lbl' style='color:var(--c);font-size:19px'><span class='dot' style='width:10px;height:10px;margin-right:14px'></span>Neurora Kompass · Mood on Demand</div>"
      + "<h1 style='margin-top:18px;font-size:72px'>Für alle, die mehr über ihren Duft <span style='color:var(--c)'>lernen wollen.</span></h1>"
      + "<div class='board glow' style='margin-top:34px;padding:32px 32px 0;flex:1;display:flex;flex-direction:column'>"
      "<div class='lbl' style='font-size:18px;color:rgba(13,27,51,.55)'><span class='dot' style='width:10px;height:10px;margin-right:12px'></span>Jetzt · 12:46</div>"
      "<div style='display:flex;align-items:baseline;gap:22px;margin-top:10px'><span style='font-size:92px;font-weight:300;letter-spacing:-.045em;color:var(--c);line-height:1'>Scharf</span>"
      "<span class='it' style='font-size:30px;color:rgba(13,27,51,.7)'>Mittag · 12:00</span></div>"
      "<p style='font-size:22px;line-height:1.45;color:rgba(13,27,51,.7);margin-top:12px'>Durchdringend, kampferartig, präzise. Die Noten für die Stunden am Schreibtisch.</p>"
      f"<div style='display:flex;gap:12px;flex-wrap:wrap;margin-top:18px'>{mol}</div>"
      f"<div style='flex:1;min-height:260px;margin:16px -32px 0;overflow:hidden;display:flex;align-items:flex-start'>{dial_svg(1000)}</div></div>"
      "<div style='display:flex;justify-content:space-between;align-items:center;margin-top:22px;gap:24px'><p class='it' style='font-size:21px;line-height:1.35;color:rgba(13,27,51,.6);max-width:520px'>Duftfamilien beschreiben den Charakter eines Moleküls, keine Wirkung.</p><div class='btn'>Zum Kompass &nbsp;→</div></div>")
    return page("Kompass", st, fmt, body)

# ---------- 13 Mood-Quiz Intro ----------
def ad_quiz_intro(fmt):
    st = "sleep"
    body = (top(st, "dots")
      + "<div class='lbl' style='font-size:19px;color:#0D1B33'><span class='dot' style='--c:#0D1B33;--g:#E6E1F4;width:11px;height:11px;margin-right:14px'></span>Dein Ritual · 4 Fragen</div>"
      + "<h1 style='font-size:118px;margin-top:20px'>Finde deinen <span class='acc'>Moment.</span></h1>"
      + "<p class='lead' style='margin-top:20px'>Vier Momente, drei Formate. In unter einer Minute weißt du, womit dein Ritual beginnt.</p>"
      + "<div class='grow' style='min-height:30px'></div>"
      + f"<div style='position:relative;border-radius:32px;overflow:hidden;border:8px solid rgba(255,255,255,.75);box-shadow:0 30px 60px -36px rgba(13,27,51,.45)'>"
        f"<img src='{A}nr-quiz-intro-abend.jpg' style='display:block;width:100%;height:520px;object-fit:cover;object-position:40% 35%'>"
        "<div style='position:absolute;left:22px;bottom:22px;background:rgba(255,255,255,.88);border-radius:999px;padding:12px 22px;font-size:20px'>Ein Atemzug.</div></div>"
      + "<div style='margin-top:28px'><div class='btn'>Quiz starten&nbsp; →</div></div>")
    return page("Quiz Intro", st, fmt, body)

# ---------- 14 Mood-Quiz Frage ----------
def ad_quiz_q(fmt):
    st = "calm"
    icons = {"activate": "☀", "focus": "◎", "calm": "≈", "sleep": "☾"}
    opts = [("activate", "Der Morgen", "Ankommen im Tag, bevor der Tag dich hat."), ("focus", "Die Arbeitsstunden", "Eine Sache, volle Aufmerksamkeit."),
            ("calm", "Der Feierabend", "Der Laptop geht zu. Der Kopf soll mitkommen."), ("sleep", "Die Nacht", "Das Licht ist aus, der Tag noch nicht.")]
    rows = "".join(
        f"<div style='display:flex;align-items:center;gap:22px;padding:22px 24px;border-radius:24px;background:linear-gradient(100deg,color-mix(in srgb,{S[s]['g']} 32%,#fff),#fff 60%);border:1px solid rgba(255,255,255,.95);box-shadow:0 12px 30px -24px rgba(13,27,51,.35)'>"
        f"<div style='width:64px;height:64px;border-radius:18px;background:color-mix(in srgb,{S[s]['g']} 30%,#fff);border:1px solid color-mix(in srgb,{S[s]['c']} 20%,transparent);display:grid;place-items:center;font-size:30px;color:{S[s]['c']}'>{icons[s]}</div>"
        f"<div style='flex:1'><div style='font-size:30px;color:{S[s]['c']};letter-spacing:-.02em'>{t}</div><div style='font-size:20px;color:rgba(13,27,51,.65);margin-top:4px'>{d}</div></div>"
        f"<div style='width:52px;height:52px;border-radius:50%;background:rgba(13,27,51,.05);display:grid;place-items:center;font-size:24px'>→</div></div>" for s, t, d in opts)
    body = (top(st, "dots")
      + "<div style='display:flex;align-items:center;gap:16px'><span style='display:flex;gap:8px'>"
      + "".join(f"<i style='display:block;width:{44 if i == 0 else 34}px;height:5px;border-radius:3px;background:{'#0D1B33' if i == 0 else 'rgba(13,27,51,.15)'}'></i>" for i in range(4))
      + "</span><span class='lbl' style='font-size:18px;color:rgba(13,27,51,.55)'>Frage 1 / 4</span></div>"
      + "<h1 style='font-size:80px;margin-top:22px'>Welchen Moment deines Tages willst du <span style='color:var(--c)'>verändern?</span></h1>"
      + "<div class='grow' style='min-height:30px'></div>"
      + f"<div class='board glow' style='padding:18px;display:flex;flex-direction:column;gap:12px'>{rows}</div>"
      + "<div style='margin-top:26px;display:flex;justify-content:space-between;align-items:center'><div class='slogan'>In unter einer Minute zu <b>deinem Ritual.</b></div><div class='btn'>Quiz starten →</div></div>")
    return page("Quiz Frage", st, fmt, body)

# ---------- 15 Glossar: MoodTech ----------
def ad_gloss_moodtech(fmt):
    st = "sleep"
    states = "".join(f"<div style='flex:1;text-align:center'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:14px;height:14px'></span><div class='lbl' style='font-size:18px;color:{S[s]['c']};margin-top:14px'>{S[s]['name']}</div></div>" for s in ("activate", "focus", "calm", "sleep"))
    body = (top(st, "dots")
      + "<div class='eyebrow grey'>Glossar · MoodTech</div>"
      + "<h1 style='font-size:94px;margin-top:18px'>Kein Parfum für andere.<br>Keine Kapsel zum Schlucken.<span class='acc'>Ein Duft für deinen Moment.</span></h1>"
      + "<div class='grow' style='min-height:30px'></div>"
      + "<div class='board glow' style='padding:38px 38px 34px'>"
        "<div style='font-size:30px;font-weight:300;letter-spacing:-.02em;line-height:1.35'>Düfte, die für einen bestimmten Moment deines Tages gemacht sind und als kurzes, wiederkehrendes Ritual genutzt werden.</div>"
        f"<div style='margin:30px 0 26px'>{signal_inline('sleep', 920, 60, 0.4)}</div><div style='display:flex'>{states}</div></div>"
      + "<div style='margin-top:24px;display:flex;justify-content:space-between;align-items:center'><div class='slogan' style='font-size:24px'>Mood on Demand. <b>Choose the moment.</b></div><div class='btn'>Momente entdecken &nbsp;→</div></div>")
    return page("Glossar MoodTech", st, fmt, body)

# ---------- 16 Glossar: Applied Scent Science ----------
def ad_gloss_science(fmt):
    st = "focus"
    items = [("Humanstudie", "Wir nennen nur Studien mit Menschen. Keine Tier- oder Laborstudien."),
             ("Einatmen, nicht einnehmen", "Nur Studien, in denen der Duft eingeatmet wurde."),
             ("Einzelöl und Mischung", "Die Studien wurden mit einzelnen Ölen gemacht, nicht mit unseren Mischungen. Das schreiben wir dazu.")]
    rows = "".join(f"<div style='padding:24px 0;border-top:1px solid rgba(13,27,51,.08)'><div style='display:flex;align-items:center;gap:14px'><span class='dot' style='width:10px;height:10px'></span>"
                   f"<span style='font-size:30px;letter-spacing:-.02em'>{t}</span></div><div style='font-size:22px;line-height:1.45;color:rgba(13,27,51,.68);margin-top:8px;padding-left:24px'>{d}</div></div>" for t, d in items)
    body = (top(st, "dots")
      + "<div class='eyebrow'>Applied Scent Science</div>"
      + "<h1 style='font-size:92px;margin-top:18px'>Wir sagen dir genau, was gemessen wurde.<span class='acc'>Und was nicht.</span></h1>"
      + "<div class='grow' style='min-height:30px'></div>"
      + f"<div class='board glow' style='padding:14px 38px 10px'>{rows}</div>"
      + "<div style='margin-top:26px'><div class='btn'>Zum Glossar →</div></div>")
    return page("Glossar Wissenschaft", st, fmt, body)


# ---------- Kompass wheel (full, "Ein Tag im Uhrzeigersinn") ----------
import math
def _pt(cx, cy, r, h):  # h in hours, 24 at top, clockwise
    a = math.radians(h * 15 - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)
def _arc(cx, cy, r, h0, h1):
    x0, y0 = _pt(cx, cy, r, h0); x1, y1 = _pt(cx, cy, r, h1)
    large = 1 if ((h1 - h0) % 24) * 15 > 180 else 0
    return f"M {x0:.1f} {y0:.1f} A {r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}"
def wheel_svg(size=900):
    cx = cy = size / 2; R1 = size * 0.432; R2 = size * 0.352; R3 = size * 0.322; Ro = size * 0.300; Ri = size * 0.150
    o = [f"<svg viewBox='0 0 {size} {size}' width='100%' style='display:block'>"]
    states = [("SLEEP", 21.2, 3.3, "#4E3D98", 0.15), ("ACTIVATE", 3.5, 10.3, "#B5471F", 7.0), ("FOCUS", 10.5, 14.8, "#1F4A3D", 12.6), ("CALM", 15.0, 21.0, "#2F6FA8", 18.0)]
    for name, a, b, col, lab in states:
        o.append(f"<path d='{_arc(cx,cy,R1,a,b)}' stroke='{col}' stroke-width='{size*0.015:.1f}' fill='none'/>")
        lx, ly = _pt(cx, cy, R1 + size * 0.036, lab)
        rot = lab * 15 if lab < 6 or lab > 18 else lab * 15 - 180
        o.append(f"<text x='{lx:.1f}' y='{ly:.1f}' font-family='Manrope' font-weight='600' font-size='{size*0.024:.1f}' letter-spacing='3' fill='{col}' text-anchor='middle' dominant-baseline='middle' transform='rotate({rot:.1f} {lx:.1f} {ly:.1f})'>{name}</text>")
    o.append(f"<circle cx='{cx}' cy='{cy}' r='{R2+size*0.012:.1f}' fill='none' stroke='rgba(13,27,51,.12)' stroke-width='1.5'/>")
    for h in range(24):
        x0, y0 = _pt(cx, cy, R2 + size * 0.012, h); x1, y1 = _pt(cx, cy, R2 + size * (0.03 if h % 3 == 0 else 0.022), h)
        o.append(f"<line x1='{x0:.1f}' y1='{y0:.1f}' x2='{x1:.1f}' y2='{y1:.1f}' stroke='rgba(13,27,51,{.5 if h%3==0 else .2})' stroke-width='{2 if h%3==0 else 1.2}'/>")
        if h % 3 == 0:
            tx, ty = _pt(cx, cy, R2 + size * 0.046, h)
            o.append(f"<text x='{tx:.1f}' y='{ty:.1f}' font-family='Manrope' font-size='{size*0.018:.1f}' fill='rgba(13,27,51,.5)' text-anchor='middle' dominant-baseline='middle'>{h if h else 24:02d}</text>")
    fams = [("Still", 0, "#4E3D98", [20, 22]), ("Geerdet", 3, "#6B4A3A", [21, 23]), ("Wach", 6, "#B5471F", [1, 6, 2, 7]), ("Klar", 9, "#B0963F", [3, 5, 4, 11]),
            ("Scharf", 12, "#1F4A3D", [9, 8, 10]), ("Warm", 15, "#7A2E2E", [13, 12]), ("Weich", 18, "#8C5A6E", [15, 16, 14]), ("Gelöst", 21, "#2F6FA8", [19, 18, 17])]
    for name, h, col, nums in fams:
        o.append(f"<path d='{_arc(cx,cy,R3,h-1.38,h+1.38)}' stroke='{col}' stroke-width='{size*0.009:.1f}' fill='none'/>")
        pts = [_pt(cx, cy, Ro, h - 1.5), _pt(cx, cy, Ro, h + 1.5), _pt(cx, cy, Ri, h + 1.5), _pt(cx, cy, Ri, h - 1.5)]
        o.append("<polygon points='" + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f"' fill='{col}' fill-opacity='.07' stroke='rgba(13,27,51,.12)' stroke-width='1.2'/>")
        lx, ly = _pt(cx, cy, Ro - size * 0.022, h)
        rot = h * 15 if (h <= 6 or h >= 18) else h * 15 - 180
        if h in (6, 18): rot = 90 if h == 6 else -90
        o.append(f"<text x='{lx:.1f}' y='{ly:.1f}' font-family='Manrope' font-size='{size*0.024:.1f}' fill='{col}' text-anchor='middle' dominant-baseline='middle' transform='rotate({rot:.1f} {lx:.1f} {ly:.1f})'>{name}</text>")
        n = len(nums)
        for i, num in enumerate(nums):
            rr = Ri + (Ro - Ri) * (0.28 + 0.27 * (i % 2)); hh = h + (i - (n - 1) / 2) * (0.78 if n > 2 else 0.95)
            x, y = _pt(cx, cy, rr, hh)
            o.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='{size*0.0225:.1f}' fill='{col}' stroke='#fff' stroke-width='3'/>"
                     f"<text x='{x:.1f}' y='{y+1:.1f}' font-family='Manrope' font-weight='600' font-size='{size*0.0175:.1f}' fill='#fff' text-anchor='middle' dominant-baseline='middle'>{num:02d}</text>")
    oct_pts = [_pt(cx, cy, Ri, h + 1.5) for h in range(0, 24, 3)]
    o.append("<polygon points='" + " ".join(f"{x:.1f},{y:.1f}" for x, y in oct_pts) + "' fill='#FBFAF7' stroke='rgba(13,27,51,.15)' stroke-width='1.5'/>")
    r = size * 0.06; sy = cy
    o.append(f"<circle cx='{cx}' cy='{sy}' r='{r:.1f}' fill='none' stroke='rgba(13,27,51,.25)' stroke-width='1.5'/>")
    o.append(f"<path d='M {cx} {sy-r*0.95:.1f} L {cx+r*0.16:.1f} {sy} L {cx} {sy+r*0.95:.1f} L {cx-r*0.16:.1f} {sy} Z' fill='#0D1B33'/>"
             f"<path d='M {cx-r*0.95:.1f} {sy} L {cx} {sy-r*0.16:.1f} L {cx+r*0.95:.1f} {sy} L {cx} {sy+r*0.16:.1f} Z' fill='#0D1B33'/>")
    o.append("</svg>")
    return "".join(o)

def ad_kompass_wheel(fmt):
    st = "focus"
    body = (top(st, "dots")
      + "<div class='lbl' style='color:var(--c);font-size:19px'><span class='dot' style='width:10px;height:10px;margin-right:14px'></span>Neurora Kompass · Mood on Demand</div>"
      + "<h1 style='margin-top:18px;font-size:82px'>Für alle, die mehr über ihren Duft <span style='color:var(--c)'>lernen wollen.</span></h1>"
      + "<div class='grow' style='min-height:20px'></div>"
      + f"<div class='board glow' style='padding:20px;margin-top:26px'><div style='width:760px;margin:0 auto'>{wheel_svg(900)}</div></div>"
      + "<div style='display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px'>"
        "<div></div>"
        "<div class='btn'>Zum Kompass &nbsp;→</div></div>")
    return page("Kompass", st, fmt, body)

# ---------- 12a VIDEO: Neurora Mood-Kompass ----------
KV_CSS = """
.w{display:inline-block}
.kbadge{display:inline-flex;align-items:center;gap:14px;background:#0D1B33;color:#F6F3EC;border-radius:999px;padding:14px 30px 14px 22px;font-size:24px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;
 box-shadow:0 0 0 7px color-mix(in srgb,var(--g) 40%,transparent),0 16px 30px -16px rgba(13,27,51,.55)}
.kh .l1{font-weight:300;letter-spacing:-.045em;line-height:1.04;display:block}
.kh .l2{font-family:'EB Garamond';font-style:italic;font-weight:400;letter-spacing:-.02em;line-height:1.04;color:var(--c);display:block}
.win{overflow:hidden;position:relative}
.facts{display:flex;justify-content:center;gap:12px;margin-top:14px}
.facts span{background:#fff;border-radius:999px;padding:10px 20px;font-size:23px;box-shadow:0 10px 24px -18px rgba(13,27,51,.5)}
.facts b{color:var(--c);font-weight:700}
.kcap{font-size:34px;font-weight:300;letter-spacing:-.025em;text-align:center;line-height:1.2}
.kcap b{font-weight:600;color:var(--c)}
body.anim .w{animation:wpop .45s cubic-bezier(.2,.9,.3,1.25) both}
body.anim .kb{animation:kbup .75s cubic-bezier(.65,0,.3,1) 1.55s both}
body.anim .kh{animation:khup .75s cubic-bezier(.65,0,.3,1) 3.25s both}
body.anim .kwb{animation:rin 1.2s cubic-bezier(.2,.8,.2,1) 3.75s both,kfade .9s ease 9.45s forwards}
@keyframes kfade{to{opacity:0}}
body.anim .kw path{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 3s cubic-bezier(.45,0,.2,1) 4.0s forwards}
body.anim .kw .inner{animation:fadein 1.6s ease 5.2s both}
body.anim .facts span{animation:cpop .6s cubic-bezier(.2,.9,.3,1.2) both}
body.anim .wininner{animation:swap 1.3s cubic-bezier(.65,0,.3,1) 9.4s both}
body.anim .kstrip{animation:slide 4.6s linear 9.4s both}
body.anim .kcta{animation:cpop .7s cubic-bezier(.2,.9,.3,1.2) 11.4s both}
@keyframes wpop{from{opacity:0;transform:translateY(16px) scale(.85)}to{opacity:1;transform:none}}
@keyframes kbup{from{transform:translateY(var(--dyb)) scale(1.45)}to{transform:none}}
@keyframes khup{from{transform:translateY(var(--dyh)) scale(1.12)}to{transform:none}}
@keyframes rin{from{opacity:0;scale:.9}to{opacity:1;scale:1}}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes fadein{from{opacity:0}to{opacity:1}}
@keyframes cpop{from{opacity:0;scale:.6}to{opacity:1;scale:1}}
@keyframes swap{from{transform:none}to{transform:translateY(var(--swap))}}
@keyframes slide{from{transform:translateX(var(--from))}to{transform:translateX(0)}}
body > svg{display:none}
"""

KV_JS = """<script>
window.__measure = function () {
  const H = innerHeight, mid = r => (r.top + r.bottom) / 2;
  const kb = document.querySelector('.kb'), kh = document.querySelector('.kh');
  kb.style.setProperty('--dyb', (H / 2 - mid(kb.getBoundingClientRect())) + 'px');
  kh.style.setProperty('--dyh', (H / 2 - mid(kh.getBoundingClientRect())) + 'px');
  const wb = document.querySelector('.kwb'), wi = document.querySelector('.wininner');
  const win = document.querySelector('.win').getBoundingClientRect().height, pr = document.querySelector('.kprod').getBoundingClientRect().height;
  wi.style.setProperty('--swap', -(wb.getBoundingClientRect().height + 30 - Math.max(0, (win - pr) / 2)) + 'px');
};
</script>"""

def ad_kompass_video(fmt):
    st = "focus"; tall = fmt == "916"
    def words(t, t0, step):
        ws = t.split(" "); return " ".join(f"<span class='w' style='animation-delay:{t0 + i * step:.2f}s'>{w}</span>" for i, w in enumerate(ws)), t0 + len(ws) * step
    bw, t = words("Der Neurora Mood-Kompass", 0.35, 0.26)
    badge = (f"<div style='text-align:center'><span class='kbadge kb'><span class='w' style='animation-delay:.15s;font-size:28px;letter-spacing:0'>✦</span>{bw}</span></div>")
    w1, t = words("Was steckt in", 1.9, 0.27); w2, _ = words("deinem Duft?", t + 0.05, 0.3)
    head = (f"<div class='kh' style='text-align:center;margin-top:22px'><span class='l1' style='font-size:{96 if tall else 88}px'>{w1}</span>"
            f"<span class='l2' style='font-size:{108 if tall else 100}px'>{w2}</span></div>")
    wsvg = wheel_svg(900).replace("<path d=", "<path pathLength='1' d=")
    # everything except the stroked arcs fades in as one layer
    first = wsvg.index("<polygon")
    wsvg = wsvg[:first] + "<g class='inner'>" + wsvg[first:].replace("</svg>", "</g></svg>")
    fx = [("23", "Duftmoleküle"), ("8", "Duftfamilien"), ("4", "Momente")]
    facts = "<div class='facts'>" + "".join(f"<span style='animation-delay:{7.3 + i * 0.45:.2f}s'><b>{n}</b> {l}</span>" for i, (n, l) in enumerate(fx)) + "</div>"
    wsize = 600 if tall else 560
    wheel_board = (f"<div class='kwb'><div class='kw' style='width:{wsize}px;margin:0 auto;filter:drop-shadow(0 30px 40px rgba(13,27,51,.10))'>{wsvg}</div>{facts}</div>")
    bleed = 78 if tall else 72; tw = 296; ih = 290 if tall else 262
    order = ("activate", "focus", "calm", "sleep")
    def tile(kind, s_):
        cc = S[s_]
        return (f"<div style='flex:none;width:{tw}px;background:#fff;border-radius:20px;padding:12px 8px 14px;text-align:center;box-shadow:0 12px 24px -22px rgba(13,27,51,.5)'>"
                f"<img src='{A}nr-{kind}-{s_}-cut.png' style='display:block;height:{ih}px;margin:0 auto;filter:drop-shadow(0 10px 10px rgba(13,27,51,.18))'>"
                f"<div style='display:flex;align-items:center;justify-content:center;gap:9px;margin-top:10px'><span class='dot' style='--c:{cc['c']};--g:{cc['g']};width:11px;height:11px'></span>"
                f"<span class='lbl' style='font-size:22px;color:{cc['c']}'>{cc['name']}</span></div>"
                f"<div style='font-size:21px;color:rgba(13,27,51,.55);margin-top:4px'>{'Textilspray' if kind == 'sbox' else 'Roll-On'}</div></div>")
    strip = "".join(tile("box", s_) for s_ in order) + "".join(tile("sbox", s_) for s_ in order)
    shift = int(1.5 * (tw + 14))
    products = (f"<div class='kprod' style='margin:0 -{bleed}px'><div class='kcap' style='padding:0 {bleed}px 22px'>Jeder Neurora-Duft hat<br><b>seinen Platz im Kompass.</b></div>"
                f"<div style='overflow:hidden;padding:6px 0 20px'><div class='kstrip' style='display:flex;gap:14px;width:max-content;--from:-{shift}px;transform:translateX(-{shift}px)'>{strip}</div></div>"
                f"<div style='text-align:center;margin-top:14px'><span class='btn kcta' style='font-size:30px;padding:30px 52px;min-height:100px'>Finde deinen Duft im Kompass&nbsp; →</span></div></div>")
    win_h = max(wsize + 80, ih + 330)
    window = (f"<div class='win' style='height:{win_h}px;margin:{26 if tall else 20}px -{bleed}px 0;padding:0 {bleed}px'>"
              f"<div class='wininner'>{wheel_board}<div style='height:30px'></div>{products}</div></div>")
    body = (top(st, "") + "<div class='grow'></div>" + badge + head + window + "<div class='grow'></div><i class='builtin'></i>" + KV_JS)
    return page("Mood-Kompass Video", st, fmt, body, KV_CSS)

ADS = [(d["key"], (lambda d: (lambda f: ad_ba(d, f)))(d)) for d in BA] + [
    ("04-founder-zitat", ad_founder), ("05-mission", ad_mission), ("06-calm-ein-atemzug", ad_atemzug),
    ("07-wo-hakt-dein-tag", ad_quiz_tiles), ("08-duft-wird-signal", ad_signal_steps), ("09-vier-momente", ad_vier_momente),
    ("10-erste-30-tage", ad_30), ("11-focus-angebot", ad_offer), ("12a-kompass-rad", ad_kompass_wheel), ("12b-kompass-scharf", ad_kompass),
    ("13-mood-quiz-intro", ad_quiz_intro), ("14-mood-quiz-frage", ad_quiz_q),
    ("15-glossar-moodtech", ad_gloss_moodtech), ("16-glossar-wissenschaft", ad_gloss_science)]

if __name__ == "__main__":
    for f in os.listdir(ROOT):
        if f.endswith(".html") and ("_45" in f or "_916" in f) and not f.startswith(("17", "18", "19", "v18", "v19")):
            os.remove(os.path.join(ROOT, f))   # 17-19 and v18/v19 belong to gen3.py
    for key, fn in ADS:
        for fmt in ("45", "916"):
            open(os.path.join(ROOT, f"{key}_{fmt}.html"), "w").write(fn(fmt))
    for fmt in ("45", "916"):
        open(os.path.join(ROOT, f"v12a-kompass-rad_{fmt}.html"), "w").write(ad_kompass_video(fmt))
    for d in BA:   # video-only layout, prefixed "v" so stills export ignores it
        for fmt in ("45", "916"):
            open(os.path.join(ROOT, f"v{d['key']}_{fmt}.html"), "w").write(ad_ba_video(d, fmt))
    print(len(ADS) * 2, "html files")
