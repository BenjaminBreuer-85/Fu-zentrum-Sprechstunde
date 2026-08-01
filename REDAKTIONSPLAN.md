# Redaktionsplan — offene Patienten-Inhalte

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
