# Auftrag Clinic (klein, zu Datenschritt 3ah): AOP-Flag neben Hybrid, Zusatzkodes im AOP-Satz

Stand 27.09.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand Commit 48f679b (801.593 Byte, md5 6af20c9d…; Zeilenangaben darauf). Daten: Datenschritt 3ah der Cowork-Sitzung (`data/katalog2026.json` neu aus der Master-Excel, `scripts/build_katalog2026.py` angepasst; liegt lokal auf dem Mac). Ein Commit, eine Vollzugsmeldung mit Zeilennummern.

## Befund

Frage des Autors 26.09.2026: „5-808.b0 ist nicht im AOP-Katalog?“ Der Kode steht im AOP-Katalog. Die App sagte „steht nicht im AOP-Katalog“, weil (1) die Master-Excel und das Build-Skript nach der Regel „Hybrid-Vorrang“ (02.07.2026) bei 258 Kodes, die in AOP und Hybrid stehen, das AOP-Bit gelöscht haben (`imAopKatalog()` Z. 1406 prüft Bit 1), und (2) die Implantat-Zusatzkodes 5-93b.0 / 5-93b.e in keinem Katalog stehen und trotzdem als „nicht im AOP-Katalog“ mitgezählt werden. Regel des Autors 27.09.2026: Kode im AOP-Katalog → ambulant nach EBM möglich; Kode im Hybrid-Katalog → Fall läuft in die Hybrid-DRG, Hybrid hat Vorrang; kommt eine Kontextprozedur dazu, fällt der Fall aus der Hybrid, kann aber weiterhin ambulant erbracht werden.

Datenschritt 3ah (Cowork): Die 258 Konflikt-Kodes tragen wieder Bit 1 (Bitmaske 3, bei 5-788.60 mit Kontext 7); `build_katalog2026.py` maskiert nicht mehr und prüft, dass jeder Kode des Blatts Konflikte AOP+Hybrid trägt. Am Fuß betroffen 83 Kodes, darunter 5-788.5c, 5-788.40, 5-788.56, 5-788.00, 5-788.52, 5-808.b0/b1/bd–bg, 5-859.1a, 5-854.0c. Ohne Codeänderung zeigt der Prüfstand mit 3ah bei Chevron Standard „Ambulant: 5-93b.0 steht nicht im AOP-Katalog; …“ und bei MTP-I unter 18 „5-93b.0, 5-93b.e …“, also nur noch die Zusatzkodes.

## 1. Zusatzkodes im AOP-Satz nicht mitzählen

`ambSatzBau` (Z. 1551–1562) und `alleImAop` (Z. 1549): Kodes, die mit `5-93` beginnen (Zusatzinformationen zu Osteosynthese und Implantat, in keinem Katalog geführt), werden vor der Prüfung ausgefiltert. Kein weiterer Kodebereich; Kodes wie 5-808.a4 oder 5-784.0u, die in keinem Katalog stehen, bleiben wie bisher „nicht im AOP-Katalog“.

## 2. Wortlaut, wenn alle Kodes im AOP-Katalog stehen und die Hybrid gesperrt ist

Heute „Ambulant EBM.“ (Z. 1553). Für `ohneHybrid === true` neu: „Ambulant: alle Kodes stehen im AOP-Katalog, Erbringung nach EBM möglich.“ Ohne den Parameter unverändert. Der Hinweis des Autors, dass die ambulante Erbringung nach EBM in der Regel weniger bringt als die Hybrid-DRG, wird nicht in den Satz aufgenommen (Sprachregel Abrechnung 14.09.2026, keine Erlösaussage im sichtbaren Text); die Hybrid-Beträge stehen ohnehin in der Fallsteuerung.

## 3. OPS-Zuordnung

Die Marken (Z. 7556–7563) zeigen bei Bitmaske 3 bereits „Hybrid-DRG“ vor „AOP-Katalog“; das ist der Hybrid-Vorrang als Anzeigeregel und bleibt so. Fußzeile Z. 7602: „Regel: Hybrid-Vorrang vor AOP“ → „Regel: Hybrid-Vorrang; Kodes in beiden Katalogen tragen beide Marken“. Die Zahl „AOP: … OPS“ steigt durch 3ah von 2.877 auf 3.135.

## Nichts anderes

`inPositivliste`, Selbsttest 7a/7b, Fallsteuerung außer Punkt 1 und 2, Brieftexte unverändert.

## Abnahme

Cowork-Prüfstand (Daten 3ah): (1) OP-Bericht → Chevron Standard (Kontext 5-854.2c): Satz endet mit „Ambulant: alle Kodes stehen im AOP-Katalog, Erbringung nach EBM möglich.“; MTP-I mit „<18 J.“ ebenso; Lapidus Standard weiter „Ambulant: 5-808.a4, 5-784.0u stehen nicht im AOP-Katalog; …“ (ohne 5-93b.0, 5-93b.e); Calcaneoplastie mit Bursektomie weiter „Ambulant: 5-782.at steht nicht im AOP-Katalog; …“. (2) Brief: 89 Referenzfälle, Briefe zeichengleich; Fallsteuerung nur in den Sperrsätzen anders. (3) OPS-Zuordnung: 5-808.b0 mit Marken „Hybrid-DRG“ und „AOP-Katalog“, Fußzeile mit 3.135 AOP-OPS und neuem Regeltext. (4) Selbsttest 0 Fehler, keine Konsolenfehler.

Deploy-Reihenfolge: erst `katalog2026.json` 3ah in den Bucket, dann Push (`app.html`, `scripts/build_katalog2026.py`). Die Master-Excel bleibt lokal in `data/`.

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
