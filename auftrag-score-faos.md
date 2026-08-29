# Auftrag: FAOS statt AOFAS + Scores-Zeile schaltbar machen (app.html)

Stand: 29.08.2026. Entscheidung des Autors. **Dieser Auftrag ersetzt den Punkt C2 aus auftrag-audit-c.md sowie Punkt 1 aus auftrag-gegenprobe-nachzuegler.md** — die dort gewünschte Lösung „Zeile nur bei eingetragenem Wert" entfällt, weil der Sprechstundenbrief bewusst keine Score-Eingabefelder hat (die Werte werden in iMED1 eingetragen). Stattdessen gilt das Folgende.

## 1. AOFAS durch FAOS ersetzen

Der AOFAS-Score wird in der App nicht mehr verwendet; an seine Stelle tritt der FAOS (Foot and Ankle Outcome Score) als Gesamtwert von 0 bis 100. AOFAS kommt in app.html an genau zwei Stellen vor, beide werden geändert:

1. Die Brief-Zeile
   `p.push("\n- Scores: EFAS /24, EFAS Sport /16, AOFAS /100, VAS Belastung /10");`
   wird zu
   `- Scores: EFAS /24, EFAS Sport /16, FAOS /100, VAS Belastung /10`
2. Der Tour-Text „…EFAS, EFAS Sport, AOFAS und die VAS unter Belastung…" wird zu „…EFAS, EFAS Sport, FAOS und die VAS unter Belastung…". Der restliche Satz (iMED1-Hinweis) bleibt unverändert, sofern Punkt 2 unten ihn nicht ohnehin anpasst.

Sonst gibt es keine AOFAS-Vorkommen — bitte nach der Änderung per Suche über die ganze Datei gegenprüfen (case-insensitiv „AOFAS"), es darf kein Treffer übrig bleiben.

## 2. Scores-Zeile hinter einen Schalter legen, Standard: AUS

Die Scores-Zeile ist ein Ausfüll-Stub für iMED1 und wird nur von einem Teil der Nutzer gebraucht. Deshalb:

- Im Sprechstundenbrief einen **An/Aus-Schalter „Scores-Zeile"** einführen, gestaltet wie die vorhandenen Options-Chips/-Toggles des SB (gleiche Optik, gleiche Interaktion), platziert bei den übrigen Brief-Optionen vor der Vorschau.
- **Standardzustand: AUS.** Ohne Zutun des Nutzers erscheint im Brief keine Scores-Zeile.
- Bei eingeschaltetem Schalter erscheint die Zeile unverändert als Ausfüll-Stub:
  `- Scores: EFAS /24, EFAS Sport /16, FAOS /100, VAS Belastung /10`
- Der Schalter gilt für alle Briefarten, in denen die Zeile heute gedruckt wird (Erstvorstellung/Diagnose-Briefe); ME- und Kontroll-Briefe bleiben wie sie sind, falls sie die Zeile heute nicht führen.
- Der Zustand darf sitzungsintern gemerkt werden (wie andere SB-Optionen), muss aber bei jedem Neuladen wieder AUS sein — kein dauerhaftes Speichern nötig.

## 3. Tour-Text anpassen

Da die Zeile jetzt standardmäßig fehlt, muss der Tour-Schritt zu den Scores den Schalter erklären, sinngemäß: Über den Schalter „Scores-Zeile" lässt sich eine Ausfüllzeile mit EFAS, EFAS Sport, FAOS und der VAS unter Belastung in den Brief aufnehmen; die Punktwerte selbst trägt man in iMED1 ein. (Formulierung bitte an den bestehenden Tour-Stil anpassen, kein Gedankenstrich-Stakkato.)

## Gegenprobe

1. SB → Herr, Links → Hallux valgus → Anzeigen: Brief **ohne** Scores-Zeile.
2. Schalter „Scores-Zeile" einschalten → Anzeigen: Zeile erscheint mit „FAOS /100", ohne „AOFAS".
3. Volltextsuche über app.html: kein „AOFAS" mehr (case-insensitiv).
4. Schalter wieder ausschalten → Zeile verschwindet; Neuladen der App → Schalter steht wieder auf AUS.

## Deploy

Nur `app.html` ändern, committen, pushen. Kein Bucket-Upload.
