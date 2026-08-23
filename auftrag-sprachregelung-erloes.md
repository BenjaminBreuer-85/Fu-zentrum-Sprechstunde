# Auftrag: Sprachregelung in der Fallsteuerung

## Warum

Die Fallsteuerung soll transparent machen, was ein Behandlungsweg wirtschaftlich bedeutet. Sie darf aber nicht so klingen, als solle die Behandlungsform nach dem Erlös gewählt werden. Formulierungen wie „stationäre Führung erwägen" oder „ökonomisch unattraktiv" lassen sich als Aufforderung zur Fehlbelegung lesen. Das ist bei einem Werkzeug, das Kollegen in der Klinik einsetzen, die größte denkbare Angriffsfläche, und es entspricht auch nicht dem, was das Werkzeug leisten soll.

**Die Linie:** Erlöszahlen und Kodierregeln sind Information und bleiben unverändert. Alles, was eine Handlungsempfehlung zur Aufenthaltsform oder zur Verweildauer ausspricht, wird entweder zur Tatsachenaussage umformuliert oder ausdrücklich an die medizinische Indikation gekoppelt.

Eine Stelle in `app.html` macht es bereits vorbildlich und dient als Muster:

> „❌ Ambulant: NICHT kodieren — sonst Verlust der H-DRG. **Bei klinischer Notwendigkeit** besser stationäre Führung."

## Wo geändert wird

