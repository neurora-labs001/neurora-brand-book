#!/usr/bin/env python3
"""Round 3: 17 Gratis-Goodie + 18 Roll-On series (all four states), Brand Book 2.0 look."""
import math, os, sys
from gen import S, A, gesture_before, gesture_after, o_mark
from gen2 import page, top, DOTS

ROOT = os.path.dirname(os.path.abspath(__file__))
ORDER = ("activate", "focus", "calm", "sleep")

EXTRA = """
.badge{display:inline-flex;align-items:center;gap:12px;background:#0D1B33;color:#F6F3EC;border-radius:999px;padding:12px 24px 12px 18px;font-size:20px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}
.emo{font-family:'Noto Color Emoji';letter-spacing:0;font-style:normal}
h1 .it{letter-spacing:-.02em;font-weight:400}
.callout{white-space:nowrap;font-size:22px;line-height:1.3;font-weight:400;color:#0D1B33;z-index:4;padding:11px 15px;border-radius:18px;
 background:linear-gradient(150deg,rgba(255,255,255,.9),rgba(255,255,255,.66));border:1px solid rgba(255,255,255,.95);
 box-shadow:0 16px 30px -22px rgba(13,27,51,.45);backdrop-filter:blur(10px)}
.callout b{font-weight:700;color:var(--c)}
.comet{opacity:0}
body.anim .comet{opacity:1;animation:spin 11s linear infinite}
body.anim .hitdot{animation:hitdot 11s ease-out infinite}
body.anim .callout{animation:hitpill 11s ease-out infinite}
body.anim .prod{animation:pfloat 5.5s ease-in-out infinite}
@keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes hitdot{0%,100%{transform:scale(1)}5.5%{transform:scale(1.45)}14%{transform:scale(1)}}
@keyframes hitpill{0%,100%{transform:translateY(-50%) scale(1);box-shadow:0 16px 30px -22px rgba(13,27,51,.45)}
 5.5%{transform:translateY(-50%) scale(1.07);box-shadow:0 0 0 3px var(--c),0 18px 34px -16px color-mix(in srgb,var(--c) 60%,transparent)}
 16%{transform:translateY(-50%) scale(1);box-shadow:0 16px 30px -22px rgba(13,27,51,.45)}}
@keyframes pfloat{0%,100%{transform:var(--base) translateY(0)}50%{transform:var(--base) translateY(-9px)}}
.moodbar{height:8px;border-radius:99px;background:linear-gradient(90deg,#F6AE8E,#8AD3BD 35%,#A3CCF0 66%,#C5B0F3)}
"""

def emo(e):
    return f"<span class='emo'>{e}</span>"

# ---------- 17 Gratis-Goodie ----------
def ad_goodie(fmt):
    st = "sleep"
    tall = fmt == "916"
    tiles = "".join(
        f"<div style='flex:1;background:#fff;border-radius:22px;padding:10px 10px 16px;box-shadow:0 14px 30px -24px rgba(13,27,51,.45)'>"
        f"<img src='{A}nr-box-{s}.jpg' style='display:block;width:100%;aspect-ratio:1/{1.9 if tall else 1.55};object-fit:cover;border-radius:14px'>"
        f"<div style='display:flex;align-items:center;justify-content:center;gap:10px;margin-top:12px'>"
        f"<span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:11px;height:11px'></span>"
        f"<span class='lbl' style='color:{S[s]['c']}'>{S[s]['name']}</span></div></div>" for s in ORDER)
    body = (top(st, "dots")
      + "<div class='center'>"
        f"<span class='badge'>{emo('🎁')} Gratis-Goodie</span>"
        f"<h1 style='margin-top:26px;font-size:{104 if tall else 92}px'>Ein Roll-On<span class='acc it'>geht aufs Haus. {emo('🎁')}</span></h1>"
        "<p class='lead' style='margin:22px auto 0;max-width:820px'>Zu jedem Komplett-Set legen wir dir einen Roll-On deiner Wahl dazu. Du wählst den Moment.</p></div>"
      + f"<div class='board glow' style='margin-top:{40 if tall else 30}px;padding:26px 26px 28px'>"
        "<div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:18px'>"
        "<span class='lbl' style='color:rgba(13,27,51,.55)'>Dein Gratis-Moment</span><span class='moodbar' style='width:46%'></span></div>"
        f"<div style='display:flex;gap:14px'>{tiles}</div>"
        "<div style='display:flex;align-items:center;gap:18px;margin-top:22px;border:2px dashed #B9A6EE;border-radius:999px;padding:14px 26px 14px 14px;background:rgba(255,255,255,.7)'>"
        f"<span class='badge' style='font-size:18px;padding:10px 18px 10px 14px'>{emo('🎁')} Gratis</span>"
        "<span style='font-size:24px;flex:1'>Roll-On deiner Wahl</span>"
        "<span style='font-size:28px;font-weight:600'>€0,00</span><s style='font-size:21px;color:rgba(13,27,51,.5)'>€29,00</s></div></div>"
      + "<div class='grow'></div>"
      + "<div style='display:flex;align-items:center;justify-content:space-between;gap:24px;margin-top:26px'>"
        "<p class='it' style='font-size:26px;line-height:1.3;color:rgba(13,27,51,.65)'>Choose the moment.</p>"
        "<div class='btn'>Set wählen, Goodie sichern &nbsp;→</div></div>")
    return page("Gratis-Goodie", st, fmt, body, EXTRA)

