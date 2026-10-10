# Auftrag Clinic: Morton-Neurom im Sprechstundenbrief (Datenschritt) und im OP-Bericht (Code + Datenschritt)

Stand 10.10.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand daf581d (808.595 B, md5 89532ef2…; Zeilenangaben darauf). Daten: `diagnosen.json` 09.10. (f011a03c…), `opmethoden.json` 09.10. (ea117270…), `optexte.json` 02.10. (d80055d7…), `kurzlinks.json` 4a6550b (298f2aca…). Wunsch des Autors 10.10.2026 („ja, bauen“): Morton-Neurom-Exzision vollständig im Brief und im OP-Bericht. Ein Commit für den Code, Vollzugsmeldung mit Commit-Hash und Zeilennummern. Die Datenschritte (Abschnitt 1 und 3) macht die Cowork-Sitzung; die Code-Sitzung sieht den Bucket nicht, prüft gegen die lokale `data/`.

## Befund

Brief: Methode `morton_neurom` vorhanden (Fallsteuerung mit Zwischenraum II/III und III/IV, Z. 1770/1935, Hinweis „ambulant über den EBM“ aus `opsteuerung.json`), aber nur unter der Diagnose Metatarsalgie; keine eigene Diagnose, keine Morton-Befunde (Mulder-Klick, Intermetatarsalraum, Sensibilität), kein Kurzlink für den Krankheitsbild-Artikel (Artikel `morton_neurom_kb` existiert in der Patienten-App; der OP-Artikel `morton` ist verlinkt).

OP-Bericht: Chip „Morton-Neurom“ in der Großzehen-Einfachauswahl (Z. 6400, `gz==="morton"`), damit nicht mit Chevron/Lapidus kombinierbar und kein zweiter Zwischenraum. Text `T.morton_neurom` (Z. 5926) mit Platzhaltern „[3–4] cm“ und „[3.] Intermetatarsalraum“. ICD G57.6 (Z. 5414, korrekt). **OPS 5-846.7 (Z. 5495, Statuszeile Z. 6413) ist falsch:** laut `katalog2026.json` ist 5-846.7 „Arthrodese an Gelenken der Hand: Interphalangealgelenk, mehrere, mit Spongiosaplastik“. Richtig: **5-041.9 „Exzision von (erkranktem) Gewebe von Nerven: Nerven Fuß“** (AOP-Katalog). Fallsteuerung: `obEintraege` Z. 1817 leitet `morton` auf `morton_neurom` ohne Modifikator, obwohl `OB_MODIFIKATOREN.morton_neurom` (Z. 1770) den Zwischenraum kennt.

## 1. Datenschritt Brief (Cowork, nach Freigabe; wirkt ohne Code)

(a) `diagnosen.json`: neue Diagnose `morton_neurom` nach `metatarsalgie`, Gruppe Vorfuß zwischen Metatarsalgie und Zehenfehlstellung. Label „Morton-Neurom“, Diagnosetext „Morton-Neurom (Interdigitalneuralgie)“, Beschwerden „im Bereich des Vorfußes plantar zwischen den Metatarsalköpfchen mit elektrisierender Ausstrahlung in die angrenzenden Zehen, verstärkt in engem Schuhwerk“. Konservativ: Belassen des Befundes, Anpassung des Schuhwerks (weite Zehenbox, flacher Absatz), Einlagenversorgung mit retrocapitaler Abstützung (Pelotte), Schmerztherapie, Infiltrationstherapie, Physiotherapie, Zehengymnastik. Befunde: Haut; Auswahl „Betroffener Zwischenraum“ II/III, III/IV, beide (Brieftext „Druckschmerz im 3. Intermetatarsalraum (III/IV) mit Ausstrahlung in die angrenzenden Zehen“ usw.); Mulder-Klick positiv/negativ; Schmerzauslösung bei seitlicher Kompression des Vorfußes; Hypästhesie der angrenzenden Zehen; Druckschmerz unter den MT-Köpfchen und Kleinzehendeformitäten (gleiche IDs wie Metatarsalgie, bei Doppelauswahl ein Chip); Wadenmuskelkontraktur (gemeinsamer Befund). Methode `morton_neurom`; Sono `interdigital`; Bildbefund „Sonographisch/MR-tomographisch Nachweis eines Interdigitalneuroms im __. Intermetatarsalraum mit einem Durchmesser von __ mm“; Literatur nach PubMed: Bhatia M, Thomson L (2020) Morton's neuroma – Current concepts review. J Clin Orthop Trauma 11(3):406–409, [DOI 10.1016/j.jcot.2020.03.024](https://doi.org/10.1016/j.jcot.2020.03.024). Metatarsalgie behält `morton_neurom` als Methode (Doppelzuordnung wie Kleinzehen).

(b) `opmethoden.json`: `PATIENT_DIAGNOSE_MAP.morton_neurom = "morton_neurom_kb"` (Diagnose-Code im Brief).

(c) `kurzlinks.json`: neue ID `morton-neurom` → `fusstrack.html?op=morton_neurom_kb&modus=aufklaerung`, Titel „Morton-Neurom“, art diagnose; `_STAND` 2026-10-10. Nur Ergänzung, keine bestehende ID berührt.

Vorab auf dem Prüfstand geprüft (daf581d + diese Daten): Diagnose erscheint, Brief „Diagnosen: Morton-Neurom (Interdigitalneuralgie) links“, „Elektive operative Option: Morton-Neurom-Resektion links“, Befundsatz, konservative Liste, Risikosatz, Online-Satz auf `fuss-track.de/i/morton`; Selbsttest 6 = 0.

## 2. Code `app.html`: OP-Bericht

