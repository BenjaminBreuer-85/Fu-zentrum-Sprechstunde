# Hybrid-DRG-Systematik Fußchirurgie: Referenzdokument

Stand: 13.09.2026 abends, zweite Fassung mit Nachträgen V1a–c, V9 (nach Auswertung des Ordners `GitHub/Hybrid` und der Nachlieferungen). Vom Autor am 13.09.2026 als Bezugspunkt freigegeben; Ablage im Repo-Root und im Projekt. Änderungen nur als datierter Nachtrag. Zweck: eine Stelle, an der die Systematik der Hybrid-DRG (Zuordnung, Ausschluss, Kodierung, Erlös) mit Quelle und Gültigkeitsjahr festgehalten ist, damit jede Änderung an `opsteuerung.json`, `katalog2026.json`, `erloes2026.json` oder an der Fallsteuerung in `app.html` gegen dieses Dokument geprüft werden kann. Grundregel des Autors: **Es zählen immer die Regeln des laufenden Jahres, derzeit 2026.** Ältere Aussagen stehen hier nur, damit erkennbar ist, was sich geändert hat. Nichts in diesem Dokument ist neu erfunden; jede Aussage trägt Quelle und Jahr. Wo Quellen sich widersprechen oder die App etwas anders macht, steht das in Abschnitt 8 und 9.

## 0. Jahresübersicht: Was sich 2024, 2025 und 2026 geändert hat

