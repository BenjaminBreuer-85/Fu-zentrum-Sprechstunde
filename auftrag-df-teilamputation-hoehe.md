# Auftrag: OP-Methoden-Karte im SB + Resektionshöhe bei der Teilamputation per Dropdown (SB + OB), Amputations-Chip ohne Dropdown

Stand: 30.08.2026. Entscheidungen des Autors, ergänzt den umgesetzten auftrag-df-kodierung-ui.md. Zwei Themen: die Optik der OP-Auswahl im Sprechstundenbrief (Teil 0) und die Höhen-Differenzierung der Teilamputation (Teile 1–3).

## 0. Sprechstundenbrief: hervorgehobene OP-Methoden-Karte statt Sprung-Leiste (Design-Entscheidung A)

Die aktuelle Lösung (große „Weiter zu Anamnese und OP-Auswahl"-Leiste, die beim Antippen nach unten springt) ersetzt der Autor durch eine **OP-Methoden-Karte direkt am Ort der Diagnosewahl**:

- Sobald eine Diagnose gewählt ist, erscheint **direkt unter den Diagnose-Chips innerhalb der geöffneten Gruppe** eine deutlich hervorgehobene Karte: Akzentfarbener Rahmen, helle Akzentfüllung (Optik wie die aktive Gruppen-Kopfzeile), Titel **„OP-Methoden für [Diagnosename] wählen"**, darin die OP-Methoden-Chips (Mehrfachauswahl wie bisher, inklusive der Zusatz-Toggles wie „+ Coalitio").
- **Es existiert immer nur EINE Karte.** Bei zwei gewählten Diagnosen (Maximum) rückt die Karte unter das Ende des Diagnose-Blocks und führt die OP-Methoden beider Diagnosen mit kleinen Zwischenüberschriften („Für Knick-Senk-Fuß", „Für Diabetisches Fußsyndrom"). Es öffnen sich also nie mehrere Fenster.
- Die bisherige OP-Methoden-Liste unterhalb („OP-METHODE(N) — MEHRFACHAUSWAHL MÖGLICH") entfällt zugunsten der Karte — keine Doppelung.
- Die große Weiter-Leiste entfällt bzw. schrumpft zu einer dezenten Zeile „Weiter zur Anamnese ▼" UNTER der Karte, die zur Sektion ① scrollt.

## 1. OP-Bericht-Generator: Höhen-Dropdown am Teilamputations-Toggle

Beim Toggle „+ Teilamputation Knochen" des Debridement-Chips ein Dropdown **„Resektions-/Amputationshöhe"** ergänzen (die vorhandene Höhenliste DF_AMP_HOEHEN kann als Grundlage dienen, ohne den Unterschenkel):

| Auswahl | OPS | DRG ohne Träger | DRG mit Träger (5-896.2g) |
|---|---|---|---|
| Teilresektion Knochen, bis zwei Strahlen (Vorbelegung) | 5-865.90 | F13C (7.568 €) | **F27B (8.102 €)** |
| Teilresektion Knochen, mehr als zwei Strahlen | 5-865.91 | F13C (7.568 €) | F27B (8.102 €) |
| Teilresektion Fußwurzel | 5-865.92 | F13C (7.568 €) | F27B (8.102 €) |
| Zehenamputation | 5-865.7 | F27C (4.845 €) | F27B (8.102 €) |
| Zehenstrahlresektion | 5-865.8 | F27C (4.845 €) | F27B (8.102 €) |
| Vorfuß, transmetatarsal | 5-865.6 | F28C (8.371 €) | F28C (8.371 €) |
| Mittelfuß, tarsometatarsal | 5-865.5 | **F27A (11.191 €)** | F27A (11.191 €) |
| Rückfuß, mediotarsal (Chopart) | 5-865.4 | **F27A (11.191 €)** | F27A (11.191 €) |

(Alle Kombinationen am 29./30.08. im Webgrouper einzeln verifiziert; €-Beträge zur Laufzeit aus erloes2026.json.) Die Kodierbox „KODIERUNG UND ABRECHNUNG" zieht OPS-Zeile und ERGIBT-DRG aus dieser Auswahl; die Stufen-Hinweise passen sich an — der Medikamententräger-Hinweis erscheint nur dort, wo der Träger die DRG tatsächlich hebt (Teilresektion, Zehe, Strahl), und entfällt bei Vorfuß/TMT/Chopart. Das Freitextfeld „Knochen" und der Osteomyelitis-Toggle bleiben bei den drei Teilresektions-Optionen; der bestehende Teilamputations-Textbaustein passt zu den Teilresektionen — für Zehe/Strahl/Vorfuß/TMT/Chopart im Rahmen des Debridements bitte den Hinweis „Für diese Höhe liegt noch kein Textbaustein vor — Passage bitte anpassen" zeigen, sofern kein passender Text existiert.

## 2. OP-Bericht-Generator: Amputations-Chip zurückbauen

Der Chip „Amputation proximale Tibia" verliert das Höhen-Dropdown wieder — er steht fest für 5-864.9 (Burgess, proximaler Unterschenkel) mit dem vorhandenen Textbaustein und den Hinweisen F27A (11.191 €) ohne äußerst schwere CC, F13B (12.130 €) mit PCCL 4, F13A (23.499 €) bei mehrzeitigen Eingriffen an verschiedenen Tagen.

## 3. Sprechstundenbrief: dieselbe Höhenwahl bei der Debridement-Empfehlung

Wählt man im SB beim Diabetischen Fußsyndrom die OP-Empfehlung Debridement und dort die Teilamputation, erscheint dasselbe Höhen-Dropdown. Folgen:

- Die **Erlössimulation** (Fallsteuerung df_debridement) zeigt die DRG der gewählten Konstellation gemäß Tabelle oben statt pauschal F27B — die vorhandenen Hinweise aus opsteuerung.json bleiben darunter bestehen.
- Der **Brief-Empfehlungstext** wird um die Höhe ergänzt, z. B. „…ein operatives Debridement bei diabetischem Fußsyndrom mit Ulzeration und Infekt, mit Teilresektion des betroffenen Knochens" bzw. „…mit Zehenamputation", „…mit transmetatarsaler Vorfußamputation", „…mit Amputation in tarsometatarsaler Höhe", „…mit mediotarsaler Amputation". Ohne Teilamputation bleibt der Text unverändert.

## Gegenprobe

Teil 0: Diagnose „Knick-Senk-Fuß" wählen → hervorgehobene OP-Karte erscheint direkt unter den Diagnose-Chips in der Gruppe, mit Titel und allen OP-Chips; zweite Diagnose aus anderer Gruppe dazu → weiterhin genau EINE Karte am Ende des Diagnose-Blocks mit beiden Abschnitten; die alte OP-Methoden-Liste weiter unten erscheint nicht mehr doppelt; die dezente „Weiter zur Anamnese"-Zeile scrollt zu ①. OB: Teilamputation wählen → Dropdown mit Vorbelegung „bis zwei Strahlen", Kodierbox zeigt 5-865.90 und F13C/F27B je nach Träger-Toggle; Höhe „Mittelfuß" → 5-865.5, F27A, Träger-Hinweis weg; Amputations-Chip ohne Dropdown, Burgess unverändert. SB: Debridement + Teilamputation + Höhe „Vorfuß" → Erlössimulation F28C (8.371 €), Brieftext mit Vorfuß-Zusatz; ohne Teilamputation alles wie bisher. Kein „AMPUTATIONSHÖHE"-Dropdown mehr am Amputations-Chip.

## Deploy

Nur `app.html` (ggf. plus abgestimmte Ergänzung in opsteuerung.json — dann DEPLOY.md Abschnitt D pflegen). Committen, pushen.
