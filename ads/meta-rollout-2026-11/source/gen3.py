#!/usr/bin/env python3
"""Round 3: 17 Gratis-Goodie + 18 Roll-On series (all four states), Brand Book 2.0 look."""
import math, os, sys
from gen import S, A
from gen2 import page, top, DOTS

ROOT = os.path.dirname(os.path.abspath(__file__))
ORDER = ("activate", "focus", "calm", "sleep")

EXTRA = """
.badge{display:inline-flex;align-items:center;gap:12px;background:#0D1B33;color:#F6F3EC;border-radius:999px;padding:12px 24px 12px 18px;font-size:20px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}
.emo{font-family:'Noto Color Emoji';letter-spacing:0;font-style:normal}
h1 .it{letter-spacing:-.02em;font-weight:400}
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
    "activate": dict(sig="Dein Signal für den Morgen.", air="Dein Morgen zum Einatmen"),
    "focus":    dict(sig="Dein Signal zum Abtauchen.", air="Dein Fokus zum Einatmen"),
    "calm":     dict(sig="Dein Signal für den Feierabend.", air="Dein Feierabend zum Einatmen"),
    "sleep":    dict(sig="Dein Signal für die Nacht.", air="Dein Abend zum Einatmen"),
}

def ring(st, W, D):
    c = S[st]; r = D / 2; cx = W / 2; cy = r + 30; H = D + 60
    def pt(deg):
        a = math.radians(deg); return cx + r * math.sin(a), cy - r * math.cos(a)
    def arc(d0, d1):
        x0, y0 = pt(d0); x1, y1 = pt(d1)
        return f"M {x0:.1f} {y0:.1f} A {r} {r} 0 {1 if (d1 - d0) % 360 > 180 else 0} 1 {x1:.1f} {y1:.1f}"
    calls = [(305, "Rund 95 Rituale pro Roll-On"), (235, "10 ml für jede Tasche"), (55, RO[st]["air"]), (125, "30 Tage testen, Geld zurück")]
    svg = (f"<svg width='{W}' height='{H}' style='position:absolute;left:0;top:0;z-index:2;overflow:visible'>"
           f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{c['c']}' stroke-opacity='.28' stroke-width='2'/>"
           f"<path d='{arc(305, 55)}' fill='none' stroke='{c['c']}' stroke-width='3.5' stroke-linecap='round'/>"
           f"<path d='{arc(125, 235)}' fill='none' stroke='{c['g']}' stroke-width='3.5' stroke-linecap='round'/>")
    labels = ""
    for deg, t in calls:
        x, y = pt(deg)
        svg += (f"<circle cx='{x:.1f}' cy='{y:.1f}' r='17' fill='{c['g']}' opacity='.45'/>"
                f"<circle cx='{x:.1f}' cy='{y:.1f}' r='8' fill='{c['c']}' stroke='#fff' stroke-width='3'/>")
        left = deg > 180
        style = (f"right:{W - x + 30:.0f}px;text-align:right" if left else f"left:{x + 30:.0f}px")
        labels += (f"<div style='position:absolute;{style};top:{y:.0f}px;transform:translateY(-50%);max-width:{x - 30 if left else W - x - 30:.0f}px;"
                   f"font-size:23px;line-height:1.3;font-weight:500;z-index:3'>{t}</div>")
    svg += "</svg>"
    disc = (f"<div style='position:absolute;left:{cx - r + 4}px;top:{cy - r + 4}px;width:{D - 8}px;height:{D - 8}px;border-radius:50%;"
            f"background:radial-gradient(circle at 50% 42%,#fff 0%,color-mix(in srgb,{c['g']} 30%,#fff) 62%,color-mix(in srgb,{c['g']} 55%,#fff) 100%);"
            f"box-shadow:0 40px 80px -50px rgba(13,27,51,.45)'></div>")
    bh = D + 40
    img = (f"<img src='{A}nr-box-{st}-cut.png' style='position:absolute;left:50%;transform:translateX(-50%);top:{cy - bh / 2 + 4:.0f}px;height:{bh}px;"
           f"z-index:1;filter:drop-shadow(0 30px 40px rgba(13,27,51,.18))'>")
    return f"<div style='position:relative;width:{W}px;height:{H}px;margin:0 auto'>{disc}{img}{svg}{labels}</div>"

def ad_rollon(st, fmt):
    c = S[st]; tall = fmt == "916"
    W = 924 if tall else 936
    D = 640 if tall else 600
    body = (top(st, "dots")
      + "<div class='center'>"
        f"<div class='eyebrow'>{c['name']} · Roll-On</div>"
        f"<h1 style='margin-top:16px;font-size:{78 if tall else 72}px'>Ein Duft. Ein Moment.<span class='acc it'>{RO[st]['sig']}</span></h1>"
        "<p class='lead' style='margin-top:18px;font-size:24px'>Aus Gewohnheit wird Ritual. Aus Ritual wird dein Signal.</p></div>"
      + "<div class='grow'></div>" + ring(st, W, D) + "<div class='grow'></div>"
      + "<div style='display:flex;align-items:center;justify-content:space-between;gap:24px'>"
        f"<div><div class='lbl' style='color:var(--c)'>{c['name']} Roll-On</div><div style='font-size:24px;margin-top:6px;color:rgba(13,27,51,.7)'>10 ml · €29</div></div>"
        "<div class='btn'>Jetzt entdecken &nbsp;→</div></div>")
    return page(f"{c['name']} Roll-On", st, fmt, body, EXTRA)

ADS3 = [("17-gratis-goodie", ad_goodie)] + [
    (f"18{l}-rollon-{s}", (lambda s: (lambda f: ad_rollon(s, f)))(s)) for l, s in zip("abcd", ORDER)]

if __name__ == "__main__":
    for key, fn in ADS3:
        for fmt in ("45", "916"):
            open(os.path.join(ROOT, f"{key}_{fmt}.html"), "w").write(fn(fmt))
    print(len(ADS3) * 2, "html files")
