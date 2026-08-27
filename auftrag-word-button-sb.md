# Auftrag: Word-Knopf im Sprechstundenbrief-Generator entfernen (app.html)

Stand: 27.08.2026. Anweisung des Autors: Der Word-Export ist im Alltag kaum relevant, weil der Text ohnehin in das jeweilige Klinikformat übertragen wird. Der Sprechstundenbrief bietet **vorerst nur noch „Kopieren"** an.

## Was zu tun ist

In `app.html`, Modul Sprechstundenbrief-Generator, gibt es den Knopf „📄 Word" zweimal (mobile und Desktop-Leiste, beide rufen `downloadWord` auf, Stand heute etwa Zeilen 3302 und 3326 in der Vorschau-/Export-Leiste neben „📋 Kopieren" und „📋 QR-Code"):

- Beide „📄 Word"-Knöpfe **entfernen** (nur die UI-Elemente).
- Die Funktion `downloadWord()` **im Code belassen** — „vorerst" heißt: der Knopf soll ohne Aufwand wieder aktivierbar sein. Ein kurzer Kommentar an der Funktion genügt: `// UI-Knopf am 27.08.2026 auf Wunsch des Autors entfernt, Funktion bleibt für evtl. Reaktivierung`.
- „📋 Kopieren" und der QR-Code-Knopf bleiben unverändert.

## Ausdrücklich NICHT in diesem Auftrag

Die Word-Knöpfe des **OP-Bericht-Generators** (dlDocx, etwa Zeilen 5551 und 6258) und des **UC-OP-Berichts** (Zeile ~5941) bleiben bestehen. Ob sie ebenfalls entfernt werden, entscheidet der Autor separat.

## Deploy

Kein Bucket-Upload. Nur `app.html` ändern, committen, pushen.
