# Abgleich der OP-Bericht-Zweige gegen OP_STEUERUNG und Regelsatz (Schritt 6a)

Erzeugt von `scripts/verify_zweige_6a.py` (Spalte C gerechnet mit jsc), app.html sha256 54073d203fc8…, 0 Zweige im Memo, 84 Zeilen. Nur Befund, keine Bewertung „richtig/falsch"; die Spalte Entscheidung ist leer und gehört dem Autor (A, B, C oder ein neuer Wert).

**Spalten.** A = was der Zweig heute anzeigt. B = der Eintrag in `opsteuerung.json`. C = was `hdrgAuswertung()` aus denselben Kodes macht (H-DRG / stationäre DRG / ambulanter Weg). betrifft = Ergänzungen a–f aus dem Umsetzungsplan.

| Nr | Zweig · Schalterstellung | Schlüssel | Kodes | A (hdrg/drg) | B (hdrg/drg) | C (hdrg/drg/ambulant) | Bewertung | betrifft | Anmerkung | Entscheidung |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Lapidus ohne Akin | lapidus | 5-808.a4 5-788.40 5-93b.0 5-93b.e 5-783.0v 5-784.0u 5-854.2c | — / I20D | I20M / I20D | — / I20D / nein | toggle (A entfaellt; C rechnet aus den Kodes) | f | Kodeliste enthaelt 5-854.2c immer; ohne Sehnentransfer gehoert er nicht in den Fall. | |
| 2 | Lapidus + Akin | lapidus | 5-808.a4 5-788.40 5-93b.0 5-93b.e 5-783.0v 5-784.0u 5-854.2c 5-788.56 | — / I20D | I20M / I20D | — / I20D / nein | toggle (A entfaellt; C rechnet aus den Kodes) | a, f | C1/C3: Zweig zeigt H-DRG '—', Daten und Auswertung I20M. | |
| 3 | Lapidus + Akin + 3× DMMO | lapidus | 5-808.a4 5-788.40 5-93b.0 5-93b.e 5-783.0v 5-784.0u 5-854.2c 5-788.56 5-788.54 5-86a.12 | — / I20D | I20M / I20D | — / I20D / nein | toggle (A entfaellt; C rechnet aus den Kodes) | a | C2: Zweigtitel bleibt 'Lapidus', die DMMO-Zahl aendert nichts. | |
| 4 | Lapidus + Spongiosa Metatarsale (Soll 5-784.0v) | lapidus | 5-808.a4 5-788.40 5-93b.0 5-93b.e 5-783.0v 5-784.0v 5-854.2c 5-788.56 | — / I20D | I20M / I20D | — / I20D / nein | toggle (A entfaellt; C rechnet aus den Kodes) | f | Kodeblock schiebt 5-784.0u (Tarsale); der Hebel in den Daten ist 5-784.0v (Metatarsale). | |
| 5 | MTP-I allein | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e | I20N / I20E | I20N / I20E | I20N / I20E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 6 | MTP-I + Akin | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e 5-788.56 | I20N / I20E | I20N / I20E | I20N / I20E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 7 | MTP-I nach Hoffmann/Tillmann (4× Arthroplastik) | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e 5-788.60 5-808.b2 | I20N / I20E | I20N / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | a | 5-788.60 steht in V70 minus V66: nichtKontext bei I20M, Kontext bei I20O/I20N. | |
| 8 | MTP-I + 1× DMMO | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e 5-788.52 5-86a.10 | I20N / I20E | I20N / I20E | I20N / I20E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 9 | MTP-I + 2× DMMO | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e 5-788.53 5-86a.11 | I20N / I20E | I20N / I20E | I20N / I20E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 10 | MTP-I + 3× DMMO | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e 5-788.54 5-86a.12 | — / I20D | I20N / I20E | — / I20D / nein | toggle (A entfaellt; C rechnet aus den Kodes) | — | Sechster Teil Punkt 2: C liefert I20D aus der Kontextregel, ohne festen Wert im Zweig. | |
| 11 | MTP-I + 4× DMMO | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e 5-788.55 5-86a.13 | — / I20D | I20N / I20E | — / I20C / nein | toggle (A entfaellt; C rechnet aus den Kodes) | — | C liefert I20C (Regel I20N → I20C), der Zweig zeigt I20D. | |
| 12 | MTP-I + PIP 3 Zehen | mtp1_arthrodese | 5-808.b0 5-93b.0 5-93b.e 5-808.bf 5-86a.12 | I20N / I20E | I20N / I20E | I20N / I20E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b | PIP wertet auf I20N auf; MTP-I steht schon bei I20N, kein I20M. | |
| 13 | Chevron ohne Zusatz | chevron | 5-788.5c 5-788.40 5-93b.0 5-854.2c | I20O / I20E | I20O / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | b | Kodeliste enthaelt 5-854.2c immer, obwohl der Zweigtext ihn als Entscheidung beschreibt. | |
| 14 | Chevron + Akin | chevron_akin | 5-788.5c 5-788.40 5-93b.0 5-854.2c 5-788.56 | I20O / I20E | I20O / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | b |  | |
| 15 | Chevron + 1× DMMO | chevron | 5-788.5c 5-788.40 5-93b.0 5-854.2c 5-788.52 5-86a.10 | I20O / I20E | I20O / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | b |  | |
| 16 | Chevron + 2× DMMO | chevron | 5-788.5c 5-788.40 5-93b.0 5-854.2c 5-788.53 5-86a.11 | I20O / I20E | I20O / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | b |  | |
| 17 | Chevron + 3× DMMO | chevron | 5-788.5c 5-788.40 5-93b.0 5-854.2c 5-788.54 5-86a.12 | I20O / I20E | I20O / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | a | C2: Zweig zeigt weiter I20O, Auswertung fuehrt nach I20E. | |
| 18 | Chevron + 4× DMMO | chevron | 5-788.5c 5-788.40 5-93b.0 5-854.2c 5-788.55 5-86a.13 | I20O / I20E | I20O / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | a |  | |
| 19 | Chevron + PIP 2 Zehen | chevron | 5-788.5c 5-788.40 5-93b.0 5-854.2c 5-808.be 5-86a.11 | I20O / I20E | I20O / I20E | — / I20E / nein | toggle (A entfaellt; C rechnet aus den Kodes) | b |  | |
| 20 | Scarf ohne Zusatz | scarf | 5-788.5e | I20O / I20E | I20O / I20E | I20O / I20E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 21 | Youngswick (Chip zeigt Scarf-Zweig) | youngswick | 5-788.5e | I20O / I20E | I20O / I20E | I20O / I20E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | — | Kein eigener Kodepfad: der Chip laeuft ueber gz='scarf'. | |
| 22 | Cheilektomie | cheilektomie | 5-788.00 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 23 | Exostosenabtragung | exostose | 5-788.00 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 24 | 1× DMMO allein | dmmo | 5-788.52 5-93b.0 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b | A zeigt I20O, Daten und Auswertung I20N (Aufwertung 5-788.52). | |
| 25 | 2× DMMO allein | dmmo | 5-788.53 5-93b.0 5-86a.10 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 26 | 1–2× Weil | weil | 5-788.53 5-93b.0 5-86a.10 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 27 | 3× DMMO allein | dmmo | 5-788.54 5-93b.0 5-86a.11 | — / I20F | I20O / I20F | — / I20F / nein | toggle (A entfaellt; C rechnet aus den Kodes) | — |  | |
| 28 | 4× DMMO allein | dmmo | 5-788.55 5-93b.0 5-86a.12 | — / I20F | I20O / I20F | — / I20F / nein | toggle (A entfaellt; C rechnet aus den Kodes) | — |  | |
| 29 | PIP 1 Zehe | kleinzehen_pip | 5-808.bd | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 30 | PIP 2 Zehen | kleinzehen_pip | 5-808.be 5-86a.10 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 31 | PIP 3 Zehen | kleinzehen_pip | 5-808.bf 5-86a.11 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b | Zweigtext traegt noch die 2024er Regel '>2 keine H-DRG'. | |
| 32 | PIP 4 Zehen | kleinzehen_pip | 5-808.bg 5-86a.12 | I20O / I20F | I20O / I20F | I20O / I20F / hybrid | gleich (A entfaellt (Zweige abgeloest)) | b |  | |
| 33 | PIP 5 Gelenke (5-808.bh) | kleinzehen_pip | 5-808.bh | I20O / I20F | I20O / I20F | — / I20F / nein | toggle (A entfaellt; C rechnet aus den Kodes) | — | Kein App-Fall: der Kodeblock deckelt bei vier Zehen (bd–bg). | |
| 34 | TEP primaer | tep_infinity, tep_vantage, tep_inbone | 5-826.00 | — / I05B | — / I05B | — / I05B / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 35 | TEP Wechsel | tep_infinity | 5-827.10 | — / I43B | — / I05B | — / I43B / — | toggle (A entfaellt; C rechnet aus den Kodes) | — | Seit 6b ueber den Modifikator wechsel an tep_*. | |
| 36 | TTC-Arthrodesenagel | arthrodesenagel_retro | 5-808.71 5-93b.6 | — / I20A | — / I20A | — / I20A / — | gleich (A entfaellt (Zweige abgeloest)) | f |  | |
| 37 | OSG-Arthrodese ohne Spongiosa | arthrodese_osg | 5-808.70 5-93b.0 | — / I13E | — / I13D | — / I13D / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 38 | OSG-Arthrodese + Spongiosa | arthrodese_osg | 5-808.70 5-93b.0 5-93b.e 5-784.0n 5-783.0d | — / I13D | — / I13D | — / I13D / — | gleich (A entfaellt (Zweige abgeloest)) | f |  | |
| 39 | AMIC offen | amic | 5-801.nk 5-783.0 5-784.0s | — / I13G | — / I13G | — / I13G / — | gleich (A entfaellt (Zweige abgeloest)) | c |  | |
| 40 | AMIC + Innenknoechelosteotomie | amic | 5-801.nk 5-783.0 5-784.0s 5-781.an 5-93b.0 | — / I13E | — / I13G | — / I13G / — | gleich (A entfaellt (Zweige abgeloest)) | c |  | |
| 41 | Brostrom ohne Internal Brace | brostrom_gould | 5-806.5 5-869.2 5-782.1r | — / I59Z | — / I59Z | — / I59Z / — | gleich (A entfaellt (Zweige abgeloest)) | c | Kodeblock schiebt 5-806.5, der Kodiertext nennt 5-806.4h. | |
| 42 | Brostrom + Internal Brace | brostrom_int_brace | 5-806.5 5-869.2 5-782.1r 5-806.6 | — / I59Z | — / I59Z | — / I59Z / — | gleich (A entfaellt (Zweige abgeloest)) | c |  | |
| 43 | Arthrorise, Alter < 18 | arthrorise | 5-809.1m 5-93b.0 | — / variabel | — / I20E | — / I20E / — | gleich (A entfaellt (Zweige abgeloest)) | b | Alter ist heute nur Text; die Auswertung kennt kein Alterskriterium. | |
| 44 | Achillessehnennaht offen | as_naht | 5-855.19 5-855.39 | — / I27E | — / I27E | — / I27E / — | gleich (A entfaellt (Zweige abgeloest)) | d |  | |
| 45 | FHL-Transfer | fhl_transfer | 5-854.49 5-869.2 5-855.39 5-855.19 | — / I27D | — / I27D | — / I27D / — | gleich (A entfaellt (Zweige abgeloest)) | a, d, f |  | |
| 46 | Subtalare Arthrodese | subtalar_arthrodese | 5-808.80 5-93b.0 | — / I13E | — / I13E | — / I13E / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 47 | TN-Arthrodese | tn_arthrodese | 5-808.80 5-93b.0 5-784.0s 5-783.0d | — / I13E | — / I13E | — / I13E / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 48 | Double-Arthrodese | double_arthrodese | 5-808.81 5-93b.0 5-784.1t 5-783.2d | — / I13E | — / I13E | — / I13E / — | gleich (A entfaellt (Zweige abgeloest)) | f |  | |
| 49 | Triple-Arthrodese | triple_arthrodese | 5-808.82 5-93b.0 5-784.1t 5-783.2d | — / I20B | — / I20B | — / I20B / — | gleich (A entfaellt (Zweige abgeloest)) | f |  | |
| 50 | Lambrinudi | hohlfuss_lambrinudi | 5-808.82 5-93b.0 | — / I20B | — / I20B | — / I20B / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 51 | MDO (minimalinvasiv oder offen) | mdo_mini, mdo_offen | 5-781.1t 5-93b.0 | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 52 | MDO + Cotton allogen | mdo_mini, mdo_offen | 5-781.1t 5-93b.0 5-781.4u 5-784.7u | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | — | Zweigtitel bleibt 'Calcaneus-OT'; der Cotton-Anteil erscheint nur in der Kodeliste. | |
| 53 | LCOT (verlaengernde Calcaneus-OT) | lcot | 5-781.8t 5-93b.e | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 54 | Calcaneoplastie (Haglund mini) | haglund_mini | 5-782.at 5-855.39 5-859.19 | I20O / I27E | I20O / I27E | I20O / I27E / hybrid | gleich (A entfaellt (Zweige abgeloest)) | a, b, c | kpAmbZusatz/hebelStat 5-859.19 stehen nur im Zweig, nicht in den Daten. | |
| 55 | Haglund + AS-Split/Refix | haglund_as_split | 5-782.at 5-855.39 5-855.19 5-854.29 5-859.19 | — / I27D | — / I27D | — / I27D / — | gleich (A entfaellt (Zweige abgeloest)) | a, d |  | |
| 56 | Os Tib Ext ohne MDO | os_tib_ext | 5-854.2b 5-782.1u 5-869.2 | — / I59Z | — / I59Z | — / I59Z / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 57 | Os Tib Ext + MDO | os_tib_ext | 5-854.2b 5-782.1u 5-869.2 5-781.1t 5-93b.0 | — / I20C | — / I59Z | — / I59Z / — | gleich (A entfaellt (Zweige abgeloest)) | a |  | |
| 58 | Luxation ohne Zusatz | peroneal_lux | 5-806.7 5-850.b9 | — / I59Z | — / I13G | — / I13G / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 59 | Luxation + Rinnenvertiefung | peroneal_lux | 5-806.7 5-850.b9 5-781.ar | — / I13G | — / I13G | — / I13G / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 60 | Luxation + Naht | peroneal_lux | 5-806.7 5-850.b9 5-855.19 5-855.39 | — / I27E | — / I13G | — / I13G / — | gleich (A entfaellt (Zweige abgeloest)) | d |  | |
| 61 | Peronealsehnennaht | peroneal_naht | 5-855.29 5-855.39 5-852.29 | — / I27E | — / I27E | — / I27E / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 62 | Peroneal-Tenodese | peroneal_rek | 5-855.29 5-855.39 5-852.29 5-855.89 | — / I27E | — / I27E | — / I27E / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 63 | Coalitio TC ohne LCOT | coalition_tc | 5-781.at 5-856.4a 5-852.g9 | — / I27D | — / I27D | — / I27D / — | gleich (A entfaellt (Zweige abgeloest)) | f |  | |
| 64 | Coalitio CN ohne LCOT | coalition_cn | 5-781.at 5-856.4a 5-852.g9 | — / I27D | — / I27D | — / I27D / — | gleich (A entfaellt (Zweige abgeloest)) | f |  | |
| 65 | Coalitio + LCOT | coalition_tc | 5-781.at 5-856.4a 5-852.g9 5-781.4t 5-784.7t | — / I20C | — / I27D | — / I27D / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 66 | Coalitio + LCOT, Alter < 12 | coalition_tc | 5-781.at 5-856.4a 5-852.g9 5-781.4t 5-784.7t | — / I20B | — / I27D | — / I27D / — | gleich (A entfaellt (Zweige abgeloest)) | — | Alter steht nur im Zweigtext; weder Daten noch Auswertung kennen es. | |
| 67 | Cotton autolog | cotton | 5-781.4u 5-784.0u | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | — | Kodiertext nennt nur die allogene Fassung (5-784.7u). | |
| 68 | Cotton allogen | cotton | 5-781.4u 5-784.7u | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | — | implantatfrei seit 34475c9; Materialsatz nur Knochen. | |
| 69 | TMT 1 (1 Gelenk) | arthrodese_tmt1 | 5-808.a4 5-93b.e 5-93b.0 5-784.0u | — / I20D | — / I20D | — / I20D / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 70 | TMT 2 (1 Gelenk, Beckenkammspan) | arthrodese_tmt1 | 5-808.a4 5-93b.e 5-784.0u 5-784.1u 5-783.2d | — / I20D | — / I20D | — / I20D / — | gleich (A entfaellt (Zweige abgeloest)) | f |  | |
| 71 | TMT 2–3 (2 Gelenke) | arthrodese_tmt | 5-808.a5 5-93b.e 5-784.0u | — / I20D | — / I20D | — / I20D / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 72 | TMT 1–3 (3 Gelenke) | arthrodese_tmt13 | 5-808.a6 5-93b.e 5-93b.0 5-784.0u | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 73 | TMT 1–3 + TMT 2 (4 Gelenke) | arthrodese_tmt13 | 5-808.a7 5-93b.e 5-93b.0 5-784.0u 5-784.1u 5-783.2d | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | f | Modifikator '4–5 Gelenke' (5-808.a7) liegt an arthrodese_tmt13. | |
| 74 | Supramalleolare OT valgisierend | supramal_valgus | 5-781.0n 5-93b.e | — / I13E | — / I13E | — / I13E / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 75 | Supramalleolare OT varisierend | supramal_varus | 5-781.1n 5-93b.e | — / I13E | — / I13E | — / I13E / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 76 | Weber B einfach | fraktur_fibula_einfach | 5-793.3r 5-793.kr | I13N / I13G | I13N / I13G | I13N / I13G / — | gleich (A entfaellt (Zweige abgeloest)) | — | Seit 6b eigener Eintrag (3ac). | |
| 77 | Weber B/C + Syndesmose | fraktur_fibula_mehrfragment | 5-794.2r 5-794.kr 5-795.kr | I13N / I13E | I13N / I13E | I13N / I13E / — | gleich (A entfaellt (Zweige abgeloest)) | — | Seit 6b eigener Eintrag mit Modifikator syndesmose (3ac). | |
| 78 | Dwyer ohne Zusatz | hohlfuss_dwyer | 5-781.1t 5-93b.0 | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | — |  | |
| 79 | Dwyer + Peronealtransfer | hohlfuss_dwyer | 5-781.1t 5-93b.0 5-854.29 | — / I20C | — / I20C | — / I20C / — | gleich (A entfaellt (Zweige abgeloest)) | d, f |  | |
| 80 | Metallentfernung | metallentfernung | 5-787.6t | — / — | — / — | — / — / — | gleich (A entfaellt (Zweige abgeloest)) | — | umgezogen: Werte kommen aus steuerAnzeige(). | |
| 81 | Diabetischer Fuss, Debridement | df_debridement | 5-893.1d | — / — | — / F27B | — / F27B / — | gleich (A entfaellt (Zweige abgeloest)) | e | umgezogen: Werte kommen aus steuerAnzeige(). | |
| 82 | Diabetischer Fuss, Amputation | df_amputation | 5-865.1 | — / — | — / F13B | — / F13B / — | gleich (A entfaellt (Zweige abgeloest)) | e | umgezogen: Werte kommen aus steuerAnzeige(). | |
| 83 | Achillessehnen-Tendoskopie | as_tendoskopie | 5-852.29 | — / — | — / I27E | — / I27E / — | gleich (A entfaellt (Zweige abgeloest)) | a | umgezogen; Rang 129 < 135 (Haglund) und < 119 (MTP-I): Ergaenzung a. | |
| 84 | AS-Debridement bei Tendinose | as_debridement | 5-852.29 | — / — | — / I27E | — / I27E / — | gleich (A entfaellt (Zweige abgeloest)) | a | umgezogen: Werte kommen aus steuerAnzeige(). | |

