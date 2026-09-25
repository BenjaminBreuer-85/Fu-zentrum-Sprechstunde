# Auftrag Clinic (Schritt 6c): Nachbesserung zu 6b

Stand 25.09.2026, Cowork-Sitzung. Gegenprobe zu f0d2e3b bestanden bis auf vier Punkte (Prüfstand-Bericht Abschnitt 38). Datei `app.html`, Ausgangsstand Commit f0d2e3b (792.649 Byte, 54073d20…, Zeilenangaben darauf). Daten Stand 3ad (lokal; `optexte.json` noch nicht im Bucket). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung durch die Code-Sitzung; Punkt 4 hat einen Datenteil, den die Cowork-Sitzung liefert (3ae), siehe dort.

## 1. Chip-Standard (Abweichung von Nachtrag 2 des 6b-Auftrags)

`vfSehnentransfer` und `vfSpongiosa` (Z. 4900 f.) starten mit `false` und werden bei jeder Wahl des Haupteingriffs auf `false` gesetzt (Z. 6113). Entscheidung des Autors 24.09.2026: beide Chips sind **standardmäßig gesetzt**, weil der Abduktor-Transfer und die Spongiosa aus der Exostose zur Standardtechnik gehören; der Chip dient dem Abwählen. Änderung: bei Wahl von chevron, scarf oder lapidus `setVfSehnentransfer(true)`, bei lapidus zusätzlich `setVfSpongiosa(true)`; bei anderen Haupteingriffen beide `false`. Chip-Beschriftung „AHL-Transfer" (Chevron, Scarf, Lapidus) statt „+ Sehnentransfer", „Spongiosaplastik" beim Lapidus; gesetzter Zustand wie bei `mitAkin` dargestellt. Folge in der Fallsteuerung: Standard-Chevron stationär I20E (I20O erst nach Abwahl), Standard-Lapidus I20D über AKF08 (I20M erst nach Abwahl der Spongiosa, mit Akin). Das ist gewollt.

## 2. Partnerbedingung im Sprechstundenbrief über alle gewählten Eingriffe (Regression)

`partnerErfuellt(fallCodes, bestKey)` (Z. 1416; Aufruf im Brief Z. 3756) prüft nur den Haupteingriff. Bei Chevron + Kleinzehen-PIP ist der Haupteingriff im Brief `kleinzehen_pip` (Auswahl nach CM, Z. 3393 f.), `fallCodes` enthält keinen Chevron-Kode; Ergebnis I20O statt I20N (Abschnitt 30 und Sollwerte 5 und 14: I20N). Mein Fehler in Abschnitt 1 des 6b-Auftrags. Änderung: `partnerErfuellt(codes, keys, ohne)` nimmt eine Liste von Schlüsseln; der Brief übergibt alle gewählten `opMethode`-Schlüssel, der OP-Bericht die Schlüssel aller beteiligten Einträge (`obListe`, Z. 5428 ff.) zusätzlich zu den Kodes. Erfüllt, wenn ein Kode in `HDRG_KOMBI.partner` (nicht der geprüfte Kode selbst) oder ein Schlüssel in `HDRG_KOMBI.partnerEintraege` vorkommt.

## 3. Positivliste und Rang über Hebel-Kodes (Sollwerte 12, 18, 28)

a) **Positivliste (H-04).** Neuer Eingang `opts.kodesVollstaendig` (true nur im OP-Bericht, Z. 5453; im Brief false, weil `fallCodes` die Hauptkodes nicht enthält). Ist er gesetzt und steht kein Kode des Falls in der Positivliste (Katalogflag 2 in `katalog2026.json`, Bitmaske `_AOP_IDX` wie in `imAopKatalog` Z. 1404–1410, Bit 2 statt Bit 1), dann `erg.hybrid = false; erg.hdrg = null; erg.sperre = "positivliste"`, `erg.drg = drgOp`, Satz: „Kein Kode des Falls steht in der Positivliste (I20-V68); der Fall gruppiert stationär nach <DRG>. Ambulant: …" (AOP-Baustein wie bei Kontext). Prüfreihenfolge: Alter, AKF08, Positivliste, Kontext, Aufwertung. Wirkung: Lapidus ohne Akin-Chip → I20D; mit Akin → I20M (5-788.56 in V68).

