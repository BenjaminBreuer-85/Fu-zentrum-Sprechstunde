# Auftrag Clinic (Backlog G10): Materialsatz-Ansicht bei implantatfreien Eingriffen

Stand 22.09.2026, Cowork-Sitzung. Anlass: Gegenprobe zu Commit 664f9fd (Bericht Abschnitt 29). Seit dem implantatfrei-Auftrag zeigt die Stationär-Box bei den 20 implantatfreien Eingriffen „Materialkosten: kein Implantat" und rechnet die DB II (real) grün; direkt darunter steht aber weiter die Materialsatz-Ansicht mit „keine Materialkosten hinterlegt", was neben „kein Implantat" widersprüchlich wirkt. Datei `app.html`, Ausgangsstand Commit f9fc66b (803.643 Byte, Zeilenangaben darauf; der Commit 7a63ddb ändert nur den OP-Bericht-Kodeblock ab Z. 4983, die Stellen hier liegen davor und sollten unverändert sein). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

`MaterialsatzAnsicht` (Z. 4331 ff.) zeigt bei leerer Positionsliste im Nur-Lese-Modus (Z. 4380–4385, Bedingung `!zeilen.length && !istModus`) den Kasten „keine Materialkosten hinterlegt", im OP-Bericht (`readOnly={false}`) zusätzlich den Link „tatsächliche Versorgung erfassen". Die Komponente weiß nicht, ob der Eingriff implantatfrei ist; sie bekommt nur `positionen`. Aufrufe: Sprechstundenbrief Z. 3740 (`readOnly={true}`, `positionen={materialPositionenFuer(bestKey, best._mods)}`), OP-Bericht Z. 6587 (`positionen={materialKosten}`, bearbeitbar). Die Stationär-Box entscheidet an drei Stellen selbst über `implantatfrei(bestKey, best._mods)` (Z. 3544, 3588, 3633).

## Änderung

1. `MaterialsatzAnsicht` bekommt eine neue optionale Eigenschaft `implantatfrei` (boolean). Im Leerzustand (Z. 4380 ff.):

```
if (!zeilen.length && !istModus) {
  return <div style={{…wie bisher…}}>
    {implantatfrei ? "kein Implantat vorgesehen" : "keine Materialkosten hinterlegt"}
    {!readOnly && <span onClick={()=>setFall([])} …>tatsächliche Versorgung erfassen</span>}
  </div>;
}
```

Der Erfassungslink bleibt in beiden Fällen (im OP-Bericht), damit Ausnahmen, etwa ein Anker bei einer Sehnennaht, weiterhin erfasst werden können.

2. Sprechstundenbrief Z. 3740: `implantatfrei={implantatfrei(bestKey, best._mods)}` mitgeben.

3. OP-Bericht Z. 6587: Der OP-Bericht kann mehrere Eingriffe enthalten; `implantatfrei` ist dort wahr, wenn alle gewählten Abrechnungs-Eingriffe implantatfrei sind und keine Positionen vorliegen. Falls die Zuordnung OP-Bericht-Chip → `OP_STEUERUNG`-Schlüssel dort nicht ohne Weiteres verfügbar ist, Punkt 3 auslassen und in der Vollzugsmeldung sagen; dann bleibt der OP-Bericht bei „keine Materialkosten hinterlegt", was dort ohnehin neben dem Erfassungslink steht.

## Nichts anderes

`implKostenFuer`, Stationär-Box, DB II (real), Preiswerkzeug, Materialsätze unverändert.

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3w.json` mit 3w/3x/3y/3z-Daten, Stand f9fc66b/7a63ddb): Briefe zeichengleich; Fallsteuerung bei den 31 implantatfreien Fällen gleich bis auf die Zeile „kein Implantat vorgesehen" statt „keine Materialkosten hinterlegt"; bei den 12 „unvollständig"-Fällen und allen übrigen unverändert. Keine Konsolenfehler, Selbsttest unverändert.

Abnahme des Autors am Handy: Hallux valgus → Exostosenabtragung → Erlössimulation: unter der Box „kein Implantat vorgesehen".

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern.
