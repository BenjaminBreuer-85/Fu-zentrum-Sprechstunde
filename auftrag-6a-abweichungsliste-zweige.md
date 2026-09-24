# Auftrag Clinic (Schritt 6a): Abweichungsliste der 31 OP-Bericht-Zweige gegen `OP_STEUERUNG` und Regelsatz

Stand 23.09.2026, Cowork-Sitzung. Fortsetzung von `auftrag-hybrid-regeln.md`, fünfter Teil, Punkt 3 (Umgang mit den 28 doppelt gepflegten Zweigen) und sechster Teil, Punkte 2–4. Datei `app.html`, Ausgangsstand Commit 70d85e7 (806.206 Byte, Zeilenangaben darauf); Daten Stand Bucket 22.09.2026 (`opsteuerung.json` 3x, `opmethoden.json` 3z, `optexte.json` 3aa).

**Dieser Schritt ändert nichts an `app.html` und nichts an den Daten.** Ergebnis sind drei Dateien im Repo-Root bzw. `scripts/` und eine Vollzugsmeldung. Die Umstellung selbst (6b) kommt als eigener Auftrag, nachdem der Autor die Liste Zeile für Zeile entschieden hat.

## Warum jetzt

Der OP-Bericht rechnet seine Fallsteuerung aus 31 festen Zweigen (`const [allOPS,erloesData]`, Z. 4995 ff.; Vorrang über `_prio`, Z. 5146; erster Zweig Lapidus Z. 5154). Der Sprechstundenbrief rechnet seit dem Regelsatz aus `OP_STEUERUNG` + `HDRG_REGELN` (`hdrgAuswertung`, Z. 1492; Aufruf Z. 3499). Beide Wege laufen auseinander, seit die Regeln 2026 in den Daten stehen. Drei belegte Fälle aus dem Prüfstand-Bericht vom 13.09.:

- **C1 Lapidus, Trigger:** Z. 3493 schiebt beim Lapidus alle `hdrgTrigger` (5-788.56, 5-788.5e, 5-788.60, 5-788.5c, 5-788.40) in die Kodeliste des Falls, nicht nur den Akin. Folge: die Fallsteuerung warnt bei jedem Lapidus „Arthroplastik MTP I (5-788.60) … kein Ausweg", obwohl niemand 5-788.60 gewählt hat. Anzeigefehler.
- **C2 Chevron + drei DMMO:** Sprechstundenbrief (Regelsatz I20O_N): 5-788.54 führt aus I20O heraus nach I20E. OP-Bericht (Zweig Z. 5177 ff.): zeigt weiter „AMBULANT ✓ H-DRG I20O", die DMMO-Zahl ändert nur den Memo-Text. Lapidus + drei DMMO ebenso: Titel bleibt „Lapidus", die DMMO werden ignoriert.
- **C3 Lapidus, Hybrid-Spalte:** Zweig zeigt „H-DRG —", der Sprechstundenbrief zeigt I20M (Akin automatisch, `lapidus.hdrgTrigger`). Der Vergleich vom 09.09. (`abgleich-zweige-opsteuerung-2026-09-09.md`) hatte nur `drg` verglichen, nicht `hdrg`.

