# CLAUDE.md — Fußzentrum Toolbox (Fu-zentrum-Sprechstunde)

Klinische Dokumentations-Toolbox des Departments Spezielle Fußchirurgie (Florence-Nightingale-Krankenhaus, Kaiserswerther Diakonie). Die gesamte App ist **eine einzige Datei: `index.html`** (~1,3 MB, ~12.300 Zeilen), React 18 + Babel Standalone via unpkg-CDN, kein Build-Schritt. Deployment erfolgt manuell per GitHub-Upload (GitHub Pages: `https://benjaminbreuer-85.github.io/Fu-zentrum-Sprechstunde/`).

Schwester-Projekt: die Patienten-App **Fuss-Track** (`../Fuss-Track/fusstrack.html`), auf die die Toolbox per QR-Code/Deep-Links verweist (`FUSSTRACK_BASE_URL`). Für beide Apps gilt die Skill `fusstrack-toolbox` (Schreibstil-Regeln, PubMed-Recherche-Pflicht, Workflow).

## Dateien im Repo

| Datei | Rolle |
|---|---|
| `index.html` | Die komplette Toolbox-App (einzige produktive Datei) |
| `bausteine.json` | **Wird von index.html NICHT geladen.** Ältere/abweichende Arbeitskopie der Fuss-Track-Patientendaten (376 Bausteine vs. 537 im Fuss-Track-Repo). Maßgebliche Version liegt im Fuss-Track-Repo — diese Kopie nicht als Quelle verwenden, ohne das mit dem Autor zu klären |
| `manuale/` | Bisher leer (`.gitkeep`). Reserviert für selbst gehostete PDF-Manuale; die `OPManuale`-Komponente verlinkt aktuell auf Google Drive, `BASE_URL` zeigt aber schon auf diesen Ordner |

## Aufbau von index.html

Drei `<script>`-Blöcke:

1. **Kopf (~Zeile 32–62):** inline eingebetteter QR-Code-Generator (qr-creator, MIT) — nicht anfassen.
2. **Katalogdaten-Block (~Zeile 103–3909, plain JS):** `window._KATALOG_META` und `window._HD` = kompletter OPS-Katalog 2026 als Array `[code, beschreibung, f]` mit Bitmaske `f`: 1=AOP, 2=Hybrid-DRG, 4=Kontextprozedur (kombinierbar). Kommentar-Regel beachten: **„NICHT VON HAND EDITIEREN"** — Quelle ist `OPS_Katalogdaten_2026_MASTER.xlsx`; Hybrid-Vorrang-Regel (Codes in AOP UND Hybrid zählen nur als Hybrid).
3. **Haupt-Block (`text/babel`, ~Zeile 3910–12281):** alle Daten-Konstanten und React-Komponenten.

Einstieg: `App()` (~Zeile 12171) schaltet per `tool`-State zwischen den Werkzeugen um, `LandingPage` ist das Menü:

| tool | Komponente | Zweck |
|---|---|---|
| `sb` | `SprechstundenbriefApp` | Arztbriefe (Sprechstundenbrief) mit Befunden, Score-Bezeichnungen, DRG-/Erlös-Simulation, QR-Code zur Patienten-App, Rich-Text-Copy für Word/Outlook |
| `ob` | `OPBerichtApp` | OP-Bericht-Generator mit Sektionen `fuss`, `uc` (Unfallchirurgie), `endo`, `ws` (Wirbelsäule): OP-Texte, ICD/OPS-Codes, Materialkosten, Hybrid-DRG-/DRG-Erlös |
| `aufklaerung` | `AufklaerungstoolView` | Aufklärungstexte: allgemeine + eingriffspezifische Risiken (dedupliziert), Alternativen |
| `hdrg` | `HDRGSearch` | OPS-Code-Zuordnung 2026: Suche in `window._HD` (H-DRG / AOP / Kontextprozedur) |
| `manuale` | `OPManuale` | PDF-Bibliothek der OP-Techniken (Google-Drive-Links) |
| `klassifikationen` | `KlassifikationenView` | Klassifikationen (`KLASSIFIKATIONEN`, ~Zeile 10189) |
| `roentgen` | `RoentgenView` | Röntgen-Standardaufnahmen (`ROENTGEN`, ~11099) + Messmethoden (`MESSMETHODEN`, ~11200) |
| `codes` | `CodeUebersicht` | Zentrale OPS-Code-Bibliothek mit Verwendung pro Eingriff |

Zeilennummern verschieben sich bei Edits — Konstanten immer per Namen greppen.

## Datenblöcke (im text/babel-Block)

