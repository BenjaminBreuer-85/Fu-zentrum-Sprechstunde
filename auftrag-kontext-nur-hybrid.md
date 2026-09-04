# Auftrag: Block „Kontextprozeduren" nur bei Hybrid-DRG-Eingriffen rendern

**Datei:** `app.html`, Sprechstundenbrief, Fallsteuerung (Block ab ca. Zeile 3148; Stationär-Box ab ca. Zeile 3082)
**Daten:** `data/opsteuerung.json` ist bereits angepasst (kontext bei `arthrodese_osg` und `haglund_as_split` entfernt, Erlöshebel als Hinweis vom Typ info; Bucket-Upload offen, siehe DEPLOY.md D)
**Anlass (03.09.2026):** Bei rein stationären Eingriffen ohne Hybrid-DRG erschien der Block „Kontextprozeduren" mit dem Satz „Stationär: IMMER kodieren zum Ausschluss H-DRG", obwohl es für diese Eingriffe keine Hybrid-DRG gibt (beobachtet bei der USG-Arthrodese in der Live-App; in den Daten betroffen: OSG-Arthrodese mit Spongiosa-Codes, Haglund mit Achillessehnen-Split). Kontextprozeduren sind nur dort relevant, wo es um Auslösung oder Vermeidung der Hybrid-DRG geht.

## Änderung 1: Block nur bei Hybrid-Bezug

Die Render-Bedingung des Blocks (Zeile ~3148) um den Hybrid-Bezug erweitern:

```js
var hatHybridBezug = (hdrg !== null && hdrg !== undefined) || (best.hdrgTrigger && best.hdrgTrigger.length > 0);
{!hideKontext && hatHybridBezug && ((best.kontext && best.kontext.length > 0) || (best.kontextExcluded && best.kontextExcluded.length > 0) || (best.hdrgTrigger && best.hdrgTrigger.length > 0)) ? <div ...> ... </div> : null}
```

`hdrg` ist hier der bereits berechnete Wert nach Override (nicht `best.hdrg`), damit Konstellationen wie „MTP-I + 3× DMMO → keine H-DRG" den Block ebenfalls unterdrücken (dort greift heute schon `hideKontext`; die neue Bedingung macht das allgemein).

Untertitel im Block ergänzen, direkt unter „Kontextprozeduren":

```
Hybrid-DRG: entscheidet über ambulant, Hybrid oder stationär.
```

## Änderung 2: Erlöshebel in der Stationär-Box

Für Einträge ohne `hdrg`, aber mit `best.hebel`, in der Stationär-Box unter der MVWD-Zeile eine grüne Zeile anzeigen:

```jsx
{!hatHybridBezug && best.hebel && <div style={{fontSize:10,color:"#2E7D32",marginTop:4,fontWeight:600}}>
  Erlöshebel: <span style={{fontFamily:"monospace"}}>{best.hebel}</span>{best.hebelName ? " ("+best.hebelName+")" : ""} → {drg}
</div>}
```

Die bestehende Zeile in der Ambulant-Box (Zeile ~3064, „❌ Kontextprozedur(en) NICHT kodieren — sonst Verlust der H-DRG") ist bereits an `ambStatus === "hdrg"` gebunden und bleibt unverändert.

## Gegenprobe

| Auswahl | Erwartung |
|---|---|
| USG-Arthrodese allein | kein Block „Kontextprozeduren", keine Hebel-Zeile (kein hebel hinterlegt) |
| OSG-Arthrodese allein | kein Block „Kontextprozeduren"; Stationär-Box zeigt „Erlöshebel: 5-783.0d + 5-784.0n (Spongiosa Beckenkamm → Tibia) → I13D"; Hinweisliste zeigt den neuen info-Hinweis und die bestehenden warn/alert-Hinweise |
| OSG-Arthrodese mit Modifikator „ohne Spongiosa" | wie oben, DRG I13E, alert-Hinweis des Modifikators |
| Haglund mit AS-Split | kein Block; Hebel-Zeile „5-854.29 → I27D"; info-Hinweis |
| Chevron | Block „Kontextprozeduren" mit 5-854.2c wie bisher, plus Untertitel |
| Lapidus | Block mit H-DRG-Trigger, Kontext und „nicht wirksam"-Liste wie bisher |
| MTP-I-Arthrodese + 3× DMMO | kein Block (Override ohne H-DRG) |

## Deploy

`app.html` (Repo, Push). **Bucket-Upload `opsteuerung.json` offen** (DEPLOY.md D). Vor dem Upload die Bucket-Kopie einmal herunterladen und mit der lokalen Datei vergleichen: Zeigt die Live-App bei der USG-Arthrodese den Block, obwohl der lokale Eintrag kein `kontext` hat, liegt im Bucket ein älterer Stand.

## Nachtrag 03.09.2026 (nach Gegenprobe der Code-Sitzung)

Bucket-Vergleich bestätigt: Bucket-Kopie von `opsteuerung.json` älter als lokal. Upload bleibt offen (DEPLOY.md D); die Codeänderung wirkt unabhängig davon.

**1. Pfeil der Hebel-Zeile auf das Ziel des Hebels.** `drg` und `best.drg` sind nach Modifikator bereits die DRG ohne Hebel (bei „ohne Spongiosa" also I13E). Das Ziel steht im Grundeintrag:

```jsx
var hebelZiel = (OP_STEUERUNG[bestKey] && OP_STEUERUNG[bestKey].drg) || drg;
{!hatHybridBezug && !hideKontext && best.hebel && <div style={{fontSize:10,color:"#2E7D32",marginTop:4,fontWeight:600}}>
  Erlöshebel: <span style={{fontFamily:"monospace"}}>{best.hebel}</span>{best.hebelName ? " ("+best.hebelName+")" : ""} → {hebelZiel}
  {hebelZiel !== drg && <span style={{color:"#C62828",fontWeight:400}}> (aktuell {drg}, Hebel nicht genutzt)</span>}
</div>}
```

Mit Modifikator „ohne Spongiosa" liest sich die Zeile dann „Erlöshebel: 5-783.0d + 5-784.0n (…) → I13D (aktuell I13E, Hebel nicht genutzt)".

**2. MTP-I + 3× DMMO: keine Hebel-Zeile.** In diesen Overrides kommt I20D aus der DMMO-Anzahl (5-788.54), nicht aus 5-784.0v; die Zeile „5-784.0v → I20D" wäre irreführend. Die Overrides setzen bereits `hideKontext:true`, deshalb reicht `!hideKontext` in der Bedingung oben. Erwartung danach: MTP-I + 3× DMMO und + 4× DMMO ohne Block und ohne Hebel-Zeile.

Gegenprobe ergänzen: OSG-Arthrodese ohne Spongiosa → Hebel-Zeile mit „→ I13D (aktuell I13E, Hebel nicht genutzt)"; MTP-I + 3× DMMO → keine Hebel-Zeile.
