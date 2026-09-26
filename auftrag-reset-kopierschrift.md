# Auftrag Clinic: Zentraler Reset in der Kopfleiste beider Generatoren, Kopierschrift des Sprechstundenbriefs

Stand 26.09.2026, Cowork-Sitzung. Wunsch des Autors 26.09.2026: (1) Sprechstundenbrief und OP-Bericht brauchen oben einen zentralen Reset-Knopf, nicht nur die Resets je Abschnitt; (2) der kopierte OP-Bericht kommt in Word als Trebuchet MS 10 an, der kopierte Sprechstundenbrief nicht, so dass die Schrift jedes Mal umgestellt werden muss. Datei `app.html`, Ausgangsstand Commit 630e9a1 (795.757 Byte, 8a7be0cc…, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## 1. Befund Reset

Beide Generatoren haben schon einen Gesamt-Reset, aber an unauffälliger Stelle und beide unvollständig:

- Sprechstundenbrief: `resetAll()` (Z. 3354–3372), Knopf „🔄 Reset" im Kopf der Generator-Karte (Z. 3395), der beim Scrollen verschwindet. Die Funktion setzt 76 Zustände zurück; es fehlen 11 der 86 `_s`-Zustände der Komponente: `setAufVariante`, `setFreitextAnam`, `setKv2Anlass`, `setKv2Feld`, `setKv2OpDatum`, `setKv2Sel`, `setLapidusRezidiv`, `setQrAktiv`, `setZeAktiv` (fachlich relevant: Freitext Anamnese, Kontrolle-Felder, Lapidus-Rezidiv, QR-Schalter, Zusatzentgelte bleiben stehen) sowie `setDiagOffen` und `setToast` (nur Anzeige, dürfen bleiben).
- OP-Bericht: Reset als Inline-Funktion am Knopf neben „📋" unter „Vorschau & Export" (Z. 6705, am Seitenende). Sie setzt 62 Zustände; es fehlen 35 der 77 `useState`-Zustände (Z. 4880–5010), darunter `setGender`, `setSide`, `setAlter`, `setSektion`, `setPraeType`, `setAna`, `setBs`, `setFprae`, `setRisk`, `setRiskTxt`, `setSs`, die Sektionen Diabetischer Fuß (`setDfOp`, `setDfAmp`, `setDfTeilamp`, `setDfTeilampHoehe`, `setDfKnochen`, `setDfOsteo`, `setDfLavanox`, `setDfVanco`, `setDfLasche`, `setDfVac`), Metallentfernung (`setMeRegion`, `setMeImpl`, `setMeZusatz`), OSG (`setAskOsteo`, `setBrostromIB`, `setOsgArtPlatte`, `setOsgArtSchraube`, `setOsgArtSpongiosa`, `setNanoSeite`), `setCoalU12`, `setWeil`, die neuen Chips `setVfSehnentransfer`, `setVfSpongiosa` sowie `setSec` (Anzeige). Praktische Folge: Nach „Reset" bleibt der Patient (Geschlecht, Seite, Alter) stehen, ebenso ein diabetischer Fuß oder eine Metallentfernung.

## 2. Änderung Reset

1. `ToolKopfleiste` (Z. 750–759) bekommt eine optionale Eigenschaft `onReset`. Ist sie gesetzt, erscheint links vom „⌂" ein Knopf „↺ Neu" im Stil der übrigen Kopfleisten-Knöpfe. Ein Tipp führt `onReset` sofort aus, danach Toast „Zurückgesetzt". Keine Rückfrage, kein Browser-Dialog (Entscheidung des Autors 26.09.2026: ein versehentlicher Reset ist verschmerzbar).
2. Sprechstundenbrief: `resetAll` um die neun fachlichen Zustände ergänzen (Anfangswerte wie bei der Deklaration; `qrAktiv` auf `true` (Z. 2232), `zeAktiv` auf `{}` (Z. 2095)) und als `onReset` an die Kopfleiste geben (Aufruf Z. 10248, über eine Eigenschaft von `SprechstundenbriefApp` nach oben gereicht, wie `onWerkzeug`; oder `resetAll` über einen Ref/Callback registrieren, wie es der Code-Sitzung am saubersten erscheint). Der Knopf „🔄 Reset" in der Generator-Karte (Z. 3395) entfällt.
3. OP-Bericht: die Inline-Funktion (Z. 6705) wird zu `function resetAll()` in der Komponente, vollständig für alle 77 Zustände außer `toast` und `sec` (Sektionsklappen bleiben, wie sie sind), Anfangswerte wie bei der Deklaration (Z. 4880–5010: `alter` „erw" Z. 4909, `sektion` „fuss" Z. 4911, `praeType` „standard" Z. 4912, `tepTalCut` „chamfer" Z. 4986 usw. genau wie dort). Kopfleiste Z. 10259 bekommt `onReset`; der Knopf unter „Vorschau & Export" bleibt und ruft dieselbe Funktion.
4. Selbsttest: neue Prüfung „Reset unvollständig" (Hinweis): je Generator die Setter-Namen der Komponente gegen die in `resetAll` aufgerufenen vergleichen (Textsuche in der eigenen Quelle über `document.scripts`, wie die vorhandenen Quellprüfungen; falls das im Selbsttest zu aufwendig ist, weglassen und in der Vollzugsmeldung sagen).

## 3. Befund Kopierschrift

OP-Bericht: `copy` (Z. 6086) kopiert reinen Text (`obFallbackCopy`, Z. 6063); Word übernimmt die Formatierung der Einfügestelle. Dass der Text als Trebuchet MS 10 ankommt, liegt an der Vorlage des Autors, nicht an der App. Sprechstundenbrief: mit QR-Code kopiert `copyWithQr` (Z. 3263 ff.) HTML mit `font-size:10pt` und ohne `font-family` (Z. 3280, so seit `auftrag-brief-gruss-schrift.md`, 20.09.2026); Word nimmt dann seine Standardschrift statt der Vorlagenschrift. Ohne QR-Code reiner Text (`fallbackCopy`, Z. 3332). Der Autor will nicht mehr umstellen müssen.

## 4. Änderung Kopierschrift

1. Z. 3280: `var html = "<div style=\"font-family:'Trebuchet MS',sans-serif;font-size:10pt\">" + htmlBody + "</div>";` (Anführungszeichen entsprechend). Das hebt die Entscheidung „ohne font-family" vom 20.09. auf; der Autor hat die Schrift am 26.09.2026 benannt: Trebuchet MS, 10.
2. Ohne QR-Code denselben Weg: `copy()` (Z. 3254–3261) ruft immer `copyWithQr()`; dort, wenn `qrListe()` leer ist, den HTML-Aufbau ohne Bildzeilen durchlaufen (die `queue`-Prüfung Z. 3266 nur bei vorhandenen QR-Codes anwenden). Plain-Text bleibt als zweiter Clipboard-Typ und als Fallback erhalten. Damit kommt der Brief mit und ohne QR gleich an.
3. OP-Bericht unverändert lassen (kommt beim Autor richtig an). Falls die Code-Sitzung beide Generatoren gleich behandeln möchte: nur nach Rücksprache, nicht in diesem Auftrag.

## Nichts anderes

Brieftexte, Fallsteuerung, Daten unverändert.

## Abnahme

Cowork-Prüfstand: (1) Brief: Diagnose + OP-Methode + Freitext Anamnese + Lapidus-Rezidiv + Zusatzentgelt setzen → „↺ Neu" → alle Felder leer, Brief leer, Fallsteuerung weg. Referenzfälle `out/6c/res.json` zeichengleich. (2) OP-Bericht: Patient, Vorfuß Chevron, Diabetischer Fuß, Metallentfernung setzen → „↺ Neu" → Geschlecht/Seite/Alter auf Anfangswert, alle Sektionen leer, Kodeliste leer, Chips AHL/Spongiosa aus; Kombinationen aus `gp_6c_ob.py` zeichengleich. (3) Kopie: Brief mit QR → `text/html` enthält `font-family:'Trebuchet MS',sans-serif;font-size:10pt`; Brief ohne QR → ebenfalls `text/html` mit diesen Angaben, Plain-Text-Teil unverändert (Clipboard-Stub des Prüfstands). Selbsttest 0 Fehler, keine Konsolenfehler.

Abnahme des Autors am PC: Brief mit und ohne QR in die Vorlage kopieren: Trebuchet MS 10 ohne Umstellen. Am Handy: „↺ Neu" in beiden Generatoren oben sichtbar, ein Tipp setzt alles zurück.

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
