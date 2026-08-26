# Auftrag: neuer OP-Text „Diabetischer Fuß — Debridement bei Ulkus und Infekt"

Neuer Eintrag in `data/optexte.json` unter `T`, dazu vier Zusatztexte als Toggles. Datei liegt im Bucket, also **nach der Änderung Upload nach `toolbox-data`**, nicht nur Push.

## Schlüssel

| Schlüssel | Rolle |
|---|---|
| `df_debridement` | Basistext |
| `df_zusatz_lavanox` | Toggle „Lavanox-Spülung" |
| `df_zusatz_vancomycin` | Toggle „Vancomycin lokal" |
| `df_zusatz_lasche` | Toggle „Drainage-Lasche" |
| `df_zusatz_vac` | Toggle „VAC-Auflage" |

## Reihenfolge und eine Besonderheit

Die vier Zusätze werden **vor** dem letzten Absatz des Basistextes eingefügt, in genau dieser Reihenfolge: Lavanox, Vancomycin, Lasche, VAC. Sie beschreiben den zeitlichen Ablauf am Ende des Eingriffs.

**Wichtig:** Der letzte Absatz des Basistextes beschreibt die offene Wundbehandlung mit Verband. Ist der VAC-Toggle gesetzt, **ersetzt** `df_zusatz_vac` diesen letzten Absatz, statt vor ihm eingefügt zu werden. Sonst stünden zwei sich widersprechende Wundabschlüsse im Bericht.

Lasche und VAC schließen sich in der Praxis meist aus. Wenn sich das im Werkzeug ohne Aufwand abbilden lässt, sollten sie sich gegenseitig ausschalten; ist das aufwendig, bleiben beide wählbar, denn es gibt Fälle mit Lasche in einer Nebenhöhle und VAC auf der Hauptwunde.

## Basistext `df_debridement`

```
Die Indikation zum Debridement bei diabetischem Fußsyndrom mit Ulzeration und Infekt wurde gestellt. Über den Eingriff, die Möglichkeit der intraoperativen Erweiterung bis hin zur Amputation von Gewebe- oder Zehenanteilen, über die Notwendigkeit wiederholter Eingriffe sowie über die Risiken wurde aufgeklärt. Der Gefäßstatus wurde präoperativ erhoben ([tastbare Fußpulse / dopplersonografisch dokumentierte Perfusion / angiologisch abgeklärt]).

Lagerung in Rückenlage. [Auf eine Blutsperre wurde mit Rücksicht auf die periphere Durchblutung bewusst verzichtet.] Hautdesinfektion und steriles Abdecken unter Einschluss des gesamten Fußes.

Befund bei Eingriffsbeginn: Ulzeration [am Vorfuß plantar unter dem Metatarsaleköpfchen §SEITE§], Durchmesser ca. [2] cm, umgeben von einem hyperkeratotischen Randwall. Aus der Wunde entleert sich [trübes Sekret]. Sondierung der Wunde: Die Wundhöhle reicht [bis auf den Knochen (positiver Probe-to-bone-Test)]. Ausdehnung des Infektes nach [proximal entlang der Beugesehnenscheide] [nicht] nachweisbar.

Abtragung des hyperkeratotischen Randwalls. Exzision der Ulkusränder im Gesunden. Schrittweises Debridement in die Tiefe unter fortlaufender Beurteilung der Gewebevitalität anhand von Farbe, Konsistenz und Blutungsverhalten. Avitales Gewebe, Fibrinbeläge und infiziertes Fettgewebe werden vollständig entfernt, bis allseits gut durchblutete, blutende Wundflächen vorliegen.

Entnahme von [drei] Gewebeproben aus verschiedenen Arealen der Wundtiefe zur mikrobiologischen Untersuchung. Auf einen alleinigen Oberflächenabstrich wurde verzichtet, da Gewebeproben die zuverlässigere Erregerdiagnostik erlauben. Zusätzlich Asservierung einer Probe zur histopathologischen Untersuchung.

Beurteilung des Knochens: [Der freiliegende Knochen zeigt sich weich, verfärbt und mit dem Löffel abtragbar, sodass von einer Osteomyelitis auszugehen ist. Resektion der befallenen Knochenanteile am §KNOCHEN§ bis in makroskopisch gesunde, spongiöse und blutende Verhältnisse. Eine gesonderte Knochenprobe wird für die Mikrobiologie und eine weitere für die Histologie asserviert.] [Der Knochen stellt sich fest und regelrecht dar, ein Anhalt für eine Osteomyelitis besteht nicht.]

Erneute Kontrolle der Wundverhältnisse. Es verbleibt kein makroskopisch avitales Gewebe. Kontrolle auf Bluttrockenheit.

Steriler Wundverband mit [nicht haftender Wundauflage] und Polsterung. Der Fuß wird in einem [Entlastungsschuh / Vorfußentlastungsschuh] versorgt. Ein Second-Look-Eingriff mit erneutem Debridement ist für [den dritten postoperativen Tag] vorgesehen und wurde mit dem Patienten besprochen. Die antibiotische Therapie wird nach Eintreffen des Antibiogramms angepasst.
```

