# Redaktionsplan — OP-Methoden ohne Patienten-Inhalt

Stand 31.07.2026. Erzeugt aus `data/opmethoden.json` gegen `infomaterial.json`
der Patienten-App. Diese Eingriffe erzeugen im Sprechstundenbrief **keinen**
QR-Code; der Generator weist ausdrücklich darauf hin.

| OP-Methode (Kennung) | Bezeichnung im Werkzeug |
|---|---|

**Offen: 0 von 43 OP-Methoden.**

## Grobe Zuordnungen (bewusst vergröbert)

Mehrere Werkzeug-Methoden zeigen auf dasselbe Patiententhema. Fachlich vertretbar,
aber beim Ausbau der Inhalte zuerst zu prüfen:

| Werkzeug-Methode | zeigt auf |
|---|---|
| `amic` | `knorpel_osg` |
| `bandplastik_autolog` | `lat_stabil` |
| `calcaneus_ot` | `calc_medial` |
| `coalition_exzision` | `coalitio_cn` |
| `mdo_mini` | `dmmo` |
| `mdo_offen` | `weil` |
| `oats` | `knorpel_osg` |
| `supramal_ot` | `smot_valgus` |
