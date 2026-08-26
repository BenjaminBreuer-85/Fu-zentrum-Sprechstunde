# Auftrag: Teilamputation im OP-Bericht und Sprechstundenbrief-Vorlage diabetischer Fuß

Zweiter Teil zu `auftrag-op-text-diabetischer-fuss.md`.

## 1. Neuer Toggle „Teilamputation Knochen"

`data/optexte.json` enthält bereits den neuen Schlüssel **`df_zusatz_teilamputation`** (von mir eingetragen, Datei muss hochgeladen werden).

Der Toggle wird in der Reihenfolge **vor** den vier bisherigen Zusätzen eingefügt, also direkt nach dem Absatz zur Knochenbeurteilung im Basistext. Grund: Die Amputation geschieht vor Spülung, lokalem Antibiotikum und Wundabschluss.

Endgültige Reihenfolge der Zusätze: Teilamputation, Lavanox, Vancomycin, Lasche, VAC.

### Zwei automatische Folgen beim Setzen dieses Toggles

**a) Histologie.** Der Text enthält den Satz zur vollständigen Einsendung des Resektats bereits fest. Zusätzlich soll das Werkzeug den histologischen Befund als Auftrag mitführen, so wie es bei anderen Eingriffen mit Resektat geschieht (Vorbild: `morton_neurom`, dort steht „Das Resektat wird zur histopathologischen Untersuchung asserviert"). Wenn es im Werkzeug eine Kennzeichnung „Histologie angefordert" gibt, wird sie durch diesen Toggle automatisch gesetzt und darf nicht abwählbar sein: Bei einer Knochenteilamputation wegen Infekt ohne Histologie fehlt der Nachweis, wie weit der Befall reichte.

**b) Zweite Diagnose.** Mit dem Toggle wird neben „Diabetischer Fuß" automatisch die Diagnose **„Osteomyelitis"** gesetzt. Sie ist die Begründung des Eingriffs, und ohne sie trägt weder der Bericht noch die Kodierung. Die Diagnose ist abwählbar für den Fall, dass sich der Verdacht intraoperativ nicht bestätigt; wird sie abgewählt, soll ein Hinweis erscheinen, dass der Berichtstext dann anzupassen ist.

## 2. Zwei neue Diagnosen in `data/diagnosen.json`

Die fertigen Einträge liegen als `diagnose-diabetischer-fuss.json` bei und werden unverändert nach `DIAG` übernommen: `diabetischer_fuss` und `osteomyelitis`.

**Einordnung im Sprechstundenbrief:** eigene Gruppe **„Diabetischer Fuß"** unterhalb von „Sehnen und Faszien", vor „Unspezifisch". Beide Diagnosen stehen dort.

### Was die Befundliste leistet

20 Befunde für den diabetischen Fuß, vier für die Osteomyelitis. Die Zahl ist hoch, und zwar aus einem Grund: Bei dieser Diagnose entscheidet nicht das Ergebnis über den Beweiswert, sondern das dokumentierte Verfahren. „Sensibilität intakt" ist im Streitfall wertlos, „10-g-Monofilament an allen drei Prüfstellen wahrgenommen" nicht.

Die Reihenfolge folgt dem Untersuchungsgang: Ulzeration, Knochenkontakt, Deformität, Durchblutung, Neuropathie, Zusammenfassung.

**Ulzeration** (4 Befunde) mit Lage und Größe, Randwall, Sekret und lokalen Infektzeichen.

**Knochenkontakt** (2) trennt den Probe-to-bone-Test vom freiliegenden Knochen. Das sind zwei verschiedene Aussagen: Der Test kann positiv sein, ohne dass Knochen sichtbar ist.

**Deformität** (2) unterscheidet die plantare Prominenz als Druckursache vom Verdacht auf eine Charcot-Arthropathie.

**Durchblutung** (5) mit Pulsen, Rekapillarisierung, Doppler-Kurvenform und den beiden Messwerten. Die Grenzwerte stehen im Text, damit sie nicht nachgeschlagen werden müssen: Knöchel-Arm-Index normal zwischen 0,9 und 1,3, Zehen-Arm-Index unter 0,7 pathologisch, Zehendruck unter 30 mmHg als Schwelle zur Revaskularisation. Die negative Fassung führt die Konsequenz mit, damit die Weiterleitung dokumentiert ist.

**Neuropathie** (6) nach den Prüfverfahren der IWGDF-Leitlinie, jedes mit seinem eigenen Kriterium:

- 10-g-Monofilament an drei Prüfstellen je Fuß, eine Stelle gilt erst als wahrgenommen, wenn zwei von drei Anwendungen richtig beantwortet werden
- Stimmgabel 128 Hz nach Rydel-Seiffer mit Zahlenwert am Großzehengrundgelenk und am Innenknöchel; über 6/8 unauffällig, ab 40 Jahren bis 4/8 und ab 85 Jahren bis 3/8 altersentsprechend
- Ipswich Touch Test an Zehe 1, 3 und 5 als Verfahren ohne Hilfsmittel; auffällig ab zwei nicht wahrgenommenen Stellen
- Temperaturempfinden, Spitz-stumpf-Diskrimination und Achillessehnenreflex je einzeln

**Der letzte Befund** fasst zusammen, ob ein Verlust der Schutzsensibilität besteht, und nennt in der negativen Fassung die Zahl der Verfahren, in denen er nachgewiesen wurde. Das ist der Satz, der später zitiert wird; die sechs Einzelbefunde darüber sind seine Begründung. Ein einzelnes Verfahren genügt dafür nicht, deshalb ist die Zahl im Text vorgesehen.

`diagnoseText` enthält Platzhalter für **Wagner und Armstrong**. Beide Klassifikationen liegen bereits in `referenz.json` und sollten, wenn das Werkzeug das kann, von dort verlinkt werden.

Der erste Befund weicht bewusst vom Muster der anderen Diagnosen ab: Dort beginnt die Liste mit „Die Haut ist reizlos, die periphere Durchblutung, Motorik und Sensibilität sind intakt". Beim diabetischen Fuß ist genau das der zu prüfende Befund und kein Vorspann.

**Zur Bedienbarkeit:** 20 Befunde sind für eine Chip-Liste viel. Wenn das Listenmuster aus `auftrag-listenmuster.md` umgesetzt ist, sollten sie in Untergruppen erscheinen (Ulzeration, Knochen, Deformität, Durchblutung, Neuropathie). Bis dahin trägt die Reihenfolge allein.

## 3. OPS und Erlös

Für die Teilamputation kommt zusätzlich zu den im ersten Auftrag genannten Codes die Gruppe 5-865 (Amputation und Exartikulation Fuß) in Betracht, je nach Höhe der Absetzung. Die Zuordnung gehört über den Katalog geprüft und von Benjamin bestätigt, bevor sie in die Erlöslogik geht. Die Osteomyelitis ist als Nebendiagnose erlösrelevant und sollte in `opsteuerung.json` entsprechend hinterlegt werden.

## Deploy

- **Supabase, Bucket `toolbox-data`:** `optexte.json` löschen und neu hochladen (enthält die sechs `df_*`-Schlüssel). `diagnosen.json` löschen und neu hochladen, sobald die beiden Diagnosen eingetragen sind.
- **Repo (Push):** `app.html` für Toggle, Reihenfolge, Histologie-Kennzeichnung, Diagnosen-Kopplung und die neue Gruppe im Auswahlbaum.
- **Reihenfolge:** erst Bucket, dann Push.
