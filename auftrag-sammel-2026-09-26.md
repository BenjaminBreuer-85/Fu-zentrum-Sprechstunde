# Auftrag Clinic (Sammelauftrag 26.09.2026): Bursektomie-Chip, AOP-Satz ohne Hybrid, Aufwertungssatz, Kacheltext OP-Manuale, Testfall 15

Stand 26.09.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand Commit 642c7cc (799.417 Byte, md5 dc0a69e0…, gepusht; Zeilenangaben darauf). Daten: Datenschritt 3ag der Cowork-Sitzung (siehe Abschnitt 5), liegt lokal auf dem Mac; `optexte.json` 3ag kommt erst mit dem Push dieses Auftrags in den Bucket. Ein Commit, eine Vollzugsmeldung mit Zeilennummern. Entscheidungen des Autors 26.09.2026: G11 Bursektomie als Chip, standardmäßig gesetzt, darunter Hinweis zur Führung; G13 Wortlaut „für Kliniken nur stationär führbar, wenn nicht Hybrid und nicht AOP“; Sollwert 15 bewusst nicht abgebildet.

## 1. G11: Bursektomie als Chip an der Calcaneoplastie (OP-Bericht)

Befund: Der Kodeblock schiebt bei `haglund_mini` immer 5-859.19 (Z. 5365); der Berichtstext `T.haglund_mini` enthält den Satzteil „Entfernung einer Bursitis subachillea, “ fest. Mit der Rangregel aus 6c ist die Calcaneoplastie im OP-Bericht damit nie Hybrid I20O, sondern immer I27E; der Sprechstundenbrief führt die Bursektomie als optionalen Hebel (`haglund_mini.hebel`).

Änderung, nach dem Muster der Chips `vfSehnentransfer`/`vfSpongiosa` (Z. 4952 f., 5310 f., 6058 f., 6222 f.):

1. Neuer Zustand `rfBursektomie` (`useState(false)`). Beim Hinzufügen von `haglund_mini` zu `rfOp` (Umschalter Z. 6383, `togArr`) wird er auf `true` gesetzt, beim Entfernen auf `false`. Standard also gesetzt, der Chip dient dem Abwählen.
2. Chip-Zeile unter den Rückfuß-Chips, nur bei `rfOp.includes("haglund_mini")`, nach dem Muster der Dwyer-Zeile (Z. 6386 ff.): ein Chip „Bursektomie“ (`tog(rfBursektomie)`), darunter in der kleinen grauen Schrift (wie „Rebalancing auto · OPS: …“ Z. 6222) der Hinweis zur Führung: „Mit Bursektomie (5-859.19) gruppiert der Fall nach I27E, keine Hybrid-DRG · ohne Bursektomie Hybrid I20O möglich“.
3. Kodeblock Z. 5365: `o.push("5-782.at","5-855.39"); if(rfBursektomie) o.push("5-859.19");`. Z. 5366 (`haglund`, AS-Split) unverändert.
4. Textkopplung Z. 6058 f.: `if(rfBursektomie) zusaetze.push("haglund_bursektomie");`. Der Platzhalter `{ZUSATZ:haglund_bursektomie}` steht nach 3ag in `T.haglund_mini` an der Stelle des Satzteils, Baustein `T.haglund_bursektomie` = „Entfernung einer Bursitis subachillea, “. Unbekannte Platzhalter weiter ignorieren (wie seit 6c).
5. Abhängigkeitslisten Z. 5529 und 6064 um `rfBursektomie` ergänzen; `resetAll()` (Z. 6106 ff.) um `setRfBursektomie(false)`, sonst meldet Selbsttest 15.

Wirkung in der Fallsteuerung (keine Änderung an `hdrgAuswertung` nötig): Standard I27E ohne Hybrid über die Rangregel (Sperre `rang`), Chip abgewählt I20O ambulant, stationär I20F. Gewollter Unterschied zum Brief (I20O mit optionalem Hebel), wie beim Chevron.

## 2. G13: AOP-Satz, wenn keine Hybrid-DRG mehr besteht

Befund: `ambSatzBau()` (Z. 1550–1555) hängt „… nicht im AOP-Katalog, für Kliniken daher Hybrid empfohlen.“ an jeden Satz, auch an die Sperr-Sätze `alter` (Z. 1577), `akf08` (Z. 1588), `positivliste` (Z. 1590 f.), `kontext` (Z. 1620–1622) und `rang` (Z. 1646), in denen es keine Hybrid mehr gibt; der Nachsatz widerspricht dann dem Satz davor.

Änderung: `ambSatzBau(ohneHybrid)` bekommt einen Parameter. Mit `ohneHybrid === true` lautet der Satz „Ambulant: <Kodes> steht/stehen nicht im AOP-Katalog; ohne Hybrid-DRG für Kliniken nur stationär führbar.“ Ohne den Parameter (heute kein weiterer Aufrufer, aber für künftige Aufwertungs-/Neutralfälle) bleibt der bisherige Wortlaut. Die fünf Sperr-Aufrufe übergeben `true`. „Ambulant EBM.“ (alle Kodes im AOP-Katalog) unverändert. Sprachregel Abrechnung (14.09.2026) beachten: keine Anweisung zum Kodieren oder zur Verweildauer, keine gesperrten Wörter.

