# CLAUDE.md — Fußzentrum Toolbox (Fu-zentrum-Sprechstunde)

Klinische Dokumentations-Toolbox des Departments Spezielle Fußchirurgie (Florence-Nightingale-Krankenhaus, Kaiserswerther Diakonie). Produktname: **Fuss-Track Clinic**. Live unter **`https://fuss-track.de/`** (GitHub Pages mit Custom Domain + Enforce HTTPS; die alte github.io-Adresse leitet um). `index.html` ist die öffentliche **Landingpage**; die App selbst ist **`app.html`** (~530 KB): die **Hülle** (React-Komponenten, Berechnungslogik, Loader), deren **Inhalte in `data/*.json`** liegen. React 18 + Babel Standalone via unpkg-CDN, kein Build-Schritt. Deployment per Git-Push (GitHub Desktop) oder Web-Upload.

**Stufe 2 (07/2026): Inhalte hinter Login.** Der Loader hat zwei Pfade: **lokal** (localhost) lädt er aus `./data/`; **produktiv** verlangt er Anmeldung (supabase-js v2 via jsDelivr, E-Mail+Passwort) und lädt die zehn JSONs aus dem **privaten Supabase-Storage-Bucket** `toolbox-data`. Konfiguration im Block `window.TOOLBOX_AUTH` in app.html (Projekt-URL + anon-Key; der anon-Key ist bewusst öffentlich, der Schutz liegt in der Storage-Policy „select nur für authenticated"). `?auth=1` erzwingt den Login-Pfad lokal zum Testen. **Supabase-Site-URL muss auf `https://fuss-track.de/app.html` zeigen** (Dashboard-Einladungen nutzen sie als Ziel — auf der Landingpage würden Invite-Links ins Leere laufen). Einrichtung/Betrieb: `SUPABASE_SETUP.md`. **Sobald Supabase live ist: `data/` gehört NICHT mehr ins öffentliche GitHub-Repo** (lokal bleibt es für Dev-Server und als Upload-Quelle); Jahres-Updates ersetzen die Datei im Supabase-Bucket.

**Stufe 3 (geplant): Bezahl-Automatik — Strategie-Entscheidungen vom 24.07.2026:**
- **Produktname: „Fuss-Track Clinic"** (die Patienten-App heißt weiterhin „Fuss-Track").
- **Zahlungsanbieter: Paddle** als Merchant of Record (Lemon Squeezy ausgeschieden — Übergangsphase nach Stripe-Übernahme; Digistore24 zu teuer).
- **Preismodell: Jahres-Abo pro Nutzer** mit 30 Tagen kostenlosem Test; Preishöhe wird nach der Beta festgelegt (Korridor 150–300 €/Jahr).
- **Reihenfolge:** Erst Landingpage + Rechtstexte (Paddle prüft die Produktseite vor Konto-Freischaltung), dann Paddle-Konto, dann Webhook-Automatik (Zahlung → Supabase Edge Function → Invite; Abo-Ende → Sperrung). Bis dahin läuft Onboarding ausschließlich über das Invite-Verfahren im Supabase-Dashboard.

Schwester-Projekt: die Patienten-App **Fuss-Track** (`../Fuss-Track/fusstrack.html`), auf die die Toolbox per QR-Code/Deep-Links verweist (`FUSSTRACK_BASE_URL`). Für beide Apps gilt die Skill `fusstrack-toolbox` (Schreibstil-Regeln, PubMed-Recherche-Pflicht, Workflow).

**Wichtig:** Seit dem Umbau funktioniert index.html NICHT mehr per Doppelklick (`file://`) — fetch braucht einen Webserver (lokal: Dev-Server, produktiv: GitHub Pages).

## Dateien im Repo

