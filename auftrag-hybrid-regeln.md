# Auftrag: Hybrid-Regeln je Hybrid-DRG in der Fallsteuerung (Konzept vom 07.09.2026, vom Autor freigegeben)

Grundlage: `konzept-fallsteuerung-hybrid-regeln.md` und `abgleich-gffc-hybrid-2026.md` (beide im Repo-Root). Die drei offenen Entscheidungen hat der Autor mit „ja" beantwortet: Konsequenz-Zeile immer sichtbar; Rahmenbedingungen als Hinweiszeile, nicht als Häkchen; Akin-Trigger beim Lapidus gilt automatisch als gesetzt.

Arbeitsteilung: Den Datenblock `HDRG_REGELN` und `HDRG_RAHMEN` in `data/opsteuerung.json` liefere ich (Cowork-Sitzung) nach Gegenprobe gegen `katalog2026.json`; er kommt als eigene Datei-Änderung mit DEPLOY.md-Eintrag. Dieser Auftrag betrifft `app.html`: Auswertung, Darstellung, Entschlackung der OP-Einträge, OP-Bericht-Kodierhinweise. Bis der Datenblock im Bucket liegt, muss die App ohne ihn lauffähig bleiben (Fallback auf die heutigen `ausschluss`/`aufwertung`-Blöcke je OP).

## 1. Datenstruktur, auf die sich der Code stützt

```json
"HDRG_REGELN": {
  "I20O_N": {
    "hdrg": ["I20O", "I20N"],
    "kontext":    [{"code": "5-788.54", "name": "3× DMMO/Weil MT II–V", "drg": "I20E"}, {"code": "5-784.0v", "name": "Spongiosatransplantation Metatarsale", "drg": null}],
    "aufwertung": [{"code": "5-788.52", "name": "1× DMMO/Weil", "hdrg": "I20N"}, {"code": "5-808.a4", "name": "Lapidus zusätzlich", "hdrg": "I20M"}],
    "neutral":    ["5-788.70", "5-788.57"],
    "positiv":    ["5-812.kk", "5-811.xk"]
  },
  "I20M": {
    "hdrg": ["I20M"],
    "kontext": [], "aufwertung": [], "neutral": [],
    "nichtKontext": [{"code": "5-854.2c", "name": "Sehnentransfer Mittelfuß/Zehen", "txt": "wirkt in I20M nicht als Kontextprozedur, Fall bleibt Hybrid"}]
  }
},
"HDRG_RAHMEN": ["Verweildauer unter 3 Tagen", "Alter über 17 Jahre", "PCCL unter 3", "kein hoher Pflegegrad", "keine Fallzusammenlegung aus zwei Aufenthalten"]
```

Bedeutung der Felder: `kontext` führt aus der Hybrid-DRG heraus; `drg` ist die Ziel-DRG stationär, `null` heißt „die `drg` der OP-Methode". `aufwertung` wechselt innerhalb der Hybrid-DRGs (I20O nach I20N, I20N nach I20M). `neutral` ändert nichts und darf keine Warnung auslösen. `positiv` sind Hybrid-Trigger, die nicht im AOP-Katalog stehen. `nichtKontext` sind Kodes, die Anwender fälschlich für einen Ausweg halten. Kodes in den Listen sind exakte OPS-Kodes ohne Schrägstrich-Sammelschreibweise; Kodes mit `x` an letzter Stelle (5-811.xk) sind wörtlich zu vergleichen, keine Platzhalter.

Zuständigen Regelsatz finden: `Object.values(HDRG_REGELN).find(r => r.hdrg.includes(best.hdrg))`. OP-Einträge behalten `hdrg`, `drg`, `empf`, `hebel`, `hebelName`, `hdrgTrigger`, `modifikatoren`, `hinweise`. Die Blöcke `ausschluss`, `aufwertung` und `kontext` je OP werden ignoriert, sobald `HDRG_REGELN` vorhanden ist, und in einem zweiten Schritt aus den Daten entfernt (mache ich).

