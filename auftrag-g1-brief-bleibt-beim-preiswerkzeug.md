# Auftrag Clinic (Backlog G1): Brief bleibt erhalten, wenn aus der Fallsteuerung ins Preiswerkzeug gewechselt wird

Stand 22.09.2026, Cowork-Sitzung. Backlog G1 (seit e2984a7, Entscheidung des Autors 22.09.2026: jetzt bauen). Datei `app.html`, Ausgangsstand Commit 34475c9 (805.008 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

Der Link „Preise hinterlegen" in der Fallsteuerung (Ambulant-Box Z. 3553, Stationär-Box Z. 3603) ruft `setTool("preise")`; `setTool` kommt als `onWerkzeug` aus `App` (Z. 1780, Aufruf Z. 10143). `App` (Z. 10111 ff.) rendert je `tool` genau einen Zweig; bei `tool === "preise"` (Z. 10208) ist `SprechstundenbriefApp` nicht mehr im Baum, ihr gesamter Zustand (Diagnosen, OP-Methoden, Befunde, Freitexte, `_s`-Zustände ab Z. 1782) geht verloren. Kommt der Nutzer über „← Menü" und die Kachel zurück, ist der Brief leer. Praktische Folge: Wer im Brief Preise nachträgt, weil die Box „unvollständig" meldet, muss den Brief danach neu aufbauen.

## Änderung (Preiswerkzeug als Überlagerung, Brief bleibt montiert)

1. In `App` ein zusätzlicher Zustand `const [briefHinterPreisen, setBriefHinterPreisen] = React.useState(false);`. Die an `SprechstundenbriefApp` gegebene Funktion (Z. 10143) wird `onWerkzeug={function(t){ if (t === "preise") setBriefHinterPreisen(true); setTool(t); }}`.

2. Der Zweig `tool === "sb"` (Z. 10139–10146) rendert auch dann, wenn `tool === "preise" && briefHinterPreisen`, dann aber unsichtbar: den bestehenden `<div>` um `<ToolKopfleiste …/><MitRundgang …>` mit `style={{display: tool === "sb" ? "block" : "none"}}` versehen und die Bedingung auf `if (tool === "sb" || (tool === "preise" && briefHinterPreisen))` erweitern; im Fall `tool === "preise"` folgt darunter im selben Fragment der Preiswerkzeug-Zweig (Z. 10208–10221) unverändert. Damit bleibt `SprechstundenbriefApp` montiert, ihr Zustand bleibt, und die Preisänderungen kommen über `useKontoStatus()` an der Wurzel (Z. 10116) beim Rücksprung wie gewohnt an.

3. Rücksprung: In der Kopfleiste des Preiswerkzeugs (Z. 10210) bei `briefHinterPreisen` statt „← Menü" einen Knopf „← Zurück zum Brief" mit `onClick={()=>setTool("sb")}`; `ToolKopfleiste` bekommt dafür die optionalen Eigenschaften `zurueckText` und `onZurueck` (Z. 750–758): ist `onZurueck` gesetzt, ruft der linke Knopf `onZurueck` und zeigt `zurueckText`, sonst wie heute `onHome` und „← Menü". Der „⌂"-Knopf (Z. 754) bleibt der Weg ins Menü.

4. Aufräumen: Beim Wechsel ins Menü (`onHome`, `setTool(null)`) und bei jedem anderen Werkzeug `setBriefHinterPreisen(false)`; am einfachsten in einer kleinen Funktion `wechselTool(t){ if (t !== "preise" && t !== "sb") setBriefHinterPreisen(false); setTool(t); }`, die `kopf()`, `zurEinstellung`, `rundgangStarten`, die `onHome`-Aufrufe und `LandingPage onSelect` (Z. 10265) nutzen. Der versteckte Brief wird dann beim nächsten Render abgebaut, wie heute.

5. Rundgang: `MitRundgang` um den versteckten Brief darf keinen Rundgang starten; `anstoss={tourWunsch.sb}` bleibt, wird aber nur gesetzt, wenn der Nutzer aus den Einstellungen „sb" wählt (Z. 10130 ff.), dann ist `tool === "sb"`. Keine Änderung nötig, bitte in der Abnahme prüfen, dass beim Wechsel Preise → Brief kein Rundgang anspringt.

## Nichts anderes

OP-Bericht, Preiswerkzeug (`ImplantatpreiseView`), Brieflogik, Daten unverändert. Der OP-Bericht hat keinen Link ins Preiswerkzeug (nur die zwei Stellen im Sprechstundenbrief), bleibt außen vor.

## Abnahme

Cowork-Prüfstand (Referenz `baseline_sb_3w.json` mit aktuellen Daten): Briefe und Fallsteuerung zeichengleich (keine Änderung der Brieflogik). Ablauf: Hallux valgus → Chevron → Erlössimulation → „Preise hinterlegen" → Kopfleiste zeigt „← Zurück zum Brief" und „⌂" → Testpreis für die Kompressionsschraube 2,5 eintragen → „← Zurück zum Brief": Diagnose, Chip und Brief unverändert vorhanden, Materialzeile zeigt jetzt den Betrag mit Ampel statt „unvollständig". Dann „⌂" → Kachel Sprechstundenbrief: leerer Brief wie heute (bewusst). Vom Menü direkt ins Preiswerkzeug: Kopfleiste „← Menü" wie heute, kein versteckter Brief. Selbsttest unverändert, keine Konsolenfehler, keine Warnung zu doppelten Schlüsseln.

Abnahme des Autors am Handy: derselbe Ablauf, zusätzlich prüfen, dass der Bildschirm im Preiswerkzeug nicht nach unten weiterscrollt (versteckter Brief nimmt keinen Platz ein).

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern.
