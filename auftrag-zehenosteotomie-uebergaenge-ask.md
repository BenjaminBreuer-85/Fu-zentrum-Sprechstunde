# Auftrag Clinic: Zehenosteotomie-Chip, Übergänge bei mehreren Kleinzehen, ASK + Nanofrakturierung einmal beschreiben

Stand 03.10.2026, Cowork-Sitzung. Datei `app.html`, Ausgangsstand 7858cbc (804.941 B, md5 f774ed0e…; Zeilenangaben darauf). Datenstand `data/*.json` vom 02.10.2026 (Prüfstand). Entscheidungen des Autors vom 03.10.2026 (Brief-Wortlaut, Autorentext für beide ASK-Chips, Shannon-Fräse 2×13, Weichteile vor Knochen) sind eingearbeitet. Wunsch des Autors: (1) im OP-Bericht am Vorfuß bei den Kleinzehen D2–D5 einen Chip „Zehenosteotomie“ mit OPS 5-788.57 (1 Zehe), 5-788.58 (2), 5-788.59 (3), 5-788.5a (4), 5-788.5b (5 und mehr), nur für die Kleinzehen; (2) ein Konzept, damit die Übergänge im Berichtstext stimmen, wenn an mehreren Zehen operiert wird; (3) beim Chip „ASK + Nanofrakturierung“ wird die Arthroskopie zweimal beschrieben (erst der generische Text, dann der Text des Autors). Ein Commit, eine Vollzugsmeldung mit Commit-Hash und Zeilennummern. Datenschritte (`opsteuerung.json`, ggf. `opmethoden.json`) macht die Cowork-Sitzung nach Freigabe, siehe Abschnitt 4.

## Befund

Kleinzehen im OP-Bericht: Zustand `zc` je Zehe D2–D5 (Z. 5019), Chips aus `zehenOpts` (Z. 6172: pip, fdl, ext_teno, ext_verl, beuge_trans, kapsulo), Anzeige Z. 6300–6304. Text: `buildZehe(z, eingriffe, isFirst)` Z. 4549–4557, aufgerufen Z. 5806 je Zehe mit `isFirst` nur für die erste Zehe. OPS: Z. 5384–5396 (PIP-Mengenkode `PIP_CODE` Z. 1777, je Eingriffstyp einmal 5-854.0c / 5-854.2c / 5-851.1a); ICD M20.4 bei PIP Z. 5305; Strahlzählung 5-86a.1x Z. 5403–5412; Materialsatz `PZ("kleinzehen_pip","je Zehe",n)` Z. 5228; Fallsteuerung `obEintraege` Z. 1817–1818 mit `OB_SCHLUESSEL` (Z. 1788–1791) und `opsteuerung.json` (`kleinzehen_pip`: hdrg I20O, drg I20F, empf both). `katalog2026.json`: 5-788.57 steht im AOP-Katalog (f=1), 5-788.59/5a/5b sind Kontextprozeduren (f=4), **5-788.58 steht in keinem Katalog** (weder AOP noch Hybrid noch Kontext); OPS-Wortlaut „Digitus II bis V, 1 Phalanx / 2 Phalangen / 3 / 4 / 5 oder mehr Phalangen“, der Kode zählt Phalangen, nicht Zehen.

Übergänge: `buildZehe` kennt nur „erster Eingriff der ersten Zehe“ (voller Text) gegen „alles andere“ (Kurztext „Zuwendung zu D{z}, hier ebenfalls … in gleicher Weise“). Folgen, nachgestellt: (a) zweiter Eingriff an derselben Zehe beginnt erneut mit „Zuwendung zu D2“; (b) ein Eingriffstyp, der vorher an keiner Zehe beschrieben wurde, bekommt trotzdem „in gleicher Weise“ (D2 PIP, D3 FDL-Tenotomie → „Beugesehnentenotomie an D3 in gleicher Weise“); (c) die Reihenfolge der Eingriffe je Zehe ist die Klickreihenfolge; (d) kein abschließender Satz über alle Zehen. Nebenbefund: Z. 5539 `zeheWeichteil: zeheOpsSet.has("weichteil")` prüft eine Option, die es in `zehenOpts` nicht gibt; der Eintrag `kleinzehen_weichteil` wird aus dem OP-Bericht nie gesetzt.

