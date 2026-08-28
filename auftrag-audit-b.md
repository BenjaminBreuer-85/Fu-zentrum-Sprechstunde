# Auftrag: Audit-Punkte B1, B2, B4, B5, B6 (app.html)

Stand: 28.08.2026. Entscheidungen des Autors aus der Audit-Durchsprache. Die Datenseite (opmethoden/diagnosen/opsteuerung) ist bereits erledigt und committet — dieser Auftrag betrifft nur `app.html`.

## B1 · Amputation proximale Tibia im OP-Bericht-Generator

In der Gruppe „DIABETISCHER FUSS / INFEKT" (Sektion ③ OP-Durchführung) neben „Debridement bei Ulkus und Infekt" einen zweiten Chip anlegen:

- Label: **„Amputation proximale Tibia"**
- Berichtstext: der vorhandene Schlüssel `T.df_amputation_tibia` (Burgess-Technik, liegt fertig in data/optexte.json).
- **Ausdrücklich KEINE Toggles** bei diesem Eingriff — die Debridement-Toggles (Lavanox, Vancomycin lokal, Einlage Lasche, VAC, Teilamputation) gelten hier nicht und dürfen nicht erscheinen.
- Die beim Debridement etablierte Zweitdiagnose-Logik (Osteomyelitis automatisch, abwählbar) gilt hier NICHT automatisch — Diagnoseblock wie vom df_amputation-Eintrag in opmethoden.json vorgegeben.

## B2 · Menü-Untertitel Sprechstundenbrief

Kachel-Untertitel „Arztbriefe mit Score & Word-Export" ersetzen durch:

> Arztbriefe mit Scores und Kopierfunktion

(Der Word-Export wurde im SB entfernt; der Untertitel verspricht ihn noch.)

## B4 · Cotton-Osteotomie ist Zusatzeingriff, kein Solo-Bericht

Entscheidung des Autors: Die Cotton-Osteotomie ist **nur Zusatzeingriff** — dass sie allein keinen Bericht erzeugt, ist richtig. Zwei Dinge sind zu tun:

1. Der Solo-Chip in der Ein-Chip-Untergruppe „COTTON-OSTEOTOMIE" (Mittelfuß) darf nicht als eigenständiger Eingriff wählbar wirken und dann nichts erzeugen. Entweder den Chip zu den passenden Haupteingriffen als Zusatz-Toggle verschieben (analog „+ Akin"), oder — falls er als Sucheinstieg bleiben soll — bei Auswahl einen Hinweis zeigen („Die Cotton-Osteotomie wird als Zusatzeingriff zu … dokumentiert"), statt stumm zu bleiben.
2. Als Zusatzeingriff muss sie Text liefern: die vorhandenen Schlüssel `T.cotton_ot_autolog` / `T.cotton_ot_allogen` verwenden (Wahl autolog/allogen als Unteroption).

Welche Haupteingriffe die Cotton als Zusatz führen sollen, bitte beim Autor rückfragen, falls nicht aus der bestehenden Struktur (Knick-Senk-Fuß/Rückfuß-Korrekturen) ersichtlich.

## B5 · Morton-Neurom: EBM-Hinweis in der Erlössimulation

`data/opsteuerung.json` enthält jetzt einen Eintrag `morton_neurom` (hdrg/drg null) mit `hinweise`-Array. Die Erlössimulation zeigt derzeit den generischen Satz „Für Morton-Neurom-Resektion ist keine eigene Fallpauschale hinterlegt. Die Kodierung muss hier manuell erfolgen."

Gewünscht: Bei Einträgen ohne drg/hdrg die `hinweise` aus OP_STEUERUNG rendern (falls vorhanden), statt des generischen Satzes. Für Morton erscheint dann:

> Die Morton-Neurom-Resektion wird in der Regel ambulant vertragsärztlich über den EBM abgerechnet. Die vertragsärztliche Abrechnung nach EBM bildet Fuss-Track Clinic nicht ab, daher erscheint hier keine Erlös-Simulation.

(Konform zur EBM-Sprachregelung: Lücke ehrlich benennen, keine Wertung.)

## B6 · WS-Sektion entfernen

Entscheidung des Autors: Das WS-Modul („WS-Modul im Aufbau — Daten teils Platzhalter") wird **vorerst entfernt** — der Sektions-Knopf „🦴 WS" im OP-Bericht-Generator darf nicht mehr anwählbar sein (Knopf ausblenden; Code und Daten dürfen als inaktiver Bestand bleiben, damit ein späterer Ausbau einfach ist).

## Gegenprobe

B1: Amputation wählen → Bericht mit Burgess-Text, ohne Debridement-Toggles. B4: Cotton-Solo-Klick bleibt nicht mehr stumm; als Zusatz erzeugt er Text. B5: Morton in der Erlössimulation zeigt den EBM-Hinweis. B6: WS-Knopf weg, UC/Endo unverändert.

## Deploy

Nur `app.html` committen/pushen. Bucket: `opsteuerung.json` steht bereits als offener Upload in DEPLOY.md Abschnitt D (Eintrag vom 28.08.); dieser Auftrag ändert keine weiteren Bucket-Dateien.
