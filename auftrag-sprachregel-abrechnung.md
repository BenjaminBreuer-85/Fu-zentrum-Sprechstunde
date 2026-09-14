# Auftrag an die Code-Sitzung: Sprachregel Abrechnung (app.html)

Stand 14.09.2026, Cowork-Sitzung. Grundlage: `sprachpruefung-abrechnung-2026-09-14.md` (Befund und Grundsätze), Anweisung des Autors: „Nach den Kodierrichtlinien muss alles, was gemacht wurde, auch kodiert werden. Wir dürfen nicht den Eindruck erwecken, hier zu betrügen; die Formulierung muss sachlicher sein." Zeilen am Stand `app.html` Commit b384ece (768.600 Byte). Nur Texte, keine Logik; Zuordnung, Beträge und Prüfstand-Sollwerte ändern sich nicht. Parallel dazu ändert die Cowork-Sitzung die Datentexte (Schritt 3l: `opsteuerung.json` Hinweise, `optexte.json` UC-Kodiertexte).

## Drei Grundsätze für jeden sichtbaren Text

1. Beschreibung statt Anweisung: Die App sagt, welche Zuordnung aus welchem Vorgehen folgt („Mit Sehnentransfer gruppiert der Fall stationär nach I20E, ohne nach I20O"), nie, was zu kodieren oder wegzulassen ist.
2. Die Entscheidung ist die Indikation: Sätze knüpfen an das Vorgehen an („Wird eine Spongiosaplastik durchgeführt, …"), nicht an den Kode.
3. Kodiert wird, was durchgeführt und im Bericht beschrieben ist (DKR P001). Dieser Satz steht als Fußzeile unter jedem Kodierhinweise-Block; kein Text widerspricht ihm.

Gesperrte Wörter in sichtbaren Texten: „NICHT kodieren", „nicht beschreiben", „IMMER kodieren/mitkodieren", „Hebel", „HEBEL-CODE", „Erlöshebel", „Ausweg", „Trigger", „verschenkt", „rechtfertigen", „Erlösverlust", „ökonomisch", „Rückfall in H-DRG", „MDK-Kürzung". Technische Namen (`hebel`, `hebelName`, `hebelZiel`, `hebelStat`, `hdrgTrigger`, `kpCodes`) bleiben.

## 1. Sprechstundenbrief, Regelsatz-Sätze (`hdrgAuswertung`, Z. 1479–1507)

| Zeile | heute | neu |
|---|---|---|
| 1482 | `… " führt aus " + hdrgStart + " heraus. Stationär " + erg.drg + ". " + ambSatz` | `… " gruppiert den Fall nicht mehr in " + hdrgStart + ", sondern stationär nach " + erg.drg + ". " + ambSatz` |
| 1488 | „Fall liegt in I20O." | „Ambulant gruppiert der Fall nach I20O." |
| 1489–1490 | „Ausweg für diese OP: <hebelName> (<hebel>) nach <drg>." | „Wird stationär zusätzlich <hebelName> (<hebel>) durchgeführt, gruppiert der Fall nach <drg>." |
| 1491 | „Kein Ausweg gesetzt." | „Kein erlösrelevanter Zusatzeingriff hinterlegt." |
| 1507 | „… steht nicht im AOP-Katalog, zieht den ambulanten Fall aus dem EBM in die Hybrid-DRG I20O." | „… steht nicht im AOP-Katalog; der ambulante Fall gruppiert dann in die Hybrid-DRG I20O, nicht nach EBM." |

## 2. Sprechstundenbrief, Fallsteuerung (Z. 3406–3568)

| Zeile | heute | neu |
|---|---|---|
| 3406 | „❌ Kontextprozedur(en) NICHT kodieren — sonst Verlust der H-DRG" | „Hybrid-DRG nur ohne Kontextprozedur: wird sie durchgeführt, wird sie kodiert, und der Fall gruppiert in die stationäre DRG." |
| 3445 | „Erlöshebel: <hebel> (<hebelName>) → <hebelZiel>" | „Erlösrelevanter Zusatzeingriff: <hebelName> (<hebel>) → <hebelZiel>" |
| 3446 | „(aktuell <drg>, Hebel nicht genutzt)" | „(ohne diesen Eingriff <drg>)" |
| 3540 | „❌ Ambulant: NICHT kodieren — sonst Verlust der H-DRG. Bei klinischer Notwendigkeit besser stationäre Führung." | „Ambulant bleibt der Fall nur ohne diese Prozedur in der Hybrid-DRG; ist sie klinisch notwendig, stationäre Führung." |
| 3541 | „✅ Stationär: IMMER kodieren zum Ausschluss H-DRG → volle DRG <drg>." | „Stationär: wird sie durchgeführt, wird sie beschrieben und kodiert; der Fall gruppiert dann nach <drg>." |
| 3568 | „kein Ausweg" | „kein Zusatzeingriff hinterlegt" |

## 3. Metallentfernung im OP-Bericht (Z. 4391)

„(Hebel-Code)" → „(führt nach I20O)".

## 4. Zweigtexte im OP-Bericht (`ziel`, `kodier`), Z. 4950–5151, 5846

Muster, auf alle Zweige anwenden; die vollständige Fundliste ergibt die Suche nach den gesperrten Wörtern. Beispiele:

| Zeile | heute | neu |
|---|---|---|
| 4950 | „5-854.2c (Sehnentransfer) IMMER mitkodieren." | „Der Sehnentransfer (5-854.2c) gehört zum Eingriff und wird beschrieben und kodiert." |
| 4950 | „⚠ Häufiger Fehler: Lapidus als ambulant geplant → nicht abrechenbar!" | „Ambulant: 5-808.a4 steht nicht im AOP-Katalog; für Kliniken ambulant daher nur als Hybrid I20M (mit Akin)." |
| 4957 | „5-784.0v (Spongiosa) IMMER mitkodieren." | „Mit Spongiosaplastik (5-784.0v), wenn durchgeführt, gruppiert der Fall nach I20D." |
| 4958 | „5-784.0v (Spongiosa) IMMER mitkodieren → I20D. ⚠ Im OP-Bericht erwähnen!" | „Wird eine Spongiosaplastik (5-784.0v) durchgeführt, wird sie beschrieben und kodiert; Zuordnung I20D." |
| 4961 | „Ambulant → H-DRG I20N (2.085 €). ❌ 5-784.0v NICHT kodieren! … Ab 2 Nächte: 5-784.0v mitkodieren → volle DRG I20E (3.923 €)." | „Ambulant ohne Spongiosaplastik: Hybrid-DRG I20N (2.085 €). 1 Belegungstag: gekürzte DRG I20E (~2.800 €). Mit Spongiosaplastik (5-784.0v) ab 2 Belegungstagen volle DRG I20E (3.923 €)." |
| 4962, 4966 | „⚠ Ambulant: 5-784.0v NICHT kodieren → H-DRG I20N! ⚠ Stationär: 5-784.0v IMMER → Kontextprozedur → I20E." | „Ambulant setzt die Hybrid-DRG I20N voraus, dass keine Spongiosaplastik durchgeführt wird. Stationär gruppiert der Fall mit Spongiosaplastik (5-784.0v) nach I20E." |
| 4962, 4966, 4976, 4983, 5151 | „💡 WEGE AUS DER H-DRG → VOLLE DRG: ① VWD ≥3 Tage (3 Nächte post-OP) → volle DRG. ⚠ Jeder Tag dokumentarisch rechtfertigen! Bei Kürzung: Rückfall in H-DRG. ② Kontextprozedur … mitkodieren → volle DRG ab 2 Nächten. ✅ EMPFOHLEN: Bei Kürzung nur gekürzte DRG (besser als H-DRG)." | „Zuordnung bei stationärer Führung: ① ab 3 Belegungstagen volle DRG; die medizinische Notwendigkeit jedes Belegungstages ist zu dokumentieren, bei kürzerer Verweildauer gruppiert der Fall in die Hybrid-DRG. ② Wird <Kontextprozedur> durchgeführt, wird sie beschrieben und kodiert; der Fall gruppiert dann ab 2 Belegungstagen in die volle DRG, bei 1 Belegungstag in die gekürzte DRG." |
| 4976 | „⚠ HEBEL-CODE: 5-854.2c … Ambulant: NICHT kodieren → H-DRG I20O. Stationär: IMMER mitkodieren → Kontextprozedur → I20E. ⚠ Sehnentransfer muss im OP-Bericht dokumentiert sein! … ⚠ Jeder Tag muss dokumentarisch gerechtfertigt sein. Bei MDK-Kürzung: Rückfall in H-DRG! … Mit Kontextprozedur ist ein Belegungstag weniger zu begründen." | „Sehnentransfer/Rebalancing (5-854.2c): ambulant bleibt der Fall nur ohne Sehnentransfer in der Hybrid-DRG I20O; wird er durchgeführt, wird er beschrieben und kodiert, und der Fall gruppiert stationär nach I20E." Der Satz „ein Belegungstag weniger zu begründen" entfällt ersatzlos. |
| 4975 | „Ambulant → H-DRG I20O (1.007 €). ❌ 5-854.2c NICHT kodieren!" | „Ambulant ohne Sehnentransfer: Hybrid-DRG I20O (1.007 €)." |
| 5012 | „⚠ HEBEL-CODE: 5-784.0n + 5-783.0d (Spongiosa Tibia) → I13E → I13D (+1.250 €)! ⚠ Spongiosa muss im OP-Bericht dokumentiert sein! ⚠ Häufiger Fehler: Spongiosa entnommen aber nicht kodiert → 1.250 € Erlösverlust!" und „💡 Toggle: + Spongiosa → I13D (7.079 € statt 5.829 €) ⚠ Häufiger Fehler: Spongiosa vergessen zu kodieren → 1.250 € verschenkt!" | „Mit Spongiosaplastik (5-783.0d Entnahme Beckenkamm, 5-784.0n Transplantation Tibia) gruppiert der Fall nach I13D (7.079 €), ohne nach I13E (5.829 €). Wird sie durchgeführt, wird sie im OP-Bericht beschrieben und kodiert." (für beide Varianten) |
| 5150, 5151 | „❌ 5-784.0r NICHT kodieren! … ⚠ HEBEL-CODE: 5-784.0r … Ambulant: NICHT kodieren → H-DRG I13N. Stationär ≥2N: IMMER mitkodieren." | „Ambulant/1 Belegungstag ohne Spongiosaplastik: Hybrid-DRG I13N (3.091 €). Mit Spongiosaplastik an der Fibula (5-784.0r), wenn durchgeführt, ab 2 Belegungstagen I13E (CM 1,278 = 5.829 €)." |
| 5846 | „· Stat: +5-784.0v (Spongiosa) · Amb: 5-784.0v NICHT kodieren!" | „· stationär mit Spongiosaplastik 5-784.0v → I20E · ambulant ohne Spongiosaplastik → I20N" |

## 5. OP-Bericht, Kodierhinweise-Block (Z. 6270, 6383, 6390–6391) und UC-Bericht (Z. 6692, 6781)

| Zeile | heute | neu |
|---|---|---|
| 6270, 6692 | „Ökonomisches Codierziel:" | „Zuordnung nach Setting:" |
| 6383 | „❌ <Kode> (<Name>) NICHT kodieren" und „Im OP-Bericht: <Namen> NICHT beschreiben." | eine Zeile: „Ambulante Führung in der Hybrid-DRG setzt voraus, dass <Namen> nicht durchgeführt werden; werden sie durchgeführt, gruppiert der Fall in die stationäre DRG." (der Ersatz aus `auftrag-beidseits-folge.md` Punkt 2 für den gesperrten Fall bleibt) |
| 6390 | „✅ <Kode> (<Name>) = Hebel → IMMER kodieren → <Ziel>" | „<Name> (<Kode>): wird beschrieben und kodiert, Zuordnung <Ziel>" |
| 6391 | „✅ <Kode> (<Name>) = Kontextprozedur → IMMER kodieren" / „Im OP-Bericht: <Namen> MUSS beschrieben und dokumentiert werden." / „Mit Kontextprozedur: 1 Nacht → gekürzte DRG (besser als Hybrid-DRG) / 2 Nächte → volle DRG <drg> / Ohne Kontextprozedur: VWD ≥ 3 Tage nötig für volle DRG. Bei Kürzung: Rückfall in Hybrid-DRG." | „<Name> (<Kode>) = Kontextprozedur: wird beschrieben und kodiert" / „Zuordnung mit Kontextprozedur: 1 Belegungstag gekürzte DRG, ab 2 Belegungstagen volle DRG <drg>. Ohne Kontextprozedur: ab 3 Belegungstagen volle DRG, sonst Hybrid-DRG. Die medizinische Notwendigkeit jedes Belegungstages ist zu dokumentieren." |
| 6781 | „OP-Bericht: Kontextprozedur-Eingriff NICHT beschreiben." | entfällt; stattdessen die Zeile aus 6383 (Ambulante Führung setzt voraus, dass … nicht durchgeführt wird) |
| Blockende (6383/6391, 6781) | – | Fußzeile: „Kodiert wird, was durchgeführt und im Bericht beschrieben ist." |

## 6. Suche und Abnahme

Nach dem Umbau Suche in `app.html` nach den gesperrten Wörtern (Abschnitt oben): null Treffer in Zeichenketten, die der Nutzer sieht; Treffer in Variablennamen und Kommentaren sind erlaubt. Cowork-Prüfstand: Sprechstundenbrief 81 Fälle, OP-Bericht 68, Kombinationen 6 gegen `baseline_*_s4.json`; erlaubt sind ausschließlich Textänderungen aus diesem Auftrag, keine Änderung an DRG-Kürzeln, Beträgen, Empfehlungen (✓) oder Kodelisten. Abnahme: Autor liest drei Fallsteuerungen (Chevron, Lapidus, OSG-Arthrodese mit Spongiosa) und einen OP-Bericht (Chevron) gegen.
