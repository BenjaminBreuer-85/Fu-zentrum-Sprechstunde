# Folgeauftrag an die Code-Sitzung: Beidseits und Calcaneoplastie, drei Nachbesserungen (app.html)

Stand 14.09.2026, Cowork-Sitzung, nach Gegenprobe des Commits 81f6f95 (Prüfstand-Bericht Abschnitt 11), der Vollzugsmeldung zu Commit 7ddd117 (Kodierhinweise-Block) und den Entscheidungen des Autors („UC-Sperre behalten"; Bursa 5-859.19). Punkt 2 beantwortet die Rückfrage der Code-Sitzung aus 7ddd117 (Bedingung „bei beidseits gesperrt entfällt der ambulante Teil": ja, so bauen), Punkt 3 die Rückfrage zur Lokalisation.

## 1. UC-Modul: Quelle der Beidseits-Sperre

Entscheidung des Autors 14.09.2026: Die pauschale Sperre im UC-Modul bleibt. Nur die Begründung ändert sich, weil I20-V67 ausschließlich für I20M/N/O gilt. Befund Band 2 (aG-DRG 2024/2026): Jede Hybrid-DRG trägt eine eigene Bedingung „Nicht [beids. Pr Hybrid MDC 08 – n (…)]" mit eigener Tabelle, für die UC-Familien I13M/I13N (PDF S. 927–930), I21M (S. 1095), I29M (S. 1214), I31M/I31N (S. 1224–1226). Die Tabellennummern sind noch nicht abgenommen extrahiert; das wird Datenschritt 3j (`HDRG_FALLREGELN.beidseitsUC` je Familie). Bis dahin gilt im UC-Modul die pauschale Sperre.

Änderung: In `ucHdrgAusgeschlossen` den Grund „Beidseitiger Eingriff (I20-V67)" ersetzen durch „Beidseitiger Eingriff (Definitionshandbuch, Beidseits-Bedingung der jeweiligen Hybrid-DRG)"; gleicher Text im UC-Sperrblock und im Prüfkasten „H-DRG-Fähigkeit". Keine Logikänderung. Sobald 3j in den Daten liegt, liest das UC-Modul die Liste je Familie analog zu `beidseitsSperre` im Fuß; das ist dann ein eigener Auftrag.

## 2. OP-Bericht: alter Kodierhinweise-Block bei beidseits gesperrtem Fall

Befund (Prüfstand, Chevron, Seite „Bds."): Über dem Block steht der Sperrblock „⛔ KEIN H-DRG MÖGLICH – beidseitiger Eingriff", die Erlösspalten zeigen „—", das Codierziel sagt „nur EBM". Der wieder sichtbare Block „Erlösrelevante Kodierhinweise" (seit `auftrag-kodierhinweise-op-bericht.md`) beginnt darunter aber weiter mit „Ambulante Führung (Hybrid-DRG I20O 1.007 €): Codes: …" und der Zeile „❌ 5-854.2c NICHT kodieren".

Änderung: Ist der Fall beidseits gesperrt (derselbe Zustand, der den Sperrblock auslöst), den Abschnitt „Ambulante Führung" des Blocks durch eine Zeile ersetzen: „Ambulante Führung: nur EBM (beidseitiger Eingriff, keine Hybrid-DRG)"; der Abschnitt „Stationäre Führung" bleibt unverändert. Bei der Prüfzeile „Hybrid bleibt nach Definitionshandbuch möglich" (Calcaneoplastie) bleibt der Block wie er ist. Endgültig ersetzt Schritt 6 den Block durch die Auswertung.

## 3. OP-Bericht: Calcaneoplastie an die Daten angleichen (Entscheidung des Autors 14.09.2026: Bursa = 5-859.19 Unterschenkel)

Die Lokalisation ist entschieden: 5-859.19 (Bursektomie Unterschenkel), nicht 5-859.1a. In `opsteuerung.json` steht seit 3i für `haglund_mini`: `hebel` 5-859.19 „Bursektomie Unterschenkel", `drg` I27E (stationär mit Bursektomie), `hdrg` I20O (ambulant nur 5-782.at). Der OP-Bericht rechnet die Calcaneoplastie noch fest im Code: Kodier-String mit „5-859.1a", stationär „I20F", und in der ambulanten Kodezeile des Kodierhinweise-Blocks steht 5-859.19 ohne Warnung, obwohl 5-859.19 wie 5-855.39 in I27-V4 steht und den Fall aus I20O nach I27E führt (Webgrouper des Autors 14.09.2026: 5-782.at + 5-859.19 → I27E).

Änderung im Zweig Calcaneoplastie des OP-Berichts: Kodier-String „5-859.1a" → „5-859.19"; stationäres Ziel I27E (Betrag aus `erloes2026.json`, wie im Brief); in der ambulanten Kodezeile 5-859.19 wie 5-855.39 als „NICHT kodieren" markieren (ambulant nur 5-782.at → I20O); in der stationären Kodezeile 5-859.19 als Hebel kennzeichnen („IMMER kodieren → I27E"). Kein weiterer Zweig wird angefasst; die Umstellung aller Zweige auf `OP_STEUERUNG` bleibt Schritt 6b.

## Abnahme (Cowork-Prüfstand)

Seite „Links": alle Referenzläufe zeichengleich mit `baseline_*_code.json` (Stand 81f6f95) bis auf den Zweig Calcaneoplastie im OP-Bericht (Sollwert: stationär I27E, Kodier-String 5-859.19, Kodezeilen wie in Punkt 3). Seite „Bds.": Chevron im OP-Bericht ohne „Ambulante Führung (Hybrid-DRG …)" im Kodierhinweise-Block; UC Radius distal „Bds." mit dem neuen Grundtext; Calcaneoplastie unverändert.
