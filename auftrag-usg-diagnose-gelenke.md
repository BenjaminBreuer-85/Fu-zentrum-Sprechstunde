# Auftrag: Diagnosetext „Arthrose des unteren Sprunggelenkes" je nach gewählter Arthrodese

Stand: 07.09.2026. Quelle: Rückmeldung des Autors mit Screenshot aus dem Sprechstundenbrief (Triple-Arthrodese gewählt, Diagnosezeile zeigt trotzdem „Arthrose des unteren Sprunggelenkes (Subtalargelenk) links").

## Problem

Die Diagnose `usg_arthrose` hat in `data/diagnosen.json` einen festen Brieftext „Arthrose des unteren Sprunggelenkes (Subtalargelenk)". Das Subtalargelenk ist aber nur ein Teil des unteren Sprunggelenkes. Wird als operative Option die Double- oder Triple-Arthrodese gewählt, nennt die Diagnosezeile weiterhin nur das Subtalargelenk, obwohl Talonavikular- und gegebenenfalls Kalkaneokuboidgelenk mitbetroffen sind. Der Brief widerspricht sich dann selbst (Diagnose ein Gelenk, OP drei Gelenke).

## Gewünschtes Verhalten

Der Diagnosetext im Brief richtet sich nach der gewählten OP-Methode:

| gewählte OP (Schlüssel in `OPS`) | Diagnosetext im Brief |
|---|---|
| `subtalar_arthrodese` | Arthrose des unteren Sprunggelenkes (Subtalargelenk) |
| `double_arthrodese` | Arthrose des unteren Sprunggelenkes (Subtalar- und Talonavikulargelenk) |
| `triple_arthrodese` | Arthrose der Rückfußgelenke (Subtalar-, Talonavikular- und Kalkaneokuboidgelenk) |
| keine dieser drei (konservativ, Arthrorise, andere OP, keine OP gewählt) | Arthrose des unteren Sprunggelenkes |

Die Seitenangabe (links/rechts/beidseits) bleibt wie bisher angehängt.

## Nachtrag 07.09.2026: Datenseite ist erledigt

`data/diagnosen.json` enthält jetzt das Feld `opText` (Map OP-Schlüssel → Diagnosetext) bei sechs Diagnosen, nicht nur beim USG: `usg_arthrose` (Subtalar, TN, Double, Triple), `lisfranc_arthrose` (künftige Schlüssel `arthrodese_tmt1`, `arthrodese_tmt`, `arthrodese_tmt13` aus `auftrag-chips-struktur.md`), `haglund` (AS-Débridement → Tendinose Midportion, Tendoskopie → Peritendinitis, FHL-Transfer → chronische Insuffizienz), `metatarsalgie` (Kleinzehen-Chips → mit Kleinzehendeformitäten, Morton → Morton-Neuralgie), `peronealsehnen` (Naht/Rekonstruktion → Riss, Stabilisierung → Luxation), `knick_senk` (Coalitio-Chips → tarsale Koalition mit rigidem Pes planovalgus). Die `diagnoseText`-Standards wurden dort verallgemeinert, wo der alte Text einen Teilbefund festschrieb. Für `app.html` bleibt Punkt 2 und 3 unten; Punkt 1 ist umgesetzt.

## Umsetzung, Vorschlag

Datengetrieben, damit weitere Diagnosen später denselben Mechanismus nutzen können:

1. In `data/diagnosen.json` beim Eintrag `usg_arthrose` den festen Text auf „Arthrose des unteren Sprunggelenkes" kürzen und ein neues Feld ergänzen (Feldname nach eurer Konvention, hier als Vorschlag `opText`):

```json
"opText": {
  "subtalar_arthrodese": "Arthrose des unteren Sprunggelenkes (Subtalargelenk)",
  "double_arthrodese": "Arthrose des unteren Sprunggelenkes (Subtalar- und Talonavikulargelenk)",
  "triple_arthrodese": "Arthrose der Rückfußgelenke (Subtalar-, Talonavikular- und Kalkaneokuboidgelenk)"
}
```

2. In `app.html` an der Stelle, an der die Diagnosezeile des Sprechstundenbriefs zusammengesetzt wird: Wenn die Diagnose ein `opText`-Objekt hat und eine der darin genannten OP-Methoden gewählt ist, diesen Text verwenden, sonst den Standardtext. Sind mehrere passende OPs gewählt (sollte bei diesen drei nicht vorkommen), gilt die zuletzt gewählte oder die mit den meisten Gelenken, bitte deterministisch.

3. Gleiche Logik bitte auch im OP-Bericht-Generator prüfen, falls dort die Diagnose aus `diagnosen.json` in den Berichtskopf übernommen wird.

Falls ihr die Diagnoselogik lieber nicht anfasst: Alternative wäre die Aufteilung in drei eigenständige Diagnosen (Subtalararthrose, Subtalar- und TN-Arthrose, Rückfußarthrose der drei Gelenke). Das hält der Autor für die schlechtere Lösung, weil die Diagnose im Alltag vor der OP-Entscheidung angeklickt wird und der Umfang der Arthrodese erst danach feststeht.

## Bereits erledigt (Daten, keine Codeänderung nötig)

`data/opmethoden.json`, Eintrag `OPS.subtalar_arthrodese`: Toggle-Beschriftung `k` von „USG-Arthrodese" auf „Subtalar-Arthrodese" geändert; `b` und `t` nennen jetzt das Subtalargelenk statt pauschal das untere Sprunggelenk. Die Patienten-App nennt den Eingriff bereits „Subtalararthrodese" (`kurzlinks.json`, Eintrag `subtalar`), die Bezeichnungen sind damit auf beiden Seiten gleich. Bucket-Upload von `opmethoden.json` steht in DEPLOY.md.

## Gegenprobe nach Umsetzung

Sprechstundenbrief, Diagnose USG-Arthrose links, dann nacheinander Subtalar-, Double-, Triple-Arthrodese wählen und die Diagnosezeile in der Vorschau vergleichen; danach OP abwählen und prüfen, dass der Standardtext ohne Klammerzusatz erscheint. Zusätzlich: Diagnose USG-Arthrose ohne OP im konservativen Weg, Klammerzusatz darf nicht erscheinen.
