# Redaktionsplan — offene Patienten-Inhalte

## Etappenplan der QR-Strecke (abgeschlossen 01.08.2026)

Der Plan stand bis zum 01.08.2026 nur in Commit-Betreffs und war nirgends
festgehalten. Hier der Stand nach Abschluss.

| Etappe | Inhalt | Stand |
|---|---|---|
| 1 | `404.html` als Router für `/i/<id>`, `kurzlinks.json` als einzige ID-Tabelle | erledigt; die drei Live-Gegenproben am 01.08. nachgeholt (siehe DEPLOY.md D2) |
| 2 | `data-tour`-Anker an Befund-Schaltern, Score, Eingriffswahl, OPS-/Erlösblock | erledigt |
| 3a | Deaktivierter Hinweis statt stillem Verschwinden, wenn kein Ziel existiert | erledigt, gilt inzwischen auch für Diagnosen |
| 3b | Ziel-Abdeckung: Eingriffe, Diagnosen, konservativ | erledigt — Diagnosen über eine eigene `PATIENT_DIAGNOSE_MAP` (Entscheidung 31.07.: zwei getrennte Codes), konservativ als Verweis auf die Startseite statt als Deep-Link |
| 3c | Kurzlink-Tabelle um alle Ziele ergänzt, IDs sprechend | erledigt, 53 IDs |
| 3d | Restliste ohne Ziel im Repo | erledigt — diese Datei (heißt `REDAKTIONSPLAN.md`, nicht `redaktionsplan-qr.md`) |
| 4 | Kurzadresse `fuss-track.de/i/<id>` als Textzeile im Brief | erledigt. **Abweichung:** der Plan sah vor, Brief-Einbettung und `copyWithQr` unangetastet zu lassen; beide wurden geändert, weil die Kürzung vom 01.08. die QR-Bilder von das Briefende unter das jeweilige Code-Feld verschoben hat |
| 5 | QR-Schritt im Rundgang, Versionszeile, Gesamt-Gegenprobe | erledigt am 01.08.2026 |

**Abweichungen in Etappe 5 gegenüber dem ursprünglichen Plan:** Die Versionszeile
steht auf **v5 · August 2026**; die geplante v2.8 wäre ein Rückschritt gewesen, weil
die App zwischenzeitlich auf v4 stand. Die geplante Gegenprobe „ein Brief für
Lapidus, Hinweis statt QR" ist nicht mehr möglich — seit 3b haben alle 44
OP-Methoden ein Ziel. An ihre Stelle tritt die Lisfranc/TMT-Arthrose als Diagnose
ohne Ziel; geprüft wurden Chevron (zwei Codes, Begleiter, Varianten) und
Lisfranc/TMT (deaktivierter Hinweis plus Konservativ-Code).



Stand 01.08.2026, erzeugt aus `data/opmethoden.json` gegen `infomaterial.json`
der Patienten-App.

**Achtung bei der Neuerzeugung:** Der Stand vom 31.07.2026 war fehlerhaft, weil
er gegen `PATIENT_DIAGNOSE_MAP` statt gegen den tatsächlichen Seitenbestand
geprüft hat. `hallux_valgus` stand dort als „ohne Krankheitsbild-Seite", obwohl
die Seite existierte — es fehlte nur die Zuordnung. Maßgeblich ist immer, ob der
Schlüssel in `INFOMATERIAL` vorkommt, nicht ob er in der Map steht.

## OP-Methoden

**Alle 44 OP-Methoden haben ein Ziel.** Hier ist nichts offen.

## Diagnosen ohne Krankheitsbild-Seite

| Diagnose (Kennung) | Bezeichnung | Anmerkung |
|---|---|---|
| `lisfranc_arthrose` | Lisfranc-Arthrose | **offen** — in der Patienten-App gibt es dazu nur die OP-Technik „TMT-Arthrodese" und `tmt1_instabilitaet_kb` (Instabilität des ersten Strahls, nicht Arthrose). Eine Krankheitsbild-Seite muss angelegt werden; die Texte kommen laut CLAUDE.md des Fuss-Track-Repos von außen. |
| `diffuse_beschwerden` | Diffuse Beschwerden | Sammelposten, bewusst ohne Ziel |

**Offen: 1 von 16 Diagnosen** (`diffuse_beschwerden` nicht mitgezählt).

## Erledigt am 01.08.2026

- `hallux_valgus` → `hallux_valgus`: Zuordnung ergänzt, Seite existierte bereits.
- `hallux_rigidus` → `hallux_rigidus`: zeigte zuvor auf `hallux_limitus_kb`, also
  auf die Frühform statt auf das eigene Krankheitsbild.
- `hallux_limitus` als eigene Diagnose angelegt, zeigt auf `hallux_limitus_kb`.
- `youngswick` als OP-Methode angelegt, zeigt auf die vorhandene Technikseite.
  Abrechnungssteuerung auf Anweisung wertgleich von `chevron` uebernommen.
- `mittelfuss_arthrose` in `lisfranc_arthrose` umbenannt, Label „Mittelfußarthrose"
  → „Lisfranc-Arthrose". Reine Umbenennung: `diagnoseText`, Befunde, OP-Methode
  und Bildbefund waren bereits durchgehend auf die Tarsometatarsalgelenke bezogen.

## Konservative Pfade — zurueckgestellt

Fuer die zehn NONOP-Themen gibt es noch keinen Fokus-Einstieg. Der Parameter
`?kb=` ist laut Quelltext eine *Vorauswahl auf der Landing-Page* und fuehrt in
die volle App — das widerspricht der Fokus-Ansicht. Konservativ-QR bleibt
deshalb offen, bis die Patienten-App einen eigenen Einstieg dafuer hat.

## Grobe Zuordnungen

Mehrere Werkzeug-Methoden zeigen bewusst auf dasselbe Patiententhema:

| Werkzeug-Methode | zeigt auf |
|---|---|
| `amic` | `knorpel_osg` |
| `bandplastik_autolog` | `lat_stabil` |
| `brostrom_gould` | `brostrom` |
| `brostrom_int_brace` | `brostrom` |
| `chevron` | `chevron_akin` |
| `coalition_exzision` | `coalitio_cn` |
| `gastroc_pmgr` | `gastroc` |
| `gastroc_strayer` | `gastroc` |
| `haglund_mini` | `calcaneoplastie` |
| `mdo_mini` | `dmmo` |
| `oats` | `knorpel_osg` |
| `peroneal_naht` | `peroneal_riss` |
| `peroneal_rek` | `peroneal_riss` |
| `supramal_ot` | `smot_valgus` |
