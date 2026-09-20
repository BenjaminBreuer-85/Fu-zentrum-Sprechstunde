# Auftrag Clinic: Sprechstundenbrief ohne Grußformel, Kopie in Schriftgröße 10

Stand 20.09.2026, Cowork-Sitzung. Wunsch des Autors 20.09.2026: Der Sprechstundenbrief wird in die Briefvorlage der Klinik kopiert; dort stehen Grußformel und Unterschrift schon, und der Text der Standardbriefe hat Schriftgröße 10. Datei `app.html`, Ausgangsstand Commit c6f3732 (802.645 Byte, Zeilenangaben darauf; falls der Auftrag `auftrag-implantatfrei.md` vorher committet ist, gilt dessen Stand, die Stellen verschieben sich um wenige Zeilen). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## 1. Keine Grußformel mehr

Befund: Der Brieftext endet in allen drei Zweigen mit „Mit freundlichen Grüßen,": Metallentfernung Z. 2503 (`lines.push`), Endo Z. 2678 (`elines.push`), Standard-Fuß Z. 2927 (`ab += "\n\nMit freundlichen Grüßen,"`). Davor steht jeweils eine Leerzeile.

Änderung: die drei Stellen entfernen, samt der jeweils vorangehenden Leerzeile (Z. 2502 `lines.push("")`, Z. 2677 `elines.push("")`, in Z. 2927 den ganzen Zusatz), damit der Brief ohne Leerzeile am Ende schließt. Der letzte Satz bleibt der bisher vorletzte („Nach gründlicher Abwägung …", „Gerne kann sich …", QR-Block oder Endo-Aufklärungssatz). Betroffen sind Vorschau, Plain-Text-Kopie und HTML-Kopie gleichermaßen, weil alle aus `fullText` kommen.

## 2. Kopie in Schriftgröße 10

Befund: Mit QR-Code kopiert `copyWithQr` (Z. 2953 ff.) HTML mit `font-family:Arial,sans-serif;font-size:11pt` (Z. 2969) plus Plain-Text; ohne QR-Code kopiert `fallbackCopy` (Z. 3021) nur Plain-Text, den Word in der Formatierung der Einfügestelle übernimmt. Die 11 pt der HTML-Variante passen nicht zur Vorlage.

Änderung: (a) Z. 2969 `font-size:10pt`. (b) Schriftart: `font-family` weglassen, damit Word die Schrift der Vorlage nimmt (der Autor hat keine Schrift benannt; Arial war nur eine Annahme der ersten Fassung). Falls Word beim Einfügen ohne Schriftangabe auf Times New Roman zurückfällt, stattdessen `font-family:inherit` setzen; bitte in der Vollzugsmeldung nennen, was gewählt wurde. (c) Ohne QR-Code weiter Plain-Text (Word übernimmt die Formatierung der Einfügestelle, also die 10 pt der Vorlage); keine Änderung an `fallbackCopy`. Wenn der Autor beide Wege gleich haben will, kann `copy()` (Z. 2944) auch ohne QR den HTML-Weg mit denselben Stilangaben nehmen; das ist eine Zeile mehr und nur nach Wunsch.

## Nichts anderes

Brieflogik, QR-Block, `briefSauber`, OP-Bericht und UC-Bericht (eigene Kopierfunktionen Z. 5915 ff.) unverändert.

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3w.json`): alle 83 Briefe und 19 konservativen Texte gleich bis auf die entfallene Schlusszeile (Vergleich mit gestrichener Grußformel zeichengleich); Fallsteuerung gleich. Kopie mit QR: `text/html` enthält `font-size:10pt`; Plain-Text-Teil ohne Grußformel. Keine Konsolenfehler, Selbsttest unverändert.

Abnahme des Autors am Handy/PC: Brief in die Vorlage kopieren (mit und ohne QR): keine doppelte Grußformel, Text in 10 pt.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern.
