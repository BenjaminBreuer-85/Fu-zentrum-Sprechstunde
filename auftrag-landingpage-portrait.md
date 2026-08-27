# Auftrag: Porträt-Platzhalter im Autor-Abschnitt (index.html, Landingpage)

Stand: 27.08.2026, erneut abgelegt am Abend. Kleiner Einzelauftrag, unabhängig von Runde 3.

## Zum Auffinden

Diese Datei liegt im **Repo-Root** von `Fu-zentrum-Sprechstunde`, direkt neben `auftrag-landingpage-texte-runde4.md` und `auftrag-landingpage-bilder-au-sb.md`:

```
/Users/benjaminbreuer/Desktop/GitHub/Fu-zentrum-Sprechstunde/auftrag-landingpage-portrait.md
```

Sie wurde am 27.08. um 06:36 zum ersten Mal geschrieben. Falls sie in einer früheren Sitzung nicht sichtbar war, lag das vermutlich daran, dass sie noch nicht committet war — jetzt bitte einfach im Repo-Root nachsehen. Das benötigte Bild `icons/icon-512.png` liegt bereits im Repo, es muss nichts heruntergeladen werden.

Hinweis: Auf der Patienten-Landingpage (Repo Fuss-Track) ist derselbe Platzhalter-Tausch bereits direkt umgesetzt — dieser Auftrag betrifft nur die Clinic-Landingpage.

## Was zu tun ist

In `index.html` (Landingpage fuss-track.de), Abschnitt `<section class="author">`:

Der bisherige Text-Platzhalter

```html
<div class="portrait">Porträtfoto<br>Dr. med. Benjamin Breuer<br>(wird ergänzt)</div>
```

wird vorerst durch das App-Icon ersetzt:

```html
<div class="portrait portrait-logo">
  <img src="icons/icon-512.png" alt="Fuss-Track Clinic – Logo" width="512" height="512" loading="lazy">
</div>
```

Dazu CSS ergänzen (an den bestehenden `.portrait`-Stil anpassen, Werte sinngemäß):

```css
.portrait-logo { display:flex; align-items:center; justify-content:center; background:#E6F0F1; }
.portrait-logo img { width:70%; height:auto; max-width:220px; }
```

Wichtig: Das Icon ist ein **vorläufiger** Platzhalter, bis ein echtes Porträtfoto vorliegt.
Die bestehende Form des Platzhalters (Rahmen, Rundung, Größe) beibehalten, nur der Inhalt wechselt vom Text zum Logo. Kein Kommentar im sichtbaren Text mehr („wird ergänzt" entfällt).

## Deploy

Kein Bucket-Upload. Nur `index.html` ändern, committen, pushen.
