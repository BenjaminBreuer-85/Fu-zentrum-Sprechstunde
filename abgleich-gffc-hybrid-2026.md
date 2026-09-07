# Abgleich Fallsteuerung (`data/opsteuerung.json`) gegen GFFC-Arbeitskreis Abrechnung, Webinar 04.03.2026

Stand: 07.09.2026. Grundlage: drei Foliensätze des GFFC-Arbeitskreises Abrechnung (Einleitung; Lapidus und MTP-I-Arthrodese; ASK OSG und MT-I-Osteotomien), verglichen mit dem Stand von `opsteuerung.json` vom 03.09.2026. Hinweis: Die GFFC-Folien sind eine fachgesellschaftliche Auslegung, keine Rechtsquelle; die 1:1-Regel gilt weiterhin für `katalog2026.json` und `erloes2026.json`.

## Kernaussagen der GFFC-Folien, die für die App neu oder klärend sind

1. **Verlassen der Hybrid-DRG heißt „I20x bzw. EBM", nie „nur stationär".** Die GFFC schreibt bei allen Ausschluss-Kombinationen der MT-I-Osteotomien ausdrücklich „I20E bzw. EBM" oder „I20F bzw. EBM". Der ambulante Weg über den EBM bleibt offen. Das Label `"ziel": "keine H-DRG → nur stationär"` in der App ist damit inhaltlich falsch und muss bei allen Einträgen mit Ausschluss-Block geändert werden.

2. **5-788.54 (3× DMMO/Weil) ist in der GFFC-Übersicht in allen vier Fußspalten als Kontextprozedur geführt** (Lapidus, Lapidus mit Akin/Arthroplastik/Reverdin, MTP-I-Arthrodese, MT-I-Osteotomien). „Kontextprozedur" ist bei der GFFC der Sammelbegriff für Kodes, die aus der Hybrid-DRG herausführen; die App verwendet den Begriff genauso. Bei Chevron, Reverdin, Youngswick: mit 5-788.54/55 → I20E bzw. EBM. Bei MTP-I-Arthrodese: mit 5-788.54 → I20D, mit 5-788.55 → I20C. Bei Lapidus: mit 5-788.54/55 → I20D. In allen Fällen ohne weitere Kontextprozedur. Die GFFC kennzeichnet 5-788.54 nicht als „nicht im AOP-Katalog" (anders als etwa 5-811.xk bei der Arthroskopie), was dafür spricht, dass die drei Osteotomien ambulant über den EBM abrechenbar sind. Das ist gegen `katalog2026.json` zu verifizieren.

3. **Rahmenbedingungen 2026 für die Hybrid-Zuordnung:** Verweildauer unter 3 Tagen, Alter über 17, PCCL unter 3, kein hoher Pflegegrad, keine Fallzusammenlegung aus zwei Aufenthalten. Prüfen, ob die App diese fünf Bedingungen bei der Setting-Empfehlung abfragt oder zumindest als Hinweis zeigt.

4. **Preise 2026 (ohne Nachbehandlung):** I20M 3.280,38 €, I20N 2.085,14 €, I20O 1.006,54 €. Die App nennt I20N mit 2.085 €, stimmt. Die Vergleichswerte der Vollstationär-DRGs auf den Folien sind aG-DRG 2025 ohne Pflege (I20D 4.442,21, I20E 3.727,88, I20F 3.040,34) und daher nicht direkt mit den 2026-Werten der App (I20D 4.710, I20C 5.068) vergleichbar.

## Eintrag für Eintrag

### Chevron, Chevron + Akin, Scarf, Youngswick (I20O)

Stimmt: Ausschluss-Trigger (5-788.54/55, 5-788.60, 5-788.59/5a/5b, 5-788.62/63/64, 5-788.69/6a) decken sich vollständig mit der GFFC-Liste. Aufwertung zu I20N (5-788.52/53, 5-788.68, 5-808.be/bf/bg) deckt sich ebenfalls vollständig.

