# Auftrag: Rückweg „Zum Krankheitsbild" OP-abhängig machen (kbinfo)

**Datei:** `app.html` (Sprechstundenbrief, Block „EIN CODE PRO PATIENT", ca. Zeile 1585–1635)
**Daten:** `data/opmethoden.json` — neue Map `PATIENT_EINGRIFF_KB_MAP` liegt bereits lokal vor (Bucket-Upload offen, siehe DEPLOY.md D)
**Anlass (03.09.2026):** Diagnose „Läsion der Peronealsehnen" mit OP „Peronealsehnennaht" erzeugt den QR-Link `?op=peroneal_riss&…&kbinfo=peroneal_luxation_kb`. In der Patienten-App steht dann über der OP-Aufklärung „← Zum Krankheitsbild: Peronealsehnen-Luxation", obwohl das Krankheitsbild der Riss ist (`ptr_kb`). Ursache: `kbinfo` kommt ausschließlich aus `PATIENT_DIAGNOSE_MAP[diagnose]`, und die Diagnose `peronealsehnen` deckt Riss und Luxation gemeinsam ab.

## Änderung

1. Map laden, gleicher Fallback wie bei den bestehenden Maps:
   ```js
   const PATIENT_EINGRIFF_KB_MAP = window._DATA.opmethoden.PATIENT_EINGRIFF_KB_MAP || {};
   ```
2. `kbArtikel` bestimmen: Im OP-Weg hat der Eintrag des gewählten Eingriffs Vorrang, im konservativen Weg bleibt die Diagnose maßgeblich. Dazu `opWeg` vor `kbArtikel` berechnen (`opWeg` hängt nicht von `kbArtikel` ab, die Zeilen nur umstellen):
   ```js
   var opGewaehlt = opMethode.filter(function(m) { return OPS[m]; }).length > 0;
   var opWeg = !nurDiagnostik && opEmpfohlen && opGewaehlt && !!aufActive;
   var kbArtikelDiag = diagActive ? PATIENT_DIAGNOSE_MAP[diagActive.key] : "";
   var kbArtikel = (opWeg && PATIENT_EINGRIFF_KB_MAP[aufActive.key]) || kbArtikelDiag;
   ```
3. Abhängigkeitsliste des `qr`-Memos unverändert (`kbArtikel` ist bereits drin).

## Gegenprobe

| Diagnose | OP-Methode | erwarteter QR-Link |
|---|---|---|
| Läsion der Peronealsehnen | Peronealsehnennaht (`peroneal_naht`) | `?op=peroneal_riss&modus=aufklaerung&kbinfo=ptr_kb` |
| Läsion der Peronealsehnen | Peronealsehnen-Rekonstruktion (`peroneal_rek`) | `?op=peroneal_riss&modus=aufklaerung&kbinfo=ptr_kb` |
| Läsion der Peronealsehnen | Peronealsehnen-Stabilisierung (`peroneal_lux`) | `?op=peroneal_instab&modus=aufklaerung&kbinfo=peroneal_luxation_kb` |
| Läsion der Peronealsehnen | keine OP / konservativ | `?op=peroneal_luxation_kb&modus=aufklaerung&thema=kb_plux_konservativ` (unverändert) |
| Hallux valgus | Chevron | unverändert (`kbinfo=hallux_valgus`) |

## Deploy

Nur `app.html` (Repo, Push). Die Datenänderung an `data/opmethoden.json` ist bereits eingetragen; **Bucket-Upload `opmethoden.json` offen** (DEPLOY.md D). `kurzlinks.json` ist ebenfalls schon angepasst (kbinfo an peroneal-riss und peroneal-instab), keine weitere Änderung nötig.
