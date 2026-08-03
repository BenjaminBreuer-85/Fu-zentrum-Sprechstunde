# E-Mail-Vorlagen für Supabase Auth

Einzutragen im Dashboard unter **Authentication → Emails**:

| Datei | Vorlage im Dashboard |
|---|---|
| `einladung.html` | Invite user |
| `passwort-zuruecksetzen.html` | Reset password |

## Warum eigene Vorlagen nötig sind

Die Standardvorlage benutzt `{{ .ConfirmationURL }}`. Diese Adresse zeigt auf
`/auth/v1/verify` und löst den Token **serverseitig beim Abruf** ein — also auch
dann, wenn ein Mail-Scanner den Link vorab öffnet. Genau daran ist die erste
Beta-Einladung gescheitert (GMX, 02.08.2026).

Diese Vorlagen geben stattdessen `{{ .TokenHash }}` an `zugang.html` weiter.
Dort passiert beim Aufruf nichts; der Token wird erst durch den Klick auf den
Knopf eingelöst. Ohne diese Vorlagen wirkt `zugang.html` nicht — Supabase
verschickt dann weiter die alten Verify-Links.

## Regeln beim Ändern

**Vollständiges HTML-Dokument lassen.** Beide Dateien beginnen mit `<!DOCTYPE html>`
und haben `<head>` und `<body>`. Als blosses Fragment ausgeliefert erschien der
Inhalt in der GMX-App **doppelt** — einmal ohne, einmal mit Knopf (Befund vom
03.08.2026). Ein vollständiges Dokument ist für Mail-Clients eindeutig.

**Keine HTML-Kommentare in der Datei.** Der ursprüngliche Erklärungsblock stand
als 720 Zeichen langer Kommentar im Markup; Kommentare können in der
automatisch erzeugten Textfassung einer Mail auftauchen. Deshalb steht die
Erklärung hier in dieser Datei und nicht dort.

**Keine externen Bilder und keine Webfonts.** Beides erhöht die Spam-Bewertung
und wird von vielen Anbietern ohnehin blockiert.

**Den Link zweimal führen** — als Knopf und darunter als abtippbare Klartext-
Adresse. Manche Clients unterdrücken gestaltete Knöpfe.

**`&amp;` statt `&`** in den Adressen, sonst ist das Dokument nicht wohlgeformt.

## Was die Vorlagen nicht leisten

Die Zustellung selbst hängt an Brevo. Für diese Transaktionsmails gehört das
**Klick-Tracking abgeschaltet**: Brevo schreibt sonst alle Links auf eigene
Tracking-Adressen um, was Scanner geradezu einlädt und einen zusätzlichen
Fehlerpunkt schafft.
