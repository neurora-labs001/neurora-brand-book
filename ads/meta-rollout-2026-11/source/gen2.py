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
.eyebrow{font-size:17px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--c)}
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
.lbl{font-size:15px;font-weight:600;letter-spacing:.18em;text-transform:uppercase}
.it{font-family:'EB Garamond';font-style:italic;font-weight:400}
.chip{display:flex;align-items:center;gap:20px;background:#fff;border-radius:24px;padding:14px 26px 14px 14px;box-shadow:0 14px 34px -24px rgba(13,27,51,.4)}
.chip img{width:88px;height:88px;object-fit:cover;border-radius:16px}
.chip .t{font-size:26px;font-weight:600;letter-spacing:-.01em}
.chip .s{font-size:19px;color:rgba(13,27,51,.55);margin-top:4px}
.chip .arr{margin-left:auto;font-size:36px;color:var(--c);font-weight:300}
.btn{display:inline-flex;align-items:center;gap:16px;background:#0D1B33;color:#F6F3EC;border-radius:999px;padding:24px 40px;font-size:26px;font-weight:600}
.grow{flex:1}
.center{text-align:center}
"""

DOTS = "<span class='dots'>" + "".join(f"<i style='background:{S[s]['c']}'></i>" for s in ("activate", "focus", "calm", "sleep")) + "</span>"

def band(st):
    from gen import gesture_before, gesture_after
    c = S[st]; y = 60
    d1 = "M 60 %d" % y + gesture_before(st, 60, 430, y); d2 = "M 482 %d" % y + gesture_after(st, 482, 1020, y)
    dots = "".join("<circle cx='%d' cy='150' r='8' fill='%s'/>" % (60 + i * 30, S[k]['c']) for i, k in enumerate(("activate", "focus", "calm", "sleep")))
    return ("<svg style='position:absolute;left:0;bottom:120px;z-index:0;opacity:.55' width='1080' height='190' viewBox='0 0 1080 190'>"
            "<path d='%s' fill='none' stroke='%s' stroke-opacity='.5' stroke-width='3' stroke-linecap='round'/>"
            "<path d='%s' fill='none' stroke='%s' stroke-width='4' stroke-linecap='round'/>%s%s</svg>") % (d1, c['c'], d2, c['c'], o_mark(456, y, st, 20), dots)

def page(title, st, fmt, body, css=""):
    c = S[st]
    H = 1350 if fmt == "45" else 1920
    pad = "64px 60px 60px" if fmt == "45" else "250px 60px 370px"   # 9:16: keep clear of Reels/Stories UI
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
 dict(key="01-sleep-vorher-nachher", st="sleep", eyebrow="So sieht dein Abend gerade aus", a="Der Körper liegt.", b="Der Kopf nicht.",
      off_t="Licht aus. Gedanken noch an.", off=[("22:50", "Licht aus. Und plötzlich fällt dir alles ein, was morgen ansteht."), ("23:40", "Du drehst das Kissen um und rechnest, wie viele Stunden noch bleiben.")],
      on_t="Licht aus. Der Tag ist vorbei.", on=[("22:16", "Ein Sprühstoß aufs Kissen, Roll-On aufs Handgelenk."), ("22:17", "Dein Signal: Der Tag ist vorbei.")],
      why="Dir fehlt keine Müdigkeit. Dir fehlt ein Ende für den Tag.", img="nr-set-sleep-hero.webp", ct="Dein Abend-Signal holen", cs="SLEEP Komplett-Set · €89"),
 dict(key="02-calm-vorher-nachher", st="calm", eyebrow="So sieht dein Feierabend gerade aus", a="Du bist zu Hause.", b="Aber nicht ganz da.",
      off_t="Zu Hause. Kopf noch im Meeting.", off=[("18:40", "Auf dem Heimweg spielst du das Meeting noch einmal durch."), ("19:30", "Am Tisch nickst du, hörst aber nur halb zu.")],
      on_t="Laptop zu. Kopf frei.", on=[("18:06", "Roll-On aufs Handgelenk. Ein Atemzug."), ("18:07", "Dein Signal: Ab jetzt ist Feierabend.")],
      why="Dir fehlt kein Feierabend. Dir fehlt ein Schlusspunkt.", img="nr-set-calm-hero_d9e1c46a-abd5-4b2b-b375-fb6d6ae9d035.webp", ct="Dein Feierabend-Signal holen", cs="CALM Komplett-Set · €89"),
 dict(key="03-focus-vorher-nachher", st="focus", eyebrow="So sieht dein Nachmittag gerade aus", a="Du bist beschäftigt.", b="Aber nicht bei der Sache.",
      off_t="Viel beschäftigt. Wenig geschafft.", off=[("14:55", "Zwölf Tabs offen. Keiner davon fertig."), ("15:10", "Dritter Kaffee. Oder doch der Riegel aus der Schublade.")],
      on_t="Eine Aufgabe. Ganz bei der Sache.", on=[("14:56", "Roll-On aufs Handgelenk. Ein Atemzug."), ("14:57", "Dein Signal zum Abtauchen.")],
      why="Dir fehlt keine Konzentration. Dir fehlt ein klarer Neustart.", img="nr-set-focus-hero_651397b1-0fd3-4ca6-a8b7-f7041f0dc4a8.webp", ct="Dein Fokus-Signal holen", cs="FOCUS Komplett-Set · €89"),
]

def ad_ba(d, fmt):
    st = d["st"]
    rows = lambda rs, on: "".join(
        f"<div style='display:grid;grid-template-columns:70px 1fr;gap:10px;padding:18px 0;border-top:1px solid rgba(13,27,51,.07);font-size:23.5px;line-height:1.38'>"
        f"<span style='font-size:16px;font-weight:600;letter-spacing:.04em;padding-top:4px;color:{'var(--c)' if on else 'rgba(13,27,51,.5)'}'>{t}</span>"
        f"<span style='color:{'#0D1B33' if on else 'rgba(13,27,51,.7)'}'>{x}</span></div>" for t, x in rs)
    card = lambda on: (
        f"<div style='border-radius:28px;padding:28px 26px 14px;{'background:var(--soft);border:1px solid color-mix(in srgb,var(--c) 14%,transparent)' if on else 'background:rgba(242,241,238,.9);border:1px solid rgba(13,27,51,.06)'}'>"
        + (f"<div class='lbl' style='color:var(--c)'><span class='dot' style='width:10px;height:10px;margin-right:12px'></span>Mit {S[st]['name']}</div>" if on else
           "<div class='lbl' style='color:rgba(13,27,51,.5)'>⦸&nbsp; Ohne Signal</div>")
        + f"<div style='font-size:32px;font-weight:300;letter-spacing:-.035em;line-height:1.12;margin:14px 0 14px;color:{'var(--c)' if on else 'rgba(13,27,51,.8)'}'>{d['on_t'] if on else d['off_t']}</div>"
        + rows(d["on"] if on else d["off"], on) + "</div>")
    body = (top(st) + "<div class='grow'></div>"
            + headline(d["eyebrow"], d["a"], d["b"], 92, center=True, grey=False)
            + f"<div style='margin:20px -10px -4px'>{signal_bridge(st, 980, drop=86, lx=245, rx=740)}</div>"
            + f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px'>{card(False)}{card(True)}</div>"
            + f"<div style='background:#121B33;color:#F6F3EC;border-radius:24px;padding:24px 28px;margin-top:16px'>"
              f"<div class='lbl' style='font-size:13px;color:var(--g)'>Der eigentliche Grund</div>"
              f"<div style='font-size:30px;font-weight:300;letter-spacing:-.02em;line-height:1.2;margin-top:8px'>{d['why']}</div></div>"
            + f"<div style='margin-top:18px'>{chip(d['img'], d['ct'], d['cs'])}</div>" + "<div class='grow'></div>")
    return page(d["key"], st, fmt, body)

# ---------- 04 Founder ----------
def ad_founder(fmt):
    st = "activate"
    body = (top(st, "dots")
      + "<div class='grow' style='display:flex;flex-direction:column;justify-content:center'>"
      f"<div style='width:230px;height:230px;border-radius:50%;padding:10px;background:rgba(255,255,255,.75);box-shadow:0 22px 50px -32px rgba(13,27,51,.35)'>"
      f"<img src='{A}nr-philip-portrait-3c.jpg' style='width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 20%'></div>"
      f"<div class='it' style='font-size:130px;line-height:.6;color:var(--c);height:60px;margin-top:34px'>“</div>"
      f"<div style='font-size:60px;font-weight:300;letter-spacing:-.04em;line-height:1.12'>Duft begleitet uns jeden Tag, meist unbewusst. Mit Neurora Labs machen wir ihn zu einem <span style='color:var(--c)'>bewussten Werkzeug</span>.</div>"
      f"<div style='display:flex;align-items:center;gap:16px;margin-top:30px'><div style='width:46px;height:46px;border-radius:10px;background:#0D1B33;display:grid;place-items:center'>{svg_logo('mono', '#F6F3EC', h=22)}</div>"
      f"<div class='lbl' style='color:rgba(13,27,51,.6);font-size:16px'>Philip Huber, Founder &amp; CEO</div></div></div>"
      f"<div class='board' style='padding:12px;margin-top:30px'><img src='{A}nr-rituale-66-tag-1.jpg' style='display:block;width:100%;height:300px;object-fit:cover;object-position:62% 55%;border-radius:22px'></div>")
    return page("Founder", st, fmt, body)

# ---------- 05 Mission (navy, product centre) ----------
def ad_mission(fmt):
    st = "sleep"
    css = "body{background:#0B1630}body::before{background:radial-gradient(700px 620px at 100% 0%,rgba(78,61,152,.6),transparent 70%),radial-gradient(620px 520px at 0% 100%,rgba(181,71,31,.2),transparent 70%)}"
    body = (top(st, "<div class='slogan' style='color:rgba(246,243,236,.7)'>Choose the <b style='color:#C5B0F3'>moment.</b></div>", dark=True)
      + "<h1 style='font-size:84px;color:#F6F3EC'>Auf Wissenschaft gebaut.<span class='acc' style='color:rgba(246,243,236,.5)'>Damit deine Stimmung dir gehört.</span></h1>"
      + "<div class='grow' style='display:flex;align-items:center;padding:34px 0'>"
      f"<div style='width:100%;border-radius:32px;overflow:hidden;box-shadow:0 40px 80px -40px rgba(0,0,0,.6);border:1px solid rgba(255,255,255,.12)'>"
      f"<img src='{A}nr-set-sleep-hero.webp' style='display:block;width:100%;height:560px;object-fit:cover;object-position:50% 58%'></div></div>"
      + f"<div class='lbl' style='font-size:15px;color:rgba(246,243,236,.65)'><span class='dot' style='--c:#B5471F;--g:#F6AE8E;width:9px;height:9px;margin-right:12px'></span>Mission</div>"
      f"<div style='font-size:38px;font-weight:300;letter-spacing:-.03em;line-height:1.2;color:#F6F3EC;margin-top:14px'>Wir übersetzen olfaktorische Wissenschaft in Werkzeuge für deinen Alltag.</div>")
    return page("Mission", st, fmt, body, css)

# ---------- 06 Ein Atemzug (CALM, Philip video) ----------
def ad_atemzug(fmt):
    st = "calm"
    times = [("07:00", "activate"), ("09:30", "focus"), ("18:30", "calm"), ("22:00", "sleep")]
    tabs = "".join(
        f"<div style='flex:1;text-align:center;padding:14px 0 12px;border-radius:18px;{'background:#fff;box-shadow:0 10px 26px -18px rgba(13,27,51,.4);' if s=='calm' else ''}'>"
        f"<span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:10px;height:10px;{'' if s=='calm' else 'box-shadow:none;'}'></span>"
        f"<div style='font-size:21px;font-weight:600;margin-top:6px'>{t}</div><div class='lbl' style='font-size:12px;color:{S[s]['c']};margin-top:3px'>{S[s]['name']}</div></div>" for t, s in times)
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
      + "<div style='font-size:19px;color:rgba(13,27,51,.55);margin-top:14px'>Philip, Gründer von Neurora, über sein Ritual am Feierabend.</div>")
    return page("Ein Atemzug", st, fmt, body)

# ---------- 07 Wo hakt dein Tag ----------
def ad_quiz_tiles(fmt):
    st = "sleep"
    items = [("activate", "07:00", "Morgens schwer in Gang?"), ("focus", "09:30", "Nachmittagstief um 15 Uhr?"),
             ("calm", "18:30", "Kopf noch im Meeting?"), ("sleep", "22:00", "Im Bett und noch hellwach?")]
    cards = "".join(
        f"<div style='background:linear-gradient(120deg,#fff 55%,color-mix(in srgb,{S[s]['g']} 28%,#fff));border-radius:26px;padding:28px 30px;box-shadow:0 14px 34px -26px rgba(13,27,51,.35);display:flex;align-items:center;gap:22px'>"
        f"<div style='flex:1'><div class='lbl' style='font-size:15px;color:{S[s]['c']}'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:10px;height:10px;margin-right:12px'></span>{t} · {S[s]['name']}</div>"
        f"<div style='font-size:36px;font-weight:300;letter-spacing:-.03em;margin-top:12px'>{h}</div></div>"
        f"<div style='width:44px;height:44px;border-radius:50%;border:1.5px solid rgba(13,27,51,.15);flex:none'></div></div>" for s, t, h in items)
    body = (top(st, "dots")
      + headline("Kennst du das?", "Wo hakt", "dein Tag?", 112)
      + "<div class='grow' style='min-height:30px'></div>"
      + f"<div style='display:flex;flex-direction:column;gap:14px'>{cards}</div>"
      + "<div style='display:flex;justify-content:space-between;align-items:center;margin-top:28px'>"
        "<div style='font-size:22px;color:rgba(13,27,51,.65);max-width:520px;line-height:1.4'>Tipp an, was du kennst. Dann zeigen wir dir, wo dein Ritual anfängt.</div>"
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
        "<div style='font-size:18px;color:rgba(246,243,236,.6);margin-top:14px'>Philip, Gründer von Neurora</div></div>")
    return page("Duft wird Signal", st, fmt, body)

# ---------- 09 Vier Momente ----------
def ad_vier_momente(fmt):
    st = "sleep"
    m = [("activate", "07:00", "Dein Start."), ("focus", "09:30", "Dein Fokus-Block."), ("calm", "18:30", "Dein Feierabend."), ("sleep", "22:00", "Dein Licht aus.")]
    cards = "".join(
        f"<div style='border-radius:30px;padding:28px 26px 30px;background:linear-gradient(160deg,rgba(255,255,255,.94) 35%,color-mix(in srgb,{S[s]['g']} 34%,#fff));box-shadow:0 18px 40px -30px rgba(13,27,51,.35);border:1px solid rgba(255,255,255,.95);display:flex;flex-direction:column'>"
        f"<div style='display:flex;justify-content:space-between;align-items:center'><span class='it' style='font-size:44px;color:{S[s]['c']}'>{t}</span>"
        f"<span class='lbl' style='font-size:13px;color:{S[s]['c']};background:#fff;border-radius:999px;padding:9px 14px'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:9px;height:9px;box-shadow:none;margin-right:8px'></span>{S[s]['name']}</span></div>"
        f"<div class='grow' style='min-height:20px'></div><div style='margin:0 0 18px'>{signal_inline(s, 410, 54, 0.36)}</div>"
        f"<div style='font-size:46px;font-weight:300;letter-spacing:-.045em;line-height:1.05'>{h}</div></div>" for s, t, h in m)
    body = (top(st, "dots")
      + headline("Dein Tag in vier Ritualen", "Vier Momente.", "Ein Duft für jeden.", 92)
      + "<p class='lead' style='margin-top:18px'>Fang mit einem Moment an. Die anderen kommen dazu, wenn du willst.</p>"
      + f"<div style='display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:14px;margin-top:34px;flex:1'>{cards}</div>")
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
      + "<div style='margin-top:26px;font-size:22px;color:rgba(13,27,51,.7)'><b style='color:#0D1B33;font-weight:600'>Einen Tag ausgelassen?</b> Macht nichts. Mach am nächsten Tag einfach weiter.</div>")
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
      "<div style='position:absolute;right:24px;bottom:22px;width:130px;height:130px;border-radius:50%;background:rgba(255,255,255,.94);display:grid;place-items:center;text-align:center'><div><div style='font-size:42px;font-weight:300;color:var(--c);line-height:1'>30</div><div class='lbl' style='font-size:11px;margin-top:4px'>Tage testen</div></div></div></div>"
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
                  f"<span style='width:44px;height:44px;border-radius:50%;background:#1F4A3D;color:#fff;display:grid;place-items:center;font-size:17px;font-weight:600;box-shadow:0 0 0 5px rgba(138,211,189,.35)'>{n}</span>{t}</span>"
                  for n, t in [("08", "1,8-Cineol"), ("09", "Kampfer"), ("10", "Verbenon")])
    body = (top(st, "dots")
      + "<div class='lbl' style='color:var(--c);font-size:16px'><span class='dot' style='width:10px;height:10px;margin-right:14px'></span>Neurora Kompass · Mood on Demand</div>"
      + "<h1 style='margin-top:18px;font-size:76px'>Für alle, die mehr über ihren Duft <span style='color:var(--c)'>lernen wollen.</span></h1>"
      + "<div class='board glow' style='margin-top:34px;padding:32px 32px 0;flex:1;display:flex;flex-direction:column'>"
      "<div class='lbl' style='font-size:15px;color:rgba(13,27,51,.55)'><span class='dot' style='width:10px;height:10px;margin-right:12px'></span>Jetzt · 12:46</div>"
      "<div style='display:flex;align-items:baseline;gap:22px;margin-top:10px'><span style='font-size:92px;font-weight:300;letter-spacing:-.045em;color:var(--c);line-height:1'>Scharf</span>"
      "<span class='it' style='font-size:30px;color:rgba(13,27,51,.7)'>Mittag · 12:00</span></div>"
      "<p style='font-size:22px;line-height:1.45;color:rgba(13,27,51,.7);margin-top:12px'>Durchdringend, kampferartig, präzise. Die Noten für die Stunden am Schreibtisch.</p>"
      f"<div style='display:flex;gap:12px;flex-wrap:wrap;margin-top:18px'>{mol}</div>"
      f"<div style='flex:1;min-height:300px;margin:16px -32px 0;overflow:hidden;display:flex;align-items:flex-start'>{dial_svg(1000)}</div></div>"
      "<p class='it' style='font-size:20px;line-height:1.4;color:rgba(13,27,51,.55);margin-top:16px'>Duftfamilien beschreiben den Charakter eines Moleküls, keine Wirkung.</p>")
    return page("Kompass", st, fmt, body)

# ---------- 13 Mood-Quiz Intro ----------
def ad_quiz_intro(fmt):
    st = "sleep"
    body = (top(st, "dots")
      + "<div class='lbl' style='font-size:16px;color:#0D1B33'><span class='dot' style='--c:#0D1B33;--g:#E6E1F4;width:11px;height:11px;margin-right:14px'></span>Dein Ritual · 4 Fragen</div>"
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
      + "</span><span class='lbl' style='font-size:15px;color:rgba(13,27,51,.55)'>Frage 1 / 4</span></div>"
      + "<h1 style='font-size:80px;margin-top:22px'>Welchen Moment deines Tages willst du <span style='color:var(--c)'>verändern?</span></h1>"
      + "<div class='grow' style='min-height:30px'></div>"
      + f"<div class='board glow' style='padding:18px;display:flex;flex-direction:column;gap:12px'>{rows}</div>"
      + "<div style='margin-top:26px;display:flex;justify-content:space-between;align-items:center'><div class='slogan'>In unter einer Minute zu <b>deinem Ritual.</b></div><div class='btn'>Quiz starten →</div></div>")
    return page("Quiz Frage", st, fmt, body)

# ---------- 15 Glossar: MoodTech ----------
def ad_gloss_moodtech(fmt):
    st = "sleep"
    states = "".join(f"<div style='flex:1;text-align:center'><span class='dot' style='--c:{S[s]['c']};--g:{S[s]['g']};width:14px;height:14px'></span><div class='lbl' style='font-size:14px;color:{S[s]['c']};margin-top:14px'>{S[s]['name']}</div></div>" for s in ("activate", "focus", "calm", "sleep"))
    body = (top(st, "dots")
      + "<div class='eyebrow grey'>Glossar · MoodTech</div>"
      + "<h1 style='font-size:94px;margin-top:18px'>Kein Parfum für andere.<br>Keine Kapsel zum Schlucken.<span class='acc'>Ein Duft für deinen Moment.</span></h1>"
      + "<div class='grow' style='min-height:30px'></div>"
      + "<div class='board glow' style='padding:38px 38px 34px'>"
        "<div style='font-size:30px;font-weight:300;letter-spacing:-.02em;line-height:1.35'>Düfte, die für einen bestimmten Moment deines Tages gemacht sind und als kurzes, wiederkehrendes Ritual genutzt werden.</div>"
        f"<div style='margin:30px 0 26px'>{signal_inline('sleep', 920, 60, 0.4)}</div><div style='display:flex'>{states}</div></div>"
      + "<div style='margin-top:26px;display:flex;justify-content:space-between;align-items:center'><div class='slogan' style='font-size:24px'>Mood on Demand. <b>Choose the moment.</b></div></div>")
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

ADS = [(d["key"], (lambda d: (lambda f: ad_ba(d, f)))(d)) for d in BA] + [
    ("04-founder-zitat", ad_founder), ("05-mission", ad_mission), ("06-calm-ein-atemzug", ad_atemzug),
    ("07-wo-hakt-dein-tag", ad_quiz_tiles), ("08-duft-wird-signal", ad_signal_steps), ("09-vier-momente", ad_vier_momente),
    ("10-erste-30-tage", ad_30), ("11-focus-angebot", ad_offer), ("12-kompass", ad_kompass),
    ("13-mood-quiz-intro", ad_quiz_intro), ("14-mood-quiz-frage", ad_quiz_q),
    ("15-glossar-moodtech", ad_gloss_moodtech), ("16-glossar-wissenschaft", ad_gloss_science)]

if __name__ == "__main__":
    for f in os.listdir(ROOT):
        if f.endswith(".html") and ("_45" in f or "_916" in f):
            os.remove(os.path.join(ROOT, f))
    for key, fn in ADS:
        for fmt in ("45", "916"):
            open(os.path.join(ROOT, f"{key}_{fmt}.html"), "w").write(fn(fmt))
    print(len(ADS) * 2, "html files")
