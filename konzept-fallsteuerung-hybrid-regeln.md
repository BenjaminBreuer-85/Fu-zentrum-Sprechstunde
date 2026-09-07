# Konzept: Hybrid-Regeln in der Fallsteuerung, schlank und ohne Redundanz

Stand: 07.09.2026. Anlass: Abgleich mit den GFFC-Folien (siehe `abgleich-gffc-hybrid-2026.md`). Ziel: Die Erkenntnisse daraus einbauen, ohne dass die Fallsteuerung zu einer Kodeliste wird.

## 1. Befund am heutigen Datenmodell

Die Regeln liegen heute je OP-Methode in `opsteuerung.json`. Chevron, Chevron + Akin, Scarf und Youngswick tragen vier identische Kopien derselben Ausschluss- und Aufwertungslisten; DMMO und Weil eine dritte Variante davon; MTP-I-Arthrodese und Lapidus haben gar keine Ausschlussliste, obwohl dieselben Kodes dort ebenfalls wirken. Die GFFC-Folien zeigen, warum das so unhandlich ist: Die Regeln hängen nicht an der OP, sondern an der Hybrid-DRG. Es gibt für die Fußchirurgie genau drei davon (I20O, I20N, I20M), und I20O und I20N teilen sich eine Kontextprozeduren-Liste. Also gibt es in Wahrheit zwei Regelsätze, nicht 44.

