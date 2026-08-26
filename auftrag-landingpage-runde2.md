# Auftrag: Landingpage, zweite Runde

Die Screenshots sind drin und wirken. Vier Änderungen.

## 1. Bilder größer, einheitlich, einzeln

Bisher steckten zwei Handyansichten in einem Querbild. Auf dem Telefon wird daraus je Ansicht ein Streifen von rund 85 Pixeln Breite — man erkennt, dass da eine App ist, aber nichts mehr davon.

Neu liegen im Repo **einzelne Bilder, eines je Ansicht**, alle im selben Format 1080 × 1350 (4 : 5), dazu je eine 640er-Fassung. Sie sind Ausschnitte, keine verkleinerten Vollbilder: Man liest die Beschriftungen.

Anzeige als **swipebarer Streifen**: ein Bild sichtbar, seitlich wischen zum nächsten. Umsetzung ohne Bibliothek:

```css
.streifen{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;
          -webkit-overflow-scrolling:touch;scrollbar-width:none}
.streifen::-webkit-scrollbar{display:none}
.streifen > figure{flex:0 0 100%;scroll-snap-align:center;margin:0}
.streifen img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:10px}
```

Darunter Punkte als Positionsanzeige (so viele Punkte wie Bilder, der aktive in Petrol). Auf Bildschirmen ab 900 px dürfen zwei Bilder nebeneinander stehen (`flex:0 0 calc(50% - 6px)`), dann entfallen die Punkte.

Wichtig: `aspect-ratio:4/5` fest setzen, damit alle Bilder gleich hoch sind und beim Laden nichts springt. `loading="lazy"` außer beim ersten Streifen.

### Zuordnung

| Abschnitt | Bilder in dieser Reihenfolge |
|---|---|
| Sprechstundenbrief in Minuten | `sb-1-eingabe`, `sb-2-untersuchung` |
| OP-Berichte, die Kodierung und Erlös mitdenken | `ob-1-auswahl`, `ob-2-vorschau` |
| Ambulant oder stationär, vor der Entscheidung sichtbar | `fs-1-chevron`, `fs-2-tn` |
| Klassifikationen mit Quelle | `kl-1-liste`, `kl-2-wagner` |
| OP-Anleitungen und Röntgenmessungen | `rx-1-meary` |
| Abrechnungswissen, jährlich gepflegt | `ops-1-suche` |
| Patienten-App (neuer Abschnitt, siehe Punkt 3) | `pat-1-start`, `pat-2-verlauf`, `pat-3-wegweiser` |

Alle Dateien in `bilder/screens/`, Namensschema `<name>.webp` und `<name>-640.webp`.

Die bisherigen Doppelbilder (`clinic-sprechstundenbrief.webp` und so weiter) werden nicht mehr eingebunden. Sie bleiben im Repo, weil sie für Vortrag und LinkedIn taugen; `bilder/screens/UEBERSICHT.md` weist sie entsprechend aus.

## 2. Das nachgebaute Beispiel oben ersetzen

Im Hero steht die Attrappe „OP-Bericht · Arthrodese MTP I" mit „Baustein 12", „Baustein 31" und einer Erlös-Simulation, die „— €" anzeigt. Als einziges Bild auf der Seite war das in Ordnung. Neben echten Screenshots wirkt es wie ein Platzhalter, und die leere Erlöszeile weckt genau die Frage, die das Werkzeug beantworten soll.

Ersetzen durch `menue-1.webp` — das Hauptmenü mit den acht Werkzeugen. Es zeigt in einem Bild den ganzen Umfang und ist echt. Der Rahmen und die Bildunterschrift „Beispieldarstellung … Kataloge des jeweiligen Jahres" entfallen mit der Attrappe.

Falls das Hero dadurch zu leer wirkt, ist die Alternative `ob-2-vorschau.webp` (fertiger Berichtstext mit Materialsumme und Word-Export) — der zeigt das Ergebnis statt des Menüs.

## 3. Neuer Abschnitt direkt nach dem Sprechstundenbrief

Überschrift: **Ihre Patienten bekommen die Begleitung dazu.**

Text: „Jeder Brief und jede Aufklärung aus Fuss-Track Clinic trägt einen QR-Code, der direkt zur passenden Stelle der Patienten-App führt: tagesgenaue Begleitung vom Vorbereitungstermin bis drei Monate nach dem Eingriff, verständliche Informationen zu Krankheitsbild und Verfahren, alles mit Quellen belegt. Wer noch keine Diagnose hat, kann sich über den Beschwerde-Wegweiser an mögliche Ursachen herantasten. Die Patienten-App ist kostenlos, werbefrei, ohne Konto und ohne Datensammlung, und sie bleibt es."

Darunter der QR-Code `bilder/screens/qr-patienten-app.png`, Anzeigegröße 140 px, daneben:

> **patienten.fuss-track.de**
> Scannen oder antippen — kein App-Store, keine Anmeldung.

Der QR-Code wird zugleich mit einem Link auf `https://patienten.fuss-track.de` hinterlegt (`target="_blank"`, `rel="noopener"`), damit er am Telefon, wo niemand den eigenen Bildschirm scannt, trotzdem funktioniert. `alt="QR-Code zur Patienten-App unter patienten.fuss-track.de"`.

Der Abschnitt wird optisch abgesetzt, zum Beispiel mit `var(--op-tint)` als Fläche, damit erkennbar ist: hier ist von der zweiten Anwendung die Rede.

## 4. Gegenprobe

