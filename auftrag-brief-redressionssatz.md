# Auftrag Clinic: Satz zu redressierenden Verbänden im Sprechstundenbrief (Hallux- und Kleinzeheneingriffe)

Stand 08.10.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand 02dd198 (808.040 B, md5 a59bd0e9…; Zeilenangaben darauf). Daten `opmethoden.json` Stand 07.10.2026 (42.473 B, md5 9d9be91f…). Wunsch des Autors 08.10.2026: Bei allen Eingriffen, nach denen redressierende Verbände nötig sind (Hallux- und Kleinzeheneingriffe), soll im Brief dieser Satz stehen:

„Nach dem Eingriff sind für mehrere Wochen redressierende Verbände zur Sicherung des OP-Ergebnisses nötig. Hier muss eine Anbindung und regelmäßige Kontrolle durch Behandler mit fußchirurgischer Erfahrung gewährleistet sein.“

Ein Commit, Vollzugsmeldung mit Commit-Hash und Zeilennummern. Den Datenschritt (Abschnitt 1) hat die Cowork-Sitzung vorbereitet und schreibt ihn nach `data/`, sobald der Mac erreichbar ist; die Code-Sitzung sieht den Bucket nicht, kann aber gegen die lokale `data/opmethoden.json` prüfen, sobald der Datenschritt geschrieben ist.

## Befund

Der Abschlussabsatz des Briefs (Z. 3246–3265) nennt bei gewählten Eingriffen den Satz „Operativ bieten wir das o. g. Verfahren an …“ bzw. „Operativ käme … in Betracht …“ und daran den Risikosatz „Es bestehen bei operativem Vorgehen gewisse Risiken (unter anderem: …).“ Für die OSG-Prothese hängt Z. 3262–3264 bereits einen verfahrensspezifischen Hinweis an (`ops.some(o => o.indexOf("tep") >= 0)`). Einen Hinweis auf die Nachbehandlung mit redressierenden Verbänden gibt es im Brief nicht. Im OP-Bericht setzt `buildVerband` (Z. 7679) bei Vorfußeingriffen automatisch den Tape-Verband; das ist eine andere Stelle und bleibt unberührt.

## 1. Datenschritt `opmethoden.json` (Cowork-Sitzung, nach Freigabe)

Damit die Liste ohne Code-Änderung erweiterbar bleibt, bekommt jede betroffene Methode in `OPS` ein Feld `"redression": true`. Liste vom Autor am 08.10.2026 bestätigt („Auswahl ist gut“); Datenschritt vorbereitet (`opmethoden.json` 42.473 → 42.680 B, md5 9d9be91f… → ea117270…, 9 Einträge mit `"redression": true`, sonst byte-gleich):

| Schlüssel | Brief-Chip | Begründung |
|---|---|---|
| `chevron` | Chevron-Osteotomie | Hallux-valgus-Korrektur, Tape-Redression |
| `chevron_akin` | Chevron + Akin | wie Chevron |
| `scarf` | Scarf-Osteotomie | wie Chevron |
| `lapidus` | Lapidus-Arthrodese | Weichteilkorrektur und Akin im Verfahren |
| `youngswick` | Youngswick-Osteotomie | Hallux rigidus, Osteotomie MT I mit Redression |
| `kleinzehen_pip` | Kleinzehen/PIP oder Osteotomie | Kleinzehenkorrektur |
| `kleinzehen_weichteil` | Kleinzehen Weichteilkorrektur | Kleinzehenkorrektur |
| `dmmo` | DMMO (MT-Osteotomie) | minimalinvasive Osteotomie ohne Fixierung, Verband hält die Stellung |
| `weil` | Weil-Osteotomie | Vorfuß, Zehenstellung im Verband |

Nicht vorgesehen: `cheilektomie`, `exostose`, `mtp1_arthrodese`, `morton_neurom` (keine redressierende Nachbehandlung). Alle übrigen Methoden ohne Feld.

## 2. Code `app.html`: Satz im Abschlussabsatz

Nach dem Risikosatz (Z. 3261) und nach dem TEP-Hinweis (Z. 3262–3264), innerhalb von `if (ops.length > 0)`:

```
if (ops.some(function(o) { return OPS[o] && OPS[o].redression === true; })) {
  ab += " Nach dem Eingriff sind für mehrere Wochen redressierende Verbände zur Sicherung des OP-Ergebnisses nötig. Hier muss eine Anbindung und regelmäßige Kontrolle durch Behandler mit fußchirurgischer Erfahrung gewährleistet sein.";
}
```

Der Satz steht damit in beiden Fällen (OP empfohlen und „käme in Betracht“), wie der TEP-Hinweis; er beschreibt das Verfahren, nicht die Empfehlung. Bei mehreren gewählten Eingriffen steht er einmal. Ohne Feld in den Daten (alter Datenstand) ändert sich nichts. Metallentfernungs-Brief (Z. 2846) unverändert.

Selbsttest: keine neue Prüfung nötig; optional in Prüfung 4a/7a nichts.

## Nichts anderes

OP-Bericht (`buildVerband`), Aufklärungstexte, Online-Satz, Begleiter, Fuss-Track unverändert.

## Abnahme

Cowork-Prüfstand: 89 Brief-Referenzfälle gegen 02dd198 mit neuem Datenstand: Abweichung genau in den Fällen mit einer der neun Methoden (Satz einmal, direkt nach dem Risikosatz bzw. nach dem TEP-Hinweis), alle anderen Briefe zeichengleich, konservative Briefe zeichengleich; Fall Chevron + Kleinzehen/PIP: Satz einmal; Fall „Konservativ empfohlen“ mit Chevron: Satz vorhanden, Schluss „raten wir zu konservativer weiterer Therapie“; mit altem Datenstand (ohne Feld) alle Briefe zeichengleich; Selbsttest unverändert; keine Konsolenfehler; JSX transpiliert.

Am Handy: Brief Hallux valgus → Chevron → Abschluss: Risikosatz, dann „Nach dem Eingriff sind für mehrere Wochen redressierende Verbände …“.

Deploy: erst Upload `opmethoden.json` in den Bucket (zusammen mit dem Stand vom 07.10.), dann Push `app.html`.
