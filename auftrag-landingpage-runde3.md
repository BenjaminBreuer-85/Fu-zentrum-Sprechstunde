# Auftrag: Landingpage, dritte Runde — Feinschliff nach Sichtprüfung

Geprüft am 26.08. in einer headless Vollansicht bei 390 px und 1280 px, alle Bilder laden, keine Konsolenfehler. Der Umbau aus Runde 2 sitzt. Sechs Punkte bleiben, drei davon sind Textkorrekturen.

## 1. Schlussblock widerspricht der Knopf-Entscheidung

Der Abschlussabschnitt (`section.final`) sagt weiterhin:

> „Testen Sie Fuss-Track Clinic 30 Tage kostenlos."
> „Kein Risiko, keine Zahlungsdaten, keine Installation — nach dem Test entscheiden Sie."

Das ist doppelt falsch. Erstens verspricht es den Sofort-Test, der laut Schalter-Entscheidung erst im Herbst kommt. Zweitens verstößt „Kein Risiko" wörtlich gegen BRAND.md Abschnitt 5 („keine Absolutaussagen (‚kein Risiko')").

Neuer Text bei `VERKAUF_AKTIV = false`, über denselben Mechanismus wie die Knopftexte:

> **Interesse an Fuss-Track Clinic?**
> Der Testzugang läuft dann 30 Tage, kostenlos und ohne Zahlungsdaten — nach dem Test entscheiden Sie.

Bei `true` kehrt die heutige Fassung zurück, aber ohne „Kein Risiko": „Keine Zahlungsdaten, keine Installation — nach dem Test entscheiden Sie." Der BRAND-Verstoß gilt in beiden Zuständen.

## 2. Meta-Description und Hero-Notiz

Die Meta-Description (Zeile 7) endet auf „30 Tage kostenlos testen." und die Hero-Notiz sagt „Keine Zahlungsdaten für den Test erforderlich". Beide sind statisch und versprechen den Sofort-Test.

- Meta-Description: „… Für Fußchirurginnen und Fußchirurgen." enden lassen, der Testsatz entfällt.
- Hero-Notiz bei `VERKAUF_AKTIV = false`: „Läuft im Browser, keine Installation · Testzugang kostenlos und ohne Zahlungsdaten". Die Reihenfolge stellt das um, was heute stimmt, nach vorn.

## 3. Einzelbild-Streifen bei Desktop halb leer

Bei ≥ 900 px ist ein Streifen zweispaltig (`flex-basis: calc(50% - 6px)`). Die Abschnitte „OP-Anleitungen und Röntgenmessungen" (`rx-1-meary`) und „Abrechnungswissen" (`ops-1-suche`) haben nur ein Bild — die rechte Hälfte der Karte bleibt sichtbar leer.

CSS-Fix, eine Zeile:

```css
@media (min-width: 900px){ .streifen > figure:only-child{flex-basis:100%;max-width:520px;margin:0 auto} }
```

Damit steht das Einzelbild zentriert statt linksbündig vor einer Leerfläche.

## 4. Drittes Patienten-Bild bei Desktop unauffindbar

Der Patienten-Streifen hat drei Bilder, bei Desktop sind zwei sichtbar und die Punkte sind ausgeblendet (`.punkte{display:none}` ab 900 px). Nichts zeigt an, dass ein drittes Bild existiert; der Streifen scrollt zwar, aber ohne Scrollbalken und ohne Punkte gibt es keinen Anlass dazu.

Fix: Punkte bei Desktop nur ausblenden, wenn alle Bilder sichtbar sind — praktisch: die Regel `display:none` an eine Klasse binden (`.streifen-komplett .punkte{display:none}`), die das vorhandene Skript setzt, wenn `scrollWidth <= clientWidth + 10`. Alternativ schlichter: bei genau drei Bildern die Punkte auch am Desktop stehen lassen.

## 5. Reihenfolge im Patienten-Streifen

Aktuell: Startseite, Verlauf, Wegweiser. Das stärkste Bild ist der Verlauf mit dem hervorgehobenen OP-Tag — er zeigt die Kernfunktion, die Startseite zeigt nur Struktur. Empfohlene Reihenfolge: **Verlauf, Startseite, Wegweiser** (`pat-2`, `pat-1`, `pat-3`). Kostet eine Zeilenvertauschung.

## 6. Nicht auf dieser Seite, aber aus Runde 2 offen

- **og:image der Patientenseite:** `og-patienten.jpg` liegt im Clinic-Repo, gehört aber in das Fuss-Track-Repo und in den `<head>` von `patienten.fuss-track.de`. Der Clinic-Teil ist erledigt, der Patienten-Teil nicht.
- **Porträtfoto** im Autor-Abschnitt ist weiterhin Platzhalter („wird ergänzt") — liegt bei Benjamin, nicht beim Code.

## Gegenprobe

1280 px: Meary- und OPS-Karte ohne Leerfläche, Patienten-Streifen zeigt Punkte oder alle drei Bilder. 390 px: unverändert. Suchmaschinen-Snippet ohne Testversprechen. Wortsuche über die ganze Seite: „Kein Risiko" kommt nicht mehr vor, „30 Tage" nur noch in den geschalteten beziehungsweise mit „dann" gebundenen Sätzen.

Deploy: nur `index.html`, kein Bucket-Upload.
