# Auftrag: OP-Chips, strukturelle Korrekturen nach Prüfung vom 07.09.2026

Grundlage: `pruefung-chips-brieftexte-2026-09-07.md` und die Entscheidungen des Autors. Die reinen Textkorrekturen (Lapidus mit Akin, Beckenkamm überall „ggf." und in der Aufklärung benannt, Peronealsehnennaht ohne Rekonstruktion, Strayer ohne Indikationszusatz, Haglund-Split in der Aufklärung, Bandplastik mit Hamstring- oder Plantarissehne, Coalitio-Interponat) sind bereits in `data/opmethoden.json` umgesetzt und brauchen keinen Code. Dieser Auftrag betrifft nur die Punkte, die neue Einträge, Verknüpfungen oder eine Zusatzauswahl brauchen. Bitte pro Punkt prüfen, welche Dateien betroffen sind (`opmethoden.json`, `opsteuerung.json`, `optexte.json`, `zuordnung/implantat_zuordnung.json`, `kurzlinks.json`, `app.html`) und DEPLOY.md Abschnitt D nachführen.

## 1. TMT-Arthrodese in drei Varianten aufteilen

Der bestehende Eintrag `arthrodese_tmt` („TMT-Arthrodese", Versteifung „der Tarsometatarsalgelenke") ist nicht eindeutig. Nachtrag 07.09.: In `opsteuerung.json` hat der Eintrag bereits Modifikatoren („3 Gelenke" → 5-808.a6 → I20C, „4–5 Gelenke" → 5-808.a7 → I20B) mit `textErsatz`. Wenn ihr die drei Varianten lieber über diesen Modifikator-Mechanismus abbildet statt über neue Chips, ist das gleichwertig; dann bitte die `textErsatz`-Texte auf „ggf. Augmentation durch autologe Beckenkammspongiosa" ändern und die OP-Bericht-Bausteine je Variante zuordnen. Ziel in beiden Fällen:

| Schlüssel | Chip `k` | Aufklärung `b` | Brief `t` | OPS-Vorschlag |
|---|---|---|---|---|
| `arthrodese_tmt1` | TMT-I-Arthrodese | eine Versteifung des ersten Tarsometatarsalgelenkes bei Verschleiß, ggf. mit Entnahme von Knochen aus dem Beckenkamm | Arthrodese (=Versteifung) des TMT-I-Gelenkes, ggf. Augmentation durch autologe Beckenkammspongiosa | 5-808.a4 (ein Gelenkfach) |
| `arthrodese_tmt` (bestehend, umbenennen) | TMT-II/III-Arthrodese | eine Versteifung des zweiten und dritten Tarsometatarsalgelenkes, ggf. mit Entnahme von Knochen aus dem Beckenkamm | Arthrodese (=Versteifung) der TMT-II- und TMT-III-Gelenke, ggf. Augmentation durch autologe Beckenkammspongiosa | 5-808.a5 (zwei Gelenkfächer) |
| `arthrodese_tmt13` | TMT-I-bis-III-Arthrodese | eine Versteifung des ersten bis dritten Tarsometatarsalgelenkes, ggf. mit Entnahme von Knochen aus dem Beckenkamm | Arthrodese (=Versteifung) der TMT-I- bis TMT-III-Gelenke, ggf. Augmentation durch autologe Beckenkammspongiosa | 5-808.a6 (drei Gelenkfächer) |

Bitte in `opsteuerung.json` den vorhandenen Hinweis zur 801D-Falle (5-808.a4 und a5 bei Diabetes-Hauptdiagnose) an alle drei Einträge hängen, die Fallsteuerung für a4 und a5 entsprechend prüfen. Patienten-Zuordnung (`PATIENT_EINGRIFF_MAP`): alle drei auf `tmt`, bis die Patienten-App eigene Varianten hat.

**OP-Bericht-Bausteine (`optexte.json`)**, Feldgliederung bitte wie beim Lapidus-Baustein (Lagerung, Blutsperre, Verschluss übernehmen):

TMT-I-Arthrodese: Medialer Längszugang über dem TMT-I-Gelenk, Präparation unter Schonung des N. cutaneus dorsalis medialis und der Sehne des M. tibialis anterior, Kapsulotomie und Darstellung des Gelenkes, Entknorpelung der Gelenkflächen mit Meißel und Kürette unter Erhalt der subchondralen Kontur, Anfrischung und Perforation der Sklerosezonen, Einstellung des ersten Strahls in anatomischer Position ohne Achskorrektur, temporäre Fixierung mit Kirschner-Drähten, Röntgenkontrolle in zwei Ebenen, definitive Fixierung mit winkelstabiler Platte und Zugschraube, ggf. Augmentation mit lokaler Spongiosa, Spülung, schichtweiser Wundverschluss.

TMT-II/III-Arthrodese: Dorsaler Längszugang zwischen zweitem und drittem Strahl über den TMT-II- und TMT-III-Gelenken, Präparation unter Schonung des Gefäß-Nerven-Bündels (A. dorsalis pedis, N. peroneus profundus) und der Strecksehnen, Kapsulotomie und Darstellung beider Gelenke, Entknorpelung mit Meißel und Kürette, Anfrischung und Perforation der Sklerosezonen, Einstellung in anatomischer Position, temporäre Fixierung mit Kirschner-Drähten, Röntgenkontrolle in zwei Ebenen, definitive Fixierung mit winkelstabiler Platte dorsal, ggf. Augmentation mit lokaler Spongiosa, Spülung, schichtweiser Wundverschluss.

TMT-I-bis-III-Arthrodese: Zwei Zugänge, medialer Längszugang über dem TMT-I-Gelenk und dorsaler Längszugang zwischen zweitem und drittem Strahl über den TMT-II- und TMT-III-Gelenken, ausreichend breite Hautbrücke. Präparation medial unter Schonung des N. cutaneus dorsalis medialis und der Tibialis-anterior-Sehne, dorsal unter Schonung des Gefäß-Nerven-Bündels (A. dorsalis pedis, N. peroneus profundus) und der Strecksehnen. Kapsulotomie und Darstellung aller drei Gelenke, Entknorpelung mit Meißel und Kürette, Anfrischung und Perforation der Sklerosezonen, Einstellung in anatomischer Position, temporäre Fixierung mit Kirschner-Drähten, Röntgenkontrolle in zwei Ebenen. Definitive Fixierung TMT II und III mit winkelstabiler Platte dorsal, TMT I mit winkelstabiler Platte und Zugschraube, ggf. Augmentation mit lokaler Spongiosa, Spülung, schichtweiser Wundverschluss.

Der vorhandene Baustein „Arthrodese TMT 1" im OP-Bericht-Generator beschreibt derzeit einen dorsalen Zugang (aus TMT II/III kopiert); er wird durch den Text oben ersetzt. Bei TMT I nur „winkelstabile Platte" ohne Lageangabe, weil medial und plantar beide vorkommen.

## 2. Peronealsehne als Zusatzauswahl

Bei `peroneal_naht`, `peroneal_rek` und `peroneal_lux` eine Zusatzauswahl nach dem Muster der Seitenangabe: „Peroneus brevis", „Peroneus longus", „beide". Die Auswahl fließt in Brief und Aufklärung ein (z. B. „Naht der Peroneus-brevis-Sehne"). Ohne Auswahl bleibt der generische Text.

