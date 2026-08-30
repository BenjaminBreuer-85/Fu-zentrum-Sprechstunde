# Auftrag: Sprechstundenbrief ohne Geschlecht/Seite nutzbar machen (app.html)

Stand: 30.08.2026. Beobachtung des Autors: Im Sprechstundenbrief erscheinen die OP-/Options-Sektionen erst, wenn oben Geschlecht UND Seite gewählt sind. Viele Nutzer verstehen nicht, warum nach der Diagnosewahl „nichts passiert" — sie sehen nicht, dass oben noch etwas anzuklicken ist. Entscheidung des Autors: Es soll auch ohne diese Angaben gehen; der Brief wird dann ohne geschlechtsspezifische Angaben und ohne Seitenangaben ausgegeben.

## Was zu ändern ist

1. **UI-Gate lockern:** Die Render-Bedingungen der Sektionen (derzeit `{gender && (diagnosen.length > 0 …) && !meMode && !kontrolleMode}` — zwei Stellen, ca. Z. 3053 und Z. 3368) so ändern, dass die **Diagnosewahl allein genügt**. Geschlecht und Seite bleiben als Optionen oben stehen, sind aber keine Voraussetzung mehr. Gleiches für die Export-/Kopier-Bedingung (`canExport = gender && side && hasAny`, ca. Z. 5064): `hasAny` genügt.
2. **Briefgenerierung ohne Geschlecht:** Den Abbruch `if (!gender) return ""` (ca. Z. 1873) entfernen. Die neutralen Fallback-Formen existieren bereits (`dd`/`dd2`/`dem`/`sich` liefern „Der/Die Patient(in)" usw.) — bei fehlendem Geschlecht sollen aber bevorzugt **neutrale Umformulierungen ohne Paarform** verwendet werden, wo das ohne großen Umbau geht, z. B. „Die Vorstellung in unserer Sprechstunde erfolgte wegen …" statt „Der Patient stellte sich vor …" und „Es erfolgte die ausführliche Aufklärung über Diagnose, Therapieoption, Risiken und Alternativen …" statt „Der Patient wurde aufgeklärt …". Wo eine neutrale Konstruktion den Satz verrenken würde, ist die vorhandene Paarform „der/die Patient(in)" der Rückfall.
3. **Briefgenerierung ohne Seite:** Ohne Seitenwahl entfallen alle Seitenangaben ersatzlos (der Diagnosetext hängt die Seite bereits nur bedingt an — `(seite ? " " + seite : "")` — bitte alle übrigen Stellen gleich behandeln; im ME-Brief steht sonst „___", auch dort: ohne Seite die Formulierung ohne Seitenbezug ausgeben, kein „___" im Brief).
4. **Dezenter Hinweis statt Blockade:** Wenn Geschlecht oder Seite fehlen, oberhalb der Vorschau eine kleine, nicht blockierende Hinweiszeile zeigen, sinngemäß: „Ohne Geschlecht/Seite wird der Brief neutral und ohne Seitenangabe formuliert — Auswahl oben ergänzt beides." (Formulierung an den App-Stil anpassen, kein Gedankenstrich-Stakkato.)
5. ME- und Kontroll-Modus gelten entsprechend: keine Blockade durch Geschlecht/Seite; fehlende Angaben führen zu neutraler bzw. seitenfreier Formulierung.

## Gegenprobe

1. SB → nur „Hallux valgus" wählen (kein Geschlecht, keine Seite): Sektionen und Vorschau erscheinen; Brief enthält weder „Herr/Frau" noch „der Patient/die Patientin" in geschlechtsspezifischer Form noch eine Seitenangabe, und kein „___".
2. Danach Geschlecht + Seite nachwählen: Brief wie bisher mit Anrede und Seite.
3. ME-Brief ohne Seite: keine „___"-Reste. Kontroll-Brief unverändert.
4. Regressionslauf: eine Diagnose je Gruppe mit Geschlecht+Seite — Texte unverändert gegenüber heute.

## Deploy

Nur `app.html` ändern, committen, pushen. Kein Bucket-Upload.
