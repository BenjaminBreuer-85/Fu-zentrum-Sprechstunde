# Auftrag: ein Listenmuster für alle Auswahllisten in app.html

## Ausgangslage

Drei Werkzeuge listen heute auf drei verschiedene Arten:

| Werkzeug | heute |
|---|---|
| Aufklärungstexte | Akkordeon, Petrol-Versalien, Chevron rechts, keine Emojis |
| OP-Bericht-Generator | Akkordeon, Zeichen ► links, Emoji je Gruppe, gemischte Schreibweise |
| Sprechstundenbrief | flache Chip-Listen unter grauen Gruppenüberschriften, kein Aufklappen |

Sonst arbeitet die App ohne Emojis. Die Emojis in der OP-Durchführung sind der einzige Ort, an dem sie vorkommen, und sie tragen keine Information (zwei Gruppen haben denselben Fuß). Ziel: ein Muster, das alle drei bedient.

Die Vorlage liegt als `listenmuster.html` bei. Sie ist bedienbar: aufklappen, Chips wählen, Zähler beobachten.

## Das Muster

**Gruppenzeile** (`<summary>` oder gleichwertig)

- Text: Gruppenname in Versalien, `font-size:12.5px`, `font-weight:700`, `letter-spacing:.06em`, Farbe Petrol `#10535B`
- Zeile: `padding:13px 14px`, `display:flex`, `gap:10px`, Cursor Zeiger
- Rechts ein Pfeil: 9 × 9 px, zwei Kanten 2 px Petrol, `transform:rotate(-45deg)`, im geöffneten Zustand `rotate(45deg)`, Übergang 160 ms. Kein ►, kein ›-Zeichen aus dem Textsatz, kein Emoji.
- Geschlossen: Hintergrund `#fff`, linke Kante 3 px transparent
- Geöffnet: Hintergrund Tint `#E6F0F1`, linke Kante 3 px Petrol — das ist das Bausteinmotiv aus BRAND.md
- Hover: `#F6FAFA`

**Gruppenrahmen**: `border:1px solid #D6E2E3`, `border-radius:10px`, Abstand zwischen Gruppen 8 px, `overflow:hidden`.

**Zähler**: rechts vom Namen, nur sichtbar wenn in der Gruppe etwas ausgewählt ist. Pille, Höhe 20 px, Radius 10 px, Petrol-Fläche, weiße Ziffer, 11 px, fett. Er ist der Grund, warum das Zuklappen im Sprechstundenbrief nicht schadet: Ohne ihn sieht man nicht mehr, wo die Auswahl steckt.

**Körper**: `padding:12px 14px 14px`, obere Trennlinie `#D6E2E3`, Chips als `flex-wrap` mit `gap:7px`.

**Chip**: `border:1px solid #D6E2E3`, `border-radius:8px`, `padding:8px 12px`, `font-size:13.5px`, Farbe Tinte `#1D2421`, Hover Rahmen Petrol. Ausgewählt: Fläche Petrol, Rahmen Petrol, Schrift weiß.

