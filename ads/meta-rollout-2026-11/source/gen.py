#!/usr/bin/env python3
"""Generate Neurora Meta ad HTML (4:5 and 9:16) from the live webshop sections."""
import os, re, html as H

ROOT = os.path.dirname(os.path.abspath(__file__))
A = "assets/"

S = {  # state tokens (Brand Book 2.0)
    "activate": dict(c="#B5471F", g="#F6AE8E", soft="#F6E9E1", name="ACTIVATE"),
    "focus":    dict(c="#1F4A3D", g="#8AD3BD", soft="#EAF3EE", name="FOCUS"),
    "calm":     dict(c="#2F6FA8", g="#A3CCF0", soft="#EAF2FB", name="CALM"),
    "sleep":    dict(c="#4E3D98", g="#C5B0F3", soft="#F0EDF9", name="SLEEP"),
}

def svg_logo(kind, color="#0D1B33", h=None, w=None):
    s = open(os.path.join(ROOT, A, f"logo-{kind}.svg")).read()
    s = s.replace("id='a'", f"id='{kind}a'").replace("id='b'", f"id='{kind}b'")
    s = s.replace("url(%23a)", f"url(#{kind}a)").replace("url(%23b)", f"url(#{kind}b)")
    s = s.replace("url(#a)", f"url(#{kind}a)").replace("url(#b)", f"url(#{kind}b)")
    style = ""
    if h: style += f"height:{h}px;"
    if w: style += f"width:{w}px;"
    return s.replace("<svg ", f"<svg fill='{color}' style='display:block;{style}' ", 1)

# ---------- Signal Line ----------
def gesture_before(kind, x0, x1, y):
    """Left (before) part of the Signal Line, from x0 to x1 at baseline y."""
    n = 6; step = (x1 - x0) / n; d = ""
    if kind == "sleep":
        for i in range(n):
            a = x0 + i * step
            d += f" Q {a+step*0.25:.1f} {y-16:.1f} {a+step*0.5:.1f} {y:.1f} Q {a+step*0.75:.1f} {y+16:.1f} {a+step:.1f} {y:.1f}"
    elif kind == "calm":
        for i in range(n):
            a = x0 + i * step
            d += (f" C {a+step*0.15:.1f} {y-30:.1f} {a+step*0.85:.1f} {y-30:.1f} {a+step*0.9:.1f} {y-6:.1f}"
                  f" C {a+step*0.95:.1f} {y+10:.1f} {a+step*0.6:.1f} {y+12:.1f} {a+step*0.7:.1f} {y:.1f}"
                  f" L {a+step:.1f} {y:.1f}")
    elif kind == "focus":
        for i in range(n):
            a = x0 + i * step
            d += f" L {a+step*0.5:.1f} {y-18:.1f} L {a+step:.1f} {y+10:.1f}"
    else:  # activate: flat and low
        d += f" L {x1:.1f} {y+8:.1f}"
    return d

def gesture_after(kind, x0, x1, y):
    w = x1 - x0
    if kind == "sleep":
        return (f" C {x0+w*0.15:.1f} {y-14:.1f} {x0+w*0.3:.1f} {y+12:.1f} {x0+w*0.5:.1f} {y+18:.1f}"
                f" S {x0+w*0.85:.1f} {y+28:.1f} {x1:.1f} {y+30:.1f}")
    if kind == "calm":
        return (f" C {x0+w*0.25:.1f} {y-36:.1f} {x0+w*0.45:.1f} {y-36:.1f} {x0+w*0.6:.1f} {y+4:.1f}"
                f" S {x0+w*0.9:.1f} {y-22:.1f} {x1:.1f} {y-18:.1f}")
    if kind == "focus":
        return f" L {x1:.1f} {y:.1f}"
    return (f" L {x0+w*0.2:.1f} {y:.1f} C {x0+w*0.28:.1f} {y:.1f} {x0+w*0.3:.1f} {y-34:.1f} {x0+w*0.36:.1f} {y-34:.1f}"
            f" C {x0+w*0.42:.1f} {y-34:.1f} {x0+w*0.4:.1f} {y-14:.1f} {x0+w*0.5:.1f} {y-14:.1f} L {x1:.1f} {y-14:.1f}")

def o_mark(cx, cy, st, r=17):
    c = S[st]
    return (f"<circle cx='{cx}' cy='{cy}' r='{r+9}' fill='{c['g']}' opacity='.25'/>"
            f"<path d='M {cx-r*0.35:.1f} {cy-r*0.94:.1f} A {r} {r} 0 1 0 {cx+r*0.35:.1f} {cy-r*0.94:.1f}' fill='none' stroke='{c['c']}' stroke-width='3' stroke-linecap='round'/>"
            f"<circle cx='{cx}' cy='{cy}' r='{r*0.45:.1f}' fill='{c['g']}'/>")

def signal_bridge(st, W, top=20, drop=120, lx=None, rx=None):
    """Signal Line that starts in the 'Ohne Signal' card and ends in the 'Mit' card."""
    c = S[st]; y = top + 18
    lx = lx or W * 0.25; rx = rx or W * 0.75; ox = W * 0.48
    before = f"M {lx:.1f} {top+drop:.1f} L {lx:.1f} {y+16:.1f} Q {lx:.1f} {y:.1f} {lx+18:.1f} {y:.1f}" + gesture_before(st, lx + 18, ox - 26, y)
    after = f"M {ox+26:.1f} {y:.1f}" + gesture_after(st, ox + 26, rx - 22, y) + f" Q {rx:.1f} {y+(30 if st=='sleep' else 0):.1f} {rx:.1f} {y+40:.1f} L {rx:.1f} {top+drop:.1f}"
    return (f"<svg class='bridge' viewBox='0 0 {W} {top+drop+14}' width='{W}' height='{top+drop+14}'>"
            f"<path d='{before}' fill='none' stroke='{c['c']}' stroke-opacity='.45' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/>"
            f"<path d='{after}' fill='none' stroke='{c['c']}' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/>"
            f"<circle cx='{lx}' cy='{top+drop}' r='6' fill='#FAF9F6' stroke='{c['c']}' stroke-opacity='.5' stroke-width='2'/>"
            f"<circle cx='{rx}' cy='{top+drop}' r='8' fill='{c['c']}'/><circle cx='{rx}' cy='{top+drop}' r='14' fill='{c['g']}' opacity='.35'/>"
            f"{o_mark(ox, y, st)}</svg>")

def signal_inline(st, W, H=70, ox_frac=0.36, color=None):
    c = S[st]; y = H / 2; ox = W * ox_frac
    col = color or c["c"]
    before = f"M 4 {y}" + gesture_before(st, 4, ox - 24, y)
    after = f"M {ox+24:.1f} {y}" + gesture_after(st, ox + 24, W - 4, y)
    return (f"<svg viewBox='0 0 {W} {H}' width='{W}' height='{H}' style='display:block;overflow:visible'>"
            f"<path d='{before}' fill='none' stroke='{col}' stroke-opacity='.5' stroke-width='2' stroke-linecap='round'/>"
            f"<path d='{after}' fill='none' stroke='{col}' stroke-width='2.8' stroke-linecap='round'/>{o_mark(ox, y, st, 13)}</svg>")

