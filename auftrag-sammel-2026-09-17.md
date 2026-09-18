# Sammel-Auftrag 17.09.2026: vier kleine Punkte aus den Gegenproben

Stand 17.09.2026, Cowork-Sitzung, Freigabe des Autors („Ok" auf den Vorschlag, zuerst den Sammel-Auftrag). Ausgangsstand `app.html`: Commit 8ae4fe5 (799.756 Byte), Zeilenangaben beziehen sich darauf. Ein Commit, eine Vollzugsmeldung. Datenteil 3s (`data/opsteuerung.json`, Feld `opsWeg`) schreibt die Cowork-Sitzung nach eigener Freigabe; Bucket-Upload vor dem Push. Der heutige Code ignoriert das Feld, die Daten können vorab raus.

## 1. Kodeliste der Fallsteuerung folgt den Zusatzeingriffen

Befund (Prüfstand 17.09.): Der Kasten „OPS-Codes (zwingend beide kodieren)" (Z. 3712–3715) zeigt nur `best.opsCodes`. Bei „Tarsale Koalition", Coalitio TC, zeigt er mit „+ LCOT" weiterhin nur 5-781.at, 5-856.4a, 5-852.g9 (ohne 5-781.4t und 5-784.7t) und mit „ohne Faszien-Fett-Lappen" weiterhin 5-856.4a und 5-852.g9, obwohl der Hinweis darunter sagt, dass sie entfallen. `fallCodes` (Z. 3448–3453), die Grundlage der Hybrid-Auswertung, nimmt die Kodes der Modifikatoren zwar auf (Z. 3450), kann aber keinen entfernen. Die Überschrift ist fest und bei drei Kodes falsch.

Neues Datenfeld (3s): Modifikator kann `opsWeg: ["<Kode>", …]` tragen = Kodes des Grundeingriffs, die mit diesem Zusatzeingriff entfallen. Stand nach 3s: `coalition_tc`/`coalition_cn` `ohne_lappen` → `["5-856.4a","5-852.g9"]`; `arthrodese_tmt13` `vier_fuenf` → `["5-808.a6"]` (5-808.a6 = drei Gelenke, mit vier bis fünf Gelenken gilt 5-808.a7/a8 aus `ops`).

Änderung: (a) In `fallCodes` (Z. 3448 ff.) nach dem Hinzufügen der Modifikator-Kodes alle Kodes entfernen, die in `opsWeg` eines aktiven Modifikators stehen. (b) Der Kasten zeigt die sichtbare Liste `kodeListe` = `best.opsCodes` ohne die `opsWeg`-Kodes der aktiven Modifikatoren, danach je aktivem Modifikator seine `ops` (Name aus `OPS_LABELS[code]`, sonst der Kode; alle Modifikator-Kodes haben heute ein Label). Der Kasten erscheint, sobald `kodeListe` nicht leer ist (heute nur bei `best.opsCodes.length > 0`; neu also auch bei AMIC + Innenknöchelosteotomie, Peronealsehnenluxation „nur Naht", OSG-TEP-Wechsel, die bisher gar keine Liste hatten). (c) Überschrift: „OPS-Kodes des Eingriffs". Die DMMO- und Lapidus-Zusätze in `fallCodes` (Z. 3451–3453) bleiben, wie sie sind, und erscheinen nicht in der sichtbaren Liste (unverändert zu heute).

## 2. Befund-Label schneidet Dezimalzahlen ab

Befund (Prüfstand-Bericht Abschnitt 19): `BefTog` bildet das Label eines nicht gesetzten Befunds aus `b.pos.split(",")[0]` (Z. 1257). Bei „Knöchel-Arm-Index [0,7], außerhalb des Normbereichs …" wird daraus „Knöchel-Arm-Index [0"; ebenso bei „Zehen-Arm-Index [0,5] …". Änderung: am ersten Komma trennen, auf das ein Leerzeichen folgt: `b.pos.split(", ")[0]`. Alle Befundtexte trennen Halbsätze mit „, " (Komma + Leerzeichen); Dezimalzahlen haben kein Leerzeichen nach dem Komma. Die Cowork-Sitzung hat die 19 Diagnosen durchgesehen: kein Label ändert sich außer den beiden Dezimalfällen. Nur die Anzeige im Untersuchungsblock, nicht der Brieftext.

## 3. Ampel-Texte der Materialkosten nach der Sprachregel

Befund: vier Texte sind von der Sprachprüfung vom 14.09. nicht erfasst worden (`auftrag-sprachregel-abrechnung.md`: keine Anweisung zum Kodieren oder zur Verweildauer, keine Wörter Hebel, Ausweg, Trigger, verschenkt, rechtfertigen, Erlösverlust, ökonomisch, Rückfall, MDK-Kürzung; Beschreibung statt Aufforderung):

Z. 3561 (Stationär-Box, rot): „⚠ Implantatkosten deutlich über InEK-Referenz — Fall droht defizitär zu werden bei Kürzung oder Erlös unter regulärer DRG. Volle DRG zwingend ansteuern (Liegezeit {ugvd+1} Tage halten), Materialalternativen prüfen."
→ „⚠ Implantatkosten deutlich über der InEK-Referenz. Bei einem Abschlag unter der unteren Grenzverweildauer deckt der Erlös die Kosten nicht mehr; Materialalternativen prüfen."

Z. 3562 (Stationär-Box, gelb): „⚠ Implantatkosten über InEK-Referenz — volle DRG sollte sicher angesteuert werden."
→ „⚠ Implantatkosten über der InEK-Referenz."

Z. 4448 (Materialsatz-Ansicht, rot): „⚠ Implantatkosten deutlich über InEK-Referenz — Fall droht defizitär zu werden bei Kürzung. Volle DRG zwingend ansteuern, Materialalternativen prüfen."
→ „⚠ Implantatkosten deutlich über der InEK-Referenz; Materialalternativen prüfen."

Z. 4449 (Materialsatz-Ansicht, gelb): wie Z. 3562 → „⚠ Implantatkosten über der InEK-Referenz."

Die Zeile davor („🔴 {pct}% über InEK — kritisch", Z. 3499) bleibt. Farben und Kästen unverändert.

## 4. Nichts anderes

Keine weiteren Änderungen. Der Brieftext ist in allen Fällen zeichengleich; die Fallsteuerung ändert sich nur in der Kodeliste (Punkt 1) und in den zwei Ampel-Texten, das Untersuchungs-Label nur bei den zwei Dezimalbefunden.

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3r.json`, 19 Diagnosen, 83 OP-Fälle): Briefe zeichengleich; Fallsteuerung gleich bis auf die Überschrift des Kodekastens, neu erscheinende Kästen bei Einträgen ohne `opsCodes`, und die Ampel-Texte (die Cowork-Sitzung weist jede Abweichung je Fall aus). Gezielt: Tarsale Koalition, Coalitio TC: ohne Toggle 5-781.at, 5-856.4a, 5-852.g9; „+ LCOT" zusätzlich 5-781.4t und 5-784.7t mit Label; „ohne Faszien-Fett-Lappen" nur 5-781.at; beides zusammen 5-781.at, 5-781.4t, 5-784.7t. `hdrgAuswertung` bekommt dieselbe bereinigte Liste (Fallsteuerung I27D/I20C wie heute). TMT-Arthrodese 1–3 mit „4–5 Gelenke": 5-808.a7 statt a6. Diabetischer Fuß, Untersuchung: Label „Knöchel-Arm-Index [0,7]" und „Zehen-Arm-Index [0,5] beziehungsweise Zehendruck [25] mmHg" vollständig. Ampel-Texte in Stationär-Box und Materialsatz-Ansicht mit Testpreisen (rot ab 150 % der Referenz). Keine Konsolenfehler.

Abnahme des Autors am Handy: Tarsale Koalition, Coalitio TC, „ohne Faszien-Fett-Lappen" und „+ LCOT" setzen: Kasten „OPS-Kodes des Eingriffs" mit 5-781.at, 5-781.4t, 5-784.7t. Diabetischer Fuß, Klinische Untersuchung: Zeile „Knöchel-Arm-Index [0,7]" lesbar.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern der vier Änderungen.
