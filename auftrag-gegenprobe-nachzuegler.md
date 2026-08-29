# Auftrag: Nachzügler aus der Audit-Gegenprobe (app.html + diagnosen.json)

Stand: 29.08.2026. Die Gegenprobe nach der Audit-Umsetzung hat 14 von 16 Prüfpunkten bestanden. Zwei Punkte aus den bestehenden Aufträgen sind noch offen — hier gesammelt mit frischer Repro, die Ursprungsaufträge (auftrag-audit-b.md B4, auftrag-df-teil3) gelten unverändert.

## 1. C2 ist ERSETZT — siehe auftrag-score-faos.md

Der Audit-Punkt C2 („Scores-Zeile nur bei Eingabe") aus auftrag-audit-c.md ist hinfällig: Der Sprechstundenbrief hat bewusst keine Score-Eingabefelder, die Zeile ist ein Ausfüll-Stub für iMED1. Neue Entscheidung des Autors in **auftrag-score-faos.md**: AOFAS wird durch FAOS ersetzt und die Scores-Zeile bekommt einen An/Aus-Schalter mit Standard AUS. Bitte NICHT die alte C2-Lösung bauen.

## 2. B4 · Cotton-Osteotomie bleibt stumm (auftrag-audit-b.md)

*Repro:* OB → M, L, ≥18 → Mittelfuß → Chip „Cotton-Osteotomie" anklicken. Es passiert sichtbar nichts — kein Hinweis, keine Unteroption (autolog/allogen), keine Export-Karte. Entscheidung des Autors: Cotton ist nur Zusatzeingriff; der Klick darf nicht stumm bleiben (Hinweis oder Zusatz-Verdrahtung mit T.cotton_ot_autolog/allogen, siehe auftrag-audit-b.md Punkt B4).

## 3. Osteomyelitis-Chip entfernen (Rest aus auftrag-df-teil3)

Der Chip „Osteomyelitis" steht weiterhin als eigene Diagnose in der SB-Gruppe „Diabetischer Fuß / Infekt", und sein Brief druckt den rohen Platzhalter „Osteomyelitis am §KNOCHEN§". Anweisung des Autors vom 26.08.: Chip entfernen (aus DIAG und DIAG_GRUPPEN in data/diagnosen.json); die automatische Zweitdiagnose Osteomyelitis im OP-Bericht-Generator bleibt davon unberührt. Mit der Entfernung erledigt sich auch der §KNOCHEN§-Fund.

**Achtung Bucket:** Punkt 3 ändert `data/diagnosen.json` → in DEPLOY.md Abschnitt D eintragen bzw. beim ohnehin offenen diagnosen-Upload mitnehmen.

## Zur Einordnung: bestanden sind

ME- und Kontroll-Brief mobil (inkl. „der Patient"-Fix), beide Wedge-Toggles in allen vier Kombinationen ohne Platzhalterreste, Amputation proximale Tibia im OB mit Burgess-Text und ohne Debridement-Toggles, Morton-EBM-Hinweis, WS-Knopf entfernt, Emojis aus SEKTION/VORBEREITUNG, Landingpage-Statusmeldungen, dazu der volle SB-Regressionslauf über alle 19 Diagnosen ohne neue Funde. Der Startbildschirm-Auftrag (Stauchung + neuer SB-Untertitel) ist separat und noch offen (gemessen: 893 px bei 852 px Fenster).