# ---------- Shared CSS ----------
CSS = """
@font-face{font-family:Manrope;src:url(fonts/Manrope-VariableFont_wght.ttf) format('truetype');font-weight:200 800}
@font-face{font-family:'EB Garamond';font-style:italic;src:url(fonts/EBGaramond-Italic.woff2) format('woff2')}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:var(--H);overflow:hidden}
body{font-family:Manrope,sans-serif;color:#0D1B33;background:#F1EEE8;-webkit-font-smoothing:antialiased;position:relative}
body::before{content:"";position:absolute;inset:0;z-index:0;background:
 radial-gradient(620px 520px at 104% -4%, color-mix(in srgb,var(--g) 42%,transparent),transparent 70%),
 radial-gradient(560px 520px at -8% 108%, color-mix(in srgb,var(--g) 22%,transparent),transparent 70%)}
.wrap{position:relative;z-index:1;height:100%;display:flex;flex-direction:column;padding:var(--pad)}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:var(--gap)}
.slogan{font-size:21px;font-weight:300;letter-spacing:-.01em;color:rgba(13,27,51,.7)}
.slogan b{font-family:'EB Garamond';font-style:italic;font-weight:400;color:var(--c);font-size:24px}
.eyebrow{font-size:17px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--c)}
.eyebrow.grey{color:rgba(13,27,51,.55)}
h1{font-weight:300;letter-spacing:-.045em;line-height:1.02;font-size:var(--h1)}
h1 .acc{color:var(--c);display:block}
.lead{font-size:var(--lead);line-height:1.5;color:rgba(13,27,51,.72);letter-spacing:-.005em}
.panel{background:rgba(251,250,247,.86);border:1px solid rgba(255,255,255,.95);border-radius:36px;box-shadow:0 30px 60px -40px rgba(13,27,51,.35),0 2px 6px -4px rgba(13,27,51,.1)}
.board{background:rgba(255,255,255,.7);border:1px solid rgba(255,255,255,.95);border-radius:24px;box-shadow:0 22px 50px -32px rgba(13,27,51,.3),0 2px 6px -4px rgba(13,27,51,.1);backdrop-filter:blur(14px)}
.dot{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--c);box-shadow:0 0 0 5px color-mix(in srgb,var(--g) 45%,transparent),0 0 16px 3px color-mix(in srgb,var(--g) 80%,transparent);vertical-align:middle}
.lbl{font-size:15px;font-weight:600;letter-spacing:.18em;text-transform:uppercase}
.it{font-family:'EB Garamond';font-style:italic;font-weight:400}
.chip{display:flex;align-items:center;gap:20px;background:#fff;border-radius:22px;padding:14px 22px 14px 14px;box-shadow:0 12px 30px -22px rgba(13,27,51,.35)}
.chip img{width:84px;height:84px;object-fit:cover;border-radius:14px}
.chip .t{font-size:24px;font-weight:600;letter-spacing:-.01em}
.chip .s{font-size:18px;color:rgba(13,27,51,.55);margin-top:4px}
.chip .arr{margin-left:auto;font-size:34px;color:var(--c);font-weight:300}
.btn{display:inline-flex;align-items:center;gap:14px;background:#0D1B33;color:#F6F3EC;border-radius:999px;padding:22px 36px;font-size:24px;font-weight:600}
.grow{flex:1}
/* before / after */
.ba .cards{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:stretch}
.ba .card{border-radius:26px;padding:26px 24px;display:flex;flex-direction:column}
.ba .off{background:#F2F1EE;border:1px solid rgba(13,27,51,.06)}
.ba .on{background:var(--soft);border:1px solid color-mix(in srgb,var(--c) 14%,transparent)}
.ba .ct{font-size:var(--ct);font-weight:300;letter-spacing:-.035em;line-height:1.1;margin:12px 0 10px}
.ba .off .ct{color:rgba(13,27,51,.78)} .ba .on .ct{color:var(--c)}
.ba .row{display:grid;grid-template-columns:62px 1fr;gap:10px;padding:13px 0;border-bottom:1px solid rgba(13,27,51,.07);font-size:var(--row);line-height:1.38}
.ba .row:last-child{border-bottom:0}
.ba .row .tm{font-size:15px;font-weight:600;letter-spacing:.04em;color:rgba(13,27,51,.5);padding-top:4px;font-variant-numeric:tabular-nums}
.ba .on .row .tm{color:var(--c)}
.ba .off .row span:last-child{color:rgba(13,27,51,.72)}
.ba .why{background:#121B33;color:#F6F3EC;border-radius:20px;padding:20px 20px;margin-top:14px}
.ba .why .lbl{color:var(--g);font-size:13px}
.ba .why .h{font-size:var(--why);font-weight:300;letter-spacing:-.02em;line-height:1.18;margin:8px 0 8px}
.ba .why p{font-size:var(--whyp);line-height:1.45;color:rgba(246,243,236,.72)}
.ba .warn{display:inline-flex;align-items:center;gap:10px;color:rgba(13,27,51,.55)}
.ba .warn i{width:24px;height:24px;border-radius:50%;border:1.5px solid rgba(13,27,51,.4);display:grid;place-items:center;font-style:normal;font-size:14px}
"""

def page(title, st, fmt, body, extra_css=""):
    c = S[st]
    Hh = 1350 if fmt == "45" else 1920
    vars_ = (f"--H:{Hh}px;--c:{c['c']};--g:{c['g']};--soft:{c['soft']};"
             + ("--pad:64px 60px 56px;--gap:34px;--h1:84px;--lead:24px;--ct:30px;--row:19.5px;--why:24px;--whyp:16.5px;" if fmt == "45" else
                "--pad:120px 60px 110px;--gap:48px;--h1:96px;--lead:27px;--ct:34px;--row:22px;--why:27px;--whyp:18.5px;"))
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{H.escape(title)}</title>"
            f"<style>:root{{{vars_}}}{CSS}{extra_css}</style></head><body class='f{fmt}'><div class='wrap'>{body}</div></body></html>")

def topbar(st, right=None):
    r = right if right is not None else f"<div class='slogan'>Choose the <b>moment.</b></div>"
    return f"<div class='top'>{svg_logo('lockup', h=46)}{r}</div>"

def foot(st):
    return f"<div style='display:flex;justify-content:space-between;align-items:center;margin-top:var(--gap)'><div class='slogan'>Choose the <b>moment.</b></div><div style='font-size:18px;font-weight:600;letter-spacing:.16em;color:rgba(13,27,51,.5)'>OWN YOUR {dict(activate='DAY',focus='NOW',calm='PAUSE',sleep='NIGHT')[st]}.</div></div>"

