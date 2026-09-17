# Auftrag: Abschnitt „⑤ Sonographie" im Sprechstundenbrief

Stand 17.09.2026, Cowork-Sitzung. Konzept vom Autor freigegeben 17.09.2026 („Ok"), Texte und Datenteil freigegeben („3r frei"): `data/sono.json` (neu, 11.228 Byte) und `data/diagnosen.json` (Feld `sono` je Diagnose, 61.320 Byte) liegen lokal auf dem Mac; Bucket-Upload durch den Autor **vor** dem Push dieses Commits, sonst bricht die Live-App beim Laden ab (fehlende Datei = DATEN-FEHLER, Z. 197 ff.). Ausgangsstand `app.html`: Commit e2984a7 (789.924 Byte). Zeilenangaben beziehen sich darauf. Ein Commit, eine Vollzugsmeldung. Hintergrund: `konzept-sonographie-sprechstundenbrief.md` (Projekt).

## Daten (liegen vor, nicht Teil des Auftrags)

`data/sono.json`:

```
{ "_kommentar": [...],
  "GRUPPEN": [ {"id":"gefaesse","titel":"Gefäße"}, {"id":"sehnen","titel":"Sehnen"}, {"id":"gelenke","titel":"Gelenke"}, {"id":"baender","titel":"Bänder"}, {"id":"weichteile","titel":"Weichteile"} ],
  "STRUKTUREN": { "<id>": { "label": "...", "gruppe": "<GRUPPEN.id>", "normal": "...", "auffaellig": "...", "immer": true (nur duplex_art, duplex_ven) }, ... } }
```

20 Strukturen in Katalogreihenfolge (Objektreihenfolge = Reihenfolge im Brief): `duplex_art`, `duplex_ven`, `as_mittel`, `as_ansatz`, `as_kontinuitaet`, `peroneal`, `tib_post`, `plantarfaszie`, `osg`, `usg`, `mtp1`, `mtp_klein`, `tmt`, `interdigital`, `lfta`, `syndesmose`, `deltaband`, `ganglion`, `abszess`, `nerv`. In `normal` und `auffaellig` steht der Platzhalter `{SEITE}`; eckige Klammern sind Markierungen für den Untersucher und bleiben stehen.

`data/diagnosen.json`: je Eintrag `DIAG[dk].sono` = Liste von Struktur-IDs (bei `diffuse_beschwerden` leer). Die Endo-Diagnosen haben kein Feld.

## Änderungen im Code

1. **Laden.** `"sono"` in `GROUPS` (Z. 176) hinter `"diagnosen"`. Damit läuft die Datei über beide Ladewege (Repo `./data/`, Bucket) und erscheint im Selbsttest unter (10) Ladezeit und Größe ohne weitere Änderung. Konstante wie bei `DIAG` (Z. 781): `const SONO = window._DATA.sono || {GRUPPEN:[], STRUKTUREN:{}};`.

2. **Selbsttest, neue Prüfung.** In `selbsttestPruefen` eine Prüfung (11) „`DIAG[].sono` ohne Struktur in `sono.json`" (Art Fehler) und (12) „`sono.json`: Struktur ohne `normal`/`auffaellig`/`gruppe` oder `gruppe` nicht in `GRUPPEN`" (Art Fehler). Erwartete Treffer am heutigen Stand: 0 und 0. Nummer (10) Ladezeit bleibt, die neuen kommen dahinter; die Kopierausgabe (`alsText`, Z. 9513 ff.) nimmt sie mit.

3. **Zustand im Sprechstundenbrief** (`SprechstundenbriefApp`, Zustände bei `bilder` und `befState`): `sonoState` (Objekt id → `"normal"` | `"auff"` | fehlt), `sonoText` (Objekt id → bearbeiteter Auffälligkeitstext), `sonoDatum` (wie `bilder[i].datum`: `""`, `"heute"` oder Freitext, Vorgabe `"heute"`), `sonoFrei` (Freitext), `sonoKatalogOffen` (bool), `sonoExtra` (Liste von IDs, die der Nutzer aus dem Katalog dazu genommen hat). `resetAll` (Z. 2940) setzt alles zurück. `sec.sono` als Auf-/Zuklappzustand wie `sec.bild`.

