# Auftrag: Bildrahmen der Feature-Karten auf fuss-track.de (index.html)

Stand: 09.09.2026. Rückmeldung des Autors mit drei Screenshots der Live-Seite. Kleine Layoutänderung, nur CSS und zwei gelöschte Bildunterschriften; in der Cowork-Sitzung lokal mit Chromium bei 1280 px und 390 px gegengeprüft.

## Befund

1. In den Karten mit zwei Bildern (Sprechstundenbrief, Röntgen und Aufklärung) füllen die Bilder die Karte nicht: 12 px Abstand, abgerundete Ecken innerhalb der Karte und darunter Leerraum. Der Leerraum entsteht, weil einzelne `figure` eine `figcaption` tragen und der Flex-Streifen alle Figuren auf die Höhe der höchsten streckt; die Bilder ohne Unterschrift bekommen dadurch unten einen leeren Block.
2. In der Karte „Abrechnungswissen" liegt nur ein Bild (`ops-1-suche.webp`), die Karte ist aber so breit wie eine Zwei-Bild-Karte: das Bild sitzt links, die rechte Hälfte ist leer.

Entscheidung des Autors: Bildunterschriften streichen, Bilder auf die volle Karte strecken, die Ein-Bild-Karte auf Bildbreite verkleinern.

## Änderung (sechs Stellen)

CSS im `<style>`-Block:

```css
/* vorher */
.streifen{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;
          -webkit-overflow-scrolling:touch;scrollbar-width:none}
.streifen > figure{flex:0 0 100%;scroll-snap-align:center;margin:0}
.streifen img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:10px}
.streifen figcaption{margin-top:7px;font-size:.8rem;color:var(--muted);line-height:1.4}
@media (min-width:900px){
  .streifen > figure{flex:0 0 calc(50% - 6px)}
  .punkte{display:none}
}

/* nachher */
.streifen{display:flex;gap:1px;background:var(--line);overflow-x:auto;scroll-snap-type:x mandatory;
          -webkit-overflow-scrolling:touch;scrollbar-width:none}
.streifen > figure{flex:0 0 100%;scroll-snap-align:center;margin:0;background:#fff}
.streifen img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover}
@media (min-width:900px){
  .streifen > figure{flex:0 0 calc(50% - .5px)}
  .punkte{display:none}
  /* Nur ein Bild: Karte auf Bildbreite, mittig in der Spalte. */
  .shot.einzel{max-width:calc(50% - .5px);margin:0 auto}
  .shot.einzel .streifen > figure{flex:0 0 100%}
}
```

Der Abstand von 1 px mit `background:var(--line)` ergibt eine feine Trennlinie zwischen den beiden Bildern, sonst liegen sie randlos in der Karte; die Karte selbst behält Rahmen, Radius und Schatten.

HTML:

- `figcaption` „Der fertige Brief endet mit dem Code für die Patienten-App." (Sprechstundenbrief, drittes Bild) ersatzlos entfernen.
- `figcaption` „Risikoliste je Eingriff, mit einem Klick übernommen." (Röntgen und Aufklärung, zweites Bild) ersatzlos entfernen.
- Bei „Abrechnungswissen, jährlich gepflegt": `<div class="shot">` wird `<div class="shot einzel">`.

Der vollständige Diff liegt als `bildrahmen.diff` in der Cowork-Sitzung; er umfasst genau diese sechs Stellen, sonst ändert sich nichts. Die Patienten-Karten (`pat-1` bis `pat-3`) und die Menü-Karte nutzen dieselben Klassen und profitieren mit, dort gab es keine Unterschriften.

## Gegenprobe

Desktop ab 900 px: Sprechstundenbrief zeigt zwei Bilder randlos in der Karte, Wischen zum dritten, kein Leerraum unten; Röntgen und Aufklärung ebenso; Abrechnungswissen zeigt eine Karte in Bildbreite, mittig in der rechten Spalte. Mobil unter 900 px: ein Bild je Karte, Punkte unter dem Bild, Wischen funktioniert wie bisher. Kein Text unter den Bildern mehr.

Deploy: nur `index.html`, Repo-Push, kein Bucket. Wegen des Vortrags am 11.09. bitte als eigenen kleinen Commit, damit er sich notfalls allein zurücknehmen lässt.
