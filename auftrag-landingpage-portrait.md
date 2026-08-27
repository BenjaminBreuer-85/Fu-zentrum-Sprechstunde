# Auftrag: Porträt-Platzhalter im Autor-Abschnitt (index.html, Landingpage)

Stand: 27.08.2026. Kleiner Einzelauftrag, unabhängig von Runde 3.

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