**Abschnittsüberschrift** über einer Gruppenfolge (etwa „Diagnose(n)"): 11 px, fett, Versalien, `letter-spacing:.07em`, Farbe Grau `#5C6660`.

## Verhalten

- Mehrere Gruppen dürfen gleichzeitig offen sein. Kombinationseingriffe brauchen das im OP-Bericht.
- Beim Betreten der Seite sind alle Gruppen zu, außer es besteht bereits eine Auswahl; dann ist genau die betroffene Gruppe offen.
- Wird eine Gruppe geöffnet, scrollt ihr Kopf an den oberen Rand des sichtbaren Bereichs, damit der Inhalt nicht unter der Kopfzeile verschwindet.
- Beim Suchen (Aufklärungstexte) öffnen sich alle Gruppen mit Treffern, die übrigen bleiben zu.
- Tastatur: Die Gruppenzeile ist mit Tabulator erreichbar und mit Leertaste oder Eingabetaste schaltbar. Bei `<details>`/`<summary>` gilt das von selbst, was für diese Umsetzung spricht.

## Anwendung je Werkzeug

**Aufklärungstexte** — nur Feinschliff: Werte oben übernehmen, Pfeil ersetzen, Petrol-Linkskante und Tint im geöffneten Zustand ergänzen. Suchfeld bleibt.

**OP-Bericht-Generator** — Emojis entfernen, ► durch den Pfeil ersetzen, Gruppennamen in Versalien, Zähler ergänzen. Die Reihenfolge der Regionen bleibt.

**Sprechstundenbrief** — Umbau von flach auf Akkordeon. Die vorhandenen Gruppen (Vorfuß, Mittelfuß, Rückfuß und Fußform, Sprunggelenk, Sehnen und Faszien, Unspezifisch) werden zu Gruppenzeilen. Die Zeile „Anlass ohne neue Diagnose" mit Metallentfernung und Verlaufskontrolle bleibt **oberhalb und offen**, mit gestricheltem Chiprahmen — sie ist keine Diagnose, sondern öffnet einen anderen Weg. Bei Auswahl wird der Rahmen durchgezogen.

**Nicht anfassen**: die Dreizustands-Chips der klinischen Untersuchung und die Anweisungslisten im Kontroll-Flow. Dort werden mehrere Gruppen gleichzeitig bedient, und das Zuklappen würde die Arbeit verlangsamen.

## Gegenprobe

Bei 390 px Breite prüfen: Die Gruppenzeile bricht nicht um, lange Chips (Calcaneus-Verschiebeosteotomie) laufen nicht über den Rand, der Zähler bleibt rechts stehen. Danach je Werkzeug einen vollständigen Durchlauf: auswählen, zuklappen, Zähler prüfen, Text erzeugen. Ein Blick in den erzeugten Text stellt sicher, dass der Umbau nur die Oberfläche betrifft.

Deploy: nur `app.html`, kein Bucket-Upload. Commit durch die Code-Sitzung, Push durch Benjamin.


---

## Nachtrag 27.08.2026 — Live-Prüfung, Stand unverändert offen

Am heutigen `app.html`-Stand (716.903 Bytes) gegengeprüft: Alle drei Listen zeigen noch den alten Zustand (Sprechstundenbrief flach mit grauen Labels, OP-Bericht Akkordeon mit Emojis und ►, Aufklärung Akkordeon mit ›). Der Auftrag gilt unverändert, dazu drei Ergänzungen:

1. **Neue Gruppe im Sprechstundenbrief:** Seit der DF-Erweiterung gibt es zusätzlich die Gruppe „Diabetischer Fuß" (zwischen „Sehnen und Faszien" und „Unspezifisch"). Sie wird wie die anderen zur Gruppenzeile — die Aufzählung im Abschnitt „Anwendung je Werkzeug" ist entsprechend zu lesen.

2. **OP-Manuale einbeziehen:** Die Gruppenzeilen der OP-Manuale (🦿 OSG-Totalendoprothese, 🦵 OSG / Rückfuß, 🔩 Implantatsysteme, 📊 Unterlagen Abrechnung) nutzen dasselbe alte ►+Emoji-Muster. Sie bekommen das gleiche Gruppenzeilen-Design: Versalien, Pfeil rechts, Petrol-Linkskante im geöffneten Zustand, keine Emojis. Die Dokumentanzahl („7 Dokumente") bleibt als graue Angabe rechts stehen — sie ist eine feste Zahl, keine Auswahl, also KEINE Zähler-Pille.

3. **Ausdrücklich unverändert bleiben** weiterhin: die Dreizustands-Chips der klinischen Untersuchung, die Anweisungslisten im Kontroll-Flow — und die Emoji-Kacheln des Hauptmenüs, die ein eigenes, bewusstes Gestaltungselement sind und nicht Teil dieses Auftrags.

Gegenprobe nach Umsetzung zusätzlich: Sprechstundenbrief mit gewählter Diagnose „Diabetischer Fuß" öffnen — die Gruppe „Diabetischer Fuß" muss beim Betreten offen sein und die Zähler-Pille „1" tragen.
