# BRAND.md — Fuss-Track Markenrichtlinie

Verbindliche Referenz für alles Sichtbare und Lesbare der Marken **Fuss-Track** (Patienten) und **Fuss-Track Clinic** (Behandlerinnen und Behandler). Gilt für Landingpages, App-Oberflächen, App-Inhalte, Videos, QR-Karten, Präsentationen und Social-Media-Grafiken. Änderungen an dieser Datei nur durch Benjamin.

---

## 1. Farben

| Rolle | Wert | Verwendung |
|---|---|---|
| Primär „Petrol" | `#10535B` | Buttons, Überschriften-Akzente, Bänder, Logo |
| Petrol dunkel | `#0B3E45` | Hover-Zustände, Verläufe |
| Petrol hell (Tint) | `#E6F0F1` | Hintergrund-Bänder, Chips, Zebra-Flächen |
| Papier | `#FAFAF7` | Seitenhintergrund |
| Tinte | `#1D2421` | Fließtext |
| Grau (gedämpft) | `#5C6660` | Sekundärtext |
| Linien | `#D6E2E3` | Rahmen, Trenner |
| Bernstein (Akzent) | `#8A5A00` Text / `#E0A82E` Fläche | NUR für Zahlen, Erlöse, Hervorhebungen — sparsam |

Regeln: Petrol ist die einzige Markenfarbe — kein zweites Blau/Grün daneben. Bernstein nie großflächig. Weißer Text nur auf Petrol/Petrol dunkel.

## 2. Typografie

**Marketingseiten** (Landingpages, Unterstützen-Seite, Rechtsseiten):

- **Überschriften/Display:** Source Serif 4 (600/700) — Fallback: Georgia, serif
- **Fließtext/UI:** IBM Plex Sans (400/500/600) — Fallback: Systemschrift (system-ui)

**App-Oberflächen** (`fusstrack.html`, `app.html`):

