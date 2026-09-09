# Abgleich: Literal-Zweige im Fuß-Erlösmemo gegen `OP_STEUERUNG`

Stand 09.09.2026 · erzeugt von `scripts/verify_zweige.py` (Aufruf: `python3 scripts/verify_zweige.py`)

Vorbereitung für die Entscheidung, ob die restlichen Zweige des Fuß-Erlösmemos
(`app.html`, Block `const [allOPS,erloesData]`) ebenfalls nach `OP_STEUERUNG`
umziehen. **Diese Datei ändert nichts** — sie ist Bestandsaufnahme.

Der Umzug der drei Zweige Metallentfernung, Achillessehne und diabetischer Fuß
ist erledigt; Teil 1 des Skripts belegt, dass dabei kein Wert unbeabsichtigt
gekippt ist.

## Wie zu lesen

Verglichen wird der DRG-Code, den der Zweig anzeigt, mit `drg` im zugehörigen
Steuerungseintrag. `abweichend` heißt **nicht** `falsch`: viele Zweige zeigen je
nach Toggle mehrere DRG (mit/ohne Spongiosa, ambulant/stationär), der
Steuerungseintrag nennt nur den Regelfall. Genau diese Fälle sind beim Umzug die
Arbeit — sie brauchen entweder Modifikatoren im Steuerungseintrag oder bleiben
als Literal stehen.

Die Zuordnung Zweig → Schlüssel steht als Tabelle `ZUORDNUNG` im Skript und ist
dort nachprüfbar.

## Ergebnis

### Übersicht

```

  Lapidus                                Zweig I20D             opsteuerung I20D             gleich
  MTP-I-Arthrodese + ≥3 DMMO             Zweig I20D             opsteuerung I20E             abweichend
                                           nur im Zweig: ['I20D']   nur in opsteuerung: ['I20E']
  MTP-I-Arthrodese + DMMO                Zweig I20E,I20N        opsteuerung I20E             abweichend
                                           nur im Zweig: ['I20N']   nur in opsteuerung: —
  MTP-I-Arthrodese                       Zweig I20E,I20N        opsteuerung I20E             abweichend
                                           nur im Zweig: ['I20N']   nur in opsteuerung: —
  lbl+(mitAkin?" + Akin":"")+(dmmo.length> Zweig I20E,I20F,I20O   opsteuerung I20E             abweichend
                                           nur im Zweig: ['I20F', 'I20O']   nur in opsteuerung: —
  Kleinzehen/DMMO                        Zweig I20F,I20O        opsteuerung I20F             abweichend
                                           nur im Zweig: ['I20O']   nur in opsteuerung: —
  (weil.length&&!dmmo.length?"Weil":dmmo.l Zweig I20F             opsteuerung I20F             gleich
  OSG-TEP primär (                       Zweig I05B             opsteuerung I05B             gleich
  OSG-TEP Wechsel (                      kein Steuerungseintrag
  Arthrodesenagel (TTC-Arthrodese)       Zweig I20A             opsteuerung I20A             gleich
  OSG-Arthrodese                         Zweig I13D,I13E        opsteuerung I13D             abweichend
                                           nur im Zweig: ['I13E']   nur in opsteuerung: —
  amicIKO?"AMIC + Innenknöchelosteotomie": Zweig I13E,I13G        opsteuerung I13G             abweichend
                                           nur im Zweig: ['I13E']   nur in opsteuerung: —
  Brostrom-Gould                         Zweig I59Z             opsteuerung I59Z             gleich
  Arthrorise                             Zweig —                opsteuerung —                gleich
  Achillessehnennaht (offen)             Zweig I27E             opsteuerung I27E             gleich
  FHL-Transfer                           Zweig I27D             opsteuerung I27D             gleich
  rfLabel                                Zweig I20B             opsteuerung I13E,I20B        abweichend
                                           nur im Zweig: —   nur in opsteuerung: ['I13E']
  Calcaneus-OT                           Zweig I20C             opsteuerung I20C             gleich
  Calcaneoplastie                        Zweig I20F,I20O        opsteuerung I20F             abweichend
                                           nur im Zweig: ['I20O']   nur in opsteuerung: —
  Haglund + AS-Split/Refix               Zweig I27D             opsteuerung I27D             gleich
  Os Tib Ext                             Zweig I20C,I59Z        opsteuerung I59Z             abweichend
                                           nur im Zweig: ['I20C']   nur in opsteuerung: —
  Peronealsehnenluxation                 Zweig —                opsteuerung I13G             im Zweig kein DRG-Literal
  Peronealsehnen                         Zweig I27E             opsteuerung I27E             gleich
  Coalitio                               Zweig I20C,I27D        opsteuerung I27D             abweichend
                                           nur im Zweig: ['I20C']   nur in opsteuerung: —
  Cotton-Osteotomie                      Zweig I20C             opsteuerung I20C             gleich
  TMT-Arthrodese 1–3                     Zweig I20C             opsteuerung I20C             gleich
  TMT-Arthrodese                         Zweig I20D             opsteuerung I20D             gleich
  Supramalleolare OT                     Zweig I13E             opsteuerung I13E             gleich
  fxLabel+" + Syndesmose"                kein Steuerungseintrag
  fxLabel                                kein Steuerungseintrag
  Dwyer-Osteotomie                       Zweig I20C             opsteuerung I20C             gleich
  Metallentfernung (generisch)           bereits umgezogen (metallentfernung)
  Diabetischer Fuß —                     bereits umgezogen (df_debridement, df_amputation)
                                         bereits umgezogen (as_tendoskopie, as_debridement)

  28 Zweige doppelt gepflegt · 3 umgezogen · 3 ohne Steuerungseintrag
```

