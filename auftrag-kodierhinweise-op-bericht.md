# Auftrag an die Code-Sitzung: OPS-Kodes im OP-Bericht wieder anzeigen

Stand 14.09.2026, Cowork-Sitzung. Meldung des Autors (14.09.2026, Screenshot Fallsteuerung „Haglund + AS-Split/Refix" am Handy): „Im OP-Bericht-Generator müssen die OPS-Codes angezeigt werden, die zu dem jeweiligen Erlös führen, den wir empfehlen. Dies hatten wir auch schon implementiert."

## Befund

Der Block „Erlösrelevante Kodierhinweise" im OP-Bericht (`app.html` Stand 12.09.2026, Z. 6364–6395) ist der einzige Ort, an dem der OP-Bericht die OPS-Kodes zeigt (Kommentar Z. 6230: „OPS CODES → nur in Kodierhinweise-Box"). Er steht unter der Bedingung `!HDRG_REGELN&&erloesData.kodier` (Z. 6368). Seit `data/opsteuerung.json` den Block `HDRG_REGELN` trägt (Deploy 13.09.2026, Daten vom 07./09.09.), ist die Bedingung immer falsch; der Block erscheint bei keinem der 68 OP-Bericht-Fälle des Prüfstands (Referenzläufe `ref_alt/baseline_ob.json` und `baseline_ob_neu.json`: 0 von 68 mit „Kodierhinweise", 0 von 68 mit „Codes:"). Der Kommentar Z. 6365 („Mit Regelsatz erzeugt die Auswertung die Kodierhinweise") beschreibt einen Zustand, der noch nicht gebaut ist: `hdrgAuswertung` wird nur im Sprechstundenbrief aufgerufen (Z. 3354), im OP-Bericht nirgends. Der Ersatz war laut `auftrag-hybrid-regeln.md` Abschnitt 4 und Punkt 4 der Nachträge ausdrücklich ein eigener dritter Durchgang; der Wegfall des alten Blocks kam aber schon mit dem ersten.

## Auftrag

Sofort (kleiner Eingriff): die Bedingung in Z. 6368 auf `erloesData.kodier` zurücksetzen, damit der bisherige Block wieder erscheint, bis der Ersatz aus der Auswertung gebaut ist. Keine weiteren Änderungen an dem Block. Gegenprobe der Cowork-Sitzung: OP-Bericht 68 Fälle gegen `baseline_ob_neu.json`; erwartete Abweichung nur das Wiedererscheinen des Blocks (Zeilen „Erlösrelevante Kodierhinweise", „Ambulante Führung (Hybrid-DRG …): Codes: …", „Stationäre Führung (volle DRG …): Codes: …"), sonst zeichengleich.

Danach (Schritt 6, wie geplant): Block aus der Auswertung erzeugen, Reihenfolge wie in `auftrag-hybrid-regeln.md` Abschnitt 4: Haupt-OPS, gesetzte Kontext-/Aufwertungskodes mit Namen, `satz`, Belegungssatz. Dabei die Kodes je Zweig aus `OP_STEUERUNG` lesen (Schritt 6b), nicht mehr aus den `kodier`-Strings.

## Beobachtung aus demselben Screenshot (Daten, nicht Code)

Bei „Haglund + AS-Split/Refix" fehlt keine Kodezeile durch Datenfehler; der Kodier-String (Z. 5052: „5-782.at + 5-855.39 + 5-855.19 + 5-854.29 + 5-859.19") ist vorhanden und wird nur nicht angezeigt. Bei „Calcaneoplastie" (Z. 5043–5046) steht im Kodier-String „5-859.1a" (Bursektomie Fuß, Positivkode, Hybrid bleibt), in der Kodeliste `o` derselben OP (Z. 4832) aber „5-859.19" (Bursektomie Unterschenkel, I27-Kode, führt aus I20O heraus). Das ist ein Widerspruch innerhalb von `app.html`; welche Lokalisation gilt, entscheidet der Autor (siehe Datenschritt 3i im Umsetzungsplan). Bitte in Schritt 6 nur nach dieser Entscheidung anfassen.