4. **Sichtbare Strukturen** (`availSono`, nach dem Muster `availBef` Z. 2022, gleiche Abhängigkeiten plus `sonoExtra`): Reihenfolge = Katalogreihenfolge von `SONO.STRUKTUREN`; aufgenommen wird eine Struktur, wenn sie `immer` trägt, in `DIAG[d].sono` einer gewählten Diagnose steht, in `sonoExtra` liegt oder ihr `sonoState` gesetzt ist (damit eine Zeile beim Diagnosewechsel nicht verschwindet, solange sie einen Befund trägt). Im Endo-Pfad (`pfad === "endo"`) erscheint der Abschnitt nicht.

5. **Abschnitt** `<Sec title="⑤ Sonographie" …>` zwischen ④ Bildgebung (endet Z. 3743) und dem Abschluss (Z. 3745); der Abschluss wird `⑥ Abschluss & Empfehlung`. Inhalt von oben nach unten: Datumzeile wie in der Bildgebung (Eingabe TT.MM.JJJJ und Knopf „heute (in Sprechstunde)", Z. 3735–3738); je Struktur aus `availSono` eine Zeile: links das Label, rechts zwei Knöpfe „Normal" und „auffällig" (Optik der Optionsknöpfe in `BefTog` Z. 1230–1245; aktiver Knopf gefüllt, erneuter Klick setzt zurück). Bei „Normal" erscheint unter der Zeile der Normalsatz mit eingesetzter Seite in Grau (Schrift 10, nicht editierbar). Bei „auffällig" erscheint ein `textarea` (3 Zeilen), vorbelegt mit `auffaellig` mit eingesetzter Seite; Änderungen gehen nach `sonoText[id]`; ein Wechsel auf „Normal" oder zurück auf — löscht `sonoText[id]`. Die beiden Duplex-Zeilen stehen oben, darunter die übrigen sichtbaren Strukturen; zwischen beiden ein Zwischentitel in der Optik von `cat` („Gelenke, Sehnen, Bänder, Weichteile"). Darunter der Knopf „Weitere Strukturen ▾" (Optik `CB(false)`), der `sonoKatalogOffen` schaltet; offen zeigt er je Gruppe aus `SONO.GRUPPEN` (ohne `gefaesse`) den Titel und darunter als Chips (`CB`) alle Strukturen der Gruppe, die nicht schon sichtbar sind; Klick nimmt die Struktur in `sonoExtra` auf, sie erscheint sofort als Zeile oben. Bei `diffuse_beschwerden` als einziger Diagnose startet `sonoKatalogOffen` mit `true`. Zuletzt ein `textarea` „Freitext Sonographie…" (2 Zeilen) für `sonoFrei`. `data-tour="sb-sono"` auf dem Abschnitt.

6. **Seite einsetzen.** Hilfsfunktion `sonoSeite(text)`: ersetzt `{SEITE}` durch `links` / `rechts` / `beidseits` nach `seite` (wie `seitenKurz` Z. 3676); ohne gewählte Seite entfällt der Platzhalter samt dem Leerzeichen davor. Wird sowohl für die Anzeige als auch für die Vorbelegung des Textfelds benutzt; ein bereits bearbeiteter `sonoText` wird bei Seitenwechsel nicht mehr angefasst.

7. **Brieftext.** Nach dem Bildgebungs-Absatz (Z. 2714–2757, vor `// Abschluss`) ein Absatz, nur wenn mindestens ein `sonoState` gesetzt ist oder `sonoFrei` Inhalt hat:

   `"\n\nSonographie " + datumText + ":\n"` mit `datumText` wie in der Bildgebung („vom heutigen Tag" bei `heute`, sonst das Datum, ohne Datum entfällt der Zusatz und der Doppelpunkt folgt direkt).

   Dann die Zeilen in `availSono`-Reihenfolge. Auffällige Strukturen: je ein Satz `sonoText[id]` (falls bearbeitet) oder `sonoSeite(auffaellig)`. Normale Strukturen: aufeinanderfolgende Normalbefunde werden zusammengezogen, wenn mindestens zwei hintereinander stehen: „`Label1`, `Label2` und `Label3` sonographisch unauffällig." (Labels aus `sono.json`, Reihenfolge wie im Katalog); ein einzelner Normalbefund zwischen Auffälligkeiten steht mit seinem vollen Normalsatz. Die Duplex-Zeilen werden nie zusammengezogen, sie stehen immer mit ihrem vollen Satz (Gefäßbefund soll im Brief vollständig lesbar sein). Sätze durch Leerzeichen getrennt in einem Absatz; `sonoFrei` als letzter Satz.

   Beispiel (Plantarfasciitis, Duplex arteriell normal, Plantarfaszie auffällig, N. tibialis und Achillessehne normal):

   „Sonographie vom heutigen Tag: Farbkodierte Duplexsonographie der Unterschenkel- und Fußarterien links: A. tibialis anterior, … regelrecht darstellbar. Plantarfaszie links am Ansatz verdickt auf 6 mm (Normwert bis 4 mm), … N. tibialis (Tarsaltunnel) und Achillessehne, Mittelteil sonographisch unauffällig."

8. **Rundgang.** Ein Schritt nach `sb-befunde` (Z. 9142): `ziele:['[data-tour="sb-sono"]']`, Titel „Sonographie", Text: „Die beiden Duplex-Zeilen stehen immer bereit, die übrigen Strukturen richten sich nach der gewählten Diagnose. „Normal" setzt den festen Satz, „auffällig" öffnet einen Vorschlagstext, den Sie im Feld anpassen; die Klammern zeigen, was zu ersetzen ist. Weitere Strukturen finden Sie hinter dem Aufklapp-Knopf.", `wennFehlt` wie bei `sb-export`.

9. **Nichts anderes.** Bildgebung, Untersuchung, Fallsteuerung, OP-Bericht, UC-Bericht, Endo-Pfad, Kopierfunktionen bleiben unverändert; der Brief ohne gesetzte Sono-Zeile ist zeichengleich mit heute.

## Abnahme

Cowork-Prüfstand (`baseline_sb_3n2.json` + Stationär-Zeile aus e2984a7): alle 83 OP-Fälle und 19 Diagnosen zeichengleich, solange keine Sono-Zeile gesetzt ist. Vorauswahl je Diagnose gegen die Tabelle im Konzept (Abschnitt 5), zwei Diagnosen vereinigt, Endo-Pfad ohne Abschnitt. Plantarfasciitis links: Duplex arteriell Normal, Plantarfaszie auffällig mit geändertem Text („6" → „5,8"), Nerv und Achillessehne Normal → Brief wie das Beispiel oben, geänderter Text steht drin. Seite wechseln nach Bearbeitung: bearbeiteter Text bleibt, Normalsätze folgen der neuen Seite. „Weitere Strukturen" bei Hallux valgus öffnen, Ganglion dazunehmen, Diagnose wechseln: Ganglion-Zeile bleibt, solange ein Befund gesetzt ist. Reset leert alles. Selbsttest: (11) 0, (12) 0, `sono.json` in (10). 393 px: keine Überlappung, Knöpfe „Normal"/„auffällig" nebeneinander mit dem Label, Textfeld volle Breite. Keine Konsolenfehler.

Abnahme des Autors am Handy: Sprechstundenbrief, Sehnen und Faszien, Plantarfasciitis, Seite links: Abschnitt ⑤ zeigt Duplex arteriell, Duplex venös, Plantarfaszie, N. tibialis, Achillessehne Mittelteil. Plantarfaszie „auffällig" tippen, im Textfeld „[6]" durch „5,8" ersetzen, Duplex arteriell „Normal": in der Briefvorschau steht der Absatz „Sonographie vom heutigen Tag:" mit dem Duplex-Satz und dem bearbeiteten Plantarfaszien-Satz. „Weitere Strukturen" öffnen, unter Gelenke „Oberes Sprunggelenk" antippen, Zeile erscheint oben.

Vollzugsmeldung bitte mit Commit-Hash, Zeilennummern der neuen Blöcke (Abschnitt, Briefabsatz, Selbsttest-Prüfungen, Rundgang) und dem Selbsttest-Ergebnis (11)/(12).