Alle betroffenen Texte stehen in `app.html`. In `data/opsteuerung.json` ist die einzige EBM-Aussage bereits neutral formuliert („Ambulant per EBM (AOP-fähig) oder kurzstationär als I59Z möglich"). Es ist also **kein Bucket-Upload nötig**, nur ein Push. Beim Umsetzen dennoch kurz prüfen, ob in `opsteuerung.json` das Wort „einplanen" in einem empfehlenden Zusammenhang steht; es kommt dort einmal vor.

## Zu ersetzende Formulierungen

| Bisher | Neu |
|---|---|
| „→ Ambulant: nur EBM-Abrechnung (unattraktiv) · stationäre Führung erwägen" | „→ Ambulant: nur EBM-Abrechnung möglich" |
| „→ Ambulant: nur EBM-Abrechnung · Stationär ≥2 Nächte: volle DRG anstreben" | „→ Ambulant: nur EBM-Abrechnung möglich · stationär ab 2 Nächten volle DRG" |
| „⚠ Ökonomisch unattraktiv — EBM-Erlös deckt klinischen Aufwand meist nicht. Stationäre Führung bevorzugen." | „Ambulant ist nur die EBM-Abrechnung möglich; sie deckt den klinischen Aufwand meist nicht." Das Warndreieck entfällt, es macht aus der Information eine Anweisung. |
| „nur EBM · ökonomisch unattraktiv" | „nur EBM · geringer Erlös" |
| „Ambulant nur EBM möglich · stationär ≥ 2 Nächte anvisieren (volle DRG)" | „Ambulant nur EBM möglich · stationär ab 2 Nächten volle DRG" |
| „Stationäre Führung dadurch gerade wegen der DRG-Aufwertung umso sinnvoller: I20D (4.710 €) statt I20E (3.923 €) → +787 €." | „Bei stationärer Führung greift I20D (4.710 €) statt I20E (3.923 €), ein Unterschied von 787 €." |
| „→ Empfehlung: Mindestens 3 Übernachtungen einplanen." | „Die untere Grenzverweildauer liegt bei 3 Tagen; bei Entlassung nach 2 Nächten greift ein Abschlag von rund 1.209 €." |
| „⚠ Häufiger Fehler: Entlassung nach 2 Nächten → 1.209 € Abschlag! Mind. 3 Nächte einplanen." | „⚠ Bei Entlassung nach 2 Nächten greift ein Abschlag von 1.209 €." |
| „→ Stationär planen, mind. 2 Nächte für volle DRG I59Z (3.225 €)." | „Ohne H-DRG-Fähigkeit ist nur die stationäre Abrechnung möglich; die volle DRG I59Z (3.225 €) wird ab 2 Nächten erreicht." |
| „✅ EMPFOHLEN: 1 Tag weniger zu rechtfertigen." | „Mit Kontextprozedur ist ein Belegungstag weniger zu begründen." |
| „Stat: 5-854.2c/0c erwägen → I20E" | „Stat: 5-854.2c/0c bei tatsächlich erbrachter Leistung → I20E" |

## DMMO 3–4 MT: Sachverhalt richtigstellen

> Bisher: „Ambulant: H-DRG-Code dazukodieren erwägen."

Dieser Satz gibt die Rechtslage verkürzt und dadurch falsch wieder. Gemeint ist keine Kodierentscheidung, sondern eine Zulässigkeitsfrage: **5-788.54/55 steht nicht im AOP-Katalog und darf als Klinikleistung nicht ambulant erbracht werden.** Eine ambulante Planung kommt nur in Betracht, wenn im selben Eingriff eine AOP- beziehungsweise H-DRG-fähige Leistung tatsächlich erbracht wird.

Neuer Text im Kodierfeld:

> „5-788.54/55 = DMMO 3–4 MT. Nicht im AOP-Katalog: als Klinikleistung ambulant nicht zulässig. Eine ambulante Planung ist nur möglich, wenn im selben Eingriff eine AOP- beziehungsweise H-DRG-fähige Leistung tatsächlich erbracht wird."

Der zugehörige Zielsatz bleibt inhaltlich, wird aber an die Zulässigkeit statt an den Erlös geknüpft:

> „Nicht im AOP-Katalog und nicht auf der H-DRG-Positivliste. Stationär ab 2 Nächten I20F (3.040 €)."

Als Muster dient die Stelle bei der Lapidus-Arthrodese, die es bereits richtig macht:

> „⚠ 5-808.a4 NICHT auf H-DRG-Positivliste UND NICHT im AOP-Katalog! → Nur stationär möglich."

Beim Umsetzen prüfen, ob es weitere Eingriffe mit derselben Konstellation gibt (Code weder im AOP-Katalog noch auf der Positivliste). Dort gilt dieselbe Sprachregelung: erst die Zulässigkeit, dann der Erlös.

## Was unverändert bleibt

- Die Überschrift „Ökonomisches Codierziel“. Die App richtet sich an Behandler, und dieses Ziel existiert; der Begriff ist fachlich korrekt und wird nicht entschärft.

- Alle Erlöszahlen, DRG-Bezeichnungen, Grenzverweildauern und Katalogangaben.
- Alle Kodierhinweise der Form „X IMMER mitkodieren" und „Y NICHT kodieren", denn sie beschreiben die korrekte Abbildung erbrachter Leistungen.
- Die Hinweise zur Dokumentationspflicht. Der Satz „Jeder Tag muss dokumentarisch gerechtfertigt sein" ist die stärkste Absicherung im Werkzeug und darf gern eher verstärkt als abgeschwächt werden.
- Die Warnungen vor MDK-Kürzungen.

## Ein Punkt zur Entscheidung durch Benjamin

**Ein Grundsatzsatz unter der Fallsteuerung.** Ein einziger Satz, etwa „Die Wahl zwischen ambulanter und stationärer Führung richtet sich nach der medizinischen Indikation; die Fallsteuerung zeigt nur, was der jeweilige Weg wirtschaftlich bedeutet." Das wäre der einzige neue Text in der App und würde alles darüber entschärfen. Benjamin wollte die App textlich nicht weiter aufblähen, deshalb nur als Vorschlag.

Deploy: nur `app.html`, Commit durch die Code-Sitzung, Push durch Benjamin nach Sichtprüfung. Kein Supabase-Upload.