Bei 390 px Breite: ein Bild füllt die Breite, Wischen führt sauber zum nächsten, die Punkte zeigen die Position, nichts springt beim Laden. Bei 1280 px: zwei Bilder nebeneinander, keine Punkte. Netzwerk-Tab: nur lokale Dateien. Der QR-Code wird mit einem Telefon vom Bildschirm gescannt und muss auf `patienten.fuss-track.de` landen.

Deploy: nur `index.html` und die Bilder, kein Bucket-Upload.

## 5. Noch offen aus `auftrag-ebm-hinweis.md`

Die beiden Landingpage-Punkte aus dem EBM-Auftrag sind noch nicht umgesetzt. Sie gehören in dieselbe Runde, weil `index.html` ohnehin angefasst wird.

**a) Ein Satz im Fallsteuerungs-Block.** Der Absatz endet heute mit „… steht dabei, bevor der Eingriff geplant wird." Direkt daran anschließen:

> „Gerechnet werden die stationären DRG und die Hybrid-DRG, also genau die Wege, an denen sich die Ambulantisierung entscheidet. Die vertragsärztliche Abrechnung nach EBM bildet Fuss-Track Clinic nicht ab."

**b) Ein FAQ-Eintrag**, ans Ende der Fragen zum Funktionsumfang:

> **Ist die EBM-Abrechnung enthalten?**
> Nein. Die Erlössimulation rechnet mit den stationären DRG und den Hybrid-DRG. Für Leistungen, die ambulant über den EBM vergütet werden, zeigt die Fallsteuerung deshalb keinen Betrag. Das ist bewusst so: Der EBM ist eine eigene Welt mit eigenen Regeln, und ein halb gepflegter EBM-Teil wäre schlechter als keiner.

Die dritte Aufgabe aus jenem Auftrag — die EBM-Zeile in `app.html` — bleibt davon unberührt und wird dort erledigt.

## 6. Der Knopf „30 Tage kostenlos testen" — entschieden

Rückmeldung aus der Prüfung: Beide Knöpfe springen auf `#preis`, dort steht bei `VERKAUF_AKTIV = false` kein Preis, kein Kauf-Knopf, kein Paddle-Skript, sondern die Interessenten-Zeile und „Testzugang anfragen" als Mailto. Es passiert also nichts Falsches.

Die Reibung bleibt trotzdem: Der Knopf verspricht Selbstbedienung, und wer ihn drückt, landet bei „erscheint im Herbst 2026". Auf dem Kongress, wo Kollegen daneben stehen und mitschauen, ist das der unangenehmere Moment. Benjamin hat entschieden:

1. **Beide Knöpfe umbeschriften** auf „Testzugang anfragen". Sprungziel `#preis` bleibt, dort steht dann genau das, was der Knopf ankündigt.
2. **Das Leistungsversprechen bleibt stehen**, aber im Zielabschnitt: „30 Tage kostenlos, ohne Zahlungsdaten" ist wahr und ein gutes Argument, es ist nur nicht selbst auslösbar. Es gehört deshalb dorthin, wo der Weg erklärt wird, nicht auf den Knopf.
3. **Die freistehende Leistungszeile** „30 Tage kostenlos testen — ohne Zahlungsdaten" weiter oben wird an denselben Schalter gehängt wie Preis und Kauf-Block. Bei `VERKAUF_AKTIV = true` erscheint sie wieder, zusammen mit der Kaufstrecke.

Damit ist der Livegang weiterhin eine Ein-Wort-Änderung: Schalter auf `true`, und Knopftexte wie Leistungszeile kehren in die Verkaufsfassung zurück. Die beiden Knopfbeschriftungen deshalb ebenfalls über den Schalter steuern, nicht fest eintragen.

### 6.4 Nachtrag: der Wortlaut der Interessenten-Zeile

Die Prüfung hat einen Widerspruch in meinem eigenen Auftrag aufgedeckt, zu Recht: Punkt 6.2 sagt, das Leistungsversprechen bleibe im Zielabschnitt stehen, Punkt 6.3 hängt die einzige Zeile mit diesem Wortlaut an den Schalter. Bei `VERKAUF_AKTIV = false` verschwand es damit ganz. Die Absicht war die andere, das Versprechen soll sichtbar bleiben. Es fehlte nur der Ort.

Die Interessenten-Zeile bekommt ihn. Neuer Wortlaut, er ersetzt die bisherige Fassung aus `auftrag-interessenten-zeile.md`:

> **Fuss-Track Clinic erscheint im Herbst 2026.**
> Der Testzugang läuft dann 30 Tage, kostenlos und ohne Zahlungsdaten. Interesse? Schreiben Sie an kontakt@fuss-track.de, dann erhalten Sie Bescheid, sobald es losgeht.

Das „dann" ist wichtig: Es bindet das Versprechen an den Herbst und sagt damit richtig, dass es heute noch keinen Selbstbedienungs-Test gibt. Die Mailadresse bleibt Mailto-Link mit dem Betreff „Testzugang Fuss-Track Clinic".

### 6.5 Bildgewicht bleibt wie es ist

`ob-2-vorschau.webp` ist mit 102 KiB der größte Einzelposten. Das bleibt so. Es ist das textreichste Bild der Seite, der fertige Berichtstext ist dort der eigentliche Inhalt, und stärkere Kompression würde genau die Buchstaben verwaschen, wegen derer das Bild überhaupt gezeigt wird. Bei verzögertem Laden fällt das Gewicht ohnehin nur an, wenn jemand bis dorthin scrollt.
