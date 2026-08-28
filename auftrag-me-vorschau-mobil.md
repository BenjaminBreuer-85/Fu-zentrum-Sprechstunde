# Auftrag: Brief-Vorschau mobil für Metallentfernung und Verlaufskontrolle (app.html)

Stand: 28.08.2026. Fund A1 aus dem Voll-Audit, vom Autor zur Umsetzung freigegeben.

## Problem

Im Sprechstundenbrief-Modul liegt die mobile Vorschau-/Export-Karte (`<div className="sb-mobile-preview" data-tour="sb-export">`, derzeit ~Zeile 3313) **innerhalb** des Blocks

```jsx
{gender && (diagnosen.length > 0 || (pfad === "endo" && endoDiag)) && !meMode && !kontrolleMode && <div>
```

(~Zeile 3004). In Metallentfernungs- und Verlaufskontroll-Modus ist dieser Block per Definition aus — unterhalb von 1024 px gibt es dadurch **keine Möglichkeit, den Brief anzusehen oder zu kopieren**. Das Desktop-Panel (`sb-split`, rechte Spalte) liegt außerhalb und funktioniert.

*Repro:* 393 px Breite → Sprechstundenbrief → Herr, Links → Metallentfernung → Region „Metatarsale", Implantat „Schraube", Zeitraum „Monaten" → keine „Vorschau & Export"-Karte. Gleiches Bild in der Verlaufskontrolle nach Anlass-Wahl.

## Was zu tun ist

1. Die mobile Vorschau-Karte aus dem Bedingungsblock herauslösen (oder die Bedingung erweitern), sodass sie auch erscheint, wenn `meMode` bzw. `kontrolleMode` aktiv ist und die jeweiligen Mindestangaben gesetzt sind — dieselbe Logik, mit der das Desktop-Panel seinen Text erzeugt (`fullText`). Kein neues Verhalten erfinden: Karte zeigen, sobald das Desktop-Panel einen Brief zeigt.
2. Sichtprüfung beider Modi bei 393 px UND am Desktop; der Normalmodus (Diagnose gewählt) darf sich nicht verändern.
3. Tippfehler im ME-Brieftext gleich mitnehmen: „Aktuell berichtet der patient über lokale Beschwerden…" → „der Patient" (Großschreibung; Textquelle in app.html, ME-Briefgenerator).

## Deploy

Kein Bucket-Upload. Nur `app.html` ändern, committen, pushen.
