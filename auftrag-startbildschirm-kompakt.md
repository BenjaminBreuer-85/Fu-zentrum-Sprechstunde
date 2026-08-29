# Auftrag: Startbildschirm auf eine Bildschirmhöhe stauchen (app.html)

Stand: 29.08.2026. Beobachtung des Autors am iPhone: Der Startbildschirm passt fast, aber nicht ganz auf den Schirm — man muss minimal scrollen, um Kopfbereich bzw. Fußzeile zu sehen.

## Messung

Bei 393 × 852 (iPhone-Viewport) ist die Menüseite derzeit **876 px** hoch — 24 px zu viel. Mit Safari-Leisten ist der sichtbare Bereich real noch kleiner. Ziel: Gesamthöhe **≤ 840 px** bei 393 px Breite, damit auch bei 390 × 844 nichts abgeschnitten wird.

## Was zu tun ist

Rund 40–60 px Höhe einsparen, ohne Kacheln zu verkleinern, dass sie schwerer tippbar würden. Sinnvolle Hebel, in dieser Reihenfolge, bis das Ziel erreicht ist:

1. **Bilderleiste oben** (die fünf Kopfbilder): Höhe reduzieren (z. B. Kachelgröße der Bilder um ~15–20 % kleiner) und die Abstände darüber/darunter halbieren.
2. **Vertikale Abstände**: Lücke zwischen Titelblock und erster Kachelreihe sowie zwischen den Kachelreihen um je 2–4 px verringern.
3. **Kachel-Innenabstand**: padding oben/unten je 2–3 px kleiner; Icon-Größe minimal reduzieren, Untertitel bleiben zweizeilig erlaubt.
4. **Fußzeile hochsetzen**: Impressum · Datenschutz · Nutzungsbedingungen (und „Abmelden") mit kleinem festen Abstand direkt unter die letzte Kachel bzw. die Patient-App-Zeile setzen, statt mit großem Leerraum.

Kein Zoom-/Skalierungstrick (kein transform: scale auf den ganzen Inhalt) — echte Abstände anpassen, damit Schriftgrößen und Tippziele unverändert lesbar bleiben.

## Zusätzlich: Kachel-Untertitel Sprechstundenbrief ändern

Der gerade erst gesetzte Untertitel „Arztbriefe mit Scores und Kopierfunktion" wird auf Wunsch des Autors ersetzt durch:

> Modulare Brieferstellung mit Kosten- und Erlössimulation

(Wortlaut des Autors; der Bindestrich in „Kosten- und Erlössimulation" ist die grammatisch richtige Kopplung — falls der Autor bewusst „Kosten und Erlössimulation" ohne Bindestrich will, gilt sein Wortlaut.)

## Gegenprobe

Headless bei 393 × 852 und 390 × 844: `document.documentElement.scrollHeight <= window.innerHeight` auf der Menüseite (nach Wegklicken der Tour). Zusätzlich Sichtprüfung: keine Kachel wirkt gequetscht, Untertitel nicht abgeschnitten (auch der neue zweizeilige SB-Untertitel), Desktop-Ansicht unverändert wohlproportioniert.

## Deploy

Kein Bucket-Upload. Nur `app.html` ändern, committen, pushen.
