# Konzept: Briefprüfung in Fuss-Track Clinic (regelbasiert, ohne Sprachmodell)

Stand: 13.09.2026. Entscheidung des Autors: Stufe 1 aus der Diskussion vom 13.09. wird gebaut; ein Sprachmodell im Betrieb (lokal oder auf einem Server) bleibt ausgeschlossen. Im selben Zug entfällt der Word-Knopf im Sprechstundenbrief (Kopie in die Zwischenablage genügt, der Text wird ohnehin in das Klinik- oder Praxissystem eingefügt).

## 1. Ziel

Bevor ein Sprechstundenbrief oder OP-Bericht kopiert wird, prüft die App den fertigen Text auf Reste aus der modularen Erzeugung und bietet zu jedem Fund eine Korrektur an, die mit einem Tipp übernommen wird. Alles läuft im Browser, nichts verlässt das Gerät, die Regeln und die Übergangssätze sind Daten im Bucket und werden vom Autor gepflegt. Die Prüfung ersetzt keine ärztliche Durchsicht; sie fängt das ab, was beim Zusammensetzen aus Vorlagen typischerweise übersehen wird.

## 2. Was geprüft wird

Die Prüfung arbeitet auf zwei Ebenen: auf dem fertigen Text (Ebene T) und auf der Modulstruktur, die der Generator kennt (Ebene M). Ebene M ist der Grund, warum keine KI nötig ist: Der Generator weiß, welcher Absatz aus welchem Modul stammt, welche Chips gesetzt sind und welche Felder leer geblieben sind.

**Platzhalter und leere Felder (T).** Reste wie `{IMPL:…}`, `§…§`, `[…]`, `XX`, `___`, `…` als Alleinstellung, `undefined`, `NaN`, leere Klammern `()`, doppelte Satzzeichen. Felder mit Namen, aber ohne Wert: Score genannt ohne Zahl, Bewegungsausmaß ohne Grad, Verweildauer ohne Tage, Datum als Platzhalter. Jede Regel ist ein Muster mit Schweregrad (blockierend, sollte, kosmetisch) und einer Korrekturart (entfernen, Feld nachtragen, Absatz streichen).

**Widersprüche zwischen Modulen (M).** Seite: links im Befund, rechts im Prozedere, beidseits im Röntgen. Geschlecht: Anrede Herr, im Text „die Patientin", oder umgekehrt; Pronomen „sie/er" nach der Anrede. Alter: unter 18 gewählt, Text nennt Erwachsenenformulierung. Weg: konservativer Weg gewählt, im Brief steht eine OP-Empfehlung oder eine Aufklärung; OP gewählt, Prozedere nennt nur konservative Maßnahmen. Setting: ambulant gewählt, Text spricht von stationärer Aufnahme. Diagnose und OP: Diagnose ohne `opText`-Treffer, aber OP-Chip, der einen anderen Diagnosetext verlangt (die Logik aus `auftrag-usg-diagnose-gelenke.md`, hier als Prüfung).

**Dubletten (T und M).** Derselbe Satz zweimal (nach Normalisierung von Leerraum und Satzzeichen); zwei Absätze mit gleichem Anfang (erste acht Wörter); dasselbe Untersuchungsergebnis in zwei Modulen (Befund-Toggle und Freitext). Korrektur: den zweiten Treffer streichen, der Nutzer sieht beide Stellen.

**Übergänge (M).** Jedes Modul trägt in den Daten ein Etikett `art` (befund, bildgebung, beurteilung, empfehlung, aufklaerung, verlauf, prozedere) und `beginn` (patient, befund, es, wir, diagnose). Die Prüfung meldet drei Fälle: zwei Module gleicher Art ohne Verbinder direkt hintereinander; drei Sätze in Folge mit demselben Satzanfang; ein Wechsel der Art ohne Verbinder (Befund zu Empfehlung). Die Korrektur ist ein Verbindungssatz aus der Tabelle `UEBERGAENGE` (siehe 4), passend zum Paar der Etiketten, in der Sprache des Autors.

**Form (T).** Doppelte Leerzeichen, Leerzeichen vor Satzzeichen, Absatz ohne Satzzeichen am Ende, Kleinschreibung am Satzanfang nach eingefügtem Modul, Zahl mit Punkt statt Komma bei Dezimalen, Einheit ohne Leerzeichen, drei Sätze in Folge mit „Es". Korrektur automatisch, einzeln oder gesammelt.

