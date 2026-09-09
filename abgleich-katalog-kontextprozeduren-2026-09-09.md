# Abgleich Kontextprozeduren: `katalog2026.json` (Modul OPS-Code-Suche) gegen `HDRG_REGELN`

Stand: 09.09.2026. Auftraggeber: B. Breuer („Gleiche die Liste, die dir vorliegt, mit der Liste im aktuellen Code ab, damit die Daten im Kapitel OPS Code Suche aktuell sind").

## Was verglichen wurde

Die OPS-Code-Suche in `app.html` liest `data/katalog2026.json`: 3.796 Kodes in `_HD` mit Bitmaske (1 = AOP, 2 = Hybrid-DRG, 4 = Kontextprozedur) und die Ausnahmen je Hybrid-DRG in `_KX`. Die Kontextliste darin trägt den Vermerk „Bestand 02.07.2026" und umfasst 70 Kodes. Verglichen wurde gegen den Regelblock `HDRG_REGELN` in `data/opsteuerung.json`, der aus den Prozedurentabellen I20-V69 (I20O/I20N) und I20-V61 (I20M) des Definitionshandbuchs Hybrid-DRG 2026 gebaut ist, wie auf den GFFC-Folien vom 04.03.2026 abgebildet: 95 Kontextkodes für I20O/I20N, 85 für I20M.

Ergebnis in einem Satz: 64 der 70 Katalogkodes stimmen, die Positivprozeduren, Aufwertungen und die drei bekannten I20M-Ausnahmen sind korrekt hinterlegt; 25 Kontextprozeduren fehlen im Katalog oder tragen kein Kontextflag, zwei tragen es zu Unrecht, vier sind unklar.

## Entscheidung des Autors (09.09.2026, Stück für Stück im Chat)

Stück 1, der Weg: Patch-Skript direkt. `katalog2026.json` wurde am 09.09.2026 mit `patch_katalog_kontext_20260909.py` geändert, jede Änderung steht im `_kommentar` der Datei; das Zeilenlayout (eine `_HD`-Zeile je Kode) ist unverändert, der Git-Diff zeigt genau die 45 betroffenen Zeilen. Die Master-Excel (`OPS_Katalogdaten_2026_MASTER.xlsx`, Blatt „Katalog") liegt damit vorübergehend hinter der JSON; die Abschnitte A, B, C und E sind die Zeilenliste zum Nachziehen, damit die 1:1-Regel aus `CLAUDE.md` beim nächsten Neuerzeugen wieder gilt.

Stück 2, die klaren Fälle: A, B, C und E vollständig übernommen.

Stück 3, die unklaren Fälle (D): Flags belassen, Prüfung gegen Tabelle I20-V69 später; 5-819.4 nicht aufgenommen.

## A. Neue Zeilen in der Master-Excel (bisher gar nicht im Katalog), Flag 4 = Kontextprozedur

| Kode | Text (OPS-Systematik) | Flag | `_KX` |
|---|---|---|---|
| 5-788.54 | Operationen an Metatarsale und Phalangen des Fußes: Osteotomie: Os metatarsale II bis V, 3 Ossa metatarsalia | 4 | |
| 5-788.55 | …: Osteotomie: Os metatarsale II bis V, 4 Ossa metatarsalia | 4 | |
| 5-788.59 | …: Osteotomie: Digitus II bis V, 3 Phalangen | 4 | |
| 5-788.5a | …: Osteotomie: Digitus II bis V, 4 Phalangen | 4 | |
| 5-788.5b | …: Osteotomie: Digitus II bis V, 5 oder mehr Phalangen | 4 | |
| 5-808.bh | Offen chirurgische Arthrodese: Zehengelenk: Interphalangealgelenk, Digitus II bis V, 5 oder mehr Gelenke | 4 | |
| 5-811.3k | Arthroskopische Operation an der Synovialis: Synovektomie, total: Oberes Sprunggelenk | 4 | I20M |
| 5-811.4k | Arthroskopische Operation an der Synovialis: Elektrothermische Denervierung von Synovialis und Kapselgewebe: Oberes Sprunggelenk | 4 | I20M |
| 5-785.2s / 2t / 2u | Implantation von keramischem Knochenersatz: Talus / Kalkaneus / Tarsale | 4 | |
| 5-785.3s / 3t / 3u | Implantation keramischer Knochenersatz, resorbierbar: Talus / Kalkaneus / Tarsale | 4 | |
| 5-785.4s / 4t / 4u / 4v / 4w | Implantation von metallischem Knochenersatz: Talus / Kalkaneus / Tarsale / Metatarsale / Phalangen Fuß | 4 | |
| 5-785.5s / 5t / 5u / 5v / 5w | Implantation keramischer Knochenersatz, resorbierbar, mit Antibiotikumzusatz: Talus / Kalkaneus / Tarsale / Metatarsale / Phalangen Fuß | 4 | |
| 5-796.pv | Offene Reposition einer Mehrfragment-Fraktur an kleinen Knochen: Durch Verriegelungsnagel: Metatarsale | 4 | |

Die Subkategorietitel von 5-785 (.2 keramisch, .3 keramisch resorbierbar, .4 metallisch, .5 keramisch resorbierbar mit Antibiotikumzusatz) und die Lokalisationsbuchstaben s bis w wurden am 09.09.2026 in der OPS-Version 2026 beim BfArM gegengeprüft. Die Texte zu 5-788.54 bis 5-788.5b, 5-808.bh, 5-811.3k/4k und 5-796.pv folgen dem Muster der Nachbarkodes im Katalog (5-788.53, 5-808.bg, 5-811.3h, 5-811.4h, 5-796.gv); der Wortlaut ist beim Eintragen in die Excel gegen den OPS-Text zu prüfen.

## B. Bestehende Zeilen: Kontextflag ergänzen (Flag 1 wird 5)

5-855.19 (Naht einer Sehne, primär, Unterschenkel; steht in I20-V69 und I20-V61), 5-810.4k (Entfernung freier Gelenkkörper OSG), 5-810.9k (Resektion von Bandanteilen OSG), 5-812.3k (Refixation osteochondrales Fragment OSG), 5-812.9k (Knorpeltransplantation OSG). Die vier Arthroskopiekodes stehen nur in I20-V69, nicht in I20-V61, deshalb zusätzlich `_KX` = I20M (in der Excel: Ausnahmespalte „I20M").

## C. Bestehende Zeilen: Kontextflag entfernen (Flag 5 wird 1)

5-788.67 und 5-788.68 (Arthroplastik Interphalangealgelenk). Nach den GFFC-Tabellen ist 5-788.67 neutral und 5-788.68 eine Aufwertung nach I20N; beide führen nicht aus der Hybrid-DRG heraus. Mit gesetztem Kontextflag würde die Code-Suche einen Ausweg anzeigen, den es nicht gibt.

## D. Unklar, bitte im Definitionshandbuch Tabelle I20-V69 nachsehen

Im Katalog als Kontextprozedur geführt, in den GFFC-Tabellen nicht gefunden: 5-796.xv (Sonstige offene Reposition Mehrfragmentfraktur Metatarsale), 5-854.0c (Sehnenverlängerung Mittelfuß und Zehen, im Katalog zugleich Hybrid), 5-854.xb und 5-854.xc (Sonstige Sehnenrekonstruktion Fußwurzel bzw. Mittelfuß). Möglich ist, dass die GFFC-Folie die Tabelle nicht vollständig abbildet. Bis zur Klärung bleibt das Flag stehen. Umgekehrt nennt die GFFC-Folie 5-819.4 ohne Lokalisation; in der OPS-Systematik tragen die 5-819-Kodes eine sechste Stelle (OSG = k). Der Kode ist im Regelblock enthalten, aber nicht für den Katalog vorgeschlagen, bis der vollständige Kode feststeht.

## E. Ausnahmen `_KX`

Bestand: 5-788.60, 5-854.1c, 5-854.2c mit [I20M], stimmt mit den Tabellen und der Grouper-Prüfung vom 07.09. überein. Neu hinzu (aus A und B): 5-810.4k, 5-810.9k, 5-812.3k, 5-812.9k, 5-811.3k, 5-811.4k mit [I20M].

## F. Reihenfolge für den Autor

Jetzt: Bucket-Upload `katalog2026.json` (erst löschen, dann hochladen) zusammen mit den anderen offenen Uploads aus DEPLOY.md, danach Push. Später: Master-Excel Blatt „Katalog" um die Zeilen aus A ergänzen, Flags aus B und C setzen, Ausnahmen aus E eintragen, D entscheiden; beim nächsten Neuerzeugen aus der Excel muss die JSON bis auf D unverändert herauskommen. Kontrolle nach dem Patch (Abgleich-Skript in der Sitzung): einzige Restabweichungen sind 5-819.4 und die vier D-Kodes.

Der Regelblock `HDRG_REGELN` bleibt die Quelle für die Fallsteuerung; die Code-Suche und die Fallsteuerung greifen nach dem Update auf denselben Stand zu.
