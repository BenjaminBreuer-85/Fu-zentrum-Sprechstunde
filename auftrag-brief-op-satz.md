# Auftrag Clinic (klein): Satz zur OP-Empfehlung im Sprechstundenbrief

Stand 01.10.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand dcc5c9f (803.466 B, md5 9d6d0def…; Zeilenangaben darauf). Wunsch des Autors: Statt „Operativ kann eine XY vorgenommen werden“ soll im Brief stehen „Operativ bieten wir das o. g. Verfahren an und erläutern dieses sowie die operativen Alternativen.“ Ein Commit, eine Vollzugsmeldung mit Zeilennummern.

## Befund

Der Satz entsteht in `buildBrief` Z. 3226: `"\n\nOperativ kann " + opBeschr.join(" sowie ") + " vorgenommen werden. Es bestehen bei operativem Vorgehen gewisse Risiken (unter anderem: " + allRisiken.join(", ") + ")."`. `opBeschr` (Z. 3219–3223) sind die Beschreibungen `OPS[m].b` aus `opmethoden.json` (AMIC mit zwei Sonderfällen); sie werden sonst nirgends im Brief verwendet. Das Verfahren selbst steht bereits weiter oben im Brief: „Elektive operative Option: <Eingriffe> <Seite>, befundbezogenes Vorgehen“ (Z. 3085). Der Schluss (Z. 3248–3256) lautet je nach Schalter „Nach gründlicher Abwägung bieten wir den oben genannten Eingriff an.“ (OP empfohlen) oder „… raten wir zu konservativer weiterer Therapie.“ (nicht empfohlen). Der Metallentfernungs-Brief hat einen eigenen Satz (Z. 2846, „Operativ kann die Metallentfernung … vorgenommen werden.“) und bleibt unverändert.

## Änderung (Z. 3226)

Der Teil „Operativ kann … vorgenommen werden.“ wird ersetzt; der Risikosatz bleibt wie er ist:

- ein Eingriff: „Operativ bieten wir das o. g. Verfahren an und erläutern dieses sowie die operativen Alternativen.“
- mehrere Eingriffe (`ops.length > 1`): „Operativ bieten wir die o. g. Verfahren an und erläutern diese sowie die operativen Alternativen.“

Schreibweise „o. g.“ mit Leerzeichen (Rechtschreibung, Kopie in Word/KIS). `opBeschr` und die AMIC-Sonderfälle entfallen damit im Brief; `OPS[m].b` in `opmethoden.json` bleibt stehen (Datenfeld, keine Änderung).

Entscheidung des Autors 01.10.2026: **B**. Die beiden Sätze oben gelten nur bei gesetztem Schalter „OP empfohlen“ (`opEmpfohlen`). Ist er aus (Schluss „raten wir zu konservativer weiterer Therapie“), stattdessen neutral: ein Eingriff „Operativ käme das o. g. Verfahren in Betracht; dieses sowie die operativen Alternativen wurden erläutert.“, mehrere Eingriffe „Operativ kämen die o. g. Verfahren in Betracht; diese sowie die operativen Alternativen wurden erläutert.“ Bei `nurDiagnostik` gilt derselbe neutrale Satz.

## Nichts anderes

Metallentfernungs-Brief, OP-Bericht, Risikosatz, Schluss unverändert.

## Abnahme

Cowork-Prüfstand: 89 Brief-Referenzfälle gegen dcc5c9f: Abweichung nur im Satz „Operativ …“ (ein Eingriff Singular, Kombinationen wie Chevron + PIP Plural), Risikosatz und Schluss zeichengleich; ein Fall mit „OP empfohlen“ aus → neutraler Satz (Singular und Plural); AMIC-Fall ohne Sonderbeschreibung; Metallentfernung unverändert; Selbsttest 0 Fehler.

Am Handy: Brief → Hallux valgus → Chevron: „Operativ bieten wir das o. g. Verfahren an und erläutern dieses sowie die operativen Alternativen. Es bestehen bei operativem Vorgehen gewisse Risiken …“.

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
