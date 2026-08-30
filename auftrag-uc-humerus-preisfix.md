# Auftrag: Null-sichere Preisanzeige im UC-Humerus-Block (app.html)

Stand: 30.08.2026. Beim Anklicken eines Humerus-Eingriffs im OP-Bericht-Generator (Sektion UC, Gruppe HUMERUS) stürzt der UC-Bereich ab: „Cannot read properties of null (reading 'toLocaleString')". Ursache ist die Implantat-Auswahl-Liste des Humerus-Blocks (bei `keys.map` über `UC_IMPL_HUMERUS_PROX`): Dort wird `imp.preis.toLocaleString("de-DE")` direkt aufgerufen, aber alle drei Einträge in `data/preise.json` → `UC_IMPL_HUMERUS_PROX` haben derzeit `preis: null` (Preise ausstehend, bewusst so gepflegt).

## Was zu tun ist

1. Im Humerus-Implantat-Block die Preisanzeige null-sicher machen: bei `preis == null` statt des Betrags den Text **„Preis ausstehend"** anzeigen (kursiv/grau, wie die bestehende PEND-Konvention der Materialkosten), sonst wie bisher formatiert mit €.
2. Einmal über app.html prüfen, ob weitere Stellen `.preis.toLocaleString` ohne Null-Guard aufrufen (gleiches Muster, gleiche Absicherung). Die Materialkosten-Funktion selbst hat mit `PEND(...)` bereits eine Absicherung — es geht um die direkten Render-Stellen.
3. Der Fehler ist unabhängig von den neu befüllten Humerus-Einträgen in optexte.json — er trat auch mit den alten „___"-Platzhaltern beim Anklicken auf.

## Gegenprobe

OB → M, L, ≥18 → Sektion UC → Gruppe HUMERUS öffnen → „Humerus subcapital (winkelstab. Platte)" anklicken: kein Absturz; Erlösübersicht zeigt I13E mit Betrag; die Implantat-Auswahl listet die drei Optionen mit „Preis ausstehend". Danach „Humerusschaft (Nagel)" ebenso. Zum Vergleich TFNA anklicken — unverändert funktionsfähig.

## Deploy

Nur `app.html` ändern, committen, pushen. Kein Bucket-Upload durch diesen Auftrag (die parallel geänderten data-Dateien optexte/opsteuerung/erloes2026 stehen bereits in DEPLOY.md Abschnitt D).
