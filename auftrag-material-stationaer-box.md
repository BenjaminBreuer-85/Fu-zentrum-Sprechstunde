# Auftrag: Zeile „Materialkosten: unvollständig" auch in der Stationär-Box der Fallsteuerung

Stand 16.09.2026, Cowork-Sitzung, Entscheidung des Autors 16.09.2026 („ja"). Ausgangsstand: `app.html` nach dem Auftrag `auftrag-material-modifikatoren.md` (789.220 Byte, Arbeitskopie vom 16.09.2026 12:39 CEST). Ein Commit, eine Vollzugsmeldung. Kein Datenschritt.

## Befund

In der Fallsteuerung des Sprechstundenbriefs zeigt die Ambulant-Box bei einem Materialsatz mit fehlendem Preis die Zeile „Materialkosten: unvollständig — n von m Positionen ohne Preis" mit dem Sprung „Preise hinterlegen" (`setTool("preise")`, Z. 3427). Die Stationär-Box (Z. 3455 ff.) hat diese Zeile nicht: sie zeigt Material nur bei fertigem Betrag (`implZahl>0`, Z. 3472–3475). Bei Eingriffen, die nur stationär möglich sind (Tarsale Koalition, OSG-Arthrodese, OSG-TEP, Arthrodesen des Rückfußes), steht bei fehlendem Preis oben nur die DRG ohne Materialkosten und ohne „DB II (real)"; der Grund ist erst in der Materialliste weiter unten zu sehen („unvollständig — n ohne Preis"), und der Sprung ins Preiswerkzeug fehlt dort. Bestand seit Einführung der Materialkosten, unabhängig vom Auftrag zu den Modifikatoren (Prüfstand-Bericht Abschnitt 20, Befund a).

## Änderung

In der Stationär-Box direkt hinter dem Block `{implZahl>0&&…}` (Z. 3472–3475) dieselbe Zeile wie in der Ambulant-Box einfügen, mit dem Abstand der Stationär-Box (`marginTop:6`):

```
{implUnvoll&&<div style={{fontSize:10,color:"#8A5A00",marginTop:6,paddingTop:4,borderTop:"1px solid rgba(0,77,64,.1)"}}><span style={{fontWeight:600}}>Materialkosten:</span> unvollständig — {implUnvoll.fehlend} von {implUnvoll.positionen} Positionen ohne Preis <span style={{textDecoration:"underline",cursor:"pointer"}} onClick={()=>setTool("preise")}>Preise hinterlegen</span></div>}
```

`implUnvoll` ist in diesem Geltungsbereich bereits definiert (Z. 3408) und ist bei gesperrtem Konto (`implGesperrt`) immer null; die Kontosperre bleibt also die einzige Meldung, wenn der Abruf fehlschlägt. Sonst nichts: keine Änderung an `implKostenFuer`, an der Materialliste, am Preiswerkzeug oder an den Texten der Ampel.

## Abnahme

Cowork-Prüfstand: Sprechstundenbrief-Referenz (`baseline_sb_3n2.json`, 19 Diagnosen, 83 OP-Fälle). Auf dem Prüfstand gibt es keine Preisliste, `implUnvoll` ist deshalb bei jedem Eingriff mit Materialsatz gesetzt; erwartete Abweichung zur Referenz ist genau die neue Zeile in den Stationär-Boxen dieser Fälle, sonst nichts (die Cowork-Sitzung weist die Abweichung je Fall aus). Brieftexte zeichengleich. Mit Testpreisen ohne Fräser-Preis: Tarsale Koalition, Coalitio TC, „+ MDO" → Stationär-Box zeigt „I20C", darunter „Materialkosten: unvollständig — 1 von 2 Positionen ohne Preis" und „Preise hinterlegen"; Klick öffnet das Werkzeug Implantatpreise. Mit vollständigen Preisen unverändert „Materialkosten: 285,00 €" mit Ampel. Ambulant-Box unverändert. Keine Konsolenfehler.

Abnahme des Autors am Handy: Sprechstundenbrief, Rückfuß und Fußform, Tarsale Koalition, Coalitio TC, „+ MDO"; im Werkzeug Implantatpreise vorher den Preis des MIS-Fräsers leeren; in der Stationär-Box erscheint die Zeile mit „Preise hinterlegen", Tippen führt ins Preiswerkzeug, Preis eintragen, zurück zum Brief: „Materialkosten: … €" mit Ampel.

Vollzugsmeldung bitte mit Commit-Hash und der Zeilennummer der Einfügung.
