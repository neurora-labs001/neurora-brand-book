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
- **18a–d Roll-On Signal-Ring** (alle vier Zustände): ersetzt die dunkle Anzeige „Kopf noch an? Licht aus, Duft an.“. Neue Botschaft „Ein Duft. Ein Moment. Dein Signal für …“. Creme, Frosted, Mood Dots, Signal-Line-Ring und die offene Box als Hero. Die Callouts bleiben, aus „4 ätherische Öle“ wird „Rund 95 Rituale pro Roll-On“.
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