Zu ändern: Das Ausschluss-Ziel ist je Kode verschieden. GFFC: 5-788.60, 5-788.59/5a/5b und 5-788.62 führen nach I20F bzw. EBM; 5-788.54/55, 5-788.63/64 und 5-788.69/6a nach I20E bzw. EBM. Die App führt einen einzigen `drg`-Wert (I20E). Vorschlag: `ausschluss.triggers[].drg` je Trigger ergänzen und das Ziel-Label auf „keine Hybrid-DRG, stationär I20E/I20F oder ambulant EBM" setzen.

Ergänzung ohne Handlungsbedarf: Folgende Zusatzkodes lassen den Fall in I20O (keine Aufwertung, kein Ausschluss): 5-788.70/71 (plantare Platte), 5-788.57/58 (1 bis 2 Osteotomien D II–V), 5-808.bd (1× IP-Arthrodese). Könnte als neutrale Information in die Hinweise.

### MTP-I-Arthrodese (5-808.b0, I20N)

Stimmt: Hybrid-DRG I20N, Spongiosatransplantation (5-784.0v) als Kontextprozedur, die aus der Hybrid-DRG führt; Ziel I20E.

Zu ändern, Hinweistexte: „Stationär mit Kontextprozedur + 3× DMMO → I20D" beschreibt einen Umweg. Nach GFFC führt 5-808.b0 + 5-788.54 direkt nach I20D und + 5-788.55 direkt nach I20C, ohne Spongiosa. Formulierungsvorschlag: „3× DMMO MT II–V (5-788.54) führt aus der Hybrid-DRG und gruppiert stationär in I20D (+787 € gegenüber I20E); 4× (5-788.55) in I20C. Die Spongiosa-Kontextprozedur ist dafür nicht erforderlich."

Fehlt, Ausschluss-Block anlegen (alle nach GFFC „I20E", bei 5-788.60 ausdrücklich „keine Hybrid → EBM"):
5-788.60 (Arthroplastik MTP I) → I20E bzw. EBM
5-788.62/63/64 (2 bis 4× Arthroplastik MTP II–V) → I20E
5-788.69 (4× Arthroplastik IP II–V) → I20E
5-808.bh (5× IP-Arthrodese) → I20E
5-788.59/5a/5b (3 bis 5× Osteotomie D II–V) → I20E
5-788.54 → I20D, 5-788.55 → I20C

Fehlt, bleibt in I20N (neutral, als Hinweis sinnvoll): 5-788.61 (1× Arthroplastik MTP II–V), 5-788.65 (IP D I), 5-788.66/67/68 (1 bis 3× IP-Arthroplastik), 5-808.bd/be/bf/bg (1 bis 4× IP-Arthrodese), 5-788.57/58, 5-788.52/53 (1 bis 2× DMMO).

Fehlt, Aufwertung innerhalb Hybrid: 5-808.b0 + 5-808.a4 (Lapidus) → I20M (3.280 € statt 2.085 €).

Fehlt, Rezidiv: 5-808.b7 (Rearthrodese mit autogenem Knochen) + 5-783.2d + 5-784.1v → I20E, keine Hybrid-DRG.

### Lapidus (5-808.a4, I20M)

Stimmt: Lapidus allein ist keine Hybrid-DRG (I20D); Hybrid I20M nur mit Trigger; Hebel Spongiosa (5-783.0v + 5-784.0u) führt nach I20D; Warnhinweis, dass 5-854.1c, 5-788.60 und 5-854.2c in I20M keine Kontextprozeduren sind, deckt sich mit der GFFC-Folie „I20M – I20N/O Unterschied".

Zu prüfen, hdrgTrigger: GFFC nennt als Auslöser für I20M Arthroplastik 5-788.60, Akin 5-788.56 und Reverdin 5-788.5e. Die App nennt 5-788.5c (Chevron), 5-788.56 und 5-788.40 (Arthroplastik MT-Basis). 5-788.60 und 5-788.5e fehlen, 5-788.5c und 5-788.40 sind bei der GFFC nicht genannt. Gegen `katalog2026.json` (Hybrid-Liste I20M) abgleichen.