**Zählung.** gleich 66 · toggle 18 · abweichend 0 · kein Eintrag 0.

## Sollwerte aus hybrid-systematik.md Abschnitt 5

| Nr | Konstellation | Kodes | Soll | Ist | Status | Quelle |
|---|---|---|---|---|---|---|
| 1 | Hallux valgus subkapital 5-788.5e allein oder mit Akin | 5-788.5e | I20O / — | I20O / I20E | gleich | MU S. 22 |
| 2 | Hallux valgus + Arthroplastik 5-788.60 | 5-788.5c 5-788.60 | — / I20F | — / I20F | gleich | MU S. 22; V70 |
| 3 | Hallux valgus + 1× Hohmann (5-788.08, 1 Knochen) | 5-788.5c 5-788.06 | I20O / — | I20O / I20E | gleich | MU S. 22 (V6) |
| 4 | Hallux valgus + 1× PIP | 5-788.5c 5-808.bd | I20O / — | I20O / I20E | gleich | MU S. 22–23 (V4) |
| 5 | Hallux valgus + 2–4× PIP | 5-788.5c 5-808.be | I20N / — | I20N / I20E | gleich | MU S. 22–23 (V4) |
| 6 | Hallux valgus + 1–2× Weil/DMMO | 5-788.5c 5-788.53 | I20N / — | I20N / I20E | gleich | MU S. 23; V70 |
| 7 | Hallux valgus + 3× DMMO 5-788.54 (2026) | 5-788.5c 5-788.54 | — / I20E | — / I20E | gleich | FR; DH S. 1081 |
| 8 | 3× DMMO allein, 1 Tag | 5-788.54 | — / I20F | — / I20F | gleich | FR S. 15 |
| 9 | Metatarsalgie 1–2× Weil/DMMO | 5-788.53 | I20O / — | I20O / I20F | gleich | MU S. 22 |
| 10 | ASK OSG mit Hybrid-Kodes | 5-812.ek 5-811.2k | I20O / — | I20O / I20F | gleich | MU S. 22 |
| 11 | Haglundabtragung 5-782.at | 5-782.at | I20O / — | I20O / I27E | gleich | MU S. 22; V68 |
| 12 | Haglund + Bursektomie Unterschenkel 5-859.19, > 15 J. | 5-782.at 5-859.19 | — / I27E | I20O / I27E | abweichend | SCH S. 24; H-03 |
| 13 | MTP-I-Arthrodese 5-808.b0 allein | 5-808.b0 | I20N / — | I20N / I20E | gleich | MU S. 23 |
| 14 | MTP-I + 1–4× PIP | 5-808.b0 5-808.bf | I20N / — | I20N / I20E | gleich | MU S. 23 |
| 15 | MTP-I + Exostosen MT II–V 3 Knochen 5-788.08 | 5-808.b0 5-788.08 | I20M / — | I20N / I20E | abweichend | MU S. 24; V36 |
| 16 | MTP-I + 3× DMMO | 5-808.b0 5-788.54 | — / I20D | — / I20D | gleich | WE |
| 17 | MTP-I + 4× DMMO | 5-808.b0 5-788.55 | — / I20C | — / I20C | gleich | WE |
| 18 | Lapidus allein | 5-808.a4 | — / I20D | I20M / I20D | abweichend | MU S. 24; V68 |
| 19 | Lapidus + Akin | 5-808.a4 5-788.56 | I20M / — | I20M / I20D | gleich | MU S. 24; V40 + V68 |
| 20 | Lapidus + Akin + 5-854.2c | 5-808.a4 5-788.56 5-854.2c | I20M / — | I20M / I20D | gleich | V70\V66; WG 07.09.2026 |
| 21 | Lapidus + Spongiosa 5-783.0v + 5-784.0v | 5-808.a4 5-788.56 5-783.0v 5-784.0v | — / I20D | — / I20D | gleich | V66 |
| 22 | Arthrorise 5-809.1m, Patient < 18 | 5-809.1m | — / I20E | — / I20E | gleich | DH S. 1042 |
| 23 | Arthrorise beidseits, Kind | 5-809.1m | — / I20E | — / I20E | gleich | FR; DH |
| 24 | Rueckfuss-Arthrodesen, Achskorrekturen Rueckfuss | 5-808.82 | — / I20B | — / I20B | gleich | MU S. 24 |
| 25 | Rezidiv MTP-I 5-808.b7 + 5-783.2d + 5-784.1v | 5-808.b7 5-783.2d 5-784.1v | — / I20E | — / I20E | kein App-Fall | WE |
| 26 | Achillessehnennaht 5-855.19 (2026 Kontextprozedur) | 5-855.19 5-855.39 | — / I27E | — / I27E | gleich | FR; SCH; DH |
| 27 | Tendoskopie 5-852.29 allein | 5-852.29 | — / I27E | — / I27E | gleich | WG 30.08.2026 |
| 28 | Tendoskopie + Calcaneoplastie 5-782.at, HD Haglund | 5-782.at 5-852.29 | — / I27E | I20O / I27E | abweichend | WG 13.09.2026 |
| 29 | Tendoskopie + MTP-I-Arthrodese, HD M20.2 | 5-808.b0 5-852.29 | I20N / — | I20N / I20E | gleich | WG 13.09.2026 |
| 30 | FHL-Transfer 5-854.29 + Lapidus 5-808.a4 + Akin 5-788.56 | 5-808.a4 5-788.56 5-854.29 | — / I20D | — / I20D | gleich | WG 13.09.2026 |