**Leere Abschnitte (M).** Überschrift ohne Inhalt (etwa „Bildgebung" ohne gewählten Befund), Prozedere ohne einen Punkt, OP-Bericht ohne Implantatzeile bei implantatpflichtigem Eingriff, Nachbehandlung ohne Belastungsangabe. Korrektur: Abschnitt entfernen oder ins Eingabefeld springen.

## 3. Darstellung

Neben „Kopie" steht der Knopf „Prüfen" (der Word-Knopf entfällt). Beim Tippen erscheint unter der Vorschau eine Liste, je Fund eine Zeile: Schweregrad als Punkt (rot, orange, grau), Kurztext, Ausschnitt mit markierter Stelle, rechts der Knopf mit der Korrektur („Satz streichen", „Verbinder einfügen", „Seite angleichen", „Feld ausfüllen"). Tippen auf die Zeile scrollt die Vorschau an die Stelle und hebt sie hervor. Am Kopf der Liste ein Satz: „3 Hinweise, davon 1 vor dem Kopieren zu klären." Blockierende Funde (Platzhalter, Seitenwiderspruch) färben den Kopie-Knopf orange, sperren ihn aber nicht; der Behandler entscheidet. Ohne Fund: „Keine Hinweise" und der Kopie-Knopf bleibt grün. Auf dem Handy dieselbe Liste unter der Vorschau, keine zweite Spalte.

Die Prüfung läuft auch stumm im Hintergrund bei jeder Änderung und zeigt am Prüfen-Knopf nur die Zahl der Funde; die Liste öffnet erst beim Tippen. So bleibt die Oberfläche ruhig.

## 4. Datenstruktur (Bucket, vom Autor pflegbar)

Neue Datei `data/pruefung.json`, Gruppe `pruefung` im Daten-Loader, abwärtskompatibel: fehlt die Datei, gibt es keinen Prüfen-Knopf.

```json
{
  "_kommentar": ["Regeln der Briefprüfung. typ: muster (Regex auf Text) | modul (Auswertung der Modulstruktur). grad: blockierend | sollte | kosmetisch."],
  "REGELN": [
    {"id": "platzhalter_impl", "typ": "muster", "muster": "\\{IMPL:[^}]*\\}", "grad": "blockierend", "text": "Implantat-Platzhalter nicht ersetzt", "korrektur": "feld", "feld": "implantate"},
    {"id": "rest_klammer", "typ": "muster", "muster": "\\(\\s*\\)|\\[[^\\]]*\\]|§[^§]*§", "grad": "blockierend", "text": "Leere Klammer oder Platzhalter", "korrektur": "entfernen"},
    {"id": "xx", "typ": "muster", "muster": "\\b(XX+|___+|undefined|NaN)\\b", "grad": "blockierend", "text": "Platzhalter im Text", "korrektur": "entfernen"},
    {"id": "doppelleer", "typ": "muster", "muster": "  +| ([,.;:])", "grad": "kosmetisch", "text": "Leerzeichen", "korrektur": "ersetzen", "ersatz": "$1"},
    {"id": "seite", "typ": "modul", "text": "Seitenangabe widerspricht der Auswahl", "grad": "blockierend", "korrektur": "seite"},
    {"id": "anrede", "typ": "modul", "text": "Anrede und Personenform passen nicht zusammen", "grad": "sollte", "korrektur": "geschlecht"},
    {"id": "weg", "typ": "modul", "text": "Gewählter Weg und Brieftext widersprechen sich", "grad": "sollte", "korrektur": "hinweis"},
    {"id": "dublette_satz", "typ": "modul", "text": "Satz kommt zweimal vor", "grad": "sollte", "korrektur": "zweiten_streichen"},
    {"id": "uebergang_gleich", "typ": "modul", "text": "Zwei Abschnitte gleicher Art ohne Übergang", "grad": "sollte", "korrektur": "verbinder"},
    {"id": "satzanfang", "typ": "modul", "text": "Drei Sätze in Folge mit gleichem Anfang", "grad": "kosmetisch", "korrektur": "verbinder"},
    {"id": "leerer_abschnitt", "typ": "modul", "text": "Überschrift ohne Inhalt", "grad": "sollte", "korrektur": "abschnitt_entfernen"}
  ],
  "UEBERGAENGE": [
    {"von": "befund", "nach": "befund", "saetze": ["Ergänzend zeigt sich …", "Darüber hinaus findet sich …"]},
    {"von": "befund", "nach": "bildgebung", "saetze": ["Bildgebend bestätigt sich dieser Befund:", "In der Bildgebung zeigt sich passend dazu …"]},
    {"von": "bildgebung", "nach": "beurteilung", "saetze": ["Zusammenfassend ergibt sich …", "Klinik und Bildgebung passen damit zu …"]},
    {"von": "beurteilung", "nach": "empfehlung", "saetze": ["Daraus leitet sich folgendes Vorgehen ab:", "Wir haben daher besprochen, …"]},
    {"von": "empfehlung", "nach": "aufklaerung", "saetze": ["Über den Eingriff wurde ausführlich aufgeklärt:", "Im Aufklärungsgespräch wurden besprochen:"]},
    {"von": "empfehlung", "nach": "prozedere", "saetze": ["Das weitere Vorgehen:", "Konkret vereinbart wurde:"]}
  ],
  "MODUL_ETIKETTEN": {
    "_kommentar": ["Etikett je Baustein-Schlüssel aus diagnosen.json (befunde, konservativ) und optexte.json (T). Fehlt ein Eintrag, gilt art = unbekannt und der Baustein wird bei Übergängen übersprungen."],
    "usg_arthrose.befunde.0": {"art": "befund", "beginn": "befund"},
    "tmt1_arthrodese": {"art": "verlauf", "beginn": "wir"}
  }
}
```

Die Etiketten liegen bewusst in der Prüfdatei und nicht in `diagnosen.json` oder `optexte.json`, damit die Inhaltsdateien unverändert bleiben und die Prüfung ohne Freigabe der Inhalte wachsen kann. Sobald sie sich bewährt haben, können sie in die Inhaltsdateien wandern.

Die Sätze in `UEBERGAENGE` liefert der Autor; die Beispiele oben sind Platzhalter für die Struktur, nicht für den Wortlaut. Vor dem Bau bittet die Cowork-Sitzung um ein Dutzend echte Übergänge, an denen der Autor sich gestört hat, und baut daraus die erste Tabelle zur Freigabe.

## 5. Auswertung im Code (Skizze)

Eine Funktion `pruefeBrief(text, struktur, pruefung)` in `app.html`, gemeinsam für beide Generatoren. `struktur` ist die Liste der eingesetzten Module in Reihenfolge, je Modul Schlüssel, Textanfang und Textende im Gesamttext, dazu die Kontextwerte (Seite, Geschlecht, Alter, Weg, Setting, gewählte OP). Rückgabe: Liste von Funden `{id, grad, text, von, bis, korrektur, ersatz}`; die Darstellung zeigt sie, die Korrektur wendet `ersatz` auf den Bereich `von` bis `bis` an oder springt ins Eingabefeld. Regeln vom Typ `muster` laufen als Regex über den Text; Regeln vom Typ `modul` sind im Code fest verdrahtet und lesen nur ihre Parameter aus der Datei. Neue Musterregeln kann der Autor damit ohne Codeänderung anlegen, neue Modulregeln nicht; das ist gewollt, weil Modulregeln Kontext brauchen.

Keine Netzverbindung, keine Bibliothek, kein Modell. Laufzeit im Millisekundenbereich, auch auf dem Handy.

## 6. Abgrenzung

Die Prüfung bewertet keine medizinischen Inhalte und formuliert keine Sätze; sie verwendet nur Sätze aus der Tabelle des Autors. Sie ist damit Teil der Individualisierungslinie aus `recherche-textbausteine-recht.md`: Der Brief wird vor der Freigabe auf Schema-Reste geprüft, die Entscheidung bleibt beim Behandler. Ein Sprachmodell im Betrieb bleibt ausgeschlossen (Bauprinzip Datenschutz, Vortrag 10.09.2026, Folie „Automatisierte Inhalte haften am Arzt").

## 7. Reihenfolge

1. Word-Knopf entfernen (kleiner Auftrag, sofort).
2. Autor liefert Übergangsbeispiele; Cowork-Sitzung baut `pruefung.json` mit erster Regel- und Übergangstabelle zur Freigabe.
3. Code-Sitzung baut Prüffunktion und Darstellung, nach dem 28-Zweige-Auftrag, damit die Fallsteuerung im OP-Bericht vorher aus einer Quelle kommt.
4. Gegenprobe: zehn Briefe und zehn OP-Berichte aus dem Alltag des Autors, jeder Fund mit Erwartung (richtig, falsch, fehlt); Ziel vor der Freigabe: keine falschen blockierenden Funde.
