# Auftrag Clinic (Backlog G5): Kacheltext der Patienten-App

Stand 22.09.2026, Cowork-Sitzung. Backlog G5 (Entscheidung des Autors 22.09.2026: nur der Kacheltext, kein Hinweis in der Patienten-App). Datei `app.html`, Ausgangsstand Commit c65a4b1 (806.200 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

Die Startseiten-Kachel öffnet die Patienten-App mit `target="_blank"` (Z. 10097). Auf dem Handy (App vom Startbildschirm) zeigt iOS dafür sein eingebautes Browserfenster, es gibt dort keinen Tab; die Unterzeile Z. 10103 sagt aber „öffnet in neuem Tab". Das Fenster selbst ist nicht beeinflussbar und bleibt (im selben Fenster zu öffnen wäre schlechter: Clinic-Zustand weg, kein Rückweg).

## Änderung

Z. 10103: „Aufklärung · Begleiter · Schmerz-Finder · öffnet in neuem Tab" → „Aufklärung · Begleiter · Schmerz-Finder · öffnet in eigenem Fenster".

## Nichts anderes

Link, `target`, `rel`, Gestaltung der Kachel, `FUSSTRACK_BASE_URL` (Z. 1039), QR-Adressen (Z. 2013, 2024), Patienten-App unverändert. Kein Parameter `von=clinic`.

## Abnahme

Cowork-Prüfstand: Startseite zeigt in der Kachel den neuen Text; Klick öffnet weiterhin `https://patienten.fuss-track.de/fusstrack.html` in neuem Fenster; Selbsttest unverändert, keine Konsolenfehler.

Abnahme des Autors am Handy: Kachel lesen, antippen, mit X oben links zurück, Clinic-Zustand erhalten.

Vollzugsmeldung bitte mit Commit-Hash und der Zeilennummer.