## Zusatztext `df_zusatz_lavanox`

```
Ausgiebige Spülung der Wundhöhle mit Lavanox. Belassen der Lösung über eine Einwirkzeit von [3] Minuten, anschließend Absaugen und Nachspülen.
```

## Zusatztext `df_zusatz_vancomycin`

```
Lokale Applikation von [1] g Vancomycin-Pulver in die Wundhöhle und auf die Resektionsflächen. Die lokale Anwendung erfolgt außerhalb der Zulassung; die Indikation wurde in Abwägung des Infektrisikos und der Ausdehnung des Befundes gestellt, der Patient ist darüber aufgeklärt.
```

## Zusatztext `df_zusatz_lasche`

```
Einlage einer Drainage-Lasche in die Wundhöhle mit Ausleitung über [die bestehende Wunde]. Fixation der Lasche mit einer Hautnaht. Entfernung nach [zwei] Tagen vorgesehen.
```

## Zusatztext `df_zusatz_vac` (ersetzt den letzten Absatz des Basistextes)

```
Anlage einer Vakuumversiegelung. Zuschnitt des Schwammes passend zur Wundfläche ohne Kontakt zu freiliegenden Gefäß- oder Sehnenstrukturen, Abdeckung mit Folie und Anschluss an einen kontinuierlichen Sog von [125] mmHg. Kontrolle auf Dichtigkeit, der Schwamm kollabiert regelrecht. Der Fuß wird in einem [Entlastungsschuh] versorgt. Der Verbandwechsel mit erneutem Debridement ist für [den dritten postoperativen Tag] vorgesehen und wurde mit dem Patienten besprochen. Die antibiotische Therapie wird nach Eintreffen des Antibiogramms angepasst.
```

## Warum der Text so gebaut ist

Vier Angaben tragen die rechtliche Absicherung und stehen deshalb fest im Text, nicht als Option:

1. **Der Gefäßstatus vor dem Eingriff.** Ein Debridement am schlecht durchbluteten Fuß ohne dokumentierte Perfusionsbeurteilung ist der häufigste Angriffspunkt im Streitfall.
2. **Die Aufklärung über eine mögliche Erweiterung bis zur Amputation.** Beim diabetischen Fuß ist die intraoperative Erweiterung Regelfall, nicht Ausnahme.
3. **Die Sondierung mit Probe-to-bone-Befund.** Sie ist der Befund, aus dem die Entscheidung über die Knochenresektion folgt, und muss deshalb dokumentiert sein.
4. **Gewebeproben statt Abstrich, mehrere und getrennt asserviert.** Das entspricht dem Vorgehen der internationalen Leitlinien und wurde zuletzt in einer Metaanalyse zum Vergleich von Abstrich und Biopsie bestätigt (PMID 42630424). Der Satz „Auf einen alleinigen Oberflächenabstrich wurde verzichtet" begründet die eigene Vorgehensweise mit.

Die Formulierung zur Vitalitätsbeurteilung („Farbe, Konsistenz und Blutungsverhalten") ist bewusst konkret: Sie belegt, dass die Grenze des Debridements nach einem nachvollziehbaren Kriterium gezogen wurde.

Beim Vancomycin steht der Off-Label-Charakter ausdrücklich im Text. Das ist kein Formfehler, sondern der Punkt, der die Anwendung überhaupt vertretbar dokumentiert.

## Noch zu klären

**Die OPS-Zuordnung** habe ich bewusst nicht festgelegt. In Betracht kommen je nach Ausdehnung Codes aus 5-893 (chirurgische Wundtoilette), 5-896 (radikale und ausgedehnte Exzision an Haut und Unterhaut), bei Knochenbeteiligung zusätzlich 5-782 (Exzision und Resektion von erkranktem Knochen) und für die Vakuumversiegelung 5-916.a0. Welche Kombination im Einzelfall trägt, hängt an Tiefe, Ausdehnung und Knochenbeteiligung. Bitte über den Katalog des Werkzeugs zuordnen und von Benjamin gegenprüfen lassen, bevor der Eintrag in die Erlöslogik aufgenommen wird.

**Die Einordnung im Auswahlbaum:** Der Eintrag passt weder unter Vorfuß noch unter Rückfuß, weil er sich nach der Region richtet, nicht nach dem Eingriff. Vorschlag: eine eigene Gruppe „Diabetischer Fuß / Infekt" in der OP-Durchführung, die später weitere Einträge aufnehmen kann (Zehenamputation, Strahlresektion, transmetatarsale Amputation).

Deploy: `data/optexte.json` ändern, in den Bucket `toolbox-data` hochladen (erst löschen, dann hochladen), zusätzlich `app.html` für die Toggle-Anbindung. Commit durch die Code-Sitzung, Push und Upload durch Benjamin.
