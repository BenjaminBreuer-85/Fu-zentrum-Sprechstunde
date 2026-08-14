# Auftrag an die Clinic-Code-Sitzung: OPS-Einträge Weil / Achilles-Tendoskopie / AS-Débridement

Stand 14.08.2026, aus der Inhalts-Sitzung (Cowork). Ziel: Für drei Eingriffe mit fertigen
Patienten-Artikeln und Begleitern fehlt der Weg über den Sprechstundenbrief/OP-Bericht.
Die DATEN-Seite (data/opmethoden.json) ist bereits vorbereitet — dort existieren jetzt die
Einträge `weil`, `as_tendoskopie`, `as_debridement` in OPS (k/b/r/t) und
PATIENT_EINGRIFF_MAP (weil→weil, as_tendoskopie→tendoskopie_achilles,
as_debridement→achilles_nekrose). Bitte NICHT neu anlegen, nur die index.html-Seite
nachziehen.

## 1. Weil-Osteotomie (Schlüssel `weil`)

- **OPS-Ziffern: exakt identisch mit der DMMO** (gleicher Osteotomie-Code je Metatarsale),
  **zusätzlich `5-93b.0` je Metatarsale** für die Twist-Off-Schraube (Osteosynthese durch
  resorbierbares/spezielles Material — pro versorgtem Strahl einmal ansetzen, analog zur
  Mehrstrahl-Logik der DMMO).
- OP-Bericht-Generator: Weil als eigene Auswahl neben der DMMO (Strahl-Auswahl II–V wie
  DMMO übernehmen); Textbaustein liegt in opmethoden.json (`t`).
- Erlös/Hybrid-DRG: aus der DMMO-Konstellation ableiten; die zusätzliche 5-93b.0 prüfen.

## 2. Achillessehnen-Tendoskopie (Schlüssel `as_tendoskopie`)

- **OPS-Ziffern: OFFEN — Platzhalter/TODO anlegen**, Benjamin trägt nach.
- Struktur komplett bauen: Auswahl im Brief + OP-Bericht, QR-Ziel
  `?op=tendoskopie_achilles` (Artikel freigegeben, Begleiter mit einer Variante
  „Standard", ambulant-Default).

## 3. AS-Débridement bei Tendinose (Schlüssel `as_debridement`)

- **OPS-Ziffern: OFFEN — Platzhalter/TODO anlegen**, Benjamin trägt nach.
- QR-Ziel `?op=achilles_nekrose` (Artikel „Débridement der Achillessehne bei Tendinose",
  freigegeben; Begleiter mit Varianten „Débridement mit Refixation" / „mit FHL-Transfer").

## Hinweise

- Die Varianten-Chips im QR-Block kommen automatisch aus PATIENT_VARIANTEN (liegt bereits
  in data/opmethoden.json: weil einfach/komplex, tendoskopie_achilles Standard,
  achilles_nekrose zwei Varianten).
- data/opmethoden.json ist gitignored → nach jedem Stand zusätzlich in den
  Supabase-Bucket `toolbox-data` laden.
- Die von der Inhalts-Sitzung angelegten k/b/r/t-Texte (Kurzname, Aufklärungs-Beschreibung,
  Risiken, OP-Text) sind Entwürfe — bei der Umsetzung von Benjamin gegenlesen lassen.

## 4. Coalitio-TC: Datenwiderspruch behoben (nur Verifikation nötig)

Der Basis-OP-Text von `coalition_exzision` in data/opmethoden.json nannte eine
„Calcaneus-Korrekturosteotomie", obwohl die Basis-Konstellation (DRG I27D) OHNE
Osteotomie kalkuliert ist. Benjamins Entscheidung: **Standard ohne Osteotomie, optional
mit** — der Basistext lautet jetzt „Exzision der Koalition mit Faszien-Fett-Interponat";
die Osteotomie läuft ausschließlich über die bestehenden Modifikatoren „+ LCOT"
(I20C, OPS 5-781.4t + 5-784.7t) bzw. „+ LCOT, Alter unter 12" (I20B) in
data/opsteuerung.json, deren textErsatz die Osteotomie nennt. In index.html bitte nur
verifizieren, dass die Modifikator-Kette im OP-Bericht-Generator und der Erlös-Hinweis
sauber greifen — Daten-Seite ist fertig.
