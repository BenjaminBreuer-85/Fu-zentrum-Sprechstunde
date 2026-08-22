# Auftrag: Verlaufsdokumentation ausbauen (Sonder-Flow „Kontrolle")

Ziel ist ein rechtssicherer **interner Karteieintrag** für wiederholte Vorstellungen in der Sprechstunde. Kein Brief an Zuweiser: keine Anrede, kein Diagnoseblock, keine Grußformel, kein QR-Code. Reiner Fließtext zum Kopieren in die Akte.

## Daten

Der fertige Datenblock liegt bei als `KONTROLLE_V2_block.json` (56 Bausteine). Er wird als neuer Top-Level-Schlüssel `KONTROLLE_V2` in `data/diagnosen.json` eingefügt. **Bitte nicht die mitgelieferte Datei als diagnosen.json verwenden**, sondern den Block in den aktuellen Stand übernehmen, damit nichts überschrieben wird. `KONTROLLE_TEXT` und `KONTROLLE_LABEL` bleiben vorerst unverändert im Bestand, bis der neue Flow abgenommen ist; danach entfernen wir sie.

`diagnosen.json` ist gitignored, der neue Stand muss also zusätzlich in den Supabase-Bucket `toolbox-data`.

## Struktur des Blocks

- `KOPF`: Kopfzeile mit Platzhalter `{ZEITPUNKT}`.
- `ANLAESSE`: sechs Anlässe (wundkontrolle, fadenzug, verlauf, roentgen, abschluss, ausserplanmaessig), je mit `label`, `anlass`-Satz, zugehörigem Maßnahmen-Set und Kennzeichen, ob ein Röntgenbefund angeboten wird.
- `ANAMNESE`, `BEFUND_NORM`, `BEFUND_ABWEICHUNG`, `MASSNAHME` (je Anlass), `ROENTGEN_BEFUND`, `ANWEISUNG` (acht Gruppen).
- `REIHENFOLGE_ANWEISUNG` legt fest, in welcher Reihenfolge die Anweisungsgruppen im Text erscheinen. Die Klickreihenfolge des Anwenders darf den Text nicht verändern.

Baustein-Felder: `id`, `text`, optional `standard` (vorausgewählt), `warn` (in Warnfarbe darstellen, inhaltlich gleichwertig), `feld` (Platzhalter mit Typ, Label und optionalem Default).

## Verhalten

1. **Zeitpunkt.** Ein Datumsfeld „OP-Datum" im Kontroll-Flow. Daraus wird `{ZEITPUNKT}` berechnet: bis Tag 20 „{N}. postoperativer Tag", ab Tag 21 „{N}. postoperative Woche" (abgerundet). Ohne Datum entfällt die Kopfzeile ersatzlos. Das Datum wird wie die übrigen Eingaben in der Sitzung gehalten, damit Folgetermine es nicht erneut brauchen.

2. **Befund.** Alle vier `BEFUND_NORM`-Sätze sind vorausgewählt und einzeln abwählbar. Wird `infekt` oder eine andere Abweichung gewählt, die dem Normalsatz widerspricht, wird der widersprechende Normalsatz automatisch abgewählt (mindestens: `infekt` schaltet `wunde` ab). Der Anwender kann das übersteuern.

3. **Sicherungsaufklärung.** Der Baustein `sicherung/standard` ist immer vorausgewählt, bleibt aber abwählbar. Wird er abgewählt, erscheint ein dezenter Hinweis, dass die Sicherungsaufklärung dann nicht dokumentiert ist. Kein Zwang, nur Sichtbarkeit.

4. **Platzhalter.** Felder erscheinen erst, wenn der zugehörige Baustein aktiv ist, direkt am Baustein. Nicht ausgefüllte Pflichtfelder bleiben im Text als `___` stehen, damit die Lücke sichtbar ist und nicht still verschwindet.

5. **Textaufbau.** Absätze in dieser Reihenfolge, leere Blöcke entfallen: Kopf, Anlass, Anamnese, Befund (Norm plus Abweichungen), Maßnahme, Röntgenbefund, Anweisungen gemäß `REIHENFOLGE_ANWEISUNG`. Innerhalb eines Absatzes werden die Sätze mit Leerzeichen verbunden, zwischen Absätzen steht eine Leerzeile. Satzproben für drei Fälle liegen bei (`satzprobe-kontrolle.txt`), der erzeugte Text muss diesen zeichengleich entsprechen.

6. **Bedienung.** Gleiche Chip-Optik wie im übrigen Brief. Gruppen mit Überschrift (Anamnese, Befund, Maßnahme, Röntgen, Anweisungen). `warn`-Bausteine in der bestehenden Warnfarbe. Der Kopierknopf übernimmt den Text unverändert.

## Gegenprobe

Die drei Satzproben aus `satzprobe-kontrolle.txt` in der App nachstellen und zeichengleich vergleichen. Dazu: kein `{` und kein `}` im erzeugten Text bei vollständig ausgefüllten Feldern; Klickreihenfolge ändert das Ergebnis nicht; ohne OP-Datum fehlt die Kopfzeile und der Rest bleibt unverändert; Abwahl der Sicherungsaufklärung entfernt genau diesen Satz; Wechsel des Anlasses setzt nur die anlassabhängigen Maßnahmen zurück, nicht die Anweisungen.

## Offen für die nächste Runde

Freitextfeld für einen eigenen Schlusssatz, Übernahme des zuletzt verwendeten Anweisungssatzes beim Folgetermin, Kopieren als Markdown für Systeme, die Absätze schlucken.