b) **Rang über Hebel-Kodes (a, zweiter Teil).** Nach der Kontextprüfung: steht `best.hebel` (alle Kodes des Strings) in `codes` und ist `best.hebel` nicht bereits als Kontext getroffen, dann gilt der Fall als „mit Hebel": `erg.drg = best.drg`; ist `DRG_RANG_LG[best.drg]` kleiner als `DRG_RANG_LG[Basis-DRG der Hybrid-Stufe]` (I20O → I20F 136, I20N → I20E 120, I20M → I20D 103), dann `erg.hybrid = false; erg.hdrg = null; erg.sperre = "rang"`, Satz: „<Hebelname> (<Kodes>) gruppiert den Fall nach <DRG> (Rang vor <Hybrid-Basis>); keine Hybrid-DRG." Beispiel Haglund + Bursektomie 5-859.19: I27E (129) vor I20F (136) → I27E ohne Hybrid (Sollwert 12); Haglund + Tendoskopie über die bestehende Rangwahl der Einträge (Sollwert 28); MTP-I + Tendoskopie: I27E 129 nach I20E 120 → Hybrid I20N bleibt (Sollwert 29). Im Brief gilt dasselbe, sobald der Hebel-Kode in `fallCodes` steht (heute nur über Modifikatoren; keine Änderung der Brief-Anzeige für Haglund erwartet, bitte bestätigen).

## 4. `T.rebalancing` an den AHL-Chip (Punkt 2 der Vollzugsmeldung)

Der Baustein enthält drei Aussagen: Kapselstreifen versetzt und fixiert, Abduktorsehne nach distal versetzt, Funktionsprüfung. Nur der zweite Satz gehört zum Transfer. Datenteil 3ae (Cowork, `optexte.json`): `T.rebalancing` wird zu „Der mediale Kapselstreifen wird nach proximal versetzt und fixiert. {ZUSATZ:ahl_transfer_ende}Danach Überprüfung der Beweglichkeit …", neuer Baustein `ahl_transfer_ende` = „Die Abduktorsehne wird nach distal versetzt. ". Codeteil: die Zuordnung Chip → Platzhalter (`zusaetze`, Z. 6001–6005) bindet `ahl_transfer_ende` an denselben Chip wie `ahl_transfer`. Kein zusätzlicher Text. Bis 3ae im Bucket ist, bleibt `rebalancing` unverändert und der zweite Satz steht auch ohne Chip im Bericht (wie heute); der Code darf deshalb nur bekannte Platzhalter binden und unbekannte ignorieren.

## Nichts anderes

Zuordnungstabelle, Rangwahl der Einträge, Darstellung `FallAuswertung`, Selbsttest 13/14 unverändert.

## Abnahme

Cowork-Prüfstand: (1) Brief: Chevron + PIP 2 → I20N, MTP-I + PIP 3 → I20N, PIP allein 2 → I20O, DMMO allein 1 → I20O, 3 → I20F; alle 89 Referenzfälle sonst zeichengleich. (2) OP-Bericht: Chevron ohne Änderung der Chips → Kodeliste mit 5-854.2c, Text mit Abduktor-Satz und (nach 3ae) mit „Die Abduktorsehne wird nach distal versetzt.", Fallsteuerung stationär I20E; AHL-Chip abgewählt → I20O, beide Sätze weg, Kode weg. Lapidus Standard → I20D (AKF08), Spongiosa abgewählt + Akin → I20M, Spongiosa abgewählt ohne Akin → I20D („Kein Kode des Falls steht in der Positivliste"). Haglund mini + Bursektomie → I27E ohne Hybrid; MTP-I + Tendoskopie → I20N. (3) Testfälle: 12, 18, 28 gleich; 15 bleibt offen (V6). (4) Selbsttest 0 Fehler, keine Konsolenfehler.

Abnahme des Autors am Handy: OP-Bericht → Chevron: Chip „AHL-Transfer" ist gesetzt, Text enthält den Abduktor-Satz, Fallsteuerung I20E; Chip abwählen → I20O.

Vollzugsmeldung mit Commit-Hash und Zeilennummern.