# ---------- 18 Roll-On: Signal ring (all states) ----------
RO = {
    "activate": dict(sig="Dein Signal für den Morgen.", air="<b>Ein Atemzug</b><br>und der Tag beginnt"),
    "focus":    dict(sig="Dein Signal zum Abtauchen.", air="<b>Ein Atemzug</b><br>dann tauchst du ab"),
    "calm":     dict(sig="Dein Signal für den Feierabend.", air="<b>Ein Atemzug</b><br>ab jetzt ist Feierabend"),
    "sleep":    dict(sig="Dein Signal für die Nacht.", air="<b>Ein Atemzug</b><br>und der Tag ist vorbei"),
}

VT0 = 3.3     # video: comet starts
VSPIN = 7.0   # video: seconds per turn
LOOP = 11.0  # seconds: one full 360° turn of the signal comet

def comet(cx, cy, r, c):
    """Signal comet: bright head + fading tail on the ring. Hidden in stills, rotates in video (body.anim)."""
    segs = ""
    n = 14
    for i in range(n):
        a0 = -(i + 1) * 4.2; a1 = -i * 4.2           # tail behind the head (head at 0° = top)
        p0 = (cx + r * math.sin(math.radians(a0)), cy - r * math.cos(math.radians(a0)))
        p1 = (cx + r * math.sin(math.radians(a1)), cy - r * math.cos(math.radians(a1)))
        segs += (f"<path d='M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}' fill='none' stroke='{c['c']}' "
                 f"stroke-opacity='{(1 - i / n) ** 1.6:.2f}' stroke-width='{5 - 3 * i / n:.1f}' stroke-linecap='round'/>")
    head = (f"<circle cx='{cx}' cy='{cy - r}' r='16' fill='{c['g']}' opacity='.55'/>"
            f"<circle cx='{cx}' cy='{cy - r}' r='7' fill='#fff' stroke='{c['c']}' stroke-width='3'/>")
    return f"<g class='comet' style='transform-origin:{cx}px {cy}px'>{segs}{head}</g>"

