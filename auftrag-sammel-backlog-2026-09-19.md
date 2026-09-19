# Sammel-Auftrag 19.09.2026: vier kleine Punkte aus dem Backlog

Stand 19.09.2026, Cowork-Sitzung, Freigabe des Autors („Backlog-Sammelauftrag"). Ausgangsstand `app.html`: Commit 7472ebe (800.530 Byte), Zeilenangaben beziehen sich darauf. Ein Commit, eine Vollzugsmeldung. Datenteil 3u (`data/opmethoden.json`, Eintrag `PATIENT_VARIANTEN.arthrodese_tmt`) schreibt die Cowork-Sitzung nach eigener Freigabe; der heutige Code liest den Eintrag nicht, die Daten können vorher oder nachher raus.

## 1. „DB II (real)" ohne Materialsatz (Backlog G2)

Befund: `implKostenFuer` (Z. 992–998) liefert `0`, wenn der Eingriff weder in `MAPPING_OPS` steht noch ein Modifikator mit `material` aktiv ist (Z. 995 `if (!m && !mitMaterial) return 0`). Die Stationär-Box nimmt `0` als echte Zahl (`implZahl`, Z. 3498), `hasRealImpl` wird wahr (Z. 3597), und der Fall zeigt „DB II (real) … 🟢 Marge besser als InEK-Median (Implantate günstiger als Referenz)", obwohl darüber „keine Materialkosten hinterlegt" steht (`dbRealText`, Z. 3599). Für implantatfreie Eingriffe ist die Rechnung richtig, für ungepflegte Materialsätze irreführend. In der Referenz (`baseline_sb_3s.json`, ohne Preisliste) betrifft das 43 der 83 OP-Fälle, alle mit „🟢 Marge besser als InEK-Median (Implantate günstiger als Referenz)" direkt über „keine Materialkosten hinterlegt", z. B. Peronealsehnen-Stabilisierung: „DB II (real): 4.539 € − 3.983,45 € − 0,00 € = +555,55 €".

Änderung: Z. 995 `return null` statt `return 0`. Folge im Bestand: `implZahl` wird `null` (Z. 3498), `implAmpel` liefert `null` (Z. 1314 `if(!soll||!ist)return null`), `implZahl>0` (Z. 3515, 3559) bleibt falsch, `hasRealImpl` wird falsch, die Box zeigt „⚪ DB II (real) nicht berechenbar — keine Materialkosten hinterlegt". `implKostenFuer` hat nur den einen Aufrufer Z. 3492. Wenn `paketPreisAusPositionen` `null` liefert (leere Positionsliste, Z. 1008), gilt dasselbe: Z. 997 `return r == null ? null : r` (oder einfach `return r`).

## 2. Befund-Label endet an einem Komma in der Klammer (Backlog G6)

Befund: `BefTog` trennt das Label eines nicht gesetzten Befunds am ersten „, " (Z. 1257, seit 7472ebe). Bei zwei Befunden steht das erste „, " innerhalb einer Klammer: Peronealsehnen „Hinweis auf laterale Instabilität (giving-way, positives laterales Aufklappen)" → Label „Hinweis auf laterale Instabilität (giving-way"; diabetischer Fuß „Ipswich Touch Test an [2] von 6 Stellen (Zehen 1, 3 und 5 beidseits) nicht wahrgenommen" → „Ipswich Touch Test an [2] von 6 Stellen (Zehen 1". Vor 7472ebe genauso. Die Brieftexte sollen unverändert bleiben, deshalb Code statt Daten.

Änderung: kleine Hilfsfunktion neben `BefTog`, die am ersten „, " außerhalb runder und eckiger Klammern trennt:

```
function befLabel(pos){
  var tiefe = 0;
  for (var i = 0; i < pos.length - 1; i++) {
    var c = pos[i];
    if (c === "(" || c === "[") tiefe++;
    else if (c === ")" || c === "]") tiefe = Math.max(0, tiefe - 1);
    else if (c === "," && pos[i+1] === " " && tiefe === 0) return pos.slice(0, i);
  }
  return pos;
}
```

Z. 1257: `b.pos ? befLabel(b.pos) : ""`. Ergebnis: „Hinweis auf laterale Instabilität (giving-way, positives laterales Aufklappen)" und „Ipswich Touch Test an [2] von 6 Stellen (Zehen 1, 3 und 5 beidseits) nicht wahrgenommen" vollständig; alle anderen Labels wie heute (die Cowork-Sitzung hat die Funktion über alle 19 Diagnosen laufen lassen: nur diese zwei ändern sich). Nur die Anzeige im Untersuchungsblock, nicht der Brieftext.

## 3. „MVWD: Tage" ohne Zahl (Backlog G7)

Befund: Beim Laden übernimmt der Code `mvwd` je Eingriff und je Modifikator nur, wenn `window._DRG[drg].mvwd` nicht null ist (Z. 1557, 1566). Für I43B ist `_DRG.I43B.mvwd` null, `GVD.I43B.mvwd` aber 8.2 (`erloes2026.json`). OSG-TEP mit „Wechseloperation" zeigt darum „MVWD: Tage · CM 2.372" (Z. 3550). Der OP-Bericht liest die MVWD bereits aus `GVD` (Z. 6424).

Änderung: (a) Z. 1557 und 1566: fällt `_DRG[drg].mvwd` aus, `GVD[drg].mvwd` nehmen, wenn vorhanden (`GVD` ist in Z. 4776 aus `window._DATA.erloes2026.GVD` gebunden; in Z. 1552 ff. bitte dieselbe Quelle `window._DATA.erloes2026.GVD` lesen). (b) Z. 3550: die Zeile „MVWD: … Tage" nur mit Zahl ausgeben; ohne Zahl nur „CM x,xxx". Keine Änderung an `erloes2026.json` (die Datei wird nicht von Hand gepflegt). Der Betrag im Hinweistext („I43B (10.819 €)") wird von `_fx` beim Laden neu gerechnet und ist kein Befund.

## 4. Patienten-Varianten je Chip statt je Ziel (Folge von 3d)

Befund: `PATIENT_VARIANTEN` ist am Ziel-Schlüssel verankert (Z. 1960 `PATIENT_VARIANTEN[aufZielKey]`, Z. 1969 ebenso). Seit 3d (19.09.2026) hat `tmt` vier Varianten; die drei Chips TMT-I-Arthrodese, TMT-II/III-Arthrodese und TMT-I-bis-III-Arthrodese zeigen deshalb alle vier, auch die TMT-II/III-Arthrodese die beiden Hallux-Varianten.

Änderung: (a) Z. 1960 und 1969: erst der Chip-Schlüssel, dann das Ziel: `PATIENT_VARIANTEN[aufActive.key] || PATIENT_VARIANTEN[aufZielKey]` (in Z. 1969 dieselbe Auflösung, am besten einmal als `aufVarianten` berechnen und in Z. 1969 `aufVarianten ? "&var=" + aufVariante : ""`). (b) Der Zustand `aufVariante` startet mit „einfach" (Z. 1898) und bleibt beim Chipwechsel stehen. Wenn `aufVarianten` wechselt und `aufVariante` darin nicht vorkommt, auf den ersten Schlüssel setzen (Effekt mit Abhängigkeit `aufVarianten`), damit nie ein `var=` ohne passenden Eintrag im Link steht. Datenteil 3u (Cowork-Sitzung): `PATIENT_VARIANTEN.arthrodese_tmt` = nur `einfach` und `komplex` (Texte wie bei `tmt`); `arthrodese_tmt1` und `arthrodese_tmt13` bekommen keinen Eintrag und fallen auf `tmt` (vier Varianten) zurück. Der Kommentar in Z. 1896 f. („Nur dort wählbar, wo die Patienten-App Varianten kennt (chevron, osg_arthrodese, osg_tep)") ist veraltet und darf mitgehen.

## 5. Nichts anderes

Keine weiteren Änderungen. Brieftexte in allen Fällen zeichengleich; Fallsteuerung ändert sich nur bei Fällen ohne Materialsatz (Punkt 1: „DB II (real)"-Zeile wird zu „nicht berechenbar") und bei I43B (Punkt 3); das Untersuchungs-Label nur bei den zwei Klammerbefunden (Punkt 2); die Varianten-Chips nur bei den TMT-Chips, sobald 3u geschrieben ist (Punkt 4).

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3s.json`, Stand 7472ebe, 19 Diagnosen, 83 OP-Fälle): Briefe zeichengleich; Fallsteuerung gleich bis auf die „DB II (real)"-Zeile bei den 43 Fällen ohne Materialsatz (die Cowork-Sitzung weist jede Abweichung je Fall aus). Gezielt: (1) ein Eingriff ohne `MAPPING_OPS` und ohne Materialmodifikator zeigt „⚪ DB II (real) nicht berechenbar — keine Materialkosten hinterlegt" und keine Ampel; Coalitio TC „+ LCOT" mit Testpreisen rechnet wie bisher (250 € → grün, DB II (real) mit Betrag). (2) Peronealsehnen und diabetischer Fuß, Klinische Untersuchung: die zwei Labels vollständig; alle übrigen Labels wie in der Referenz. (3) OSG-Arthrose → OSG-TEP Low Profile → „Wechseloperation": „MVWD: 8.2 Tage · CM 2.372". (4) Nach 3u: TMT-II/III-Arthrodese zeigt zwei Varianten, TMT-I- und TMT-I-bis-III-Arthrodese vier; Wechsel von TMT-I („Hallux-Korrektur, Teilbelastung" gewählt) auf TMT-II/III setzt die Variante auf „Teilbelastung", QR-Ziel `var=einfach`. Keine Konsolenfehler, Selbsttest unverändert.

Abnahme des Autors am Handy: OSG-TEP mit „Wechseloperation" zeigt eine MVWD-Zahl; diabetischer Fuß, Untersuchung: Zeile „Ipswich Touch Test …" vollständig; ein Eingriff ohne Preise zeigt „nicht berechenbar" statt einer grünen Marge.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern der vier Änderungen.