## Was auffällt

**Drei Zweige haben gar keinen Steuerungseintrag** — OSG-TEP Wechsel und die
beiden Sprunggelenksfraktur-Zweige (Weber B einfach / Weber B–C Mehrfragment,
je mit und ohne Syndesmose). Sie können nur umziehen, wenn dafür Einträge
angelegt werden.

**Ein echter Wertunterschied**, kein Toggle-Effekt: Der Zweig
„MTP-I-Arthrodese + ≥3 DMMO" zeigt **I20D**, `opsteuerung.mtp1_arthrodese`
führt **I20E**. Der Zweig begründet das selbst („≥3 DMMO → keine H-DRG.
Stationär ≥2 Nächte → I20D"), der Steuerungseintrag kennt diese Fallzahl-Regel
nicht. Vor einem Umzug ist zu entscheiden, ob das als Modifikator abgebildet
wird.

**Die übrigen `abweichend`-Zeilen sind Toggle-Fälle** und je ein zusätzlicher
Code neben dem Regelfall:

| Zweig | zusätzlich im Zweig | Grund |
|---|---|---|
| MTP-I-Arthrodese (mit/ohne DMMO) | I20N | ambulante H-DRG |
| Chevron/Scarf/Akin | I20F, I20O | Cheilektomie-Variante, H-DRG |
| Kleinzehen/DMMO, Calcaneoplastie | I20O | H-DRG |
| OSG-Arthrodese | I13E | ohne Spongiosa |
| AMIC | I13E | mit Innenknöchelosteotomie |
| Os Tib Ext | I20C | mit MDO |
| Coalitio | I20C | mit LCOT |
| Rückfuß-Arthrodesen (`rfLabel`) | – (I13E fehlt im Zweig) | Zweig zeigt nur die Triple-DRG |
| Peronealsehnenluxation | – | DRG wird zur Laufzeit aus `luxDrg` gebildet |

## Nächster Schritt

Offen und separat zu entscheiden: ob die 28 doppelt gepflegten Zweige umziehen,
und in welcher Form die Toggle-Fälle in `OP_STEUERUNG` abgebildet werden
(Modifikatoren wie bei `peroneal_lux`, oder Zweig bleibt Literal).