ASK + Nanofrakturierung: Z. 5822–5827 (`op==="ask_nano"`, Varianten mit/ohne `askOsteo`) pushen einen Text, der mit dem generischen Absatz „Anlage der standardisierten Arthroskopie-Portale anterolateral und anteromedial … Systematische Inspektion … Es zeigt sich ein ventrales/weichteiliges Impingement … Debridement … Stresstest …“ beginnt und danach den Text des Autors anhängt („Auffüllen des … OSG mit 15ml Kochsalzlösung. Anlage des medialen Portales … antero-laterales Portal … Knorpelschaden der Talusschulter … Nanofrakturierung …“). Portale, Inspektion und Stabilitätsprüfung stehen damit zweimal. Der reine `ask`-Chip (Z. 5816–5820) nutzt nur den generischen Text.

## 1. Chip „Zehenosteotomie“ (Kleinzehen D2–D5)

(a) `zehenOpts` (Z. 6172) um `{id:"osteot", l:"Zehenosteotomie"}` ergänzen; erscheint damit je Zehe D2–D5 wie die übrigen Chips. Nicht bei der Großzehe.

(b) OPS nach Zahl der Zehen mit Osteotomie: neue Konstante neben `PIP_CODE` (Z. 1777) `var ZEHEN_OT_CODE = {1:"5-788.57", 2:"5-788.58", 3:"5-788.59", 4:"5-788.5a", 5:"5-788.5b"};` mit Kommentar: zählt nach OPS Phalangen; eine Osteotomie je Zehe, daher am einen Fuß höchstens 4 (5-788.5b nur erreichbar, wenn an einer Zehe zwei Phalangen osteotomiert werden, das ist nicht abgebildet). Im Kodeblock Z. 5388 ff. analog zur PIP-Zählung: `otZehenCnt = [2,3,4,5].filter(z => (zc[z]||[]).includes("osteot")).length; if (otZehenCnt>0) o.push(ZEHEN_OT_CODE[Math.min(otZehenCnt,5)]);`. Keine Doppelzählung mit dem Metatarsale-Mengenkode 5-788.5x (der zählt Ossa metatarsalia, Z. 5398).

(c) ICD (Entscheidung des Autors 03.10.2026): wie bei PIP (Z. 5305) bei Osteotomie ohne PIP `M20.5` + Seite („Sonstige Deformitäten der Zehe(n) (erworben)“); bei PIP an derselben Zehe bleibt M20.4 führend, M20.5 entfällt.

(d) Fallsteuerung: neuer Schlüssel `kleinzehen_osteotomie` in `OB_SCHLUESSEL` (Z. 1791, leere Modifikatorliste) und in `obEintraege` (nach Z. 1817): `if (z.otZahl > 0) add("kleinzehen_osteotomie", [], [ZEHEN_OT_CODE[Math.min(z.otZahl,5)]]);`, `otZahl` im Chip-Zustand (Z. 5539) wie `pipZahl`. Der Eintrag `kleinzehen_osteotomie` in `opsteuerung.json` kommt als Datenschritt (Abschnitt 4); bis dahin meldet der Selbsttest den fehlenden Eintrag, das ist erwartet und in der Vollzugsmeldung zu nennen.

