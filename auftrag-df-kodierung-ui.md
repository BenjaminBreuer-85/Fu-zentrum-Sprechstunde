# Auftrag: OP-Optionen sichtbarer machen (SB) + DF-Kodierung mit Stufenlogik und Amputations-Dropdown (OB)

Stand: 30.08.2026. Drei Teile; die DRG-Stufen in Teil B/C sind am 29./30.08. im Webgrouper (GetDRG, G-DRG 2026) einzeln verifiziert, alle €-Beträge mit LBFW 4.562 € gerechnet. Die dafür nötigen DRG-Zeilen (inkl. neuer Minimal-Zeilen F21E und F28C) liegen bereits in `data/erloes2026.json` — Beträge bitte zur Laufzeit aus dem Block ableiten, keine neuen Literale.

## A) Sprechstundenbrief: OP-Optionen nach Diagnosewahl hervorheben

Problem: Nach der Diagnosewahl erscheinen die Sektionen ①–⑤ dezent UNTERHALB der langen Diagnose-Gruppenliste — Nutzer merken nicht, dass unten etwas Neues wählbar ist. Umsetzung (Entscheidung des Autors, Punkte 1–3; Punkt 4 nur falls vom Autor zusätzlich freigegeben):

1. **Feedback am Ort der Aktion:** Sobald mindestens eine Diagnose gewählt ist, direkt unter dem Diagnose-Block eine kräftige Weiter-Schaltfläche in der Akzentfarbe der App rendern: „Weiter zu Anamnese und OP-Auswahl ▼". Antippen scrollt sanft zur Sektion ①.
2. **Einmaliges Auto-Scroll:** Beim Wechsel von null auf eine gewählte Diagnose einmalig sanft zur Sektion ① scrollen (danach nicht mehr, um Mehrfachwahl nicht zu stören).
3. **Sektionsköpfe aufwerten:** Die Titel ①–⑤ von der dezenten Textzeile zu deutlich sichtbaren Karten-Headern machen (Akzentfarbe/Hintergrund wie die aktive Diagnose-Gruppe, etwas größere Schrift, Aufklapp-Pfeil rechts wie im Listenmuster); Sektion ① nach Diagnosewahl standardmäßig aufgeklappt.
4. *(Option, nur nach Freigabe des Autors)* Nach der Wahl die übrigen Diagnose-Gruppen einklappen und die gewählte Diagnose als kompakte Zeile mit „ändern"-Link zusammenfassen — verkürzt den Scrollweg deutlich.

## B) OP-Bericht-Generator, Diabetischer Fuß: Kodier- und Abrechnungsbox statt „OPS noch nicht zugeordnet"