## 2. Auswertung (eine Funktion, für Sprechstundenbrief und OP-Bericht)

Eingabe: Haupt-OP-Schlüssel, Menge der angeklickten OPS-Kodes (Haupt-OPS, Modifikatoren, Zusatzkodes), Setting-Auswahl.

1. `hdrg` der Haupt-OP. Hat die OP `hdrgTrigger`, gilt die Hybrid-Zugehörigkeit nur bei gesetztem Trigger. Für `lapidus` gilt der Akin-Trigger (5-788.56) als gesetzt, sobald der Chip gewählt ist; wird 5-788.56 in der Kodeliste ausdrücklich entfernt, entfällt er.
2. Kontextprozedur gesetzt (Schnittmenge angeklickte Kodes mit `kontext` des Regelsatzes nicht leer): Fall verlässt die Hybrid-DRG. Ziel-DRG = `drg` des ersten treffenden Kontextkodes mit gesetztem Wert, sonst `drg` der OP. Bei mehreren Treffern die höchstwertige DRG (Reihenfolge I20B, I20C, I20D, I20E, I20F).
3. Keine Kontextprozedur, aber Aufwertungskode: Hybrid-DRG wechselt auf `aufwertung.hdrg`; bei mehreren die höchste (I20M vor I20N vor I20O).
4. Ambulant: bestehende AOP-Katalogprüfung. Alle Kodes im Katalog und Fall in Hybrid: ambulant als Hybrid vergütet. Alle Kodes im Katalog und Fall außerhalb Hybrid: ambulant als EBM. Ein `positiv`-Kode angeklickt: ambulant nur als Hybrid, nicht als EBM (Warnung, siehe 5).
5. Warnungen (rot): (a) Kode aus `nichtKontext` angeklickt und keine echte Kontextprozedur gesetzt; (b) `positiv`-Kode angeklickt bei ambulanter Führung, Text „<Name> (<Kode>) steht nicht im AOP-Katalog, zieht den ambulanten Fall aus dem EBM in die Hybrid-DRG <hdrg>"; (c) Hebel der OP gesetzt, aber Fall ambulant (bestehende Logik, unverändert).

Rückgabe: `{hdrg, drg, setting: {ambulant: 'hybrid'|'ebm'|'nein', hybrid: bool, stationaer: drg}, satz, warnungen[], listen: {kontext, aufwertung}}`. `satz` ist der eine Klartextsatz für die Konsequenz-Zeile.

## 3. Darstellung im Sprechstundenbrief

Die drei Spalten (ambulant, Hybrid, stationär) bleiben unverändert. Direkt darunter, in normaler Schrift ohne Kasten, die Konsequenz-Zeile (`satz`), immer sichtbar. Muster:

„Fall liegt in I20O. Ausweg für diese OP: Sehnentransfer (5-854.2c) nach I20E."
„3× DMMO (5-788.54) führt aus I20O heraus. Stationär I20E, ambulant EBM."
„1× DMMO (5-788.52) wertet auf I20N auf."
„Fall liegt in I20M. Kein Ausweg gesetzt; Spongiosa (5-783.0v + 5-784.0v) führt nach I20D."

Kodes stehen nur im Satz, wenn sie angeklickt sind oder als der eine `hebel` der OP empfohlen werden. Unter der Konsequenz-Zeile die Warnungen aus Schritt 5, rot, je eine Zeile.

Darunter ein Aufklapper, standardmäßig geschlossen, Beschriftung „Kontextprozeduren <hdrg> anzeigen". Inhalt beim Öffnen: zwei Gruppen („führt heraus", „wertet auf"), je Zeile Kode, Name, Ziel; `neutral` und `positiv` werden nicht gelistet. Bei I20M zusätzlich eine dritte Gruppe „kein Ausweg" mit den `nichtKontext`-Einträgen.

