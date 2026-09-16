# Auftrag: Materialkosten der Zusatzeingriffe (Modifikatoren) im Sprechstundenbrief

Stand 16.09.2026, Cowork-Sitzung, Entscheidung des Autors 16.09.2026. Ausgangsstand: `app.html` Commit a0a93b2. Ein Commit, eine Vollzugsmeldung. Kein Datenschritt in diesem Auftrag: das neue Datenfeld schreibt die Cowork-Sitzung (Schritt 3p, `data/opsteuerung.json`, lokal und Bucket).

## Befund

Im Sprechstundenbrief zeigt die Fallsteuerung bei „Tarsale Koalition" mit gesetztem Zusatzeingriff „+ LCOT" oder „+ MDO" die Zeile „keine Materialkosten hinterlegt", obwohl die Materialsätze in `zuordnung/implantat_zuordnung.json` vorhanden sind (`EINGRIFFE.coalitio_lcot` „mit LCOT": 1 allogener Knochenblock; `EINGRIFFE.mdo_mini` „minimalinvasiv": 2 Kompressionsschrauben 7,0 kopflos + 1 MIS-Fräser 2,2). Ursache: die Fallsteuerung holt das Material nur über `implKostenFuer(bestKey)` (Z. 3383), und diese Funktion liest ausschließlich `MAPPING_OPS[bestKey]` (Z. 975–980). Die aktiven Zusatzeingriffe (`best._mods`, gesetzt in `opSteuerungEff` Z. 1574) werden beim Material nirgends berücksichtigt; dasselbe gilt für die Materialliste unter der Fallsteuerung (Z. 3588–3591, `MaterialsatzAnsicht` mit `MAPPING_OPS[bestKey]`). Für `coalition_tc`/`coalition_cn` gibt es keinen `MAPPING_OPS`-Eintrag, und das ist richtig: die Resektion mit Faszien-Fett-Lappen braucht kein Implantat. Das Material kommt erst mit dem Zusatzeingriff.

Der OP-Bericht-Generator löst das heute im Code (`if(coalLCOT)PZ("coalitio_lcot","mit LCOT")`, Z. 4704). Im Brief soll es datengetrieben laufen, wie DRG, Kodes und Text der Modifikatoren.

## Neues Datenfeld (schreibt die Cowork-Sitzung, Schritt 3p)

Jeder Modifikator in `OP_STEUERUNG[key].modifikatoren` kann optional `material: [eingriffId, variante]` tragen, gleiches Format wie ein `MAPPING_OPS`-Eintrag (`eingriffId` aus `EINGRIFFE`, `variante` ein Schlüssel von `varianten`). Stand nach 3p:

```
coalition_tc / coalition_cn:
  lcot, lcot_u12: "material": ["coalitio_lcot", "mit LCOT"]
  mdo,  mdo_u12:  "material": ["mdo_mini", "minimalinvasiv"]
```

Alle übrigen Modifikatoren haben kein Feld; für sie ändert sich nichts.

## Änderung im Code

1. `implKostenFuer(opsKey)` (Z. 975) bekommt einen zweiten Parameter `mods` (die Liste `best._mods`, ggf. leer). Positionsliste = `MATPOS(MAPPING_OPS[opsKey][0], [1])` (falls Eintrag vorhanden) plus, je aktivem Modifikator mit `material`, `MATPOS(m.material[0], m.material[1])`. Reihenfolge: Grundeingriff zuerst, dann die Modifikatoren in Listenreihenfolge. Aus der Liste wird der Betrag nach genau der Regel von `paketPreis` (Z. 981–990) gebildet: Konto nicht bereit → `{nichtGeladen}`; keine Position → wie bisher `0`; eine Position ohne Preis → `{unvollstaendig, fehlend, positionen}`; sonst Summe auf Cent gerundet. Am einfachsten: `paketPreis` um eine Fassung ergänzen, die eine fertige Positionsliste nimmt, und `implKostenFuer` darauf aufsetzen; `MATPOS` selbst bleibt unverändert.
2. Aufruf Z. 3383: `implKostenFuer(bestKey, best._mods)`.
3. Materialliste Z. 3588–3591: statt `eingriffId`/`variante` aus `MAPPING_OPS` dieselbe kombinierte Positionsliste als `positionen` an `MaterialsatzAnsicht` geben (der Weg besteht schon, Z. 4155; der OP-Bericht nutzt ihn Z. 6404). Ohne Positionen bleibt „keine Materialkosten hinterlegt".
4. Nichts anderes: `implAmpel`, „DB II (real)" (Z. 3484 ff.) und die Materialzeilen der Ambulant-/Stationär-Box (Z. 3406 f., 3450 f.) rechnen mit `implZahl` weiter und zeigen den Betrag dann von selbst.

Ein unbekanntes `material`-Feld darf der Code an keiner anderen Stelle auswerten; ein Modifikator ohne `material` bringt kein Material. Ein `material`-Eintrag, dessen `eingriffId` in `EINGRIFFE` fehlt, liefert über `MATPOS` eine leere Liste; das ist gewollt (kein Absturz), ein Hinweis in der Konsole reicht.

## Abnahme

Cowork-Prüfstand (`baseline_sb_3n2.json`, 81 Sprechstundenbriefe): alle Briefe ohne gesetzten Modifikator zeichengleich, ebenso alle Fälle mit Modifikator ohne `material`. Neu: „Tarsale Koalition", Chip Coalitio TC oder CN, Toggle „+ LCOT" → Materialkosten = Preis des allogenen Knochenblocks aus der Preisliste, Ampel und „DB II (real)" gegen I20C; Toggle „+ MDO" → Summe aus 2 × Kompressionsschraube 7,0 kopflos + 1 × MIS-Fräser 2,2; Toggle „+ MDO, Alter unter 12 Jahren" dasselbe gegen I20B; ohne Toggle weiterhin „keine Materialkosten hinterlegt". Fehlt ein Preis in der Nutzerliste: „Materialkosten: unvollständig — n von m Positionen ohne Preis" mit dem Sprung „Preise hinterlegen". Keine Konsolenfehler. Abnahme des Autors am Handy: Sprechstundenbrief, Tarsale Koalition, Coalitio TC, „+ MDO" setzen, Materialkosten und DB II (real) sichtbar; Toggle wieder lösen, Zeile verschwindet.

Vollzugsmeldung bitte mit Commit-Hash, den geänderten Zeilennummern und der Angabe, ob `paketPreis` erweitert oder eine neue Hilfsfunktion angelegt wurde.
