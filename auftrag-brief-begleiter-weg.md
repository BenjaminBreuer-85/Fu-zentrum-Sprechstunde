# Auftrag Clinic + Fuss-Track: Der OP-Begleiter steht im Brief und ist auf der QR-Zielseite sofort zu finden

Stand 04.10.2026, Cowork-Sitzung. Frage des Autors: Wie kommt ein Patient heute aus dem QR-Code im Sprechstundenbrief in den OP-Begleiter? Der Begleiter muss im Brieftext erwähnt sein und auf der Zielseite klar zu finden sein. Dateien: Clinic `app.html` 7858cbc (804.941 B, f774ed0e…), Clinic `kurzlinks.json` (Stand 20.09.2026, 63 Ziele), Fuss-Track `fusstrack.html` 74e099a (695.379 B, f457e3a7…); Zeilenangaben darauf. Zwei Commits (je Repo einer), zwei Vollzugsmeldungen mit Commit-Hash und Zeilennummern; der Datenschritt `kurzlinks.json` kommt von der Cowork-Sitzung nach Freigabe (Abschnitt 1).

## Befund: der heutige Weg

Der Brief sagt bei einem OP-Weg (`app.html` Z. 3286–3291): „Zum Thema „Chevron-/Akin-Osteotomie“ liegen in der Fuss-Track-App weitere Informationen für Sie bereit. Sie können sie über den folgenden Code aufrufen.“ Darunter „Ihr Code: fuss-track.de/i/chevron“. Der Begleiter kommt im Brief nicht vor.

Die Kurzadresse wird (laut Datenlandkarte 13.09.2026) von `404.html` über `kurzlinks.json` aufgelöst; das Ziel ist für alle 45 OP-Einträge `fusstrack.html?op=<key>&modus=aufklaerung`, ohne `ctx=begleiter` und ohne Variante. Die Patienten-App zeigt dann die Artikelseite in der Fokus-Ansicht (`fusstrack.html` Z. 1389–1397: `begleitVerfuegbar` ist nur mit `ctx=begleiter` oder gültiger Variante wahr). Folge, am Prüfstand für alle 45 OP-Ziele geprüft: kein Umschalter zum Begleiter in der Kopfzeile, kein Knopf am Ende der Slides (`begleiterUrl` Z. 1411 ist null), kein Hauptmenü (Fokus-Ansicht). Der Fußhinweis (Z. 3169–3195) sagt zwar „Fuss-Track bietet darüber hinaus … einen Begleiter für die Zeit nach der Operation“, bietet aber nur den Link „Mehr über Fuss-Track“ auf die Landingpage; der Knopf „Weitere Themen in Fuss-Track ansehen“ erscheint gerade im OP-Fall nicht (`!opKontext`, Z. 3177). Der Patient müsste also: Landingpage → App öffnen → Kachel Begleiter → Krankheitsbild → Eingriff → Variante. Sechs Schritte, ohne dass ihn irgendetwas dorthin führt.

Mit `&ctx=begleiter` am Ziel (für 41 der 45 OP-Ziele geprüft; die vier übrigen sind `cotton` ohne Begleiter sowie die vom Brief nicht verwendeten Alt-IDs `osg-arthrodese-op`, `osg-tep-op`, `fhl`) zeigt die App heute: oben rechts einen kleinen Umschalter „→ Zum Patientenbegleiter“ (28 px hoch) und am Ende des letzten Textslides (Reiter 6, nicht 7 Quellen) den großen Knopf „Nachbehandlung Schritt für Schritt — zum Begleiter“ (Z. 3504–3512). Beide führen zur Begleiter-Einrichtung des passenden Krankheitsbildes („Hallux valgus · Begleitung“, Frage „Wie wird operiert?“, dann Variante). Der Mechanismus ist also da; er wird vom Brief nur nicht ausgelöst, und auf Slide 1 ist er leicht zu übersehen.

## 1. Datenschritt `kurzlinks.json` (Cowork-Sitzung, nach Freigabe)

Für jedes Ziel mit `art: "op"`, dessen Artikel in der Patienten-App einen Begleiter erreicht (41 Einträge, Liste aus dem Prüfstand `ww/qr_begleiter2.json`): an `url` den Parameter `&ctx=begleiter` anhängen und ein Feld `"begleiter": true` ergänzen. `cotton` und die Alt-IDs bleiben ohne. IDs und Titel unverändert (Regel in der Datei: IDs werden nie geändert; die Zieladresse darf angepasst werden, der Inhalt bleibt derselbe Artikel, nur mit Begleiter-Kontext). Keine Patientendaten, kein Tracking (der Parameter ist ein fester Modus-Schalter). Deploy: Push `kurzlinks.json` (Repo-Datei, kein Bucket). Damit wirkt der neue Weg auch für bereits ausgedruckte Briefe.

## 2. Clinic `app.html`: Satz im Brief (Z. 3286–3291)

`kurzlinkTitel(ziel)` (Z. 2316–2320) um eine Schwester `kurzlinkBegleiter(ziel)` ergänzen, die `ZIELE[kurzlinkId(ziel)].begleiter === true` liefert. Satz bei `qr.art === "eingriff"`:

- mit Titel und Begleiter: „Zum Thema „<Titel>“ liegen in der Fuss-Track-App weitere Informationen für Sie bereit. Dort finden Sie auch den OP-Begleiter, der Sie von der Vorbereitung bis zum Ende der Nachbehandlung Schritt für Schritt durch Ihre Operation führt. Beides erreichen Sie über den folgenden Code.“ (Korrektur des Autors 04.10.2026: der Begleiter beginnt Wochen vor der Operation, `SHARED_PRE_OP_PHASEN` ab Tag −50, nicht erst danach.)
- mit Titel ohne Begleiter: wie heute („… weitere Informationen für Sie bereit. Sie können sie über den folgenden Code aufrufen.“).
- ohne Titel (Datei fehlt): wie heute „Zum geplanten Eingriff liegen …“.
- `qr.art === "krankheitsbild"`: unverändert.

Selbsttest-Prüfung 6 (`kurzlinks.json`) um das Feld `begleiter` erweitern: jeder OP-Eintrag mit `ctx=begleiter` in der `url` muss `begleiter: true` tragen und umgekehrt.

## 3. Fuss-Track `fusstrack.html`: Begleiter auf der Zielseite sofort sichtbar

(a) **Begleiter-Karte oben**, direkt unter dem Fokus-Kopf (nach Z. 1426), nur wenn `begleiterUrl` gesetzt ist (also `ctx=begleiter` oder gültige Variante) und nicht `IN_APP_NAV`: Karte in der Hauptfarbe mit Überschrift „Ihr OP-Begleiter: von der Vorbereitung bis zur Nachbehandlung“, einem Satz „Fuss-Track begleitet Sie von den Wochen vor der Operation bis zum Ende der Nachbehandlung: was wann ansteht, mit Erinnerungen, Checklisten und Übungen.“ und dem Knopf „Begleiter einrichten →“ (Ziel `begleiterUrl`, derselbe wie am Slide-Ende). Darunter in 12 px: „Lesen Sie zuerst die Information zu Ihrem Eingriff; der Begleiter wartet danach hier und am Ende des Textes.“ Die Karte steht über den Reitern, damit sie auf jedem Slide beim Hochscrollen erreichbar ist; nicht fest (kein `position: sticky`), damit sie den Text nicht verdeckt.

(b) **Fußhinweis** (Z. 3169–3195): im OP-Fall (`opKontext`) zusätzlich zum Satz einen Knopf „Zum OP-Begleiter“ mit `begleiterUrl` (als Prop durchreichen), wenn `begleiterUrl` gesetzt ist; sonst wie heute. Der Link „Mehr über Fuss-Track“ bleibt.

(c) **Umschalter** (Z. 1424, Header) unverändert. **Slide-Ende-Knopf** (Z. 3504–3512): Titel „Nachbehandlung Schritt für Schritt — zum Begleiter“ ändern in „Ihr OP-Begleiter: Vorbereitung und Nachbehandlung“, Unterzeile „Von den Wochen vor der Operation bis zum Ende der Nachbehandlung, mit Erinnerungen und Übungen.“; die Karte oben ist der dritte, früheste Weg.

(d) Der Weg aus dem Begleiter zurück zur Information bleibt wie heute (`fokus`-Rücksprung, Z. 1425).

## Nichts anderes

QR-Erzeugung, `kurzlinkId`, Kurzadresse, Diagnose-Satz, Begleiter-Inhalte, `phasen.json`, Wegweiser unverändert.

## Abnahme

Cowork-Prüfstand: (1) Clinic: 89 Brief-Referenzfälle gegen 7858cbc: Abweichung nur im Online-Satz der OP-Fälle mit Begleiter (Chevron, Lapidus, OSG-TEP, AMIC, Kleinzehen/PIP …), Cotton-Fall mit altem Satz, konservative Briefe zeichengleich; Selbsttest 6 ohne Fehler, ohne `kurzlinks.json` alter Wortlaut. (2) Fuss-Track, 393 px: `?op=chevron&modus=aufklaerung&ctx=begleiter` → Karte oben mit Knopf, Umschalter, Slide-6-Knopf, Fußknopf, alle vier mit derselben Zieladresse (`?kb=hallux_valgus&fokus=…`); Ziel zeigt „Hallux valgus · Begleitung“; ohne `ctx` keine Karte und kein Fußknopf (Archiv-Aufruf bleibt linkfrei); `?op=cotton&modus=aufklaerung&ctx=begleiter` ohne Karte (kein Begleiter); In-App-Aufruf (`nav=1`) ohne Karte. (3) Alle 41 Ziele aus `kurzlinks.json` mit `ctx`: Karte vorhanden, Ziel lädt, keine Konsolenfehler; JSX-Transpile-Prüfung.

Am Handy: Brief → Hallux valgus → Chevron: Satz mit „OP-Begleiter, der Sie von der Vorbereitung bis zum Ende der Nachbehandlung …“; Code scannen → Artikel mit blauer Karte oben → „Begleiter einrichten“ → „Hallux valgus · Begleitung“ → Variante wählen → Begleiter läuft; „← zurück zur ausgewählten Information“ führt zum Artikel.

Deploy: Clinic Push `kurzlinks.json` + `app.html`; Fuss-Track Push `fusstrack.html`. Reihenfolge: zuerst Fuss-Track (Karte), dann `kurzlinks.json`, dann `app.html`.

Vollzugsmeldungen bitte mit Commit-Hash und Zeilennummern.