# ---------- Ads ----------
def ad_before_after(d, fmt):
    st = d["st"]
    rows = lambda rs: "".join(f"<div class='row'><span class='tm'>{t}</span><span>{x}</span></div>" for t, x in rs)
    off_rows = d["off_rows"] if fmt == "916" else d["off_rows"][:3] + d["off_rows"][3:]
    body = (topbar(st, "")
            + f"<div style='text-align:center'><div class='eyebrow'>{d['eyebrow']}</div>"
              f"<h1 style='margin-top:18px'>{d['h1a']}<br>{d['h1b']}</h1></div>"
            + f"<div style='margin:22px -10px -6px'>{signal_bridge(st, 980, drop=96 if fmt=='45' else 130, lx=245, rx=740)}</div>"
            + "<div class='cards'>"
              f"<div class='card off'><div class='warn lbl'><i>!</i>Ohne Signal</div><div class='ct'>{d['off_t']}</div>{rows(off_rows)}"
              f"<div class='grow'></div><div class='why'><div class='lbl'>Der eigentliche Grund</div><div class='h'>{d['why_h']}</div>"
              + (f"<p>{d['why_p']}</p>" if fmt == "916" else "") + "</div></div>"
              f"<div class='card on'><div class='lbl' style='color:var(--c)'><span class='dot' style='width:10px;height:10px;margin-right:12px'></span>Mit {S[st]['name']}</div>"
              f"<div class='ct'>{d['on_t']}</div>{rows(d['on_rows'])}<div class='grow'></div>"
              f"<div class='chip' style='margin-top:16px;padding:10px 16px 10px 10px;gap:14px'><img src='{A}{d['img']}' style='width:70px;height:70px'><div><div class='t' style='font-size:19px'>{d['chip_t']}</div><div class='s' style='font-size:15px'>{d['chip_s']}</div></div><div class='arr' style='font-size:28px'>→</div></div>"
              "</div></div>"
            + (foot(st) if fmt == "916" else ""))
    css = ".ba .cards{flex:1}" if fmt == "916" else ""
    return page(d["title"], st, fmt, f"<div class='ba' style='display:flex;flex-direction:column;height:100%'>{body}</div>", css)

BA = [
 dict(key="01-sleep-vorher-nachher", title="SLEEP Vorher Nachher", st="sleep", eyebrow="So sieht dein Abend gerade aus",
      h1a="Der Körper liegt.", h1b="Der Kopf nicht.", off_t="Licht aus. Gedanken noch an.",
      off_rows=[("22:15","Zähne geputzt, Handy auf dem Nachttisch. Noch kurz die Nachrichten."),("22:50","Licht aus. Und plötzlich fällt dir alles ein, was morgen ansteht."),("23:40","Du drehst das Kissen um und rechnest, wie viele Stunden noch bleiben."),("06:30","Der Wecker. Und das Gefühl, kaum abgeschaltet zu haben.")],
      why_h="Dir fehlt keine Müdigkeit. Dir fehlt ein Ende für den Tag.", why_p="Solange der Abend kein festes Ende hat, holt der Kopf nach, was liegen geblieben ist. Ein Ritual, das jeden Abend gleich ist, setzt diesen Schlusspunkt.",
      on_t="Licht aus. Der Tag ist vorbei.", on_rows=[("22:15","Zähne geputzt, Handy weg."),("22:16","Ein Sprühstoß aufs Kissen, Roll-On aufs Handgelenk. Lavendel, Kamille, warmes Zedernholz."),("22:17","Dein Signal: Der Tag ist vorbei. Ab jetzt nur noch Abend."),("Danach","Mit jedem Abend gehören Duft und Loslassen enger zusammen.")],
      chip_t="Dein Abend-Signal holen", chip_s="SLEEP Komplett-Set · €89", img="nr-set-sleep-hero.webp"),
 dict(key="02-calm-vorher-nachher", title="CALM Vorher Nachher", st="calm", eyebrow="So sieht dein Feierabend gerade aus",
      h1a="Du bist zu Hause.", h1b="Aber nicht ganz da.", off_t="Zu Hause. Kopf noch im Meeting.",
      off_rows=[("18:05","Laptop zu. Noch ein letzter Blick aufs Handy."),("18:40","Auf dem Heimweg spielst du das Meeting noch einmal durch."),("19:30","Am Tisch nickst du, hörst aber nur halb zu."),("21:00","Erst jetzt merkst du, wie angespannt du den ganzen Abend warst.")],
      why_h="Dir fehlt kein Feierabend. Dir fehlt ein Schlusspunkt.", why_p="Der Kopf schaltet nicht ab, nur weil der Laptop zu ist. Er braucht einen klaren Moment, der den Arbeitstag beendet. Fehlt der, läuft das Meeting einfach weiter.",
      on_t="Laptop zu. Kopf frei.", on_rows=[("18:05","Laptop zu."),("18:06","Roll-On aufs Handgelenk. Ein Atemzug: Neroli, Rose, helle Orange."),("18:07","Dein Signal: Der Arbeitstag ist vorbei. Ab jetzt ist Feierabend."),("Danach","Mit jedem Abend gehören Duft und Ankommen enger zusammen.")],
      chip_t="Dein Feierabend-Signal holen", chip_s="CALM Komplett-Set · €89", img="nr-set-calm-hero_d9e1c46a-abd5-4b2b-b375-fb6d6ae9d035.webp"),
 dict(key="03-focus-vorher-nachher", title="FOCUS Vorher Nachher", st="focus", eyebrow="So sieht dein Nachmittag gerade aus",
      h1a="Du bist beschäftigt.", h1b="Aber nicht bei der Sache.", off_t="Viel beschäftigt. Wenig geschafft.",
      off_rows=[("13:40","Zurück vom Mittag. Die Liste ist länger als am Morgen."),("14:55","Zwölf Tabs offen. Keiner davon fertig."),("15:10","Dritter Kaffee. Oder doch der Riegel aus der Schublade."),("16:30","Viel beschäftigt gewesen. Wenig geschafft.")],
      why_h="Dir fehlt keine Konzentration. Dir fehlt ein klarer Neustart.", why_p="Nach der Mittagspause springt der Kopf nicht von selbst zurück in die Arbeit. Er braucht einen Moment, der sagt: Jetzt geht es weiter. Fehlt der, gewinnt der nächste Tab.",
      on_t="Eine Aufgabe. Ganz bei der Sache.", on_rows=[("14:55","Tabs zu. Einer bleibt offen."),("14:56","Roll-On aufs Handgelenk. Ein Atemzug: Rosmarin, Zitrone, Minze, ein Hauch Zimt."),("14:57","Dein Signal zum Abtauchen. Jetzt nur noch diese eine Aufgabe."),("Danach","Mit jedem Nachmittag gehören Duft und Fokus-Block enger zusammen.")],
      chip_t="Dein Fokus-Signal holen", chip_s="FOCUS Komplett-Set · €89", img="nr-set-focus-hero_651397b1-0fd3-4ca6-a8b7-f7041f0dc4a8.webp"),
]

