# Auftrag: Word-Knopf entfernen, Briefprüfung einbauen

Stand: 13.09.2026. Grundlage: `konzept-briefpruefung.md` (Repo-Root), vom Autor freigegeben. Zwei Teile, getrennt zu committen.

## Teil A, sofort: Word-Knopf entfernen

Der Word-Export im Sprechstundenbrief (eingeführt nach `auftrag-word-button-sb.md`, Funktion mit `Sprechstundenbrief.doc` und eingebetteten QR-Bildern, `app.html` ab Zeile 2895) entfällt ersatzlos. Bestandsaufnahme vom 13.09.: Dieselbe Funktion gibt es auch im OP-Bericht (`OP-Bericht_<Seite>_<Geschlecht>.docx`, Zeilen 5747 und 5758) und im UC-Bericht (`UC_OP_Bericht.docx`, Zeile 6807). Ob diese beiden ebenfalls entfallen, entscheidet der Autor vor Beginn; bis dahin gilt Teil A nur für den Sprechstundenbrief. Die Excel-Bibliothek `lib/xlsx-style.min.js` bleibt, sie trägt Import und Export der Implantatpreise. Der Autor: „Diese Funktion wird nicht benötigt, man kopiert diesen Bericht immer wo rein." Zu entfernen sind der Knopf, die Erzeugungsfunktion für die Word-Datei und alle nur dafür eingebundenen Hilfsroutinen; „Kopie" bleibt der einzige Ausgabeweg, in beiden Generatoren. Falls die Hilfe oder ein Rundgang den Word-Knopf erwähnt, dort ebenfalls streichen. Gegenprobe: Sprechstundenbrief erzeugen, Kopie funktioniert, kein Word-Element mehr sichtbar, keine Konsolenfehler; Suche im Code nach dem Word-Bezeichner liefert keine Reste.

Eigener kleiner Commit, deploybar ohne Bucket-Änderung.

## Teil B, nach dem 28-Zweige-Auftrag: Briefprüfung

Umsetzung nach Konzept, Abschnitte 2 bis 5. Kurzfassung der Anforderungen:

1. Neue Datengruppe `pruefung` (`data/pruefung.json`, Bucket, DEPLOY.md Abschnitt D). Fehlt die Datei, erscheint kein Prüfen-Knopf, sonst keine Änderung im Verhalten.
2. Eine Funktion `pruefeBrief(text, struktur, pruefung)` für beide Generatoren. `struktur` ist die Modulliste in Reihenfolge mit Schlüssel, Textbereich und Kontext (Seite, Geschlecht, Alter, Weg, Setting, gewählte OP). Rückgabe: Funde mit `id, grad, text, von, bis, korrektur, ersatz`.
3. Musterregeln (`typ: muster`) laufen als Regex aus der Datei; Modulregeln (`typ: modul`) sind im Code umgesetzt und lesen nur Parameter aus der Datei. Die im Konzept genannten Modulregeln: Seite, Anrede, Weg, Dublette, Übergang gleicher Art, Satzanfang, leerer Abschnitt.
4. Darstellung: Knopf „Prüfen" neben „Kopie", Zahl der Funde am Knopf, Liste unter der Vorschau mit Schweregrad, Kurztext, markiertem Ausschnitt und Korrekturknopf; Tippen auf die Zeile scrollt die Vorschau zur Stelle. Blockierende Funde färben den Kopie-Knopf orange, sperren ihn nicht.
5. Korrekturen wirken auf den erzeugten Text (nicht auf die Vorlagen) und bleiben bis zur nächsten Änderung der Auswahl erhalten; danach läuft die Erzeugung neu und die Prüfung erneut. Korrektur „feld" springt in das Eingabefeld.
6. Übergänge: Verbindungssätze ausschließlich aus `UEBERGAENGE`, nie generiert. Fehlt ein passendes Paar, meldet die Prüfung nur, ohne Korrekturknopf.
7. Kein Netzzugriff, keine Bibliothek.

Die Cowork-Sitzung liefert `data/pruefung.json` mit der ersten Regel- und Übergangstabelle (Freigabe des Autors) sowie die Modul-Etiketten für die Bausteine aus `diagnosen.json` und `optexte.json`, bevor Teil B beginnt. Bis dahin bitte nicht anfangen; Teil A ist unabhängig davon.

Gegenprobe Teil B: zehn Briefe und zehn OP-Berichte, die der Autor benennt; jeder Fund mit Erwartung. Vor der Freigabe keine falschen blockierenden Funde.
