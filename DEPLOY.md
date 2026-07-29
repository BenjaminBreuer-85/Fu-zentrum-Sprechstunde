# DEPLOY.md — Was gehört wohin

Die App lädt ihre Daten aus **zwei getrennten Quellen**. Wer nur eine davon aktualisiert, bekommt eine kaputte Live-Seite. Diese Liste verhindert das.

| Quelle | Inhalt | Wie aktualisieren |
|---|---|---|
| **GitHub-Repo** (Push) | Programmcode, Schriften, Bibliotheken, Rechtstexte, Standard-Materialsatz | GitHub Desktop → Commit → Push |
| **Supabase-Bucket** `toolbox-data` (Upload) | die zehn lizenzpflichtigen Inhaltsdateien | Dashboard → Storage → Datei überschreiben |

**Merksatz:** Alles, was Preise, Katalogdaten oder ausformulierte Inhalte enthält, gehört in den Bucket. Alles andere ins Repo.

---

## A) Dateien im Repo (Push)

| Datei / Ordner | Zweck |
|---|---|
| `index.html` | Öffentliche Landingpage |
| `app.html` | Die App (Hülle, Loader, alle Komponenten) |
| `impressum.html`, `datenschutz.html`, `agb.html`, `widerruf.html` | Rechtstexte |
| `landing.html` | Produktseite (Vorstufe, noindex) |
| **`zuordnung/implantat_zuordnung.json`** | **Standard-Materialsatz** — enthält keine Preise, keine Marken, keine Artikelnummern und darf deshalb öffentlich liegen |
| `lib/` (5 Dateien) | React, ReactDOM, Babel, supabase-js, xlsx-js-style — lokal statt CDN |
| `fonts/` (7 Dateien) | Source Serif 4, IBM Plex Sans/Mono (woff2) |
| `icons/` (6 Dateien) | Favicon, App-Icon, Logo-Quelle |
| `CNAME` | Custom Domain `fuss-track.de` — **niemals löschen** |
| `scripts/`, `*.md` | Werkzeuge und Dokumentation |

**Nicht im Repo** (steht in `.gitignore`): `data/` und `meine-preise/`.

## B) Dateien im Supabase-Bucket `toolbox-data` (Upload)

Genau zehn Dateien, Namen exakt wie hier:

```
katalog2026.json    erloes2026.json    diagnosen.json     opmethoden.json
opsteuerung.json    endo.json          preise.json        optexte.json
aufklaerung.json    referenz.json
```

Der Bucket ist privat; gelesen wird nur mit gültigem Login (Row Level Security).

---

## C) Reihenfolge beim Deployen

Damit die Live-Seite **keine Sekunde bricht**, gilt: **erst Bucket, dann Push.**

1. **Bucket-Upload zuerst.** Neue Inhaltsdateien hochladen. Die alte App-Version im Netz liest sie noch nicht — es passiert also nichts.
2. **Kurz prüfen.** Storage-Ansicht: Sind alle zehn Dateien da, Zeitstempel aktuell?
3. **Dann Push.** Erst jetzt geht der neue Code live, der die neuen Daten erwartet.

Andersherum (erst Push) entsteht ein Zeitfenster, in dem der neue Code alte Daten liest — genau so entstand die Panne vom 29.07.2026.

**Ausnahme:** Ändert sich nur Code (Oberfläche, Texte in `app.html`), genügt der Push. Ändert sich nur Inhalt, genügt der Upload.

---

## D) Offener Upload-Stand (Stand 29.07.2026)

Diese **sieben** Dateien wurden nach dem letzten Bucket-Upload geändert und müssen **vor dem nächsten Push** hochgeladen werden:

| Datei | Was sich geändert hat |
|---|---|
| `diagnosen.json` | Kennung `t2_nagel` → `arthrodesenagel_retro` |
| `aufklaerung.json` | dieselbe Umbenennung, Markennamen entfernt |
| `opmethoden.json` | dieselbe Umbenennung, Prothesennamen generisch |
| `opsteuerung.json` | dieselbe Umbenennung, alle Paketpreise entfernt |
| `optexte.json` | dieselbe Umbenennung, `{IMPL:…}`-Platzhalter, Markennamen entfernt |
| `endo.json` | Implantatlisten generisch, Preise entfernt |
| `preise.json` | `EINZELPREISE` geleert, UC-Implantate generisch |

Unverändert und **nicht** neu hochzuladen: `katalog2026.json`, `erloes2026.json`, `referenz.json`.

> **Warum das zusammengehört:** Die Kennung `arthrodesenagel_retro` steht sowohl in `zuordnung/implantat_zuordnung.json` (Repo) als auch in fünf Bucket-Dateien. Passt eines nicht zum anderen, zeigt die App beim Start eine Warnung mit den betroffenen Kennungen.

---

## E) Wenn doch etwas fehlt

Die App nennt Datei und erwarteten Ort:

- „Erwartet im Repository unter …" → Datei fehlt im Push
- „Erwartet im Supabase-Bucket …" → Datei fehlt im Upload
- „DATEN-WARNUNG: n Kennung(en) … fehlen in data/opsteuerung.json" → Repo und Bucket sind nicht auf demselben Stand

## F) Jahres-Update (z. B. Katalog 2027)

1. Neue `katalog2026.json` / `erloes2026.json` aus den Master-Excel-Dateien erzeugen (1:1-Regel beachten, siehe CLAUDE.md).
2. Lokal testen: `python3 scripts/dev-server.py`, dann `http://localhost:8000/app.html`.
3. Dateien im Bucket ersetzen. Kein Push nötig, solange sich der Code nicht ändert.
