# Auftrag: Word-Knopf entfernen, Briefprüfung einbauen

Stand: 13.09.2026, Teil A neu gefasst 14.09.2026 (Entscheidung „alle drei", Zeilen am aktuellen Stand geprüft). Grundlage: `konzept-briefpruefung.md` (Repo-Root), vom Autor freigegeben. Zwei Teile, getrennt zu committen.

## Teil A, sofort: Word-Export entfernen (alle drei Generatoren)

Entscheidung des Autors 13.09.2026: alle drei. Freigabe 14.09.2026 („weiter mit Word-Knopf"). Der Autor: „Diese Funktion wird nicht benötigt, man kopiert diesen Bericht immer wo rein." „Kopie" bleibt der einzige Ausgabeweg. Bestandsaufnahme am Stand `app.html` vom 14.09.2026 (779.959 Byte, nach dem Folgeauftrag Beidseits/Calcaneoplastie; Zeilennummern dieses Stands):

Sprechstundenbrief: Der Knopf ist seit `auftrag-word-button-sb.md` (27.08.2026) weg, die Funktion `downloadWord()` (Z. 2915–2949, `Sprechstundenbrief.doc`, HTML-Blob mit eingebetteten QR-Bildern) steht noch im Code und wird nirgends mehr aufgerufen. Sie entfällt jetzt ersatzlos, samt Kommentar zur Reaktivierung. Bleiben müssen: `getQrDataUrl` (Z. 1665, auch von der Rich-Text-Kopie Z. 2826/2866 genutzt), `copyQrToClipboard` und `downloadKlick` (Z. 736, QR-Bild-Download Z. 2873/2887 und Excel-Export der Preise).

OP-Bericht: `dlDocx` (Z. 5801–5840, `OP-Bericht_<Seite>_<Geschlecht>.docx`) und die beiden Knöpfe „📄 Word" (Z. 6504 Desktop-Leiste „Vorschau & Export", Z. 7219 mobile Vorschau) entfallen. `canExport` bleibt, weil die Vorschau davon abhängt.

UC-Bericht: der Knopf „📄 Word" mit Inline-Erzeugung (Z. 6902, `UC_OP_Bericht.docx`) entfällt; „📋 Kopieren" (Z. 6901) bleibt.

Gemeinsame Hilfsroutinen, nur für Word genutzt: `createZip` (Z. 7234), `buildDocx` mit den eingebetteten docx-Vorlagen (Z. 7276–7343, Content-Types, Relationships, `word/document.xml`, `word/styles.xml`) (die CRC32-Berechnung liegt innerhalb von `createZip`, Z. 7240–7244). Alles entfernen. Die Excel-Bibliothek `lib/xlsx-style.min.js` bleibt (Implantatpreise). Kommentare „für Word-Export" an `icdText` (Z. 5247) und `ucFullText` (Z. 5348) anpassen, die Werte selbst werden weiter für die Kopie gebraucht.

Rundgang und Hilfe: Texte, die „Word" nennen, umformulieren: Z. 9216 („… übernehmen Sie nach Word" → „… übernehmen Sie über Kopieren in Ihre Dokumentation"), Z. 9264 („geht er über „Word" in Ihre Dokumentation oder über „Kopieren" …" → nur Kopieren), Z. 9281–9282 (`wennFehlt` „Vorschau und Word-Export erscheinen …" → „Vorschau und Kopieren erscheinen …"; Text „über „Word" oder „Kopieren"" → „über „Kopieren""). Danach Suche im Code nach `Word`, `docx`, `.doc"`, `msword`, `wordprocessingml`, `dlDocx`, `downloadWord`, `buildDocx`, `createZip` ohne Reste (Treffer in Passwort-Feldern und Kommentaren zum Rich-Text-Kopieren sind keine Reste).

Gegenprobe (Cowork-Prüfstand): Sprechstundenbrief 81 Fälle, OP-Bericht 68 Fälle, Kombinationen 6 Fälle zeichengleich mit den Referenzläufen zum Stand nach dem Folgeauftrag (`baseline_*_code2.json`), abgesehen vom Wegfall der Zeile „📄 Word" in den Vorschau-Leisten; Kopieren in allen drei Generatoren funktioniert; keine Konsolenfehler. Abnahme: Autor am Handy.

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
