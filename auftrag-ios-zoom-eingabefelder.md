# Auftrag: iOS-Safari zoomt beim Antippen von Eingabefeldern (OPS-Code Zuordnung und andere)

Stand: 07.09.2026. Quelle: Rückmeldung des Autors mit Screenshot (iPhone, OPS-Code Zuordnung 2026, Suchfeld angetippt: Seite ist hineingezoomt, der Suchen-Knopf rechts ist abgeschnitten, Titel läuft aus dem Bild, danach muss der Nutzer von Hand herauszoomen).

## Ursache

iOS Safari zoomt automatisch auf ein Eingabefeld, sobald dessen berechnete Schriftgröße unter 16 px liegt. Das betrifft `input`, `textarea` und `select`. Der Zoom bleibt nach dem Verlassen des Feldes bestehen.

## Gewünschte Lösung

Schriftgröße aller Eingabefelder auf mindestens 16 px setzen. Das ist die saubere Lösung; sie hält die Pinch-Zoom-Funktion für sehbehinderte Nutzer intakt. Bitte NICHT `user-scalable=no` oder `maximum-scale=1` in den Viewport-Meta-Tag setzen, das schaltet den Zoom für alle ab und gilt als Barrierefreiheitsverstoß.

Vorschlag als globale Regel in `app.html` (und, falls dort ebenfalls Eingabefelder liegen, in `index.html`):

```css
input, textarea, select { font-size: 16px; }
@media (min-width: 768px) { input, textarea, select { font-size: inherit; } }
```

Die zweite Zeile stellt auf dem Desktop die bisherige Größe wieder her, damit sich dort nichts verschiebt. Wo Felder im Desktop-Layout bewusst kleiner gesetzt sind (Score-Eingaben im Sprechstundenbrief, Zahlenfelder in der Fallsteuerung), bitte prüfen, ob 16 px auf dem Handy in die Zeile passen; sonst das Feld dort etwas breiter machen oder die Beschriftung darüber statt daneben setzen.

## Zusätzlich im Screenshot sichtbar

Im gezoomten Zustand läuft das Suchfeld samt Knopf über den rechten Rand. Das ist Folge des Zooms und verschwindet mit der Lösung oben. Falls das Suchfeld auf dem Handy auch ohne Zoom breiter als der Bildschirm ist (bitte einmal mit Safari-Simulator in 393 px Breite prüfen), Feld und Knopf als Flex-Zeile mit `min-width: 0` auf dem Feld setzen.

## Gegenprobe

iPhone, Safari: OPS-Code Zuordnung öffnen, Suchfeld antippen, Tastatur erscheint ohne Zoom, Suchen-Knopf bleibt sichtbar. Danach dasselbe im Sprechstundenbrief (Freitext- und Score-Felder) und im OP-Bericht-Generator (Freitext Präop). Pinch-Zoom muss weiterhin funktionieren.
