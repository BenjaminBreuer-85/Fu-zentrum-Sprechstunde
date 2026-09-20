# Auftrag Clinic: Anzahl bei Kleinzehen/PIP und DMMO aus der Zehen-/Strahlwahl ableiten

Stand 20.09.2026, Cowork-Sitzung. Handy-Abnahme des Autors 20.09.2026: Unter dem Chip „Kleinzehen/PIP" stehen zwei Blöcke, „Zehe" (D2–D5) und „Anzahl" (1–2 Zehen / ≥3 Zehen). Das wirkt doppelt, und man weiß nicht, ob beides zu klicken ist. Entscheidung des Autors („B"): Die Anzahl wird aus der Zehenwahl berechnet, der Anzahl-Block entfällt; dasselbe für DMMO (Strahl statt Anzahl-Block). Datei `app.html`, Ausgangsstand Commit c6f3732 (802.645 Byte, Zeilenangaben darauf; liegen die Aufträge `auftrag-implantatfrei.md` oder `auftrag-brief-gruss-schrift.md` schon davor, verschieben sich die Stellen um wenige Zeilen). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

Zwei getrennte Eingaben, die nichts voneinander wissen:

- „Zehe" bzw. „Strahl" kommt aus `OP_ZUSATZWAHL` (Z. 1620–1629, `kleinzehen_pip` und `kleinzehen_weichteil` D2–D5, `dmmo` und `weil` MT II–IV), Zustand `opZusatz` (Z. 1811), `togZusatz` (Z. 1812). Wirkung: nur der Brieftext über `opZusatzText` (Z. 1631) und `opTextMitMods` (Z. 1652).
- „Anzahl" sind eigene Zustände: `dmmoCount` (Z. 1807, Chips Z. 2173–2177: „1 MT", „MT II–III (2×)", „MT II–IV (3×)", „MT II–V (4×)"), `pipCount` (Z. 1808, Chips Z. 2183–2184: „1–2 Zehen", „≥3 Zehen"). Wirkung: nur die Fallsteuerung, Z. 3410–3412 (`dmmoSmall`, `dmmo3`, `dmmo4`), Z. 3415 (DMMO ≥3 → keine H-DRG), Z. 3416 (PIP ≥3 → keine H-DRG), Z. 3417 (Chevron + DMMO ≥3), Z. 3445 (Chevron/Scarf + DMMO klein oder PIP ≥3 → I20N), Z. 3476 f. (`DMMO_CODE` nach `dmmoCount` → 5-788.52 bis .55 in `fallCodes`).

Folge heute: Wer D2, D3 und D4 wählt und den Anzahl-Block vergisst, bekommt eine Erlössimulation mit Hybrid-DRG, obwohl bei drei Zehen keine möglich ist; bei DMMO fehlt zudem der OPS-Kode 5-788.5x.

## Änderung

1. `OP_ZUSATZWAHL.dmmo` (Z. 1627) um `["mt5","MT V"]` ergänzen, damit vier Strahlen wählbar sind (der bisherige Anzahl-Block reichte bis MT II–V). `weil` (Z. 1628) ebenfalls um `mt5` ergänzen, damit beide Osteotomien dieselben Strahlen anbieten; dort hängt keine Regel dran. Brieftext über `opZusatzText` ergibt dann z. B. „MT II, III und V", keine weitere Anpassung.

2. Die Zustände `dmmoCount`/`setDmmoCount` (Z. 1807) und `pipCount`/`setPipCount` (Z. 1808) durch abgeleitete Werte ersetzen, direkt hinter `opZusatz` (Z. 1811):

```
var pipZahl  = [].concat(opZusatz.kleinzehen_pip || []).length;
var dmmoZahl = [].concat(opZusatz.dmmo || []).length;
var pipCount  = pipZahl === 0 ? "" : (pipZahl <= 2 ? "1-2" : "3");
var dmmoCount = ({1:"1", 2:"2-3", 3:"2-4", 4:"2-5"})[dmmoZahl] || "";
```