def ad_founder(fmt):
    st = "activate"
    big = fmt == "916"
    body = (topbar(st)
      + f"<div class='grow' style='display:flex;flex-direction:column;justify-content:center'>"
      f"<div style='width:{300 if big else 250}px;height:{300 if big else 250}px;border-radius:50%;padding:10px;background:rgba(255,255,255,.75);box-shadow:0 22px 50px -32px rgba(13,27,51,.35);margin-bottom:{44 if big else 30}px'>"
      f"<img src='{A}nr-philip-portrait-3c.jpg' style='width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 20%'></div>"
      f"<div class='it' style='font-size:{150 if big else 120}px;line-height:.6;color:var(--c);height:{70 if big else 56}px'>“</div>"
      f"<div style='font-size:{64 if big else 56}px;font-weight:300;letter-spacing:-.04em;line-height:1.14'>Duft begleitet uns jeden Tag, meist unbewusst. Mit Neurora Labs machen wir ihn zu einem <span style='color:var(--c)'>bewussten Werkzeug</span>.</div>"
      f"<div style='height:1px;background:rgba(13,27,51,.12);margin:{36 if big else 28}px 0 22px'></div>"
      f"<div style='display:flex;align-items:center;gap:16px'><div style='width:46px;height:46px;border-radius:10px;background:#0D1B33;display:grid;place-items:center'>{svg_logo('mono', '#F6F3EC', h=22)}</div>"
      f"<div class='lbl' style='color:rgba(13,27,51,.6);font-size:16px'>Philip Huber, Founder &amp; CEO</div></div></div>"
      f"<div class='panel' style='padding:14px;margin-top:{40 if big else 26}px'><img src='{A}nr-rituale-66-tag-1.jpg' style='display:block;width:100%;height:{520 if big else 300}px;object-fit:cover;object-position:62% 55%;border-radius:24px'>"
      f"<div style='display:flex;justify-content:space-between;align-items:center;padding:16px 10px 4px'><div style='font-size:21px;font-weight:300;letter-spacing:-.01em'>Activate · Focus · Calm · Sleep</div><div class='slogan' style='font-size:19px'>Vier Momente. Ein Duft für jeden.</div></div></div>")
    return page("Founder Zitat", st, fmt, body)

def ad_mission(fmt):
    st = "sleep"; big = fmt == "916"
    css = ("body{background:#0B1630}body::before{background:radial-gradient(700px 600px at 100% 0%,rgba(78,61,152,.55),transparent 70%),radial-gradient(600px 500px at 0% 100%,rgba(181,71,31,.18),transparent 70%)}"
           ".m h1{color:#F6F3EC}.m h1 .acc{color:rgba(246,243,236,.55)}.m .lbl{color:rgba(246,243,236,.7)}")
    body = (f"<div class='m' style='display:flex;flex-direction:column;height:100%'>"
      f"<div class='top'>{svg_logo('lockup', '#F6F3EC', h=46)}<div class='slogan' style='color:rgba(246,243,236,.7)'>Choose the <b style='color:#C5B0F3'>moment.</b></div></div>"
      f"<h1 style='font-size:{98 if big else 80}px'>Auf Wissenschaft gebaut.<span class='acc'>Damit deine Stimmung dir gehört.</span></h1>"
      f"<div class='grow' style='display:flex;align-items:center;justify-content:center;padding:{44 if big else 28}px 0'>"
      f"<div style='width:100%;border-radius:32px;overflow:hidden;box-shadow:0 40px 80px -40px rgba(0,0,0,.6);border:1px solid rgba(255,255,255,.12)'>"
      f"<img src='{A}nr-set-sleep-hero.webp' style='display:block;width:100%;height:{760 if big else 470}px;object-fit:cover;object-position:50% 58%'></div></div>"
      f"<div style='height:1px;background:rgba(246,243,236,.14);margin-bottom:24px'></div>"
      f"<div class='lbl' style='font-size:15px'><span class='dot' style='--c:#B5471F;--g:#F6AE8E;width:9px;height:9px;margin-right:12px'></span>Mission</div>"
      f"<div style='font-size:{40 if big else 34}px;font-weight:300;letter-spacing:-.03em;line-height:1.18;color:#F6F3EC;margin:14px 0 14px'>Wir übersetzen olfaktorische Wissenschaft in Werkzeuge für deinen Alltag.</div>"
      f"<div style='font-size:{22 if big else 19}px;line-height:1.55;color:rgba(246,243,236,.66)'>Neurora schließt die Lücke zwischen olfaktorischer Neurowissenschaft und Alltag. Zugänglich, präzise und überprüfbar. Der Rahmen ist der circadiane Takt: Vier Zustände, drei Formate, ein Tag.</div>"
      + (f"<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px;padding-top:28px;border-top:1px solid rgba(246,243,236,.14)'>"
         + "".join(f"<div><div class='lbl' style='font-size:13px;color:rgba(246,243,236,.5)'>{k}</div><div style='font-size:21px;color:#F6F3EC;margin-top:8px'>{v}</div></div>" for k, v in [("Unternehmen","Neurora Labs GmbH"),("Gegründet","2026 in Wien"),("Gründer","Philip Huber")])
         + "</div>" if big else "")
      + "</div>")
    return page("Mission", st, fmt, body, css)

