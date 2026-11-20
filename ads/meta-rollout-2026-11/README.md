# Meta Ads · Rollout KW 47–49 / 2026

Built 1:1 from the live webshop sections (theme NEURORA MOOD 6.1) and Brand Book 2.0. Webshop photos only, Manrope + EB Garamond Italic, original logo.

- `feed-4x5/` 1080×1350 (Feed) · `story-9x16/` 1080×1920 (Reels/Stories; all copy inside the Meta safe zone, bottom band is decorative only)
- `overview-*.jpg` contact sheets
- `source/` generator (`gen2.py` = current version, `render.js` = Playwright renderer). Fonts and webshop images are not committed; see the asset list in `gen2.py`.

| # | Ad | State | Funnel role |
|---|---|---|---|
| 01 | Der Körper liegt. Der Kopf nicht. | SLEEP | Cold · Kennst du das |
| 02 | Du bist zu Hause. Aber nicht ganz da. | CALM | Cold · Kennst du das |
| 03 | Du bist beschäftigt. Aber nicht bei der Sache. | FOCUS | Cold · Kennst du das |
| 04 | Founder-Zitat Philip | Brand | Cold / warm · Trust |
| 05 | Auf Wissenschaft gebaut. | Brand | Warm · Trust |
| 06 | Ein Atemzug. Jeden Tag im selben Moment. | CALM | Cold · Mechanism + founder video |
| 07 | Wo hakt dein Tag? | All four | Cold · Quiz entry |
| 08 | Ein Duft wird zum Signal. Durch Wiederholung. | Brand | Cold · Mechanism |
| 09 | Vier Momente. Ein Duft für jeden. | All four | Warm · System |
| 10 | Die ersten 30 Tage. | Brand | Warm · Objection (time) |
| 11 | Alles für deinen Fokus-Block. €89 | FOCUS | Retargeting · Offer |
| 12 | Kompass: Für alle, die mehr über ihren Duft lernen wollen. | FOCUS | Cold · Curiosity |
| 13 | Finde deinen Moment. (Quiz) | SLEEP visual | Cold · Quiz |
| 14 | Welchen Moment deines Tages willst du verändern? (Quiz) | All four | Cold · Quiz |
| 15 | Kein Parfum für andere. Keine Kapsel zum Schlucken. | Brand | Cold · Belief (Glossar) |
| 16 | Wir sagen dir genau, was gemessen wurde. Und was nicht. | Brand | Cold · Skeptic trust (Glossar) |

Before launch: claims marked in the strategy doc (§9) still need Claims Register clearance, in particular „auf Abruf" (06, 10, 13) and the study reference in 10.

## Runde 3 (20.11.2026)

- **17 Gratis-Goodie** (Retargeting): „Ein Roll-On geht aufs Haus. 🎁“. Zeigt die vier Geschenk-Boxen, ohne Schwellenwert, ohne Enddatum. Ziel: `/collections/sets`.
- **18a–d Roll-On Signal-Ring** (alle vier Zustände): ersetzt die dunkle Anzeige „Kopf noch an? Licht aus, Duft an.“. Neue Botschaft „Ein Duft. Ein Moment. Dein Signal für …“. Creme, Frosted, Mood Dots, Signal-Line-Ring und die offene Box als Hero. Die Callouts bleiben, aus „4 ätherische Öle“ wurde zuerst „Rund 95 Rituale pro Roll-On“, siehe Runde 5.
- Generator: `source/gen3.py`. Freisteller der Boxen: `source/boxcut.py` (harter Freisteller mit leichtem Kontrast- und Farb-Boost, ohne Fotoschatten).
- **19a–d Roll-On Signal-Ring, Flasche ohne Verpackung**: gleiche Texte wie 18a–d. Die Flasche steht leicht geneigt in einem dichteren Zustandsfarb-Kreis. Durch den Kreis läuft eine feine, zustandsspezifische Signal Line hinter der Flasche. In 9:16 entfällt das untere Signal-Band (eine Signal Line pro Fläche).
  Die Flaschen sind aus dem Brand-Atlas-Packshot „Sleep Roll-On“ (Line-up) freigestellt. Der seitliche Farbstreifen wurde retuschiert, weil der KI-Packshot dort verfälschten Text zeigt („SCEN YOU CAN FEEY…“). Sobald echte Freisteller-Fotos der Flaschen vorliegen, bitte austauschen. Skript: `source/bottlecut.py`.
