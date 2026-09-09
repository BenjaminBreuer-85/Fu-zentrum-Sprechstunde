#!/usr/bin/env python3
"""Prüfskript zum Umzug der OP-Bericht-Zweige nach OP_STEUERUNG.

Teil 1  Wertevergleich der drei umgezogenen Zweige (Metallentfernung,
        Achillessehne, diabetischer Fuß) gegen die Fassung vor dem Umzug.
        Jede Abweichung wird einzeln gemeldet; erwartete Abweichungen stehen
        in ERWARTET und werden als solche ausgewiesen.

Teil 2  Vergleichsliste der übrigen Literal-Zweige im Fuß-Erlösmemo gegen
        ihren Eintrag in opsteuerung.json (Doppelpflege). Verglichen wird der
        DRG-Code, den der Zweig anzeigt, mit `drg` im Steuerungseintrag.
        Nur Bestandsaufnahme — es wird nichts geändert.

Aufruf:  python3 scripts/verify_zweige.py [<git-ref>]     (Default: HEAD)
"""
import json, os, re, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF  = sys.argv[1] if len(sys.argv) > 1 else "HEAD"

# Bewusst herbeigeführte Abweichungen: (Zweig, Feld) -> Begründung
ERWARTET = {
    ("Achillessehne", "drg"):
        "Zielsetzung des Umzugs: statt '—' jetzt I27E aus opsteuerung.as_tendoskopie; "
        "die TODO-Zeile im Memo entfällt damit.",
    ("Diabetischer Fuß (Debridement)", "drg"):
        "Zielsetzung des Umzugs: statt '—' jetzt F27B aus opsteuerung.df_debridement.",
    ("Diabetischer Fuß (Amputation)", "drg"):
        "Zielsetzung des Umzugs: statt '—' jetzt F13B aus opsteuerung.df_amputation; "
        "bei gleichzeitiger Auswahl beider Chips gewinnt die Amputation (höherwertige DRG).",
}

# Zweig-Nr. (Reihenfolge im Memo) -> (Label-Anker, [OP_STEUERUNG-Schlüssel])
# Leere Schlüsselliste = kein Steuerungseintrag vorhanden, keine Doppelpflege.
ZUORDNUNG = [
    ('"Lapidus"',                          ["lapidus"]),
    ('"MTP-I-Arthrodese + ≥3 DMMO"',       ["mtp1_arthrodese"]),
    ('"MTP-I-Arthrodese + DMMO"',          ["mtp1_arthrodese"]),
    ('"MTP-I-Arthrodese"',                 ["mtp1_arthrodese"]),
    ('lbl+(mitAkin',                       ["chevron", "chevron_akin", "scarf", "youngswick"]),
    ('"Kleinzehen/DMMO"',                  ["dmmo", "weil", "kleinzehen_pip"]),
    ('(weil.length&&!dmmo.length',         ["dmmo", "weil"]),
    ('"OSG-TEP primär ("',                 ["tep_infinity", "tep_vantage", "tep_inbone"]),
    ('"OSG-TEP Wechsel ("',                []),
    ('"Arthrodesenagel (TTC-Arthrodese)"', ["arthrodesenagel_retro"]),
    ('"OSG-Arthrodese"',                   ["arthrodese_osg"]),
    ('amicIKO?',                           ["amic"]),
    ('"Brostrom-Gould"',                   ["brostrom_gould", "brostrom_int_brace"]),
    ('"Arthrorise"',                       ["arthrorise"]),
    ('"Achillessehnennaht (offen)"',       ["as_naht"]),
    ('"FHL-Transfer"',                     ["fhl_transfer"]),
    ('rfLabel',                            ["subtalar_arthrodese", "tn_arthrodese",
                                            "double_arthrodese", "triple_arthrodese"]),
    ('"Calcaneus-OT"',                     ["mdo_offen", "mdo_mini"]),
    ('"Calcaneoplastie"',                  ["haglund_mini"]),
    ('"Haglund + AS-Split/Refix"',         ["haglund_as_split"]),
    ('"Os Tib Ext"',                       ["os_tib_ext"]),
    ('"Peronealsehnenluxation"',           ["peroneal_lux"]),
    ('"Peronealsehnen "',                  ["peroneal_naht", "peroneal_rek"]),
    ('"Coalitio "',                        ["coalition_cn", "coalition_tc"]),
    ('"Cotton-Osteotomie"',                ["cotton"]),
    ('"TMT-Arthrodese 1–3"',               ["arthrodese_tmt13"]),
    ('"TMT-Arthrodese"',                   ["arthrodese_tmt1", "arthrodese_tmt"]),
    ('"Supramalleolare OT"',               ["supramal_valgus", "supramal_varus"]),
    ('fxLabel+" + Syndesmose"',            []),
    ('fxLabel',                            []),
    ('"Dwyer-Osteotomie"',                 ["hohlfuss_dwyer"]),
    ('"Metallentfernung (generisch)"',     ["metallentfernung"]),          # umgezogen
    ('"Diabetischer Fuß — "',              ["df_debridement", "df_amputation"]),  # umgezogen
    (None,                                 ["as_tendoskopie", "as_debridement"]), # umgezogen
]
UMGEZOGEN = {"metallentfernung", "df_debridement", "df_amputation",
             "as_tendoskopie", "as_debridement"}


def datei(ref, pfad):
    return subprocess.check_output(["git", "-C", REPO, "show", f"{ref}:{pfad}"], text=True)

