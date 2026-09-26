#!/usr/bin/env python3
"""Schritt 6a: Abweichungsliste der Literal-Zweige des OP-Berichts.

Drei Spalten je Zeile (Zweig × Schalterstellung):

  A  Literal   — was der Zweig im OP-Bericht heute anzeigt (aus app.html gelesen)
  B  Daten     — der zugehoerige Eintrag in data/opsteuerung.json
  C  Auswertung— was hdrgAuswertung() aus denselben Kodes macht

Spalte C rechnet mit dem echten Code aus app.html: die Funktionen werden zur
Laufzeit aus der Datei geschnitten (Marker s. JS_MARKER) und in einer
JS-Laufzeit ausgefuehrt. Node wird bevorzugt, sonst jsc (JavaScriptCore,
liegt auf macOS im System). Nichts wird kopiert, damit die Pruefung bei jedem
Stand von app.html neu gilt.

Aufruf:  python3 scripts/verify_zweige_6a.py
Ausgabe: out/abgleich_6a.json, abgleich-zweige-6a.md, hybrid_testfaelle.json
         sowie eine Zusammenfassung auf der Konsole.

Das Skript aendert app.html und data/ nicht.
"""
import json, os, re, shutil, subprocess, sys, tempfile, hashlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(REPO, "app.html")
DATEN = os.path.join(REPO, "data", "opsteuerung.json")
KATALOG = os.path.join(REPO, "data", "katalog2026.json")
OUT = os.path.join(REPO, "out")

# Schnittmarken fuer den JS-Ausschnitt: (Anfang, Ende-exklusiv)
JS_MARKER = [
    ("var DRG_RANG  =", "// Gruppen des Aufklappers"),
    ("function steuerAnzeige(key){", "// Hydration (Single Source)"),
    ("function obEintragEff(key, mods){", "// Zahl der Gelenkfaecher"),
]