(a) **OPS-Korrektur zuerst:** Z. 5495 `o.push("5-846.7")` → `"5-041.9"`; Statuszeile Z. 6413 entsprechend („OPS: 5-041.9 · ICD: G57.6“, ohne „zu bestätigen“, ohne „Intermetatarsalraum im Text anpassen“).

(b) **Eigener Block statt Großzehen-Chip.** `morton` aus der `gz`-Liste (Z. 6400) entfernen; im Vorfuß-Abschnitt nach den Weil-Chips (Z. 6418) neue Kategorie „Morton-Neurom“ mit zwei Mehrfach-Chips „II/III“ und „III/IV“ (Zustand `morton`, Array aus "23"/"34", Reset in Z. 6299 und 6397 ergänzen, `hasVF` Z. 5247 und `anzahl` Z. 6397 um `morton.length` erweitern). Damit ist Morton mit Chevron, DMMO, Weil und Kleinzehen kombinierbar und zwei Zwischenräume sind möglich.

(c) **Text.** `optexte.json` liefert künftig `T.morton_neurom` mit dem Platzhalter `{IMR}` statt „[3.]“ und ohne „[3–4]“ (Datenschritt Abschnitt 3) sowie `T.morton_neurom_weiterer` (Kurzfassung für den zweiten Zwischenraum, beginnt „Nun Zuwendung zum {IMR} Intermetatarsalraum. …“). Code: `var IMR = {"23":"2.","34":"3."}`; erster gewählter Zwischenraum → `T.morton_neurom.replace(/\{IMR\}/g, IMR[x])`, jeder weitere → `T.morton_neurom_weiterer.replace(…)`; Reihenfolge 23 vor 34. Einbau an der Stelle von Z. 5926 (nach den Großzehentexten, vor DMMO/Weil/Kleinzehen; der Weichteilspreizer-Text passt vor die Osteotomien).

(d) **Kodes.** ICD Z. 5414: Bedingung `morton.length>0`, G57.6 + Seite, `hd: codes.length===0` wie bei den Kleinzehen (Z. 5418), damit bei Chevron M20.1 (Z. 5410) führend bleibt und G57.6 Nebendiagnose wird. OPS: `5-041.9` einmal je gewähltem Zwischenraum (zwei Nerven = zwei Kodes). Strahlzählung 5-86a.1x unverändert (keine Osteotomie).

(e) **Fallsteuerung.** `obEintraege` (Z. 1817): `morton` aus der `vf`-Zuordnung nehmen; stattdessen `if (z.morton && z.morton.length) add("morton_neurom", z.morton, ["5-041.9"])` mit den Zwischenraum-Schlüsseln als Modifikatoren (Z. 1770 kennt "23"/"34"); `obZustand` (Z. 5657 ff.) um `morton` ergänzen. `opsteuerung.json` bleibt (EBM-Hinweis, implantatfrei).

(f) Nachbehandlung: Morton allein löst keinen redressierenden Verband aus; der automatische Tape-Verband bei `hasVF` (Z. 7679 `buildVerband`) bleibt, weil der Watteverband im Text steht. Keine Änderung.

## 3. Datenschritt `optexte.json` (Cowork; Upload erst zusammen mit dem Push von `app.html`, weil der alte Code `{IMR}` nicht ersetzt)

`T.morton_neurom`: „… Hautinzision von ca. 3–4 cm im {IMR} Intermetatarsalraum, …“ (sonst wortgleich); neu `T.morton_neurom_weiterer`: „Nun Zuwendung zum {IMR} Intermetatarsalraum. Gesonderte dorsale Längsinzision, Präparation in gleicher Weise mit Durchtrennung des Lig. metatarsale transversum profundum, Darstellung des Interdigitalnerven mit spindelförmiger Auftreibung. Mobilisierung, Absetzen distal der Bifurkation und weit proximal, Resektion des Neuroms in toto. Auch dieses Resektat wird zur histopathologischen Untersuchung asserviert. Kontrolle auf Bluttrockenheit, Spülung, schichtweiser Wundverschluss.“ Selbsttest 4a listet den neuen Schlüssel bis zur Code-Umsetzung als unbenutzt (informativ).

## Nichts anderes

Großzehen-Chips, DMMO/Weil, Kleinzehen, Brieftexte der übrigen Diagnosen, Fuss-Track unverändert. `katalog2026.json` unverändert.

## Abnahme

Cowork-Prüfstand: (1) OP-Bericht Vorfuß: Chips II/III und III/IV; ein Zwischenraum → Volltext mit „3. Intermetatarsalraum“, Kodes 5-041.9 und G57.6L (HD); beide → Volltext + Kurztext, 5-041.9 zweimal; Chevron + Morton III/IV → Chevron-Text, dann Morton-Text, M20.1 HD, G57.6 ND, Kodes 5-788.5c … + 5-041.9; kein „[“ im Text; Fallsteuerung „Fallsteuerung – Morton-Neurom-Resektion Zwischenraum III/IV“ mit EBM-Hinweis; kein 5-846.7 mehr im Code. (2) Brief wie oben. (3) Selbsttest ohne neue Fehler (4a/7a informativ), keine Konsolenfehler, JSX transpiliert; 89 Brief-Referenzfälle zeichengleich.

Am Handy: OP-Bericht → Vorfuß → Morton III/IV → Text ohne eckige Klammern, Kode 5-041.9; Sprechstundenbrief → Vorfuß → Morton-Neurom → Zwischenraum, Mulder-Klick → Brief.

Deploy: Bucket `diagnosen.json` + `opmethoden.json` und Push `kurzlinks.json` sofort nach Freigabe (Brief); Push `app.html` und danach Bucket `optexte.json` (OP-Bericht).