- **Fix 18a–d (20.11.)**: Der Box-Freisteller ist jetzt sauber, ohne grauen Fotoschatten (die kaputte Ecke unten links bei Calm ist behoben). Die Box sitzt im Kreis, der Ring liegt hinter der Box. Der Kreis ist in der Zustandsfarbe dicht gefüllt, wie bei 19, mit derselben feinen Signal Line. Das Bild hat etwas mehr Kontrast und Farbe. In 9:16 entfällt das untere Signal-Band.

## Runde 4 (20.11.2026)

- **Signal Lines neu gezeichnet** (alle Anzeigen): mathematisch glatte Kurven. Sleep klingt aus, Calm zeigt gleichmäßige Atem-Schleifen, Focus geht vom Zickzack in eine gerade Linie über, Activate steigt weich an. Dazu saubere Eckradien an den Brücken.
- **01–03 Vorher/Nachher**: Eyebrow als Frage mit Emoji („🌙 Sieht dein Abend so aus?“, „🛋️ … Feierabend …“, „💻 … Nachmittag …“). Statt des Produkt-Chips gibt es ein Frosted Board mit der Produktreihe (01: Textilspray-Reihe, 02/03: Roll-On-Reihe, eigener Zustand hervorgehoben) und CTA. In 9:16 ist alles zentriert und nichts abgeschnitten.
- **18/19 Roll-On-Ring**: Glas-Scheibe statt flacher Farbfläche. Die Bögen sind oben und unten hervorgehoben, sodass beide Benefit-Paare verbunden sind. Die Callouts stehen als Frosted Pills mit größeren Punkten und fetten Schlüsselwörtern.
- Layout-Fix für alle Anzeigen: Elemente schrumpfen nicht mehr unbemerkt (keine abgeschnittenen Boards). Die Mindestschriftgröße liegt überall bei 18 px.
- **04 Founder-Zitat**: Das Porträt von der Startseite (Poster des Gründer-Videos, Philip vor dem Neurora-Regal) ist jetzt das Hero-Bild, im Frosted Board mit „Philip über das Ritual“-Play-Badge. Der runde Avatar und das Produktfoto entfallen.
- **01–03 Frage-Badge**: Die Emojis 🌙, 🛋️ und 💻 sind entfernt. Die Frage steht jetzt als Navy-Pille im Stil des Gratis-Goodie-Badges („SIEHT DEIN ABEND SO AUS“) und endet in einem ❓ in einer leuchtenden Creme-Scheibe.
  Es gibt zusätzlich animierte Versionen: Das ❓ wackelt, wird kurz größer und leuchtet auf, als Loop von 4,8 s. Dateien: `video-4x5/` und `video-9x16/` (MP4, H.264). In Meta als Video-Anzeige hochladen, mit denselben Texten wie die Standbilder. Skript: `source/anim.js`.
- **Runde 5, Callouts 18/19**: „Duft mit Funktion · wissenschaftliche Formel“ ersetzt „Rund 95 Rituale“. Dazu „Immer dabei · 10 ml für jede Tasche“, „Ein Atemzug · und der Tag beginnt / dann tauchst du ab / ab jetzt ist Feierabend / und der Tag ist vorbei“ und „30 Tage testen · Passt nicht? Geld zurück.“ Die Punkte sitzen flacher am Ring, damit alle Pills zweizeilig passen.
  **Claims-Check offen:** „wissenschaftliche Formel“ vor dem Livegang im Claims Register freigeben lassen. Live freigegeben ist auf der Seite „Auf Wissenschaft gebaut“.

## Animierte Video-Anzeigen (20.11.2026)