Zweiter Befund: Der Ausschluss ist heute mit „keine H-DRG → nur stationär" beschriftet. Richtig ist „keine Hybrid-DRG, dann stationär I20x oder ambulant EBM". Die App kennt den ambulanten Weg bereits (Spalte „Ambulant" mit AOP-Katalogprüfung), er wird nur beim Ausschluss nicht mitgedacht.

## 2. Grundsätze

Regeln je Hybrid-DRG, nicht je OP. Jede OP-Methode sagt nur noch, in welche Hybrid-DRG sie führt und welche Vollstationär-DRG sie ohne Hybrid hat. Alles andere (was herausführt, was aufwertet, was neutral ist, was nicht im AOP-Katalog steht) steht einmal je Hybrid-DRG.

Eine Aussage pro Fall, nicht eine Liste pro OP. Die Fallsteuerung zeigt nach dem Anklicken der Kodes das Ergebnis in drei Spalten wie bisher (ambulant, Hybrid, stationär) plus genau einen Satz, der erklärt, warum der Fall dort steht, wo er steht. Kodes erscheinen in diesem Satz nur, wenn sie tatsächlich angeklickt sind.

Listen nur auf Nachfrage. Die vollständigen Kontextprozeduren-Listen bleiben hinter einem Aufklapper („Was führt aus I20O heraus?"). Wer sie braucht, hat sie mit einem Klick; wer den Fall nur steuern will, sieht sie nicht.

Ein Regelwerk für beide Generatoren. Der Sprechstundenbrief (Fallsteuerung) und der OP-Bericht (Kodierhinweise) rechnen mit demselben Regelsatz. Die Kodierhinweise im OP-Bericht werden aus der Auswertung erzeugt, nicht als eigene Texte gepflegt.

## 3. Datenmodell

Neuer Block in `opsteuerung.json`:

```json
"HDRG_REGELN": {
  "I20O_N": {
    "hdrg": ["I20O", "I20N"],
    "kontext": [
      {"code": "5-788.54", "name": "3× DMMO/Weil MT II–V", "drg": "I20E"},
      {"code": "5-788.55", "name": "4× DMMO/Weil MT II–V", "drg": "I20E"},
      {"code": "5-788.60", "name": "Arthroplastik MTP I", "drg": "I20F"},
      {"code": "5-788.59", "name": "3× Osteotomie D II–V", "drg": "I20F"},
      {"code": "5-788.62", "name": "2× Arthroplastik MTP II–V", "drg": "I20F"},
      {"code": "5-788.63", "name": "3× Arthroplastik MTP II–V", "drg": "I20E"},
      {"code": "5-784.0v", "name": "Spongiosatransplantation Metatarsale", "drg": null},
      {"code": "5-854.2c", "name": "Sehnentransfer Mittelfuß/Zehen", "drg": null}
    ],
    "aufwertung": [
      {"code": "5-788.52", "name": "1× DMMO/Weil", "hdrg": "I20N"},
      {"code": "5-788.53", "name": "2× DMMO/Weil", "hdrg": "I20N"},
      {"code": "5-808.a4", "name": "Lapidus zusätzlich", "hdrg": "I20M"}
    ],
    "neutral": ["5-788.70", "5-788.71", "5-788.57", "5-788.58", "5-808.bd", "5-788.61", "5-788.65"],
    "positiv": ["5-811.xk", "5-812.kk", "5-812.xk", "5-819.xk"]
  },
  "I20M": {
    "hdrg": ["I20M"],
    "kontext": [ "... wie oben, aber ohne 5-854.1c, 5-854.2c, 5-788.60 ..." ],
    "nichtKontext": [
      {"code": "5-854.2c", "name": "Sehnentransfer", "txt": "wirkt in I20M nicht als Kontextprozedur, Fall bleibt Hybrid"},
      {"code": "5-854.1c", "name": "Sehnenverkürzung", "txt": "wirkt in I20M nicht als Kontextprozedur"},
      {"code": "5-788.60", "name": "Arthroplastik MTP I", "txt": "ist in I20M Hybrid-Trigger, kein Ausweg"}
    ],
    "neutral": ["5-788.61", "5-788.66", "5-788.67", "5-788.68", "5-808.bd", "5-808.be", "5-808.bf", "5-808.bg", "5-788.57", "5-788.58", "5-788.52", "5-788.53"]
  }
},
"HDRG_RAHMEN": [
  "Verweildauer unter 3 Tagen",
  "Alter über 17 Jahre",
  "PCCL unter 3",
  "kein hoher Pflegegrad",
  "keine Fallzusammenlegung aus zwei Aufenthalten"
]
```

Die Kodes oben sind die aus den GFFC-Folien; die vollständigen Listen werden vor dem Einbau gegen `katalog2026.json` abgeglichen (1:1-Regel). `drg: null` bei einer Kontextprozedur heißt: Der Fall verlässt die Hybrid-DRG und gruppiert in die `drg` der OP-Methode (I20E beim Chevron, I20D beim Lapidus); ein gesetzter Wert überschreibt das (5-788.54 bei MTP-I führt nach I20D, nicht nach I20E).

Die OP-Einträge werden entsprechend entschlackt. Beispiel Chevron danach:

```json
"chevron": {
  "hdrg": "I20O", "drg": "I20E", "empf": "both",
  "hebel": "5-854.2c", "hebelName": "Sehnentransfer"
}
```

Die Blöcke `kontext`, `aufwertung`, `ausschluss` verschwinden aus den einzelnen OP-Einträgen. Bleiben dürfen OP-spezifische Dinge: `hebel` (der eine empfohlene Ausweg für genau diese OP), `modifikatoren` (TMT-Gelenkfächer), `hdrgTrigger` (Lapidus, weil dort die Hybrid-Zugehörigkeit erst durch Zusatzkodes entsteht) und Hinweise, die nur diese OP betreffen (801D-Falle, Twist-Off-Schraube).

## 4. Auswertungslogik (einmal, für beide Generatoren)

Eingabe: die Menge der angeklickten OPS-Kodes des Falls plus die gewählte Haupt-OP.

Schritt 1, Hybrid-Zugehörigkeit: Die Haupt-OP hat `hdrg`. Beim Lapidus gilt sie nur, wenn ein `hdrgTrigger` gesetzt ist; da Akin jetzt fester Bestandteil ist, gilt der Trigger als gesetzt, sobald der Lapidus-Chip gewählt ist.

Schritt 2, Ausweg: Ist einer der `kontext`-Kodes des zuständigen Regelsatzes angeklickt, verlässt der Fall die Hybrid-DRG. Ziel ist die `drg` des Kontextkodes, sonst die `drg` der OP.

Schritt 3, Aufwertung: Ist keine Kontextprozedur gesetzt, aber ein `aufwertung`-Kode, wechselt die Hybrid-DRG (I20O nach I20N, I20N nach I20M).

Schritt 4, Ambulant: Sind alle angeklickten Kodes im AOP-Katalog (Prüfung existiert bereits), ist der ambulante Weg offen. Steht der Fall in der Hybrid-DRG, wird ambulant als Hybrid vergütet; steht er außerhalb, als EBM. Ist ein `positiv`-Kode angeklickt (nicht im AOP-Katalog, aber Hybrid-Trigger), gilt: ambulant nur als Hybrid möglich, nicht als EBM.

Schritt 5, Warnungen: `nichtKontext`-Kode angeklickt und kein echter Kontextkode gesetzt (Lapidus mit 5-854.2c); `positiv`-Kode zieht einen ambulanten EBM-Fall in die Hybrid-DRG (Arthroskopie mit Osteophytenabtragung); Rahmenbedingungen nicht bestätigt.

## 5. Darstellung

Die drei Spalten bleiben. Neu ist darunter eine einzige Konsequenz-Zeile in normaler Schrift, ohne Kästen, zum Beispiel:

„3× DMMO (5-788.54) führt aus der Hybrid-DRG I20O heraus. Stationär I20E, ambulant EBM."

„Fall liegt in I20N. Ausweg für diese OP: Spongiosa MTP I (5-784.0v) nach I20E."

„Sehnentransfer 5-854.2c wirkt bei I20M nicht als Kontextprozedur, der Fall bleibt Hybrid (rot)."

Darunter ein Aufklapper, standardmäßig geschlossen: „Kontextprozeduren I20O anzeigen". Beim Öffnen die Liste in zwei Gruppen (führt heraus, wertet auf), je Zeile Kode, Kurzname, Ziel. Die neutralen Kodes werden nicht angezeigt, sie sind nur für die Logik da (damit sie keine Warnung auslösen).

Die Hebel-Zeile aus dem Kontext-Auftrag bleibt in der Stationär-Box, weil sie eine andere Frage beantwortet (wie komme ich stationär auf die höhere DRG), und bezieht sich weiterhin auf den einen `hebel` der OP.

Die Rahmenbedingungen erscheinen einmal je Fall als Zeile unter der Hybrid-Spalte („Hybrid nur bei: Verweildauer unter 3 Tagen, Alter über 17, PCCL unter 3, kein hoher Pflegegrad"), nicht als Abfrage. Wer eine Bedingung als nicht erfüllt kennt, steuert ohnehin stationär.

Was bewusst nicht angezeigt wird: EBM-Beträge (die App hat keine EBM-Daten, und die Stufen E2 bis E5 hängen von OP-Zeit und Zugang ab, das gehört in die ambulante Abrechnung, nicht in die Fallsteuerung); die vollständige Kontextprozeduren-Liste im Standardzustand; Kodes, die nicht angeklickt sind.

## 6. OP-Bericht

Die Kodierhinweise im OP-Bericht („Erlösrelevante Kodierhinweise") werden aus derselben Auswertung erzeugt: Haupt-OPS, gesetzte Kontext- oder Aufwertungskodes, ein Satz zur Setting-Konsequenz, ein Satz zur Belegungsdokumentation, wenn stationär. Damit entfallen die je OP gepflegten Hinweistexte, die heute in `hinweise[]` liegen und teilweise dieselben Kodes ein drittes Mal nennen (MTP-I: „Stationär mit Kontextprozedur + 3× DMMO").

## 7. Umsetzung in Schritten

Erstens `HDRG_REGELN` und `HDRG_RAHMEN` in `opsteuerung.json` anlegen, Kodes gegen `katalog2026.json` prüfen (dieser Schritt ist Datenarbeit, mache ich mit Freigabe des Autors).

Zweitens Auswertungsfunktion in `app.html` nach Abschnitt 4 bauen und in der Fallsteuerung die Konsequenz-Zeile plus Aufklapper rendern; die alten Blöcke `ausschluss` und `aufwertung` je OP werden ab dann ignoriert (Auftrag an die Code-Sitzung).

Drittens die OP-Einträge entschlacken und die OP-Bericht-Kodierhinweise auf die Auswertung umstellen; erst wenn Gegenprobe mit den bekannten Fällen (Chevron plus 3× DMMO, MTP-I plus 3× DMMO, Lapidus plus Akin plus 5-854.2c, USG-Arthrodese, Arthroskopie plus Osteophytenabtragung) dieselben Ergebnisse liefert wie die GFFC-Folien.

Viertens ASK OSG: eigener Regelsatz-Anteil (Positivprozeduren, Ausschlüsse) in `I20O_N` ergänzen, plus der Hinweis zum gesonderten Zugang bei Simultaneingriffen (LSG BW L4 KR 799/23) als OP-spezifischer Hinweis beim `ask_osg`-Eintrag.

## 8. Entscheidungen, die ich brauche

Ob die Konsequenz-Zeile immer sichtbar ist oder nur, wenn sich durch einen Zusatzkode etwas ändert (mein Vorschlag: immer, ein Satz stört nicht und erklärt die Ampel).

Ob die Rahmenbedingungen als Hinweiszeile reichen oder als Häkchen je Fall geführt werden sollen (mein Vorschlag: Hinweiszeile).

Ob beim Lapidus der Akin-Trigger automatisch gesetzt gilt (mein Vorschlag: ja, weil Akin jetzt Bestandteil des Chips ist; wer einmal ohne Akin operiert, nimmt den Kode im Bericht heraus, und die Steuerung folgt).