(e) Statuszeile unter den Kleinzehen (nach Z. 6304): bei ≥ 1 Osteotomie „Zehenosteotomie: n Zehe(n) → 5-788.5x“, bei genau 2 Zehen zusätzlich „(5-788.58 steht in keinem Katalog)“ in derselben Schriftgröße wie die übrigen Hinweise (10 px, #718096). Sprachregel Abrechnung beachten: nur die Zuordnung benennen.

(f) Materialsatz: keiner, die Osteotomie ist implantatfrei (kein K-Draht, Entscheidung des Autors 03.10.2026); kein `PZ`-Aufruf.

(g) Text (Vorgabe des Autors 03.10.2026, Wortlaut zur Freigabe): „Stichinzision dorsomedial über dem Grundglied D{z}, Einbringen der Shannon-Fräse 2×13. Osteotomie des Grundgliedes unter dauerhafter Spülung und BV-Kontrolle in korrigierender Form entsprechend der Fehlstellung. Nun sehr gute Stellung der Zehe, orthograd und in korrekter Länge zu den Nachbarzehen.“ Keine Fixierung, kein K-Draht (Entscheidung des Autors 03.10.2026); die Stellung hält der redressierende Verband. Kurztext bei Wiederholung: „Zehenosteotomie am Grundglied D{z} mit der Shannon-Fräse in gleicher Weise, sehr gute Stellung.“ Befund-Fragment: „eine Achsabweichung der Zehe im Grundglied“.

## 2. Konzept Übergänge bei mehreren Kleinzehen (ersetzt `buildZehe`)

Neue Funktion `buildZehen(zc)` baut den ganzen Kleinzehen-Block und ersetzt die Schleife Z. 5806. Vorgabe des Autors 03.10.2026: an jeder Zehe zuerst die Weichteile (Narkosemobilisierung, Kapselrelease, Sehnen), dann die noch unzureichende Korrektur benennen, dann die Osteotomie, dann die sehr gute Stellung; ohne Weichteileingriff nur die Osteotomie. Daraus fünf Regeln:

1. **Eine Zuwendung je Zehe.** Erste Zehe: „Zuwendung zu D{z}.“; jede weitere: „Nun Zuwendung zu D{z}.“ Danach der Befundsatz: „Unter Narkosemobilisierung zeigt sich {Fragment 1}, {Fragment 2} und {Fragment 3}.“ aus den Befund-Fragmenten der gewählten Eingriffe (Tabelle unten); „ebenfalls“ nur, wenn dasselbe Fragment schon bei einer vorherigen Zehe stand. Wenn pip und beuge_trans an derselben Zehe gewählt sind, widersprechen sich „rigide“ und „flexibel“; dann nur das PIP-Fragment.

2. **Feste Reihenfolge je Zehe**, unabhängig von der Klickreihenfolge: Weichteile zuerst (Strecksehnen-Tenotomie oder -Verlängerung → dorsale Kapsulotomie → FDL-Tenotomie oder Beugesehnentransfer), dann Knochen (PIP-Arthrodese → Zehenosteotomie).

3. **Übergang Weichteil → Knochen.** Sind an einer Zehe Weichteileingriffe und PIP oder Osteotomie gewählt, steht nach dem letzten Weichteiltext der Satz „Die Korrektur ist nach den Weichteilmaßnahmen noch unzureichend, die Zehe steht weiterhin fehl.“ und danach der Knochentext. Ohne Weichteileingriff folgt der Knochentext direkt auf den Befundsatz. Innerhalb der Weichteile werden die Eingriffe mit „Anschließend“ (zweiter) und „Zusätzlich“ (dritter) verbunden, nie mit einer neuen Zuwendung.

4. **Voller Text beim ersten Vorkommen des Eingriffstyps im ganzen Bericht, Kurztext bei jeder Wiederholung**, gezählt über alle Zehen (Set `beschrieben`). Die vorhandenen Texte in `buildZehe` werden dafür zerlegt in `befund` (Fragment), `voll` (bisheriger Volltext ohne den Satz „Zuwendung zu D{z}. Es zeigt sich …“) und `kurz` (bisheriger Kurztext ohne „Zuwendung zu D{z}, hier ebenfalls …“). Der Stellungssatz „Nun sehr gute Stellung der Zehe …“ steht am Ende jedes Knochentextes (PIP: der vorhandene Satz „Korrekte Ausrichtung der Zehe, das MTP-Gelenk ist frei beweglich“ bleibt; Osteotomie: Satz aus 1(g)).

5. **Abschlusssatz nach der letzten Zehe:** „BV-Kontrolle: regelrechte Stellung der korrigierten Zehen D2 und D3{, K-Drähte korrekt platziert}.“ Klammerteil nur, wenn an mindestens einer Zehe PIP oder Kapsulotomie (K-Draht-Transfixation) gewählt ist; die Osteotomie allein hat keinen K-Draht. Aufzählung „D2“, „D2 und D3“, „D2, D3 und D4“.

Befund-Fragmente (aus den vorhandenen Texten): pip „eine rigide Krallenzehe, passiv nicht redressierbar“; fdl „eine Kontraktur der Beugesehnen“; ext_teno „eine Kontraktur der langen Strecksehne“; ext_verl „eine Strecksehnenkontraktur“; beuge_trans „eine flexible Krallenzehe mit Hyperextension im MTP-Gelenk“; kapsulo „eine Hyperextensionsstellung im MTP-Gelenk“; osteot „eine Achsabweichung der Zehe im Grundglied“.

Beispiel D2 Kapsulotomie + Zehenosteotomie, D3 Zehenosteotomie: „Zuwendung zu D2. Unter Narkosemobilisierung zeigt sich eine Hyperextensionsstellung im MTP-Gelenk und eine Achsabweichung der Zehe im Grundglied. Dorsale Inzision über dem MTP-Gelenk, Darstellung der Gelenkkapsel, dorsale Kapsulotomie … Temporäre K-Draht-Transfixation des MTP-Gelenkes in Plantarflexionsstellung. Die Korrektur ist nach den Weichteilmaßnahmen noch unzureichend, die Zehe steht weiterhin fehl. Stichinzision dorsomedial über dem Grundglied D2, Einbringen der Shannon-Fräse 2×13. Osteotomie des Grundgliedes unter dauerhafter Spülung und BV-Kontrolle in korrigierender Form entsprechend der Fehlstellung. Nun sehr gute Stellung der Zehe, orthograd und in korrekter Länge zu den Nachbarzehen.

Nun Zuwendung zu D3. Unter Narkosemobilisierung zeigt sich ebenfalls eine Achsabweichung der Zehe im Grundglied. Zehenosteotomie am Grundglied D3 mit der Shannon-Fräse in gleicher Weise, sehr gute Stellung.

BV-Kontrolle: regelrechte Stellung der korrigierten Zehen D2 und D3, K-Drähte korrekt platziert.“

Nebenbefund Z. 5539 (`zeheWeichteil` nie wahr): auf `zeheOpsSet` mit fdl/ext_teno/ext_verl/beuge_trans/kapsulo abbilden, damit `kleinzehen_weichteil` in der Fallsteuerung erscheint, wenn nur Weichteileingriffe gewählt sind.

## 3. ASK und ASK + Nanofrakturierung: nur der Text des Autors

Entscheidung des Autors 03.10.2026: der generische Arthroskopie-Absatz entfällt bei beiden Chips.

(a) `ask_nano` (Z. 5822–5827): Text beginnt mit „Auffüllen des … OSG mit 15ml Kochsalzlösung.“ (Text des Autors, unverändert bis zum Ende „… freie Beweglichkeit des Gelenkes.“). Osteophyten-Variante (`askOsteo`) als bedingte Einfügung nach „Eingehen mit dem Shaver und Entfernung der Vernarbungen“: „, Abtragung der ventralen Osteophyten an Tibiavorderkante und Talushals mit der arthroskopischen Fräse“. Ein Textbaustein statt zwei fast gleicher Strings.

(b) `ask` (Z. 5816–5820): derselbe Text des Autors ohne den Talusschulter-Teil, also von „Auffüllen des … OSG mit 15ml Kochsalzlösung.“ bis „… Stabilitätstestung, die Syndesmose ist stabil, keine vermehrte laterale Aufklappbarkeit.“, dann „Ausgiebige Spülung. Abschließende Kontrolle, freie Beweglichkeit des Gelenkes.“; Osteophyten-Einfügung wie in (a). Der Satz „In Plantarflexion und unter Distraktion kommt ein … Knorpelschaden der Talusschulter zur Darstellung … Nanofrakturierung …“ bleibt dem Chip ASK + Nanofrakturierung vorbehalten. Beide Texte als gemeinsamen Baustein mit zwei Schaltern (osteophyten, nano) anlegen, damit der Wortlaut des Autors nur einmal im Code steht. OPS (Z. 5417) unverändert.

## 4. Datenschritte nach der Code-Umsetzung (Cowork-Sitzung, nach Freigabe)

`opsteuerung.json`: Eintrag `kleinzehen_osteotomie` {hdrg "I20O", drg "I20F", impl null, empf "both", hebel null, hebelName null, hinweise: info „5-788.57 (eine Zehe) steht im AOP-Katalog; ab drei Zehen (5-788.59/5a) sind die Kodes Kontextprozeduren; 5-788.58 (zwei Zehen) steht in keinem Katalog.“} — Zuordnung I20O/I20F wie bei `kleinzehen_pip`, vom Autor am 03.10.2026 bestätigt; Prüfung von 5-788.58 in der Master-Excel durch den Autor.

`opmethoden.json`, Entscheidung des Autors 03.10.2026: Im Sprechstundenbrief wird die Kleinzehen-Methode künftig immer als „PIP-Arthrodese oder Korrekturosteotomie“ geführt, damit alle Optionen offen bleiben. Eintrag `kleinzehen_pip`: k „Kleinzehen/PIP oder Osteotomie“, b „eine Korrektur der Kleinzehenfehlstellung mit PIP-Arthrodese oder Korrekturosteotomie“, t „Kleinzehenkorrektur mit PIP-Arthrodese oder Korrekturosteotomie“, r unverändert; kein neuer Brief-Eintrag. Folgen: Chip-Label im Brief ändert sich (Prüfstand-Skripte, die `OPS[k].k` suchen, anpassen); `kurzlinks.json`-Titel „Korrektur bei Fehlstellungen der Kleinzehen“ passt weiterhin; die 89 Brief-Referenzfälle weichen in den Kleinzehen-Fällen genau in diesem Wortlaut ab. Bucket-Reihenfolge: erst Upload, dann Push.

## Nichts anderes

Großzehen-Chips, DMMO/Weil, Brief, Aufklärung, Begleiter, Fuss-Track unverändert. Keine Änderung an `katalog2026.json` (nur per Skript aus der Master-Excel).

## Abnahme

Cowork-Prüfstand: (1) Chip „Zehenosteotomie“ an D2–D5; 1/2/3/4 Zehen → 5-788.57/58/59/5a in der Kodeliste und Statuszeile, bei 2 Zehen der Hinweis zum Katalog; PIP + Osteotomie an derselben Zehe → beide Kodes; Fallsteuerung zeigt `kleinzehen_osteotomie` (Selbsttest-Meldung bis zum Datenschritt). (2) Übergänge: die Fälle D2 PIP+FDL / D3 PIP; D2 PIP / D3 FDL; D3 Kapsulotomie / D4 PIP+Kapsulotomie; D2 Kapsulotomie+Osteotomie / D3 Osteotomie; D2 nur Osteotomie ergeben je Zehe genau eine Zuwendung mit Narkosemobilisierung im Befundsatz, Weichteile vor Knochen, Übergangssatz „noch unzureichend“ nur bei Weichteil + Knochen, Stellungssatz nach jedem Knochentext, „in gleicher Weise“ nur bei wiederholtem Eingriffstyp, Abschlusssatz mit richtiger Aufzählung; Einzelzehe mit einem Eingriff unverändert zum heutigen Volltext bis auf den Befundsatz. (3) ASK und ASK + Nanofrakturierung, je mit und ohne Osteophyten: „Anlage des“ Portales genau einmal, kein „standardisierte Arthroskopie-Portale“ mehr im Bericht, Osteophytenabtragung nur mit Chip, Talusschulter-Teil nur bei Nanofrakturierung. (4) Selbsttest ohne neue Fehler außer dem erwarteten fehlenden `opsteuerung`-Eintrag; keine Konsolenfehler; JSX-Transpile-Prüfung; 89 Brief-Referenzfälle unverändert.

Am Handy: OP-Bericht → Vorfuß → D2 PIP-Arthrodese + Zehenosteotomie, D3 Zehenosteotomie → Text mit einer Zuwendung je Zehe, Kode 5-788.58 in der Liste; OSG → ASK + Nanofrakturierung → Arthroskopie einmal.

Vollzugsmeldung bitte mit Commit-Hash und Zeilennummern.
