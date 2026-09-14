# Nachtrag zum Auftrag Sprachregel Abrechnung: drei Sätze im festen Zweig (app.html)

Stand 15.09.2026, Cowork-Sitzung, nach Gegenprobe des Commits 6537db9 (Prüfstand-Bericht Abschnitt 15, bestanden) und Entscheidung des Autors („Ja"). Nur Text, keine Logik; die Umstellung der Zweige auf `OP_STEUERUNG` bleibt Schritt 6b.

## 1. Lapidus, Zieltext (`ziel`, Z. ~4949)

Alt: „Keine H-DRG (5-808.a4 nicht auf Positivliste) → stationär, mind. 2 Nächte → volle DRG I20D (CM 1,033 = 4.710 €)."

Neu: „Mit Spongiosaplastik oder mit DMMO an 3 bis 4 Mittelfußknochen (5-788.54/55) keine Hybrid-DRG: stationär, ab 2 Belegungstagen volle DRG I20D (CM 1,033 = 4.710 €). Ohne diese Zusatzeingriffe gruppiert der Fall mit Akin (5-788.56) in die Hybrid-DRG I20M."

Beleg: `HDRG_REGELN.I20M.kontext` (5-788.54, 5-788.55 → I20D; 5-784.0v → I20D), `katalog2026.json` (5-788.54/55 Flag 4, 5-788.52/53 Flag 2), Hybrid-Systematik H-04 (Lapidus mit Akin = I20M), MU S. 24 (1–2 Weil/DMMO bleiben I20M).

## 2. Lapidus, Zeile im Kodierblock (`kodier`, Z. 4950, aus Commit 6537db9)

Alt: „5-808.a4 selbst steht nicht in der Positivliste; der Fall gruppiert über den Akin (5-788.56) in I20M."

Neu: „5-808.a4 selbst steht nicht in der Positivliste; mit Akin (5-788.56) gruppiert der Fall in I20M, sofern keine Kontextprozedur (Spongiosaplastik am Metatarsale, DMMO an 3 bis 4 Mittelfußknochen 5-788.54/55) durchgeführt wird; dann I20D."

## 3. OSG-Arthrodese, Zieltext mit Spongiosa (Z. 5011)

Alt: „Mit Spongiosa → I13D (CM 1,552 = 7.079 €). Mit Spongiosaplastik I13D (7.080 €), ohne I13E (5.830 €)." (Aussage doppelt, zwei Beträge für I13D: CM × LBFW und Erlöstabelle.)

Neu: „Mit Spongiosaplastik an der distalen Tibia (Entnahme Beckenkamm 5-783.0d, Transplantation Tibia distal 5-784.0n) I13D (CM 1,552 = 7.079 €), ohne I13E (5.829 €)." (Beträge laufen wie bisher durch `_fx`.)

Ergänzung des Autors 15.09.2026: Die Lokalisation ist Teil der Aussage. 5-784.0n heißt im OPS „Transplantation von Spongiosa, autogen, offen chirurgisch: Tibia distal"; nur dieser Kode ist der belegte Weg nach I13D (`arthrodese_osg.hebel`, Hybrid-Systematik Anhang B). Eine Spongiosa an den Talus wäre 5-784.0s, ein anderer Kode ohne diesen Beleg. Deshalb in der Kodierblock-Zeile derselben Stelle (Z. 5012, beide Zweige des Ternärs) „5-784.0n Transplantation Tibia" → „5-784.0n Transplantation Tibia distal".

## Nicht Teil dieses Nachtrags, vorgemerkt für Schritt 6a

Die Kodeliste des Lapidus-Zweigs enthält keinen Akin-Kode 5-788.56 und führt Spongiosa an das Tarsale (5-784.0u) statt an das Metatarsale (5-784.0v, `lapidus.hebel`). Beides gehört in die Abweichungsliste 6a, nicht in diesen Textauftrag.

## Abnahme

Cowork-Prüfstand: OP-Bericht Lapidus und Kombinationen Lapidus/Lapidus + DMMO 3 gegen `baseline_*_3n.json` (Stand 6537db9): nur die Sätze 1 und 2; OSG-Arthrodese mit Spongiosa-Schalter: Satz 3 sichtbar, keine Doppelung, Kodierblock mit „Tibia distal"; sonst zeichengleich, keine Konsolenfehler. Deploy: nur `app.html`, Push durch den Autor.
