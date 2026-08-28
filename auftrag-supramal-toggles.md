# Auftrag: Zwei Toggles für die supramalleoläre Open-Wedge-Osteotomie (app.html + data/optexte.json)

Stand: 28.08.2026. Fund A3 aus dem Voll-Audit; Texte vom Autor freigegeben.

## Problem

Der OP-Bericht der Variante „Med. Open Wedge" (T-Schlüssel `supramal_wedge`) enthält die rohen Marker `§FIBULA_OT§` und `§BROSTROM§` — es gibt dafür keine Ersetzungslogik. *Repro:* OP-Bericht → M/L/≥18 → Umstellungsosteotomien → Supramalleolare OT → „Med. Open Wedge" → Anzeigen: beide Marker stehen wörtlich im Text (zwischen Plattenosteosynthese und radiologischer Abschlusskontrolle).

## Was zu tun ist

**1. Zwei Toggles in app.html** an der Varianten-Auswahl „Med. Open Wedge" (Muster wie „+ Akin" beim Chevron):

- „+ Fibula-Verkürzungsosteotomie"
- „+ Laterale Stabilisierung (Brostrom-Gould)"

Toggle aktiv → Marker wird durch den jeweiligen Textbaustein ersetzt; Toggle inaktiv → Marker ersatzlos entfernt. Beide Marker müssen in JEDEM Fall aus dem erzeugten Text verschwinden. Nur die Wedge-Variante betrifft das; Dome und Closed Wedge haben die Marker nicht.

**2. Zwei neue T-Schlüssel in data/optexte.json** (Texte wörtlich so übernehmen):

`supramal_zusatz_fibula_ot`:

> Nach Aufspreizen der Tibiaosteotomie zeigt sich, dass sich das Gelenk nicht korrekt einstellt, die Fibula steht relativ zu lang. Daher separate Inzision über der distalen Fibula, schichtweise Präparation unter Schonung des N. peronaeus superficialis. Verkürzungsosteotomie der Fibula mit der oszillierenden Säge, Einstellen von Länge und Rotation, Osteosynthese mit winkelstabiler Platte. Nun kongruente Einstellung des Gelenkes.

`supramal_zusatz_brostrom`:

> Bei zusätzlich bestehender lateraler Instabilität erfolgt in gleicher Sitzung die laterale Bandstabilisierung: Darstellung des Retinaculum extensorum inferius und der antero-lateralen Kapsel, Ablösung des Kapsel-Bandansatzes LFTA/LFC unter Schutz der Peronealsehnen, dann Schaffung eines spongiösen Lagers an der Vorderfläche der distalen Fibula. Einbringung von {IMPL:anker_faden_geflochten} entsprechend der anatomischen Insertionen von LFTA/LFC. Raffende Fixierung des Kapselbandapparates unter Halten des Fußes in mittlerer Extensions-/Eversionsposition mittels Mason-Allen-Nähten und Nutzung resorbierbarer Fäden, Augmentation durch das Retinaculum und Fixierung mit transossärer Naht. Das Gelenk ist lateral nun eindeutig stabil.

Der `{IMPL:…}`-Platzhalter ist Absicht (läuft über `implantatBezeichnung()`, wie im Standalone-Brostrom-Text).

**3. Absatzführung prüfen:** Im Bestandstext stehen die Marker direkt hintereinander (`§FIBULA_OT§§BROSTROM§`) ohne Leerzeichen/Umbrüche — bei aktiven Toggles je einen Absatz (\n\n) davor/dazwischen setzen, damit der Text nicht zusammenklebt.

**4. Gegenprobe:** Wedge-Bericht in allen vier Toggle-Kombinationen erzeugen — kein `§` mehr im Text, KEINE geschweifte Klammer im erzeugten Text (der `{IMPL:…}`-Platzhalter muss durch `textPlatzhalter()` laufen; ohne Preisliste erscheint dann die Katalogbezeichnung „Fadenanker mit geflochtenem Faden", niemals der rohe Platzhalter), Absätze sauber, Dome/Closed unverändert.

## Deploy

`app.html` committen/pushen UND `data/optexte.json` in den Supabase-Bucket `toolbox-data` (erst löschen, dann hochladen). DEPLOY.md Abschnitt D ist entsprechend zu ergänzen, falls der Upload nicht sofort erfolgt.
