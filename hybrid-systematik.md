# Hybrid-DRG-Systematik Fußchirurgie: Referenzdokument

Stand: 13.09.2026 abends, zweite Fassung mit Nachträgen V1a–c, V9 (nach Auswertung des Ordners `GitHub/Hybrid` und der Nachlieferungen). Nachtrag 14.09.2026: Band 4 des Definitionshandbuchs (Version 2026) ausgewertet; V3 und V10 erledigt, H-02 um die Fallsperre „Ausschluss Kontextfaktoren MDC 08" ergänzt, Anhang B neu (Quelle DH4). Vom Autor am 13.09.2026 als Bezugspunkt freigegeben; Ablage im Repo-Root und im Projekt. Änderungen nur als datierter Nachtrag. Zweck: eine Stelle, an der die Systematik der Hybrid-DRG (Zuordnung, Ausschluss, Kodierung, Erlös) mit Quelle und Gültigkeitsjahr festgehalten ist, damit jede Änderung an `opsteuerung.json`, `katalog2026.json`, `erloes2026.json` oder an der Fallsteuerung in `app.html` gegen dieses Dokument geprüft werden kann. Grundregel des Autors: **Es zählen immer die Regeln des laufenden Jahres, derzeit 2026.** Ältere Aussagen stehen hier nur, damit erkennbar ist, was sich geändert hat. Nichts in diesem Dokument ist neu erfunden; jede Aussage trägt Quelle und Jahr. Wo Quellen sich widersprechen oder die App etwas anders macht, steht das in Abschnitt 8 und 9.

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
| Diagnosen | – | – | Die Fuß-Hybrid-DRGs I20M/N/O setzen voraus: keine Hauptdiagnose aus I20-V9 (Frakturen obere Extremität), I20-V10 (Frakturen Unterschenkel/Knöchel), I20-V11 (M96.0 Pseudarthrose nach Arthrodese, S82.5/.6/.81/.82 Knöchelfrakturen) (DH S. 1042, 1057–1058). Das ist kein Hybrid-Ausschluss im Ganzen: Ein Fall mit Knöchelfraktur als Hauptdiagnose gehört zur Fraktur-Hybrid I13M/I13N (Positivliste MU S. 15), nicht zur Fuß-Hybrid (Hinweis des Autors 13.09.2026) |
| Fallsperre „Ausschluss Kontextfaktoren MDC 08" (AKF08) | – | – | Zusätzliche Bedingung aller Fuß-Hybrid-DRGs: „Nicht [Ausschluss Kontextfaktoren MDC 08]" (DH S. 1042). Die Funktion steht in Band 4 (DH4 S. 5685–5779) und sperrt die Hybrid, sobald irgendeine kodierte Prozedur in AKF08-V6 (5.774 Kodes, außer den 141 Ausnahmen V7), V13 (4.746) oder V16 (44) steht, eine Diagnose (Haupt- oder Nebendiagnose) in AKF08-V1 (1.433, außer V2), V3 (525 bösartige Neubildungen), V4 (5) oder V5 (16) steht, eine Frakturkombination aus V8–V12 vorliegt oder Beatmung > 0 Stunden. Nachtrag 14.09.2026, Einzelheiten H-02 und Anhang B |
| OPS-Fassung | OPS 2024 | OPS 2025: 5-808.b2–b5 aufgeteilt in 5-808.b9–bc (MTP II–V) und 5-808.bd–bg (IP II–V), 5-808.b6 in 5-808.bh (OPS-2026-Liste GFFC) | Das Handbuch 2024/2026 führt die Tabellen in OPS-Fassung 2024 (5-808.b2–b5 statt b9–bg); der Leistungskatalog 2026 in OPS 2026. Beim Vergleich ist zu übersetzen |
| Zuzahlung Implantate | – | – | GFFC-Vortrag 28.11.2025 (ZZ-2025), nicht ausgewertet, betrifft Abrechnung, nicht Zuordnung |

## 1. Quellen und ihr Rang

| Kürzel | Quelle | Jahr | Rang |
|---|---|---|---|
| DH | aG-DRG-Version 2024/2026 Definitionshandbuch Band 2 (InEK, 1.406 S.), `GitHub/Hybrid/GFFC 2025 Abrechnung/DefHandbuch_aGDRG_2024_2026_Band2.pdf`. Definitionen DRG I20M S. 1042–1045 (PDF 1054–1057), I20N S. 1046–1053, I20O S. 1054; Tabellen I20-V1 bis V70 S. 1055–1081 (PDF 1067–1093); Struktur MDC 08 S. 409, 411 (PDF 421, 423). Seitenangaben unten sind Handbuchseiten | 2026 | 1, verbindlich für die Zuordnung |
| DH4 | aG-DRG-Version 2026 Definitionshandbuch Band 4 (InEK, 6.302 PDF-Seiten), `GitHub/Hybrid/DefHandbuch_aGDRG_2026_Band4_260205.pdf`. Funktion „Ausschluss Kontextfaktoren MDC 08" (AKF08): Struktur S. 5685, Definitionen S. 5687, Tabellen AKF08-V1 bis V16 S. 5687–5779 (PDF 5697–5791). Achtung Versionsunterschied: Band 2 liegt als Version „2024/2026" vor (Migrationshandbuch, OPS-Fassung 2024; dort verweist das Inhaltsverzeichnis für AKF08 auf S. 5525), Band 4 als Version „2026" (S. 5685). Beide sind vom InEK, aber nicht dieselbe Ausgabe; Band 2 der Version 2026 fehlt noch (siehe V11) | 2026 | 1, verbindlich |
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

