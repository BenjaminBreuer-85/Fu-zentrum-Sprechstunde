# Datenlandkarte Fuss-Track Clinic (Stand der Dateien vom 13.09.2026)

Bestandsaufnahme auf Wunsch des Autors („nichts annehmen"). Jede Zahl stammt aus den am 13.09.2026 gestagten Dateien (Repo `Fu-zentrum-Sprechstunde`, letzter Commit 63c16e8; Patienten-Repo `Fuss-Track`, letzter Commit 06cdcfd). Was nicht gelesen wurde, steht nicht hier. Prüfskript und Rohausgaben liegen in der Cowork-Sitzung.

## 1. Die App und ihre Werkzeuge (`app.html`, 770 KB)

Der Daten-Loader lädt zehn Gruppen: `katalog2026, erloes2026, diagnosen, opmethoden, opsteuerung, endo, preise, optexte, aufklaerung, referenz` (Zeile 176). `kurzlinks.json` und `zuordnung/implantat_zuordnung.json` liegen im Repo, `kurzlinks.json` wird von `404.html` für die Kurzadresse `fuss-track.de/i/<id>` gelesen, nicht von der App.

Hauptmenü, acht Kacheln plus Link zur Patienten-App: Sprechstundenbrief, OP-Bericht Generator, OPS-Code Zuordnung, OP-Manuale, Klassifikationen, Implantatpreise, Röntgen und Messmethoden, Aufklärungstexte.

**Sprechstundenbrief.** Fachrichtung Fuß/Sprunggelenk oder Endoprothetik (Endo seit Commit 63c16e8 gesperrt, „in Arbeit"). Im Fußpfad zwei Sonderflüsse über der Diagnoseliste: „Metallentfernung" (setzt Diagnose „Störendes Implantat") und „Verlaufskontrolle" (`kontrolleMode`, Datenblock `KONTROLLE_V2` in `diagnosen.json`: sechs Anlässe wundkontrolle, fadenzug, verlauf, roentgen, abschluss, ausserplanmaessig; acht Anweisungsgruppen belastung, ruhigstellung, thrombose, sicherung, abweichung, verordnung, wiedervorstellung, au; Zeitpunkt aus OP-Datum). Die Verlaufskontrolle ist damit vorhanden und deckt die Sprechstunde nach der OP ab; eine tägliche stationäre Dokumentation gibt es nicht. Word-Export vorhanden: `Sprechstundenbrief.doc` mit eingebetteten QR-Bildern (Zeile 2895 ff.).

**OP-Bericht Generator.** Sektionen fuss, endo (gesperrt), uc (Unfallchirurgie, 21 Eingriffe aus `UC_EINGRIFFE`), ws (Wirbelsäule, seit 28.08.2026 stillgelegt). Fuß-Erlösmemo mit 31 Zweigen, davon drei seit c378f42 aus `OP_STEUERUNG` (Metallentfernung, Achillessehne, diabetischer Fuß), 28 weiter im Code (`abgleich-zweige-opsteuerung-2026-09-09.md`). Word-Export vorhanden: `OP-Bericht_<Seite>_<Geschlecht>.docx` (Zeilen 5747, 5758) und `UC_OP_Bericht.docx` (Zeile 6807).

**Implantatpreise.** Excel-Import und -Export über `lib/xlsx-style.min.js` (Zeilen 7975, 8068, 8481, 9560); Preise liegen ausschließlich im Supabase-Konto des Nutzers.

## 2. Datendateien im Bucket `toolbox-data` (Repo: `data/` ist gitignored)

| Datei | Blöcke (Anzahl) | Bemerkung |
|---|---|---|
| `diagnosen.json` 58 KB | `DIAG` 18 Diagnosen in 7 Gruppen (Vorfuß, Mittelfuß, Rückfuß und Fußform, Sprunggelenk, Sehnen und Faszien, Diabetischer Fuß/Infekt, Unspezifisch); `COALITIO_BEFUNDE` 3; `KONSERV` 11; `RISIKEN` 8; `RISIKEN_ENDO` 3; `KONTROLLE_TEXT`/`KONTROLLE_LABEL` 3 (alt, laut Auftrag Kontrolle v2 nach Abnahme zu entfernen); `KONTROLLE_V2`; `DIAG_GRUPPEN` 7 | `opText` bei sechs Diagnosen |
| `opmethoden.json` 41 KB | `OPS` 58 Eingriffe (Felder k, b, r, t); `OPS_LABELS` 140 Kodes; `AUFKLAERUNG_MAP` 6; `PATIENT_EINGRIFF_MAP` 52; `KB_THEMA` 47; `PATIENT_VARIANTEN` 35; `PATIENT_EINGRIFF_KB_MAP` 3; `PATIENT_DIAGNOSE_MAP` 14 | Brücke zur Patienten-App |
| `opsteuerung.json` 60 KB | `OP_STEUERUNG` 59 (58 OPS plus `metallentfernung`; Felder hdrg, drg, empf, impl, hebel, hebelName, hdrgTrigger, kontext, modifikatoren, hinweise, ausschluss, aufwertung, opsCodes, ambStatus); `UGVD_ABSCHLAG` 23; `ME_REGIONEN` 5; `HDRG_REGELN` (I20O_N, I20M); `HDRG_RAHMEN` 5 | alte Blöcke ausschluss/aufwertung/kontext noch in 8 Einträgen |
| `optexte.json` 143 KB | `T` 109 Bausteine; `UC_EINGRIFFE` 21; `UC_TEXT_MAP` 21; `WS_EINGRIFFE` 2; `WS_WIRBEL` 8; `WS_SEGMENTE` 8 | 26 T-Schlüssel werden nur dynamisch angesprochen (UC, ME, Endo), keiner fehlt |
| `katalog2026.json` 446 KB | `_HD` 3.821 Kodes (Bitmaske AOP/Hybrid/Kontext); `_KX` 9 Ausnahmen; `_KATALOG_META` | Quelle Master-Excel; am 09.09. per Patch geändert, Excel nachzuziehen |
| `erloes2026.json` 16 KB | `_DRG` 29; `_HDRG` 7 (I20O, I20N, I20M, I13N, I21M, I29M, I31N); `GVD` 34; `_KURZ` 10; `_ERLOES_META` | Quelle `Erloesdaten_2026_MASTER.xlsx` (liegt in `data/`, gitignored) |
| `aufklaerung.json` 23 KB | `AUFKLAERUNG_RISIKEN`: allgemein 26, elektiv 85, gruppen 18, eingriffe 42, labels 42, alternativen 8 | Eingriffsliste eigenständig, nicht an `OPS` gekoppelt |
| `referenz.json` 93 KB | `KLASSIFIKATIONEN` 47; `ROENTGEN` 9 Aufnahmen; `MESSMETHODEN` 26; `MANUALE` 4 Kategorien mit 18 Einträgen | |
| `endo.json` 22 KB | 14 Blöcke (ENDO_DRG 14, Konstellationen 7, Implantatlisten) | Endo gesperrt, Daten vorhanden |
| `preise.json` 1 KB | `EINZELPREISE` leer (bewusst); UC-Implantattypen 4 | |

Im Repo, nicht im Bucket: `kurzlinks.json` (58 Ziele, IDs unveränderlich), `zuordnung/implantat_zuordnung.json` (KATALOG 42 Implantattypen, EINGRIFFE 42 Materialsätze, MAPPING_OPS 30), `diagnose-diabetischer-fuss.json` und `opmethoden-diabetischer-fuss.json` (Quelldateien des DF-Auftrags, Inhalte sind in `diagnosen.json` bzw. `opmethoden.json` übernommen: `diabetischer_fuss`, `df_debridement`, `df_amputation` vorhanden).

Patienten-App (`Fuss-Track`): `phasen.json` mit `BEGLEITER` 48 Eingriffen (je label, kurzlabel, merkmale, praeop, varianten, platzhalter, aufenthalt_default), `infomaterial.json`, `bausteine.json`, `nonop.json`, `katalog.json` (Beschwerde-Wegweiser), `aufklaerung.json`.

## 3. Querprüfungen (Skript in der Sitzung, Ergebnis vom 13.09.)

Stimmig: alle `DIAG.opMethoden` haben einen `OPS`-Eintrag; alle 58 `OPS` haben einen `OP_STEUERUNG`-Eintrag; alle `{IMPL:…}`-Platzhalter in `optexte.T` haben einen Eintrag im Implantatkatalog; alle DRGs der Steuerung haben Erlösdaten; alle Ziele von `PATIENT_DIAGNOSE_MAP` existieren als Kurzlink; alle `MAPPING_OPS`-Schlüssel sind gültige `OPS`.

Befunde, nach Gewicht:

**B1, dringend, Vertraulichkeit.** `_testdaten_temp.json` liegt im Repo-Root und ist committet (Commit 1c83162 „xx"), nicht gitignored. Inhalt: Block `preise` mit 40 Implantatpreisen je Katalogschlüssel und Block `erwartet` mit 43 Werten. Das Repo ist der Quellordner von GitHub Pages, also öffentlich erreichbar. Wenn die Beträge echte Einkaufspreise sind, verstößt das gegen die Regel „Preise nie ins Repo". Die Datei wird von keinem Code referenziert. Nötig: Datei aus dem Repo entfernen und aus der Git-Historie tilgen (die Code-Sitzung kennt das Vorgehen; ein einfaches Löschen lässt die Historie öffentlich). Entscheidung und Ausführung beim Autor, ich fasse Git nicht an.

**B2, Aufklärungstexte hinken der Chip-Struktur hinterher.** `aufklaerung.json` führt 42 Eingriffe. Drei davon gibt es in `OPS` nicht mehr: `calcaneus_ot`, `coalition_exzision`, `supramal_ot` (im Auftrag Chips-Struktur ersetzt). 19 `OPS`-Eingriffe haben keinen Eintrag in der Aufklärung, darunter die neuen `coalition_cn`, `coalition_tc`, `supramal_valgus`, `supramal_varus`, `arthrodese_tmt1`, `arthrodese_tmt13`, außerdem `as_debridement`, `as_tendoskopie`, `chevron` (nur `chevron_akin`), `df_amputation`, `df_debridement`, `exostose`, `fdl_transfer`, `hohlfuss_dwyer`, `hohlfuss_lambrinudi`, `kleinzehen_weichteil`, `os_tib_ext`, `weil`, `youngswick`. Das Aufklärungswerkzeug listet seine Eingriffe aus der eigenen Tabelle (Zeile 7793), zeigt also die drei alten Namen weiter an und die neuen nicht. Datenarbeit für mich, nach Freigabe: alte Einträge auf die neuen Schlüssel übertragen, fehlende ergänzen.

**B3, TMT-Varianten.** `PATIENT_VARIANTEN.tmt` in der Clinic kennt `einfach` und `komplex`; der Begleiter `tmt` der Patienten-App kennt `einfach`, `komplex`, `hallux_einfach`, `hallux_komplex`. Nach der Aufteilung in `arthrodese_tmt1`, `arthrodese_tmt`, `arthrodese_tmt13` müssten die TMT-I-Varianten (`hallux_*`) aus der Clinic erreichbar sein; heute zeigen alle drei Chips auf `tmt` ohne Variantenunterschied. Entscheidung des Autors, welche Variante welcher Chip auslöst.

**B4, Kurzlinks fehlen für neue Ziele.** `PATIENT_EINGRIFF_MAP` zeigt auf `coalitio_tc`, `smot_varus`, `achilles_insuffizienz_kb`; für diese drei gibt es keinen Eintrag in `kurzlinks.json` (58 IDs). Die App baut die Adresse direkt aus dem Schlüssel, der Brief funktioniert; nur die Kurzadresse `fuss-track.de/i/<id>` fehlt. Ergänzen, nie ändern (Regel in der Datei).

**B5, Ziel ohne Begleiter.** `PATIENT_EINGRIFF_MAP.cotton` zeigt auf `cotton`. In `infomaterial.json` existiert dazu der Artikel „Cotton-Osteotomie" (Kategorie OP-Technik, vier Slides), in `phasen.json` gibt es keinen Begleiter `cotton`. Der Link aus dem Brief führt also zur Aufklärung, aber nicht zu einem Nachbehandlungsbegleiter; der Patient nach Cotton-Osteotomie bekommt keine tagesgenaue Begleitung. Entscheidung: Begleiter anlegen oder bewusst so lassen.

**B6, acht Begleiter ohne Weg aus der Clinic.** In der Patienten-App existieren Begleiter, die kein Clinic-Chip erreicht: `tarsaltunnel`, `schede`, `moberg`, `mica`, `teilprothese_talus`, `calc_medial_sehne`, `calc_verlaengerung_sehne`, `kidner`. Entweder gewollt (Inhalt für Patienten anderer Behandler) oder es fehlen Chips.

**B7, veraltete Schlüssel.** `DIAG.knick_senk.opText` enthält noch `coalition_exzision`; der Chip existiert nicht mehr, der Eintrag ist wirkungslos. `OP_STEUERUNG.fhl_transfer.ausschluss.ziel` nennt 5-854.29 als Kontextprozedur; der Kode steht in keiner Hybrid-Tabelle und nicht im Katalog, der Satz stammt aus der Zeit vor den Hybrid-Regeln (die alten Blöcke sollen ohnehin fallen).

**B8, Steuerungskodes ohne Katalogzeile.** 5-781.1t, 5-781.ar, 5-784.0n, 5-854.29, 5-896.2g kommen in `OP_STEUERUNG` vor, stehen aber nicht in `katalog2026.json`. Das ist erwartbar, wenn ein Kode weder AOP noch Hybrid noch Kontext ist; die OPS-Code-Suche zeigt sie dann als „nicht gelistet". Nur zur Kenntnis.

**B9, Word-Export an drei Stellen.** Die Entscheidung „Word-Knopf entfernen" bezog sich auf den Sprechstundenbrief; im OP-Bericht (Fuß und UC) gibt es dieselbe Funktion. Vor dem Auftrag Teil A klären, ob alle drei entfallen. Die Excel-Bibliothek bleibt für die Implantatpreise nötig.

## 4. Folgen für die laufenden Aufträge

- `auftrag-verbesserungen-2026-09.md`, Paket 2: Die Aussage zur Verlaufskontrolle ist belegt (Sonderfluss im Sprechstundenbrief, `KONTROLLE_V2`); Visite bleibt das stationäre Gegenstück. Die Belegungsgründe werden dort geführt, die Verlaufskontrolle bleibt unverändert.
- `auftrag-briefpruefung.md`, Teil A: Umfang des Word-Exports klären (B9).
- Neue Datenarbeit vor Paket 3: Aufklärung nachziehen (B2), TMT-Varianten (B3), Kurzlinks (B4), `cotton` (B5), veraltete Schlüssel (B7).
- Selbsttest-Seite (Paket 1, E1): die Prüfungen aus Abschnitt 3 sind die Vorlage; sie haben heute B2 bis B8 gefunden.