- **Überschriften:** Source Serif 4 (600/700) — lokal geladen, damit die App als dieselbe Marke erkennbar bleibt
- **Fließtext, Bedienelemente, Formulare:** Systemschriften (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`). Das ist eine bewusste Entscheidung zugunsten der Ladezeit auf Mobilgeräten und keine Abweichung.

**Überall:**

- **Codes/Zahlenwerte (OPS, Beträge):** IBM Plex Mono (400/500) — Fallback: `ui-monospace, monospace`. Liegt die Datei in einem Repo nicht lokal vor, ist `ui-monospace` zulässig; nachgeladen wird nichts.
- Schriften stets **lokal gehostet** (woff2 im Repo), niemals von externen Servern (DSGVO).
- Dasselbe gilt für **alle übrigen Ressourcen**: Programmbibliotheken, Skripte, Symbole und Videos werden ausschließlich lokal ausgeliefert. Keine CDN-Einbindungen, keine iframes fremder Anbieter. Ausgenommen sind allein zwei funktionsnotwendige Verbindungen:
  - **Supabase-API** — Anmeldung und Nutzerdaten (Preise, Materialsätze).
  - **Paddle (nur Kaufstrecke, Nachladen erst bei Klick)** — Paddle.js wird nicht beim Seitenaufruf geladen, sondern erst, wenn jemand den Kauf-Knopf drückt. Bis zur Kaufabsicht bleibt die Landingpage frei von externen Verbindungen. Danach gilt die Ausnahme nur für den Checkout selbst; alles Übrige bleibt lokal.
- Keine weiteren Schriftfamilien, kein Kursiv als Dauerstil, Fettung sparsam.

## 3. Logo & Bildsprache

- **FT-Monogramm:** weißes Serifen-„FT" auf Petrol, abgerundetes Quadrat, feiner Innenrahmen. Quelldatei: ft-monogramm.svg. Nicht verzerren, nicht umfärben, Schutzraum ≈ Breite des „F".
- **Wortmarken:** „Fuss-Track" (Patienten) und „Fuss-Track Clinic" — Schreibweise immer mit Bindestrich und Doppel-s, „ß" nur dekorativ zulässig, nie in Domains/Dateinamen.
- **Signatur-Motiv:** der „Baustein" — modulare Karten/Chips mit Petrol-Linkskante (siehe Hero der Clinic-Seite). Wiederverwenden, wo Modularität gezeigt wird.
- Fotos: echte Screenshots und echte Personen statt Stock-Material; klinisch-aufgeräumt, keine Symbolbild-Klischees (keine Stethoskop-auf-Tastatur-Fotos).
- Screenshot-Rahmen: weiße Karte, drei Punkte oben, dezenter Schatten (wie auf den Landingpages).

## 4. Gestaltungsprinzipien (UI)

- Eckenradius 10–12 px, Schatten weich und sparsam (`rgba(16,83,91,…)`-Töne)
- Viel Papier-Weißraum; Petrol-Bänder als bewusste Zäsuren, max. 1–2 pro Seite
- Fokus-Ring in Bernstein (Barrierefreiheit), Animationen dezent und mit reduced-motion-Fallback
- Mobile immer mitdenken: einspaltig, Buttons kompakt

## 5. Sprache & Tonalität

**Beide Marken:**
- Geschlechtergerecht mit Paarformen („Ärztinnen und Ärzte", „Patientinnen und Patienten"); wo sperrig, neutral umformulieren oder direkte Anrede („liegt bei Ihnen")
- Sachlich und belegbar — keine Superlative („das beste"), keine Heil- oder Erfolgsversprechen, keine Absolutaussagen („kein Risiko")
- Die Erzählfigur: „vom Fußchirurgen gebaut, der es selbst täglich nutzt" — ehrlich, nie übertrieben
- Sie-Anrede

**Fuss-Track (Patienten):** einfache Sprache, Fachbegriffe stets erklärt („Hallux valgus — der ‚Ballenzeh'"), kurze Sätze, beruhigender Grundton; immer klar: ersetzt keinen Arztbesuch, diagnostiziert nicht. Der Frage-Baustein heißt „Beschwerde-Wegweiser" (niemals „Diagnose-Helfer" nach außen).

**Fuss-Track Clinic (Fachpublikum):** fachlich präzise, Terminologie ohne Erklärschleifen, Zahlen in Mono-Schrift, Kodier-/Erlösangaben immer mit Verantwortungshinweis („Orientierung; Verantwortung liegt bei Ihnen").

## 6. Rechtliche Sprach-Leitplanken

- Kein „Spende"/„gemeinnützig" (nur „freiwilliger Beitrag/unterstützen")
- Kein „kostenlos" für Clinic, kein Preisversprechen ohne „vorläufig", solange nicht final
- Werbung stets sachlich informierend (ärztliches Berufsrecht); Klinik- und D.A.F.-Nennung nur im freigegebenen Rahmen
- Quellenangaben bei medizinischen Aussagen, wo vorhanden

## 7. Wo diese Datei lebt und wer sie durchsetzt

- Identische Kopie in **beiden Repos** (Toolbox + Fußtrack), Master ist die Toolbox-Version. Die Synchronisierung erfolgt **von Hand**: Wer den Master ändert, kopiert die Datei anschließend in das andere Repo und pusht beide.
- **Claude Code (beide Projekte):** CLAUDE.md verweist verbindlich auf BRAND.md — jede UI-/Text-Änderung wird dagegen geprüft.
- **Inhalte-Projekt (Patiententexte):** Abschnitt 5 „Sprache & Tonalität" ist Teil der Projektanweisungen.
- **Claude Design:** Beim ersten Projekt einmal das Designsystem aus dieser Datei/den Landingpages anlegen und für alle weiteren Entwürfe verwenden.
- **Chat (Strategie/Fable):** kennt diese Richtlinie und wendet sie auf alles an, was hier entsteht.