def ring(st, W, D, bottle=False, video=False):
    c = S[st]; r = D / 2; cx = W / 2; cy = r + 30; H = D + 60
    def pt(deg):
        a = math.radians(deg); return cx + r * math.sin(a), cy - r * math.cos(a)
    def arc(d0, d1):
        x0, y0 = pt(d0); x1, y1 = pt(d1)
        return f"M {x0:.1f} {y0:.1f} A {r} {r} 0 {1 if (d1 - d0) % 360 > 180 else 0} 1 {x1:.1f} {y1:.1f}"
    calls = [(326, "<b>Duft mit Funktion</b><br>wissenschaftliche Formel"), (214, "<b>Immer dabei</b><br>10 ml für jede Tasche"), (34, RO[st]["air"]), (146, "<b>30 Tage testen</b><br>Passt nicht? Geld zurück.")]
    # layer 0: dense state-colour disc
    disc = (f"<div style='position:absolute;left:{cx - r}px;top:{cy - r}px;width:{D}px;height:{D}px;border-radius:50%;"
            f"background:radial-gradient(circle at 30% 22%,rgba(255,255,255,.9) 0%,rgba(255,255,255,0) 42%),"
            f"radial-gradient(circle at 78% 88%,color-mix(in srgb,{c['c']} 22%,transparent) 0%,transparent 55%),"
            f"radial-gradient(circle at 50% 50%,color-mix(in srgb,{c['g']} 38%,#F7F4EE) 0%,color-mix(in srgb,{c['g']} 62%,#F7F4EE) 58%,color-mix(in srgb,{c['g']} 85%,{c['c']}) 100%);"
            f"border:1.5px solid rgba(255,255,255,.85);"
            f"box-shadow:inset 0 0 0 9px rgba(255,255,255,.22),inset 0 -40px 70px -30px color-mix(in srgb,{c['c']} 30%,transparent),"
            f"0 0 110px 0 color-mix(in srgb,{c['g']} 50%,transparent),0 50px 90px -55px rgba(13,27,51,.45)'></div>")
    # layer 1 (behind the product): ring, arcs and the filigree Signal Line
    ly = cy + r * 0.30; x0 = cx - r; x1 = cx + r; ox = cx - r * (0.47 if bottle else 0.72)
    d1 = f"M {x0:.1f} {ly:.1f}" + gesture_before(st, x0, ox - 16, ly)
    d2 = f"M {ox + 16:.1f} {ly:.1f}" + gesture_after(st, ox + 16, x1, ly)
    back = (f"<svg width='{W}' height='{H}' style='position:absolute;left:0;top:0;z-index:1;overflow:visible'>"
            f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{c['c']}' stroke-opacity='.28' stroke-width='2'/>"
            f"<defs><linearGradient id='ag' x1='0' x2='1'><stop offset='0' stop-color='{c['c']}' stop-opacity='.55'/><stop offset='.5' stop-color='{c['c']}'/><stop offset='1' stop-color='{c['c']}' stop-opacity='.55'/></linearGradient></defs>"
            f"<path d='{arc(316, 44)}' fill='none' stroke='url(#ag)' stroke-width='3.2' stroke-linecap='round'/>"
            f"<path d='{arc(136, 224)}' fill='none' stroke='url(#ag)' stroke-width='3.2' stroke-linecap='round'/>"
            + comet(cx, cy, r, c) +
            f"<defs><clipPath id='dc'><circle cx='{cx}' cy='{cy}' r='{r - 3}'/></clipPath></defs><g clip-path='url(#dc)'>"
            f"<path d='{d1}' fill='none' stroke='#fff' stroke-opacity='.85' stroke-width='1.6' stroke-linecap='round'/>"
            f"<path d='{d2}' fill='none' stroke='{c['c']}' stroke-width='1.8' stroke-linecap='round'/>"
            f"{o_mark(round(ox), round(ly), st, 11)}</g></svg>")
    # layer 2: product
    if bottle:
        bh = D * 0.84
        img = (f"<img src='{A}nr-rollon-{st}-cut.png' style='position:absolute;left:50%;top:{cy - bh / 2 - 6:.0f}px;height:{bh:.0f}px;"
               f"--base:translateX(-50%) rotate(9deg);transform:var(--base);z-index:2;filter:drop-shadow(0 36px 34px rgba(13,27,51,.28))' class='prod'>")
    else:
        bh = D * 0.9
        img = (f"<img src='{A}nr-box-{st}-cut.png' style='position:absolute;left:50%;top:{cy - bh / 2 + 6:.0f}px;height:{bh:.0f}px;"
               f"--base:translateX(-50%);transform:var(--base);z-index:2;filter:drop-shadow(0 34px 30px rgba(13,27,51,.30)) drop-shadow(0 4px 6px rgba(13,27,51,.15))' class='prod'>")
    # layer 3/4: callout dots and labels
    dots = f"<svg width='{W}' height='{H}' style='position:absolute;left:0;top:0;z-index:3;overflow:visible'>"
    labels = ""
    for deg, t in calls:
        x, y = pt(deg)
        dl = (f"animation-delay:{VT0 + deg / 360 * VSPIN - 0.33:.2f}s" if video else f"animation-delay:{deg / 360 * LOOP - 0.45 - LOOP:.2f}s")
        vh = " vhit" if video else ""
        dots += (f"<g class='hitdot{vh}' style='transform-origin:{x:.1f}px {y:.1f}px;{dl}'>"
                 f"<circle cx='{x:.1f}' cy='{y:.1f}' r='22' fill='{c['g']}' opacity='.45'/>"
                 f"<circle cx='{x:.1f}' cy='{y:.1f}' r='13' fill='#fff'/>"
                 f"<circle cx='{x:.1f}' cy='{y:.1f}' r='8' fill='{c['c']}'/></g>")
        left = deg > 180; gap = 28
        style = (f"right:{W - x + gap:.0f}px;text-align:right" if left else f"left:{x + gap:.0f}px")
        labels += (f"<div class='callout{vh}' style='position:absolute;{style};top:{y:.0f}px;transform:translateY(-50%);max-width:{x - gap if left else W - x - gap:.0f}px;"
                   f"transform-origin:{'right' if left else 'left'} center;{dl}'>{t}</div>")
    dots += "</svg>"
    return f"<div class='ringwrap' style='position:relative;width:{W}px;height:{H}px;margin:0 auto'><div class='ringbody'>{disc}{back}{img}</div>{dots}{labels}</div>"