22 MP4s (H.264, 30 fps), je in `video-4x5/` und `video-9x16/`:

- **01–03 Vorher/Nachher (7 s)**: Die Signal Line zeichnet sich von links nach rechts, erst die unruhige Vorher-Geste, dann die ruhige Nachher-Geste. Die O-Marke ploppt am Wechsel auf und atmet danach. Der Endpunkt leuchtet auf. Die ❓-Pille schwebt, das ❓ wackelt und leuchtet. In 9:16 zeichnet sich zusätzlich die Band-Linie unten.
- **18a–d und 19a–d Roll-On-Ring (8 s, nahtloser Loop)**: Ein Signal-Komet mit Leuchtschweif läuft einmal 360° um den Ring. Erreicht er einen Benefit-Punkt, pulsiert der Punkt und die Benefit-Pille hebt sich mit Zustandsfarb-Kontur hervor (Reihenfolge: Ein Atemzug → 30 Tage → Immer dabei → Duft mit Funktion). Das Produkt schwebt leicht.

Die Animation ist nur im Video-Render aktiv (`body.anim`), die JPG-Standbilder bleiben unverändert. Neu rendern: `node source/anim.js <filter> <sekunden>`.

## Videos v2: alle 26 Anzeigen, 11 Sekunden (20.11.2026)

52 MP4s (26 Anzeigen × 4:5 und 9:16, H.264, 30 fps, je 11 s), ruhigeres Tempo mit mehr Zeit zum Lesen:

- **01–03**: Die Signal Line zeichnet sich über etwa 5 s, danach bleibt das Bild 4–5 s ruhig stehen. Die ❓-Pille schwebt langsam.
- **18/19 Ring**: Der Komet braucht 11 s pro Runde (nahtloser Loop), die Benefit-Pillen leuchten nacheinander auf.
- **04–17**: Die Elemente bauen sich nacheinander auf (Logo, Headline, Boards, dann Kacheln und Zeilen gestaffelt). Linien zeichnen sich, Fotos zoomen langsam (Ken Burns), die Mood Dots pulsieren, das 🎁 hüpft und der CTA pulsiert bei 6 s und 9 s.

## Videos v3: neue Video-Layouts (20.11.2026)

- **01–03 Vorher/Nachher (13,5 s)**: Erst die Frage-Badge, dann die Headline, beide Wort für Wort, groß und zentriert, danach wandern sie nach oben. Die Karte „Ohne Signal“ kommt von links in voller Breite (große Schrift, ein Statement, Schlüsselwörter fett). Die Signal Line zeichnet sich, „Mit [Zustand]“ übernimmt. Danach rutscht der Block hoch und der Produkt-Slider (Textilspray- und Roll-On-Reihe) läuft vollflächig ein. Ohne „Der eigentliche Grund“, ohne „Choose the moment.“, ohne Band unten.
- **12a Mood-Kompass (14 s)**: „✦ Der Neurora Mood-Kompass“, dann „Was steckt in deinem Duft?“. Der Kompass ohne Karte zeichnet sich langsam, der Stern sitzt mittig. Danach Fakten-Chips (23 Duftmoleküle · 8 Duftfamilien · 4 Momente). Der Kompass scrollt weg und große Produkte gleiten langsam ein. Zum Schluss der CTA „Finde deinen Duft im Kompass →“.
- **18a–d und 19a–d Roll-On-Ring (12,5 s)**: Ein großes Statement pro Zustand (Activate: „Nie wieder Morgenmuffel!“, Focus: „Schluss mit Tab-Chaos!“, Calm: „Feierabend? Kopf macht Überstunden.“, Sleep: „Schluss mit Kopfkino im Bett!“). Die Benefits poppen nacheinander auf, sobald der Komet sie erreicht. Am Ende steht „[ZUSTAND] Roll-On“ groß mit gezeichneter Signal-Unterstreichung, ohne Preis und Button.
- Claims-Check offen: „Nie wieder Morgenmuffel!“ (absolutes Versprechen). Der Kompass-Disclaimer zu Duftfamilien wurde auf Wunsch entfernt.
