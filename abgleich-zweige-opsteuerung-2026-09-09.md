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
Steuerungseintrag. `abweichend` heißt **nicht** `falsch`: Viele Zweige zeigen je
nach Toggle mehrere DRG (mit oder ohne Spongiosa, ambulant oder stationär, mit
oder ohne LCOT). Das sind genau die Fälle, die die Auswertung aus den Regeln
erzeugt — sie brauchen keine Entscheidung (Autor, 09.09.2026).

Die Zuordnung Zweig → Schlüssel steht als Tabelle `ZUORDNUNG` im Skript und ist
dort nachprüfbar.

## Ergebnis

### Übersicht

```

  Lapidus                                Zweig I20D             opsteuerung I20D             gleich
  MTP-I-Arthrodese + ≥3 DMMO             Zweig I20D             opsteuerung I20E             abweichend
                                           nur im Zweig: ['I20D']   nur in opsteuerung: ['I20E']
                                           erklärt: Kein Widerspruch (Autor 09.09.): mtp1_arthrodese.drg = I20E ist die Ziel-DRG über den Hebel Spongiosa (5-784.0v). Mit 5-788.54 greift die Kontextregel HDRG_REGELN.I20O_N mit drg {I20O: I20E, I20N: I20D} — also aus I20N heraus nach I20D, ohne Spongiosa. Der Zweig hatte das fest kodiert, die Auswertung liefert es aus den Regeln. Daten bleiben unverändert.
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

## Was noch offen ist

**Drei Zweige haben keinen Steuerungseintrag** — OSG-TEP Wechsel und die beiden
Sprunggelenksfraktur-Zweige (Weber B einfach / Weber B–C Mehrfragment, je mit
und ohne Syndesmose). Sie bleiben vorerst im Code; der Autor legt die Einträge
im Rahmen des 28-Zweige-Auftrags an, nachdem er die Werte freigegeben hat
(Entscheidung 09.09.2026).

Alles Übrige ist geklärt. Die Zeile „MTP-I-Arthrodese + ≥3 DMMO" (Zweig I20D
gegen `mtp1_arthrodese.drg` I20E) war zunächst als möglicher Wertunterschied
notiert; der Autor hat am 09.09.2026 klargestellt, dass beides richtig ist und
sich nichts an den Daten ändert. Die Begründung steht im Skript unter
`ERLAEUTERT` und wird bei jedem Lauf mit ausgegeben.

## Nächster Schritt

Offen und separat zu entscheiden: ob die 28 doppelt gepflegten Zweige umziehen.
Bei der Umstellung ersetzt die Auswertung aus `HDRG_REGELN` die fest kodierten
Werte — die Toggle-Fälle lösen sich damit von selbst auf.
