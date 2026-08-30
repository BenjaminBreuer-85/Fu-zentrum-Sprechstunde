# Auftrag: AOFAS durch FAOS ersetzen (app.html) — verschlankte Fassung

Stand: 30.08.2026. **Diese Fassung ersetzt die vom 29.08.** Der damalige Punkt 2 (Scores-Zeile hinter einen Schalter legen, Standard aus) ist erledigt und entfällt: Die inzwischen umgesetzte Lösung mit vier Eingabefeldern („SCORES — nur Erhobenes wird gedruckt", Zeile entfällt ohne Werte) erfüllt die Absicht des Autors bereits besser. Bitte daran nichts ändern.

Übrig bleibt nur die Umbenennung: Der AOFAS-Score wird in der App nicht mehr verwendet; an seine Stelle tritt der **FAOS** (Foot and Ankle Outcome Score) als Gesamtwert von 0 bis 100. AOFAS steht aktuell an drei Stellen in app.html:

1. Brief-Ausgabe (ca. Z. 2115): `scores.push("AOFAS " + scAofas.trim() + "/100")` → `"FAOS "` (der Wertebereich /100 bleibt).
2. Eingabefeld-Beschriftung (ca. Z. 2795): `["AOFAS","/100",scAofas,setScAofas]` → Label `"FAOS"`.
3. Tour-Text (ca. Z. 8497): „…EFAS, EFAS Sport, AOFAS und die VAS unter Belastung…" → „…FAOS…". Rest des Satzes unverändert.

Die Variablennamen (`scAofas`/`setScAofas`) dürfen mit umbenannt werden, müssen aber nicht — sichtbarer Text ist das Kriterium.

## Gegenprobe

Volltextsuche über app.html, case-insensitiv „AOFAS": kein Treffer mehr. SB: Wert 82 ins FAOS-Feld eintragen → Brief-Zeile „- Scores: FAOS 82/100"; alle vier Felder leer → keine Scores-Zeile (Bestandsverhalten).

## Deploy

Nur `app.html` ändern, committen, pushen. Kein Bucket-Upload.
