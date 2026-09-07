# Prüfung der OP-Chips und Brieftexte auf Unstimmigkeiten (wie beim USG-Fall)

Stand: 07.09.2026. Geprüft: alle 58 Einträge in `data/opmethoden.json` → `OPS` (Chip-Beschriftung `k`, Aufklärungssatz `b`, Brieftext `t`) sowie die Zuordnung zur Patienten-App (`PATIENT_EINGRIFF_MAP`). Die Diagnosetexte aus `data/diagnosen.json` konnten noch nicht geprüft werden (Datei nicht erreichbar, siehe Ende).

Prüffrage: Sagt der Brieftext etwas anderes oder mehr als der angeklickte Chip, nennt er die falsche Struktur, oder lässt er offen, welche Struktur gemeint ist, obwohl der Brief das braucht?

## A. Gleiche Fehlerklasse wie beim USG-Fall (Text behauptet mehr oder anderes als der Chip)

**1. `lapidus` — Brieftext enthält Akin-Osteotomie, die der Chip nicht verspricht.**
Chip „Lapidus-Arthrodese", Aufklärung „eine modifizierte Lapidus Arthrodese (Versteifung TMT I Gelenk)", Brief „modifizierte Lapidus Arthrodese (=Versteifung TMT I Gelenk), Weichteilkorrektur, Akin-Osteotomie, ggf. subcapitale Korrekturosteotomie additiv". Der Brief legt eine Akin-Osteotomie fest, obwohl weder Chip noch Aufklärung sie nennen. Vorschlag: entweder Chip und Aufklärung auf „Lapidus + Akin" erweitern (analog zu „Chevron + Akin"), oder Akin und subcapitale Osteotomie aus dem Brieftext streichen und bei Bedarf als eigenen Chip anbieten. Nebenbei: Schreibweise „Lapidus Arthrodese" ohne Bindestrich in `b` und `t`, im Chip mit Bindestrich.

**2. `arthrodese_tmt` — „Versteifung der Tarsometatarsalgelenke" ohne Angabe, welche.**
Chip „TMT-Arthrodese", Aufklärung „eine Versteifung der Tarsometatarsalgelenke", Brief „Arthrodese (=Versteifung) der Tarsometatarsalgelenke". Die Mehrzahl klingt nach allen fünf. Gemeint sind in der Regel TMT II und III (Lisfranc-Arthrose), TMT I läuft als Lapidus. Für die Kodierung ist die Zahl der Gelenkfächer entscheidend (5-808.a4/a5/a6, dazu die 801D-Falle in `opsteuerung.json`). Vorschlag: gleiche Lösung wie beim USG, Text abhängig von der Auswahl der Gelenke, oder drei Chips „TMT II", „TMT II+III", „TMT II bis IV".

**3. `peroneal_naht` — Brieftext sagt „Naht/-rekonstruktion", obwohl es den Chip `peroneal_rek` daneben gibt.**
Chip „Peronealsehnennaht", Aufklärung „eine Naht/Rekonstruktion der Peronealsehne", Brief „Peronealsehnennaht/-rekonstruktion". Wer die Naht anklickt, bekommt im Brief auch die Rekonstruktion. Vorschlag: bei `peroneal_naht` auf „Naht der Peronealsehne" beschränken, die Rekonstruktion bleibt bei `peroneal_rek`. Zusatz für beide: welche Sehne (Peroneus brevis, longus, beide) fehlt.

**4. `coalition_exzision` — Text passt zur talokalkanearen Koalition, Patienten-Link zeigt auf die kalkaneonavikuläre.**
Aufklärung „Exzision der Koalition mit Interposition eines autologen Faszien-Fett-Flaps vom Unterschenkel" (typisches Vorgehen bei der talokalkanearen Koalition), `PATIENT_EINGRIFF_MAP` verweist auf `coalitio_cn` (kalkaneonavikulär, dort üblicherweise Interposition des M. extensor digitorum brevis oder Fett). Vorschlag: zwei Chips (Coalitio CN, Coalitio TC) mit jeweils passendem Interponat und passendem Patienten-Artikel.

**5. `supramal_ot` — Richtung fehlt, Patienten-Link zeigt immer auf die Valgus-Variante.**
Chip „Supramalleolare OT", Brief „Supramalleolare Umstellungsosteotomie", Patienten-Link `smot_valgus`. Bei einer varisierenden Osteotomie landet der Patient im falschen Artikel. Vorschlag: zwei Chips (Valgus-Korrektur, Varus-Korrektur) oder Richtung als Zusatzauswahl mit angepasstem Link.

**6. `fhl_transfer` — Patienten-Link zeigt auf den Haglund-Artikel.**
Chip „FHL-Transfer" (Augmentation der insuffizienten Achillessehne), `PATIENT_EINGRIFF_MAP` → `haglund_split`. Der Patient liest nach dem Scan die Haglund-Aufklärung. Vorschlag: eigenen Artikel verlinken (Achillessehnen-Insuffizienz, `achilles_insuffizienz_kb` existiert als Krankheitsbild) oder bis dahin die Zuordnung entfernen, damit der Code auf das Krankheitsbild zurückfällt.

## B. Aufklärungssatz unvollständig oder von der Brieffassung abweichend

**7. Beckenkamm-Entnahme fehlt in der Aufklärung, steht aber fest im Brief.**
Betrifft `arthrodese_osg`, `subtalar_arthrodese`, `tn_arthrodese`, `double_arthrodese`, `triple_arthrodese`, `arthrodese_tmt`: Der Brieftext nennt „Augmentation durch autologe Beckenkammspongiosa" beziehungsweise „Beckenkammspan" als festen Bestandteil, der Aufklärungssatz `b` erwähnt die Entnahmestelle nicht. Die Beckenkammentnahme ist ein zweiter Eingriffsort mit eigenen Risiken (Hämatom, Schmerz, Nervenreizung) und gehört in die Aufklärung. Zweite Frage dahinter: Ist die Beckenkammentnahme wirklich immer Standard? Der Erlöshebel-Hinweis bei `arthrodese_osg` („5-783.0d + 5-784.0n hebt I13E auf I13D") legt nahe, dass sie fallweise erfolgt. Dann wäre im Brief „ggf." richtig oder die Augmentation ein eigener Chip, der Brief, Aufklärung und Kodierung gemeinsam steuert. Bei `lcot` und `cotton` steht „autologe oder allogene Spongiosa", das ist offen formuliert und in Ordnung.

**8. `gastroc_strayer` — Aufklärung koppelt den Eingriff an eine einzige Indikation.**
„… zur Korrektur der Wadenverkürzung als Ursache der plantaren Fersenschmerzsymptomatik". Der Strayer wird auch bei Achillessehnen-Tendinopathie, Vorfußüberlastung und diabetischem Fuß eingesetzt; der Satz passt dann nicht zur gestellten Diagnose. Vorschlag: „… zur Korrektur der Gastrocnemius-Verkürzung" ohne Indikationszusatz, die Indikation liefert die Diagnosezeile. `gastroc_pmgr` ist bereits so formuliert.

**9. `haglund_as_split` — Aufklärung ohne den Split.**
Chip „Haglund + AS-Split/Refix", Brief „mit Achillessehnen-Split und Refixation", Aufklärung nur „mit Achillessehnen-Refixierung". Der Split (Längsspaltung und teilweise Ablösung der Sehne) ist für den Patienten die relevante Information. Vorschlag: „mit Längsspaltung und Refixation der Achillessehne".

## C. Struktur nicht benannt, obwohl der Brief sie braucht (kein Fehler, aber Lücke)

**10. Zehen- und Strahlangaben fehlen:** `kleinzehen_pip` und `kleinzehen_weichteil` (welche Zehe, D2 bis D5), `morton_neurom` (welcher Zwischenraum, meist II/III oder III/IV), `dmmo` und `weil` (welche Metatarsalia, häufig II bis IV, für die OPS-Kodierung je Knochen relevant). Falls die Seite bereits automatisch angehängt wird, wäre eine analoge Zusatzauswahl für Zehe beziehungsweise Strahl die konsequente Lösung.

**11. `calcaneus_ot` — generischer Chip „zur Achskorrektur", Patienten-Link zeigt fest auf die medialisierende Variante (`calc_medial`).** Neben `mdo_offen`, `mdo_mini`, `hohlfuss_dwyer` und `lcot` ist unklar, wofür dieser Chip noch gebraucht wird. Wenn er bleibt, Link entfernen oder auf einen neutralen Artikel setzen.

**12. `bandplastik_autolog`** nennt weder Band noch Transplantat (Gracilis, Plantaris). Für den Brief ausreichend, für die Aufklärung dünn.

**13. Ohne Patienten-Zuordnung:** `exostose`, `kleinzehen_weichteil`, `os_tib_ext`, `df_debridement`, `df_amputation`, `hohlfuss_dwyer` ist zugeordnet. Bei den nicht zugeordneten fällt der QR-Code auf das Krankheitsbild zurück; das ist gewollt oder bewusst offen, nur zur Kenntnis.

## Sauber

Alle übrigen Einträge sind in sich stimmig: Chevron, Chevron + Akin, Scarf, Cheilektomie, Youngswick, MTP-I-Arthrodese, Exostose, Os tibiale externum, Dwyer, Lambrinudi, Brostrom-Gould, Brostrom + Internal Brace, ASK OSG, die drei OSG-TEP-Varianten, AMIC, OATS, MDO offen und mini-invasiv, LCOT, Cotton, TN-Arthrodese, Double, Triple, Arthrorise, Calcaneoplastie, FDL-Transfer, Achillessehnennaht, Peronealsehnen-Stabilisierung, TTC-Nagel, plantare Fasziotomie, PMGR, Achillessehnen-Tendoskopie, AS-Débridement, Debridement DFS, Amputation.

## Noch offen: `data/diagnosen.json`

Die Diagnosetexte (Chip-Beschriftung gegen Brieftext, wie beim USG-Fall „Arthrose des unteren Sprunggelenkes (Subtalargelenk)") sind der zweite Teil dieser Prüfung. Die Datei liegt nicht im gestageten Stand; sobald der Rechner erreichbar ist, wird sie nach demselben Raster geprüft und dieser Bericht ergänzt.

## Vorgeschlagene Reihenfolge

Zuerst A1 bis A3 (reine Textänderungen in `opmethoden.json`, kann ich direkt umsetzen), dann B7 und B9 (Aufklärungssätze, ebenfalls Daten), danach A4 bis A6 und C10 (neue Chips beziehungsweise Zusatzauswahl, Auftrag an die Code-Sitzung, weil `app.html` und Patienten-Links betroffen sind). Für B7 brauche ich vorher deine Entscheidung, ob die Beckenkammentnahme Standard ist oder fallweise gewählt wird.