## Feld `ziel` je Zweig (Punkt 10: geht beim Umzug etwas verloren?)

| Zweig | erste Schalterstellung | `ziel` im Zweig | `hinweise` in den Daten | Status |
|---|---|---|---|---|
| "Lapidus" | Lapidus ohne Akin | nein | 3 | nur in den Daten |
| "MTP-I-Arthrodese" | MTP-I allein | nein | 2 | nur in den Daten |
| "MTP-I-Arthrodese + DMMO" | MTP-I + 1× DMMO | nein | 2 | nur in den Daten |
| "MTP-I-Arthrodese + ≥3 DMMO" | MTP-I + 3× DMMO | nein | 2 | nur in den Daten |
| lbl+(mitAkin | Chevron ohne Zusatz | nein | 0 | keins von beidem |
| "Kleinzehen/DMMO" | 1× DMMO allein | nein | 1 | nur in den Daten |
| (weil.length&&!dmmo.length | 3× DMMO allein | nein | 1 | nur in den Daten |
| "OSG-TEP primär (" | TEP primaer | nein | 3 | nur in den Daten |
| "OSG-TEP Wechsel (" | TEP Wechsel | nein | 1 | nur in den Daten |
| "Arthrodesenagel (TTC-Arthrodese)" | TTC-Arthrodesenagel | nein | 2 | nur in den Daten |
| "OSG-Arthrodese" | OSG-Arthrodese ohne Spongiosa | nein | 3 | nur in den Daten |
| amicIKO? | AMIC offen | nein | 1 | nur in den Daten |
| "Brostrom-Gould" | Brostrom ohne Internal Brace | nein | 1 | nur in den Daten |
| "Arthrorise" | Arthrorise, Alter < 18 | nein | 1 | nur in den Daten |
| "Achillessehnennaht (offen)" | Achillessehnennaht offen | nein | 2 | nur in den Daten |
| "FHL-Transfer" | FHL-Transfer | nein | 1 | nur in den Daten |
| rfLabel | Subtalare Arthrodese | nein | 1 | nur in den Daten |
| "Calcaneus-OT" | MDO (minimalinvasiv oder offen) | nein | 2 | nur in den Daten |
| "Calcaneoplastie" | Calcaneoplastie (Haglund mini) | nein | 1 | nur in den Daten |
| "Haglund + AS-Split/Refix" | Haglund + AS-Split/Refix | nein | 2 | nur in den Daten |
| "Os Tib Ext" | Os Tib Ext ohne MDO | nein | 1 | nur in den Daten |
| "Peronealsehnenluxation" | Luxation ohne Zusatz | nein | 1 | nur in den Daten |
| "Peronealsehnen " | Peronealsehnennaht | nein | 0 | keins von beidem |
| "Coalitio " | Coalitio TC ohne LCOT | nein | 1 | nur in den Daten |
| "Cotton-Osteotomie" | Cotton autolog | nein | 0 | keins von beidem |
| "TMT-Arthrodese" | TMT 1 (1 Gelenk) | nein | 1 | nur in den Daten |
| "TMT-Arthrodese 1–3" | TMT 1–3 (3 Gelenke) | nein | 1 | nur in den Daten |
| "Supramalleolare OT" | Supramalleolare OT valgisierend | nein | 1 | nur in den Daten |
| fxLabel | Weber B einfach | nein | 2 | nur in den Daten |
| fxLabel+" + Syndesmose" | Weber B/C + Syndesmose | nein | 2 | nur in den Daten |
| "Dwyer-Osteotomie" | Dwyer ohne Zusatz | nein | 0 | keins von beidem |
| "Metallentfernung (generisch)" | Metallentfernung | nein | 4 | nur in den Daten |
| "Diabetischer Fuß — " | Diabetischer Fuss, Debridement | nein | 5 | nur in den Daten |
| (ohne Anker) | Achillessehnen-Tendoskopie | nein | 2 | nur in den Daten |