| Thema | 2024 | 2025 | 2026 (gilt) |
|---|---|---|---|
| Rechtsgrundlage | Hybrid-DRG-Verordnung BMG 19.12.2023, Anlage 2 (VO; FR S. 4, BK S. 3) | Vereinbarung der Vertragspartner, Änderungsvereinbarung 11.10.2024 (SCH S. 10–11) | Beschluss des ergänzten erweiterten Bewertungsausschusses 28.04.2025 zum Leistungskatalog 2026 (BA-2026 S. 1–3); Vergütung nach KBV-Tabelle vom 05.12.2025 (VG-2026) |
| Fuß-Hybrid-DRGs | I20M (aus I20F), I20N (aus I20E) | unverändert | I20O (aus I20F), I20N (aus I20E), I20M (aus I20D); die Kürzel M und N wechseln die Bedeutung (MU S. 16, DH S. 411) |
| Pauschalen | I20M 909,25 €, I20N 1.072,95 € (VO Anlage 2) | plus 11,6 % bzw. 2,1 % (BK S. 38); Nachbehandlung plus 30 € (Autor, „Hybrid 2025") | VG-2026 nennt zwei Tabellen: I20M 3.341,18 / I20N 2.120,68 / I20O 1.018,50 (S. 1–12) und I20M 3.280,38 / I20N 2.085,14 / I20O 1.006,54 (S. 13–23), jeweils plus 30 € mit postoperativer Nachbehandlung im Krankenhaus. GFFC (MU S. 13, WE S. 5) und die App verwenden die zweite Tabelle. Welche für die Klinik gilt: offen, V9 |
| Positivliste Fuß | I20-V60, 66 OPS (FR S. 5–6, 10–11) | plus 68 OPS (BK S. 8–9; SCH S. 15–17); Achillessehnennaht 5-855.19 gestrichen (SCH S. 12) | I20-V68 „Hybrid MDC 08 – 1", 161 OPS in OPS-Fassung 2024 des Handbuchs, 167 nach GFFC-Zählung (MU S. 17–19; DH S. 1079–1080); amtlicher Leistungskatalog 2026 gesamt 904 OPS (BA-2026, LK-2026) |
| Kontextprozeduren | I20-V59 „Komplexer Eingriff am Fuß" (BK S. 12, SCH S. 6) | I20-V59 erweitert (BK S. 13) | zwei Listen: I20-V70 „Hybrid MDC 08 – 8" für I20N und I20O (88 Kodes) und I20-V66 „Hybrid MDC 08 – 7" für I20M (85 Kodes); Unterschied: 5-788.60, 5-854.1c, 5-854.2c wirken nur bei I20N/I20O (DH S. 1078–1081). Achtung: Die GFFC-Folien vom 04.03.2026 nennen dieselben Listen „I20-V69" und „I20-V61"; in der App-Datei steht diese GFFC-Bezeichnung. Im Handbuch 2024/2026 ist I20-V69 „Hoher Pflegegrad" und I20-V61 „Eingriffe Zehenstrahl II bis V und Sehnen am Fuß (II)". Inhaltlich stimmen die App-Listen mit V70/V66 überein (Abschnitt 7) |
| Verweildauer | < 2 Tage (FR S. 12) | < 2 Tage | Tagesdifferenz Aufnahme–Entlassung ≤ 2, VWD < 3 Tage (DH S. 1042; MU S. 9; BA-2026 S. 1 „bis zu zwei Tagen") |
| Alter | > 1 Jahr (FR S. 12) | > 1 Jahr | > 17 Jahre (DH S. 1042; MU S. 9, 29) |
| Beidseitig | wie einseitig vergütet (FR S. 27) | wie einseitig | Ausschluss: „Nicht [beids. Pr Hybrid MDC 08 – 17 (I20-V67)]", 82 Kodes (DH S. 1042, 1079) |
| Pflegegrad | – | – | Ausschluss Pflegegrad 4 und 5, I20-V69 = 9-984.9, 9-984.a (DH S. 1081) |
| Diagnosen | – | – | Ausschluss Hauptdiagnose aus I20-V9 (Frakturen obere Extremität), I20-V10 (Frakturen Unterschenkel/Knöchel), I20-V11 (M96.0 Pseudarthrose nach Arthrodese, S82.5/.6/.81/.82 Knöchelfrakturen) (DH S. 1042, 1057–1058) |
| OPS-Fassung | OPS 2024 | OPS 2025: 5-808.b2–b5 aufgeteilt in 5-808.b9–bc (MTP II–V) und 5-808.bd–bg (IP II–V), 5-808.b6 in 5-808.bh (OPS-2026-Liste GFFC) | Das Handbuch 2024/2026 führt die Tabellen in OPS-Fassung 2024 (5-808.b2–b5 statt b9–bg); der Leistungskatalog 2026 in OPS 2026. Beim Vergleich ist zu übersetzen |
| Zuzahlung Implantate | – | – | GFFC-Vortrag 28.11.2025 (ZZ-2025), nicht ausgewertet, betrifft Abrechnung, nicht Zuordnung |

## 1. Quellen und ihr Rang

| Kürzel | Quelle | Jahr | Rang |
|---|---|---|---|
| DH | aG-DRG-Version 2024/2026 Definitionshandbuch Band 2 (InEK, 1.406 S.), `GitHub/Hybrid/GFFC 2025 Abrechnung/DefHandbuch_aGDRG_2024_2026_Band2.pdf`. Definitionen DRG I20M S. 1042–1045 (PDF 1054–1057), I20N S. 1046–1053, I20O S. 1054; Tabellen I20-V1 bis V70 S. 1055–1081 (PDF 1067–1093); Struktur MDC 08 S. 409, 411 (PDF 421, 423). Seitenangaben unten sind Handbuchseiten | 2026 | 1, verbindlich für die Zuordnung |
| BA-2026 | Beschluss des ergänzten erweiterten Bewertungsausschusses 28.04.2025 zum Hybrid-DRG-Leistungskatalog 2026 (35 S., KGNW-Rundschreiben 276/2025 Anlage 1) mit Anlage Leistungskatalog; Entscheidungserhebliche Gründe (21 S., Anlage 2) | 2026 | 1 |
| LK-2026 | hybrid-drg-leistungskatalog-2026.xlsx, 904 OPS | 2026 | 1 |
| VG-2026 | hybrid-drg-verguetung-2026.pdf (KBV, 05.12.2025), Fallpauschalen Spalte A ohne / Spalte B mit postoperativer Nachbehandlung im Krankenhaus; zwei Tabellen, siehe V9 | 2026 | 1 |
| VO | Hybrid-DRG-Verordnung 19.12.2023 mit Anlage 2; Referentenentwurf 28.09.2023 (RefE) | 2024 | 1, nur 2024 |
| MU | Wilde, „Hybrid DRG 2026", 33. Symposium 05.12.2025 (33 S.) | 2026 | 2 |
| WE | GFFC & Friends Webinar 04.03.2026: Einleitung (12 S.), Lapidus und MTP-I-Arthrodese (30 S.), ASK OSG und MT-I-Osteotomien (18 S.), Verteilung H-DRG 2026 Schemmann (16 S.); ausgewertet in `abgleich-gffc-hybrid-2026.md` | 2026 | 2 |
| AUF | „Übersicht Aufteilung Hybrid-DRG 2026", GFFC 30.12.2025 (31 S.) | 2026 | 2, Kostenaufteilung |
| GFFC-OPS | „OPS-Codes DRG 2026 Chirurgie" (GFFC-Tabelle mit Jahr der Aufnahme je Kode; Fuß 2024: 117, 2025: 113, 2026: 136) | 2026 | 2 |
| BK | Köhne/Wilde, Beleger und Klinikbetreiber, 32. Symposium 29.11.2024 (39 S.) | 2024/25 | 2 |
| FR | GFFC & Friends „Hybrid-DRGs 2024" (42 S.) | 2024 | 2 |
| NÜ | Köhne/Schemmann/Wilde, Nürnberg/Penzberg 08.05.2024 (23 Folien) | 2024 | 2 |
| SCH | Schemmann „Hybrid-DRG 2024–2025" (27 S.), Axomed-Baum, KBV-Stand 08.11.2024 | 2024/25 | 2 |
| BVOU | „Grundlagen Hybrid-DRG" BVOU/Lembeck (46 S., 12/2024) | 2024/25 | 2, Kalkulation |
| DIA | „Hybrid Diakonie" (93 S., 06/2025) | 2025 | 2, nicht ausgewertet |
| GFFC-ST | GFFC-Stellungnahme zum Referentenentwurf (10/2023) | 2023 | 3, historisch |
| BB-2024 | Autor, „Konzept ambulantes Operieren und Hybrid-DRG für die Fußchirurgie" (01/2024) | 2024 | 2, eigene Festlegung |
| BB-2025 | Autor, „Hybrid 2025" (Notizen 04/2025) | 2025 | 2, eigene Festlegung |
| WG | Webgrouper-Läufe des Autors (GetDRG, G-DRG 2026), z. B. 29./30.08.2026 | 2026 | 2, empirisch für den Einzelfall |
| APP | `app.html`, `data/opsteuerung.json`, `data/katalog2026.json`, `data/erloes2026.json` (Commit 63c16e8 plus Patch 09.09.2026) | 2026 | 3, Umsetzung, nie Quelle |
| FK | Fragenkatalog zur Hybrid-DRG (Umfrage 04/2024) | – | keine Regelquelle |

Regel für dieses Dokument: Eine Aussage wird nur aufgenommen, wenn sie in einer Rang-1-Quelle des Jahres 2026 steht, in einer Rang-2-Quelle 2026 mit Folie belegt ist oder der Autor sie per Webgrouper 2026 geprüft hat. Rang-2-Aussagen gelten als Auslegung; wo sie über DH hinausgehen, ist das markiert. Ältere Jahre werden nur zur Abgrenzung genannt. Rang 3 (die App) wird gegen Rang 1 und 2 geprüft, nie umgekehrt.

## 2. Grundbegriffe (Stand 2026)

**Hybrid-DRG.** Sektorengleiche Pauschale nach § 115f SGB V für ambulant und vollstationär erbrachte Fälle mit Verweildauer bis zu zwei Tagen (BA-2026 S. 1). Krankenhaus: keine Wahlfreiheit, hybridfähige Fälle werden als Hybrid abgerechnet (FR S. 39; BB-2025). Vertragsarzt: theoretische Wahlfreiheit (FR S. 40).

**Basis-DRG und Hybrid-Zwilling 2026.** I20M ist die Hybrid-DRG der DRG I20D, I20N der I20E, I20O der I20F (DH S. 1042, 1046, 1054; Struktur S. 411). Die Hybrid-Abfrage sitzt im Entscheidungsbaum unmittelbar vor der jeweiligen Basis-DRG (DH Struktur S. 411).

**Positivliste I20-V68.** Tabelle „Hybrid MDC 08 – 1", Bedingung „Pr Hybrid MDC 08 – 1 (I20-V68)" in allen drei Definitionen (DH S. 1042). Mindestens ein Kode des Falls muss darin stehen. Katalogflag 2 in `katalog2026.json`.

**Kontextfaktoren.** Ausschlussbedingungen auf Fallebene in den Definitionstabellen (DH S. 1042): Alter > 17, PCCL < 3, VWD < 3 Tage und Tagesdifferenz ≤ 2, kein hoher Pflegegrad (I20-V69), nicht beidseitig (I20-V67), keine Hauptdiagnose aus I20-V9/V10/V11, „Nicht [Ausschluss Kontextfaktoren MDC 08]" (Tabelle in Band 4, S. 5525, liegt nicht vor). GFFC-Zusammenfassung MU S. 9 und 29.

**Kontextprozeduren.** Ausschlussbedingung auf Kodeebene: „Ohne Pr Hybrid MDC 08 – 8 (I20-V70)" bei I20N/I20O, „Ohne Pr Hybrid MDC 08 – 7 (I20-V66)" bei I20M (DH S. 1042, 1046; Tabellen S. 1078, 1081). Vier Gruppen: Knochentransplantation und Knochenersatz (5-784, 5-785), Osteotomien und Arthroplastiken ab bestimmter Zahl (5-788.54/55/59/5a/5b/62/63/64/69/6a, 5-808.b6 bzw. OPS 2026 5-808.bh), offene Frakturreposition (5-795, 5-796), Sehnenrekonstruktion Fußwurzel/Mittelfuß (5-854.0b–9c) und Achillessehnennaht 5-855.19. Katalogflag 4.

**Positivprozeduren.** Kodes der Positivliste ohne AOP-Eintrag: ambulant nur als Hybrid, nicht als EBM (WE ASK OSG; HDRG_REGELN `positiv`: 5-811.xk, 5-812.kk, 5-812.xk, 5-819.xk, alle in I20-V68, DH S. 1080).

**Aufwertung, neutral.** GFFC-Begriffe für Zusatzkodes, die die Hybrid-Stufe heben (I20O nach I20N, I20N nach I20M) oder nichts ändern (MU S. 22–24). Im Handbuch ergibt sich das aus den Zusatzbedingungen der Definitionen (Tabellen I20-V12 bis V23, V34/V36/V40/V50/V51), nicht aus eigenen Listen.

**AOP-Katalog.** § 115b SGB V, Anlage 1; bindet Kliniken. Kode nicht im AOP-Katalog: Klinik ambulant nur über Hybrid (FR S. 15–16; Sprachregel des Autors 09.09.2026). Katalogflag 1; Hybrid-Vorrang (Flag 2 schlägt Flag 1) nach Regel des Autors 02.07.2026.

**Trojanische Prozeduren.** Kodes, die einen Fall unbemerkt in die Hybrid-DRG hinein- oder herausziehen (MU S. 24; FR S. 25; NÜ S. 17–19).

## 3. Die drei Fuß-Hybrid-DRGs 2026

| H-DRG | Basis-DRG | Pauschale 2026 Spalte A / B (VG-2026 S. 13–23, von GFFC und App verwendet) | Alternative Tabelle VG-2026 S. 1–12 | App `_HDRG` |
|---|---|---|---|---|
| I20O | I20F (3.120 € 2026 App; 3.040,34 € 2025 MU) | 1.006,54 / 1.036,54 | 1.018,50 / 1.048,50 | 1007 |
| I20N | I20E (3.923 €; 3.727,88 €) | 2.085,14 / 2.115,14 | 2.120,68 / 2.150,68 | 2085 |
| I20M | I20D (4.713 €; 4.442,21 €) | 3.280,38 / 3.310,38 | 3.341,18 / 3.371,18 | 3280 |

Inhalt der Stufen nach MU S. 22–24 (2026): I20O Hallux valgus subkapital auch mit Akin, 1× Hohmann, 1–4× PIP-Arthrodese, 1–2× Weil/DMMO, ASK OSG mit Hybrid-Kodes, Haglundabtragung, Biopsie/Tenotomie, Schleimbeutel/Ganglion, Débridement Phalanx. I20N MTP-I-Arthrodese (auch mit 1–3 Hohmann, 1–4 PIP, 1–2 Weil/DMMO), Hallux valgus mit Zusatzeingriffen (3 Hohmann, 2–4 PIP, 1–2 Weil/DMMO). I20M Lapidus nur mit Reverdin/Arthroplastik/Akin (dann auch mit 1–3 Hohmann, 1–4 PIP, 1–2 Weil/DMMO), MTP-I-Arthrodese mit Exostosenresektion MT II–V/3 Phalangen. Rückfuß-Arthrodesen und Achskorrekturen des Rückfußes keine Hybrid (MU S. 24).

## 4. Prüfreihenfolge: So entscheidet der Grouper 2026

Reihenfolge nach DH Struktur MDC 08 (S. 409, 411) und den Definitionstabellen (S. 1042ff), ergänzt um den Axomed-Baum (SCH S. 5). Jede Regel trägt eine Nummer H-xx, auf die App-Daten, Testfälle und Prüfskripte verweisen.

**H-01 Hauptdiagnose und MDC.** Nur Fälle in MDC 08 erreichen die Fuß-DRGs. Hauptdiagnose diabetisches Fußsyndrom (E10.74/75, E11.74/75) führt in MDC 05 (F27), Hauptdiagnose Nerv (G57.6 Morton-Neurom) in MDC 01; beide nie Fuß-Hybrid (`abrechnung-diabetischer-fuss-drg2026.md`, WG 29.08.2026; BB-2025: „Alle Diagnosen mit Nerven G… als Hauptdiagnose, daher Morton nicht Hybrid"). Diabetes mit Komplikationen oder chronische Polyarthritis als Nebendiagnose (Tabelle I20-V8, DH S. 1057) ist dagegen ein Split nach I20E und damit Richtung I20N (DH Struktur S. 411; SCH S. 25).

**H-02 Kontextfaktoren auf Fallebene (Ausschluss).** Nach DH S. 1042 (Definition I20M, gleichlautend I20N/I20O): Alter > 17 Jahre; PCCL < 3; VWD < 3 Tage und Tagesdifferenz Aufnahme–Entlassung ≤ 2; kein Pflegegrad 4 oder 5 (I20-V69, DH S. 1081); nicht beidseitig (I20-V67, 82 Kodes der Positivliste, DH S. 1079); keine Hauptdiagnose aus I20-V9 (Frakturen Klavikula, Humerus, Unterarm, Hand), I20-V10 (Frakturen Unterschenkel, Knöchel, Patella), I20-V11 (M96.0 Pseudarthrose nach Fusion/Arthrodese, S82.5, S82.6, S82.81, S82.82) (DH S. 1057–1058); „Nicht [Ausschluss Kontextfaktoren MDC 08]" (Band 4, liegt nicht vor; nach MU S. 9 Fallzusammenlegung aus zwei Aufenthalten). Zerebralparese G80.x (I20-V2, DH S. 1055) steht ganz oben im I20-Baum und führt nach I20A/B (Struktur S. 411), also nie zur Hybrid-Abfrage. Sonstige Nennungen MU S. 29 (mehrere Lokalisationen, Mehrfachfrakturen, Weichteilschaden III, Knochenersatz, Transplantationen, Pseudarthrose, DRG-spezifische Ausnahmen) sind teils Kontextprozeduren (H-05), teils Diagnosen (I20-V3/V5/V7), keine eigene Fallregel.

**H-03 Höher eingestufte DRG schlägt Hybrid (Verdrängung).** Der Baum prüft die DRG-Zweige von komplex nach einfach; die Hybrid-Abfrage liegt erst unmittelbar vor I20D, I20E und I20F (DH Struktur S. 411). Ein Kode oder eine Kombination, die in I20A–I20C oder bei I20N/I20O-Fällen in I20D führt, verhindert damit die Hybrid-DRG (SCH S. 5: „Prozedur oder Kombination, welche eine höher bewertete DRG als I20F oder I20E auslöst"). Für Kodes anderer Basis-DRGs (Unterschenkel, Weichteile) entscheidet die Zuteilungsfunktion „LG_allgemein" mit Rangzahl je DRG (DH Struktur S. 409, 411): I20M 102, I20D 103, I27D 114, I20N 119, I20E 120, I27E 129, I20O 135, I20F 136 (kleinere Zahl gewinnt; I59Z nach automatischem Auszug 130, Seite nicht einzeln geprüft). Folgen, sofern der Webgrouper sie bestätigt (V1, V2): Ein I27E-Kode (Tendoskopie 5-852.29, Bursektomie Unterschenkel 5-859.19) schlägt I20O/I20F, aber nicht I20N/I20E und nicht I20M/I20D. Ein I27D-Kode (FHL-Transfer 5-854.29) schlägt I20N und I20O; bei I20M bleibt der Fall zwar in I20D (Rang 103 vor 114), verliert die Hybrid aber trotzdem (Webgrouper 13.09.2026: I20D), also über eine zweite Sperre, siehe V10. Das deckt sich mit SCH S. 24 (Haglund + Bursektomie Unterschenkel > 15 J.: I27E, EBM) und SCH S. 23 (< 16 J.: I20E, dann I20N), und mit BB-2025 („gilt auch für Eingriffe aus I27E, I59Z") nur für die Stufen I20N/I20M. Aussage des Autors 13.09.2026 „Tendoskopie mit Haglund ist I20O" und „alles über I20C oder CM 1,111 sicher raus": nach DH liegt die Grenze bei der Rangzahl, nicht beim Gewicht; I20D verdrängt I20N/I20O, nicht I20M.

**H-04 Positivliste.** Mindestens ein Kode in I20-V68 (DH S. 1042, 1079–1080). Lapidus 5-808.a4/a5 stehen nicht darin (Tabellen V16, V28, V29, V32, V40, V42), Lapidus allein ist keine Hybrid-DRG (MU S. 24). Mit einem Positivkode (Akin 5-788.56, Reverdin 5-788.5e, Arthroplastik 5-788.60, distale OT 5-788.5c, Weichteilkorrektur 5-788.40, alle in V68 und nicht in V66) wird der Fall I20M, weil Lapidus über V40 „Bestimmte Eingriffe an Sprunggelenk, Fuß (I)" die I20D-Bedingung erfüllt (DH S. 1043). Die fünf `hdrgTrigger` der App sind damit belegt (V5 erledigt).

**H-05 Kontextprozeduren.** Ein Kode aus I20-V70 (I20N/I20O) bzw. I20-V66 (I20M) verlässt die Hybrid-DRG; Ziel stationär die Basis-DRG oder höher, ambulant der EBM, sofern alle Kodes im AOP-Katalog stehen (WE; `abgleich-gffc-hybrid-2026.md` Kernaussage 1). V70 minus V66 = {5-788.60, 5-854.1c, 5-854.2c}: bei I20M keine Kontextprozeduren (DH S. 1078, 1081; MU S. 29; WG des Autors 07.09.2026). HDRG_REGELN entspricht V70/V66 bis auf die OPS-Übersetzung 5-808.b6 → 5-808.bh und sieben Arthroskopiekodes, die nur nach GFFC ausschließen (V8).

**H-06 Aufwertung innerhalb der Hybrid.** Zusatzkodes aus den Tabellen der I20E-Bedingung (V12–V21) heben einen I20F-Fall nach I20E und damit I20O nach I20N; Zusatzkodes aus der I20D-Bedingung (V34\V50, V36\V51, V40\V52) heben nach I20D/I20M (DH S. 1042–1047). GFFC-Beispiele MU S. 23–24: 1–2 DMMO, 2–4 PIP, 3 Hohmann nach I20N; MTP-I + Lapidus oder + Exostosen MT II–V nach I20M. HDRG_REGELN `aufwertung` (7 Einträge) folgt den GFFC-Beispielen; Handbuch-Herleitung je Kode offen (V6).

**H-07 Ambulant oder stationär.** Innerhalb der Hybrid ist der Erlös gleich; die Frage ist nur, ob die Klinik ambulant erbringen darf (AOP-Katalog oder Positivprozedur). Außerhalb der Hybrid: stationär volle DRG mit UGVD-Abschlag (`erloes2026.json` GVD, `UGVD_ABSCHLAG`), ambulant EBM nur mit AOP-Kodes (FR S. 15–16, SCH S. 24). MD-Risiko: Kürzung auf 1 Tag macht aus dem DRG-Fall einen Hybrid-Fall (FR S. 27, 29). Postoperative Nachbehandlung im Krankenhaus plus 30 € (VG-2026 Spalte B; BB-2025: Kennzeichnung 88110).

**H-08 Inhalt der Pauschale.** OP, Anästhesie und Prämedikation, Sachkosten und Implantate außer Sprechstundenbedarf, Labor, Pathologie, Übernachtung, Nachbeobachtung (BK S. 38; SCH S. 13; BB-2025). Nicht enthalten: Nachbehandlung außerhalb der 30 € (VG-2026). Aufteilung Chirurgie/Anästhesie jährlich zu verhandeln (BK S. 33, 37; AUF, GFFC 30.12.2025). Lokalanästhesie ist ebenfalls Hybrid (BK S. 33). Sprechstundenbedarf je KV verschieden; Nordrhein erlaubt Drähte, Platten, Schrauben (BB-2025).

**H-09 Kodierung.** Alle relevanten Prozeduren kodieren, gleichwertig, unabhängig von OP-Zeit (FR S. 24). Ein im EBM nicht abrechnungsrelevanter Zusatzkode (Arthroplastik 5-788.60 beim Chevron) entscheidet im Hybrid-System (FR S. 25). Seitenangabe ist 2026 gruppierungsrelevant (I20-V67). Kontextprozeduren nur kodieren, wenn erbracht und im OP-Bericht dokumentiert; erbrachte nie weglassen (App-Hinweis Metallentfernung; NÜ S. 20 „Missachtung der Kodierrichtlinien … keine Lösung").

## 5. Beispiele aus den Quellen (Sollwerte für Tests, Stand 2026 soweit nicht anders vermerkt)

| Konstellation | Ergebnis | Quelle |
|---|---|---|
| Hallux valgus subkapital 5-788.5e allein oder mit Akin 5-788.56 | I20O | MU S. 22 |
| Hallux valgus + Arthroplastik 5-788.60 | keine Hybrid (I20F/EBM) | MU S. 22; V70 |
| Hallux valgus + 1× Hohmann | I20O; > 1 Hohmann keine Hybrid | MU S. 22 (V6) |
| Hallux valgus + 1× PIP | I20O; + 2–4× PIP I20N | MU S. 22–23 (V4) |
| Hallux valgus + 1–2× Weil/DMMO | I20N; > 2 keine Hybrid | MU S. 23; V70 |
| Hallux valgus + 3× DMMO 5-788.54, 1 Tag | 2024: I20N (FR S. 16); 2026: 5-788.54 in V70, Ausschluss → I20E | FR; DH S. 1081 |
| 3× DMMO allein, 1 Tag | I20F, nicht im AOP-Katalog, für Kliniken nur stationär | FR S. 15 |
| Metatarsalgie 1–2× Weil/DMMO | I20O | MU S. 22 |
| ASK OSG mit Hybrid-Kodes | I20O; Arthrolyse kein Kontextfaktor | MU S. 22 |
| Haglundabtragung 5-782.at | I20O | MU S. 22; V68 |
| Haglund + Bursektomie Unterschenkel 5-859.19, > 15 J., 1 Tag | I27E, ambulant EBM | SCH S. 24 (2024/25); H-03 Rang 129 < 135 |
| Haglund + Bursektomie Unterschenkel, < 16 J., 1 Tag | I20E wegen Alter, Hybrid I20N | SCH S. 23 (2024/25; 2026 durch Alter > 17 hinfällig) |
| MTP-I-Arthrodese 5-808.b0 allein | I20N | MU S. 23 |
| MTP-I + 1–3 Hohmann / 1–4 PIP / 1–2 Weil | I20N; > 3 Hohmann, > 2 Weil, Arthroplastik keine Hybrid | MU S. 23 |
| MTP-I + Exostosen MT II–V 3 Knochen 5-788.08 | I20M | MU S. 24; V36 |
| MTP-I + 3× / 4× DMMO | I20D / I20C, keine Hybrid | WE; APP Z. 3307/3312 |
| Lapidus allein | keine Hybrid (I20D) | MU S. 24; V68 |
| Lapidus + Akin/Reverdin/Arthroplastik | I20M | MU S. 24; V40 + V68 |
| Lapidus + Akin + 5-854.2c | bleibt I20M | V70\V66; WG 07.09.2026 |
| Lapidus + Spongiosa 5-783.0v + 5-784.0v | I20D, keine Hybrid | V66 |
| Arthrorise 5-809.1m, Patient < 18 | Positivliste ja, Alter → keine Hybrid | DH S. 1042; APP Z. 5007 |
| Arthrorise bds. Kind, 1 Tag | 2024: I20N 1.072,95 € (FR S. 33); 2026: Alter und Beidseitigkeit → keine Hybrid | FR; DH |
| Rückfuß-Arthrodesen, Achskorrekturen Rückfuß | keine Hybrid | MU S. 24 |
| Rezidiv MTP-I 5-808.b7 + 5-783.2d + 5-784.1v | I20E, keine Hybrid | WE |
| Achillessehnennaht 5-855.19 | 2024 Positivliste (FR S. 6); 2025 gestrichen (SCH S. 12); 2026 Kontextprozedur (V66/V70) | FR; SCH; DH |
| Tendoskopie 5-852.29 allein | I27E stationär; ambulant EBM (AOP-Flag 1) | WG 30.08.2026; Katalog |
| Tendoskopie 5-852.29 + Calcaneoplastie 5-782.at, HD Haglund-Exostose | I27E, keine Hybrid, ambulant EBM (Webgrouper des Autors 13.09.2026, bestätigt H-03 Rang 129 < 135) | WG 13.09.2026 |
| Tendoskopie 5-852.29 + MTP-I-Arthrodese 5-808.b0, HD M20.2 | I20N, Hybrid bleibt (Rang 119 < 129) | WG 13.09.2026 |
| FHL-Transfer 5-854.29 + Lapidus 5-808.a4 + Akin 5-788.56, HD M20.1 | I20D, keine Hybrid: der Fall bleibt in I20 (Rang I20D 103 < I27D 114), die Hybrid-Bedingung scheitert aber; 5-854.29 steht in keiner I20-Tabelle von Band 2, vermutlich in „Ausschluss Kontextfaktoren MDC 08" (Band 4, V10). Aussage des Autors „FHL holt raus" bestätigt | WG 13.09.2026 |

## 6. Erlös: Wann lohnt sich welcher Weg

Hybrid-Pauschalen liegen 2026 bei 33 %, 56 % und 74 % der Basis-DRG 2025 (MU S. 16). Eingriffe ohne Implantatkosten profitieren gegenüber dem EBM (SCH S. 7); mit Simultaneingriffen und Zuschlägen kippt es (SCH S. 8); implantatlastige Eingriffe sind in der Hybrid defizitär (BK S. 28–31; FR S. 37–38; BB-2024). Klinik: Wo die volle DRG erreichbar und begründbar ist, ist sie dem Hybrid-Fall vorzuziehen; klinisch indizierte Kontextprozeduren führen in die volle DRG (App: Hebel). Kostenaufteilung Chirurgie/Anästhesie 2026 nach AUF (GFFC 30.12.2025), Details dort.

## 7. Prüfung der App-Daten gegen die Rang-1-Quellen 2026 (13.09.2026)

**Positivliste.** `katalog2026.json` Flag 2: 883 Kodes, alle im amtlichen Leistungskatalog 2026 (0 falsche). 21 Kodes des Leistungskatalogs fehlen im Katalog vollständig, davon fußnah 5-79a.1r, 5-79a.1x, 5-79a.xr, 5-79a.xx, 5-79a.y (geschlossene Reposition Gelenkluxation mit Osteosynthese Zehen/sonstige; alle in I20-V68), ferner 16 Kodes 8-83c/8-83d/8-84d (Gefäßinterventionen). Betrifft die Master-Excel (1:1-Regel).

**Kontextprozeduren.** HDRG_REGELN `I20O_N.kontext` (95) gegen I20-V70 (88): deckungsgleich bis auf 5-808.b6 (Handbuch, OPS 2024) = 5-808.bh (App, OPS 2026) und sieben nur in der App: 5-810.4k, 5-810.9k, 5-811.3k, 5-811.4k, 5-812.3k, 5-812.9k, 5-819.4 (Arthroskopie-Ausschlüsse nach WE ASK OSG; nicht in V70, siehe V8). `I20M.kontext` (85) gegen I20-V66 (85): deckungsgleich bis auf b6/bh. Katalogflag 4 (98) gegen V66 ∪ V70 (88): zusätzlich geflaggt 5-796.xv, 5-854.0c, 5-854.xb, 5-854.xc (Gruppe D vom 09.09., „unklar, belassen") und die sieben Arthroskopiekodes; 5-854.0c und 5-854.xc stehen sogar in der Positivliste V68 und in V67. Empfehlung: Flag 4 bei 5-854.0c, 5-854.xc, 5-854.xb, 5-796.xv entfernen (nach DH keine Kontextprozeduren); Arthroskopiekodes nach V8 entscheiden.

**`_KX`.** {5-788.60, 5-854.1c, 5-854.2c} = V70 minus V66, exakt (DH). Die sechs Arthroskopiekodes in `_KX` stammen aus WE (V8).

**Beidseitig.** I20-V67 (82 Kodes) ist eine Teilmenge von V68; die App kennt keine Beidseits-Regel (A2).

**Pauschalen.** `_HDRG` 1007/2085/3280 = VG-2026 Tabelle S. 13–23 gerundet; Tabelle S. 1–12 nennt 1.018,50/2.120,68/3.341,18 (V9).

**Rahmenbedingungen.** `HDRG_RAHMEN` (5 Zeilen) deckt Alter, PCCL, VWD, Pflegegrad, Fallzusammenlegung; Beidseitigkeit und Diagnose-Ausschlüsse fehlen (A2, A3).

**Lapidus-Trigger.** Alle fünf in V68 und nicht in V66: belegt (V5 erledigt).

## 8. Lücken und Abweichungen der App

A1 **Reihenfolge Haupt-OP.** Die App wählt die Haupt-OP nach dem höchsten DRG-Gewicht und wertet nur deren Hybrid aus (`app.html` Z. 3253). Nach H-03/H-04 wäre zu prüfen: (1) Kode in I20A–C, oder in I20D bei I20N/I20O-Fällen, oder Kode einer fremden DRG mit besserer Rangzahl → keine Hybrid; (2) sonst irgendein Kode in V68 → Hybrid-Stufe nach H-05/H-06. Schritt 6, nach V1/V2.

A2 **Beidseitigkeit** fehlt. Vorschlag: Zeile „beidseitiger Eingriff → keine Hybrid-DRG (I20-V67)", sobald beide Seiten gewählt sind; Entscheidung des Autors zur Seitenauswahl.

A3 **Diagnose-Ausschlüsse** fehlen (DFS, Nerv als Hauptdiagnose, Zerebralparese, I20-V11). Bei `diabetischer_fuss` und `morton_neurom` ist die Diagnose bekannt; dort könnte die Hybrid-Spalte entfallen (bei Morton bereits `hdrg: null`).

A4 **Kontextfaktoren im Sprechstundenbrief** nur als Hinweiszeile (Entscheidung 09.09.2026, bleibt).

A5 **Unterschenkel-Kodes** (5-854.29, 5-852.29, 5-859.0x) wirken über H-03, nicht über Kontextlisten; nicht in V66/V70 eintragen.

A6 **Tendoskopie**: Entscheidung 3e am 13.09.2026: `ambStatus: "ebm"` ergänzen, `empf` bleibt `stat` (Grouper: allein oder mit Exostose I27E, ambulant EBM).

A7 erledigt (V5).

A8 **`neutral`-Listen** werden im Code nicht ausgewertet.

A9 **`kontextExcluded`** in `app.html` Z. 3502 ohne Daten.

A10 **Alte Blöcke** `ausschluss`/`aufwertung`/`kontext` in 8 OP-Einträgen als Fallback (Doppelpflege).

A11 **`ambStatus`-Reihenfolge** Z. 3355/3365/3371 zu prüfen.

A12 **Metallentfernung** entspricht der Aussage des Autors (EBM, Ziel Hybrid über Zusatzeingriff).

A13 **Tabellenbezeichnung** in `opsteuerung.json` `_kommentar` und `_KATALOG_META` („I20-V69 und I20-V61") ist die GFFC-Bezeichnung; im Handbuch heißen die Listen I20-V70 und I20-V66. Beim nächsten Datenupdate den Kommentar ergänzen („nach GFFC-Zählung; Handbuch 2024/2026: V70/V66").

A14 **Katalog unvollständig**: 21 Kodes des Leistungskatalogs 2026 fehlen (Abschnitt 7).

## 9. Offene Punkte zur Verifikation im Webgrouper

V1 **Verdrängung durch I27/I59-Kodes.** (a) erledigt 13.09.2026: HD Haglund-Exostose, 5-782.at + 5-852.29 → I27E, ambulant EBM (Webgrouper des Autors). Steuerungsregel des Autors daraus: stationär beim Haglund die Tendoskopie 5-852.29 immer mitkodieren und die Bursektomie beschreiben (I27E statt I20F); ambulant ökonomisch besser nur die Exostose abtragen (5-782.at allein) und I20O ansteuern. Gehört als Hinweis an `haglund_mini`/`haglund_as_split` und in die Auswertung (Schritt 6). (b) erledigt 13.09.2026: HD M20.2, 5-808.b0 + 5-852.29 → I20N, wie nach Rangregel erwartet. (c) erledigt 13.09.2026: HD M20.1, 5-808.a4 + 5-788.56 + 5-854.29 → I20D, keine Hybrid; meine Erwartung I20M war falsch: Die Rangregel entscheidet nur, dass der Fall in I20 bleibt; die Hybrid-Bedingung scheitert an einer Sperre, die nicht in Band 2 steht (V10). Für die Systematik: 5-854.29 holt bei allen drei Stufen aus der Hybrid (Grouper), Ziel stationär I20D beim Lapidus, bei I20N/I20O-Fällen nach Rangregel I27D. Entscheidung des Autors 13.09.2026 für die App: Der FHL-Transfer wird beim Lapidus NICHT als Ausweg geführt. Grundsatz: Die App zeigt als Ausweg nur Eingriffe, die gängigerweise mit dem Haupteingriff zusammen gemacht werden (beim Lapidus Spongiosaplastik 5-783.0v + 5-784.0v als Hebel, 2–4 DMMO 5-788.54/55 aus der Kontextliste). Theoretische Kodes, die den Fall herausholen würden, gibt es viele; einen davon zu führen und die anderen nicht, stiftet nur Verwirrung. Das Grouper-Ergebnis bleibt hier als Wissen dokumentiert, wird aber nicht in `HDRG_REGELN` oder in die Hebel übernommen. Ursprünglicher Text: (b) HD M20.2, OPS 5-808.b0 + 5-852.29: erwartet I20N; (c) HD M20.1, OPS 5-808.a4 + 5-788.56 + 5-854.29: erwartet nach H-03 I20M, nach Autor „raus". Ergebnis hier eintragen; danach A1 bauen.

V2 **Grenze der Verdrängung.** Autor: „über I20C oder CM 1,111". DH: I20D verdrängt I20N/I20O, nicht I20M; fremde DRGs nach Rangzahl (durch V1a und V1b bestätigt). Zusätzlich gibt es die Sperre aus V10, die auch innerhalb von I20 wirkt. Bestätigung des Autors zur Formulierung.

V3 erledigt: I20-V9/V10/V11 liegen vor (Abschnitt 4, H-02). Offen bleibt nur „Ausschluss Kontextfaktoren MDC 08" (Band 4).

V4 **PIP beim Hallux valgus:** MU S. 22 gegen S. 23; Lesart 1× I20O, 2–4× I20N; HDRG_REGELN entspricht. Bestätigen.

V5 erledigt (Lapidus-Trigger belegt).

V6 **Hohmann beim Hallux valgus:** MU S. 22 „> 1× keine Hybrid"; 5-788.58 (2 Osteotomien D II–V) steht in V16, nicht in V70; nach DH also keine Kontextprozedur, aber möglicherweise Aufwertung nach I20N über V16. HDRG_REGELN führt 5-788.58 als neutral. Webgrouper: HD M20.1, 5-788.5e + 5-788.58.

V7 erledigt: I20-V67 liegt vor (82 Kodes). Offen: DH-Konvention „beids. Pr" (Seitenkennzeichen B oder derselbe Kode mit R und L) — Band 1 Konventionen prüfen.

V8 **Arthroskopie-Ausschlüsse** 5-810.4k, 5-810.9k, 5-811.3k, 5-811.4k, 5-812.3k, 5-812.9k, 5-819.4: nach WE „keine Hybrid", nach DH nicht in V70/V66. Mechanismus belegt: Diese Kodes stehen in den I59-Tabellen (DH Band 2, PDF S. 1348–1349, I59-V2/V3/V5 bis V10), steuern also I59Z (Rang 130) an, das I20O/I20F (135/136) verdrängt, I20N/I20E aber nicht. Für die App heißt das: Ausweg nur bei I20O-Fällen (ASK OSG), Ziel I59Z statt I20F; bei I20N-Fällen wirkungslos. Webgrouper zur Bestätigung: HD M24.87, 5-812.kk + 5-810.4k (erwartet I59Z). Bis zur Klärung bleiben sie in HDRG_REGELN und im Katalog wie am 09.09. freigegeben, aber mit Quelle „GFFC" markiert.

V10 **„Ausschluss Kontextfaktoren MDC 08"** (Definitionshandbuch Band 4, S. 5525) liegt nicht vor. Nach V1c enthält sie mindestens 5-854.29 oder eine Regel, die den FHL-Transfer sperrt. Band 4 besorgen (g-drg.de, Definitionshandbuch 2024/2026), Tabelle extrahieren, in H-02 aufnehmen und gegen HDRG_REGELN prüfen; 5-854.29 wird nach Entscheidung des Autors nicht als Ausweg in der App geführt (siehe V1c).

V9 erledigt 13.09.2026: Entscheidung des Autors, weiter die gerundeten Werte der zweiten Tabelle (S. 13–23: I20M 3.280,38, I20N 2.085,14, I20O 1.006,54; App 3280/2085/1007) zu verwenden. Keine Änderung an `erloes2026.json`. Die erste Tabelle (S. 1–12) bleibt als Hinweis in Abschnitt 0 stehen.

## 10. Vorschlag: So werden die Regeln sicher erfasst

Grundsatz: drei Ebenen, jede mit Quelle, Jahr und Prüfweg; keine Ebene ohne die andere änderbar; Jahreswechsel als eigener Vorgang.

**Ebene 1, dieses Dokument.** Regeln H-01 bis H-09 mit Quelle, Jahr und Status (belegt / per Webgrouper geprüft / offen). Änderung nur mit Rang-1-Quelle des laufenden Jahres oder Webgrouper-Nachweis und Freigabe des Autors; als datierter Nachtrag, nie stillschweigend.

**Ebene 2, die Daten (`opsteuerung.json`, `katalog2026.json`, `erloes2026.json`).** `HDRG_REGELN` bleibt die Kodequelle, künftig mit Feld `quelle` je Kode („DH 2026 I20-V70" oder „GFFC WE 04.03.2026") und Kommentar zur Tabellenbezeichnung (A13). Neu, ohne bestehende Felder zu ändern: `HDRG_FALLREGELN` (H-02: Alter, PCCL, VWD, Pflegegrad, beidseitig mit Liste V67, Diagnosen V11, DFS, Nerv), `HDRG_VERDRAENGUNG` (H-03: Rangzahlen der DRGs aus DH S. 409/411, nach V1/V2 bestätigt). Katalog: Positivliste aus LK-2026 nachziehen (21 Kodes), Flag 4 nach V66/V70 bereinigen.

**Ebene 3, die Prüfung.** (a) Querprüfungsskript: HDRG_REGELN gegen V66/V70, Katalogflag 2 gegen LK-2026, Flag 4 gegen V66 ∪ V70, `_KX` gegen V70 minus V66, `_HDRG` gegen VG-2026, `hdrgTrigger` gegen V68 minus V66; jede Abweichung als Zeile. Die Tabellen dafür liegen jetzt maschinenlesbar vor (`dh2026_tabellen.json`, `leistungskatalog2026.json`, in der Sitzung erzeugt, ins Repo nach Freigabe). (b) Sollwert-Tabelle `hybrid_testfaelle.json` aus Abschnitt 5, auf dem Prüfstand gegen die Fallsteuerung. (c) `webgrouper-nachweise.md` mit Datum, HD, ND, OPS, Alter, VWD, Ergebnis je Lauf.

**Jahreswechsel (Backlog C3).** Neues Definitionshandbuch besorgen (Band 2 und Band 4 für „Ausschluss Kontextfaktoren MDC 08"), Tabellen neu extrahieren, Nummern und OPS-Fassung prüfen, Leistungskatalog und Vergütung nachziehen, Testfälle laufen lassen, Jahresübersicht (Abschnitt 0) fortschreiben.

Was dieses Dokument nicht ist: keine Rechtsquelle und kein Ersatz für den Webgrouper. Es sagt, was wir wissen, aus welchem Jahr und woher, und was wir noch nicht wissen.
