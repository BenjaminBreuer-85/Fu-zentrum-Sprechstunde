# Auftrag Clinic: Kleinzehen/PIP nach Regelsatz 2026 (Kode je Zehenzahl statt „≥3 → nur stationär")

Stand 20.09.2026, Cowork-Sitzung. Anlass: Gegenprobe zu Commit 664f9fd und die beiden Beobachtungen der Code-Sitzung (PIP ≥3 ohne Notiz, Chevron + PIP ≥3 ohne I20N). Datei `app.html`, Ausgangsstand Commit 664f9fd (803.569 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

Die Regel „≥3 Zehen → keine H-DRG möglich → nur stationär" (Override Z. 3420, PIP-Anteil in Z. 3449) stammt aus der Systematik 2024 und ist überholt. Nach den Regeln 2026 (`hybrid-systematik.md`: MU S. 22–23, I20O enthält 1–4× PIP-Arthrodese; Hallux valgus + 1× PIP → I20O, + 2–4× PIP → I20N, Webgrouper des Autors 13.09.2026, V4) gilt: 5-808.bd (1 Gelenk) neutral, 5-808.be/bf/bg (2–4 Gelenke) Aufwertung auf I20N, nur 5-808.bh (≥5 Gelenke) Kontextprozedur. Genau so steht es im Regelsatz `HDRG_REGELN.I20O_N` (`opsteuerung.json`: `aufwertung` be/bf/bg → I20N, `kontext` bh, `neutral` bd) und im Katalog (`katalog2026.json`: bd–bg Flag 2, bh Flag 4).

Warum die Anzeige heute so aussieht: Im Sprechstundenbrief trägt `kleinzehen_pip` keinen OPS-Kode in `fallCodes` (`OP_STEUERUNG.kleinzehen_pip` hat keine `opsCodes`; der OP-Bericht kodiert dagegen je Zehenzahl über `pipMap`, Z. 4989–4995). Der Regelsatz für I20O greift (`hdrgAuswertung`, Z. 3487 ff., `hAus.regel` wahr) und setzt die Werte des JS-Overrides zurück (Z. 3489–3499: `hdrg = hAus.hdrg`, `extraNote = ""`). Ohne Kode findet der Regelsatz nichts, also bleibt I20O ohne Notiz (Beobachtung 1) und ohne Aufwertung (Beobachtung 2). Der Auftrag `auftrag-anzahl-ableiten.md` hat die überholte Regel in die Statuszeile übernommen („3 Zehen → nur stationär"); das war ein Fehler der Cowork-Sitzung, nicht der Umsetzung.

## Änderung

1. Modulebene, neben `DMMO_CODE` (Z. 1638): `var PIP_CODE = {1:"5-808.bd", 2:"5-808.be", 3:"5-808.bf", 4:"5-808.bg"};`

2. Fallsteuerung, hinter der DMMO-Zeile (Z. 3480): `if(opMethode.indexOf("kleinzehen_pip")>=0&&PIP_CODE[pipZahl]) fallCodes.push(PIP_CODE[pipZahl]);` Damit bewertet der Regelsatz die Zehenzahl: 1 Zehe neutral, 2–4 Zehen Aufwertung auf I20N (Satz „… wertet auf I20N auf." wie bei DMMO 1–2×), im I20M-Umfeld (MTP-I-Arthrodese + PIP) neutral. Der Kode erscheint in der Kodeliste der Box.

3. Überholte Overrides entfernen: Z. 3420 (`else if(bestKey==="kleinzehen_pip"&&pipCount==="3") …`) ganz; in Z. 3449 den Teil `||(opMethode.indexOf("kleinzehen_pip")>=0&&pipCount==="3")` streichen, der DMMO-Teil bleibt. `pipCount` (Z. 1823) wird dann nirgends mehr gelesen und entfällt; `pipZahl` bleibt.

4. Statuszeile Kleinzehen/PIP (Z. 2181–2184) nur noch mit dem Kode, ohne DRG-Aussage (die Wirkung hängt von der Haupt-OP ab und steht in der Fallsteuerung): 0 → „Bitte Zehe(n) wählen; die Anzahl bestimmt OPS-Kode und Fallpauschale."; sonst `pipZahl + (pipZahl === 1 ? " Zehe → " : " Zehen → ") + PIP_CODE[pipZahl]`. DMMO-Zeile unverändert.

## Nichts anderes

OP-Bericht (`pipMap`, Z. 4989–4995), Brieftext, `OP_ZUSATZWAHL`, DMMO-Logik, HDRG_REGELN unverändert.

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3w.json`; Briefe ohne Grußformel, sonst zeichengleich; Fallsteuerung gleich, weil die Referenz keine Zehen wählt): Zehenfehlstellung → Kleinzehen/PIP: D2 → Kode 5-808.bd, I20O; D2+D3 → 5-808.be, I20N mit Satz „… wertet auf I20N auf."; D2–D4 → 5-808.bf, I20N; D2–D5 → 5-808.bg, I20N. Hallux valgus → Chevron + Kleinzehen/PIP D2 → I20O; + D2+D3 → I20N. Hallux rigidus → MTP-I-Arthrodese + Kleinzehen/PIP D2–D4 → I20M unverändert (neutral). Keine Notiz „≥3 Zehen" mehr. Keine Konsolenfehler, Selbsttest unverändert.

Abnahme des Autors am Handy: Zehenfehlstellung → Kleinzehen/PIP, D2 und D3 wählen: Statuszeile „2 Zehen → 5-808.be", Erlössimulation Ambulant I20N mit dem Aufwertungssatz. Falls der Autor die Aufwertung 2× PIP allein (ohne Hallux valgus) im Webgrouper gegenprüfen will: HD M20.4, 5-808.be.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern.