### Diagnosen & OP-Methoden (Sprechstundenbrief)
- **`DIAG`** (~3945): 15 Diagnosen (`hallux_valgus`, `hallux_rigidus`, `osg_instabil`, `osg_arthrose`, `usg_arthrose`, `ocl`, `knick_senk`, `mittelfuss_arthrose`, `haglund`, `achillesruptur`, `juvenil_ppv`, `metatarsalgie`, `peronealsehnen`, `diffuse_beschwerden`, `plantarfasciitis`). Struktur: `{ label, diagnoseText, lokBeschwerden, konservativ[], befunde[{id,pos,neg} | {id,input:true,…}], opMethoden[], bildBefunde, literatur }`. Das Menü wird aus `Object.keys(DIAG)` generiert.
- **`OPS`** (~4280): ~43 OP-Methoden `{ k, b, r, t }` = Kurzname, Beschreibung (Brieftext), Risiken, Technik. Keys wie `chevron`, `lapidus`, `tep_infinity`, `subtalar_arthrodese` … — `DIAG[x].opMethoden` referenziert diese Keys.
- **`AUFKLAERUNG_MAP`**, **`PATIENT_EINGRIFF_MAP`** / **`PATIENT_VARIANTEN`**: verdrahten OP-Methoden mit Aufklärung und mit Fuss-Track-Deep-Links (QR).
- **`KONSERV`**, **`RISIKEN`**, **`RISIKEN_ENDO`**: Auswahllisten.
- **`AUFKLAERUNG_RISIKEN`** (~5183): Datenbasis des Aufklärungstools (`allgemein`, `gruppen`, `eingriffe{gruppe,kontext}`, `elektiv`).

### Erlösdaten / DRG (zentral!)
- **Erlösdaten-Block 2026** (~4450–4519, markiert `BEGIN/END ERLÖSDATEN 2026 — NICHT VON HAND EDITIEREN`): Single Source `Erloesdaten_2026_MASTER.xlsx`. Enthält `window._ERLOES_META` (u. a. `lbfw` = Landesbasisfallwert 4562 €), `window._DRG` (Fuß-/OSG-DRGs: bwr, ugvd, mvwd, mvd, inekImpl, pflegeProTag, InEK-Fallkosten-Aufschlüsselung), `window._HDRG` (Hybrid-DRG-Pauschalen), `window._KURZ` (Kurzlieger-Schätzwerte). Helper: `window._E(code)` = Erlös aus CM×LBFW, `window._fx(text)` schreibt €-Beträge in Hinweistexten zur Laufzeit aus diesem Block um. **Jahres-Update = kompletten Block ersetzen, nie mischen; Einzelwerte nie von Hand ändern.**
- **`FUSS_DRG`**: zur Laufzeit aus `window._DRG`/`window._HDRG` abgeleitet (keine eigene Datenquelle).
- **`OP_STEUERUNG`** (~5308): pro OP-Methode die Abrechnungslogik `{ hdrg, drg, impl, empf (amb/stat/both), hebel/hebelName, kontext[], aufwertung{ziel,triggers}, ausschluss{triggers}, hinweise[] }` — Herzstück der Erlös-Beratung im Sprechstundenbrief.
- **`ENDO_DRG`** (~4420), **`ENDO_KONSTELLATIONEN`** (~4541), **`ENDO_ZE`**, **`ENDO_*_IMPL`**-Blöcke (~4784 ff.): Endoprothetik (Hüfte/Knie) mit ICD+OPS+DRG-Pfaden und Implantatpreisen.
- **`EINZELPREISE`** (~4624): Implantat-/Material-Einzelpreise für die Materialkosten-Blöcke; **`INEK_IMPL`**, **`UGVD_ABSCHLAG`**, **`ME_REGIONEN`** (Metallentfernung), **`OPS_LABELS`** (~4960).

### OP-Texte (OP-Bericht Generator)
- **`const T`** (~7010): ausformulierte Fuß-OP-Texte pro Eingriff (z. B. `tep_vantage_standard`). Innerhalb von `OPBerichtApp` sind je Sektion Eingriffs-Kataloge definiert: `UC_EINGRIFFE`/`UC_TEXT_MAP` (~7955/8109), `ENDO_EINGRIFFE` (~8047), `WS_EINGRIFFE` (~8093). Je Eingriff verdrahtet: Material (`P(name,lieferant,preis)`), ICD (`codes.push`), OPS (`o.push`), CM-Kandidaten, OP-Text, Reset.

