# Auftrag: Diagnosenauswahl im Sprechstundenbrief neu ordnen

Betrifft nur die **Anzeige und Anordnung** der Auswahl im Block „DIAGNOSE(N) – MAX. 2" des Sprechstundenbriefs. Keine Änderung an Diagnose-Schlüsseln, Textbausteinen, Befundlogik oder Auswahlverhalten. Die Auswahl bleibt auf zwei Diagnosen begrenzt, alle 17 bleiben vorhanden.

## 1. Sonder-Flows nach oben abtrennen

„Metallentfernung (Sonder-Flow)" und „Verlaufskontrolle (Sonder-Flow)" stehen heute zwischen der Überschrift und dem Diagnosenraster und wirken dadurch wie zwei Diagnosen unter vielen. Sie gehören in einen eigenen, sichtbar abgesetzten Bereich **über** den Diagnosen, mit eigener Kopfzeile:

```
ANLASS OHNE NEUE DIAGNOSE
[Metallentfernung]  [Verlaufskontrolle]

DIAGNOSE(N) – MAX. 2
[Raster wie unten]
```

Die bestehende visuelle Kennzeichnung der beiden Chips (gestrichelter Rahmen, eigene Farbe) bleibt. Der Zusatz „(Sonder-Flow)" kann in den Beschriftungen entfallen, weil die Trennung jetzt aus der Position hervorgeht. Der Chip „Kontrolle" heißt künftig „Verlaufskontrolle", passend zum ausgebauten Flow.

## 2. Diagnosen anatomisch gruppieren

Die heutige Reihenfolge ist gewachsen und folgt keiner Systematik. Neue Reihenfolge mit Gruppenüberschriften, von proximal der Zehen bis unspezifisch:

**Vorfuß**
1. Hallux valgus
2. Hallux rigidus
3. Hallux limitus
4. Metatarsalgie

**Mittelfuß**
5. Lisfranc/TMT-Arthrose

**Rückfuß und Fußform**
6. Knick-Senk-Fuß
7. Juvenil PPV
8. Hohlfuß
9. USG-Arthrose

**Sprunggelenk**
10. OSG-Arthrose
11. OSG-Instabilität
12. OCL / Knorpelschaden

**Sehnen und Faszien**
13. Haglund / Achillodynie
14. Achillessehnenruptur
15. Läsion der Peronealsehnen
16. Plantarfasciitis

**Unspezifisch**
17. Diffuse Beschwerden

Die Gruppenüberschriften im selben Stil wie „DIAGNOSE(N) – MAX. 2", nur kleiner und zurückhaltender, damit die Chips die Hauptsache bleiben. Falls Überschriften die Chip-Optik zerreißen, genügt die reine Sortierung mit etwas mehr Abstand zwischen den Gruppen; dann bitte kurz Bescheid geben.

Die Reihenfolge gehört in die Daten, nicht in den Programmtext: entweder als Sortierschlüssel je Diagnose in `data/diagnosen.json` oder als eigene Reihenfolge-Liste dort. Wenn der OP-Bericht-Generator eine vergleichbare anatomische Gruppierung führt, bitte melden, dann ziehen wir beide auf dieselbe Quelle.

## Gegenprobe

Alle 17 Diagnosen vorhanden und auswählbar, keine Dublette, keine fehlt · Auswahl von zwei Diagnosen unverändert möglich · beide Sonder-Flows lösen weiterhin ihren Flow aus · ein Bestandsbrief mit denselben Eingaben bleibt zeichengleich · Screenshot der neuen Anordnung im Mobilformat, weil die Auswahl dort am häufigsten benutzt wird.