Unter der Hybrid-Spalte eine Hinweiszeile in grau, klein: „Hybrid nur bei: " + `HDRG_RAHMEN.join(', ')`. Keine Abfrage, keine Häkchen.

Die Hebel-Zeile in der Stationär-Box (aus `auftrag-kontext-nur-hybrid.md`) bleibt. Der Block „Kontextprozeduren" aus demselben Auftrag wird durch den Aufklapper ersetzt, damit die Liste nicht zweimal erscheint.

## 4. OP-Bericht: Kodierhinweise aus der Auswertung

Der Block „Erlösrelevante Kodierhinweise" wird aus der Auswertung erzeugt: Zeile 1 Haupt-OPS; Zeile 2 gesetzte Kontext- oder Aufwertungskodes mit Namen; Zeile 3 `satz`; Zeile 4 bei stationärer Führung der bestehende Satz zur Belegungsdokumentation. Die je OP gepflegten `hinweise` mit Typ `erloes`, die dieselben Kodes nennen (MTP-I-Arthrodese „Stationär mit Kontextprozedur + 3× DMMO"), entfallen; `hinweise` mit Typ `info` oder `warn` (801D-Falle, Twist-Off-Schraube, LSG-Urteil bei Arthroskopie) bleiben und werden wie bisher angezeigt.

## 5. Gegenprobe

| Fall | erwartet |
|---|---|
| Chevron allein | Hybrid I20O; ambulant Hybrid; stationär I20E; Satz nennt Hebel 5-854.2c |
| Chevron + 5-788.52 | Hybrid I20N; Satz „wertet auf I20N auf" |
| Chevron + 5-788.54 | kein Hybrid; stationär I20E; ambulant: 5-788.54 nicht im AOP-Katalog, für Kliniken Hybrid empfohlen |
| Chevron + 5-788.60 | kein Hybrid; stationär I20F; ambulant: 5-788.60 nicht im AOP-Katalog (Hybrid-Kode ohne AOP-Eintrag), für Kliniken Hybrid empfohlen |
| MTP-I-Arthrodese allein | Hybrid I20N; Hebel 5-784.0v nach I20E |
| MTP-I + 5-788.54 | kein Hybrid; stationär I20D; keine Spongiosa nötig |
| MTP-I + 5-808.a4 | Hybrid I20M |
| Lapidus (Akin automatisch) | Hybrid I20M; Hebel Spongiosa nach I20D |
| Lapidus + 5-854.2c | Hybrid I20M bleibt; rote Warnung „kein Ausweg" |
| Lapidus + 5-788.54 | kein Hybrid; stationär I20D |
| ASK OSG 5-810.2k + 5-812.kk, ambulant | Hybrid I20O; rote Warnung Positivprozedur |
| USG-Arthrodese | kein Hybrid-Bezug; keine Konsequenz-Zeile zu Hybrid, kein Aufklapper |

Ergebnisse müssen den GFFC-Folien vom 04.03.2026 entsprechen (Ablage `_vortrag/` nicht, sondern beim Autor; Zusammenfassung in `abgleich-gffc-hybrid-2026.md`).


## Nachtrag 07.09.2026 abends: Datenblock liegt vor

`data/opsteuerung.json` (Vorschlag, nach Freigabe des Autors im Repo) enthält `HDRG_REGELN` und `HDRG_RAHMEN`. Abweichung zur Skizze oben: `drg` einer Kontextprozedur kann ein String sein (gilt immer) oder ein Objekt nach der Hybrid-DRG der Haupt-OP (`{"I20O": "I20E", "I20N": "I20D"}`), weil 5-788.54 beim Chevron nach I20E, bei der MTP-I-Arthrodese nach I20D führt. Fehlt `drg`, gilt die `drg` der OP-Methode. Kodes mit `x` an letzter Stelle (5-811.xk) sind wörtliche Katalogkodes, keine Platzhalter. Die Arthroskopie-Ausschlüsse (5-810.4k, 5-810.9k, 5-811.3k, 5-811.4k, 5-812.3k, 5-812.9k, 5-819.4) liegen im Regelsatz `I20O_N` mit Ziel I20F; `neutral` enthält dort auch 5-810.2k, 5-812.0k, 5-819.1k. Beim Lapidus ist der Hebel auf „5-783.0v + 5-784.0v" korrigiert (5-784.0u ist keine Kontextprozedur), `hdrgTrigger` um 5-788.5e und 5-788.60 ergänzt, Warnhinweis nach Grouper-Prüfung des Autors. Die alten Blöcke `ausschluss`/`aufwertung` je OP sind noch da (Fallback) und tragen ein korrigiertes Ziel-Label; sie werden entfernt, sobald die Auswertung auf `HDRG_REGELN` läuft.