## 3. Aufwertungssatz, wenn die Stufe schon erreicht ist

Befund (Prüfstand-Bericht Abschnitt 30): MTP-I-Arthrodese + Kleinzehen-PIP 3 Zehen zeigt „3× Arthrodese IP Dig II–V (5-808.bf) wertet auf I20N auf.“, obwohl der Fall mit MTP-I schon in I20N startet (Z. 1623–1626: `erg.hdrg` aus `hoechste(aTreffer)` ist gleich `hdrgStart`).

Änderung: Ist `erg.hdrg === hdrgStart`, lautet der Satz „Ambulant gruppiert der Fall nach <hdrgStart>; <Name> (<Kode>) liegt in derselben Stufe.“ Ist die Stufe höher, bleibt „… wertet auf <hdrg> auf.“

## 4. G5-Rest: Kacheltext OP-Manuale

Z. 7620: „Klick öffnet in neuem Tab“ → „Klick öffnet in eigenem Fenster“ (wie Z. 10103 seit 70d85e7).

## 5. Datenteil 3ag (Cowork, nicht Teil der Code-Änderung; zur Kenntnis)

`data/optexte.json`: `T.haglund_mini` mit `{ZUSATZ:haglund_bursektomie}`, neuer Baustein `T.haglund_bursektomie`. `data/opsteuerung.json`: `lapidus.hinweise[0]` nennt „Spongiosatransplantation an das Tarsale (5-783.0v + 5-784.0u, Fallsperre AKF08)“ statt 5-784.0v (G12). `hybrid_testfaelle.json` (Repo): Fall 15 `status: "bewusst nicht abgebildet"` mit Begründung im Feld `hinweis`. Bitte `scripts/verify_zweige_6a.py` so ergänzen, dass dieser Status in der Zusammenfassung als eigene Kategorie gezählt wird (weder gleich noch abweichend) und der Lauf ihn nicht als Abweichung meldet; Sollwert im Fall bleibt I20M.

Deploy-Reihenfolge: erst `optexte.json` 3ag und `opsteuerung.json` 3ag in den Bucket, dann Push. Vorher stünde ohne den Code der Bursektomie-Satz im Bericht nicht (Platzhalter ohne Chip wird leer).

## Nichts anderes

Zuordnungstabelle, `hdrgAuswertung` außer Punkt 2 und 3, Brieftexte, Sprechstundenbrief-Darstellung unverändert.

## Abnahme

Cowork-Prüfstand (Daten 3ag): (1) OP-Bericht → Rückfuß → Calcaneoplastie: Chip „Bursektomie“ gesetzt, Hinweiszeile darunter, Kodeliste 5-782.at, 5-855.39, 5-859.19, Text mit „Entfernung einer Bursitis subachillea“, Fallsteuerung I27E ohne Hybrid; Chip abgewählt: Kodeliste ohne 5-859.19, Satzteil weg, Fallsteuerung ambulant I20O, stationär I20F; Calcaneoplastie abgewählt und neu gewählt: Chip wieder gesetzt; „↺ Neu“ setzt den Chip zurück. (2) Chevron Standard (Kontext 5-854.2c): Satz endet mit „… steht nicht im AOP-Katalog; ohne Hybrid-DRG für Kliniken nur stationär führbar.“; Lapidus Standard (AKF08) ebenso; MTP-I mit „<18 J.“ ebenso; Haglund mit Bursektomie „Ambulant EBM.“ (5-859.19 ist AOP-Kode). (3) Brief: Hallux rigidus → MTP-I-Arthrodese + Kleinzehen/PIP 3 Zehen: „Ambulant gruppiert der Fall nach I20N; 3× Arthrodese IP Dig II–V (5-808.bf) liegt in derselben Stufe.“; Hallux valgus → Chevron + PIP 2: weiter „… wertet auf I20N auf.“ (4) 89 Brief-Referenzfälle `out/6c/res.json`: Briefe zeichengleich, Fallsteuerung nur in den Kontext-/Sperrsätzen (neuer Nachsatz) verändert; 17 OP-Bericht-Kombinationen: nur Haglund + AS-Split unverändert, Calcaneoplastie wie (1). (5) OP-Manuale: Fußzeile „in eigenem Fenster“. (6) Selbsttest 0 Fehler, Prüfung 15 ohne Treffer, keine Konsolenfehler; `verify_zweige_6a.py` zählt Fall 15 als „bewusst nicht abgebildet“.

Abnahme des Autors am Handy: OP-Bericht → Calcaneoplastie: Chip „Bursektomie“ gesetzt, Fallsteuerung I27E; Chip abwählen → I20O.

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