def ad_atemzug(fmt):
    st = "calm"; big = fmt == "916"
    times = [("07:00","activate"),("09:30","focus"),("18:30","calm"),("22:00","sleep")]
    tabs = "".join(
        f"<div style='flex:1;text-align:center;padding:16px 0 14px;border-radius:18px;{'background:#fff;box-shadow:0 10px 26px -18px rgba(13,27,51,.4);' if s=='calm' else ''}'>"
        f"<span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:10px;height:10px;{'' if s=='calm' else 'box-shadow:none;'}'></span>"
        f"<div style='font-size:22px;font-weight:600;margin-top:8px;font-variant-numeric:tabular-nums'>{t}</div><div class='lbl' style='font-size:13px;color:{S[s]['c']};margin-top:4px'>{S[s]['name']}</div></div>" for t, s in times)
    card = (f"<div class='board' style='padding:12px 12px 20px'>"
            f"<div style='display:flex;gap:4px;background:rgba(242,240,236,.7);border-radius:20px;padding:6px'>{tabs}</div>"
            f"<div style='padding:18px 18px 0'>{signal_inline('calm', 880, 64, 0.32)}"
            f"<div style='display:flex;justify-content:space-between;font-size:21px;margin-top:10px'><span>Angespannt</span><span style='color:var(--c)'>Angekommen</span></div>"
            f"<div style='height:1px;background:rgba(13,27,51,.08);margin:16px 0 14px'></div>"
            f"<div style='display:flex;justify-content:space-between;align-items:center;font-size:20px'><span><span class='lbl' style='font-size:13px;color:rgba(13,27,51,.5);margin-right:12px'>Auslöser</span>Tag geschafft</span><span style='color:var(--c);font-weight:600'>Zum Ritual →</span></div></div></div>")
    poster = (f"<div style='position:relative;border-radius:30px;overflow:hidden;border:8px solid rgba(255,255,255,.7);box-shadow:0 30px 60px -36px rgba(13,27,51,.45)'>"
              f"<img src='{A}nr-founder-ritual-3c-poster.jpg' style='display:block;width:100%;height:{760 if big else 450}px;object-fit:cover;object-position:50% {38 if big else 30}%'>"
              f"<div style='position:absolute;left:50%;bottom:{54 if big else 34}px;transform:translateX(-50%);text-align:center;color:#fff'>"
              f"<div style='width:104px;height:104px;border-radius:50%;background:#fff;margin:0 auto;display:grid;place-items:center;box-shadow:0 0 0 12px rgba(197,176,243,.45)'><div style='width:0;height:0;border-left:22px solid #0D1B33;border-top:14px solid transparent;border-bottom:14px solid transparent;margin-left:6px'></div></div>"
              f"<div style='margin-top:14px;font-size:22px;font-weight:600;text-shadow:0 1px 8px rgba(0,0,0,.4)'>Mit Ton ansehen</div></div></div>"
              f"<div style='font-size:17px;color:rgba(13,27,51,.55);margin-top:12px'>Philip, Gründer von Neurora, über sein Ritual am Feierabend.</div>")
    body = (topbar(st)
      + f"<div class='eyebrow grey'>Rituale</div>"
      f"<h1 style='font-size:{124 if big else 104}px;margin-top:10px'>Ein Atemzug.</h1>"
      f"<div style='font-size:{62 if big else 50}px;font-weight:300;letter-spacing:-.04em;line-height:1.08;color:#4E3D98;margin-top:8px'>Jeden Tag im selben Moment.</div>"
      + (f"<p class='lead' style='margin-top:26px'>Ein Duft, den du jeden Tag im selben Moment auflegst, wird mit der Zeit zu deinem Signal für genau diesen Moment. Kein neues Programm, kein früheres Aufstehen: ein Atemzug, eingebaut in das, was du ohnehin tust.</p>" if big else "")
      + f"<div style='margin-top:{36 if big else 28}px'>{poster}</div>"
      f"<div style='margin-top:{-110 if big else -96}px;position:relative;z-index:2;padding:0 18px'>{card}</div>"
      f"<div class='grow'></div>"
      f"<div style='display:flex;gap:30px;font-size:19px;color:rgba(13,27,51,.7);margin-top:24px'><span>◷ 30 Tage testen</span><span>▭ Versand gratis ab 50 €</span><span>◉ Made in Europe</span></div>")
    return page("Ein Atemzug", st, fmt, body)

def ad_quiz(fmt):
    st = "sleep"; big = fmt == "916"
    items = [("activate","07:00","Morgens schwer in Gang?","Wach, aber noch nicht da."),("focus","09:30","Nachmittagstief um 15 Uhr?","Beschäftigt, aber nicht bei der Sache."),
             ("calm","18:30","Kopf noch im Meeting?","Zu Hause, aber noch nicht angekommen."),("sleep","22:00","Im Bett und noch hellwach?","Licht aus, Tag aus.")]
    cards = "".join(
        f"<div style='background:#fff;border-radius:24px;padding:26px 26px;box-shadow:0 14px 34px -26px rgba(13,27,51,.35);position:relative'>"
        f"<div class='lbl' style='font-size:15px;color:{S[s]['c']}'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:10px;height:10px;box-shadow:none;margin-right:12px'></span>{t} · {S[s]['name']}</div>"
        f"<div style='position:absolute;right:22px;top:20px;width:34px;height:34px;border-radius:50%;border:1.5px solid rgba(13,27,51,.12)'></div>"
        f"<div style='font-size:{32 if big else 29}px;font-weight:400;letter-spacing:-.025em;line-height:1.15;margin-top:16px'>{h}</div>"
        f"<div style='font-size:{21 if big else 19}px;color:rgba(13,27,51,.6);margin-top:10px;line-height:1.4'>{p}</div></div>" for s, t, h, p in items)
    body = (topbar(st)
      + f"<div class='panel grow' style='padding:{56 if big else 46}px {44 if big else 40}px;display:flex;flex-direction:column'>"
      f"<div class='eyebrow grey'>Kennst du das?</div><h1 style='margin-top:18px;font-size:{108 if big else 92}px'>Wo hakt dein Tag?</h1>"
      f"<p class='lead' style='margin-top:16px'>Tipp an, was du kennst. Mehrere gehen auch.</p>"
      f"<div class='grow'></div>"
      f"<div style='display:grid;grid-template-columns:{'1fr' if big else '1fr 1fr'};gap:14px;margin-top:30px'>{cards}</div>"
      f"<div style='background:#F0EFEC;border-radius:22px;padding:24px 28px;margin-top:16px;font-size:21px;color:rgba(13,27,51,.72)'>Tipp an, was du kennst. Dann zeigen wir dir, wo dein Ritual anfängt.</div></div>")
    return page("Wo hakt dein Tag", st, fmt, body)