Ohne gewählte Zehe/Strahl bleiben beide leer, also wie heute ohne Anzahl-Klick: keine Überschreibung, kein 5-788.5x. Die Fallsteuerungsstellen Z. 3410–3417, 3445, 3476 f. lesen weiter `dmmoCount`/`pipCount` und bleiben unverändert. (Die lokale Variable `pipCount` im OP-Bericht Z. 4827 ist ein anderer Geltungsbereich und bleibt.)

3. Die beiden Anzahl-Blöcke in `opUnterbloecke` entfernen: DMMO Z. 2171–2179 (`{opMethode.indexOf("dmmo") >= 0 && …}` mit Überschrift „DMMO Anzahl/Lokalisation MT"), Kleinzehen/PIP Z. 2180–2186 („Kleinzehen/PIP Anzahl"). Der Block `amic` (Z. 2168–2170) und die Modifikatoren-Blöcke danach bleiben.

4. Statuszeile unter den Zehen-/Strahl-Chips (im `OP_ZUSATZWAHL`-Block Z. 2158–2166, nach `<div style={row}>…</div>`), nur für `kleinzehen_pip` und `dmmo`, im Stil der Überschrift (fontSize 10, `#718096`):
   - `kleinzehen_pip`: `pipZahl === 0` → „Bitte Zehe(n) wählen; die Anzahl bestimmt die Fallpauschale."; 1–2 → „{n} Zehe(n) → Hybrid-DRG möglich"; ≥3 → „{n} Zehen → nur stationär".
   - `dmmo`: 0 → „Bitte Strahl(en) wählen; die Anzahl bestimmt OPS-Kode und Fallpauschale."; 1–2 → „{n} Strahl(en) → {Kode} → Hybrid-DRG möglich"; 3–4 → „{n} Strahlen → {Kode} → nur stationär" mit `Kode` aus derselben Tabelle wie Z. 3476 (`{"1":"5-788.52","2-3":"5-788.53","2-4":"5-788.54","2-5":"5-788.55"}`; die Tabelle einmal auf Modulebene als `DMMO_CODE` ziehen und in Z. 3476 wiederverwenden, statt sie zweimal zu schreiben).
   
   Sprachregel 14.09.: Die Zeile beschreibt nur die Regel, keine Anweisung; „Hybrid-DRG möglich" / „nur stationär" wie in den bestehenden `note`-Texten.

## Nichts anderes

`OP_ZUSATZWAHL` für Peronealsehnen, Morton, `kleinzehen_weichteil` unverändert; `opZusatzText`, `togZusatz`, Brieflogik, OP-Bericht, HDRG_REGELN unverändert.

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3w.json`, Stand c6f3732 mit 3w/3x/3y/3z-Daten): alle Briefe zeichengleich (die Referenz enthält keine gewählten Zehen/Strahlen). Fallsteuerung: Zehenfehlstellung → Kleinzehen/PIP ohne Zehe = wie heute ohne Anzahl; D2 + D3 = wie heute „1–2 Zehen" (I20O); D2 + D3 + D4 = wie heute „≥3 Zehen" (keine H-DRG, nur stationär); Hallux valgus → Chevron + Kleinzehen/PIP D2–D4 = I20N-Aufwertung wie heute. Metatarsalgie → DMMO MT II = 5-788.52 wie heute „1 MT"; MT II + III = 5-788.53; MT II–IV = 5-788.54 und nur stationär; MT II–V = 5-788.55. Brief bei DMMO MT II, III und V: „… MT II, III und V …". Keine Konsolenfehler, Selbsttest unverändert.

Abnahme des Autors am Handy: Zehenfehlstellung → Kleinzehen/PIP: nur noch ein Block „Zehe" mit Statuszeile darunter; drei Zehen anklicken → Zeile „3 Zehen → nur stationär", Erlössimulation zeigt keine Hybrid-DRG. Metatarsalgie → DMMO: Block „Strahl" MT II–V mit Statuszeile und Kode.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern.