def ad_rollon(st, fmt, bottle=False):
    c = S[st]; tall = fmt == "916"
    W = 924 if tall else 936
    D = 560
    body = (top(st, "dots")
      + "<div class='center'>"
        f"<div class='eyebrow'>{c['name']} · Roll-On</div>"
        f"<h1 style='margin-top:16px;font-size:{78 if tall else 72}px'>Ein Duft. Ein Moment.<span class='acc it'>{RO[st]['sig']}</span></h1>"
        "<p class='lead' style='margin-top:18px;font-size:24px'>Aus Gewohnheit wird Ritual. Aus Ritual wird dein Signal.</p></div>"
      + "<div class='grow'></div>" + ring(st, W, D, bottle) + "<div class='grow'></div>"
      + "<div style='display:flex;align-items:center;justify-content:space-between;gap:24px'>"
        f"<div><div class='lbl' style='color:var(--c)'>{c['name']} Roll-On</div><div style='font-size:24px;margin-top:6px;color:rgba(13,27,51,.7)'>10 ml · €29</div></div>"
        "<div class='btn'>Jetzt entdecken &nbsp;→</div></div>")
    return page(f"{c['name']} Roll-On", st, fmt, body, EXTRA + "body > svg{display:none}")

HEAD = {"activate": ("Nie wieder", "Morgenmuffel!"), "focus": ("Schluss mit", "Tab-Chaos!"),
        "calm": ("Feierabend?", "Kopf macht Überstunden."), "sleep": ("Schluss mit", "Kopfkino im Bett!")}

VR_CSS = """
.hd{text-align:center}
.hd .l1{font-weight:300;letter-spacing:-.045em;line-height:1.02;display:block}
.hd .l2{font-family:'EB Garamond';font-style:italic;font-weight:400;letter-spacing:-.02em;line-height:1.02;color:var(--c);display:block}
.w{display:inline-block}
.pname{text-align:center}
.pname .st{font-weight:700;letter-spacing:.14em;color:var(--c)}
.pname .it{color:#0D1B33}
.comet{opacity:0}
body.anim .w{animation:wpop .45s cubic-bezier(.2,.9,.3,1.25) both}
body.anim .hd{animation:hdup .8s cubic-bezier(.65,0,.3,1) 1.75s both}
body.anim .ringbody{animation:rin .9s cubic-bezier(.2,.8,.2,1) 2.3s both}
body.anim .comet{animation:fadein .4s ease 3.1s both,spin 7s linear 3.3s infinite}
body.anim .hitdot.vhit{animation:cdot .5s cubic-bezier(.3,1.6,.5,1) both,hitdot 7s ease-out infinite}
body.anim .callout.vhit{animation:cpop .65s cubic-bezier(.2,.9,.3,1.2) both,hitpill 7s ease-out infinite}
body.anim .pname{animation:pnin .9s cubic-bezier(.2,.8,.2,1) 10.3s both}
body.anim .pname path{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 1.4s cubic-bezier(.45,0,.2,1) 10.7s forwards}
@keyframes wpop{from{opacity:0;transform:translateY(16px) scale(.85)}to{opacity:1;transform:none}}
@keyframes hdup{from{transform:translateY(var(--dyh)) scale(1.12)}to{transform:none}}
@keyframes rin{from{opacity:0;scale:.86}to{opacity:1;scale:1}}
@keyframes fadein{from{opacity:0}to{opacity:1}}
@keyframes cdot{from{opacity:0;scale:0}to{opacity:1;scale:1}}
@keyframes cpop{from{opacity:0;scale:.6}to{opacity:1;scale:1}}
@keyframes pnin{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}
@keyframes draw{to{stroke-dashoffset:0}}
body > svg{display:none}
.callout{font-size:21px;line-height:1.3;padding:12px 18px}
.callout b{font-size:27px;line-height:1.2;display:inline-block;margin-bottom:3px}
"""

