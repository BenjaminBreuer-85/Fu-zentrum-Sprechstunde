# Bildmaterial Fuss-Track — Übersicht

Stand: 27.08.2026. Alle Dateien in `bilder/screens/`.

## A) Landingpage: Einzelbilder für die Bildstreifen

Format **1080 × 1350 (4 : 5)** als WebP, dazu je eine 640er-Fassung (`…-640.webp`). Es sind Ausschnitte, keine verkleinerten Vollbilder — die Beschriftungen bleiben lesbar. Statusleisten, Adresszeilen und eingeblendete Bedienelemente sind entfernt.

| Datei | Inhalt | Abschnitt |
|---|---|---|
| `sb-1-eingabe` | Eingabemaske mit Anlass und gruppierten Diagnosen | Sprechstundenbrief |
| `sb-2-untersuchung` | Klinische Untersuchung mit Dreizustands-Chips | Sprechstundenbrief |
| `ob-1-auswahl` | OP-Durchführung, Eingriffsauswahl Rückfuß | OP-Bericht |
| `ob-2-vorschau` | Materialsumme, InEK-Referenz, fertiger Berichtstext, Word-Export | OP-Bericht |
| `fs-1-chevron` | Chevron-Osteotomie, ambulant gegen stationär | Fallsteuerung |
| `fs-2-tn` | TN-Arthrodese, Belegungstage und Deckungsbeitrag | Fallsteuerung |
| `kl-1-liste` | Klassifikationsliste mit Filtern | Klassifikationen |
| `kl-2-wagner` | Wagner-Graduierung mit Tabelle und Quelle | Klassifikationen |
| `rx-1-meary` | Meary-Winkel mit Normwert, Quelle und Referenzaufnahme | Röntgenmessungen |
| `ops-1-suche` | OPS-Suche 2026 mit AOP- und Hybrid-DRG-Kennzeichnung | Abrechnungswissen |
| `menue-1` | Hauptmenü mit den acht Werkzeugen | Hero |
| `pat-1-start` | Startseite der Patienten-App | Patienten-Abschnitt |
| `pat-2-verlauf` | Hervorgehobener OP-Tag und Verlauf danach | Patienten-Abschnitt |
| `pat-3-wegweiser` | Beschwerde-Wegweiser, Markierung am Fußfoto | Patienten-Abschnitt |
| `pat-4-uebung` | Übungsprogramm Achillodynie Stufe 4 mit Übungsfotos | Patienten-Abschnitt |
| `au-1-risiken` | Aufklärungstexte: „Chevron + Akin" gewählt, generierter Risikotext mit Kopie-Knopf | Sprechstundenbrief (Kandidat) |
| `sb-3-brief-qr` | Schluss des generierten Briefs mit Kurzadresse und QR-Code zur Patienten-App | Sprechstundenbrief oder Patienten-Abschnitt (Kandidat) |

`qr-patienten-app.png` (720 × 720, Petrol auf Weiß) zeigt auf `https://patienten.fuss-track.de` und gehört in den Patienten-Abschnitt.

## B) Doppelbilder 1600 × 950 — nicht mehr auf der Landingpage

Diese Dateien waren die erste Fassung und stehen **nicht mehr** in `index.html`. Sie bleiben im Repo als Material für Vortragsfolien, LinkedIn-Posts und das Kongress-Handout, wo zwei Ansichten nebeneinander sinnvoll sind:

`clinic-uebersicht`, `clinic-sprechstundenbrief`, `clinic-op-bericht`, `clinic-fallsteuerung`, `clinic-klassifikationen`, `clinic-roentgen`, `clinic-ops-katalog`, `clinic-kodierlogik`, `patienten-uebersicht`, `patienten-begleiter`, `patienten-op-einrichten`, `patienten-op-verlauf`, `patienten-wegweiser`, `patienten-infomaterial` — jeweils mit 800er-Fassung.

`og-clinic.jpg` und `og-patienten.jpg` (je 1200 × 630) bleiben die Vorschaubilder für geteilte Links.

## C) Regeln für weitere Aufnahmen

- Behandler-App: Summen und Katalogwerte dürfen sichtbar sein, Artikelzeilen mit Herstellernamen, Stückzahlen oder Einzelpreisen nicht.
- Röntgenaufnahmen nur ohne Patientenangaben und ohne Aufnahmedatum, auch nicht eingebrannt.
- Zuschnitt oben unter der Statusleiste, unten oberhalb eingeblendeter Bedienelemente.
- Neue Landingpage-Bilder immer im Format 4 : 5, damit die Streifen gleich hoch bleiben.