def ad_signal_steps(fmt):
    st = "sleep"; big = fmt == "916"
    steps = [("01","Der Moment","Ein fester Auslöser, den es in deinem Tag schon gibt: der erste Kaffee, Laptop auf, Licht aus.","nr-rituale-schritt-1-moment.jpg"),
             ("02","Der Duft","Immer derselbe Duft, nur für diesen einen Moment. So bleibt er eindeutig.","nr-rituale-schritt-2-duft.jpg"),
             ("03","Der Atemzug","Ein bewusster, tiefer Atemzug. Für ein paar Sekunden bist du nur beim Duft und nicht bei der nächsten Aufgabe.","nr-rituale-schritt-3-atemzug-v2.jpg"),
             ("04","Das Signal","Mit jeder Wiederholung gehören Duft und Moment enger zusammen. Irgendwann kündigt der Duft den Moment an.","nr-rituale-schritt-4-signal.jpg")]
    cards = "".join(
        f"<div style='background:rgba(251,250,247,.9);border-radius:26px;padding:10px 10px 20px;box-shadow:0 18px 40px -30px rgba(13,27,51,.35)'>"
        f"<img src='{A}{img}' style='display:block;width:100%;height:{200 if big else 150}px;object-fit:cover;border-radius:18px'>"
        f"<div style='padding:0 12px'><div class='it' style='font-size:{40 if big else 34}px;margin-top:10px'>{n}</div>"
        f"<div style='font-size:{25 if big else 22}px;font-weight:400;margin-top:2px'>{t}</div>"
        f"<div style='font-size:{18.5 if big else 16}px;line-height:1.45;color:rgba(13,27,51,.65);margin-top:8px'>{p}</div></div></div>" for n, t, p, img in steps)
    quote = (f"<div style='background:#0F1A35;border-radius:28px;padding:{34 if big else 28}px {34 if big else 30}px;color:#F6F3EC;margin-top:16px'>"
             f"<div style='font-size:{33 if big else 28}px;font-weight:300;letter-spacing:-.025em;line-height:1.22'>„Der angenehme Duft wird zum Signal. Und durch die Routine lerne ich, dass der Feierabend jetzt anfangen kann.“</div>"
             f"<div style='font-size:16px;color:rgba(246,243,236,.6);margin-top:14px'>Philip, Gründer von Neurora, im Video über sein Feierabend-Ritual</div>"
             f"<div style='display:flex;align-items:center;gap:20px;margin-top:16px'><div style='flex:1'>{signal_inline('calm', 560, 50, 0.34, '#A3CCF0')}</div>"
             f"<div style='border:1px solid rgba(246,243,236,.35);border-radius:999px;padding:12px 22px;font-size:18px;white-space:nowrap'>▶ Im Video ansehen</div></div></div>")
    body = (topbar(st)
      + f"<div style='text-align:center'><div class='eyebrow grey'>Warum Rituale</div>"
      f"<h1 style='margin-top:16px;font-size:{90 if big else 76}px'>Ein Duft wird zum Signal.<span class='acc'>Durch Wiederholung.</span></h1></div>"
      f"<div class='grow' style='min-height:20px'></div>"
      f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:26px'>{cards}</div>{quote}"
      + (foot(st) if big else ""))
    return page("Ein Duft wird zum Signal", st, fmt, body)

def ad_vier_momente(fmt):
    st = "sleep"; big = fmt == "916"
    m = [("activate","07:00","Dein Start.","Der erste Kaffee, noch bevor das Handy dran ist."),("focus","09:30","Dein Fokus-Block.","Laptop auf: vor dem ersten Meeting oder nach der Mittagspause."),
         ("calm","18:30","Dein Feierabend.","Der Tag ist geschafft."),("sleep","22:00","Dein Licht aus.","Zähne geputzt, Handy weg.")]
    cards = "".join(
        f"<div style='border-radius:28px;padding:24px 22px 26px;background:linear-gradient(160deg,rgba(255,255,255,.92) 40%,color-mix(in srgb,{S[s]['g']} 30%,#fff));box-shadow:0 18px 40px -30px rgba(13,27,51,.35);border:1px solid rgba(255,255,255,.95)'>"
        f"<div style='display:flex;justify-content:space-between;align-items:center'><span class='it' style='font-size:{44 if big else 38}px;color:{S[s]['c']}'>{t}</span>"
        f"<span class='lbl' style='font-size:13px;color:{S[s]['c']};background:#fff;border-radius:999px;padding:9px 14px;box-shadow:0 6px 16px -10px rgba(13,27,51,.3)'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:9px;height:9px;box-shadow:none;margin-right:8px'></span>{S[s]['name']}</span></div>"
        f"<div style='margin:14px 0 12px'>{signal_inline(s, 400, 48, 0.36)}</div>"
        f"<div style='font-size:{44 if big else 38}px;font-weight:300;letter-spacing:-.045em;line-height:1.05'>{h}</div>"
        f"<div class='lbl' style='font-size:13px;color:rgba(13,27,51,.5);margin-top:16px'>Auslöser</div>"
        f"<div style='font-size:{20 if big else 18}px;line-height:1.4;color:rgba(13,27,51,.7);margin-top:6px'>{a}</div></div>" for s, t, h, a in m)
    body = (topbar(st)
      + f"<div style='text-align:center'><div class='eyebrow grey'>Dein Tag in vier Ritualen</div>"
      f"<h1 style='margin-top:16px;font-size:{100 if big else 86}px'>Vier Momente.<span class='acc'>Ein Duft für jeden.</span></h1>"
      f"<p class='lead' style='margin-top:18px'>Fang mit einem Moment an. Die anderen kommen dazu, wenn du willst.</p></div>"
      f"<div class='grow' style='min-height:20px'></div>"
      f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:26px'>{cards}</div>"
      + (f"<div class='panel' style='padding:12px;margin-top:18px'><img src='{A}nr-rituale-66-tag-1.jpg' style='display:block;width:100%;height:330px;object-fit:cover;object-position:62% 55%;border-radius:26px'></div>" + foot(st) if big else ""))
    return page("Vier Momente", st, fmt, body)

def ad_30_tage(fmt):
    st = "sleep"; big = fmt == "916"
    steps = [("Tag 1","Wähle einen Moment.","Einen, den es jeden Tag gibt. Leg den Duft genau dorthin, wo dein Tag gerade hakt.","nr-rituale-66-tag-1.jpg"),
             ("Woche 1","Gleicher Duft, gleicher Moment.","Jeden Tag gleich: Auslöser, Duft, ein Atemzug. Mehr braucht es nicht.","nr-rituale-66-woche-1.jpg"),
             ("Woche 4","Der Duft läuft mit.","Er kostet dich keinen Gedanken mehr. Jetzt kannst du einen zweiten Moment dazunehmen.","nr-rituale-66-woche-4.jpg"),
             ("Ab Tag 30","Dein Signal. Auf Abruf.","Du setzt den Duft dort ein, wo du ihn brauchst. Mood on Demand.","nr-rituale-66-tag-66.jpg")]
    cards = "".join(
        f"<div><div style='display:flex;align-items:center;gap:12px'>"
        + (f"<span style='width:22px;height:22px;border-radius:50%;border:2.5px solid #0D1B33;display:inline-block;background:#F1EEE8'></span>" if i < 3 else o_inline())
        + f"<span class='it' style='font-size:{34 if big else 30}px'>{l}</span></div>"
        f"<div style='font-size:{25 if big else 22}px;font-weight:500;letter-spacing:-.015em;margin-top:8px'>{t}</div>"
        f"<div style='font-size:{18.5 if big else 16.5}px;line-height:1.45;color:rgba(13,27,51,.65);margin-top:6px;min-height:{80 if big else 70}px'>{p}</div>"
        f"<img src='{A}{img}' style='display:block;width:100%;height:{220 if big else 170}px;object-fit:cover;border-radius:20px;margin-top:12px'></div>" for i, (l, t, p, img) in enumerate(steps))
    body = (topbar(st)
      + f"<div style='text-align:center'><div class='eyebrow grey'>Dein Plan</div>"
      f"<h1 style='margin-top:16px;font-size:{100 if big else 86}px'>Die ersten 30 Tage.<span class='acc'>Ein Moment nach dem anderen.</span></h1></div>"
      f"<div class='grow' style='min-height:20px'></div>"
      f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:{34 if big else 26}px 24px;margin-top:26px'>{cards}</div>"
      f"<div class='board' style='padding:22px 26px;margin-top:24px;font-size:{20 if big else 18}px;line-height:1.5;color:rgba(13,27,51,.7)'><b style='color:#0D1B33;font-weight:600'>Einen Tag ausgelassen?</b> Macht nichts. Mach am nächsten Tag einfach weiter. Auch in der Studie zur Gewohnheitsbildung (Lally et al. 2010) hat ein ausgelassener Tag den Verlauf kaum verändert.</div>"
      + (foot(st) if big else ""))
    return page("Die ersten 30 Tage", st, fmt, body)

