# Auftrag: EBM sauber kennzeichnen

## Das Problem

In der Fallsteuerung steht in der Ambulant-Karte derzeit zweimal dasselbe Zeichen mit zwei völlig verschiedenen Bedeutungen:

```
AMBULANT
H-DRG    —      ← Aussage: dieser Eingriff ist nicht H-DRG-fähig
EBM      —      ← Aussage: der EBM ist in der App nicht hinterlegt
```

Der erste Strich ist ein Ergebnis, der zweite eine Datenlücke. Wer das liest, kann den zweiten Strich als „ambulant über EBM nicht möglich" oder „keine Vergütung" verstehen, und das wäre fachlich falsch. Genau das soll ausgeschlossen werden.

## Aufgabe 1: app.html, Fallsteuerung

Die EBM-Zeile bekommt statt des Strichs einen knappen Vermerk. Statt zweizeilig (Label plus Strich) einzeilig, damit kein zusätzlicher Platz verbraucht wird, eher weniger:

```
EBM  nicht hinterlegt
```

Umsetzung: Label „EBM" wie bisher, an der Stelle des Werts der Text „nicht hinterlegt" in der kleinen, gedeckten Schrift, die auch für Nebenangaben verwendet wird (gleiche Größe und Farbe wie „Hybrid-DRG · pauschal" in der Chevron-Ansicht). Keine Klammer, kein Sternchen, kein Tooltip, keine Info-Schaltfläche. Ein Tooltip wäre am Telefon ohnehin nicht bedienbar.

Wichtig: Der Strich bei H-DRG bleibt unverändert, er ist ein echtes Ergebnis. Nur die EBM-Zeile wird angefasst. Wenn dieselbe EBM-Zeile an weiteren Stellen vorkommt, gilt die Änderung dort ebenso, damit die Kennzeichnung einheitlich ist.

Sonst ändert sich in der App nichts. Kein Erklärtext, kein Hinweisfeld, keine zusätzliche Zeile.

## Aufgabe 2: index.html, Beschreibungstext zur Fallsteuerung

In dem Feature-Block, der die Fallsteuerung beschreibt, wird der Zuschnitt beiläufig benannt. Anzuhängen an den vorhandenen Absatz:

> Gerechnet werden die stationären DRG und die Hybrid-DRG, also genau die Wege, an denen sich die Ambulantisierung entscheidet. Die vertragsärztliche Abrechnung nach EBM bildet Fuss-Track Clinic nicht ab.

## Aufgabe 3: index.html, neuer FAQ-Eintrag

In die bestehende Fragenliste aufnehmen, an das Ende der Fragen zum Funktionsumfang:

> **Ist die EBM-Abrechnung enthalten?**
> Nein. Die Erlössimulation rechnet mit den stationären DRG und den Hybrid-DRG. Für Leistungen, die ambulant über den EBM vergütet werden, zeigt die Fallsteuerung deshalb keinen Betrag. Das ist bewusst so: Der EBM ist eine eigene Welt mit eigenen Regeln, und ein halb gepflegter EBM-Teil wäre schlechter als keiner.

## Gegenprobe

In der App eine Ansicht mit nicht H-DRG-fähigem Eingriff öffnen, zum Beispiel die TN-Arthrodese. Prüfen: Der Strich steht nur noch bei H-DRG, die EBM-Zeile trägt den Vermerk, die Karte ist nicht höher geworden als vorher. Auf der Seite prüfen, dass der Absatz und der FAQ-Eintrag stehen und der Screenshot der Fallsteuerung weiterhin passt.

Nach dieser Änderung wird der Screenshot `bilder/screens/clinic-fallsteuerung.webp` neu aufgenommen, damit Bild und Anwendung übereinstimmen. Bis dahin bleibt das vorhandene Bild stehen, es ist inhaltlich nicht falsch.

Deploy wie üblich: Commit durch die Code-Sitzung, Push durch Benjamin nach Sichtprüfung.

## Nachtrag: vorhandene EBM-Hinweise beachten

In `app.html` stehen bereits mehrere ausformulierte EBM-Aussagen, unter anderem:

- „→ Ambulant: nur EBM-Abrechnung (unattraktiv) · stationäre Führung erwägen"
- „⚠ Ökonomisch unattraktiv — EBM-Erlös deckt klinischen Aufwand meist nicht."
- „Bei ambulanter Führung: Abrechnung per EBM möglich. Hierfür Auseinandersetzung mit EBM-Logik und Abrechnung nötig."

Diese Hinweise sind gut und bleiben. Sie zeigen aber, dass die Aussage „EBM ist möglich, wird hier nur nicht gerechnet" in der App bereits an mehreren Stellen steht — nur eben nicht dort, wo der Strich sitzt. Der neue Vermerk „nicht hinterlegt" muss deshalb sprachlich zu diesen Sätzen passen und darf ihnen nicht widersprechen. Wenn die Prüfung ergibt, dass in der betroffenen Karte einer dieser Hinweise ohnehin unmittelbar darunter erscheint, genügt es, den Strich durch den Vermerk zu ersetzen, ohne weiteren Text.
