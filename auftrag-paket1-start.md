# Startnotiz Schritt 5: Paket 1 aus `auftrag-verbesserungen-2026-09.md` (A6, B4, E1) plus C4

Stand 15.09.2026, Cowork-Sitzung, Freigabe des Autors („dann Schritt 5"). Ausgangsstand: `app.html` Commit e823db3 (771.166 Byte), Daten im Bucket-Stand nach 3a/3b/3c/3k/3l/3m. Der Auftrag vom 13.09. gilt unverändert; diese Notiz ordnet ihn in die heutige Reihenfolge ein und ergänzt, was sich seither geändert hat.

## Reihenfolge

Der Auftrag sah Paket 1 „nach dem 28-Zweige-Auftrag" vor. Entscheidung des Autors 15.09.2026: Paket 1 kommt vor Schritt 6 (28 Zweige). Teil A der Briefprüfung (Word-Knopf) ist erledigt (b384ece). Vier Teilcommits in dieser Folge, je Commit eine Vollzugsmeldung: (1) C4, (2) A6, (3) B4, (4) E1. Kein Push zwischen den Commits nötig; die Gegenprobe der Cowork-Sitzung läuft je Commit auf dem Prüfstand.

## C4, neu in Paket 1: leere Sektion „Umstellungsosteotomien" im OP-Bericht

Befund (Prüfstand-Bericht 13.09., C4): `app.html` Z. 6111–6114 zeigt `<OBSec title="Umstellungsosteotomien" …>` mit leerer `row`; die Chips sind seit dem Chips-Struktur-Auftrag in `rfOp` (Kommentar Z. 5672 „umOp entfernt (supramal jetzt in rfOp)"). Auf dem Prüfstand erscheint die Sektion als „Umstellungsosteotomien 0 Chips". Änderung: die Sektion samt leerer `row` entfernen; `umOp`/`setUmOp` (Z. 4502), `hasUM` (Z. 4572, 4627, 5209, 5730) und `sec.um`/`togSec("um")` dürfen mit weg, wenn sie danach keinen Leser mehr haben, sonst bleiben sie stehen. Kein Verhalten ändert sich: `umOp` ist immer leer.

## A6 und B4

Wie im Auftrag. Fundstellen am heutigen Stand: Hilfe-Abschnitt „Hilfe & Rundgänge" in den Einstellungen ab Z. 9408; Rundgang-Texte ab Z. 9023 (Kachel-Tour) und die Werkzeug-Rundgänge im selben Block; OP-Anleitungen `tool === "manuale"` ab Z. 9706 (Inhalte aus `manuale/`, `BASE_URL` Z. 7246), Klassifikationen ab Z. 9722. Für B4 gilt: Abschnittsnamen nur aus vorhandenen Überschriften der geöffneten Ansicht; kein neuer Datenblock.

## E1, Selbsttest: Präzisierungen nach dem Lauf der Cowork-Sitzung (15.09.2026)

Die Cowork-Sitzung hat die neun Prüfungen gegen den heutigen Stand laufen lassen (`querpruefung_e1.py`, Prüfstand `clinic_3o`). Der Selbsttest der App muss dieselben Treffer liefern; das ist die Abnahme.

Präzisierungen zur Definition:

(4) `optexte.T`-Schlüssel ohne Verweis: Der Code liest `T` auch dynamisch (`T[UC_TEXT_MAP[ucOp]]` Z. 5315; `"me_zusatz_"+Kode` Z. 5664 und 6605). Der Selbsttest zählt einen Schlüssel als referenziert, wenn er wörtlich als `T.<key>`/`T["<key>"]` vorkommt, als Wert in `UC_TEXT_MAP` steht oder mit `me_zusatz_` beginnt. Übrig bleiben heute acht Schlüssel, deren Text die festen Zweige nicht benutzen (die Zweige tragen den Text hart im Code): `arthrodese_osg`, `as_naht`, `ask_nano`, `fasziotomie_offen`, `gastroc_pmgr`, `gastroc_strayer`, `me_stell`, `tep_infinity_flatcut`. Das ist ein echter Befund für Schritt 6b, kein Fehler des Selbsttests.

(6) Nur `PATIENT_EINGRIFF_MAP` und `PATIENT_DIAGNOSE_MAP` werden gegen `kurzlinks.json` (`ZIELE`, Regel `kurzlinkId()` Z. 1905: Unterstrich zu Bindestrich, Suffix `-kb` entfällt) geprüft. `PATIENT_EINGRIFF_KB_MAP` enthält `kbinfo`-Artikel, keine Kurzlink-Ziele; sie werden nicht geprüft (die Artikel liegen in `infomaterial.json` der Patienten-App, für die Clinic ohne Netzzugriff nicht erreichbar).

(7) Katalogzeile fehlt: gilt als Hinweis, nicht als Fehler (Kodes ohne AOP-, Hybrid- oder Kontext-Flag stehen nicht im Katalog, Datenlandkarte B8). Flag-Widerspruch (Kontextkode ohne Flag 4) ist ein Fehler.

Erwartete Treffer am Stand 15.09.2026 (Bucket = Prüfstand):

1. `DIAG.opMethoden` ohne `OPS`: 0.
2. `OPS` ohne `OP_STEUERUNG`: 0.
3. `opText`-Schlüssel ohne `OPS`: 0.
4. `optexte.T` ohne Verweis: 8 (Liste oben); Verweise ohne Text: 0.
5. `{IMPL:…}` ohne Zuordnung: 0.
6. Patienten-Ziele ohne Kurzlink: 0.
7. Steuerungskodes ohne Katalogzeile (Hinweis): 10 — 5-781.1t (os_tib_ext.hebel), 5-781.ar (peroneal_lux.hebel), 5-784.0n (arthrodese_osg.hebel), 5-808.a4 (arthrodese_tmt1.opsCodes), 5-808.a5 (arthrodese_tmt.opsCodes), 5-808.a6 (arthrodese_tmt13.opsCodes), 5-819.4 (HDRG_REGELN.I20O_N.kontext), 5-854.29 (haglund_as_split.hebel), 5-859.0 (gastroc_pmgr/gastroc_strayer.opsCodes), 5-896.2g (df_debridement.hebel). Kontextkode ohne Flag 4: 0.
8. `_KX` ohne Katalogzeile: 0.
9. Hinweise mit Doppelpunkt-Ende oder `undefined`: 0.
10. Ladezeit und Größe je Datei: nur Anzeige.

Weicht der Selbsttest davon ab, ist entweder der Selbsttest oder das Skript falsch; die Cowork-Sitzung klärt das anhand der Trefferliste in der Vollzugsmeldung.

Hinweis zur Datenquelle: Der Auftrag verlangt „die aktuell im Bucket liegenden Dateien". Auf `localhost` liest die App `./data/` (Z. 183 und 193); der Selbsttest soll denselben Ladeweg nehmen wie die App, dann prüft der Prüfstand die lokalen Dateien und die Live-App den Bucket.

## Abnahme (Cowork-Prüfstand, je Commit)

Referenz `baseline_*_3n.json` (Stand 6537db9; e823db3 unterscheidet sich nur in der Lapidus-Zeile). Sprechstundenbrief 81, OP-Bericht 68, Kombinationen 6 Fälle: zeichengleich bis auf (C4) den Wegfall der Sektion „Umstellungsosteotomien" im OP-Bericht. A6: beide Sätze sichtbar, Rundgang läuft. B4: 393 px und 1280 px, alle Anleitungen und Klassifikationen, keine Überlappung, keine Marke ohne Ziel. E1: Ausgabe gleich der Liste oben, kopierbar. Keine Konsolenfehler. Abnahme des Autors: Sprungmarken in zwei Anleitungen am Handy; Selbsttest einmal live aufrufen (`app.html?selbsttest=1`).