VR_JS = """<script>
window.__measure = function () {
  const hd = document.querySelector('.hd'); const r = hd.getBoundingClientRect();
  hd.style.setProperty('--dyh', (innerHeight / 2 - (r.top + r.bottom) / 2) + 'px');
};
</script>"""

def ad_rollon_video(st, fmt, bottle=False):
    c = S[st]; tall = fmt == "916"
    W = 924 if tall else 936; D = 560 if tall else 500
    l1, l2 = HEAD[st]
    def words(t, t0, step=0.3):
        out = []
        for i, w in enumerate(t.split(" ")):
            out.append(f"<span class='w' style='animation-delay:{t0 + i * step:.2f}s'>{w}</span>")
        return " ".join(out), t0 + len(t.split(" ")) * step
    w1, t = words(l1, 0.25); w2, _ = words(l2, t + 0.05)
    hd = (f"<div class='hd'><span class='l1' style='font-size:{108 if tall else 100}px'>{w1}</span>"
          f"<span class='l2' style='white-space:nowrap;font-size:{min(120 if tall else 112, int((860 if tall else 880) / (len(l2) * 0.43)))}px'>{w2}</span></div>")
    uw = 520; uy = 26
    ul = (f"<svg width='{uw}' height='60' viewBox='0 0 {uw} 60' style='display:block;margin:8px auto 0;overflow:visible'>"
          f"<path pathLength='1' d='M 4 {uy}" + gesture_after(st, 4, uw - 4, uy) + f"' fill='none' stroke='{c['c']}' stroke-width='4' stroke-linecap='round'/></svg>")
    pname = (f"<div class='pname'><span class='st' style='font-size:{58 if tall else 54}px'>{c['name']}</span>&nbsp; "
             f"<span class='it' style='font-family:\"EB Garamond\";font-style:italic;font-size:{76 if tall else 70}px'>Roll-On</span>{ul}</div>")
    body = (top(st, "") + "<div class='grow'></div>" + hd + "<div class='grow'></div>"
            + ring(st, W, D, bottle, video=True) + "<div class='grow'></div>" + pname + "<div class='grow'></div>" + VR_JS)
    return page(f"{c['name']} Roll-On Video", st, fmt, body, EXTRA + VR_CSS)

ADS3 = [("17-gratis-goodie", ad_goodie)] + [
    (f"18{l}-rollon-{s}", (lambda s: (lambda f: ad_rollon(s, f)))(s)) for l, s in zip("abcd", ORDER)] + [
    (f"19{l}-rollon-signal-{s}", (lambda s: (lambda f: ad_rollon(s, f, True)))(s)) for l, s in zip("abcd", ORDER)]

if __name__ == "__main__":
    for key, fn in ADS3:
        for fmt in ("45", "916"):
            open(os.path.join(ROOT, f"{key}_{fmt}.html"), "w").write(fn(fmt))
    for l, s_ in zip("abcd", ORDER):
        for fmt in ("45", "916"):
            open(os.path.join(ROOT, f"v18{l}-rollon-{s_}_{fmt}.html"), "w").write(ad_rollon_video(s_, fmt, False))
            open(os.path.join(ROOT, f"v19{l}-rollon-signal-{s_}_{fmt}.html"), "w").write(ad_rollon_video(s_, fmt, True))
    print(len(ADS3) * 2, "html files")