## 3. Coalitio in zwei Chips

`coalition_exzision` aufteilen:

| Schlüssel | Chip | Aufklärung | Brief | Patienten-Link |
|---|---|---|---|---|
| `coalition_cn` | Coalitio CN | eine Exzision der kalkaneonavikulären Koalition mit Interposition eines körpereigenen Faszien-Fett-Lappens, ggf. über einen Zusatzschnitt am Unterschenkel | Resektion der kalkaneonavikulären Koalition mit Faszien-Fett-Interponat | `coalitio_cn` |
| `coalition_tc` | Coalitio TC | eine Exzision der talokalkanearen Koalition mit Interposition eines körpereigenen Faszien-Fett-Lappens, ggf. über einen Zusatzschnitt am Unterschenkel | Resektion der talokalkanearen Koalition mit Faszien-Fett-Interponat | `coalitio_tc`, falls in der Patienten-App vorhanden, sonst `coalitio_cn` und Rückmeldung an mich, dann lege ich den Artikel an |

OPS und Fallsteuerung vom bestehenden Eintrag übernehmen.

## 4. Supramalleoläre Osteotomie in zwei Chips

`supramal_ot` aufteilen in `supramal_valgus` („SMOT Valgus-Korrektur", Brief „Supramalleolare Umstellungsosteotomie zur Valgus-Korrektur", Patienten-Link `smot_valgus`) und `supramal_varus` („SMOT Varus-Korrektur", Brief „Supramalleolare Umstellungsosteotomie zur Varus-Korrektur", Patienten-Link `smot_varus`, falls vorhanden, sonst wie bei 3 melden). Aufklärung analog.

## 5. FHL-Transfer, Patienten-Link

`PATIENT_EINGRIFF_MAP.fhl_transfer` von `haglund_split` auf das Krankheitsbild `achilles_insuffizienz_kb` umstellen (mit `kbinfo`-Mechanik aus `auftrag-kbinfo-eingriff.md`, falls der Eingriff selbst keinen Artikel hat). Der Patient darf nach dem Scan nicht in der Haglund-Aufklärung landen.

## 6. Zehen- und Strahlauswahl

Zusatzauswahl nach dem Muster der Seitenangabe, Mehrfachauswahl erlaubt:
`kleinzehen_pip`, `kleinzehen_weichteil`: Zehe D2, D3, D4, D5.
`morton_neurom`: Zwischenraum II/III, III/IV.
`dmmo`, `weil`: Strahl MT II, MT III, MT IV.
Die Auswahl erscheint im Brief („Weil-Osteotomie MT II und III") und steuert die OPS-Anzahl (je Knochen ein Code). Ohne Auswahl bleibt der bisherige generische Text.

## 7. Chip `calcaneus_ot` entfernen

Der generische Chip „Calcaneus-OT" wird gestrichen; MDO offen, MDO mini-invasiv, Dwyer und LCOT decken alle Fälle ab. Bitte alle Verweise entfernen (`opsteuerung.json`, `optexte.json`, `implantat_zuordnung.json`, `PATIENT_EINGRIFF_MAP`) und prüfen, dass gespeicherte Fälle mit diesem Schlüssel nicht abstürzen (Fallback auf leeren Chip mit Hinweis).

## Gegenprobe

Sprechstundenbrief: jeden neuen oder geänderten Chip einmal anklicken, Brief- und Aufklärungstext lesen, QR-Ziel prüfen. OP-Bericht: die drei TMT-Bausteine erzeugen und den Zugang kontrollieren. Fallsteuerung: TMT I (a4) und TMT II/III (a5) mit Diabetes-Hauptdiagnose, 801D-Warnung muss erscheinen.