def o_inline():
    c = S["sleep"]
    return (f"<svg width='30' height='30' viewBox='0 0 30 30'><circle cx='15' cy='15' r='14' fill='{c['g']}' opacity='.3'/>"
            f"<path d='M 11.5 5.6 A 10 10 0 1 0 18.5 5.6' fill='none' stroke='{c['c']}' stroke-width='2.5' stroke-linecap='round'/><circle cx='15' cy='15' r='4.5' fill='{c['g']}'/></svg>")

def ad_focus_offer(fmt):
    st = "focus"; big = fmt == "916"
    check = "<span style='width:32px;height:32px;border-radius:50%;background:#1F4A3D;display:grid;place-items:center;flex:none'><svg width='16' height='16' viewBox='0 0 16 16'><path d='M3 8.5l3.2 3L13 4.8' stroke='#fff' stroke-width='2.2' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg></span>"
    items = [("FOCUS Roll-On","Roll-On · 10 ml","€29"),("FOCUS Textilspray","Textilspray · 30 ml","€39"),("FOCUS Raumdiffuser","Raumdiffuser · 125 ml","€49"),
             ("Versand gratis","Deutschland und Österreich ab 50 €","€5,99"),("30 Tage testen","Passt es nicht zu dir, bekommst du dein Geld zurück.","ohne Risiko")]
    rows = "".join(f"<div style='display:flex;gap:16px;align-items:flex-start;padding:{16 if big else 12}px 0;border-bottom:1px solid rgba(13,27,51,.08)'>{check}"
                   f"<div style='flex:1'><div style='font-size:{23 if big else 21}px'>{a}</div><div style='font-size:{17 if big else 15.5}px;color:rgba(13,27,51,.55);margin-top:3px'>{b}</div></div>"
                   f"<div style='font-size:{21 if big else 19}px;color:rgba(13,27,51,.7)'>{c}</div></div>" for a, b, c in items)
    body = (topbar(st)
      + f"<div style='text-align:center'><div class='eyebrow'>Dein Angebot</div><h1 style='margin-top:14px;font-size:{88 if big else 72}px'>Alles für deinen Fokus-Block.</h1></div>"
      f"<div class='panel grow' style='margin-top:{34 if big else 24}px;overflow:hidden;display:flex;flex-direction:column'>"
      f"<div style='position:relative;background:#F4EFE8'><img src='{A}nr-set-focus-hero_651397b1-0fd3-4ca6-a8b7-f7041f0dc4a8.webp' style='display:block;width:100%;height:{520 if big else 300}px;object-fit:cover;object-position:50% 60%'>"
      f"<div style='position:absolute;right:24px;bottom:22px;width:{150 if big else 128}px;height:{150 if big else 128}px;border-radius:50%;background:rgba(255,255,255,.92);display:grid;place-items:center;text-align:center'><div><div style='font-size:{48 if big else 40}px;font-weight:300;color:var(--c);line-height:1'>30</div><div class='lbl' style='font-size:11px;margin-top:4px'>Tage testen</div><div style='font-size:12px;color:rgba(13,27,51,.55)'>Geld zurück</div></div></div></div>"
      f"<div style='padding:{30 if big else 22}px {36 if big else 34}px {30 if big else 24}px;display:flex;flex-direction:column;flex:1'>"
      f"<div class='lbl' style='color:var(--c);font-size:14px'>Im Fokus-Set</div>"
      f"<div style='font-size:{34 if big else 27}px;font-weight:300;letter-spacing:-.03em;line-height:1.15;margin:10px 0 {10 if big else 4}px'>Roll-On für den Moment, Textilspray für unterwegs, Raumdiffuser für deinen Platz.</div>"
      f"{rows}"
      f"<div style='display:flex;justify-content:space-between;align-items:flex-end;margin-top:{18 if big else 12}px'><div style='font-size:20px;color:rgba(13,27,51,.6)'>Gesamtwert <s>€122,99</s></div>"
      f"<div style='text-align:right'><div class='lbl' style='font-size:13px;color:rgba(13,27,51,.55)'>Dein Preis</div><div style='font-size:{78 if big else 64}px;font-weight:300;color:var(--c);line-height:1'>€89</div></div></div>"
      f"<div style='background:#E6F2EC;border-radius:18px;padding:16px 20px;margin-top:14px;font-size:{18.5 if big else 16.5}px;line-height:1.45'>🎁&nbsp; Bonus: Dein Set liegt über 85 €, deshalb legen wir dir einen Roll-On deiner Wahl gratis dazu (Wert 29 €), zum Beispiel ACTIVATE für deinen Morgen.</div>"
      f"<div class='grow'></div><div class='btn' style='justify-content:center;margin-top:16px'>Fokus-Set in den Warenkorb · €89</div></div></div>")
    return page("FOCUS Angebot", st, fmt, body)

