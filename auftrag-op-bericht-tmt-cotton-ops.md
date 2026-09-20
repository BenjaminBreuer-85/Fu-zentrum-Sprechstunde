# Auftrag Clinic: OPS-Kodes für TMT-Arthrodese und Cotton-Osteotomie im OP-Bericht

Stand 20.09.2026, Cowork-Sitzung. Beobachtung des Autors 20.09.2026: Im OP-Bericht-Generator sind bei den TMT-Arthrodesen keine OPS-Kodes hinterlegt. Datei `app.html`, Ausgangsstand Commit f9fc66b (803.643 Byte, Zeilenangaben darauf). Ein Commit, eine Vollzugsmeldung. Keine Datenänderung.

## Befund

Der Kodeblock des OP-Berichts (`allOPS`, Z. 4983–5081) hat für den Abschnitt „Mittelfuß" keine Zeile: weder `mfTmt` (Chips TMT 1, TMT 1–3, TMT 2–3, TMT 2, Z. 4680) noch `mfCotton` (Z. 4678) schieben einen Kode in `o`. Der OP-Text (Z. 5824 ff.), der Materialsatz (`PZ("arthrodese_tmt", …, tmtGelenke)`, Z. 4890) und der Erlösblock (Z. 5307–5320) kennen die Eingriffe; nur die Kodeliste bleibt leer. Im Erlösblock steht die Kodierung bereits als Text: TMT „5-808.a4 + 5-93b.e + 5-93b.0. TMT 2: + 5-784.0v (Spongiosa immer dabei)", TMT 1–3 „5-808.a6 = 3 Gelenke → I20C. 5-808.a7/a8 = 4–5 Gelenke → I20B", Cotton „5-781.4u + 5-784.7u (Spongiosa immer dabei)". Der Sprechstundenbrief hat die Kodes (`opsteuerung.json`: `arthrodese_tmt1` 5-808.a4 „ein Gelenkfach", `arthrodese_tmt` 5-808.a5 „zwei Gelenkfächer", `arthrodese_tmt13` 5-808.a6 „drei Gelenkfächer", Modifikator 4–5 Gelenke 5-808.a7).

Zweiter Punkt, gleicher Block: Bei „+ Cotton autolog/allogen" im Rückfuß-Abschnitt (`mdoCotton`, Z. 5061 f.) wird `5-781.6t` geschoben (varisierende Rotationsosteotomie am Kalkaneus, also der MDO-Kode, nicht die Cotton-Osteotomie am Cuneiforme), und zwar für autolog und allogen gleich; der Knochen wird nicht kodiert. Bitte mit prüfen.

## Entscheidungen des Autors 20.09.2026

Spongiosa immer kodieren (bei allen TMT-Eingriffen und bei Cotton); Cotton ohne Implantat; 5-781.6t bei „+ Cotton" ist ein Versehen; MDO ist immer 5-781.1t, Cotton immer 5-781.4u mit Augmentation durch Spongiosa allogen oder autogen (meist allogen).

## Änderung

1. TMT-Arthrodese, im Kodeblock hinter Z. 5060 (`fdlTransfer`), Gelenkzahl wie in Z. 4890 gerechnet (tmt1 = 1, tmt2 = 1, tmt2_3 = 2, tmt1_3 = 3, Summe über die gewählten Chips):

```
if(mfTmt.length>0){
  var tmtG=tmtGelenkzahl(mfTmt);
  var TMT_CODE={1:"5-808.a4",2:"5-808.a5",3:"5-808.a6",4:"5-808.a7"};
  o.push(TMT_CODE[Math.min(tmtG,4)]||"5-808.a8");
  o.push("5-93b.e");                                                        // winkelstabile Platte (alle TMT-Texte)
  if(mfTmt.includes("tmt1")||mfTmt.includes("tmt1_3")) o.push("5-93b.0");  // Kompressionsschraube TMT I (Materialsatz arthrodese_tmt1/tmt13)
  o.push("5-784.0u");                                                       // lokal gewonnene Spongiosa, Tarsale (alle TMT-Texte)
  if(mfTmt.includes("tmt2")) o.push("5-784.1u","5-783.2d");                 // trikortikaler Beckenkammspan (Text tmt_arthrodese_2), wie Double-/Triple-Arthrodese Z. 5044 f.
}
```

`tmtGelenkzahl(mfTmt)` als kleine Funktion aus Z. 4890 herausziehen und dort ebenfalls nutzen, damit Material und Kode nicht auseinanderlaufen. Der Erlösblock Z. 5307–5320 bleibt (nennt die Kodes nur im Text; die Zeile „TMT 2: + 5-784.0v" dort bitte auf „Spongiosa 5-784.0u bei allen TMT, TMT 2 zusätzlich Beckenkammspan 5-784.1u + 5-783.2d" anpassen, damit Text und Kodeliste übereinstimmen).

2. Cotton-Osteotomie (Mittelfuß-Chip `mfCotton`, Knochenwahl `mfCottonKnochen`, leer = autolog wie im OP-Text Z. 5820): `o.push("5-781.4u", mfCottonKnochen==="allogen" ? "5-784.7u" : "5-784.0u");` Kein 5-93b-Kode (Cotton ohne Implantat).

3. `mdoCotton` (Z. 5061 f.): statt `5-781.6t` dieselben Kodes wie Punkt 2, `mdoCotton==="allogen"` → 5-784.7u, sonst 5-784.0u. Der MDO-Kode 5-781.1t + 5-93b.0 kommt weiter über `rfOp` (Z. 5037), er wird nicht doppelt geschoben.

Hinweis zu den Daten (kein Teil dieses Auftrags): Die OP-Texte `cotton_ot_autolog` und `cotton_ot_allogen` (`optexte.json`) enthalten den Satz „Fixation mittels winkelstabiler Platte oder Zugschraube."; nach der Entscheidung „Cotton ohne Implantat" passt er nicht mehr. Streichung als Datenschritt nach Freigabe des Autors (Cowork-Sitzung, Bucket-Upload durch den Autor).

## Nichts anderes

OP-Texte, Materialsätze (`PZ`), Erlösblock, Sprechstundenbrief unverändert.

## Abnahme

Cowork-Prüfstand: OP-Bericht → Mittelfuß → TMT 1: Kodeliste 5-808.a4, 5-93b.e, 5-93b.0, 5-784.0u; TMT 2–3: 5-808.a5, 5-93b.e, 5-784.0u; TMT 1–3: 5-808.a6, 5-93b.e, 5-93b.0, 5-784.0u; TMT 2: 5-808.a4, 5-93b.e, 5-784.0u, 5-784.1u, 5-783.2d; TMT 1–3 + TMT 2: 5-808.a7. Cotton (ohne Knochenwahl und autolog): 5-781.4u, 5-784.0u; allogen: 5-781.4u, 5-784.7u; kein 5-93b. Rückfuß MDO + Cotton allogen: 5-781.1t, 5-93b.0 (MDO wie bisher) plus 5-781.4u, 5-784.7u, kein 5-781.6t. Alle anderen OP-Bericht-Fälle der Referenz (`baseline_ob_kombi_*`) unverändert; Selbsttest unverändert; keine Konsolenfehler.

Abnahme des Autors am Handy: OP-Bericht → Mittelfuß → TMT 1–3: Kodeliste zeigt 5-808.a6 und 5-784.0u; Cotton allogen: 5-781.4u und 5-784.7u.

Vollzugsmeldung bitte mit Commit-Hash und den Zeilennummern.