def memo_zweige(quelle):
    """Alle Literal-Zweige des Fuß-Erlösmemos als (Anker, Block) in Reihenfolge."""
    i = quelle.index("const [allOPS,erloesData]")
    j = quelle.index("  // Text version for Word export", i)
    zs = quelle[i:j].split("\n")
    starts = [n for n, z in enumerate(zs) if "return [o,{" in z]
    out = []
    for a, b in zip(starts, starts[1:] + [len(zs)]):
        m = re.search(r"label:([^,]+)", zs[a])
        out.append((m.group(1) if m else None, "\n".join(zs[a:b])))
    return out

def feld(block, name):
    m = re.search(rf'\b{name}:"((?:[^"\\]|\\.)*)"', block)
    return m.group(1) if m else None

def drg_codes(block):
    """DRG-Codes, die der Zweig in seinen Anzeigefeldern nennt."""
    txt = "\n".join(filter(None, (feld(block, "drg"), feld(block, "kurz"))))
    txt += " " + " ".join(re.findall(r'drg:([^\n]*)', block))
    return sorted(set(re.findall(r"\b([A-Z]\d{2}[A-Z])\b", txt)))


alt = datei(REF, "app.html")
neu = open(os.path.join(REPO, "app.html"), encoding="utf-8").read()
st  = json.load(open(os.path.join(REPO, "data/opsteuerung.json"), encoding="utf-8"))["OP_STEUERUNG"]

# ---------------------------------------------------------------- Teil 1
print("Teil 1 — Wertevergleich der umgezogenen Zweige (Basis: %s)\n" % REF)
FAELLE = [
    ("Metallentfernung", "metallentfernung",
     'if(hasME) return [o,{label:"Metallentfernung', '// Diabetischer Fuß: Die OPS-Zuordnung'),
    ("Achillessehne", "as_tendoskopie",
     'if(rfOp.includes("as_tendoskopie")||rfOp.includes("as_debridement"))', 'return [o,null];'),
    ("Diabetischer Fuß (Debridement)", "df_debridement",
     'label:"Diabetischer Fuß — "', '// OPS-Ziffern fuer Tendoskopie'),
    ("Diabetischer Fuß (Amputation)", "df_amputation",
     'label:"Diabetischer Fuß — "', '// OPS-Ziffern fuer Tendoskopie'),
]
offen = 0
for name, key, marke, ende in FAELLE:
    try:
        i = alt.index(marke); block = alt[i:alt.index(ende, i)]
    except ValueError:
        print(f"  {name}: Zweig in {REF} nicht auffindbar — Anker prüfen"); offen += 1; continue
    e = st.get(key)
    if not e:
        print(f"  {name}: ABWEICHUNG — '{key}' fehlt in opsteuerung.json"); offen += 1; continue
    for f in ("hdrg", "drg", "empf"):
        vorher = feld(block, f)
        if vorher is None:
            continue
        nachher = e.get(f)
        nachher = nachher if nachher is not None else "—"
        if vorher == nachher:
            print(f"  {name}.{f}: {vorher!r} unverändert")
        elif (name, f) in ERWARTET:
            print(f"  {name}.{f}: {vorher!r} → {nachher!r}  (erwartet: {ERWARTET[(name, f)]})")
        else:
            print(f"  {name}.{f}: ABWEICHUNG {vorher!r} → {nachher!r}"); offen += 1
print("\n  Ergebnis:", "keine ungeklärte Abweichung" if not offen else f"{offen} ungeklärt")

# ---------------------------------------------------------------- Teil 2
zweige = memo_zweige(neu)
print(f"\n\nTeil 2 — Doppelpflege: {len(zweige)} Literal-Zweige im Fuß-Erlösmemo\n")
if len(zweige) != len(ZUORDNUNG):
    print(f"  ⚠ Zuordnungstabelle passt nicht ({len(ZUORDNUNG)} Einträge) — Tabelle nachziehen.\n")

doppelt = ohne = migriert = 0
for (anker, block), (erwartet_anker, keys) in zip(zweige, ZUORDNUNG):
    if erwartet_anker and anker and erwartet_anker not in anker:
        print(f"  ⚠ Anker verschoben: erwartet {erwartet_anker!r}, gefunden {anker!r}")
    label = feld(block, "label") or (anker or "")[:40]
    codes = drg_codes(block)
    if not keys:
        print(f"  {label:38s} kein Steuerungseintrag"); ohne += 1; continue
    if set(keys) & UMGEZOGEN:
        print(f"  {label:38s} bereits umgezogen ({', '.join(keys)})"); migriert += 1; continue
    doppelt += 1
    st_codes = sorted({st[k].get("drg") for k in keys if st.get(k) and st[k].get("drg")})
    fehlt = [k for k in keys if k not in st]
    status = ("Schlüssel fehlt: " + ", ".join(fehlt)) if fehlt else \
             ("gleich" if set(codes) == set(st_codes) else
              "abweichend" if codes and st_codes else "im Zweig kein DRG-Literal")
    print(f"  {label:38s} Zweig {','.join(codes) or '—':16s} "
          f"opsteuerung {','.join(st_codes) or '—':16s} {status}")
    if status == "abweichend":
        print(f"  {'':38s}   nur im Zweig: {sorted(set(codes)-set(st_codes)) or '—'}   "
              f"nur in opsteuerung: {sorted(set(st_codes)-set(codes)) or '—'}")

print(f"\n  {doppelt} Zweige doppelt gepflegt · {migriert} umgezogen · {ohne} ohne Steuerungseintrag")
print("\n  Hinweis: 'abweichend' heißt nicht 'falsch'. Viele Zweige zeigen je nach Toggle")
print("  mehrere DRG (z. B. mit/ohne Spongiosa), der Steuerungseintrag nennt nur eine.")
print("  Die Liste ist Entscheidungsgrundlage, keine Fehlerliste.")