def dial_svg(W=900):
    cx, cy, R = W / 2, 470, 400
    import math
    def arc(r, a0, a1):
        p0 = (cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0)))
        p1 = (cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1)))
        large = 1 if abs(a1 - a0) > 180 else 0
        return f"M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 {large} 1 {p1[0]:.1f} {p1[1]:.1f}"
    out = [f"<svg viewBox='0 0 {W} 520' width='100%' style='display:block'>",
           f"<defs><radialGradient id='kg' cx='50%' cy='100%' r='70%'><stop offset='0' stop-color='#8AD3BD' stop-opacity='.55'/><stop offset='1' stop-color='#8AD3BD' stop-opacity='0'/></radialGradient></defs>",
           f"<rect x='0' y='0' width='{W}' height='520' fill='url(#kg)'/>",
           f"<path d='{arc(R,172,152)}' stroke='#B5471F' stroke-width='7' fill='none' stroke-linecap='round'/>",
           f"<path d='{arc(R,148,47)}' stroke='#1F4A3D' stroke-width='9' fill='none' stroke-linecap='round'/>",
           f"<path d='{arc(R,43,8)}' stroke='#2F6FA8' stroke-width='7' fill='none' stroke-linecap='round'/>"]
    for i, a in enumerate(range(160, 15, -12)):
        r0, r1 = (R - 52, R - 22) if i % 3 == 1 else (R - 40, R - 26)
        x0, y0 = cx + r0 * math.cos(math.radians(a)), cy - r0 * math.sin(math.radians(a))
        x1, y1 = cx + r1 * math.cos(math.radians(a)), cy - r1 * math.sin(math.radians(a))
        out.append(f"<line x1='{x0:.1f}' y1='{y0:.1f}' x2='{x1:.1f}' y2='{y1:.1f}' stroke='rgba(13,27,51,{.55 if i%3==1 else .25})' stroke-width='{3 if i%3==1 else 2}'/>")
    for lab, a in [("09", 136), ("12", 96), ("15", 52)]:
        r = R - 80
        out.append(f"<text x='{cx + r*math.cos(math.radians(a)):.1f}' y='{cy - r*math.sin(math.radians(a))+8:.1f}' font-family='Manrope' font-size='26' fill='rgba(13,27,51,.6)' text-anchor='middle'>{lab}</text>")
    r2 = R - 140
    out += [f"<path d='{arc(r2,168,122)}' stroke='#D7D3A8' stroke-width='22' fill='none'/>",
            f"<path d='{arc(r2,119,72)}' stroke='#1F4A3D' stroke-width='30' fill='none' stroke-linecap='round'/>",
            f"<path d='{arc(r2,69,22)}' stroke='#CBBDB8' stroke-width='22' fill='none'/>",
            f"<text x='{cx-30:.1f}' y='{cy-r2+62:.1f}' font-family='Manrope' font-size='30' fill='#1F4A3D' text-anchor='middle'>Scharf</text>",
            f"<text x='{cx+170:.1f}' y='{cy-r2+100:.1f}' font-family='Manrope' font-size='28' fill='#9C8682' transform='rotate(28 {cx+170:.1f} {cy-r2+100:.1f})'>Warm</text>",
            f"<text x='{cx-250:.1f}' y='{cy-r2+180:.1f}' font-family='Manrope' font-size='28' fill='#BDB88A' transform='rotate(-58 {cx-250:.1f} {cy-r2+180:.1f})'>Klar</text>"]
    for x, y, col in [(cx-80, cy-r2+105, '#1F4A3D'), (cx-40, cy-r2+97, '#1F4A3D'), (cx, cy-r2+93, '#1F4A3D'),
                      (cx+165, cy-r2+148, '#B8A7A2'), (cx+200, cy-r2+168, '#B8A7A2'),
                      (cx-220, cy-r2+165, '#D7D3A8'), (cx-245, cy-r2+200, '#D7D3A8'), (cx-262, cy-r2+238, '#D7D3A8')]:
        out.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='15' fill='{col}'/>")
    out += [f"<line x1='{cx}' y1='{cy-R-6}' x2='{cx}' y2='{cy-r2}' stroke='rgba(13,27,51,.35)' stroke-width='2' stroke-dasharray='4 6'/>",
            f"<path d='M {cx-16} {cy-R-34} L {cx+16} {cy-R-34} L {cx} {cy-R-12} Z' fill='#0D1B33'/>", "</svg>"]
    return "".join(out)

def ad_kompass(fmt):
    st = "focus"; big = fmt == "916"
    mol = "".join(f"<span style='display:inline-flex;align-items:center;gap:12px;background:#fff;border-radius:999px;padding:8px 22px 8px 8px;box-shadow:0 8px 22px -14px rgba(13,27,51,.35);font-size:{23 if big else 21}px'>"
                  f"<span style='width:44px;height:44px;border-radius:50%;background:#1F4A3D;color:#fff;display:grid;place-items:center;font-size:17px;font-weight:600;box-shadow:0 0 0 5px rgba(138,211,189,.35)'>{n}</span>{t}</span>"
                  for n, t in [("08","1,8-Cineol"),("09","Kampfer"),("10","Verbenon")])
    body = (topbar(st)
      + f"<div class='lbl' style='color:var(--c);font-size:16px'><span class='dot' style='width:10px;height:10px;margin-right:14px'></span>Neurora Kompass · Mood on Demand</div>"
      f"<h1 style='margin-top:18px;font-size:{86 if big else 70}px'>Für alle, die mehr über ihren Duft lernen wollen.</h1>"
      f"<div class='grow' style='min-height:20px'></div>"
      f"<div class='panel' style='margin-top:28px;padding:{36 if big else 28}px {34 if big else 30}px 0;overflow:hidden'>"
      f"<div class='lbl' style='font-size:15px;color:rgba(13,27,51,.55)'><span class='dot' style='width:10px;height:10px;margin-right:12px'></span>Jetzt · 12:46</div>"
      f"<div style='font-size:{104 if big else 84}px;font-weight:300;letter-spacing:-.045em;color:var(--c);line-height:1;margin-top:12px'>Scharf</div>"
      f"<div style='margin-top:8px;font-size:{34 if big else 30}px'><span class='it' style='color:rgba(13,27,51,.75)'>Mittag · 12:00</span> <span class='lbl' style='font-size:16px;color:var(--c)'>Focus</span></div>"
      f"<p style='font-size:{23 if big else 20}px;line-height:1.45;color:rgba(13,27,51,.7);margin-top:12px'>Durchdringend, kampferartig, präzise. Die Noten für die Stunden am Schreibtisch.</p>"
      f"<div style='display:flex;gap:12px;flex-wrap:wrap;margin-top:18px'>{mol}</div>"
      f"<div class='lbl' style='font-size:14px;color:rgba(13,27,51,.45);margin-top:{34 if big else 24}px'>Zum Drehen wischen</div>"
      f"<div style='margin:6px -34px 0;height:{470 if big else 330}px;overflow:hidden'>{dial_svg(1000)}</div></div>"
      f"<p class='it' style='font-size:{22 if big else 19}px;line-height:1.45;color:rgba(13,27,51,.55);margin-top:18px'>Die Duftfamilien beschreiben den Charakter eines Moleküls, keine Wirkung. Studien wurden mit einzelnen Ölen oder Duftstoffen gemacht, nicht mit unseren Rezepturen.</p>")
    return page("Neurora Kompass", st, fmt, body)

ADS = [(d["key"], (lambda d: (lambda f: ad_before_after(d, f)))(d)) for d in BA] + [
    ("04-founder-zitat", ad_founder), ("05-mission", ad_mission), ("06-calm-ein-atemzug", ad_atemzug),
    ("07-wo-hakt-dein-tag", ad_quiz), ("08-duft-wird-signal", ad_signal_steps), ("09-vier-momente", ad_vier_momente),
    ("10-erste-30-tage", ad_30_tage), ("11-focus-angebot", ad_focus_offer), ("12-kompass", ad_kompass)]

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "html"), exist_ok=True)
    for key, fn in ADS:
        for fmt in ("45", "916"):
            open(os.path.join(ROOT, f"{key}_{fmt}.html"), "w").write(fn(fmt))
    print(len(ADS) * 2, "html files")