Dazu seit dem 09.09. neu in den Daten und im Sprechstundenbrief, im OP-Bericht-Zweig aber nicht: PIP-Regel 2026 (5-808.bd neutral, be/bf/bg → I20N, bh Kontext; die Zweige tragen noch „≥3 … keine H-DRG"-Texte, z. B. Z. 5169, 5173, 5183, 5190, 6599), Beidseits-Sperre I20-V67 (`beidseitsSperre`, Z. 1477, im OP-Bericht nur über `erloesData.hdrg`, Z. 5427–5431), Fallsperre AKF08, TMT-Kodes (7a63ddb) und Cotton implantatfrei.

## Was die Liste enthält

Eine Zeile je Zweig **und je Schalterstellung**, die der Zweig unterscheidet (mit/ohne Spongiosa, DMMO-Zahl 0/1–2/3/4, mit/ohne Akin, mit/ohne LCOT, mit/ohne MDO, mit/ohne IKO, Luxation mit/ohne Rinne/Naht, Alter < 18 bei Arthrorise/Coalitio, TMT-Gelenkzahl 1/2/3/4, Cotton autolog/allogen, MDO + Cotton). Toggle-Fälle sind keine Abweichungen (sechster Teil, Punkt 4), aber sie müssen in der Liste stehen, damit der Autor sieht, was die Auswertung daraus macht. Je Zeile drei Spalten:

**A Literal (Zweig, wie heute im OP-Bericht):** `label`, `hdrg`, `hdrg_n1`, `drg` (nur der DRG-Kode, ohne Betrag), `empf`, `ops` (die Kodeliste `o`, die der Zweig schiebt), die Kodes im `kodier`-Text, `hebelStat`/`kpAmbZusatz`/`hebelZiel`, sofern gesetzt, und die Aussagen in `ziel`/`kodier`, die eine Regel behaupten („≥3 DMMO → keine H-DRG", „Alter < 18", „< 12 Jahre → I20B" usw.), als Stichwort.

**B Daten (`OP_STEUERUNG[key]`):** `hdrg`, `drg`, `empf`, `opsCodes`, `hdrgTrigger`, `hebel`, `kontext`, Modifikatoren (`modifikatoren`), `beidseitsHybridBleibt`, `ambStatus`, `aufwertung`/`ausschluss` (Altbestand), `implantatfrei`, `hinweise` (nur Typ und erste Worte). Zuordnung Zweig → Schlüssel wie `ZUORDNUNG` in `scripts/verify_zweige.py`; wo ein Zweig mehrere Schlüssel abdeckt (Chevron/Scarf/Youngswick, DMMO/Weil/PIP, TEP-Modelle, Rückfuß-Arthrodesen), eine Zeile je Schlüssel.

**C Auswertung (was der Regelsatz aus denselben Kodes macht):** `hdrgAuswertung({best: OP_STEUERUNG[key], bestKey: key, hdrg: best.hdrg, drg: best.drg, codes: <ops aus A + Modifikator-Kodes der Schalterstellung>, ambulant: true})` → `hdrg`, `drg`, `setting`, `warnungen`, `treffer.kontext`, `treffer.aufwertung`; dazu `beidseitsSperre("bds", …)` als eigener Wert. Berechnung in Node: `hdrgRegelsatz`, `hdrgAuswertung`, `beidseitsSperre`, `steuerAnzeige` (Z. 1444–1564) sind reines JS ohne React; sie lassen sich per Textausschnitt aus `app.html` laden, `OP_STEUERUNG`, `HDRG_REGELN`, `HDRG_FALLREGELN` aus `data/opsteuerung.json`, `window._fx`/`_E`/`_DRG`/`_HDRG` als Stubs, die nur den Kode zurückgeben. Bitte den Ausschnitt nicht kopieren, sondern zur Laufzeit aus `app.html` schneiden (Marker: Funktionsnamen), damit das Skript bei jedem Stand neu läuft.

**Bewertung je Zeile:** `gleich` (A = B = C), `toggle` (A weicht von B ab, C liefert A: die Auswertung erzeugt den Fall aus den Regeln, keine Entscheidung nötig), `abweichend` (A ≠ C oder B ≠ C: Entscheidung des Autors), `kein Eintrag` (die drei Zweige OSG-TEP-Wechsel, Sprunggelenksfraktur mit/ohne Syndesmose: A vollständig ausgeben als Vorlage für den neuen Eintrag). Spalte **Entscheidung** leer lassen; der Autor trägt „A", „B", „C" oder einen neuen Wert ein.

## Zeilen, die auf jeden Fall erscheinen müssen

1. Lapidus: `hdrg` (A „—", B/C I20M mit Akin), Kodeliste ohne 5-788.56 obwohl `hdrgTrigger` den Akin als festen Bestandteil führt, Spongiosa 5-784.0u (Tarsale, AKF08-V6) statt 5-784.0v (Metatarsale, `lapidus.hebel`), Lapidus + 5-854.2c (bleibt I20M, V70 minus V66), Lapidus + drei DMMO (C2), Lapidus + 5-783.0v/5-784.0v (I20D, keine Hybrid).
2. MTP-I-Arthrodese + ≥3 DMMO: A I20D fest, B I20E, C aus `I20O_N.kontext` 5-788.54 `{I20N: I20D}` = I20D (sechster Teil, Punkt 2). Bitte zeigen, dass C das ohne festen Wert liefert; dann ist die Zeile `toggle`, nicht `abweichend`.
3. Chevron/Scarf/Youngswick/Cheilektomie/Exostose mit 0/1/2/3/4 DMMO und mit/ohne 5-854.2c (C2), dazu Chevron + Akin.
4. Kleinzehen/DMMO/Weil/PIP: 1–2 DMMO (I20N), 3–4 DMMO (5-788.54/55 → I20E/I20C bzw. I20F allein), PIP 1 (bd neutral), 2–4 (I20N), ≥5 (bh Kontext), Chevron + PIP, MTP-I + PIP (bleibt I20N, kein I20M).
5. Rückfuß-Arthrodesen (`rfLabel`): A nur die Triple-DRG, B I13E/I20B je Schlüssel.
6. OSG-Arthrodese mit/ohne Spongiosa (I13D/I13E), AMIC mit/ohne IKO, Os Tib Ext mit/ohne MDO, Coalitio mit/ohne LCOT und < 12 J., Peronealsehnenluxation (`luxDrg` zur Laufzeit), Arthrorise < 18.
7. Calcaneoplastie (Haglund): I20O; Haglund + Bursektomie 5-859.19 (I27E, Ausweg nach 3i), Haglund + Tendoskopie 5-852.29 (I27E, Rang 129 < 135, Grouper 13.09.); ASK OSG mit Arthroskopiekodes (`{I20O: I59Z}`).
8. TMT-Arthrodese nach Gelenkzahl (a4–a8, 5-93b.e, 5-93b.0 bei TMT I, 5-784.0u, TMT 2 mit 5-784.1u + 5-783.2d) gegen `arthrodese_tmt1`/`arthrodese_tmt`/`arthrodese_tmt13` + Modifikator 4–5 Gelenke; Cotton autolog/allogen (5-781.4u + 5-784.0u/7u, kein Implantat, `hdrg` —); MDO + Cotton.
9. Metallentfernung, Achillessehne, diabetischer Fuß: bereits auf `steuerAnzeige` (Z. 5376, 5395, 5409); nur als Kontrollzeile mit „umgezogen", damit die Liste vollständig ist.
10. Feld `ziel` und `erloesText` (Z. 5434 ff.): im Fuß-OP-Bericht ohne Leser (Entscheidung 15.09.: bleibt bis 6b unsichtbar); in der Liste je Zweig vermerken, ob `ziel` noch etwas sagt, was nicht in `hinweise` steht, damit beim Umzug nichts verloren geht.

## Sollwerte

`hybrid-systematik.md` Abschnitt 5 (Repo-Root) ist die Sollwert-Tabelle, 29 Konstellationen, Stand 2026. Bitte je Zeile die Kodes, die ihr dafür verwendet (bei Text-Konstellationen wie „1× Hohmann" den Katalogkode aus `katalog2026.json` bzw. `HDRG_REGELN` nennen), durch `hdrgAuswertung` schicken und Soll gegen Ist ausgeben. Ergebnis als `hybrid_testfaelle.json` (Entwurf, Repo-Root; Felder je Fall: `nr`, `konstellation`, `codes`, `alter`, `seite`, `soll` {hdrg, drg}, `ist` {hdrg, drg}, `quelle`, `status`). Zeilen mit Jahresangabe 2024 nur mit dem 2026-Wert übernehmen. Die sechs Grouper-Läufe vom 13.09. stehen in Abschnitt 5 mit „WG 13.09.2026". Wo ein Sollwert nur mit einem Kode erreichbar ist, der in keiner App-Kodeliste vorkommt, das als `status: "kein App-Fall"` markieren, nicht raten.

## Ergänzungen a–f (für 6b, hier nur markieren)

Je Zeile eine Spalte „betrifft", in der steht, welche der Ergänzungen aus dem Umsetzungsplan den Zweig beim Umzug berührt: (a) Verdrängungsregel V2 in zwei Stufen statt `_prio`-Reihenfolge (Rangzahlen I20M 102, I20D 103, I27D 114, I20N 119, I20E 120, I27E 129, I59Z 130, I20O 135, I20F 136); (b) Seitenwahl beidseits; (c) Arthroskopie-Ausschlüsse I59Z, Hinweise Haglund/ASK OSG; (d) 5-854.29 kein Ausweg; (e) Hauptdiagnose schließt Fuß-Hybrid aus (diabetischer Fuß, Morton); (f) Fallsperre AKF08 vor der Kontextprüfung. Nichts davon jetzt bauen; nur zeigen, wo `_prio` heute anders entscheidet als die Rangzahl (Beispiel: Tendoskopie + MTP-I-Arthrodese → I20N, Rang 119 < 129).

## Ergebnisdateien

`abgleich-zweige-6a.md` (Repo-Root; Tabelle wie oben, nummerierte Zeilen, Spalte Entscheidung leer, am Ende Zählung gleich/toggle/abweichend/kein Eintrag), `scripts/verify_zweige_6a.py` (oder Erweiterung von `verify_zweige.py`, Aufruf ohne Parameter gegen die Arbeitskopie, Node-Aufruf für Spalte C eingeschlossen, Ausgabe zusätzlich als `out/abgleich_6a.json`), `hybrid_testfaelle.json` (Entwurf). Alle drei ins Repo, ein Commit; `app.html` und `data/` unverändert (bitte in der Vollzugsmeldung bestätigen, Prüfsumme `app.html` d3f63960…).

## Nichts anderes

Kein Umbau, keine Textänderung, keine Datenänderung, keine Bewertung „richtig/falsch" in der Liste; nur Befund. Wo ihr eine Entscheidung empfehlt, in einer eigenen Spalte „Anmerkung", kurz.

## Danach

Der Autor entscheidet je Zeile. Die Cowork-Sitzung trägt die Entscheidungen als Datenschritt in `opsteuerung.json` ein (Modifikatoren, neue Einträge für die drei Zweige ohne Eintrag, `hinweise`), nach Freigabe und Bucket-Upload durch den Autor. Dann 6b: Umstellung der Zweige auf `steuerAnzeige` + `hdrgAuswertung`, Verweildauer-Zeile und `kodier` stumm (dritter Teil, Punkte 1 und 5), Ergänzungen a–f, Gegenprobe mit `verify_zweige_6a.py` ohne ungeklärte Abweichung und `hybrid_testfaelle.json` ohne Fehlfall.

Vollzugsmeldung bitte mit Commit-Hash, Dateigrößen und der Zählung der Bewertungen.
