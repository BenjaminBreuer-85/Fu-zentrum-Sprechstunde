# Auftrag Clinic: Chip „+ Stabilisierung (Broström)“ bei der OSG-Endoprothese

Stand 29.09.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand Commit 9e55c0e (802.149 Byte, md5 812aa066…; Zeilenangaben darauf). Daten: Datenschritt 3ai der Cowork-Sitzung (`data/opsteuerung.json` Modifikator `stabilisierung` an `tep_infinity`, `tep_vantage`, `tep_inbone`; `data/optexte.json` Baustein `tep_brostrom` und Platzhalter `{ZUSATZ:tep_brostrom}` in den sechs TEP-Texten), liegt lokal auf dem Mac; `optexte.json` und `opsteuerung.json` 3ai kommen erst mit dem Push dieses Auftrags in den Bucket. Konzept: `konzept-tep-stabilisierung.md`. Entscheidungen des Autors 29.09.2026: Chip standardmäßig aus; DRG ändert sich nie; zwei Fadenanker kommen zum Materialsatz; immer separater lateraler Zugang wie im Broström-Text, mit Abtragung der lateralen Osteophyten gegen Impingement. Ein Commit, eine Vollzugsmeldung mit Zeilennummern.

## 1. Zustand und Chip

Neuer Zustand `tepStabi` (`useState(false)`), Standard aus. Er bleibt beim Wechsel zwischen den sechs `tepType`-Werten erhalten und wird auf `false` gesetzt, wenn die TEP abgewählt wird (Sektions-Reset Z. 6324, `setTepType("")`-Stellen) sowie in `resetAll()` (Z. 6138 ff., Selbsttest 15). Chip „+ Stabilisierung (Broström)“ (`tog(tepStabi)`) in der TEP-Unterzeile Z. 6341 f. neben „+ Prophecy“, für alle sechs Werte (primär und Wechsel, alle drei Modelle). OPS-Zeile Z. 6408: bei gesetztem Chip „, 5-806.5, 5-869.2, 5-782.1r“ und „ · mit Bandstabilisierung“ anhängen.

## 2. Kodes und Diagnose

Kodeblock Z. 5390 f.: bei `tepStabi` zusätzlich `5-806.5`, `5-869.2`, `5-782.1r` (Bandrekonstruktion OSG, Sehnenanker, Osteophytenabtragung Fibula; wie beim isolierten Broström Z. 5381, ohne Internal Brace). ICD Z. 5282-Muster: bei `tepStabi` Nebendiagnose `M24.27` + Seite „Chronische Bandinstabilität OSG“ (`hd:false`).

## 3. Zuordnung, Materialsatz, Fallsteuerung

`OB_SCHLUESSEL` Z. 1781: `tep_infinity`, `tep_vantage`, `tep_inbone` je `["wechsel", "stabilisierung"]`. `obEintraege` Z. 1809–1812: Modifikatorliste der TEP um `"stabilisierung"` ergänzen, wenn `z.tepStabi` gesetzt ist (neben `wechsel`). Damit übernimmt die vorhandene Mechanik Materialsatz (Modifikator `material: ["brostrom_gould","Standard"]` = 2 Fadenanker, zusätzlich zum Prothesensatz), Hinweistext und Kodes in der Fallsteuerung. Keine Änderung an `hdrgAuswertung`; die DRG bleibt I05B bzw. I43B (Entscheidung des Autors).

## 4. Text

Textkopplung Z. 6071 (`zusaetze`): `if(tepStabi) zusaetze.push("tep_brostrom");`. Der Platzhalter steht nach 3ai in allen sechs TEP-Texten vor der abschließenden Stabilitätsaussage; ohne Chip sind die Texte zeichengleich zu heute. Abhängigkeitslisten Z. 5560 und 6096 um `tepStabi` ergänzen. Unbekannte Platzhalter weiter ignorieren.

## Nichts anderes

Sprechstundenbrief: keine Codeänderung nötig, der Modifikator erscheint über die vorhandene Mechanik als Chip unter jeder TEP-Auswahl (bitte in der Vollzugsmeldung bestätigen, dass Textzusatz, Kodes und Materialliste dort erscheinen). Fuss-Track unverändert.

## Abnahme

Cowork-Prüfstand (Daten 3ai): (1) OP-Bericht → OSG-TEP → Infinity: Chip „+ Stabilisierung (Broström)“ vorhanden und aus; Bericht und Kodeliste zeichengleich zu 9e55c0e; ebenso alle 17 Referenz-Kombinationen. (2) Chip gesetzt: Kodeliste 5-826.00, 5-806.5, 5-869.2, 5-782.1r; ICD M24.27 als Nebendiagnose; Text nach „… Rückfußachse.“ mit „Bei der Stabilitätsprüfung nach Einsetzen des Inlays …“ bis „Das Gelenk ist lateral nun eindeutig stabil.“, danach der bisherige Schlusssatz; Anker als „Fadenanker mit geflochtenem Faden“ aufgelöst; Materialliste mit 2× Fadenanker zusätzlich zum Prothesensatz; Fallsteuerung I05B unverändert, Hinweis „Laterale Bandstabilisierung … DRG unverändert; zwei Fadenanker kommen zum Materialsatz.“ (3) Vantage, Inbone und die drei Wechsel-Werte: derselbe Zusatz an der jeweiligen Stelle (Inbone vor „Die Bandspannung ist gut balanciert“), beim Wechsel zusätzlich 5-827.10 und I43B. (4) Chip gesetzt, dann Modell gewechselt: Chip bleibt; TEP abgewählt und neu gewählt: Chip aus; „↺ Neu“: aus. (5) Brief → OSG-Arthrose → OSG-TEP: Chip „+ Stabilisierung (Broström)“, Eingriff „… mit lateraler Bandstabilisierung nach Broström-Gould“, Kodeliste und Materialliste mit Ankern. (6) Selbsttest 0 Fehler, Prüfung 15 leer, keine Konsolenfehler; Faktencheck ohne Befund.

Abnahme des Autors am Handy: OP-Bericht → Infinity → Chip setzen: Broström-Absatz mit Osteophytenabtragung vor dem Schlusssatz, Kodes und Anker in der Liste.

Deploy-Reihenfolge: erst `optexte.json` und `opsteuerung.json` 3ai in den Bucket, dann Push.

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
