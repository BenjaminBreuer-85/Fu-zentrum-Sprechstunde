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
| `impressum.html`, `datenschutz.html`, `nutzungsbedingungen.html` | Rechtstexte |
| `zugang.html` | Zwischenseite für Einladungs- und Passwort-Links. Löst den Token **erst auf Knopfdruck** ein, damit Mail-Scanner ihn nicht vorab verbrauchen. Muss zusammen mit den E-Mail-Vorlagen aus `supabase/vorlagen/` live gehen — die Vorlagen verweisen darauf |
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

**Stand 26.08.2026: EIN UPLOAD OFFEN, VIER DATEIEN UNGEKLÄRT.**

Diese Dateien im Ordner `data/` wurden nach dem letzten dokumentierten Upload (01.08.2026) lokal geändert. Ob sie seither in den Bucket gewandert sind, ist **nicht dokumentiert**. Vor dem nächsten Deploy klären:

| Datei | lokal geändert | Anlass |
|---|---|---|
| `diagnosen.json` | 22.08.2026 | KONTROLLE_V2, Sortierung der Diagnosen |
| `referenz.json` | 18.08.2026 | Messmethoden und Klassifikationen |
| `opmethoden.json` | 15.08.2026 | — |
| `opsteuerung.json` | 15.08.2026 | — |
| `optexte.json` | **26.08.2026** | Achilles- und Weil-Texte (18.08.) sowie fünf neue Schlüssel `df_*` für den diabetischen Fuß — **muss hochgeladen werden** |

So wird geklärt, ob eine Datei im Bucket aktuell ist: Datei aus dem Dashboard herunterladen und zeichengenau mit der lokalen vergleichen. Der Blick auf den Zeitstempel in der Storage-Ansicht genügt nicht, weil er nur sagt, wann zuletzt hochgeladen wurde, nicht was drinsteht.

**Richtung merken:** Der lokale Ordner `data/` ist die Quelle, der Bucket ist das Ziel. Geändert wird immer lokal, danach wird hochgeladen. Im Dashboard wird nie direkt bearbeitet. Ein altes Änderungsdatum an einer lokalen Datei heißt deshalb nur, dass seither niemand daran gearbeitet hat, nicht dass sie veraltet ist.

### Diese Liste wird gepflegt

Jede Änderung an einer der zehn Bucket-Dateien wird hier eingetragen, mit Datum und Anlass, und beim Upload wieder ausgetragen. Wer eine Bucket-Datei ändert, ohne diesen Abschnitt zu ergänzen, hinterlässt genau die Unklarheit, die oben steht.

Umgekehrt gilt für jeden Auftrag an eine Code-Sitzung: Er endet mit einer Deploy-Zeile, die ausdrücklich sagt, ob eine Bucket-Datei betroffen ist oder nicht. „Kein Bucket-Upload" ist eine Aussage, die dasteht, kein Weglassen.

### Erledigt am 01.08.2026

Drei Bucket-Dateien, alle hochgeladen:

- `data/opmethoden.json` — neue OP-Methode `youngswick` (44 gesamt);
  PATIENT_DIAGNOSE_MAP auf 14 Eintraege (`hallux_valgus` und `hallux_limitus`
  ergaenzt, `hallux_rigidus` von der Fruehform auf das eigene Krankheitsbild
  korrigiert).
- `data/diagnosen.json` — neue Diagnose `hallux_limitus`, `mittelfuss_arthrose`
  → `lisfranc_arthrose` umbenannt (16 gesamt).
- `data/opsteuerung.json` — Eintrag `youngswick`. Die Abrechnungssteuerung wurde
  auf Anweisung des Autors **wertgleich von `chevron` uebernommen** (hdrg I20O,
  drg I20E, Hebel 5-854.2c, Aufwertung I20N, gleiche Ausschluss-Trigger). Der
  Akin-Code 5-788.56, der `chevron` von `chevron_akin` unterscheidet, spielt hier
  keine Rolle — beide Eintraege sind ohnehin identisch. Der OPS-Code des
  Eingriffs steht bereits als `5-788.51` in `OPS_LABELS`.

Repo-Seite gepusht und live gegengeprueft: `app.html` byte-identisch mit lokal,
`kurzlinks.json` mit 53 IDs, D2-Gegenprobe fuer die drei neuen Kurzadressen
bestanden (siehe unten).

**Reihenfolge beachten: erst Upload, dann Push.** Die Kurzlinks in
`kurzlinks.json` (Repo) verweisen auf Ziele, welche die App erst kennt, wenn die
Datendateien im Bucket liegen.

**Netz seit 01.08.2026:** `PATIENT_DIAGNOSE_MAP`, `PATIENT_EINGRIFF_MAP` und
`PATIENT_VARIANTEN` fallen in `app.html` auf ein leeres Objekt zurueck. Wird
versehentlich vor dem Upload gepusht, entfallen nur die QR-Bloecke, statt dass
die App beim Start in einen TypeError laeuft. Das ersetzt die Reihenfolge nicht.

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

**Zuletzt geprueft am 01.08.2026** nach dem Push der drei neuen IDs — alle vier
Zeilen bestanden, zusaetzlich `fuss-track.de/i/hallux-valgus` und
`fuss-track.de/i/youngswick` (beide leiten korrekt in die Patienten-App weiter).
Live-Tabelle: 53 IDs.

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