### Referenz-Inhalte
- **`KLASSIFIKATIONEN`** (~10189), **`ROENTGEN`** (~11099), **`MESSMETHODEN`** (~11200), **`COALITIO_BEFUNDE`**, `MANUALE`-Liste in `OPManuale` (~10108).

## Wichtige Regeln

- **UNVERÄNDERLICHKEIT DER ABRECHNUNGSDATEN (oberste Regel):** Alle Abrechnungs- und Katalogdaten — OPS-Codes, ICD-Codes, DRG-Zuordnungen, Bewertungsrelationen, Pauschalen, Preise, Verweildauern (uGVD/mGVD/oGVD), InEK-Kostenwerte — sind behördlich bzw. vertraglich festgelegt und folgen KEINER inneren Logik. Sie dürfen niemals korrigiert, vereinheitlicht, ergänzt, umformatiert oder aus Mustern abgeleitet werden. Scheinbare Inkonsistenzen (Lücken in Code-Reihen, uneinheitliche Suffixe, „unplausible" Beträge) sind kein Fehler, sondern Katalogrealität. Beim Verschieben/Auslagern solcher Daten werden alle Werte exakt 1:1 übernommen und anschließend Wert für Wert gegen den alten Stand verglichen.
- **Kodierung ist deutsch:** ICD-10-GM und G-DRG/Hybrid-DRG. Der verbundene ICD-10-Connector (MCP) liefert US-ICD-10-CM/PCS und passt NICHT 1:1 — nur als grobe Orientierung, nie ungeprüft übernehmen.
- Die zwei „NICHT VON HAND EDITIEREN"-Blöcke (Katalogdaten, Erlösdaten) nur als Ganzes aus den Master-Excel-Dateien ersetzen.
- Medizinische Textänderungen: erst recherchieren (PubMed, mit PMID/DOI), dann Vorschlag zur Freigabe — nie stillschweigend genehmigte Texte überschreiben.
- Schreibstil (auch für Aufklärungs-/Patiententexte): Fließtext statt Label-Bullets, keine rhetorischen Fragen, keine stilistischen Doppelpunkte, deutsche Anführungszeichen „…", schwierige Begriffe kurz in Klammern erklären. ICD-Codes gehören in die klinischen Tools, nie in Patiententexte.

## Workflow für Änderungen

1. **Ändern** in `index.html` (bzw. Vorschlag zur Freigabe bei medizinischem Inhalt).
2. **Validieren:**
   - JSX: `text/babel`-Block extrahieren und mit Babel transpilieren (Node + `@babel/standalone`, z. B. `../Fuss-Track/lib/babel.min.js` — dieses Repo hat keinen `lib/`-Ordner, React/Babel kommen zur Laufzeit vom unpkg-CDN).
   - JSON (`bausteine.json` falls berührt): parsen.
   - Referenzen prüfen: jeder Key in `DIAG[x].opMethoden` existiert in `OPS`; `OP_STEUERUNG`-/`AUFKLAERUNG_MAP`-Keys passen zu `OPS`; DRG-Codes existieren in `window._DRG`/`window._HDRG`.
3. **Live-Preview:** über den Dev-Server mit Live-Reload (siehe unten) unter `http://localhost:8000/index.html`.
4. **Deploy:** Der Autor lädt die Datei(en) manuell auf GitHub hoch — am Ende immer die exakt zu deployenden Dateien benennen.

## Lokaler Dev-Server (Standard bei jeder Arbeitssitzung)

Zu Beginn jeder Arbeitssitzung wird standardmäßig der Live-Reload-Dev-Server gestartet:

```
python3 scripts/dev-server.py
```

- **Adresse: `http://localhost:8000/index.html`** — der Browser lädt bei jeder Dateiänderung im Repo automatisch neu (Polling auf `/__livereload`, .git ausgenommen), Caching ist deaktiviert.
- Kein Node.js nötig (auf diesem Rechner nicht installiert); das Skript ist reine Python-Standardbibliothek. Als JS-Runtime für Prüfskripte dient macOS-`jsc` (`/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc`).
- In Claude-Code-Sitzungen: Server per Bash im Hintergrund starten (die `.claude/launch.json`-Preview-Integration scheitert an macOS-Berechtigungen für den Desktop-Ordner); vor dem Start prüfen, ob Port 8000 schon belegt ist.
- **Achtung Injektionsfalle:** index.html hat KEIN schließendes `</body>`-Tag (Datei endet mitten im Markup); das einzige `</body>` der Datei liegt in einem JS-String (Word-Export, ~Zeile 6135). Der Dev-Server hängt sein Snippet deshalb ans Dateiende an — niemals an `</body>`-Fundstellen injizieren.
