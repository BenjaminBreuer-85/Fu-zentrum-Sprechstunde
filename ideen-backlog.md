# Ideen-Backlog Fuss-Track Clinic und Fuss-Track Patient

Stand: 13.09.2026. Angelegt auf Wunsch des Autors, damit Verbesserungsideen nicht nur dann genannt werden, wenn gerade ein Auftrag dazu läuft. Regel: Jede Sitzung, die an der App arbeitet, trägt hier ein, was ihr nebenbei auffällt, mit Nutzen, Aufwand und Voraussetzung. Der Autor entscheidet, was in einen Auftrag wird. Nichts hier ist beauftragt, solange es nicht unter „Beauftragt" steht.

Bewertung: Nutzen für den Behandler (Zeit, Erlös, Rechtssicherheit, Patientennutzen), Aufwand (klein: ein Nachmittag der Code-Sitzung; mittel: ein Auftrag mit Datenteil; groß: mehrere Aufträge), Voraussetzung.

## A. Rechtssicherheit der Dokumentation

**A1 Briefprüfung (beauftragt, `auftrag-briefpruefung.md`).** Platzhalter, Widersprüche, Dubletten, Übergänge, Form. Nutzen hoch, Aufwand mittel.

**A2 Aufklärungszeitpunkt prüfen.** Bei elektiven Eingriffen verlangt die Rechtsprechung eine angemessene Bedenkzeit zwischen Aufklärung und Eingriff; am OP-Tag aufgeklärt reicht bei planbaren Eingriffen regelmäßig nicht. Die App kennt das Aufklärungsdatum (Brief) und könnte das geplante OP-Datum abfragen; liegt weniger als ein Tag dazwischen oder fehlt das Datum, erscheint ein Hinweis im Brief und in der Aufklärung („Aufklärung am …, Bedenkzeit bis …"). Nutzen hoch (häufigster formaler Angriffspunkt im Haftungsprozess), Aufwand klein. Voraussetzung: Feld OP-Datum im Sprechstundenbrief.

**A3 Erstellungszeitpunkt des OP-Berichts.** Verspätete OP-Berichte verlieren Beweiswert (KG Berlin, siehe `recherche-textbausteine-recht.md`). Der OP-Bericht-Generator könnte das OP-Datum abfragen und bei Erstellung später als am Folgetag einen Satz „Bericht erstellt am … aus dem OP-Protokoll" anbieten, damit die Verspätung erklärt ist. Nutzen mittel, Aufwand klein.

**A4 Kodier-Konsistenz zwischen Text und Kodes.** Der OP-Bericht nennt Spongiosaentnahme, Sehnentransfer oder Osteotomien im Text, die Kodeliste enthält den Kode nicht, oder umgekehrt. Die Fallsteuerung kennt die Kodes, der Bausteintext kennt die Eingriffe; ein Abgleich über eine kleine Tabelle „Baustein nennt Eingriff X, erwarteter Kode Y" fängt beides. Das ist die erlösseitige Ergänzung der Briefprüfung und trifft genau die Fälle, in denen die Kontextprozedur zwar operiert, aber nicht kodiert wurde. Nutzen hoch (Erlös und MDK), Aufwand mittel; gehört als Regelgruppe in `pruefung.json`.

**A5 Begründung stationärer Belegungstage.** Die Fallsteuerung sagt heute „jeden Tag in der Akte begründen". Eine Auswahl typischer Gründe (Schmerztherapie i.v., Wundkontrolle bei Risikofaktor, Mobilisation unter Entlastung nicht gesichert, Antikoagulation, soziale Situation) als Chips, die einen Satz in den OP-Bericht oder Verlaufsbrief setzen, macht aus dem Hinweis eine Dokumentation. Nutzen hoch bei Kürzungen, Aufwand klein bis mittel (Daten in `opsteuerung.json`, Darstellung in beiden Generatoren).

**A6 Hinweis zur Individualisierung im Onboarding.** Aus der Recherche: ein Satz in Hilfe oder Rundgang, dass Vorschläge zu prüfen und an den Fall anzupassen sind. Nutzen klein, aber kostenlos, Aufwand sehr klein.

## B. Zeit im Alltag

**B1 Merken der letzten Auswahl je Diagnose.** Wer dreimal am Tag Hallux valgus dokumentiert, klickt dreimal dieselben Befunde. Die Tabelle `nutzer_einstellungen` (aus dem Rundgang-Auftrag) kann je Diagnose die zuletzt gewählten Chips und Toggles speichern und beim nächsten Aufruf als „Wie zuletzt" anbieten, ohne sie automatisch zu setzen. Nutzen hoch, Aufwand mittel. Keine Patientendaten, nur Auswahlmuster.

**B2 Eigene Formulierungen je Behandler.** Ein Behandler ändert einen Bausteinsatz regelmäßig auf dieselbe Weise. Ein Feld „eigene Fassung" je Baustein, in `nutzer_einstellungen` gespeichert, ersetzt den Standard nur für dieses Konto; der Standard bleibt für alle anderen. Nutzen hoch für Vielnutzer, Aufwand mittel; Vorsicht: Vertraulichkeit der Inhalte bleibt gewahrt, weil nur der eigene Text gespeichert wird.

**B3 Offline-Fähigkeit im OP-Trakt.** Die Landingpage verspricht „auch am Tablet im OP-Trakt". Ohne Netz lädt die App heute nicht. Ein Service Worker, der `app.html`, `lib/` und die zuletzt geladenen Bucket-Dateien für das angemeldete Konto zwischenspeichert, macht OP-Anleitungen und Messmethoden ohne Netz nutzbar; Login und Preise bleiben online. Nutzen mittel bis hoch, Aufwand mittel; Voraussetzung: Entscheidung, welche Bucket-Inhalte auf dem Gerät liegen dürfen (Lizenzschutz).

**B4 Sprungmarken in langen Ansichten.** OP-Anleitungen und Klassifikationen sind lang; eine schwebende Inhaltsleiste (Zugang, Schritte, Implantate, Nachbehandlung) spart Scrollen am Handy. Nutzen mittel, Aufwand klein.

## C. Erlös und Steuerung

**C1 28 Zweige auf eine Quelle (beauftragt, `auftrag-hybrid-regeln.md`, fünfter Teil).**

**C2 Jahresstatistik ohne Patientendaten.** Die App könnte je Konto zählen, welche Dokumente je Eingriff, Setting und Ziel-DRG erzeugt wurden (nur Zähler, kein Fallbezug), und eine Tabelle „mein Fallmix" anzeigen. Das ist genau die Datenmatrix, die für den Vortrag von Hand gebaut wurde, und das Argument für die Klinikleitung. Nutzen mittel, Aufwand mittel; Voraussetzung: Speicherung in `nutzer_einstellungen` oder eigener Tabelle, Datenschutzerklärung prüfen (nur Zähler, aber konto­bezogen).

**C3 Katalogjahr-Wechsel als Ablauf.** Für 2027 stehen OPS-, Hybrid- und AOP-Katalog neu an. Ein dokumentierter Ablauf mit Prüfskript (Master-Excel gegen `katalog2026.json`, Regelblock gegen Definitionshandbuch) spart im Dezember Tage. Nutzen hoch für die Pflege, Aufwand klein (Skript existiert in Teilen aus dem Abgleich vom 09.09.).

**C4 Implantatampel mit eigener Referenz.** Die Ampel vergleicht mit InEK-Kosten. Ein zweiter Vergleichswert „mein Durchschnitt der letzten zehn Fälle desselben Eingriffs" (nur Beträge, kein Fallbezug) zeigt Ausreißer im eigenen Haus. Nutzen mittel, Aufwand klein bis mittel; hängt an C2.

## D. Patientenseite und Verbindung beider Apps

**D1 Nachbehandlungsabgleich.** Der OP-Bericht enthält ein Nachbehandlungsschema, der Begleiter in der Patienten-App ein anderes (Belastung, Walker-Wechsel, Röntgentermine). Beide stammen aus verschiedenen Dateien. Ein Abgleich beim Erzeugen des Kurzlinks („Begleiter sagt Teilbelastung ab Woche 4, OP-Bericht sagt Entlastung 6 Wochen") verhindert widersprüchliche Anweisungen an den Patienten. Nutzen hoch (Patientensicherheit, Haftung), Aufwand mittel; Voraussetzung: gemeinsames Schema-Feld je Eingriff.

**D2 Rückmeldung des Patienten an den Behandler.** Die Patienten-App speichert nichts; eine anonyme Rückmeldung („Anleitung verstanden ja/nein", „Schmerz höher als erwartet") per Kurzlink ohne Konto ist möglich, wäre aber der erste Datenfluss vom Patienten und braucht eine eigene Datenschutzentscheidung. Nutzen mittel, Aufwand mittel, Voraussetzung: rechtliche Klärung. Vorerst nur notiert.

**D3 QR-Code auf dem Aufklärungsbogen.** Heute steht der Code im Brief; die Aufklärung wäre der zweite natürliche Ort (Patient liest die Risikoliste zu Hause nach, mit dem Artikel zum Eingriff). Nutzen mittel, Aufwand klein.

## E. Betrieb und Pflege

**E1 Selbsttest-Seite in der App.** Eine versteckte Ansicht, die alle Bucket-Dateien lädt und die Querprüfungen aus dem Audit (Schlüssel zwischen `diagnosen`, `opmethoden`, `optexte`, `opsteuerung`, `kurzlinks`) ausführt, zeigt nach jedem Bucket-Upload in einer Minute, ob alles zusammenpasst. Nutzen hoch für den Autor, Aufwand klein.

**E2 Bucket-Stand sichtbar machen.** Unter „Über" die Versionsdaten der geladenen Datendateien anzeigen (Datum aus `_kommentar` oder Dateidatum), damit ein Tester sagen kann, welchen Stand er sieht. Aufwand sehr klein.

**E3 Deploy-Reihenfolge absichern.** Die App könnte beim Start prüfen, ob die Datendateien einen Mindeststand haben, den der Code erwartet (Versionsfeld je Datei), und sonst eine klare Meldung zeigen statt eines stillen Fehlers wie beim fehlenden Eintrag `metallentfernung`. Aufwand klein, verhindert die Pannenklasse vom 29.07.

## Entscheidung des Autors (13.09.2026, Stück für Stück)

Beauftragt: A1 (Briefprüfung, `auftrag-briefpruefung.md`), C1 (28 Zweige, `auftrag-hybrid-regeln.md`), und aus dieser Runde A4, A5 (als neues Werkzeug „Visite" für die tägliche stationäre Dokumentation; Inhalte werden abgestimmt), A6, B2, B4, D1, D2 (anonym, rückverfolgbar auf den Inhalt, feste Antworten plus Freitext, erst intern, später Anzeige in der Clinic), E1 (`auftrag-verbesserungen-2026-09.md`).

Zurückgestellt: B3 Offline, C3 Katalogjahr-Wechsel (im November), C4 Ampel mit eigener Referenz, E2 Bucket-Stand, E3 Versionsprüfung.

Gestrichen: A2 Aufklärungszeitpunkt, A3 Erstellungszeitpunkt, B1 Merken der letzten Auswahl, C2 Jahresstatistik, D3 QR-Code auf dem Aufklärungsbogen.