**Kontextfaktoren.** Ausschlussbedingungen auf Fallebene in den Definitionstabellen (DH S. 1042): Alter > 17, PCCL < 3, VWD < 3 Tage und Tagesdifferenz ≤ 2, kein hoher Pflegegrad (I20-V69), nicht beidseitig (I20-V67), keine Hauptdiagnose aus I20-V9/V10/V11, „Nicht [Ausschluss Kontextfaktoren MDC 08]" (Funktion AKF08 in Band 4, DH4 S. 5685–5779, seit 14.09.2026 ausgewertet, siehe H-02 und Anhang B). GFFC-Zusammenfassung MU S. 9 und 29.

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

**H-02 Kontextfaktoren auf Fallebene (Ausschluss).** Nach DH S. 1042 (Definition I20M, gleichlautend I20N/I20O): Alter > 17 Jahre; PCCL < 3; VWD < 3 Tage und Tagesdifferenz Aufnahme–Entlassung ≤ 2; kein Pflegegrad 4 oder 5 (I20-V69, DH S. 1081); nicht beidseitig (I20-V67, 82 Kodes der Positivliste, DH S. 1079); keine Hauptdiagnose aus I20-V9 (Frakturen Klavikula, Humerus, Unterarm, Hand), I20-V10 (Frakturen Unterschenkel, Knöchel, Patella), I20-V11 (M96.0 Pseudarthrose nach Fusion/Arthrodese, S82.5, S82.6, S82.81, S82.82) (DH S. 1057–1058) — diese Bedingung grenzt nur die Fuß-Hybrid ab: Frakturfälle laufen in die Fraktur-Hybrids I13M/I13N (distale Fibula/Tibia), I31M/N, I21M/I29M (MU S. 14–15, 25–28), die Knöchelfraktur schließt Hybrid also nicht aus, sondern wechselt die Familie (Autor 13.09.2026); „Nicht [Ausschluss Kontextfaktoren MDC 08]": Nachtrag 14.09.2026, Funktion AKF08 aus Band 4 (DH4 S. 5687). Sie ist erfüllt, und die Hybrid damit gesperrt, wenn mindestens eine dieser Zeilen zutrifft: (1) eine Prozedur aus AKF08-V6 „Kontextfaktoren allgemein Prozeduren 1" (5.774 Kodes), sofern sie nicht in AKF08-V7 „MDC 08 Prozeduren 1 (Ausschluss)" steht (141 Ausnahmen, darunter 5-854.xc und die Frakturkodes 5-793/5-794 an Radius, Ulna, Tibia distal und Fibula distal); (2) Prozeduren aus mindestens zwei der Tabellen V8–V12 (Frakturkombinationen Klavikula, Radius, Ulna, Tibia distal); (3) eine Prozedur aus AKF08-V13 „allgemein Prozeduren 2" (4.746 Kodes); (4) eine Diagnose aus AKF08-V1 „allgemein Diagnosen 1" (1.433 Kodes: Sepsis, Infektionen, Osteomyelitis M86.0x/M86.1x, eitrige Arthritis M00.x, Erysipel A46, Dekubitus Grad 4 L89.3x, arterielle Embolie I74.x, Diabetes mit Koma/Ketoazidose u. a.), sofern nicht in AKF08-V2 (4 Ausnahmen, darunter L03.11 Phlegmone untere Extremität); (5) eine Prozedur aus V14 zusammen mit einer aus V15 (intrakranielle Thrombektomie, nicht fußrelevant); (6) eine Diagnose aus AKF08-V3 „allgemein Diagnosen 2 (BNB)" (525 bösartige Neubildungen C00–C97); (7) eine Diagnose aus AKF08-V4 „MDC 08 Diagnosen" (S41.86, S41.89, S51.89, S81.86, S81.89: Weichteilschaden III bei offener Wunde); (8) eine Diagnose aus AKF08-V5 (16 Kodes, angeborene Herzfehler, Z99.4); (9) eine Prozedur aus AKF08-V16 „allgemein Prozeduren 3" (44 Kodes Knorpeltransplantation/Chondrozytentransplantation 5-801.a/b/c/k und 5-812.9/a/h, offen und arthroskopisch, auch Sprunggelenk, Tarsalgelenk, MTP, Zehen); (10) Beatmung > 0 Stunden. „Diagnose" meint hier Haupt- oder Nebendiagnose (Konvention „Dg" des Handbuchs), „Prozedur" jede kodierte Prozedur. Für den Fuß wichtig: V6 enthält Sehnenrekonstruktionen am Unterschenkel (5-854.29 Transposition, 5-854.39, 5-854.49 Ersatzplastik = FHL-Transfer, 5-854.89), Ersatzplastik/Transplantation/Transplantatwechsel von Sehnen am Fuß (5-854.4b–8c), fast alle Knochentransplantationen 5-784.* (Spongiosa Tibia 5-784.0n, Fibula 5-784.0r, Talus 5-784.0s, Tarsale 5-784.0u, Kalkaneus 5-784.1t/7t, Metatarsale 5-784.3v/cv/xv, Phalangen 5-784.0w/cw/xw; nicht aber 5-784.0v und 5-784.1v, die nur über I20-V70 wirken), die MT-I-Doppelosteotomie beim Rezidiv 5-788.5h, den OSG-Prothesenwechsel 5-827.10, die offene Synovektomie Fußwurzel 5-856.4a und die Frakturkodes 5-796.* mit Fixateur/Nagel; V13 enthält 5-829.k2 und Knorpelkodes 5-801.k*/5-812.h*. Vollständige Liste der in der App verwendeten Kodes in Anhang B. Das erklärt Grouper-Lauf V1c (Lapidus + Akin + FHL-Transfer 5-854.29 → I20D ohne Hybrid). Die Tabellen liegen maschinenlesbar vor (`akf08_tabellen.json`, `akf08_sperrlisten_2026.json`, Ebene 3). Die Angabe MU S. 9 „Fallzusammenlegung aus zwei Aufenthalten" ist ein anderer Punkt und keine Wiedergabe dieser Funktion. Zerebralparese G80.x (I20-V2, DH S. 1055) steht ganz oben im I20-Baum und führt nach I20A/B (Struktur S. 411), also nie zur Hybrid-Abfrage. Sonstige Nennungen MU S. 29 (mehrere Lokalisationen, Mehrfachfrakturen, Weichteilschaden III, Knochenersatz, Transplantationen, Pseudarthrose, DRG-spezifische Ausnahmen) sind teils Kontextprozeduren (H-05), teils Diagnosen (I20-V3/V5/V7), keine eigene Fallregel.

