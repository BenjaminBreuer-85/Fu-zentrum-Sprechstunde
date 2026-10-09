# Auftrag Clinic (Einzeiler): Beschriftung der Fallsteuerung für die Zehenosteotomie

Stand 07.10.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand 02dd198 (808.040 B, md5 a59bd0e9…; Zeilenangaben darauf). Ein Commit, Vollzugsmeldung mit Commit-Hash und Zeilennummer.

## Befund

Seit dem Datenschritt vom 07.10.2026 steht in `opsteuerung.json` der Eintrag `kleinzehen_osteotomie` (I20O/I20F, implantatfrei). Die Fallsteuerung erscheint damit bei einer reinen Zehenosteotomie, ihr Titel wird aber aus `OPS[obKey].k` (Z. 5702, Daten `opmethoden.json`) oder `OB_LABEL[obKey]` (Z. 1791–1792) gebildet; für `kleinzehen_osteotomie` gibt es weder das eine noch das andere, darum zeigt die Box den Rohschlüssel „Fallsteuerung – kleinzehen_osteotomie“ (Prüfstand 05.10.2026, Fälle D2 nur Osteotomie und D2–D4 Osteotomie). Ein Eintrag in `opmethoden.json` kommt nicht in Frage, weil die Kleinzehen-Methode im Brief bewusst nur als `kleinzehen_pip` („Kleinzehen/PIP oder Osteotomie“) geführt wird.

## Änderung

Z. 1791–1792, `OB_LABEL` um einen Schlüssel ergänzen:

```
var OB_LABEL = { fraktur_fibula_einfach: "Weber B einfach", metallentfernung: "Metallentfernung",
                 fraktur_fibula_mehrfragment: "Weber B/C Mehrfragment",
                 kleinzehen_osteotomie: "Zehenosteotomie (Kleinzehen)" };
```

Sonst nichts: Kodes, Texte, `opsteuerung.json`, `opmethoden.json`, Brief unverändert.

## Abnahme

OP-Bericht → Vorfuß → D2 Zehenosteotomie: Titel „Fallsteuerung – Zehenosteotomie (Kleinzehen)“; D2 PIP-Arthrodese + D3 Zehenosteotomie: Titel weiterhin „Fallsteuerung – Kleinzehen/PIP oder Osteotomie (führend)“ (PIP führt). Selbsttest ohne neue Meldung, keine Konsolenfehler, JSX transpiliert.

Deploy: Push `app.html` (keine Daten, kein Bucket).
