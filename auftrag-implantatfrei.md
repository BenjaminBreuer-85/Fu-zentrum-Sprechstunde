# Auftrag Clinic: Eingriffe ohne Implantat in der Stationär-Box („kein Implantat" statt „nicht berechenbar")

Stand 20.09.2026, Cowork-Sitzung. Entscheidung des Autors 20.09.2026 (G8, „2b"): Eingriffe ohne Implantat bekommen in `opsteuerung.json` das Feld `implantatfrei: true`; die Stationär-Box zeigt dann „kein Implantat" und rechnet die DB II (real) mit 0 € Material. Datei `app.html`, Ausgangsstand Commit c6f3732 (802.645 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Datenteile 3w (`zuordnung/implantat_zuordnung.json`, neun neue Mappings) und 3x (`opsteuerung.json`, Feld `implantatfrei` an 20 Eingriffen) schreibt die Cowork-Sitzung nach Freigabe; der heutige Code ignoriert das Feld, die Daten können vor oder nach dem Code raus.

## Befund

Seit 52d9383 liefert `implKostenFuer` (Z. 992–1000) ohne Materialsatz `null`, die Box zeigt „⚪ DB II (real) nicht berechenbar — keine Materialkosten hinterlegt" (Z. 3653). Für Eingriffe, die kein Implantat brauchen (Morton, Exostose, Cheilektomie, Gastrocnemius, Sehnennähte, Débridements, Amputation, Coalitio ohne Zusatz, 20 Einträge), ist das unnötig: die DB II (real) wäre mit 0 € richtig, und die InEK-Implantatreferenz entfällt zugunsten des Falls.

## Änderung

1. `implKostenFuer` (Z. 997): vor dem `return null` prüfen, ob der Eingriff implantatfrei ist und kein Modifikator mit `material` aktiv ist:

```
var e = OP_STEUERUNG[opsKey];
if (!m && !mitMaterial) return (e && e.implantatfrei === true) ? 0 : null;
```

Mit aktivem Materialmodifikator (Coalitio „+ LCOT", „+ MDO") gilt der Modifikator-Satz wie heute; `implantatfrei` wirkt nur ohne Zusatz. (`OP_STEUERUNG` ist die Konstante aus Z. 1344; `implKostenFuer` steht davor in der Datei, wird aber erst zur Laufzeit aufgerufen, wenn die Konstante gebunden ist.)

2. Stationär-Box, Materialzeile (Z. 3581, Bedingung `implZahl>0`): bei `implZahl === 0` und implantatfreiem Eingriff statt der Betragszeile die Zeile „Materialkosten: kein Implantat" im selben Stil (Z. 3581 f., ohne Ampel; `implAmpel` liefert bei `ist = 0` ohnehin `null`, Z. 1328). Dieselbe Zeile in der Ambulant-Box (Z. 3537, gleiche Bedingung).

3. DB II (real) (Z. 3619 ff.): `hasRealImpl` ist bei `implZahl === 0` schon wahr, `dbIIReal = dbII + inekImpRef`. Text in diesem Fall (neuer erster Zweig vor Z. 3623): `dbRealAmpel = "🟢"`, `dbRealText = "kein Implantat, InEK-Implantatreferenz von " + inekImpRef + " € entfällt"` (Betrag mit `toLocaleString("de-DE")`). Formelzeile Z. 3646 bleibt (zeigt „− 0,00 €"). Der Kasten Z. 3653 („nicht berechenbar") erscheint bei `implZahl === 0` nicht (Bedingung `implZahl===null` bleibt).

4. Kleine Hilfsfunktion, damit die drei Stellen dieselbe Prüfung nutzen: `function implantatfrei(opsKey, mods){ var e=OP_STEUERUNG[opsKey]; return !!(e&&e.implantatfrei===true) && !(mods||[]).some(function(mo){ return mo&&Array.isArray(mo.material); }); }`.

## Nichts anderes

`paketPreisAusPositionen`, `materialPositionenFuer`, Materialsatz-Ansicht, Preiswerkzeug, OP-Bericht unverändert. Eingriffe mit Materialsatz, aber ohne Preise zeigen weiter „unvollständig — n von m Positionen ohne Preis".

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3w.json`, Stand c6f3732, mit 3w- und 3x-Daten): Briefe zeichengleich. Fallsteuerung: bei den 20 implantatfreien Eingriffen „Materialkosten: kein Implantat" und „🟢 DB II (real): … − 0,00 € = …" mit dem Text zur entfallenden Referenz; bei den neun neu gemappten Eingriffen (Dwyer, Lambrinudi, Weil, FDL-Transfer, Youngswick, TMT-I, TMT I–III, OATS, Kidner) ohne Preise „unvollständig — n von m Positionen ohne Preis" mit „Preise hinterlegen", mit Testpreisen Ampel und DB II (real); alle übrigen Fälle gleich. Coalitio TC ohne Zusatz „kein Implantat", mit „+ LCOT" und Testpreis wie bisher (250 € → grün). Keine Konsolenfehler, Selbsttest unverändert.

Abnahme des Autors am Handy: Hallux valgus → Exostosenabtragung → Erlössimulation: „Materialkosten: kein Implantat", DB II (real) grün mit „Referenz … entfällt". Hohlfuß → Dwyer-Osteotomie: „Materialkosten: unvollständig — 1 von 1 Positionen ohne Preis" (bis Preise hinterlegt sind).

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern.
