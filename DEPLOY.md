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
| `manifest.json` | Web-App-Manifest (Homescreen startet in `app.html`) |
| `404.html` | Auffang- und Kurzlink-Router (`/i/<id>`) — wirkt nur live |
| `kurzlinks.json` | ID-Tabelle der Kurzlinks; IDs nur ergaenzen, nie aendern |
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

## D) Upload-Stand

**Stand 01.08.2026: ZWEI Bucket-Uploads OFFEN.**

`data/opmethoden.json` — enthaelt (a) den Stand vom 31.07.: PATIENT_EINGRIFF_MAP
von 6 auf 43 Eintraege, neue PATIENT_DIAGNOSE_MAP; (b) den Stand vom 01.08.: neue
OP-Methode `youngswick` (44 gesamt), PATIENT_DIAGNOSE_MAP auf 14 Eintraege
(`hallux_valgus` und `hallux_limitus` ergaenzt, `hallux_rigidus` von der Frueh-
form auf das eigene Krankheitsbild korrigiert).

`data/diagnosen.json` — neue Diagnose `hallux_limitus` (16 gesamt).

**Reihenfolge beachten: erst Upload, dann Push.** Die neuen Kurzlinks in
`kurzlinks.json` (Repo) verweisen auf Ziele, welche die App erst kennt, wenn die
neuen Dateien im Bucket liegen. Betroffen sind diesmal `hallux-valgus`,
`hallux-rigidus` und `youngswick`.

**Hinweis zu `youngswick`:** Der Eingriff hat bewusst noch keinen Eintrag in
`data/opsteuerung.json` — H-DRG/DRG sind Abrechnungsdaten und werden nicht
abgeleitet, sondern nur uebernommen. Bis sie nachgetragen sind, erscheint der
Eingriff im Sprechstundenbrief, aber nicht in der Erloessimulation. Das ist
derselbe Zustand wie bei `morton_neurom`, `peroneal_rek` und `peroneal_lux`.
Die DATEN-WARNUNG loest das nicht aus, weil sie ueber `MAPPING_OPS` prueft.

**Offen ist dagegen ein einmaliger SQL-Befehl in Supabase.** Die Funktion
„Implantat anlegen" speichert eine Sektion je Position und braucht dafuer eine
neue Spalte. SQL Editor → New query → ausfuehren:

```sql
alter table public.implantatpreise add column if not exists sektion text;
```

Reihenfolge egal: die App laeuft auch ohne die Spalte weiter und speichert dann
nur die Sektion nicht mit (Hinweis in der Browser-Konsole). Details in
`SUPABASE_SETUP.md`.

Diesen Abschnitt bei der naechsten Aenderung wieder fuellen: Welche Datei wurde
geaendert, was steht drin, und ob sie ins Repo oder in den Bucket gehoert.
Pruefen laesst sich das jederzeit mit den Zeitstempeln:

```bash
cd data && ls -lT *.json | awk '{print $9, $6, $7, $8}'
```

> **Warum das zusammengehoert:** Die Kennung `arthrodesenagel_retro` steht sowohl in
> `zuordnung/implantat_zuordnung.json` (Repo) als auch in fuenf Bucket-Dateien.
> Passt eines nicht zum anderen, zeigt die App beim Start eine Warnung mit den
> betroffenen Kennungen.

---

## D2) Kurzlinks /i/<id> — Gegenprobe erst LIVE

Die Weiterleitung `fuss-track.de/i/<id>` laeuft ueber `404.html`. GitHub Pages
liefert diese Datei bei unbekannten Pfaden aus — **lokal tut der Dev-Server das
nicht**. Die Funktion laesst sich deshalb erst nach dem Push pruefen, nie vorher.

Nach jedem Push, der `404.html` oder `kurzlinks.json` beruehrt, diese drei
Adressen im Browser aufrufen:

| Adresse | Erwartung |
|---|---|
| `https://fuss-track.de/i/chevron` | leitet sofort in die Patienten-App weiter |
| `https://fuss-track.de/i/quatsch` | „Dieser Link ist nicht mehr gueltig" + Link zur Patienten-App |
| `https://fuss-track.de/tippfehler` | normale „Seite nicht gefunden" + Link zur Startseite |

**Regel zu den IDs:** Eine einmal vergebene ID wird nie geaendert und nie
wiederverwendet — sie steht in bereits ausgehaendigten Arztbriefen. Details im
Kopf von `kurzlinks.json`.

Beide Dateien gehoeren ins **Repo** (Push), nicht in den Bucket.

## E) Wenn doch etwas fehlt

Die App nennt Datei und erwarteten Ort:

- „Erwartet im Repository unter …" → Datei fehlt im Push
- „Erwartet im Supabase-Bucket …" → Datei fehlt im Upload
- „DATEN-WARNUNG: n Kennung(en) … fehlen in data/opsteuerung.json" → Repo und Bucket sind nicht auf demselben Stand

## F) Jahres-Update (z. B. Katalog 2027)

1. Neue `katalog2026.json` / `erloes2026.json` aus den Master-Excel-Dateien erzeugen (1:1-Regel beachten, siehe CLAUDE.md).
2. Lokal testen: `python3 scripts/dev-server.py`, dann `http://localhost:8000/app.html`.
3. Dateien im Bucket ersetzen. Kein Push nötig, solange sich der Code nicht ändert.
