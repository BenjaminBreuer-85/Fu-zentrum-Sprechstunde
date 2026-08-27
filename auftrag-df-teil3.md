# Auftrag: diabetischer Fuß, Korrekturen nach dem ersten Test

Zwei Befunde aus dem Test am Gerät, dazu die Zuordnung der OP-Methoden.

## 1. Befundtexte werden am ersten Komma abgeschnitten

In der klinischen Untersuchung zeigt die Chip-Liste nur den Text bis zum ersten Komma:

| angezeigt | gemeint |
|---|---|
| „Trübes" | „Trübes, teils fötides Sekret aus der Wunde" |
| „Rötung" | „Rötung, Überwärmung und Schwellung im Sinne einer Weichteilinfektion" |
| „Knöchel-Arm-Index [1" | „Knöchel-Arm-Index [1,05], im Normbereich zwischen 0,9 und 1,3" |
| „Zehen-Arm-Index [0" | „Zehen-Arm-Index [0,8] und Zehendruck [65] mmHg, …" |
| „Ipswich Touch Test an Zehe 1" | „… an Zehe 1, 3 und 5 beidseits sicher wahrgenommen" |

Das Muster ist eindeutig: Die Anzeige übernimmt `pos` nur bis zum ersten Komma. Bei den Altbeständen fiel das kaum auf („Die Haut ist reizlos, …" wurde zu „Die Haut ist reizlos", was als Kurzform noch trug). Bei den neuen Befunden zerstört es die Aussage, und beim Knöchel-Arm-Index schneidet sogar das **Dezimalkomma** ab.

**Fix in `app.html`:** Die Chip-Beschriftung zeigt den vollständigen `pos`-Text. Umbruch über mehrere Zeilen ist in der Liste bereits vorgesehen (der Monofilament-Befund läuft heute schon dreizeilig sauber). Die Kürzung am Komma entfällt ersatzlos; falls sie irgendwo bewusst als Kurzlabel diente, wäre ein optionales Feld `kurz` je Befund der saubere Weg — dann zeigt die Liste `kurz`, wenn vorhanden, sonst den vollen Text. Der Brieftext selbst war nie betroffen und bleibt unverändert.

Gegenprobe: Diagnose diabetischer Fuß öffnen, alle 20 Befunde vollständig lesbar, insbesondere die fünf oben genannten.

## 2. Osteomyelitis als eigene Diagnose entfernen

Die Gruppe „Diabetischer Fuß" im Sprechstundenbrief enthält derzeit zwei Chips. Die Osteomyelitis fliegt raus — sie ist Bestandteil des diabetischen Fußes, keine parallele Auswahl. Der Eintrag `osteomyelitis` wird aus `DIAG` in `data/diagnosen.json` gelöscht, die Gruppe behält nur „Diabetischer Fuß". Die aktualisierte Vorlage liegt als `diagnose-diabetischer-fuss.json` bei (enthält jetzt nur noch diesen einen Eintrag).

Unberührt davon bleibt der OP-Bericht-Generator: Dort setzt der Toggle „Teilamputation Knochen" weiterhin die Osteomyelitis als Diagnose in den Bericht (`auftrag-df-teil2.md`, Punkt 1b) — das ist Berichtslogik, keine Sprechstunden-Auswahl.

## 3. OP-Methoden: Labels statt Rohschlüssel

Der Chip zeigt derzeit wörtlich „df_debridement", weil in `data/opmethoden.json` der Eintrag fehlt. Die beiden Einträge liegen als `opmethoden-diabetischer-fuss.json` bei und werden nach `OPS` übernommen:

- **`df_debridement`** — Label „Debridement". OP-Plan-Text (`t`) wörtlich nach Vorgabe: „Exploration, schichtübergreifendes Debridement, Probenentnahme, Debridement Knochen/ggf. Teilresektion, befundbezogenes Vorgehen, ggf. mehrzeitiges Vorgehen"
- **`df_amputation`** — Label „Amputation proximale Tibia"

`diagnosen.json` verweist im Eintrag `diabetischer_fuss` auf beide (`opMethoden: ["df_debridement", "df_amputation"]`).

Der Hinweis „Keine Online-Information — der Brief enthält keinen QR-Code" ist korrekt: In der Patienten-App gibt es noch keinen Begleiter für das Debridement beim diabetischen Fuß. Das bleibt so, bis dort einer existiert.

## Deploy

- **Supabase, Bucket `toolbox-data`:** `diagnosen.json` (Osteomyelitis raus, opMethoden erweitert) und `opmethoden.json` (zwei neue OPS-Einträge) — jeweils löschen und neu hochladen. `optexte.json` unverändert gegenüber dem Stand vom 26.08. (sechs `df_*`-Schlüssel), falls noch nicht hochgeladen, jetzt mit.
- **Repo (Push):** `app.html` für die Chip-Beschriftung (Punkt 1).
- Reihenfolge: erst Bucket, dann Push. `DEPLOY.md` Abschnitt D nachführen.

## 4. OP-Text zur Amputation proximale Tibia

`data/optexte.json` enthält jetzt zusätzlich den Schlüssel **`df_amputation_tibia`** (T gesamt: 104). Der Text folgt der Technik nach Burgess mit langem dorsalem Muskel-Haut-Lappen, wie sie in der aktuellen deutschsprachigen Übersicht beschrieben ist (Operationstechniken der Ober- und Unterschenkelamputation, Die Unfallchirurgie 2024):

- Gefäßstatus und Wahl der Amputationshöhe nach Perfusion und Weichteilbefund, Blutsperre als Klammer-Option (beim ischämischen Bein verzichtet man darauf)
- Ligatur der A./V. tibialis anterior und posterior sowie der V. saphena magna
- Traktionsneurektomie von N. tibialis (ca. 3–4 cm proximal der Resektion), N. peronaeus (ca. 2–3 cm proximal der Fibularesektion), N. suralis und Verlagerung des N. saphenus
- Fibulaosteotomie ca. 1 cm proximal der Tibiahöhe, Anschrägen der ventralen Tibiakante gegen das Anschlagen im Prothesenschaft
- Myoplastik des dorsalen Gastrocnemiuslappens über der Resektionsfläche, alternativ transossäre Myopexie als Klammer
- Redon-Drainage, spannungsfreier Verschluss, bei kritischer Durchblutung Klammerpflaster statt Nähte
- als Klammern: Gewebeproben aus dem Absetzungsrand plus Histologie des Amputats (Infektkontext), Ausdünnen des M. soleus, zweizeitiges Vorgehen bei ausgedehntem Infekt
- postoperative Zeile zu Stumpfwicklung und Strecklagerung gegen die Beugekontraktur

Der OP-Bericht-Generator bindet den Eingriff in der neuen Gruppe „Diabetischer Fuß / Infekt" ein, neben dem Debridement. Die fünf Debridement-Toggles gelten hier **nicht** — die Amputation hat ihren Wundabschluss im eigenen Text.

OPS-Zuordnung zur Prüfung durch Benjamin: 5-864.- (Amputation und Exartikulation, Unterschenkel), genaue Endstelle nach Höhe; Diagnosen im Bericht: diabetisches Fußsyndrom, bei Knochenbefall zusätzlich Osteomyelitis.

Deploy unverändert: `optexte.json` in den Bucket (löschen, neu hochladen) — der Stand vom heutigen Tag enthält alle sieben `df_*`-Schlüssel.