# ---------------------------------------------------------------- Faelle
# Je Zeile: Zweig-Anker (wie im Memo), Schalterstellung, OP_STEUERUNG-Schluessel,
# die Kodes, die der Kodeblock (allOPS) in dieser Stellung schiebt, sowie die
# Anzeigewerte des Zweigs (A). "betrifft" markiert die Ergaenzungen a–f aus dem
# Umsetzungsplan, "anmerkung" ist knapp und nur, wo eine Empfehlung naheliegt.
F = lambda **kw: kw
FAELLE = [
 F(zweig='"Lapidus"', stellung="Lapidus ohne Akin", keys=["lapidus"],
   codes=["5-808.a4","5-788.40","5-93b.0","5-93b.e","5-783.0v","5-784.0u","5-854.2c"],
   a_hdrg="—", a_drg="I20D", betrifft=["f"],
   anmerkung="Kodeliste enthaelt 5-854.2c immer; ohne Sehnentransfer gehoert er nicht in den Fall."),
 F(zweig='"Lapidus"', stellung="Lapidus + Akin", keys=["lapidus"],
   codes=["5-808.a4","5-788.40","5-93b.0","5-93b.e","5-783.0v","5-784.0u","5-854.2c","5-788.56"],
   a_hdrg="—", a_drg="I20D", betrifft=["a","f"],
   anmerkung="C1/C3: Zweig zeigt H-DRG '—', Daten und Auswertung I20M."),
 F(zweig='"Lapidus"', stellung="Lapidus + Akin + 3× DMMO", keys=["lapidus"],
   codes=["5-808.a4","5-788.40","5-93b.0","5-93b.e","5-783.0v","5-784.0u","5-854.2c","5-788.56","5-788.54","5-86a.12"],
   a_hdrg="—", a_drg="I20D", betrifft=["a"],
   anmerkung="C2: Zweigtitel bleibt 'Lapidus', die DMMO-Zahl aendert nichts."),
 F(zweig='"Lapidus"', stellung="Lapidus + Spongiosa Metatarsale (Soll 5-784.0v)", keys=["lapidus"],
   codes=["5-808.a4","5-788.40","5-93b.0","5-93b.e","5-783.0v","5-784.0v","5-854.2c","5-788.56"],
   a_hdrg="—", a_drg="I20D", betrifft=["f"],
   anmerkung="Kodeblock schiebt 5-784.0u (Tarsale); der Hebel in den Daten ist 5-784.0v (Metatarsale)."),
 F(zweig='"MTP-I-Arthrodese"', stellung="MTP-I allein", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e"], a_hdrg="I20N", a_drg="I20E", betrifft=["b"]),
 F(zweig='"MTP-I-Arthrodese"', stellung="MTP-I + Akin", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e","5-788.56"], a_hdrg="I20N", a_drg="I20E", betrifft=["b"]),
 F(zweig='"MTP-I-Arthrodese"', stellung="MTP-I nach Hoffmann/Tillmann (4× Arthroplastik)", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e","5-788.60","5-808.b2"], a_hdrg="I20N", a_drg="I20E", betrifft=["a"],
   anmerkung="5-788.60 steht in V70 minus V66: nichtKontext bei I20M, Kontext bei I20O/I20N."),
 F(zweig='"MTP-I-Arthrodese + DMMO"', stellung="MTP-I + 1× DMMO", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e","5-788.52","5-86a.10"], a_hdrg="I20N", a_drg="I20E", betrifft=["b"]),
 F(zweig='"MTP-I-Arthrodese + DMMO"', stellung="MTP-I + 2× DMMO", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e","5-788.53","5-86a.11"], a_hdrg="I20N", a_drg="I20E", betrifft=["b"]),
 F(zweig='"MTP-I-Arthrodese + ≥3 DMMO"', stellung="MTP-I + 3× DMMO", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e","5-788.54","5-86a.12"], a_hdrg="—", a_drg="I20D", betrifft=[],
   anmerkung="Sechster Teil Punkt 2: C liefert I20D aus der Kontextregel, ohne festen Wert im Zweig."),
 F(zweig='"MTP-I-Arthrodese + ≥3 DMMO"', stellung="MTP-I + 4× DMMO", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e","5-788.55","5-86a.13"], a_hdrg="—", a_drg="I20D", betrifft=[],
   anmerkung="C liefert I20C (Regel I20N → I20C), der Zweig zeigt I20D."),
 F(zweig='"MTP-I-Arthrodese"', stellung="MTP-I + PIP 3 Zehen", keys=["mtp1_arthrodese"],
   codes=["5-808.b0","5-93b.0","5-93b.e","5-808.bf","5-86a.12"], a_hdrg="I20N", a_drg="I20E", betrifft=["b"],
   anmerkung="PIP wertet auf I20N auf; MTP-I steht schon bei I20N, kein I20M."),
 F(zweig='lbl+(mitAkin', stellung="Chevron ohne Zusatz", keys=["chevron"],
   codes=["5-788.5c","5-788.40","5-93b.0","5-854.2c"], a_hdrg="I20O", a_drg="I20E", betrifft=["b"],
   anmerkung="Kodeliste enthaelt 5-854.2c immer, obwohl der Zweigtext ihn als Entscheidung beschreibt."),
 F(zweig='lbl+(mitAkin', stellung="Chevron + Akin", keys=["chevron_akin"],
   codes=["5-788.5c","5-788.40","5-93b.0","5-854.2c","5-788.56"], a_hdrg="I20O", a_drg="I20E", betrifft=["b"]),
 F(zweig='lbl+(mitAkin', stellung="Chevron + 1× DMMO", keys=["chevron"],
   codes=["5-788.5c","5-788.40","5-93b.0","5-854.2c","5-788.52","5-86a.10"], a_hdrg="I20O", a_drg="I20E", betrifft=["b"]),
 F(zweig='lbl+(mitAkin', stellung="Chevron + 2× DMMO", keys=["chevron"],
   codes=["5-788.5c","5-788.40","5-93b.0","5-854.2c","5-788.53","5-86a.11"], a_hdrg="I20O", a_drg="I20E", betrifft=["b"]),
 F(zweig='lbl+(mitAkin', stellung="Chevron + 3× DMMO", keys=["chevron"],
   codes=["5-788.5c","5-788.40","5-93b.0","5-854.2c","5-788.54","5-86a.12"], a_hdrg="I20O", a_drg="I20E", betrifft=["a"],
   anmerkung="C2: Zweig zeigt weiter I20O, Auswertung fuehrt nach I20E."),
 F(zweig='lbl+(mitAkin', stellung="Chevron + 4× DMMO", keys=["chevron"],
   codes=["5-788.5c","5-788.40","5-93b.0","5-854.2c","5-788.55","5-86a.13"], a_hdrg="I20O", a_drg="I20E", betrifft=["a"]),
 F(zweig='lbl+(mitAkin', stellung="Chevron + PIP 2 Zehen", keys=["chevron"],
   codes=["5-788.5c","5-788.40","5-93b.0","5-854.2c","5-808.be","5-86a.11"], a_hdrg="I20O", a_drg="I20E", betrifft=["b"]),
 F(zweig='lbl+(mitAkin', stellung="Scarf ohne Zusatz", keys=["scarf"],
   codes=["5-788.5e"], a_hdrg="I20O", a_drg="I20E", betrifft=["b"]),
 F(zweig='lbl+(mitAkin', stellung="Youngswick (Chip zeigt Scarf-Zweig)", keys=["youngswick"],
   codes=["5-788.5e"], a_hdrg="I20O", a_drg="I20E", betrifft=[],
   anmerkung="Kein eigener Kodepfad: der Chip laeuft ueber gz='scarf'."),
 F(zweig='lbl+(mitAkin', stellung="Cheilektomie", keys=["cheilektomie"],
   codes=["5-788.00"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"]),
 F(zweig='lbl+(mitAkin', stellung="Exostosenabtragung", keys=["exostose"],
   codes=["5-788.00"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"]),
 F(zweig='"Kleinzehen/DMMO"', stellung="1× DMMO allein", keys=["dmmo"],
   codes=["5-788.52","5-93b.0"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"],
   anmerkung="A zeigt I20O, Daten und Auswertung I20N (Aufwertung 5-788.52)."),
 F(zweig='"Kleinzehen/DMMO"', stellung="2× DMMO allein", keys=["dmmo"],
   codes=["5-788.53","5-93b.0","5-86a.10"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"]),
 F(zweig='"Kleinzehen/DMMO"', stellung="1–2× Weil", keys=["weil"],
   codes=["5-788.53","5-93b.0","5-86a.10"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"]),
 F(zweig='(weil.length&&!dmmo.length', stellung="3× DMMO allein", keys=["dmmo"],
   codes=["5-788.54","5-93b.0","5-86a.11"], a_hdrg="—", a_drg="I20F", betrifft=[]),
 F(zweig='(weil.length&&!dmmo.length', stellung="4× DMMO allein", keys=["dmmo"],
   codes=["5-788.55","5-93b.0","5-86a.12"], a_hdrg="—", a_drg="I20F", betrifft=[]),
 F(zweig='"Kleinzehen/DMMO"', stellung="PIP 1 Zehe", keys=["kleinzehen_pip"],
   codes=["5-808.bd"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"]),
 F(zweig='"Kleinzehen/DMMO"', stellung="PIP 2 Zehen", keys=["kleinzehen_pip"],
   codes=["5-808.be","5-86a.10"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"]),
 F(zweig='"Kleinzehen/DMMO"', stellung="PIP 3 Zehen", keys=["kleinzehen_pip"],
   codes=["5-808.bf","5-86a.11"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"],
   anmerkung="Zweigtext traegt noch die 2024er Regel '>2 keine H-DRG'."),
 F(zweig='"Kleinzehen/DMMO"', stellung="PIP 4 Zehen", keys=["kleinzehen_pip"],
   codes=["5-808.bg","5-86a.12"], a_hdrg="I20O", a_drg="I20F", betrifft=["b"]),
 F(zweig='"Kleinzehen/DMMO"', stellung="PIP 5 Gelenke (5-808.bh)", keys=["kleinzehen_pip"],
   codes=["5-808.bh"], a_hdrg="I20O", a_drg="I20F", betrifft=[],
   anmerkung="Kein App-Fall: der Kodeblock deckelt bei vier Zehen (bd–bg)."),
 F(zweig='"OSG-TEP primär ("', stellung="TEP primaer", keys=["tep_infinity","tep_vantage","tep_inbone"],
   codes=["5-826.00"], a_hdrg="—", a_drg="I05B", betrifft=[]),
 F(zweig='"OSG-TEP Wechsel ("', stellung="TEP Wechsel", keys=["tep_infinity"], mods=["wechsel"],
   codes=["5-827.10"], a_hdrg="—", a_drg="I43B", betrifft=[],
   anmerkung="Seit 6b ueber den Modifikator wechsel an tep_*."),
 F(zweig='"Arthrodesenagel (TTC-Arthrodese)"', stellung="TTC-Arthrodesenagel", keys=["arthrodesenagel_retro"],
   codes=["5-808.71","5-93b.6"], a_hdrg="—", a_drg="I20A", betrifft=["f"]),
 F(zweig='"OSG-Arthrodese"', stellung="OSG-Arthrodese ohne Spongiosa", keys=["arthrodese_osg"],
   codes=["5-808.70","5-93b.0"], a_hdrg="—", a_drg="I13E", betrifft=[]),
 F(zweig='"OSG-Arthrodese"', stellung="OSG-Arthrodese + Spongiosa", keys=["arthrodese_osg"],
   codes=["5-808.70","5-93b.0","5-93b.e","5-784.0n","5-783.0d"], a_hdrg="—", a_drg="I13D", betrifft=["f"]),
 F(zweig='amicIKO?', stellung="AMIC offen", keys=["amic"],
   codes=["5-801.nk","5-783.0","5-784.0s"], a_hdrg="—", a_drg="I13G", betrifft=["c"]),
 F(zweig='amicIKO?', stellung="AMIC + Innenknoechelosteotomie", keys=["amic"],
   codes=["5-801.nk","5-783.0","5-784.0s","5-781.an","5-93b.0"], a_hdrg="—", a_drg="I13E", betrifft=["c"]),
 F(zweig='"Brostrom-Gould"', stellung="Brostrom ohne Internal Brace", keys=["brostrom_gould"],
   codes=["5-806.5","5-869.2","5-782.1r"], a_hdrg="—", a_drg="I59Z", betrifft=["c"],
   anmerkung="Kodeblock schiebt 5-806.5, der Kodiertext nennt 5-806.4h."),
 F(zweig='"Brostrom-Gould"', stellung="Brostrom + Internal Brace", keys=["brostrom_int_brace"],
   codes=["5-806.5","5-869.2","5-782.1r","5-806.6"], a_hdrg="—", a_drg="I59Z", betrifft=["c"]),
 F(zweig='"Arthrorise"', stellung="Arthrorise, Alter < 18", keys=["arthrorise"], alter="<18",
   codes=["5-809.1m","5-93b.0"], a_hdrg="—", a_drg="variabel", betrifft=["b"],
   anmerkung="Alter ist heute nur Text; die Auswertung kennt kein Alterskriterium."),
 F(zweig='"Achillessehnennaht (offen)"', stellung="Achillessehnennaht offen", keys=["as_naht"],
   codes=["5-855.19","5-855.39"], a_hdrg="—", a_drg="I27E", betrifft=["d"]),
 F(zweig='"FHL-Transfer"', stellung="FHL-Transfer", keys=["fhl_transfer"],
   codes=["5-854.49","5-869.2","5-855.39","5-855.19"], a_hdrg="—", a_drg="I27D", betrifft=["a","d","f"]),
 F(zweig='rfLabel', stellung="Subtalare Arthrodese", keys=["subtalar_arthrodese"],
   codes=["5-808.80","5-93b.0"], a_hdrg="—", a_drg="I13E", betrifft=[]),
 F(zweig='rfLabel', stellung="TN-Arthrodese", keys=["tn_arthrodese"],
   codes=["5-808.80","5-93b.0","5-784.0s","5-783.0d"], a_hdrg="—", a_drg="I13E", betrifft=[]),
 F(zweig='rfLabel', stellung="Double-Arthrodese", keys=["double_arthrodese"],
   codes=["5-808.81","5-93b.0","5-784.1t","5-783.2d"], a_hdrg="—", a_drg="I13E", betrifft=["f"]),
 F(zweig='rfLabel', stellung="Triple-Arthrodese", keys=["triple_arthrodese"],
   codes=["5-808.82","5-93b.0","5-784.1t","5-783.2d"], a_hdrg="—", a_drg="I20B", betrifft=["f"]),
 F(zweig='rfLabel', stellung="Lambrinudi", keys=["hohlfuss_lambrinudi"],
   codes=["5-808.82","5-93b.0"], a_hdrg="—", a_drg="I20B", betrifft=[]),
 F(zweig='"Calcaneus-OT"', stellung="MDO (minimalinvasiv oder offen)", keys=["mdo_mini","mdo_offen"],
   codes=["5-781.1t","5-93b.0"], a_hdrg="—", a_drg="I20C", betrifft=[]),
 F(zweig='"Calcaneus-OT"', stellung="MDO + Cotton allogen", keys=["mdo_mini","mdo_offen"],
   codes=["5-781.1t","5-93b.0","5-781.4u","5-784.7u"], a_hdrg="—", a_drg="I20C", betrifft=[],
   anmerkung="Zweigtitel bleibt 'Calcaneus-OT'; der Cotton-Anteil erscheint nur in der Kodeliste."),
 F(zweig='"Calcaneus-OT"', stellung="LCOT (verlaengernde Calcaneus-OT)", keys=["lcot"],
   codes=["5-781.8t","5-93b.e"], a_hdrg="—", a_drg="I20C", betrifft=[]),
 F(zweig='"Calcaneoplastie"', stellung="Calcaneoplastie (Haglund mini)", keys=["haglund_mini"],
   codes=["5-782.at","5-855.39","5-859.19"], a_hdrg="I20O", a_drg="I27E", betrifft=["a","b","c"],
   anmerkung="kpAmbZusatz/hebelStat 5-859.19 stehen nur im Zweig, nicht in den Daten."),
 F(zweig='"Haglund + AS-Split/Refix"', stellung="Haglund + AS-Split/Refix", keys=["haglund_as_split"],
   codes=["5-782.at","5-855.39","5-855.19","5-854.29","5-859.19"], a_hdrg="—", a_drg="I27D", betrifft=["a","d"]),
 F(zweig='"Os Tib Ext"', stellung="Os Tib Ext ohne MDO", keys=["os_tib_ext"],
   codes=["5-854.2b","5-782.1u","5-869.2"], a_hdrg="—", a_drg="I59Z", betrifft=[]),
 F(zweig='"Os Tib Ext"', stellung="Os Tib Ext + MDO", keys=["os_tib_ext"],
   codes=["5-854.2b","5-782.1u","5-869.2","5-781.1t","5-93b.0"], a_hdrg="—", a_drg="I20C", betrifft=["a"]),
 F(zweig='"Peronealsehnenluxation"', stellung="Luxation ohne Zusatz", keys=["peroneal_lux"],
   codes=["5-806.7","5-850.b9"], a_hdrg="—", a_drg="I59Z", betrifft=[]),
 F(zweig='"Peronealsehnenluxation"', stellung="Luxation + Rinnenvertiefung", keys=["peroneal_lux"],
   codes=["5-806.7","5-850.b9","5-781.ar"], a_hdrg="—", a_drg="I13G", betrifft=[]),
 F(zweig='"Peronealsehnenluxation"', stellung="Luxation + Naht", keys=["peroneal_lux"],
   codes=["5-806.7","5-850.b9","5-855.19","5-855.39"], a_hdrg="—", a_drg="I27E", betrifft=["d"]),
 F(zweig='"Peronealsehnen "', stellung="Peronealsehnennaht", keys=["peroneal_naht"],
   codes=["5-855.29","5-855.39","5-852.29"], a_hdrg="—", a_drg="I27E", betrifft=[]),
 F(zweig='"Peronealsehnen "', stellung="Peroneal-Tenodese", keys=["peroneal_rek"],
   codes=["5-855.29","5-855.39","5-852.29","5-855.89"], a_hdrg="—", a_drg="I27E", betrifft=[]),
 F(zweig='"Coalitio "', stellung="Coalitio TC ohne LCOT", keys=["coalition_tc"],
   codes=["5-781.at","5-856.4a","5-852.g9"], a_hdrg="—", a_drg="I27D", betrifft=["f"]),
 F(zweig='"Coalitio "', stellung="Coalitio CN ohne LCOT", keys=["coalition_cn"],
   codes=["5-781.at","5-856.4a","5-852.g9"], a_hdrg="—", a_drg="I27D", betrifft=["f"]),
 F(zweig='"Coalitio "', stellung="Coalitio + LCOT", keys=["coalition_tc"],
   codes=["5-781.at","5-856.4a","5-852.g9","5-781.4t","5-784.7t"], a_hdrg="—", a_drg="I20C", betrifft=[]),
 F(zweig='"Coalitio "', stellung="Coalitio + LCOT, Alter < 12", keys=["coalition_tc"], alter="<12",
   codes=["5-781.at","5-856.4a","5-852.g9","5-781.4t","5-784.7t"], a_hdrg="—", a_drg="I20B", betrifft=[],
   anmerkung="Alter steht nur im Zweigtext; weder Daten noch Auswertung kennen es."),
 F(zweig='"Cotton-Osteotomie"', stellung="Cotton autolog", keys=["cotton"],
   codes=["5-781.4u","5-784.0u"], a_hdrg="—", a_drg="I20C", betrifft=[],
   anmerkung="Kodiertext nennt nur die allogene Fassung (5-784.7u)."),
 F(zweig='"Cotton-Osteotomie"', stellung="Cotton allogen", keys=["cotton"],
   codes=["5-781.4u","5-784.7u"], a_hdrg="—", a_drg="I20C", betrifft=[],
   anmerkung="implantatfrei seit 34475c9; Materialsatz nur Knochen."),
 F(zweig='"TMT-Arthrodese"', stellung="TMT 1 (1 Gelenk)", keys=["arthrodese_tmt1"],
   codes=["5-808.a4","5-93b.e","5-93b.0","5-784.0u"], a_hdrg="—", a_drg="I20D", betrifft=[]),
 F(zweig='"TMT-Arthrodese"', stellung="TMT 2 (1 Gelenk, Beckenkammspan)", keys=["arthrodese_tmt1"],
   codes=["5-808.a4","5-93b.e","5-784.0u","5-784.1u","5-783.2d"], a_hdrg="—", a_drg="I20D", betrifft=["f"]),
 F(zweig='"TMT-Arthrodese"', stellung="TMT 2–3 (2 Gelenke)", keys=["arthrodese_tmt"],
   codes=["5-808.a5","5-93b.e","5-784.0u"], a_hdrg="—", a_drg="I20D", betrifft=[]),
 F(zweig='"TMT-Arthrodese 1–3"', stellung="TMT 1–3 (3 Gelenke)", keys=["arthrodese_tmt13"],
   codes=["5-808.a6","5-93b.e","5-93b.0","5-784.0u"], a_hdrg="—", a_drg="I20C", betrifft=[]),
 F(zweig='"TMT-Arthrodese 1–3"', stellung="TMT 1–3 + TMT 2 (4 Gelenke)", keys=["arthrodese_tmt13"],
   codes=["5-808.a7","5-93b.e","5-93b.0","5-784.0u","5-784.1u","5-783.2d"], a_hdrg="—", a_drg="I20C", betrifft=["f"],
   anmerkung="Modifikator '4–5 Gelenke' (5-808.a7) liegt an arthrodese_tmt13."),
 F(zweig='"Supramalleolare OT"', stellung="Supramalleolare OT valgisierend", keys=["supramal_valgus"],
   codes=["5-781.0n","5-93b.e"], a_hdrg="—", a_drg="I13E", betrifft=[]),
 F(zweig='"Supramalleolare OT"', stellung="Supramalleolare OT varisierend", keys=["supramal_varus"],
   codes=["5-781.1n","5-93b.e"], a_hdrg="—", a_drg="I13E", betrifft=[]),
 F(zweig='fxLabel', stellung="Weber B einfach", keys=["fraktur_fibula_einfach"],
   codes=["5-793.3r","5-793.kr"], a_hdrg="I13N", a_drg="I13G", betrifft=[],
   anmerkung="Seit 6b eigener Eintrag (3ac)."),
 F(zweig='fxLabel+" + Syndesmose"', stellung="Weber B/C + Syndesmose", keys=["fraktur_fibula_mehrfragment"], mods=["syndesmose"],
   codes=["5-794.2r","5-794.kr","5-795.kr"], a_hdrg="I13N", a_drg="I13E", betrifft=[],
   anmerkung="Seit 6b eigener Eintrag mit Modifikator syndesmose (3ac)."),
 F(zweig='"Dwyer-Osteotomie"', stellung="Dwyer ohne Zusatz", keys=["hohlfuss_dwyer"],
   codes=["5-781.1t","5-93b.0"], a_hdrg="—", a_drg="I20C", betrifft=[]),
 F(zweig='"Dwyer-Osteotomie"', stellung="Dwyer + Peronealtransfer", keys=["hohlfuss_dwyer"],
   codes=["5-781.1t","5-93b.0","5-854.29"], a_hdrg="—", a_drg="I20C", betrifft=["d","f"]),
 F(zweig='"Metallentfernung (generisch)"', stellung="Metallentfernung", keys=["metallentfernung"],
   codes=["5-787.6t"], a_hdrg=None, a_drg=None, betrifft=[], umgezogen=True,
   anmerkung="umgezogen: Werte kommen aus steuerAnzeige()."),
 F(zweig='"Diabetischer Fuß — "', stellung="Diabetischer Fuss, Debridement", keys=["df_debridement"],
   codes=["5-893.1d"], a_hdrg=None, a_drg=None, betrifft=["e"], umgezogen=True,
   anmerkung="umgezogen: Werte kommen aus steuerAnzeige()."),
 F(zweig='"Diabetischer Fuß — "', stellung="Diabetischer Fuss, Amputation", keys=["df_amputation"],
   codes=["5-865.1"], a_hdrg=None, a_drg=None, betrifft=["e"], umgezogen=True,
   anmerkung="umgezogen: Werte kommen aus steuerAnzeige()."),
 F(zweig=None, stellung="Achillessehnen-Tendoskopie", keys=["as_tendoskopie"],
   codes=["5-852.29"], a_hdrg=None, a_drg=None, betrifft=["a"], umgezogen=True,
   anmerkung="umgezogen; Rang 129 < 135 (Haglund) und < 119 (MTP-I): Ergaenzung a."),
 F(zweig=None, stellung="AS-Debridement bei Tendinose", keys=["as_debridement"],
   codes=["5-852.29"], a_hdrg=None, a_drg=None, betrifft=["a"], umgezogen=True,
   anmerkung="umgezogen: Werte kommen aus steuerAnzeige()."),
]

# ------------------------------------------------- Sollwerte (Abschnitt 5)
# codes = die Kodes, mit denen die Konstellation in der App entsteht; key = der
# Eintrag, dessen hdrg/drg die Auswertung als Ausgangspunkt nimmt.
SOLL = [
 dict(nr=1, konstellation="Hallux valgus subkapital 5-788.5e allein oder mit Akin",
      key="scarf", codes=["5-788.5e"], soll=dict(hdrg="I20O", drg=None), quelle="MU S. 22"),
 dict(nr=2, konstellation="Hallux valgus + Arthroplastik 5-788.60",
      key="chevron", codes=["5-788.5c","5-788.60"], soll=dict(hdrg=None, drg="I20F"), quelle="MU S. 22; V70"),
 dict(nr=3, konstellation="Hallux valgus + 1× Hohmann (5-788.08, 1 Knochen)",
      key="chevron", codes=["5-788.5c","5-788.06"], soll=dict(hdrg="I20O", drg=None), quelle="MU S. 22 (V6)"),
 dict(nr=4, konstellation="Hallux valgus + 1× PIP",
      key="chevron", codes=["5-788.5c","5-808.bd"], soll=dict(hdrg="I20O", drg=None), quelle="MU S. 22–23 (V4)"),
 dict(nr=5, konstellation="Hallux valgus + 2–4× PIP",
      key="chevron", codes=["5-788.5c","5-808.be"], soll=dict(hdrg="I20N", drg=None), quelle="MU S. 22–23 (V4)"),
 dict(nr=6, konstellation="Hallux valgus + 1–2× Weil/DMMO",
      key="chevron", codes=["5-788.5c","5-788.53"], soll=dict(hdrg="I20N", drg=None), quelle="MU S. 23; V70"),
 dict(nr=7, konstellation="Hallux valgus + 3× DMMO 5-788.54 (2026)",
      key="chevron", codes=["5-788.5c","5-788.54"], soll=dict(hdrg=None, drg="I20E"), quelle="FR; DH S. 1081"),
 dict(nr=8, konstellation="3× DMMO allein, 1 Tag",
      key="dmmo", codes=["5-788.54"], soll=dict(hdrg=None, drg="I20F"), quelle="FR S. 15"),
 dict(nr=9, konstellation="Metatarsalgie 1–2× Weil/DMMO",
      key="dmmo", codes=["5-788.53"], soll=dict(hdrg="I20O", drg=None), quelle="MU S. 22",
      hinweis="Block 2 (24.09.2026): ohne Partnerkode bleibt es bei I20O."),
 dict(nr=10, konstellation="ASK OSG mit Hybrid-Kodes",
      key="ask_osg", codes=["5-812.ek","5-811.2k"], soll=dict(hdrg="I20O", drg=None), quelle="MU S. 22"),
 dict(nr=11, konstellation="Haglundabtragung 5-782.at",
      key="haglund_mini", codes=["5-782.at"], soll=dict(hdrg="I20O", drg=None), quelle="MU S. 22; V68"),
 dict(nr=12, konstellation="Haglund + Bursektomie Unterschenkel 5-859.19, > 15 J.",
      key="haglund_mini", codes=["5-782.at","5-859.19"], soll=dict(hdrg=None, drg="I27E"), quelle="SCH S. 24; H-03"),
 dict(nr=13, konstellation="MTP-I-Arthrodese 5-808.b0 allein",
      key="mtp1_arthrodese", codes=["5-808.b0"], soll=dict(hdrg="I20N", drg=None), quelle="MU S. 23"),
 dict(nr=14, konstellation="MTP-I + 1–4× PIP",
      key="mtp1_arthrodese", codes=["5-808.b0","5-808.bf"], soll=dict(hdrg="I20N", drg=None), quelle="MU S. 23"),
 dict(nr=15, konstellation="MTP-I + Exostosen MT II–V 3 Knochen 5-788.08",
      key="mtp1_arthrodese", codes=["5-808.b0","5-788.08"], soll=dict(hdrg="I20M", drg=None), quelle="MU S. 24; V36"),
 dict(nr=16, konstellation="MTP-I + 3× DMMO",
      key="mtp1_arthrodese", codes=["5-808.b0","5-788.54"], soll=dict(hdrg=None, drg="I20D"), quelle="WE"),
 dict(nr=17, konstellation="MTP-I + 4× DMMO",
      key="mtp1_arthrodese", codes=["5-808.b0","5-788.55"], soll=dict(hdrg=None, drg="I20C"), quelle="WE"),
 dict(nr=18, konstellation="Lapidus allein",
      key="lapidus", codes=["5-808.a4"], soll=dict(hdrg=None, drg="I20D"), quelle="MU S. 24; V68"),
 dict(nr=19, konstellation="Lapidus + Akin",
      key="lapidus", codes=["5-808.a4","5-788.56"], soll=dict(hdrg="I20M", drg=None), quelle="MU S. 24; V40 + V68"),
 dict(nr=20, konstellation="Lapidus + Akin + 5-854.2c",
      key="lapidus", codes=["5-808.a4","5-788.56","5-854.2c"], soll=dict(hdrg="I20M", drg=None), quelle="V70\\V66; WG 07.09.2026"),
 dict(nr=21, konstellation="Lapidus + Spongiosa 5-783.0v + 5-784.0v",
      key="lapidus", codes=["5-808.a4","5-788.56","5-783.0v","5-784.0v"], soll=dict(hdrg=None, drg="I20D"), quelle="V66"),
 dict(nr=22, konstellation="Arthrorise 5-809.1m, Patient < 18",
      key="arthrorise", codes=["5-809.1m"], alter="u18", soll=dict(hdrg=None, drg="I20E"), quelle="DH S. 1042",
      hinweis="Alter unter 18 (H-02): keine Hybrid."),
 dict(nr=23, konstellation="Arthrorise beidseits, Kind",
      key="arthrorise", codes=["5-809.1m"], seite="bds", alter="u18", soll=dict(hdrg=None, drg="I20E"), quelle="FR; DH",
      hinweis="Alter und Beidseitigkeit; beidseitsSperre wird mitgerechnet."),
 dict(nr=24, konstellation="Rueckfuss-Arthrodesen, Achskorrekturen Rueckfuss",
      key="triple_arthrodese", codes=["5-808.82"], soll=dict(hdrg=None, drg="I20B"), quelle="MU S. 24"),
 dict(nr=25, konstellation="Rezidiv MTP-I 5-808.b7 + 5-783.2d + 5-784.1v",
      key="mtp1_arthrodese", codes=["5-808.b7","5-783.2d","5-784.1v"], soll=dict(hdrg=None, drg="I20E"), quelle="WE",
      hinweis="5-808.b7 kommt in keiner Kodeliste der App vor."),
 dict(nr=26, konstellation="Achillessehnennaht 5-855.19 (2026 Kontextprozedur)",
      key="as_naht", codes=["5-855.19","5-855.39"], soll=dict(hdrg=None, drg="I27E"), quelle="FR; SCH; DH"),
 dict(nr=27, konstellation="Tendoskopie 5-852.29 allein",
      key="as_tendoskopie", codes=["5-852.29"], soll=dict(hdrg=None, drg="I27E"), quelle="WG 30.08.2026"),
 dict(nr=28, konstellation="Tendoskopie + Calcaneoplastie 5-782.at, HD Haglund",
      key="haglund_mini", codes=["5-782.at","5-852.29"], soll=dict(hdrg=None, drg="I27E"), quelle="WG 13.09.2026"),
 dict(nr=29, konstellation="Tendoskopie + MTP-I-Arthrodese, HD M20.2",
      key="mtp1_arthrodese", codes=["5-808.b0","5-852.29"], soll=dict(hdrg="I20N", drg=None), quelle="WG 13.09.2026"),
 dict(nr=30, konstellation="FHL-Transfer 5-854.29 + Lapidus 5-808.a4 + Akin 5-788.56",
      key="lapidus", codes=["5-808.a4","5-788.56","5-854.29"], soll=dict(hdrg=None, drg="I20D"), quelle="WG 13.09.2026",
      hinweis="Sperre folgt aus AKF08-V6; HDRG_FALLREGELN liest app.html noch nicht."),
]


# ---------------------------------------------------------------- Helfer
def js_runtime():
    node = shutil.which("node")
    if node:
        return [node], "node"
    jsc = "/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc"
    if os.path.exists(jsc):
        return [jsc], "jsc"
    sys.exit("Weder node noch jsc gefunden — Spalte C kann nicht gerechnet werden.")


def js_ausschnitt(app):
    teile = []
    for anfang, ende in JS_MARKER:
        i = app.index(anfang)
        j = app.index(ende, i)
        teile.append(app[i:j])
    return "\n".join(teile)


def rechne_c(app, daten, katalog, faelle, sollfaelle):
    """Spalte C und die Sollwerte in einer JS-Laufzeit rechnen."""
    js = """
var _aus = (typeof print === "function") ? print : console.log;
var _DATEN = %s, _KAT = %s, _FAELLE = %s, _SOLL = %s;
var window = { _fx: function(s){ return s; }, _HD: _KAT._HD, _DRG: {}, _HDRG: {},
               _DATA: { opsteuerung: _DATEN, katalog2026: _KAT } };
var OP_STEUERUNG = _DATEN.OP_STEUERUNG;
var HDRG_REGELN = _DATEN.HDRG_REGELN || null;
var HDRG_FALLREGELN = _DATEN.HDRG_FALLREGELN || null;
var HDRG_KOMBI = _DATEN.HDRG_KOMBI || null;
var DRG_RANG_LG = _DATEN.DRG_RANG_LG || null;
%s
function auswerten(key, codes, seite, alter){
  var best = OP_STEUERUNG[key] || {};
  var erg = hdrgAuswertung({ best: best, bestKey: key, hdrg: best.hdrg, drg: best.drg,
                             codes: codes, ambulant: true, kodesVollstaendig: true,
                             partner: (typeof partnerErfuellt === "function")
                                        ? partnerErfuellt(codes, key) : undefined,
                             alter: alter || null });
  return { hdrg: erg.hdrg, drg: erg.drg, hybrid: erg.hybrid, sperre: erg.sperre || null,
           partner: erg.partner,
           setting: erg.setting, satz: erg.satz, warnungen: erg.warnungen,
           regel: erg.regel ? (erg.regel.hdrg || []).join("/") : null,
           kontext: (erg.treffer.kontext || []).map(function(k){ return k.code; }),
           aufwertung: (erg.treffer.aufwertung || []).map(function(a){ return a.code; }),
           beidseits: beidseitsSperre(seite || "", !!best.hdrg, codes, key) };
}
var raus = { faelle: [], soll: [] };
_FAELLE.forEach(function(f){
  var zeile = { keys: {} };
  (f.keys || []).forEach(function(k){
    var best = OP_STEUERUNG[k];
    if (!best) { zeile.keys[k] = null; return; }
    var eff = (typeof obEintragEff === "function" && (f.mods || []).length) ? obEintragEff(k, f.mods) : best;
    var erg = hdrgAuswertung({ best: eff, bestKey: k, hdrg: eff.hdrg, drg: eff.drg, codes: f.codes,
                               ambulant: true, kodesVollstaendig: true,
                               partner: (typeof partnerErfuellt === "function") ? partnerErfuellt(f.codes, f.keys || k) : undefined,
                               alter: f.alter || null });
    zeile.keys[k] = { hdrg: erg.hdrg, drg: erg.drg, hybrid: erg.hybrid, sperre: erg.sperre || null,
                      partner: erg.partner, setting: erg.setting, satz: erg.satz,
                      warnungen: erg.warnungen,
                      regel: erg.regel ? (erg.regel.hdrg || []).join("/") : null,
                      kontext: (erg.treffer.kontext || []).map(function(x){ return x.code; }),
                      aufwertung: (erg.treffer.aufwertung || []).map(function(x){ return x.code; }),
                      beidseits: beidseitsSperre("bds", !!eff.hdrg, f.codes, k) };
  });
  raus.faelle.push(zeile);
});
_SOLL.forEach(function(s){
  raus.soll.push(OP_STEUERUNG[s.key] ? auswerten(s.key, s.codes, s.seite || "", s.alter || null) : null);
});
_aus(JSON.stringify(raus));
""" % (json.dumps(daten, ensure_ascii=False), json.dumps(katalog, ensure_ascii=False),
       json.dumps(faelle, ensure_ascii=False), json.dumps(sollfaelle, ensure_ascii=False),
       js_ausschnitt(app))
    cmd, name = js_runtime()
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
        fh.write(js)
        pfad = fh.name
    try:
        roh = subprocess.check_output(cmd + [pfad], text=True)
    finally:
        os.unlink(pfad)
    return json.loads(roh.strip().splitlines()[-1]), name


def memo_zweige(app):
    i = app.index("const [allOPS,erloesData]=useMemo")
    j = app.index("return [o,null];},[", i)
    zs = app[i:j].split("\n")
    starts = [n for n, z in enumerate(zs) if "return [o,{" in z]
    out = []
    for a, b in zip(starts, starts[1:] + [len(zs)]):
        m = re.search(r"label:([^,]+)", zs[a])
        # Ein paar Zeilen Vorlauf: Werte wie luxDrg oder fxLabel werden vor dem
        # return gesetzt und gehoeren zur Anzeige des Zweigs.
        out.append(((m.group(1) if m else ""), "\n".join(zs[max(0, a - 8):b])))
    return out


def block_fuer(zweige, anker):
    # Seit Schritt 6b gibt es keine Literal-Zweige mehr: Spalte A entfaellt,
    # die Liste vergleicht dann nur noch B gegen C.
    if anker is None or not zweige:
        return ""
    for label, block in zweige:
        if anker in label:
            return block
    for label, block in zweige:
        if anker in block:
            return block
    return ""


def ziel_uebersicht(zweige, st):
    """Punkt 10: Traegt das Feld ziel des Zweigs etwas, was nicht in hinweise steht?"""
    gesehen, zeilen = set(), []
    for fall in FAELLE:
        anker = fall["zweig"]
        if anker in gesehen:
            continue
        gesehen.add(anker)
        block = block_fuer(zweige, anker)
        m = re.search(r'ziel:(.{0,400})', block, re.S)
        ziel = (m.group(1).split("\n")[0].strip() if m else "")
        hinweise = []
        for k in fall["keys"]:
            hinweise += [h.get("typ", "?") for h in (st.get(k, {}).get("hinweise") or [])]
        zeilen.append({
            "zweig": anker or "(ohne Anker)", "stellung": fall["stellung"],
            "ziel_vorhanden": bool(ziel), "ziel_laenge": len(ziel),
            "hinweise_in_daten": len(hinweise),
            "status": ("nur im Zweig" if ziel and not hinweise else
                       "in beiden" if ziel and hinweise else
                       "nur in den Daten" if hinweise else "keins von beidem"),
        })
    return zeilen


def b_spalte(eintrag):
    if not eintrag:
        return None
    felder = ("hdrg", "drg", "empf", "opsCodes", "hdrgTrigger", "hebel", "hebelName",
              "kontext", "aufwertung", "ausschluss", "beidseitsHybridBleibt",
              "ambStatus", "implantatfrei")
    b = {f: eintrag.get(f) for f in felder if eintrag.get(f) is not None}
    mods = eintrag.get("modifikatoren")
    if mods:
        b["modifikatoren"] = [m.get("label") for m in mods]
    hin = eintrag.get("hinweise")
    if hin:
        b["hinweise"] = [(h.get("typ", "?") + ": " + str(h.get("txt"))[:40]) for h in hin]
    return b


def bewerte(fall, a, b, c, ohne_a=False):
    if ohne_a:
        if not fall["keys"]:
            return "kein Eintrag", "kein OP_STEUERUNG-Schluessel"
        if not c:
            return "kein Eintrag", "Schluessel fehlt in opsteuerung.json"
        b_h = (b or {}).get("hdrg") or "—"; b_d = (b or {}).get("drg") or "—"
        c_h = c.get("hdrg") or "—"; c_d = c.get("drg") or "—"
        if b_h == c_h and b_d == c_d:
            return "gleich", "A entfaellt (Zweige abgeloest)"
        return "toggle", "A entfaellt; C rechnet aus den Kodes"
    if fall.get("umgezogen"):
        return "gleich", "umgezogen — Anzeige kommt aus steuerAnzeige()"
    if not fall["keys"]:
        return "kein Eintrag", "kein OP_STEUERUNG-Schluessel"
    if not c:
        return "kein Eintrag", "Schluessel fehlt in opsteuerung.json"
    a_h, a_d = a.get("hdrg"), a.get("drg")
    c_h = c.get("hdrg") or "—"
    c_d = c.get("drg") or "—"
    b_h = (b or {}).get("hdrg") or "—"
    b_d = (b or {}).get("drg") or "—"
    gleich_ac = (a_h == c_h) and (a_d == c_d or a_d in (None, "variabel"))
    gleich_bc = (b_h == c_h) and (b_d == c_d)
    if gleich_ac and gleich_bc:
        return "gleich", ""
    if gleich_ac and not gleich_bc:
        return "toggle", "A = C; B traegt den statischen Grundwert"
    if not gleich_ac and gleich_bc:
        return "abweichend", "A weicht von B und C ab"
    return "abweichend", "A, B und C unterscheiden sich"


# ---------------------------------------------------------------- Lauf
def main():
    app = open(APP, encoding="utf-8").read()
    daten = json.load(open(DATEN, encoding="utf-8"))
    katalog = json.load(open(KATALOG, encoding="utf-8"))
    st = daten["OP_STEUERUNG"]
    # Ab Schritt 6b rechnet der OP-Bericht aus den Daten; Literal-Zweige und
    # damit Spalte A gibt es dann nicht mehr.
    zweige = [] if "FALLSTEUERUNG AUS DEN DATEN" in app else memo_zweige(app)

    c_roh, runtime = rechne_c(app, daten, katalog, FAELLE, SOLL)

    zeilen, zaehlung = [], {"gleich": 0, "toggle": 0, "abweichend": 0, "kein Eintrag": 0}
    warnungen = []
    for nr, (fall, c_zeile) in enumerate(zip(FAELLE, c_roh["faelle"]), start=1):
        block = block_fuer(zweige, fall["zweig"])
        if zweige and fall["zweig"] and not block:
            warnungen.append(f"Zeile {nr}: Zweig-Anker {fall['zweig']!r} nicht gefunden")
        a = {"hdrg": fall.get("a_hdrg"), "drg": fall.get("a_drg"),
             "im_zweig_belegt": bool(block) and all(
                 (w in block) for w in [fall.get("a_drg")] if w and w not in ("—", "variabel"))}
        if zweige and block and fall.get("a_drg") and not a["im_zweig_belegt"]:
            warnungen.append(f"Zeile {nr}: '{fall['a_drg']}' steht nicht im Zweigtext — Wert pruefen")
        key = fall["keys"][0] if fall["keys"] else None
        b = b_spalte(st.get(key)) if key else None
        c = c_zeile["keys"].get(key) if key else None
        note, grund = bewerte(fall, a, b, c, ohne_a=not zweige)
        zaehlung[note] += 1
        zeilen.append({
            "nr": nr, "zweig": fall["zweig"], "stellung": fall["stellung"],
            "keys": fall["keys"], "codes": fall["codes"],
            "alter": fall.get("alter"), "seite": fall.get("seite"),
            "A": a, "B": b, "C": c, "bewertung": note, "grund": grund,
            "betrifft": fall.get("betrifft", []), "anmerkung": fall.get("anmerkung", ""),
            "entscheidung": "",
        })

    # Faelle, die der Autor bewusst nicht abbildet, behalten ihren Status aus
    # hybrid_testfaelle.json und zaehlen als eigene Kategorie.
    bewusst = {}
    tf_pfad = os.path.join(REPO, "hybrid_testfaelle.json")
    if os.path.exists(tf_pfad):
        try:
            for f in json.load(open(tf_pfad, encoding="utf-8")).get("faelle", []):
                if f.get("status") == "bewusst nicht abgebildet":
                    bewusst[f["nr"]] = f.get("hinweis", "")
        except Exception:
            pass

    testfaelle = []
    for s, c in zip(SOLL, c_roh["soll"]):
        ist = {"hdrg": (c or {}).get("hdrg"), "drg": (c or {}).get("drg")}
        if s["nr"] in bewusst:
            status = "bewusst nicht abgebildet"
        elif s.get("hinweis", "").startswith("5-808.b7") or "kommt in keiner Kodeliste" in s.get("hinweis", ""):
            status = "kein App-Fall"
        elif not c:
            status = "kein App-Fall"
        elif (s["soll"].get("hdrg") or None) == (ist["hdrg"] or None) and \
             (s["soll"].get("drg") is None or s["soll"]["drg"] == ist["drg"]):
            status = "gleich"
        else:
            status = "abweichend"
        testfaelle.append({
            "nr": s["nr"], "konstellation": s["konstellation"], "codes": s["codes"],
            "alter": s.get("alter"), "seite": s.get("seite"),
            "sperre": (c or {}).get("sperre"), "partner": (c or {}).get("partner"),
            "soll": s["soll"], "ist": ist, "quelle": s["quelle"],
            "status": status,
            "hinweis": bewusst.get(s["nr"]) or s.get("hinweis", ""),
            "beidseits": (c or {}).get("beidseits", ""),
        })

    zielzeilen = ziel_uebersicht(zweige, st)

    os.makedirs(OUT, exist_ok=True)
    pruef = hashlib.sha256(open(APP, "rb").read()).hexdigest()
    ergebnis = {"stand": {"app_html_sha256": pruef, "runtime": runtime,
                          "zweige_im_memo": len(zweige), "zeilen": len(zeilen)},
                "zaehlung": zaehlung, "warnungen": warnungen, "zeilen": zeilen,
                "ziel_feld": zielzeilen}
    json.dump(ergebnis, open(os.path.join(OUT, "abgleich_6a.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump({"_kommentar": [
        "Entwurf 23.09.2026 (Schritt 6a). Sollwerte aus hybrid-systematik.md Abschnitt 5,",
        "Ist-Werte aus hdrgAuswertung() mit den genannten Kodes. Alter und Seite wirken",
        "in der Auswertung noch nicht; 'kein App-Fall' = der Sollwert braucht einen Kode,",
        "den keine Kodeliste der App erzeugt."],
        "faelle": testfaelle},
        open(os.path.join(REPO, "hybrid_testfaelle.json"), "w", encoding="utf-8"),
        ensure_ascii=False, indent=1)
    schreibe_md(ergebnis, testfaelle)
    nur_zweig = sum(1 for z in zielzeilen if z["status"] == "nur im Zweig")

    print(f"Spalte C gerechnet mit: {runtime}")
    print(f"Zweige im Memo: {len(zweige)} · Zeilen: {len(zeilen)}")
    for k, v in zaehlung.items():
        print(f"  {k:12s} {v}")
    soll_z = {}
    for t in testfaelle:
        soll_z[t["status"]] = soll_z.get(t["status"], 0) + 1
    print("Sollwerte:", ", ".join(f"{k} {v}" for k, v in soll_z.items()))
    print(f"Feld ziel: {nur_zweig} von {len(zielzeilen)} Zweigen tragen Text, "
          "der in den Daten keine Entsprechung hat")
    for w in warnungen:
        print("  ⚠", w)


def schreibe_md(ergebnis, testfaelle):
    z = ergebnis["zaehlung"]
    L = []
    L.append("# Abgleich der OP-Bericht-Zweige gegen OP_STEUERUNG und Regelsatz (Schritt 6a)")
    L.append("")
    L.append(f"Erzeugt von `scripts/verify_zweige_6a.py` (Spalte C gerechnet mit "
             f"{ergebnis['stand']['runtime']}), app.html sha256 "
             f"{ergebnis['stand']['app_html_sha256'][:12]}…, "
             f"{ergebnis['stand']['zweige_im_memo']} Zweige im Memo, "
             f"{ergebnis['stand']['zeilen']} Zeilen. Nur Befund, keine Bewertung "
             "„richtig/falsch\"; die Spalte Entscheidung ist leer und gehört dem Autor "
             "(A, B, C oder ein neuer Wert).")
    L.append("")
    L.append("**Spalten.** A = was der Zweig heute anzeigt. B = der Eintrag in "
             "`opsteuerung.json`. C = was `hdrgAuswertung()` aus denselben Kodes macht "
             "(H-DRG / stationäre DRG / ambulanter Weg). betrifft = Ergänzungen a–f aus "
             "dem Umsetzungsplan.")
    L.append("")
    L.append("| Nr | Zweig · Schalterstellung | Schlüssel | Kodes | A (hdrg/drg) | "
             "B (hdrg/drg) | C (hdrg/drg/ambulant) | Bewertung | betrifft | Anmerkung | Entscheidung |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in ergebnis["zeilen"]:
        a = f"{r['A'].get('hdrg') or '—'} / {r['A'].get('drg') or '—'}"
        b = (f"{(r['B'] or {}).get('hdrg') or '—'} / {(r['B'] or {}).get('drg') or '—'}"
             if r["B"] else "—")
        if r["C"]:
            c = (f"{r['C'].get('hdrg') or '—'} / {r['C'].get('drg') or '—'} / "
                 f"{(r['C'].get('setting') or {}).get('ambulant') or '—'}")
        else:
            c = "—"
        L.append("| {nr} | {st} | {keys} | {codes} | {a} | {b} | {c} | {bew} | {betr} | {anm} | |".format(
            nr=r["nr"], st=(r["stellung"]), keys=", ".join(r["keys"]) or "—",
            codes=" ".join(r["codes"]), a=a, b=b, c=c,
            bew=r["bewertung"] + (f" ({r['grund']})" if r["grund"] else ""),
            betr=", ".join(r["betrifft"]) or "—", anm=r["anmerkung"].replace("|", "/")))
    L.append("")
    L.append(f"**Zählung.** gleich {z['gleich']} · toggle {z['toggle']} · "
             f"abweichend {z['abweichend']} · kein Eintrag {z['kein Eintrag']}.")
    L.append("")
    L.append("## Sollwerte aus hybrid-systematik.md Abschnitt 5")
    L.append("")
    L.append("| Nr | Konstellation | Kodes | Soll | Ist | Status | Quelle |")
    L.append("|---|---|---|---|---|---|---|")
    for t in testfaelle:
        soll = f"{t['soll'].get('hdrg') or '—'} / {t['soll'].get('drg') or '—'}"
        ist = f"{t['ist'].get('hdrg') or '—'} / {t['ist'].get('drg') or '—'}"
        L.append(f"| {t['nr']} | {t['konstellation']} | {' '.join(t['codes'])} | {soll} | "
                 f"{ist} | {t['status']} | {t['quelle']} |")
    L.append("")
    L.append("## Feld `ziel` je Zweig (Punkt 10: geht beim Umzug etwas verloren?)")
    L.append("")
    L.append("| Zweig | erste Schalterstellung | `ziel` im Zweig | `hinweise` in den Daten | Status |")
    L.append("|---|---|---|---|---|")
    for zz in ergebnis.get("ziel_feld", []):
        L.append(f"| {zz['zweig']} | {zz['stellung']} | "
                 f"{'ja (' + str(zz['ziel_laenge']) + ' Zeichen)' if zz['ziel_vorhanden'] else 'nein'} | "
                 f"{zz['hinweise_in_daten']} | {zz['status']} |")
    if ergebnis["warnungen"]:
        L.append("")
        L.append("## Warnungen des Skripts")
        L.append("")
        for w in ergebnis["warnungen"]:
            L.append(f"- {w}")
    L.append("")
    open(os.path.join(REPO, "abgleich-zweige-6a.md"), "w", encoding="utf-8").write("\n".join(L))


if __name__ == "__main__":
    main()
