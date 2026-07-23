# CLAUDE.md — Fußzentrum Toolbox (Fu-zentrum-Sprechstunde)

Klinische Dokumentations-Toolbox des Departments Spezielle Fußchirurgie (Florence-Nightingale-Krankenhaus, Kaiserswerther Diakonie). Seit Stufe 1 des Lizenz-Umbaus (07/2026) ist `index.html` (~516 KB) die **Hülle** (React-Komponenten, Berechnungslogik, Loader); die **Inhalte liegen in `data/*.json`** und werden zur Laufzeit per fetch geladen. React 18 + Babel Standalone via unpkg-CDN, kein Build-Schritt. Deployment manuell per GitHub-Upload (GitHub Pages: `https://benjaminbreuer-85.github.io/Fu-zentrum-Sprechstunde/`). Geplante Stufe 2: Inhalte hinter Supabase-Login.

Schwester-Projekt: die Patienten-App **Fuss-Track** (`../Fuss-Track/fusstrack.html`), auf die die Toolbox per QR-Code/Deep-Links verweist (`FUSSTRACK_BASE_URL`). Für beide Apps gilt die Skill `fusstrack-toolbox` (Schreibstil-Regeln, PubMed-Recherche-Pflicht, Workflow).

**Wichtig:** Seit dem Umbau funktioniert index.html NICHT mehr per Doppelklick (`file://`) — fetch braucht einen Webserver (lokal: Dev-Server, produktiv: GitHub Pages).

## Dateien im Repo

| Datei | Rolle |
|---|---|
| `index.html` | App-Hülle: Loader, alle React-Komponenten, Berechnungslogik |
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
| `scripts/dev-server.py` | Lokaler Dev-Server mit Live-Reload (s. u.) |
| `scripts/verify_extraction.py` | Prüfskript: vergleicht data/*.json Wert für Wert mit dem alten Einbettungs-Stand aus Git |
| `bausteine.json` | **Wird von index.html NICHT geladen.** Ältere Arbeitskopie der Fuss-Track-Patientendaten; maßgebliche Version im Fuss-Track-Repo |
| `manuale/` | Bisher leer; reserviert für selbst gehostete PDF-Manuale (OPManuale verlinkt derzeit Google Drive) |

## Aufbau von index.html

1. **Kopf:** CSS, QR-Code-Generator (inline, MIT) — nicht anfassen.
2. **Daten-Loader (`<script>`, plain JS):** definiert die Erlös-Helper `window._E`/`_EF`/`_fx` (Code, keine Daten), lädt alle zehn `data/*.json` per `fetch(...?v=Date.now())`, setzt `window._KATALOG_META/_HD/_KX/_ERLOES_META/_DRG/_HDRG/_KURZ` und `window._DATA.<gruppe>`, wendet den **__fx-Reviver** an und aktiviert erst dann das App-Skript (setzt dessen type auf `text/babel` + `Babel.transformScriptTags()`). Ladefehler erscheinen in der roten Fehlerleiste `#err-display`.
3. **App-Skript (`<script type="text/plain" id="app-src">`):** alle Komponenten. Die früheren Daten-Konstanten sind Verweise: `const DIAG = window._DATA.diagnosen.DIAG` usw. (43 Stück). Abgeleitete Strukturen bleiben Code: `FUSS_DRG` und `INEK_IMPL` (IIFEs aus `window._DRG`), `ENDO_IMPL_PRO_DIAG` (referenziert die Impl-Listen), die Fuß-Eingriffs-Verdrahtung im OP-Bericht (`codes.push`/`o.push`-Logik).

**__fx-Mechanik:** In den JSONs stehen an ehemals `window._fx("…")`-Stellen Marker-Objekte `{"__fx": "…"}` mit dem Roh-Text. Der Reviver im Loader ersetzt exakt diese durch `window._fx(rohtext)` — €-Beträge werden so weiterhin zur Laufzeit aus den Erlösdaten berechnet, und ein Jahres-Update von data/erloes2026.json schreibt alle Hinweis-Beträge automatisch um.

Werkzeuge (`App()`-Routing per `tool`-State): `sb` Sprechstundenbrief · `ob` OP-Bericht Generator (Sektionen fuss/uc/endo/ws) · `aufklaerung` · `hdrg` OPS-Code-Zuordnung · `manuale` · `klassifikationen` · `roentgen` · `codes`.

## Wichtige Regeln

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
4. **Deploy:** Der Autor lädt manuell auf GitHub hoch — am Ende immer die exakt zu deployenden Dateien benennen. Bei Inhaltsänderungen gehören die betroffenen `data/*.json` IMMER mit zum Deploy.

## Lokaler Dev-Server (Standard bei jeder Arbeitssitzung)

Zu Beginn jeder Arbeitssitzung wird standardmäßig der Live-Reload-Dev-Server gestartet:

```
python3 scripts/dev-server.py
```

- **Adresse: `http://localhost:8000/index.html`** — der Browser lädt bei jeder Dateiänderung im Repo automatisch neu (Polling auf `/__livereload`, .git ausgenommen), Caching ist deaktiviert.
- Kein Node.js nötig; reine Python-Standardbibliothek.
- In Claude-Code-Sitzungen: Server per Bash im Hintergrund starten (die `.claude/launch.json`-Preview-Integration scheitert an macOS-Berechtigungen für den Desktop-Ordner); vor dem Start prüfen, ob Port 8000 schon belegt ist.
- **Achtung Injektionsfalle:** index.html hat KEIN schließendes `</body>`-Tag (Datei endet mitten im Markup); das einzige `</body>` der Datei liegt in einem JS-String (Word-Export). Der Dev-Server hängt sein Snippet deshalb ans Dateiende an — niemals an `</body>`-Fundstellen injizieren.