Die beiden Platzhalter-Kästen („OPS noch nicht zugeordnet — bitte manuell kodieren") beim Debridement- und beim Amputations-Chip werden durch eine dynamische Box ersetzt, die je Toggle-Stand drei Dinge zeigt: die **empfohlenen OPS-Kodes**, die **DRG der aktuellen Konstellation** (mit €-Betrag aus erloes2026) und den **Hinweis auf die nächste Stufe**. Hinweise zu bereits erreichten Stufen werden ausgeblendet.

### Debridement-Chip — Kodes je Toggle

| Toggle-Stand | empfohlene OPS | ergibt DRG |
|---|---|---|
| Basis (schichtübergreifendes Debridement) | 5-869.1 (Weichteildebridement, schichtenübergreifend) | F27C (4.845 €) |
| + Vancomycin lokal *als eingelegter Medikamententräger* | zusätzlich 5-896.2g (großfl. Debridement mit Einlegen eines Medikamententrägers, Fuß) | **F27B (8.102 €)** |
| + Teilamputation Knochen (ohne Träger) | zusätzlich 5-865.90 (innere Amputation Metatarsale/Phalangen, bis zwei Strahlen; >2 Strahlen 5-865.91, Fußwurzel 5-865.92) | F13C (7.568 €) |
| + Teilamputation UND Träger | beide Kodes | **F27B (8.102 €)** |
| + VAC-Auflage | zusätzlich 5-916.a1 (Vakuumtherapie tiefreichend, Extremitäten; oberflächlich 5-916.a0) — DRG-neutral, trotzdem kodieren | unverändert |
| Lavanox-Spülung / Drainage-Lasche | kein eigener OPS (in der Prozedur enthalten) | unverändert |
| Osteomyelitis-Toggle | ND-Empfehlung M86.-7 einblenden mit Zusatz: spezifisch kodieren — M86.47 (chronisch mit Fistel) zählt CCL 2, M86.97 (n.n.bez.) CCL 0 | — |

Stufen-Hinweise (nur anzeigen, was noch NICHT erreicht ist):

- Ohne Träger-Toggle: „Mit eingelegtem Medikamententräger (5-896.2g) steigt die Konstellation auf F27B (8.102 €). Voraussetzung: Der Träger wird tatsächlich eingelegt und ist im OP-Bericht beschrieben." *(ausblenden, sobald Vancomycin-Toggle aktiv)*
- Bei Teilamputation ohne Träger zusätzlich warnen: „Teilamputation ohne Medikamententräger fällt in die F13C (7.568 €) — mit Träger gilt die F27B (8.102 €)."
- Immer (letzte Stufe): „Mit äußerst schweren CC (PCCL 4) steigt die Konstellation weiter — mit Träger auf F27A (11.191 €), mit Amputationskode auf F13B (12.130 €). PCCL 4 verlangt spezifische Kodes (z. B. A41.5- statt A41.9, R57.2); rein klinische Schwere ohne Kodes zählt nicht."
- Das einfache großflächige Haut-/Unterhaut-Debridement (5-896.1g) NICHT als Empfehlung führen — es fiele in die F21E (4.161 €); der DF-Berichtstext ist ohnehin schichtübergreifend.

### C) Amputations-Chip: Dropdown Amputationshöhe

Der Chip „Amputation proximale Tibia" bekommt ein Dropdown **„Amputationshöhe"** (Pflichtwahl, Vorbelegung: Unterschenkel proximal). Je Auswahl passen sich empfohlener OPS-Kode und Abrechnungsinfo an:

| Höhe (Dropdown) | OPS | DRG ohne äußerst schwere CC | mit PCCL 4 |
|---|---|---|---|
| Zehenamputation | 5-865.7 | F27C (4.845 €) | — |
| Zehenstrahlresektion | 5-865.8 | F27C (4.845 €) | — |
| Innere Amputation (Strahl-Teilresektion) | 5-865.90/.91/.92 | F13C (7.568 €) | F13B (12.130 €) |
| Vorfuß, transmetatarsal | 5-865.6 | F28C (8.371 €) | F13B (12.130 €) |
| Mittelfuß, tarsometatarsal | 5-865.5 | **F27A (11.191 €)** | F13B (12.130 €) |
| Rückfuß, mediotarsal (Chopart) | 5-865.4 | **F27A (11.191 €)** | F13B (12.130 €) |
| Unterschenkel proximal (Burgess) | 5-864.9 | **F27A (11.191 €)** | **F13B (12.130 €)**; zweizeitig an verschiedenen Tagen + PCCL 4: **F13A (23.499 €)** |

Verhalten: Der vorhandene Burgess-Berichtstext (T.df_amputation_tibia) wird nur bei „Unterschenkel proximal" eingefügt; bei allen anderen Höhen zeigt die Box die Kodier-/DRG-Empfehlung, und statt des Berichtstexts erscheint der Hinweis „Für diese Amputationshöhe liegt noch kein Textbaustein vor — Bericht bitte frei formulieren." (Textbausteine je Höhe können später folgen.) Beim Unterschenkel zusätzlich der Mehrzeitigkeits-Hinweis: „Bei zweizeitigem Vorgehen die Eingriffe mit ihren tatsächlichen OPS-Daten kodieren — verschiedene Tage sind Voraussetzung der F13A."

Die bestehenden df_debridement-/df_amputation-Hinweise der Erlössimulation im Sprechstundenbrief (opsteuerung.json) bleiben unverändert — dieser Auftrag betrifft den OP-Bericht-Generator.

## Gegenprobe

A: Diagnose wählen → Weiter-Schaltfläche erscheint, Tipp scrollt zu ①; Sektionsköpfe deutlich sichtbar; ① offen. B: DF-Debridement anklicken → Box zeigt 5-869.1 + F27C samt Träger-Hinweis; Vancomycin-Toggle an → Kode 5-896.2g erscheint, DRG wechselt auf F27B, Träger-Hinweis verschwindet, PCCL-Hinweis bleibt; Teilamputation ohne Träger → F13C-Warnung. C: Dropdown durchschalten → OPS/DRG wechseln laut Tabelle; Burgess-Text nur bei Unterschenkel proximal; kein „OPS noch nicht zugeordnet" mehr im DF-Bereich. Alle €-Beträge müssen aus erloes2026.json stammen (Kontrolle: LBFW in META ändern → Beträge folgen).

## Deploy

`app.html` committen/pushen. `erloes2026.json` (F21E/F28C-Minimalzeilen) steht bereits als offener Upload in DEPLOY.md Abschnitt D.
