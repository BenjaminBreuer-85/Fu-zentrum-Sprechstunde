# Auftrag an die Clinic-Code-Sitzung: Kauf-Knopf vor dem Kongress ersetzen

Kontext: Benjamin präsentiert Fuss-Track am 10.09. auf dem Kongress. Paddle läuft noch in der Sandbox, die Live-Tore (Gewerbe, Police/Impressum, VIES) sind offen. Bis zum Livegang soll die Landingpage keine Kaufstrecke zeigen, aber Interessenten einsammeln.

## Aufgaben (index.html, Landingpage)

1. **Verkaufs-Schalter einbauen statt Code löschen.** Eine Konfigurationskonstante `VERKAUF_AKTIV = false` nahe der bestehenden Sandbox/Live-Konfigstelle. Der komplette Kauf-Block (Kauf-Knopf, Paddle.js-Nachladen, Dankeansicht, Nutzungsbedingungen-Satz unter dem Knopf) bleibt im Code erhalten und wird bei `false` nicht gerendert. Der spätere Livegang ist dann eine Ein-Wort-Änderung plus MODUS live.

2. **Interessenten-Block anzeigen, wenn `VERKAUF_AKTIV = false`.** An der Stelle des Kauf-Knopfs:

   Überschrift oder fette Zeile: „Fuss-Track Clinic erscheint im Herbst 2026."
   Text: „Interesse an einem Testzugang? Schreiben Sie an kontakt@fuss-track.de und Sie erhalten Bescheid, sobald es losgeht."
   Die Mailadresse als mailto-Link mit vorbelegtem Betreff „Testzugang Fuss-Track Clinic".

   Kein Formular, keine Datenbank, kein neues Datenschutz-Thema. Stilregeln beachten: Fließtext, keine Gedankenstriche, Petrol-Farbwelt.

3. **Sandbox-Spuren prüfen.** Bei `VERKAUF_AKTIV = false` darf nirgends ein Sandbox- oder Testbetrieb-Hinweis sichtbar sein. Preisangaben auf der Seite ebenfalls prüfen: Wenn der Preis irgendwo steht, entweder mit dem Kauf-Block ausblenden oder bewusst stehen lassen (Benjamins Linie: Preis auf Nachfrage offen nennen, nicht bewerben).

4. **LinkedIn-Vorschau (og-Tags) für BEIDE Seiten.** fuss-track.de und patienten.fuss-track.de bekommen og:title, og:description und og:image, damit geteilte Links in den Kongress-Posts ein sauberes Vorschaubild zeigen. og:image als lokales Bild im Repo (keine externen Quellen, BRAND.md), 1200x630, Petrol-Fläche mit Wortmarke reicht. Titelvorschläge: „Fuss-Track Clinic — Werkzeuge für die Fuß- und Sprunggelenkchirurgie" und „Fuss-Track — Ihr Begleiter bei Erkrankungen von Fuß und Sprunggelenk". Beschreibung je ein Satz, Patienten-Seite mit „kostenlos und werbefrei".

5. **Gegenprobe.** Lokal: Seite mit `VERKAUF_AKTIV = false` rendern, kein Kauf-Knopf, kein Paddle.js-Request (Netzwerk-Tab), Interessenten-Block sichtbar, mailto-Link öffnet mit Betreff. Schalter testweise auf true: Kaufstrecke erscheint unverändert. LinkedIn-Vorschau mit dem Post-Inspector oder einem og-Preview-Werkzeug prüfen, sobald live.

Deploy wie üblich: nur nach Freigabe durch Benjamin, Commit durch die Code-Sitzung, Benjamin pusht. Zieltermin: vor dem 05.09., damit die Kongress-Posts auf die fertige Seite verlinken.