Konsequenz-Zeile bei 5-788.54/55: „… führt aus I20O heraus. Stationär I20E; ambulant nur mit unvergüteten Osteotomien (5-788.54 nicht im AOP-Katalog)." Der Satz „ambulant EBM" gilt nur, wenn alle angeklickten Kodes im AOP-Katalog stehen.


## Nachtrag 09.09.2026: Antworten auf die Rückmeldung der Code-Sitzung

1. Gegenprobe Zeile 4 war veraltet, jetzt korrigiert: Chevron + 5-788.60 ergibt „ambulant nur mit unvergüteter Arthroplastik", weil 5-788.60 im Katalog Hybrid und Kontext ohne AOP-Flag trägt. Der Code folgt richtig der Regel aus dem Nachtrag vom 07.09.; die Tabellenzeile war der Fehler.

2. `positivNamen` ist im Regelsatz `I20O_N` ergänzt (5-811.xk, 5-812.kk, 5-812.xk, 5-819.xk mit Klartext, z. B. „Arthroskopische Osteophytenabtragung (OSG)"). Damit lautet die Warnung „Arthroskopische Osteophytenabtragung (OSG) (5-812.kk) steht nicht im AOP-Katalog …". Bitte den Kode in der Warnung nur einmal ausgeben, falls der Name ihn nicht enthält.

3. Aufklapper mit 120 Zeilen: gewollt, aber bitte innerhalb des Aufklappers nach Kodegruppen unterteilen, jede Gruppe mit einer Überschrift und der Anzahl, standardmäßig zusammengeklappt: „Osteotomien und Arthroplastiken Vorfuß" (5-788.x, 5-808.bh), „Knochentransplantation und Knochenersatz" (5-784.x, 5-785.x), „Offene Frakturreposition" (5-795.x, 5-796.x), „Sehneneingriffe" (5-854.x, 5-855.19), „Arthroskopie OSG" (5-81x.xk). Die Gruppe ergibt sich aus dem Kodepräfix, dafür ist kein zusätzliches Datenfeld nötig. Wer eine Gruppe öffnet, sieht die Zeilen wie bisher.

4. Abschnitt 4 (OP-Bericht-Kodierhinweise aus der Auswertung) und das Entfernen der `ausschluss`/`aufwertung`-Blöcke samt Overrides bleiben bewusst ein eigener dritter Durchgang, wie im Konzept vorgesehen. Reihenfolge: erst der Code hört auf, die alten Blöcke zu lesen (dieser Auftrag, Punkt 1 „ignoriert, sobald HDRG_REGELN vorhanden"), dann entferne ich die Blöcke aus den Daten. Zu `erloesData.kodier`: Bitte vor dem Umbau einmal auflisten, welche Führungstexte dort stehen, die die Auswertung nicht abdeckt (Belegungsdokumentation, Diabetes-Hauptdiagnose, Implantatdokumentation), damit wir entscheiden, was davon als `hinweise` vom Typ info in die OP-Einträge wandert und was entfällt. Diese Liste ist der Startpunkt für den dritten Durchgang.

## Nachtrag 09.09.2026, zweiter Teil: Entscheidung des Autors zum Aufklapper

Der Autor hat den Aufklapper in der App gesehen und entschieden, dass er bleibt. Darstellung nach seiner Vorgabe, Abweichung zu Punkt 3 oben:

1. Überschriften innerhalb des Aufklappers heißen „Führt aus Hybrid heraus" und „Wertet Eingriff auf" (statt „führt heraus" und „wertet auf"). Unter „Wertet Eingriff auf" steht je Kode die nächste Hybrid-DRG, in die der Kode führt (z. B. „5-788.52 → I20N", „5-808.a4 → I20M").

2. Die Kodegruppen („Osteotomien und Arthroplastiken Vorfuß", „Knochentransplantation und Knochenersatz", „Offene Frakturreposition", „Sehneneingriffe", „Arthroskopie") bleiben mit Überschrift und Anzahl, werden aber standardmäßig aufgeklappt gezeigt (`<details open>`), der Autor möchte die Kodes ohne weiteres Antippen sehen. Der äußere Aufklapper „Kontextprozeduren I20O anzeigen" bleibt standardmäßig geschlossen, damit die Fallsteuerung auf dem Handy kompakt bleibt.

3. Die je Eingriff hinterlegten, im Alltag relevanten Kontextprozeduren aus dem OP-Eintrag (`kontext`, `kontextExcluded`, Hebel) bleiben wie bisher sichtbar oberhalb des Aufklappers. Der Aufklapper ist die Gesamtliste, der OP-Eintrag die Auswahl.

4. Datenseite: In `HDRG_REGELN` tragen die Knochenersatz-Kodes 5-785.2s bis 5-785.5w und 5-796.pv jetzt Klartextnamen (bisher stand der Kode als Name). 5-819.4 bleibt ohne Namen, der Kode ist noch gegen die OPS-Systematik zu prüfen (Lokalisation fehlt), bitte in der Liste so lassen und nicht auffüllen.

5. Katalog (`katalog2026.json`, Modul OPS-Code-Suche): Der Abgleich der Kontextflags gegen `HDRG_REGELN` ist in `abgleich-katalog-kontextprozeduren-2026-09-09.md` dokumentiert. Der Autor hat die Änderungen freigegeben, `katalog2026.json` ist per Patch-Skript angepasst (25 neue Kontextprozeduren, Flags bei sieben Kodes, `_KX` um sechs Arthroskopiekodes erweitert; Bucket-Upload steht in DEPLOY.md). Kein Code-Eingriff nötig, `_HD` und `_KX` werden weiter wie bisher gelesen.

## Nachtrag 09.09.2026, dritter Teil: Entscheidungen zum dritten Durchgang (Abschnitt 4 und `erloesData.kodier`)

Grundlage ist eure Aufstellung der 31 `kodier`-Blöcke (90 Zeilen, 57 mit Kode, 24 ohne). Der Autor hat Stück für Stück entschieden:

1. **Belegungsdauer und Abschläge (6 Zeilen):** entfallen als Freitext, weil die festen Beträge (1.209 €, MVWD 6,2) veralten. Ersatz ist eine berechnete Zeile je Ziel-DRG aus `erloes2026.json` (`GVD`, `UGVD_ABSCHLAG`), sinngemäß: „Volle DRG I20E ab N Belegungstagen, darunter Abschlag X € je Tag; jeden Tag in der Akte begründen." Die Zeile steht unter der Konsequenz-Zeile, nur wenn der Fall stationär landet.

2. **Dokumentationspflichten und ICD-Hinweise (5 Zeilen):** wandern als `hinweise` vom Typ `info` an den jeweiligen Eingriff in `opsteuerung.json` (FHL-Transfer, Achillessehnennaht mit Paratenon, Metallentfernung mit Z47.0 und den Komplikations-Nebendiagnosen). FHL-Transfer (`fhl_transfer`) und Achillessehnennaht (`as_naht`) sind auf der Datenseite eingetragen. Für die Metallentfernung gibt es in `opsteuerung.json` keinen Eintrag; bitte nennt mir den Schlüssel, unter dem die `erloesData` der Metallentfernung im Code liegt, dann lege ich den Eintrag mit den ICD-Hinweisen an. Der Code muss dafür nichts Neues können. Die Zeile „H-DRG-TRIGGER I20O (Zusatzeingriff …)" ist eine Überschrift über Kodezeilen und entfällt mit ihnen.

3. **Setting-Aussagen, Gliederungszeilen, TODO-Rest (13 Zeilen):** entfallen, die Konsequenz-Zeile deckt sie ab. Bitte nennt mir den Eingriff, bei dem „TODO: OPS-Ziffern werden nachgetragen" steht, damit ich prüfe, ob dort Daten fehlen.

4. **Lapidus-Warnung:** bleibt, aber neu formuliert und bereits als `hinweise`-Warnung im Eintrag `lapidus` hinterlegt (siehe Sprachregel unten). Die alte Zeile „nicht abrechenbar" war falsch.

5. **`erloesData.kodier` bleibt vorerst in den Daten** (Entscheidung des Autors: Reserve, bis die Auswertung einige Wochen im Alltag gelaufen ist). Anzeige: sobald `HDRG_REGELN` vorhanden ist, `kodier` nicht mehr rendern, sonst stehen die 57 Kodezeilen doppelt neben der Auswertung. Ohne Regelsatz wie bisher. Das Entfernen der alten `ausschluss`/`aufwertung`/`kontext`-Blöcke aus den Daten verschiebt sich entsprechend.

**Sprachregel (Autor, 09.09.2026), gilt für Konsequenz-Zeile, Warnungen und Gegenprobe:** Der AOP-Katalog bindet nur Kliniken; niedergelassene Operateure dürfen die Eingriffe ambulant über den EBM abrechnen. Deshalb nie „ambulant unvergütet" oder „nicht abrechenbar" schreiben, sondern nur den Sachverhalt und die Empfehlung: „<Kode> steht nicht im AOP-Katalog, für Kliniken ambulant daher Hybrid empfohlen." Auf der Datenseite ist das umgesetzt: `ausschluss.ziel` bei Chevron, Chevron mit Akin, Scarf, Youngswick, DMMO und Weil lautet jetzt „keine Hybrid-DRG: stationär I20E/I20F; 5-788.54/55 stehen nicht im AOP-Katalog, für Kliniken ambulant daher Hybrid empfohlen", und der `_kommentar` in `HDRG_REGELN` ist angepasst. Für den Code heißt das: Der Satzbaustein „ambulant nur mit unvergüteten …" aus dem Nachtrag vom 07.09. (Zeile 4 der Gegenprobe, Konsequenz-Zeile bei 5-788.54/55 und 5-788.60) wird ersetzt durch „… führt aus I20O heraus. Stationär I20E. Ambulant: 5-788.54 steht nicht im AOP-Katalog, für Kliniken daher Hybrid empfohlen." Die Gegenprobe-Zeilen 3 und 4 oben gelten mit dieser Formulierung.

## Nachtrag 09.09.2026, vierter Teil: Antwort auf eure beiden Rückfragen, neuer Teilauftrag

Der Autor hat entschieden: Alle vier fest im Code stehenden OP-Bericht-Zweige (Metallentfernung `app.html:5098`, Achillessehnen-Tendoskopie und AS-Débridement `app.html:5121–5125`, diabetischer Fuß, Unfallchirurgie) werden auf `OP_STEUERUNG` umgestellt.

1. **Schlüssel:** `metallentfernung` wie von euch vorgeschlagen. Der Zustand `hasME` (`meOp.length>0 || (meRegion && meImpl)`) bleibt der Auslöser im Generator; er wählt dann den Eintrag `OP_STEUERUNG.metallentfernung` statt des Literal-Objekts. Für Achillessehne gelten die vorhandenen Einträge `as_tendoskopie` und `as_debridement` (beide `drg: "I27E"`), für diabetischen Fuß und Unfallchirurgie die Schlüssel, die ihr aus den heutigen Zweigen ableitet; bitte im Nachtrag benennen.

2. **Werte 1:1:** Die Erlöswerte, Labels und Kodes der vier Zweige übernehmt ihr unverändert aus dem Code in `opsteuerung.json` (oberste Regel aus CLAUDE.md: keine Korrektur, keine Vereinheitlichung) und prüft Wert für Wert nach dem Muster von `scripts/verify_extraction.py`. Weil `data/*.json` gitignored ist, ist das eine Datei-Änderung mit Eintrag in DEPLOY.md Abschnitt D; `opsteuerung.json` steht dort ohnehin als offener Upload.

3. **Hinweise:** Sobald der Eintrag `metallentfernung` existiert, hänge ich die ICD-Hinweise an (`hinweise` Typ `info`: Hauptdiagnose Z47.0 bei Entfernung einer Metallplatte oder Fixationsvorrichtung; Nebendiagnosen bei Komplikation T84.6 Infektion, M84.1 Pseudarthrose). Bitte meldet, wenn die Einträge angelegt sind, damit ich nicht in eine Datei schreibe, die ihr gerade ändert.

4. **TODO-Zeile:** entfällt mit der Umstellung, die Daten liegen bereits in den beiden Achillessehnen-Einträgen.

5. **Reihenfolge:** Dieser Teilauftrag läuft nach den Punkten 1 bis 5 des dritten Teils (Verweildauer-Zeile, `kodier` ausblenden, Sprachregel), damit die Auswertung im OP-Bericht am Ende für alle Eingriffe aus derselben Quelle kommt.

## Nachtrag 09.09.2026, fünfter Teil: Schema für `metallentfernung`, Umgang mit den 31 Zweigen

Antwort auf eure Analyse (31 Literal-Objekte im Fuß-Erlösmemo, 28 davon parallel in `OP_STEUERUNG`, unpassende Schemata). Der Autor hat entschieden:

1. **Schema: OP_STEUERUNG-Konvention**, euer Vorschlag. `metallentfernung` bekommt `hdrg: null`, `drg: null`, `empf: "amb"` und die übrigen Felder in der Schreibweise der Datei („—" wird `null`, wie bei `morton_neurom`). Die Freitexte `ziel` und `kodier` werden `hinweise` vom Typ `info`, inhaltlich unverändert. Kein zweites Schema in der Datei. Laufzeitwerte (die gesammelte Kodeliste `ops: o`, bedingte Labels, der aus Schaltern zusammengesetzte DF-`kodier`) bleiben im Code; die Datei trägt nur, was statisch ist.

2. **Jetzt nur drei Zweige:** `metallentfernung` neu anlegen, Achillessehne auf die vorhandenen `as_tendoskopie` und `as_debridement` (I27E, löst den Widerspruch zu `drg: "—"` und der TODO-Zeile), diabetischer Fuß auf `df_debridement` und `df_amputation`. Unfallchirurgie entfällt. Wertevergleich nach dem Muster von `scripts/verify_extraction.py`, DEPLOY.md Abschnitt D, Vollzugsmeldung; danach hänge ich die ICD-Hinweise an `metallentfernung`.

3. **Die 28 Doppelpflege-Zweige bekommen einen eigenen Auftrag nach dem dritten Durchgang.** Erster Schritt dort ist kein Umbau, sondern ein Vergleich: je Zweig die Werte im Code gegen den Eintrag in `opsteuerung.json` (hdrg, drg, empf, Hebel, Kodes, Texte), Abweichungen als Liste an den Autor zur Entscheidung, welche Seite gilt. Erst danach die Umstellung, ebenfalls in der OP_STEUERUNG-Konvention. Bitte den Vergleich schon jetzt als Datei vorbereiten, wenn er sich beim Umzug der drei Zweige nebenbei erzeugen lässt; entschieden wird er separat.