| Datei | Rolle |
|---|---|
| `index.html` | **Öffentliche Landingpage** „Fuss-Track Clinic" (Marketing, Preis, FAQ; Design gem. BRAND.md) |
| `app.html` | **App-Hülle**: Loader, Login, alle React-Komponenten, Berechnungslogik (bis 07/2026 hieß sie index.html) |
| `BRAND.md` | Verbindliche Markenrichtlinie (Farben, Typografie, Ton) — identische Kopie im Fuss-Track-Repo pflegen |
| `fonts/*.woff2` | Lokale Schriften (Source Serif 4, IBM Plex Sans/Mono; latin-Subset, SIL OFL) — DSGVO: keine externen Font-Server |
| `CNAME` | GitHub-Pages-Custom-Domain `fuss-track.de` — nie löschen |
| `manifest.json` | Web-App-Manifest: `start_url` = `/app.html`, damit Homescreen-Verknüpfungen immer in der App starten (auch wenn von der Landingpage aus angelegt) |
| `data/katalog2026.json` | `_KATALOG_META`, `_KX`, `_HD` = OPS-Katalog 2026 (Bitmaske f: 1=AOP, 2=Hybrid-DRG, 4=Kontextprozedur). **NICHT von Hand editieren** — Quelle: OPS_Katalogdaten_2026_MASTER.xlsx |
| `data/erloes2026.json` | `_ERLOES_META` (u. a. `lbfw`), `_DRG`, `_HDRG`, `_KURZ`, `GVD`. **NICHT von Hand editieren** — Quelle: Erloesdaten_2026_MASTER.xlsx; Jahres-Update = Datei komplett ersetzen |
| `data/diagnosen.json` | `DIAG` (15 Diagnosen), `COALITIO_BEFUNDE`, `KONSERV`, `RISIKEN`, `RISIKEN_ENDO`, `KONTROLLE_TEXT`, `KONTROLLE_LABEL` |
| `data/opmethoden.json` | `OPS` (~43 OP-Methoden `{k,b,r,t}`), `OPS_LABELS`, `AUFKLAERUNG_MAP`, `PATIENT_EINGRIFF_MAP`, `PATIENT_VARIANTEN` |
| `data/opsteuerung.json` | `OP_STEUERUNG` (Abrechnungslogik je Eingriff), `UGVD_ABSCHLAG`, `ME_REGIONEN` |
| `data/endo.json` | `ENDO_DRG`, `ENDO_KONSTELLATIONEN`, `ENDO_BEF_*`, `ENDO_ZE`, `ENDO_*_IMPL`, `ENDO_EINGRIFFE` |
| `data/preise.json` | `EINZELPREISE` (145 Implantat-/Materialpreise), `UC_IMPL_*` |
| `data/optexte.json` | `T` (93 Fuß-OP-Texte), `UC_EINGRIFFE`, `UC_TEXT_MAP`, `WS_EINGRIFFE`, `WS_WIRBEL`, `WS_SEGMENTE` |
| `data/aufklaerung.json` | `AUFKLAERUNG_RISIKEN` (43 Eingriffe) |
| `data/referenz.json` | `KLASSIFIKATIONEN` (47), `ROENTGEN` (14), `MESSMETHODEN` (32), `MANUALE` |
| `landing.html` | Öffentliche Produktseite „Fuss-Track Clinic" (Voraussetzung für Paddle-Prüfung; `noindex` bis Rechtstexte final) |
| `impressum.html`, `datenschutz.html`, `agb.html`, `widerruf.html` | Rechtstexte-Gerüst mit [PLATZHALTER]-Blöcken — Inhalte kommen von Anwalt/Generator, nie von Claude formulieren |
| `DEPLOY.md` | **Deploy-Checkliste**: was ins Repo, was in den Bucket, in welcher Reihenfolge — vor jedem Deploy lesen |
| `zuordnung/implantat_zuordnung.json` | Standard-Materialsatz (Eingriff → Implantattyp → Anzahl), preis- und markenfrei — liegt bewusst offen im Repo, nicht im Bucket |
| `SUPABASE_SETUP.md` | Einrichtungs- und Betriebsanleitung für den Login (Stufe 2) |
| `scripts/dev-server.py` | Lokaler Dev-Server mit Live-Reload (s. u.) |
| `scripts/verify_extraction.py` | Prüfskript: vergleicht data/*.json Wert für Wert mit dem alten Einbettungs-Stand aus Git |
| `bausteine.json` | **Wird von index.html NICHT geladen.** Ältere Arbeitskopie der Fuss-Track-Patientendaten; maßgebliche Version im Fuss-Track-Repo |
| `manuale/` | Bisher leer; reserviert für selbst gehostete PDF-Manuale (OPManuale verlinkt derzeit Google Drive) |

## Aufbau von app.html (der App-Hülle)

1. **Kopf:** CSS, QR-Code-Generator (inline, MIT) — nicht anfassen.
2. **Daten-Loader (`<script>`, plain JS):** definiert die Erlös-Helper `window._E`/`_EF`/`_fx` (Code, keine Daten) und `window.TOOLBOX_AUTH` (Stufe-2-Konfiguration). Lädt die zehn Daten-Gruppen — lokal per `fetch("data/…?v=Date.now())`, produktiv nach Login via `supabase.storage.download()` —, setzt `window._KATALOG_META/_HD/_KX/_ERLOES_META/_DRG/_HDRG/_KURZ` und `window._DATA.<gruppe>`, wendet den **__fx-Reviver** an und aktiviert erst dann das App-Skript (setzt dessen type auf `text/babel` + `Babel.transformScriptTags()`). Login-Maske, „Passwort vergessen?"-Strecke, „Neues Passwort setzen" (Einladungs-/Reset-Links, Hash-Typ `recovery`/`invite`) und „Abmelden"-Link sind plain-DOM im Loader; Nutzer-Onboarding läuft über Dashboard-„Invite user" (Selbstregistrierung bleibt AUS — Lizenzschutz). Ladefehler erscheinen in der roten Fehlerleiste `#err-display`.
3. **App-Skript (`<script type="text/plain" id="app-src">`):** alle Komponenten. Die früheren Daten-Konstanten sind Verweise: `const DIAG = window._DATA.diagnosen.DIAG` usw. (43 Stück). Abgeleitete Strukturen bleiben Code: `FUSS_DRG` und `INEK_IMPL` (IIFEs aus `window._DRG`), `ENDO_IMPL_PRO_DIAG` (referenziert die Impl-Listen), die Fuß-Eingriffs-Verdrahtung im OP-Bericht (`codes.push`/`o.push`-Logik).

**__fx-Mechanik:** In den JSONs stehen an ehemals `window._fx("…")`-Stellen Marker-Objekte `{"__fx": "…"}` mit dem Roh-Text. Der Reviver im Loader ersetzt exakt diese durch `window._fx(rohtext)` — €-Beträge werden so weiterhin zur Laufzeit aus den Erlösdaten berechnet, und ein Jahres-Update von data/erloes2026.json schreibt alle Hinweis-Beträge automatisch um.

Werkzeuge (`App()`-Routing per `tool`-State): `sb` Sprechstundenbrief · `ob` OP-Bericht Generator (Sektionen fuss/uc/endo/ws) · `aufklaerung` · `hdrg` OPS-Code-Zuordnung · `manuale` · `klassifikationen` · `roentgen` · `codes`.

## Meine Implantatpreise (Modul in Arbeit)

Implantatpreise sind **Nutzerdaten**, keine Auslieferungsdaten — jeder Nutzer pflegt seine eigenen (die Preise der Klinik sind vertraulich). Datenmodell zweistufig: **Einzelpreise** (Implantat-ID → Stückpreis, einzige Preisquelle) und **Zuordnungen** (Eingriff-ID → Implantat-ID → Anzahl, preisfrei). Paketpreise werden immer berechnet, nie gespeichert.

**Excel-Vorlage (Export wie Import), drei Blätter:** „Anleitung" · „Meine Preise" (Implantat | Hersteller | Artikelnummer | Einzelpreis | Implantat-ID grau) · „Eingriffe" (Sektion | Eingriff | Variante | Implantat | Anzahl | Einzelpreis | Zeilensumme | IDs grau, Zwischensumme je Eingriff, echte INDEX/MATCH- und SUM-Formeln). Erzeugt mit `lib/xlsx-style.min.js` (xlsx-js-style, MIT) — SheetJS Community kann keine Styles schreiben.

**Abschnitte A/B in „Meine Preise":** Abschnitt A = Positionen, die in den hinterlegten Eingriffen vorkommen (wird beim Erzeugen automatisch aus den Zuordnungen berechnet, damit er mitwächst); Abschnitt B = alle übrigen, optional. Keine Position wird je gelöscht.

**Import-Regeln (verbindlich, entschieden 27.07.2026):**
- Zuordnung primär über die ID-Spalten, ersatzweise über die Bezeichnung.
- **Konfliktregel: Bezeichnung schlägt ID.** Weicht die Bezeichnung von der zur ID gehörenden ab und ist sie in „Meine Preise" auflösbar, gilt die Bezeichnung (der Nutzer hat sichtbar getippt, die ID ist graue Technik). Die Vorschau weist das als „ausgetauscht: alt → neu" aus.
- **Fehlende Eingriffe werden nie automatisch gelöscht:** Fehlt eine Eingriffsgruppe komplett in der hochgeladenen Datei, meldet die Vorschau das ausdrücklich („1 Eingriff fehlt in der Datei: … — behalten oder löschen?") und der Nutzer entscheidet pro Import.
- Der Import ersetzt den Materialsatz **je Eingriff** vollständig (nicht additiv), damit gelöschte Positionen nicht zurückkehren.
- Positionen aus Abschnitt B und eigene, vom Nutzer ergänzte Zeilen werden übernommen und gespeichert — **nie** als Fehler oder „nicht zugeordnet" gemeldet.
- Die Vorschau vor der Übernahme unterscheidet drei Zahlen: „X benötigte Positionen mit Preis", „Y optionale Positionen", „Z Positionen ohne Preis (nur relevant, wenn benötigt)". Wirklich unklare Zeilen werden als „nicht zugeordnet" gemeldet, nie stillschweigend verworfen.
- **Kein stiller Teilbetrag:** Fehlt zu einem Eingriff auch nur ein Preis, wird kein DB2 ausgegeben, sondern „unvollständig — X Positionen ohne Preis".

## Wichtige Regeln

- **Markenrichtlinie (verbindlich):** Alle Änderungen an Oberfläche, Texten oder Grafiken müssen `BRAND.md` entsprechen. Bei Konflikten BRAND.md folgen und den Autor auf den Konflikt hinweisen. Bestehende Oberflächen werden NICHT automatisch an BRAND.md angeglichen — nur künftige Änderungen laufen dagegen; Abweichungen im Bestand nur auflisten, nicht ändern.
- **BRAND.md-Synchronisation:** BRAND.md existiert identisch in beiden Fuss-Track-Repos (dieses Toolbox-Repo und `../Fuss-Track`). Nach jeder Änderung an BRAND.md den Nutzer erinnern, die Kopie im jeweils anderen Repo zu aktualisieren.
- **UNVERÄNDERLICHKEIT DER ABRECHNUNGSDATEN (oberste Regel):** Alle Abrechnungs- und Katalogdaten — OPS-Codes, ICD-Codes, DRG-Zuordnungen, Bewertungsrelationen, Pauschalen, Preise, Verweildauern (uGVD/mGVD/oGVD), InEK-Kostenwerte — sind behördlich bzw. vertraglich festgelegt und folgen KEINER inneren Logik. Sie dürfen niemals korrigiert, vereinheitlicht, ergänzt, umformatiert oder aus Mustern abgeleitet werden. Scheinbare Inkonsistenzen (Lücken in Code-Reihen, uneinheitliche Suffixe, „unplausible" Beträge) sind kein Fehler, sondern Katalogrealität. Beim Verschieben/Auslagern solcher Daten werden alle Werte exakt 1:1 übernommen und anschließend Wert für Wert gegen den alten Stand verglichen (`scripts/verify_extraction.py`).
- **Kodierung ist deutsch:** ICD-10-GM und G-DRG/Hybrid-DRG. Der verbundene ICD-10-Connector (MCP) liefert US-ICD-10-CM/PCS und passt NICHT 1:1 — nur als grobe Orientierung, nie ungeprüft übernehmen.
- `data/katalog2026.json` und `data/erloes2026.json` nur als Ganzes aus den Master-Excel-Dateien ersetzen, nie einzelne Werte ändern.
- Medizinische Textänderungen: erst recherchieren (PubMed, mit PMID/DOI), dann Vorschlag zur Freigabe — nie stillschweigend genehmigte Texte überschreiben.
- Schreibstil (auch für Aufklärungs-/Patiententexte): Fließtext statt Label-Bullets, keine rhetorischen Fragen, keine stilistischen Doppelpunkte, deutsche Anführungszeichen „…", schwierige Begriffe kurz in Klammern erklären. ICD-Codes gehören in die klinischen Tools, nie in Patiententexte.

## Workflow für Änderungen

1. **Ändern** in `index.html` (Komponenten/Logik) bzw. `data/*.json` (Inhalte); bei medizinischem Inhalt erst Vorschlag zur Freigabe.
2. **Validieren:**
   - JSON: jede geänderte Datei parsen (`python3 -c "import json;json.load(open('data/x.json'))"`).
   - JSX: App-Skript-Block extrahieren und mit Babel transpilieren (kein Node installiert — als JS-Runtime dient macOS-`jsc`: `/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc`; Babel z. B. aus `../Fuss-Track/lib/babel.min.js`).
   - Referenzen: jeder Key in `DIAG[x].opMethoden` existiert in `OPS`; `OP_STEUERUNG`-/`AUFKLAERUNG_MAP`-Keys passen zu `OPS`; DRG-Codes existieren in `_DRG`/`_HDRG`; `__fx`-Marker nur als `{"__fx": "string"}`.
   - Nach Daten-Verschiebungen: `python3 scripts/verify_extraction.py <ref>` — `<ref>` ist ein Git-Stand, der die Daten noch EINGEBETTET in index.html hat (Stufe-1-Vergleich; nach dem Umbau-Commit den Pre-Umbau-Hash angeben, z. B. `2aafcc5`).
3. **Live-Preview:** Dev-Server (s. u.), `http://localhost:8000/index.html`.
4. **Deploy:** **Zuerst `DEPLOY.md` lesen** — Bucket-Upload vor Push. Der Autor lädt manuell auf GitHub hoch — am Ende immer die exakt zu deployenden Dateien benennen. Solange Supabase noch nicht live ist, gehören bei Inhaltsänderungen die betroffenen `data/*.json` mit zum GitHub-Deploy. **Sobald Supabase live ist:** Inhaltsänderungen werden im Supabase-Bucket ersetzt (Storage → Datei überschreiben), `data/` bleibt aus dem GitHub-Repo draußen; zu GitHub geht dann nur noch index.html/Hüllen-Code.

## Lokaler Dev-Server (Standard bei jeder Arbeitssitzung)

Zu Beginn jeder Arbeitssitzung wird standardmäßig der Live-Reload-Dev-Server gestartet:

```
python3 scripts/dev-server.py
```

- **Adressen: App `http://localhost:8000/app.html` · Landingpage `http://localhost:8000/`** — der Browser lädt bei jeder Dateiänderung im Repo automatisch neu (Polling auf `/__livereload`, .git ausgenommen), Caching ist deaktiviert.
- Kein Node.js nötig; reine Python-Standardbibliothek.
- In Claude-Code-Sitzungen: Server per Bash im Hintergrund starten (die `.claude/launch.json`-Preview-Integration scheitert an macOS-Berechtigungen für den Desktop-Ordner); vor dem Start prüfen, ob Port 8000 schon belegt ist.
- **Achtung Injektionsfalle:** index.html hat KEIN schließendes `</body>`-Tag (Datei endet mitten im Markup); das einzige `</body>` der Datei liegt in einem JS-String (Word-Export). Der Dev-Server hängt sein Snippet deshalb ans Dateiende an — niemals an `</body>`-Fundstellen injizieren.