Ausschluss aus I20M nach GFFC (fehlt in der App als Block): 5-788.54/55 → I20D; 5-788.59/5a/5b → I20D; 5-788.62/63/64 → I20D; 5-788.69 → I20D; 5-808.bh → I20D; Spongiosa 5-783.0t + 5-784.0v → I20D. Bleibt I20M: 5-788.61, 5-788.66/67/68, 5-808.bd bis bg, 5-788.57/58, 5-788.52/53.

**5-854.2c ist bei I20M keine Kontextprozedur (bestätigt, Folien 15 und 16 in hoher Auflösung verglichen):** Die Kontextprozeduren-Liste für I20O/I20N enthält im Sehnenblock 5-854.1c und 5-854.2c, die Liste für I20M enthält beide nicht (Reihe 5-854.1b, 5-854.2b, 5-854.3b). Die Praxis des Zentrums, Lapidus mit Akin über 5-854.2c aus der Hybrid-DRG zu führen, funktioniert damit nicht; der Fall bleibt I20M. Herausführen tun nur die Kodes der roten Spalte der Übersichtsfolie (5-788.54/55, 5-788.59/5a/5b, 5-788.62/63/64, 5-788.69/6a, 5-808.bh, Spongiosatransplantation 5-783.0t + 5-784.0v). Vorschlag für die App: roter Warnhinweis, sobald bei Lapidus 5-854.2c als einziger Hebel gesetzt ist („Sehnentransfer 5-854.2c ist bei I20M keine Kontextprozedur, Fall bleibt Hybrid"). Empfehlung an den Autor: bereits stationär abgerechnete Fälle Lapidus + Akin + 5-854.2c mit der Kodierfachkraft durchsehen.

**Folge der Entscheidung „Akin immer bei Lapidus":** Der Akin-Kode 5-788.56 ist Hybrid-Trigger. Lapidus ohne Akin gruppiert stationär in I20D, Lapidus mit Akin in die Hybrid-DRG I20M, sofern kein Ausschluss oder Hebel greift. Das ist die „trojanische Prozedur" aus der GFFC-Folie in die andere Richtung. Die App bildet das über `hdrgTrigger` bereits ab; im Sprechstundenbrief steht Akin jetzt fest im Text, die Fallsteuerung muss den Trigger also standardmäßig als gesetzt behandeln.

### DMMO, Weil (I20O, allein)

Stimmt: Hybrid I20O, Ausschluss bei 5-788.54/55.
Zu ändern: Ziel-Label wie oben; Ziel-DRG für 3 bis 4 Osteotomien ohne MT-I-Eingriff gegen `erloes2026.json` prüfen (die GFFC-Folie behandelt nur die Kombination mit MT-I-Osteotomie, dort I20E).

### ASK OSG (I20O)

Der App-Eintrag hat weder Ausschluss noch Hinweise. Nach GFFC:
In I20O führen: 5-811.2k, 5-811.xk, 5-812.ek, 5-812.fk, 5-812.kk, 5-819.0k, 5-812.xk, 5-819.xk. Davon nicht im AOP-Katalog: 5-811.xk, 5-812.kk, 5-812.xk, 5-819.xk („Positivprozeduren").
Bleibt I20O in Kombination: 5-810.2k (Arthrolyse), 5-812.0k (Exzision Knorpel), 5-819.1k (Sehnendebridement).
Keine Hybrid-DRG in Kombination: 5-810.9k, 5-811.3k, 5-811.4k, 5-810.4k, 5-812.3k, 5-812.9k, 5-819.4.
Wichtige Falle (GFFC-Beispiel): Arthroskopische Arthrolyse (5-810.2k, AOP-Katalog, EBM E5, rund 1.783 € Chirurgie und Anästhesie) plus Osteophytenabtragung (5-812.kk, Positivprozedur) wird ambulant zur Hybrid-DRG I20O mit 1.006,54 €. Die Positivprozedur zieht den Fall in die schlechter vergütete Hybrid-DRG. Dazu das LSG Baden-Württemberg (L4 KR 799/23): Simultaneingriffe bei Arthroskopien brauchen neben der Zeitdokumentation einen gesonderten Zugangsweg; ein Portalwechsel genügt nicht.
Vorschlag: Ausschluss-Block, Positiv-Liste und Warnhinweis für `ask_osg` anlegen; Hinweis auch bei `amic` und `oats` prüfen (5-812.9k Knorpeltransplantation = keine Hybrid).

### TMT-Arthrodese

Der Eintrag hat bereits Modifikatoren „3 Gelenke" (5-808.a6 → I20C) und „4–5 Gelenke" (5-808.a7/a8 → I20B) mit `textErsatz`. Für den Auftrag `auftrag-chips-struktur.md` bedeutet das: Die Aufteilung TMT I, TMT II–III, TMT I–III lässt sich über diesen Modifikator-Mechanismus abbilden statt über neue Chips; die `textErsatz`-Texte brauchen dann ebenfalls „ggf. Augmentation".

## Reihenfolge

1. Label „nur stationär" bei allen Ausschluss-Blöcken ersetzen (Chevron, Chevron + Akin, Scarf, Youngswick, DMMO, Weil).
2. MTP-I-Arthrodese: Hinweistexte korrigieren, Ausschluss-Block, Aufwertung Lapidus, Rezidiv.
3. Lapidus: hdrgTrigger und Ausschluss gegen `katalog2026.json` abgleichen.
4. ASK OSG: Ausschluss, Positivprozeduren, Warnhinweis.
5. Rahmenbedingungen 2026 als Prüfliste in der Setting-Empfehlung.

Alle Änderungen an `opsteuerung.json` erst nach Freigabe des Autors und nach Gegenprüfung gegen `katalog2026.json` und `erloes2026.json`.

## Nachtrag 07.09.2026 abends: Gegenprobe gegen `data/katalog2026.json`

Die Katalogdatei (Quelle `OPS_Katalogdaten_2026_MASTER.xlsx`, Blatt „Katalog", 02.07.2026; Bitmaske 1 = AOP, 2 = Hybrid, 4 = Kontextprozedur; `_KX` = Ausnahmen je Hybrid-DRG) zeigt Folgendes:

1. **5-788.54 und 5-788.55 fehlen im Katalog vollständig**, also weder AOP noch Hybrid noch Kontextprozedur. Die Aussage des Autors, dass 3 und 4 Metatarsale-Osteotomien nicht im AOP-Katalog stehen, ist damit durch die App-Daten bestätigt. Folge für die Konsequenz-Zeile: „stationär I20E; ambulant nur mit unvergüteten Osteotomien (5-788.54 nicht im AOP-Katalog)". Das GFFC-Kürzel „bzw. EBM" bezieht sich auf den Haupteingriff.

2. **`_KX` stimmt mit der GFFC-Folie überein:** 5-788.60, 5-854.1c und 5-854.2c sind als Ausnahmen für I20M hinterlegt. Die App weiß also bereits, dass der Sehnentransfer beim Lapidus nicht wirkt; sie zeigt es nur nicht in der Fallsteuerung.

3. **Die Kontextprozeduren-Liste im Katalog (70 Kodes, „Bestand 02.07.2026") weicht von der offiziellen Tabelle I20-V69 (Definitionshandbuch Hybrid 2026, auf der GFFC-Folie abgebildet) ab.** Im Katalog als Kontextprozedur geführt, aber nicht in I20-V69: 5-788.67, 5-788.68 (nach GFFC neutral, Fall bleibt in I20N), 5-854.0c, 5-854.xb, 5-854.xc. In I20-V69 enthalten, aber im Katalog nicht als Kontextprozedur (teils gar nicht vorhanden): 5-788.54, 5-788.55, 5-788.59, 5-788.5a, 5-788.5b, 5-808.bh, 5-855.19 sowie die Knochenersatz-Kodes 5-785.2s/2t/2u, 3s/3t/3u, 4s bis 4w, 5s bis 5w (Talus, Kalkaneus, Tarsale). Vermutlich ist der Bestand aus der 2025er Liste übernommen. Das ist Katalogdatum und unterliegt der 1:1-Regel: Der Autor muss die Master-Excel gegen die Tabellen I20-V69 und I20-V61 des Definitionshandbuchs Hybrid-DRG 2026 aktualisieren und `katalog2026.json` neu erzeugen. Bis dahin zeigt die OPS-Suche bei 5-788.54 „nicht gelistet" und bei 5-788.68 fälschlich „Kontextprozedur".

4. **Lapidus-Trigger:** 5-788.5c, 5-788.5e, 5-788.51, 5-788.56, 5-788.40 und 5-788.60 sind alle als Hybrid-Kodes geführt; 5-808.a4/a5/a6 fehlen im Katalog (die Lapidus-Kodes selbst sind kein Hybrid-Trigger, das deckt sich mit der GFFC-Aussage „Lapidus allein keine Hybrid"). Der Katalog entscheidet damit nicht, welche der Zusatzkodes I20M auslösen; das bleibt eine Steuerungsangabe in `opsteuerung.json` (`hdrgTrigger`). Ich übernehme die GFFC-Liste (5-788.56, 5-788.5e, 5-788.60) und ergänze 5-788.5c und 5-788.40 nur, wenn der Autor sie aus der Praxis bestätigt.

5. **Arthroskopie:** Die Katalogflags decken sich mit der GFFC-Folie: 5-811.xk, 5-812.kk, 5-812.xk, 5-819.xk sind Hybrid ohne AOP (Positivprozeduren); 5-810.2k, 5-812.0k, 5-819.1k sind AOP ohne Hybrid; 5-810.4k, 5-810.9k, 5-812.3k, 5-812.9k sind AOP; 5-811.3k, 5-811.4k und 5-819.4 fehlen im Katalog (nach GFFC „keine Hybrid").

Konsequenz für `HDRG_REGELN`: Der Block wird aus den GFFC-Tabellen I20-V69 und I20-V61 gebaut, nicht aus den heutigen Katalogflags, und mit dem Hinweis versehen, dass er nach der Aktualisierung der Master-Excel gegen `katalog2026.json` erneut geprüft wird.

## Nachtrag 07.09.2026 spät: Bestätigung des Autors und Korrektur des Lapidus-Hebels

Der Autor hat im Grouper geprüft: Lapidus mit Akin bleibt auch mit 5-854.2c in I20M. Ausweg nur über Spongiosatransplantation oder 5-788.54. Ergänzung des Autors: Auch eine auf einen Belegungstag gekürzte I20D mit Zusatzkode ist besser als die Hybrid-DRG. Rechnung mit den App-Werten: I20D rund 4.710 € abzüglich UGVD-Abschlag 1.079 € für den einen Tag ergibt rund 3.630 € zuzüglich Pflegeentgelt, gegenüber I20M 3.280 € pauschal; ab zwei Belegungstagen entfällt der Abschlag.

Korrektur am Lapidus-Eintrag in `opsteuerung.json`: Der hinterlegte Hebel „5-783.0v + 5-784.0u" (Transplantation Tarsale) ist wirkungslos, weil 5-784.0u weder im Katalog noch in der Tabelle I20-V61 als Kontextprozedur steht. Wirksam ist die Transplantation an das Metatarsale, 5-784.0v (Kontextprozedur laut Katalog und GFFC). Der Entnahmekode ist keine Kontextprozedur und richtet sich nach der Entnahmestelle: 5-783.0v bei Spongiosa aus der abgetragenen Pseudoexostose (so steht es im OP-Bericht-Baustein), 5-783.0t bei Entnahme am Kalkaneus. Neuer Hebel: „5-783.0v + 5-784.0v", Hebelname „Spongiosa MT I". Wird mit dem `HDRG_REGELN`-Block zusammen geändert.