**H-03 Höher eingestufte DRG schlägt Hybrid (Verdrängung).** Der Baum prüft die DRG-Zweige von komplex nach einfach; die Hybrid-Abfrage liegt erst unmittelbar vor I20D, I20E und I20F (DH Struktur S. 411). Ein Kode oder eine Kombination, die in I20A–I20C oder bei I20N/I20O-Fällen in I20D führt, verhindert damit die Hybrid-DRG (SCH S. 5: „Prozedur oder Kombination, welche eine höher bewertete DRG als I20F oder I20E auslöst"). Für Kodes anderer Basis-DRGs (Unterschenkel, Weichteile) entscheidet die Zuteilungsfunktion „LG_allgemein" mit Rangzahl je DRG (DH Struktur S. 409, 411): I20M 102, I20D 103, I27D 114, I20N 119, I20E 120, I27E 129, I20O 135, I20F 136 (kleinere Zahl gewinnt; I59Z nach automatischem Auszug 130, Seite nicht einzeln geprüft). Folgen, sofern der Webgrouper sie bestätigt (V1, V2): Ein I27E-Kode (Tendoskopie 5-852.29, Bursektomie Unterschenkel 5-859.19) schlägt I20O/I20F, aber nicht I20N/I20E und nicht I20M/I20D. Ein I27D-Kode (FHL-Transfer 5-854.29) schlägt I20N und I20O; bei I20M bleibt der Fall zwar in I20D (Rang 103 vor 114), verliert die Hybrid aber trotzdem (Webgrouper 13.09.2026: I20D), also über eine zweite Sperre: 5-854.29 steht in AKF08-V6 (Band 4), siehe H-02 und V10 (erledigt 14.09.2026). Das deckt sich mit SCH S. 24 (Haglund + Bursektomie Unterschenkel > 15 J.: I27E, EBM) und SCH S. 23 (< 16 J.: I20E, dann I20N), und mit BB-2025 („gilt auch für Eingriffe aus I27E, I59Z") nur für die Stufen I20N/I20M. Aussage des Autors 13.09.2026 „Tendoskopie mit Haglund ist I20O" und „alles über I20C oder CM 1,111 sicher raus": nach DH liegt die Grenze bei der Rangzahl, nicht beim Gewicht; I20D verdrängt I20N/I20O, nicht I20M.

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
| FHL-Transfer 5-854.29 + Lapidus 5-808.a4 + Akin 5-788.56, HD M20.1 | I20D, keine Hybrid: der Fall bleibt in I20 (Rang I20D 103 < I27D 114), die Hybrid-Bedingung scheitert aber; 5-854.29 steht in keiner I20-Tabelle von Band 2, aber in AKF08-V6 „Kontextfaktoren allgemein Prozeduren 1" (Band 4, DH4, bestätigt 14.09.2026; V10 erledigt). Aussage des Autors „FHL holt raus" bestätigt | WG 13.09.2026 |

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

A2 **Beidseitigkeit**: Entscheidung des Autors 13.09.2026, bauen. Vorgabe: dritte Seitenwahl „beidseits" im Sprechstundenbrief und OP-Bericht; Fallsteuerung zeigt „beidseitiger Eingriff → keine Hybrid-DRG (I20-V67)", Setting stationär volle DRG oder ambulant EBM. Textregel für den OP-Bericht: bei beidseits wird das beidseitige Abwaschen in den Vorbereitungsbausteinen beschrieben, die Eingriffe stehen ohne Seitenangabe, die Seite muss je Eingriff im Text ergänzt werden; das prüft der Prüfdurchlauf der Briefprüfung (Konzept `konzept-briefpruefung.md`, Modulregel „Seite") vor Herausgabe des finalen Textes. Umsetzung: Schritt 6 (Auswertung) und Briefprüfung Teil B. Nachtrag 14.09.2026: Vorgabe des Autors „beidseits keine Hybrid, nur EBM, nur bei Hybrid-Fällen"; Prüfung gegen DH S. 1042/1079 ergab, dass I20-V67 nur 82 der 161 Positivkodes umfasst (alle Vorfuß-Knochenkodes, OSG-Arthroskopie 5-811.2k/5-812.ek/fk/kk, Arthrorise 5-809.1m, Sehnenkodes 5-852.xa/5-854.0c/xc), nicht aber 5-782.at/au (Calcaneoplastie), 5-851.1a/2a/xa, 5-855.1a, 5-859.1a, 5-819.0k, 5-780.x, 5-800.x. Entscheidung des Autors 14.09.2026: Variante (b), handbuchgenau: beidseits sperrt nur, wenn ein Fallkode in I20-V67 steht; Liste als `HDRG_FALLREGELN.beidseits` in `opsteuerung.json` (3i, geschrieben 14.09.2026, mit Übertragung 5-808.b2–b5 → b9–bg als `ergaenzungOps2026`, vom Autor freigegeben), Ausnahme-Feld `beidseitsHybridBleibt` bei `haglund_mini`; Code-Auftrag `auftrag-beidseits-hybrid.md` (Repo-Root). Webgrouper-Absicherung 14.09.2026 durch den Autor bestätigt (V12): 5-782.at B → I20O bleibt, 5-788.5c B → I20F. Umgesetzt in `app.html` (Commit 81f6f95, Gegenprobe Prüfstand-Bericht Abschnitt 11). UC-Modul (Nachtrag 14.09.2026 abends): I20-V67 gilt nur für I20M/N/O; jede andere Hybrid-Familie trägt im Band 2 eine eigene Bedingung „Nicht [beids. Pr Hybrid MDC 08 – n (…)]" (I13M/N PDF S. 927–930, I21M S. 1095, I29M S. 1214, I31M/N S. 1224–1226). Entscheidung des Autors: pauschale UC-Sperre behalten, Quelle im Code korrigieren (`auftrag-beidseits-folge.md`), Tabellen je Familie als Datenschritt 3j extrahieren und abnehmen.

A3 **Diagnose-Ausschlüsse** (DFS, Nerv als Hauptdiagnose, Zerebralparese, M96.0): bei `diabetischer_fuss` und `morton_neurom` bereits stumm richtig (`hdrg: null`). Knöchelfrakturen gehören nicht hierher (Fraktur-Hybrid, siehe H-02). Hinweiszeile in der Fallsteuerung „Hauptdiagnose schließt die Fuß-Hybrid aus" bei `diabetischer_fuss` und `morton_neurom`: Entscheidung des Autors 13.09.2026, ja, bauen (Schritt 6).

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

A14 erledigt 13.09.2026 (Schritt 3h): Master-Excel fortgeschrieben, `scripts/build_katalog2026.py` erzeugt die JSON; Hybrid-Flag = Leistungskatalog 2026 (904/904); Flag 4 bei 5-854.0c/xc/xb und 5-796.xv entfernt. Korrektur: 5-788.57/58 stehen in keiner der drei Listen und gehören nicht in den Katalog.

A15 **Datenkorrekturen 14.09.2026 (3i, vom Autor entschieden).** (1) `fasziotomie_offen` führte den Kode 5-841.10, laut Katalog „Operationen an Bändern der Hand: Durchtrennung: Radiokarpalband", mit `hdrg: I20O`. Entscheidung des Autors: 5-851.5a (Fasziotomie quer, offen chirurgisch, partiell, Fuß). Der Kode ist AOP (Katalogflag 1), steht nicht im Leistungskatalog 2026 und nicht in I20-V68: `hdrg` jetzt null, `ambStatus: ebm`; die offene plantare Fasziotomie ist damit in der App kein Hybrid-Eingriff. Stationäres Ziel I59Z ohne dokumentierte Herkunft belassen; nach DH-Struktur steht 5-851.5a in I20-V18 (ADRG I20), was auf I20F deutet — Grouper-Lauf offen (HD M72.2 + 5-851.5a). (2) `haglund_mini` (Calcaneoplastie) hatte keinen Ausweg; Entscheidung des Autors: Bursektomie am Unterschenkel 5-859.19 als Hebel, Ziel I27E (5-859.19 steht wie 5-852.29 in I27-V4/V8/V17/V18, DH PDF S. 1150ff; Grouper-Lauf für 5-859.19 am 14.09.2026 bestätigt, für 5-852.29 belegt 13.09.2026). Die Bursektomie am Fuß 5-859.1a wäre dagegen Positivkode (I20-V68) und ließe den Fall in I20O; `app.html` nennt im Kodier-String der Calcaneoplastie noch „.1a" (Z. 5046), in der Kodeliste „.19" (Z. 4832) — Angleichung in Schritt 6 auf .19.

## 9. Offene Punkte zur Verifikation im Webgrouper

V1 **Verdrängung durch I27/I59-Kodes.** (a) erledigt 13.09.2026: HD Haglund-Exostose, 5-782.at + 5-852.29 → I27E, ambulant EBM (Webgrouper des Autors). Steuerungsregel des Autors daraus: stationär beim Haglund die Tendoskopie 5-852.29 immer mitkodieren und die Bursektomie beschreiben (I27E statt I20F); ambulant ökonomisch besser nur die Exostose abtragen (5-782.at allein) und I20O ansteuern. Gehört als Hinweis an `haglund_mini`/`haglund_as_split` und in die Auswertung (Schritt 6). (b) erledigt 13.09.2026: HD M20.2, 5-808.b0 + 5-852.29 → I20N, wie nach Rangregel erwartet. (c) erledigt 13.09.2026: HD M20.1, 5-808.a4 + 5-788.56 + 5-854.29 → I20D, keine Hybrid; meine Erwartung I20M war falsch: Die Rangregel entscheidet nur, dass der Fall in I20 bleibt; die Hybrid-Bedingung scheitert an einer Sperre, die nicht in Band 2 steht (V10). Für die Systematik: 5-854.29 holt bei allen drei Stufen aus der Hybrid (Grouper), Ziel stationär I20D beim Lapidus, bei I20N/I20O-Fällen nach Rangregel I27D. Entscheidung des Autors 13.09.2026 für die App: Der FHL-Transfer wird beim Lapidus NICHT als Ausweg geführt. Grundsatz: Die App zeigt als Ausweg nur Eingriffe, die gängigerweise mit dem Haupteingriff zusammen gemacht werden (beim Lapidus Spongiosaplastik 5-783.0v + 5-784.0v als Hebel, 2–4 DMMO 5-788.54/55 aus der Kontextliste). Theoretische Kodes, die den Fall herausholen würden, gibt es viele; einen davon zu führen und die anderen nicht, stiftet nur Verwirrung. Das Grouper-Ergebnis bleibt hier als Wissen dokumentiert, wird aber nicht in `HDRG_REGELN` oder in die Hebel übernommen. Ursprünglicher Text: (b) HD M20.2, OPS 5-808.b0 + 5-852.29: erwartet I20N; (c) HD M20.1, OPS 5-808.a4 + 5-788.56 + 5-854.29: erwartet nach H-03 I20M, nach Autor „raus". Ergebnis hier eintragen; danach A1 bauen.

V2 erledigt 13.09.2026, vom Autor bestätigt („Regel so"): **Verdrängungsregel in zwei Stufen.** Stufe 1, Basis-DRG: Unter allen kodierten Eingriffen gewinnt der mit der besten Rangzahl der Zuteilungsfunktion (DH Struktur S. 409, 411): I20M 102, I20D 103, I27D 114, I20N 119, I20E 120, I27E 129, I59Z 130 (automatisch gezogen), I20O 135, I20F 136; kleinere Zahl gewinnt. Stufe 2, Hybrid: nur wenn die Basis-DRG I20D, I20E oder I20F ist, mindestens ein Kode in I20-V68 steht, kein Kode in I20-V66 (I20M) bzw. I20-V70 (I20N/I20O) steht und keine Fallsperre greift (H-02 sowie die Tabelle aus Band 4, V10). Für die Code-Sitzung (Schritt 6): nur geprüfte Rangzahlen verwenden (I20-Familie und I27D/I27E belegt, I59Z bis zur Einzelprüfung nur als Hinweis); jede neue Kombination bekommt vor dem Einbau einen Grouper-Sollwert in `hybrid_testfaelle.json`.

V3 erledigt: I20-V9/V10/V11 liegen vor (Abschnitt 4, H-02); „Ausschluss Kontextfaktoren MDC 08" seit 14.09.2026 ebenfalls (Band 4, V10).

V4 erledigt 13.09.2026 (Webgrouper des Autors): HD M20.1, 5-788.5e + 5-808.be (2× PIP-Arthrodese) → I20N. Aufwertung 5-808.be/bf/bg in HDRG_REGELN bestätigt.

V5 erledigt (Lapidus-Trigger belegt).

V6 erledigt 13.09.2026 (Webgrouper des Autors): HD M20.1, 5-788.5e + 5-788.58 (2 Osteotomien D II–V) → I20O. 5-788.58 ist neutral, wie in HDRG_REGELN; die Folie MU S. 22 („> 1× Hohmann keine Hybrid") gilt für 2026 nicht in dieser Lesart. 5-788.58 fehlt in `katalog2026.json` ganz (A14).

V7 erledigt: I20-V67 liegt vor (82 Kodes). Offen: DH-Konvention „beids. Pr" (Seitenkennzeichen B oder derselbe Kode mit R und L) — Band 1 Konventionen prüfen.

V8 erledigt 13.09.2026 (Webgrouper des Autors): HD M24.87, 5-812.kk + 5-810.4k (Entfernung freier Gelenkkörper OSG) → I59Z. Mechanismus belegt: Die sieben Kodes 5-810.4k, 5-810.9k, 5-811.3k, 5-811.4k, 5-812.3k, 5-812.9k, 5-819.4 stehen in den I59-Tabellen des Handbuchs (Band 2, PDF S. 1348–1349), steuern I59Z (Rang 130) an und verdrängen damit I20O/I20F, nicht I20N/I20E. Steuerungsregel des Autors: Bei stationärer Arthroskopie des OSG die Entfernung des freien Gelenkkörpers 5-810.4k immer mitkodieren, damit der Fall aus der Hybrid nach I59Z geht (3.225 € statt I20O 1.007 €); ambulant nur die Positivkodes, dann I20O. Folge für die App (Datenänderung, Freigabe nötig): In `HDRG_REGELN.I20O_N.kontext` tragen die sieben Kodes heute `drg: {I20O: I20F}`; richtig ist Ziel I59Z. Dazu Hinweis am Eintrag `ask_osg`, analog zum Haglund-Hinweis (V1a).

V10 erledigt 14.09.2026: **„Ausschluss Kontextfaktoren MDC 08"** liegt vor (Band 4, Version 2026, vom Autor in `GitHub/Hybrid/` gelegt; DH4 S. 5685–5779). Ergebnis: Es ist keine einzelne Tabelle, sondern eine Funktion (AKF08) mit zehn Bedingungen und 16 Tabellen, Wortlaut in H-02, Struktur und App-Abgleich in Anhang B. 5-854.29 steht in AKF08-V6; damit ist V1c erklärt. Prüfung gegen `HDRG_REGELN` (Stand nach Deploy 13.09.2026): keiner der Kodes in `neutral`, `aufwertung`, `positiv`, `hdrg` oder `nichtKontext` (I20O_N, I20M) steht in einer AKF08-Prozedurenliste; kein Kode der Positivliste I20-V68 und kein Fuß-Kode des Leistungskatalogs 2026 steht darin (nur 5-546.20–22 Bauchwandrekonstruktion aus der Hernien-Hybrid, nicht fußrelevant); von den 94 Kontextkodes des Katalogs (Flag 4) stehen 23 zugleich in AKF08-V6 (5-784.0w/3v/cv/cw/xv/xw, 5-796.ev/gv/gw/mv/nv/nw/pv, 5-854.4b–8c), die übrigen 71 nur in I20-V66/V70. Es gibt also keinen Widerspruch zwischen App-Daten und Band 4; die Fallsperre kommt als zusätzliche Ebene hinzu. Von den 269 in `opsteuerung.json`, `opmethoden.json` und `app.html` verwendeten OPS-Kodes stehen 40 in AKF08 (Anhang B); die 17 davon, die keine Kontextprozedur nach I20-V70 sind, führt die App nur in stationären Pfaden (Hebel I27D/I13D, Coalitio, TEP-Wechsel, FHL-Transfer „nur stationär"), also ohne Hybrid-Anspruch. Diagnosen: Von den in App und Daten genannten ICD-Kodes stehen nur A41.x (Sepsis), R57.2 und E15 in AKF08-V1, alle im DFS-Kontext ohne Hybrid-Bezug. 5-854.29 wird nach Entscheidung des Autors weiterhin nicht als Ausweg in der App geführt (V1c). Vorschlag für die Umsetzung: siehe Abschnitt 10, Ebene 2 (`HDRG_FALLREGELN.akf08`) und Ebene 3.

V9 erledigt 13.09.2026: Entscheidung des Autors, weiter die gerundeten Werte der zweiten Tabelle (S. 13–23: I20M 3.280,38, I20N 2.085,14, I20O 1.006,54; App 3280/2085/1007) zu verwenden. Keine Änderung an `erloes2026.json`. Die erste Tabelle (S. 1–12) bleibt als Hinweis in Abschnitt 0 stehen.

V12 **Beidseits und Bursektomie im Webgrouper**: vom Autor am 14.09.2026 bestätigt („Grouper-Durchläufe bestätigt"): (a) 5-782.at Seitenkennzeichen B, HD M76.6 → I20O bleibt (Beidseits-Regel Variante b belegt: kein V67-Kode, keine Sperre); (b) 5-788.5c B, HD M20.1 → I20F, keine Hybrid (V67-Sperre belegt); (c) 5-782.at + 5-859.19, HD M76.6 → I27E (Ausweg der Calcaneoplastie belegt). (d) 5-851.5a, HD M72.2: Lauf erfolgt, Ergebnis (I20F oder I59Z) noch nicht einzeln genannt — nachtragen, dann `fasziotomie_offen.drg` prüfen.

V11 **Band 2 der Version 2026 fehlt.** Der vorliegende Band 2 ist die Ausgabe „2024/2026" (Migrationshandbuch, OPS-Fassung 2024), Band 4 die Ausgabe „2026". Die I20-Tabellen (V66, V67, V68, V70) sollten aus dem Band 2 der Version 2026 gegengelesen werden, weil die Positivliste 2026 in OPS-Fassung 2026 mehr Kodes führt (Leistungskatalog 904 gesamt, Fuß 167 nach GFFC) als die 161 der Ausgabe 2024/2026. Bis dahin gilt: Positivliste = amtlicher Leistungskatalog 2026 (LK-2026, Rang 1), Kontextlisten = I20-V66/V70 der Ausgabe 2024/2026 plus GFFC-Abgleich (A13). Kein Handlungsbedarf in den Daten, nur Beschaffung (InEK, g-drg.de, Definitionshandbuch aG-DRG-Version 2026 Band 2).

## 10. Vorschlag: So werden die Regeln sicher erfasst

Grundsatz: drei Ebenen, jede mit Quelle, Jahr und Prüfweg; keine Ebene ohne die andere änderbar; Jahreswechsel als eigener Vorgang.

**Ebene 1, dieses Dokument.** Regeln H-01 bis H-09 mit Quelle, Jahr und Status (belegt / per Webgrouper geprüft / offen). Änderung nur mit Rang-1-Quelle des laufenden Jahres oder Webgrouper-Nachweis und Freigabe des Autors; als datierter Nachtrag, nie stillschweigend.

**Ebene 2, die Daten (`opsteuerung.json`, `katalog2026.json`, `erloes2026.json`).** `HDRG_REGELN` bleibt die Kodequelle, künftig mit Feld `quelle` je Kode („DH 2026 I20-V70" oder „GFFC WE 04.03.2026") und Kommentar zur Tabellenbezeichnung (A13). Neu, ohne bestehende Felder zu ändern: `HDRG_FALLREGELN` (H-02: Alter, PCCL, VWD, Pflegegrad, beidseitig mit Liste V67, Diagnosen V11, DFS, Nerv; neu seit 14.09.2026 dazu `akf08`: die Kodes aus Anhang B als Sperrliste mit Quelle „DH4 2026 AKF08-V6/V13/V16", in der Auswertung als eigener Zustand „Fallsperre Band 4" vor der Kontextprüfung; die Diagnoseseite V1/V3/V4/V5 zunächst nur als Hinweistext, weil die App keine Nebendiagnosen erfasst), `HDRG_VERDRAENGUNG` (H-03: Rangzahlen der DRGs aus DH S. 409/411, nach V1/V2 bestätigt). Katalog: erledigt 13.09.2026 (3h); Regel ab jetzt: Änderung nur in `data/OPS_Katalogdaten_2026_MASTER.xlsx` (Blätter Katalog, KX, Kommentar, Meta, Aenderungslog), JSON ausschließlich per `scripts/build_katalog2026.py`, Prüfung mit `--check`.

**Ebene 3, die Prüfung.** (a) Querprüfungsskript: HDRG_REGELN gegen V66/V70, Katalogflag 2 gegen LK-2026, Flag 4 gegen V66 ∪ V70, `_KX` gegen V70 minus V66, `_HDRG` gegen VG-2026, `hdrgTrigger` gegen V68 minus V66; jede Abweichung als Zeile. Die Tabellen dafür liegen jetzt maschinenlesbar vor (`dh2026_tabellen.json`, `leistungskatalog2026.json`, seit 14.09.2026 auch `akf08_tabellen.json` mit allen 16 Tabellen und `akf08_sperrlisten_2026.json` mit den fertigen Listen V6 minus V7, V13, V16, V4, V5, V2; in der Sitzung erzeugt, ins Repo nach Freigabe). Neue Querprüfung (d): jeder Kode in `HDRG_REGELN.neutral/aufwertung/positiv/hdrg` und jeder `hdrgTrigger` gegen `akf08_sperrlisten_2026.json` (darf nicht darin stehen); jeder Kode in `OP_STEUERUNG[*].codes` mit `hdrg` ≠ null gegen dieselbe Liste (Treffer = Fallsperre, dann darf `hdrg` nicht gesetzt sein). Stand 14.09.2026: null Abweichungen. (b) Sollwert-Tabelle `hybrid_testfaelle.json` aus Abschnitt 5, auf dem Prüfstand gegen die Fallsteuerung. (c) `webgrouper-nachweise.md` mit Datum, HD, ND, OPS, Alter, VWD, Ergebnis je Lauf.

**Jahreswechsel (Backlog C3).** Neues Definitionshandbuch besorgen (Band 2 für die I20-Tabellen und Band 4 für „Ausschluss Kontextfaktoren MDC 08", beide in derselben Version), Tabellen neu extrahieren, Nummern und OPS-Fassung prüfen, Leistungskatalog und Vergütung nachziehen, Testfälle laufen lassen, Jahresübersicht (Abschnitt 0) fortschreiben.

Was dieses Dokument nicht ist: keine Rechtsquelle und kein Ersatz für den Webgrouper. Es sagt, was wir wissen, aus welchem Jahr und woher, und was wir noch nicht wissen.

## Anhang B: Fallsperre „Ausschluss Kontextfaktoren MDC 08" (AKF08), Band 4, Version 2026 (Nachtrag 14.09.2026)

Quelle DH4 S. 5685–5779. Aufbau der Funktion (S. 5687): zehn Bedingungen, ODER-verknüpft; trifft eine zu, ist die Hybrid-Bedingung „Nicht [Ausschluss Kontextfaktoren MDC 08]" verletzt und der Fall bleibt in der stationären DRG. Die Prüfreihenfolge H-01 bis H-09 ändert sich nicht; die Sperre gehört zu H-02 und wird vor der Kontextprüfung (H-05) geprüft.

| Tabelle | Name im Handbuch | Kodes | Inhalt, fußrelevanter Teil |
|---|---|---|---|
| AKF08-V1 außer V2 | Kontextfaktoren allgemein Diagnosen 1 (Ausschluss) | 1.433 (V2: 4) | Haupt- oder Nebendiagnose: Sepsis A40/A41, Infektionen A/B, Erysipel A46, akute Osteomyelitis M86.0x/1x, eitrige Arthritis M00.x, Knochentuberkulose M90.x, Dekubitus Grad 4 L89.3x, arterielle Embolie I74.x, Diabetes mit Koma/Ketoazidose E10–E14.01/.11, Hypoglykämie E15, Schock R57.x, Meningitis G00–G09 u. a. Ausnahmen V2: I24.0, J43.9, L03.11 (Phlegmone untere Extremität), L03.3 |
| AKF08-V3 | Kontextfaktoren allgemein Diagnosen 2 (BNB) | 525 | bösartige Neubildungen C00–C97 als Haupt- oder Nebendiagnose |
| AKF08-V4 | Kontextfaktoren MDC 08 Diagnosen | 5 | S41.86, S41.89, S51.89, S81.86, S81.89 (offene Wunde mit Weichteilschaden III) |
| AKF08-V5 | Kontextfaktoren allgemein Diagnosen 3 | 16 | angeborene Herzfehler Q20–Q26, Z99.4 |
| AKF08-V6 außer V7 | Kontextfaktoren allgemein Prozeduren 1 / MDC 08 Prozeduren 1 (Ausschluss) | 5.774 (V7: 141) | jede Prozedur; fußnah: 5-784.* Knochentransplantationen (bis auf 5-784.0v/1v), 5-854.x9 Sehnen Unterschenkel, 5-854.4b–8c Sehnen Fuß, 5-788.5h, 5-808.72/a9–ad, 5-827.x (11) und 5-828.x (12) Prothesenwechsel/-entfernung, 5-856.4a, 5-796.* mit Fixateur/Nagel, 5-857/5-858 (je 121), 5-90x/5-92x plastische Deckung (367/709); Ausnahmen V7: 5-854.xc, 5-793/5-794 an Radius, Ulna, Tibia distal (n) und Fibula distal (r), 5-795.h0/x0, 5-796.20/x0, 5-856.x6, Gefäßkodes 5-397/5-39c |
| AKF08-V8–V12 | Kontextfaktoren MDC 08 Prozeduren 2–6 | 4/12/12/7/11 | nur als Kombination aus mindestens zwei Tabellen: Frakturversorgung Klavikula, Radius proximal/distal, Ulna proximal, Tibia distal (5-793/5-794/5-795/5-796) |
| AKF08-V13 | Kontextfaktoren allgemein Prozeduren 2 | 4.746 | jede Prozedur; fußnah: 5-785.2d–5d, 5-801.k*, 5-812.h*, 5-820.20–22, 5-822.90–92, 5-829.c/k0–k4/m, 5-930.22, 5-93b.d0/d1, 1-940 |
| AKF08-V14 + V15 | Kontextfaktoren allgemein Prozeduren 4 und 5 | 12 + 2 | nur zusammen: Stentretriever 8-83b.8x mit intrakranieller Thrombektomie 8-836.60/80, nicht fußrelevant |
| AKF08-V16 | Kontextfaktoren allgemein Prozeduren 3 | 44 | Knorpel- und Chondrozytentransplantation 5-801.a4/ak, 5-801.b*/c*/k* und 5-812.9*/a*/h* (auch OSG, Tarsalgelenk, TMT, MTP, Zehen) |
| Beatmung | – | – | Beatmung > 0 Stunden |

Zählung nach eigener Extraktion vom 14.09.2026 (zweiter Durchgang mit Kodes, die an dritter Stelle einen Buchstaben tragen, und Seite 5791; erster Durchgang hatte V6 mit 5.114 und V13 mit 3.775 unterzählt). Kein Kode der Positivliste I20-V68 und kein Fuß-Kode des Leistungskatalogs 2026 steht in einer AKF08-Prozedurenliste.

In der App verwendete Kodes, die in einer AKF08-Prozedurenliste stehen (40 von 269; Namen aus `katalog2026.json`, sonst Kurztext des Handbuchs):

| OPS | Bezeichnung | AKF08 | Katalogflag | zugleich I20-V70 | Verwendung in der App |
|---|---|---|---|---|---|
| 5-784.0n | Tx von Spongiosa, autogen off chir, Tibia distal | V6 | kein Flag | nein | Hebel stationär OSG-Arthrodese/TTC (I13E→I13D), `arthrodese_osg` hebel |
| 5-784.0r | Tx von Spongiosa, autogen off chir, Fibula distal | V6 | kein Flag | nein | Hebel stationär Fibulafraktur ≥ 2 N (I13N→I13E), UC-Modul |
| 5-784.0s | Tx von Spongiosa, autogen off chir, Talus | V6 | kein Flag | nein | AMIC, TN-Arthrodese (UC-Modul) |
| 5-784.0u | Tx von Spongiosa, autogen off chir, Tarsale | V6 | kein Flag | nein | Lapidus UC-Modul Kodeliste (Transplantation Tarsale), stationär |
| 5-784.0w | Tx von Spongiosa, autogen offen chir.: Phalangen Fuß | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-784.1n | Tx kortikospong Span, autogen off chir, Tibia distal | V6 | kein Flag | nein | SMOT Open Wedge (UC-Modul) |
| 5-784.1t | Tx kortikospong Span, autogen off chir, Kalkan | V6 | kein Flag | nein | Double/Triple-Arthrodese BK-Span (UC-Modul) |
| 5-784.3v | Knochentransplantation, nicht gefäßgestielt: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-784.7n | Tx von Spongiosa, allogen off chir, Tibia distal | V6 | kein Flag | nein | SMOT Open Wedge allogen (UC-Modul) |
| 5-784.7t | Tx von Spongiosa, allogen off chir, Kalkaneus | V6 | kein Flag | nein | Coalitio LCOT (UC-Modul), OP_STEUERUNG Kodelisten |
| 5-784.7u | Tx von Spongiosa, allogen off chir, Tarsale | V6 | kein Flag | nein | Kalkaneus/Tarsale-Osteotomie (UC-Modul) |
| 5-784.cv | Tx von Spongiosa, autogen endoskopisch: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-784.cw | Tx von Spongiosa, autogen endoskopisch: Phalangen Fuß | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-784.xv | Sonstige Knochentransplantation und -transposition: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-784.xw | Sonstige Knochentransplantation und -transposition: Phalangen Fuß | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-788.5h | Fuß: Osteotomie: Os metatarsale I, Doppelost, ReOP Rezid | V6 | kein Flag | nein | nur Name in `opmethoden.json` |
| 5-796.ev | Off. Reposition MFF: Blount-Klammer: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-796.gv | Off. Reposition MFF: Intramedullärer Draht: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-796.gw | Off. Reposition MFF: Intramedullärer Draht: Phalangen Fuß | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-796.mv | Off. Reposition MFF: Ringfixateur: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-796.nv | Off. Reposition MFF: Bewegungsfixateur: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-796.nw | Off. Reposition MFF: Bewegungsfixateur: Phalangen Fuß | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-796.pv | Offene Reposition einer Mehrfragment-Fraktur an kleinen Knochen: Durch Verriegelungsnagel: Metatarsale | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-827.10 | Wechsel SprunggelEndoprot: SprunggelEndoprot, n zement | V6 | kein Flag | nein | OSG-TEP-Wechsel, stationär (OP_STEUERUNG, UC-Modul) |
| 5-829.k2 | Impl/(T)We mod EndPr kn DefSit/Kn(t)ers SchK m KnDf ent L/D | V13 | kein Flag | nein | OSG-TEP-Wechsel Inbone (UC-Modul) |
| 5-854.29 | (Part) Transposition von Sehnen, Unterschenkel | V6 | kein Flag | nein | Hebel stationär Haglund/Achillessehnen-Split (I27E→I27D), Dwyer mit Peroneal (UC-Modul) |
| 5-854.39 | Augmentation von Sehnen, Unterschenkel | V6 | kein Flag | nein | nur Name in `opmethoden.json` |
| 5-854.49 | Ersatzplastik Sehnen, Unterschenkel | V6 | kein Flag | nein | FHL-Transfer `fhl_transfer`, „nur stationär" (UC-Modul) |
| 5-854.4b | Rekonstruktion Sehnen: Ersatzplastik: Fußwurzel | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.4c | Rekonstruktion Sehnen: Ersatzplastik: Mittelfuß und Zehen | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.5b | Ersatzplastik Sehnen mit Interponat: Fußwurzel | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.5c | Ersatzplastik Sehnen mit Interponat: Mittelfuß und Zehen | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.6b | Schaffung Transplantatlager Sehnen: Fußwurzel | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.6c | Schaffung Transplantatlager Sehnen: Mittelfuß und Zehen | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.7b | Rekonstruktion Sehnen: Transplantation: Fußwurzel | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.7c | Rekonstruktion Sehnen: Transplantation: Mittelfuß und Zehen | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.89 | Transplantatwechsel von Sehnen, Unterschenkel | V6 | kein Flag | nein | nur Name in `opmethoden.json` |
| 5-854.8b | Rekonstruktion Sehnen: Transplantatwechsel: Fußwurzel | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-854.8c | Rekonstruktion Sehnen: Transplantatwechsel: Mittelfuß und Zehen | V6 | 4 | ja | Kontextliste I20-V70 |
| 5-856.4a | Transplantation, autogen Fasz, Fuß | V6 | kein Flag | nein | Coalitio mit Faszie (UC-Modul), stationär |

Lesart für die App (Vorschlag, noch nicht gebaut): Die 23 Kodes mit „zugleich I20-V70 = ja" sind bereits Kontextprozeduren und ändern nichts. Die 17 übrigen sind in den App-Daten nur in stationären Pfaden hinterlegt; sie bekommen mit `HDRG_FALLREGELN.akf08` eine Quelle und einen sichtbaren Grund („Fallsperre Band 4"), damit die Fallsteuerung sie nie als „neutral" wertet, falls sie einmal zu einem Hybrid-Haupteingriff hinzukommen (Beispiel: Lapidus + 5-784.0u im UC-Modul, FHL-Transfer 5-854.49 zu einem Hybrid-Eingriff). Diagnoseseite: Die App erfasst keine Nebendiagnosen; ein Hinweistext in der Auswertung („Sepsis, akute Osteomyelitis, eitrige Arthritis, bösartige Neubildung oder Weichteilschaden III als Nebendiagnose schließen die Hybrid aus, Band 4 AKF08") reicht als erste Stufe.
