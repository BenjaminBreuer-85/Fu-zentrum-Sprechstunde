# Auftrag: Zwei neue Bilder auf der Landingpage (index.html)

Stand: 27.08.2026. Freigegeben vom Autor. Die Dateien liegen bereits in `bilder/screens/` (je 1080×1350 plus 640er-Fassung):

- `au-1-risiken.webp` / `au-1-risiken-640.webp` — Aufklärungstexte: Eingriff „Chevron + Akin" gewählt, darunter der generierte Risikotext mit Kopie-Knopf.
- `sb-3-brief-qr.webp` / `sb-3-brief-qr-640.webp` — Schluss des generierten Sprechstundenbriefs: Kurzadresse `fuss-track.de/i/hallux-valgus`, Grußformel, QR-Block zur Patienten-App.

## 1. sb-3-brief-qr in den Abschnitt „Sprechstundenbrief in Minuten"

Der Bildstreifen dieses Abschnitts hat bisher `sb-1-eingabe` und `sb-2-untersuchung`. `sb-3-brief-qr` wird als **drittes Bild** angehängt. Es zeigt das Ergebnis (fertiger Brief) und die Brücke zur Patienten-App — die logische Reihenfolge ist Eingabe → Untersuchung → fertiger Brief.

Bildunterschrift (figcaption analog zu den bestehenden): „Der fertige Brief endet mit dem Code für die Patienten-App."

## 2. au-1-risiken einbauen

Die Aufklärungstexte haben auf der Seite bisher kein Bild. Einbau dort, wo der Werkzeugkasten-Abschnitt die Aufklärung erwähnt; falls es dafür keinen eigenen Bildstreifen gibt, als zweites Bild neben einem bestehenden Nachbar-Motiv einhängen — an der Stelle entscheiden, die ohne neuen Abschnitt auskommt. Keinen neuen Textblock dafür anlegen.

Bildunterschrift: „Risikoliste je Eingriff, mit einem Klick übernommen."

## 3. Technik

Gleiches Markup wie die bestehenden Streifenbilder: `<img>` mit `srcset` (640er- und Vollfassung), `loading="lazy"`, `width`/`height`-Attribute 1080/1350. Alt-Texte:

- au-1: „Aufklärungstexte: gewählter Eingriff Chevron plus Akin und generierte Risikoliste"
- sb-3: „Briefschluss mit Kurzadresse und QR-Code zur Patienten-App"

## Hinweis zum Bildinhalt au-1

Das Bild zeigt bewusst nur noch „Chevron + Akin" — der Solo-Eintrag „Chevron-Osteotomie" wurde am 27.08.2026 aus `data/aufklaerung.json` entfernt (siehe DEPLOY.md Abschnitt D, Upload offen). Das Bild passt also zum kommenden Datenstand.

## Deploy

Kein Bucket-Upload durch diesen Auftrag (nur `index.html` und bereits committete Bilder). Aber Achtung: unabhängig davon steht `data/aufklaerung.json` als offener Bucket-Upload in DEPLOY.md Abschnitt D.
