# Auftrag Clinic: Hinweiszeile für Klammerwerte, kürzerer Kontextprozedur-Satz

Stand 20.09.2026, Cowork-Sitzung. Zwei Punkte aus der Handy-Abnahme des Autors 20.09.2026: (1) Entscheidung „A": Werte in eckigen Klammern bleiben als Markierung „im Brief ersetzen", der Untersuchungsblock sagt das dazu; (2) der rote Satz zur Kontextprozedur in der Ambulant-Box ist zu umständlich, Wortlaut vom Autor vorgegeben. Datei `app.html`, Ausgangsstand Commit 52d9383 (802.359 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## 1. Hinweiszeile für Klammerwerte

Befund: Eckige Klammern in Befundtexten kommen heute nur beim diabetischen Fuß vor (`diagnosen.json`, 16 Werte in 8 Befunden, z. B. „Knöchel-Arm-Index [0,7]", „Ipswich Touch Test an [2] von 6 Stellen …", „Ulzeration [am Vorfuß plantar unter dem Metatarsaleköpfchen], Durchmesser ca. [2] cm"). Sie gehen wörtlich in den Brief (Z. 2573 ff., Z. 2786 ff.) und sollen dort durch den gemessenen Wert ersetzt werden; dieselbe Konvention gilt für die Sonographie-Vorschlagstexte (`sono.json`, Kommentar). Im Untersuchungsblock steht das nirgends, der Autor hat „[2]" für einen Fehler gehalten.

Änderung: Im Untersuchungsblock (Z. 3788, unter „Klicken: — → ✓ (positiv) → ✗ (negativ) → —") eine zweite Hinweiszeile im selben Stil, nur wenn mindestens ein Befund der gewählten Diagnose eine eckige Klammer enthält:

```
{availBef.some(function(b){ return /\[[^\]]+\]/.test(b.pos || ""); }) &&
  <div style={{ fontSize: 10, color: "#718096", marginBottom: 6 }}>Werte in eckigen Klammern sind Vorgaben, bitte im Brief durch den gemessenen Wert ersetzen.</div>}
```

Bei den anderen 18 Diagnosen erscheint die Zeile nicht. Brieftext, Befundtexte, `BefTog`, `befLabel` unverändert.

## 2. Kontextprozedur-Satz in der Ambulant-Box

Befund: Z. 3539 zeigt bei Eingriffen mit `best.hebel` in der Ambulant-Box in Rot: „Hybrid-DRG nur ohne Kontextprozedur: wird sie durchgeführt, wird sie kodiert, und der Fall gruppiert in die stationäre DRG." (neun der 83 Referenzfälle, z. B. Chevron-Osteotomie). Der Autor findet den Satz zu umständlich.

Änderung: Z. 3539, neuer Wortlaut genau so: „Hybrid-DRG nur, wenn keine Kontextprozedur erfolgt/kodiert wird." Schreibweise „kodiert" wie überall in der App (der Autor schrieb „codiert"; „codiert" kommt in `app.html` nicht vor). Farbe, Stelle und Bedingung unverändert. Der Satz beschreibt weiter nur die Regel (Sprachregel 14.09.: keine Anweisung zum Kodieren oder Weglassen); der Grundsatz „Kodiert wird, was durchgeführt wird" bleibt an seinen Stellen im OP-Bericht (Z. 6563, 6956).

## Nichts anderes

Keine weiteren Änderungen.

## Abnahme

Cowork-Prüfstand: diabetischer Fuß, ③ Klinische Untersuchung zeigt die Zeile; Hallux valgus, OSG-Arthrose, Peronealsehnen nicht. Referenz `baseline_sb_3v.json`: Briefe zeichengleich, Fallsteuerung gleich bis auf den neuen Satz in genau den neun Fällen mit `hebel`. Keine Konsolenfehler.

Abnahme des Autors am Handy: Diabetischer Fuß → ③ Klinische Untersuchung: unter „Klicken: …" steht der Hinweis zu den Klammerwerten; bei Hallux valgus nicht. Hallux valgus → Chevron → Erlössimulation, Ambulant-Box: „Hybrid-DRG nur, wenn keine Kontextprozedur erfolgt/kodiert wird."

Vollzugsmeldung bitte mit Commit-Hash und den zwei Zeilennummern.
