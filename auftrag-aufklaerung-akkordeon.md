# Auftrag: Eingriffsauswahl im Aufklärungstool aufklappbar machen

Betrifft die Ansicht „Aufklärungstexte", Block „Eingriff(e) auswählen". Heute stehen alle acht Kategorien mit sämtlichen Chips gleichzeitig untereinander. Auf dem Telefon ergibt das eine sehr lange, flache Fläche, in der die Kategorieüberschriften zwischen den Chips untergehen. Keine Änderung an Auswahllogik, Texterzeugung oder Daten.

## Ziel

Die Kategorien erscheinen als geschlossene, klickbare Zeilen. Erst beim Antippen klappt die zugehörige Chip-Gruppe auf. Beim Öffnen der Ansicht sind alle Gruppen zu, sodass der Bildschirm mit acht Zeilen beginnt statt mit rund vierzig Chips.

## Verhalten

**Gruppenzeile.** Volle Breite, Mindesthöhe 44 Punkte für sichere Bedienung mit dem Daumen. Links der Kategoriename in der bestehenden Petrol-Schrift, rechts ein Chevron, das beim Aufklappen um 90 Grad dreht. Die Zeile trägt eine dezente Trennlinie oder eine leicht abgesetzte Fläche, damit die Gliederung ohne Farbe erkennbar bleibt. Mehrere Gruppen dürfen gleichzeitig offen sein, das Aufklappen einer Gruppe schließt keine andere.

**Getroffene Auswahl bleibt sichtbar.** Zwei Dinge sorgen dafür, dass niemand eine Auswahl in einer zugeklappten Gruppe übersieht:

1. Über den Gruppen steht eine Zeile „Ihre Auswahl" mit den aktuell gewählten Eingriffen als Chips, jeder einzeln durch Antippen wieder abwählbar. Ist nichts gewählt, entfällt die Zeile ersatzlos.
2. Jede Gruppenzeile mit mindestens einer aktiven Auswahl trägt rechts neben dem Namen einen kleinen Zähler, etwa „2", und bleibt farblich als aktiv erkennbar.

Gruppen, die beim Betreten der Ansicht bereits eine Auswahl enthalten (etwa nach einem Wechsel zurück in die Ansicht), starten aufgeklappt.

**Suche.** Das Suchfeld bleibt an seiner Stelle und wird wichtiger als bisher. Sobald etwas eingegeben ist, klappen alle Gruppen mit Treffern automatisch auf und zeigen nur die passenden Chips, Gruppen ohne Treffer werden ausgeblendet. Wird das Feld geleert, kehrt die Ansicht in den zugeklappten Ausgangszustand zurück, wobei Gruppen mit Auswahl offen bleiben. Findet die Suche nichts, erscheint eine kurze Zeile „Kein Eingriff gefunden".

**Zustand.** Der Aufklapp-Zustand gilt innerhalb der Sitzung und muss nicht gespeichert werden. Beim Verlassen und erneuten Betreten der Ansicht greift die Regel von oben: alles zu, außer Gruppen mit Auswahl.

## Gegenprobe

Alle acht Kategorien und sämtliche Eingriffe weiterhin erreichbar, keiner fehlt · Mehrfachauswahl über Gruppengrenzen hinweg unverändert möglich · erzeugter Aufklärungstext bei gleicher Auswahl zeichengleich zum Bestand · Auswahl in einer zugeklappten Gruppe erscheint in der Zeile „Ihre Auswahl" und im Zähler · Suche klappt auf, Leeren klappt zu, Gruppen mit Auswahl bleiben offen · Screenshot im Mobilformat im zugeklappten Zustand und mit einer offenen Gruppe.

## Hinweis

Falls dieselbe flache Chip-Liste an weiteren Stellen der App vorkommt, bitte nur melden, nicht mitändern. Wir entscheiden dann, ob das Muster übertragen wird.
