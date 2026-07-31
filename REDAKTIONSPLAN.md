# Redaktionsplan — offene Patienten-Inhalte

Stand 31.07.2026, erzeugt aus `data/opmethoden.json` gegen `infomaterial.json`
der Patienten-App.

## OP-Methoden

**Alle 43 OP-Methoden haben ein Ziel.** Hier ist nichts offen.

## Diagnosen ohne Krankheitsbild-Seite

| Diagnose (Kennung) | Bezeichnung |
|---|---|
| `diffuse_beschwerden` | Diffuse Beschwerden |
| `hallux_valgus` | Hallux valgus |
| `mittelfuss_arthrose` | Mittelfußarthrose |

**Offen: 3 von 15 Diagnosen.**

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
