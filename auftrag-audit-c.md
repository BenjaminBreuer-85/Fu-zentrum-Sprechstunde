# Auftrag: Audit-Kosmetikpunkte C2, C4, C5, C6 (app.html + Landingpage index.html)

Stand: 28.08.2026. Entscheidungen des Autors aus der Audit-Durchsprache. Die Datenpunkte C1 (Gruppentitel „Diabetischer Fuß / Infekt" im Sprechstundenbrief) und C3 (Ausfüll-Platzhalter der ME-Zusatztexte auf eckige Klammern) sind bereits direkt in diagnosen.json/optexte.json erledigt und committet. C7 (Tippfehler „der patient") steckt im Auftrag auftrag-me-vorschau-mobil.md.

## C2 · Scores-Zeile im Sprechstundenbrief nur bei Eingabe

Die Zeile „- Scores: EFAS /24, EFAS Sport /16, AOFAS /100, VAS Belastung /10" wird derzeit auch gedruckt, wenn kein einziger Wert eingetragen ist. Änderung: Zeile nur ausgeben, wenn mindestens ein Score-Wert eingegeben wurde; dabei nur die tatsächlich befüllten Scores nennen.

## C4 · Letzte Emojis in den Auswahl-Leisten entfernen (app.html)

- VORBEREITUNG-Chips: „💊 Single-Shot" → „Single-Shot", „🩸 Blutsperre" → „Blutsperre", „💉 LA" → „LA"
- SEKTION-Zeile: „🦶 Fuß / Sprunggelenk" → „Fuß / Sprunggelenk", „🦴 UC" → „UC", „🦿 Endo" → „Endo" (WS entfällt ohnehin per auftrag-audit-b.md)
- Die Emoji-Kacheln des HAUPTMENÜS bleiben unverändert (bewusstes Gestaltungselement).

## C5 · Untertitel für zwei Menü-Kacheln

- Klassifikationen: **„47 Graduierungen mit Quelle und DOI"**
- Röntgen & Messmethoden: **„26 Messungen mit Normwert und Referenzbild"**

(Formatierung wie bei den übrigen Kachel-Untertiteln.)

## C6 · Landingpage: zwei Gedankenstriche in Statusmeldungen (index.html)

- Danke-Meldung: „Ihre Einladung kommt in wenigen Minuten von kontakt@fuss-track.de — bitte auch den Spam-Ordner prüfen." → „… von kontakt@fuss-track.de, bitte auch den Spam-Ordner prüfen."
- Sandbox-Hinweis: „⚠️ Testbetrieb — dieser Kauf läuft gegen die Paddle-Sandbox …" → „⚠️ Testbetrieb: Dieser Kauf läuft gegen die Paddle-Sandbox …"

## Gegenprobe

Brief ohne Scores → keine Scores-Zeile; Brief mit einem Score → nur dieser erscheint. OP-Bericht-Kopf ohne Emojis in VORBEREITUNG/SEKTION. Menü zeigt die zwei neuen Untertitel. Landingpage-Statusmeldungen ohne Gedankenstrich.

## Deploy

`app.html` und `index.html` committen/pushen. Bucket: optexte.json und diagnosen.json stehen bereits als offene Uploads in DEPLOY.md Abschnitt D — dieser Auftrag ergänzt keine weiteren.
