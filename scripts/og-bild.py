#!/usr/bin/env python3
"""Erzeugt das Vorschaubild (og:image) dieser Seite: icons/og-bild.png, 1200x630.

Start:  python3 scripts/og-bild.py   (aus dem Repo-Root)

Warum ein Skript und keine fertige PNG-Datei: Wortlaut und Untertitel aendern
sich; ein Bild, das niemand mehr bearbeiten kann, veraltet still. Hier steht
der Text im Klartext und das Bild wird daraus neu gebaut.

Ablauf: SVG mit eingebetteten Repo-Schriften (woff2, base64) -> qlmanage
rastert es -> sips schneidet auf 1200x630. Beides gehoert zu macOS, es wird
nichts nachinstalliert und nichts aus dem Netz geladen (BRAND.md).
"""
import base64, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
ZIEL = ROOT / "icons" / "og-bild.png"

# Farben aus BRAND.md
PETROL, PAPIER, TINT = "#10535B", "#FAFAF7", "#E6F0F1"

WORTMARKE = "Fuss-Track Clinic"
UNTERTITEL = "Dokumentation für Fuß- und Sprunggelenkchirurgie"
ZUSATZ = ""                       # dritte Zeile, leer lassen wenn nicht gebraucht
DOMAIN = "fuss-track.de"


def schrift(name):
    roh = (ROOT / "fonts" / name).read_bytes()
    return base64.b64encode(roh).decode()


def svg_bauen():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<defs><style>
@font-face{{font-family:'FT-Serif';font-weight:700;src:url(data:font/woff2;base64,{schrift('source-serif-4-700.woff2')}) format('woff2');}}
@font-face{{font-family:'FT-Sans';font-weight:400;src:url(data:font/woff2;base64,{schrift('ibm-plex-sans-400.woff2')}) format('woff2');}}
@font-face{{font-family:'FT-Sans';font-weight:500;src:url(data:font/woff2;base64,{schrift('ibm-plex-sans-500.woff2')}) format('woff2');}}
.marke{{font-family:'FT-Serif',Georgia,serif;font-weight:700;fill:{PAPIER}}}
.unter{{font-family:'FT-Sans',system-ui,sans-serif;font-weight:400;fill:{TINT}}}
.klein{{font-family:'FT-Sans',system-ui,sans-serif;font-weight:500;fill:{TINT}}}
</style></defs>
<rect width="1200" height="630" fill="{PETROL}"/>
<text class="marke" x="90" y="286" font-size="66">{WORTMARKE}</text>
<rect x="92" y="322" width="120" height="5" fill="{PAPIER}" opacity=".55"/>
<text class="unter" x="90" y="386" font-size="26">{UNTERTITEL}</text>
{f'<text class="klein" x="90" y="432" font-size="23" opacity=".85">{ZUSATZ}</text>' if ZUSATZ else ''}
<text class="klein" x="90" y="556" font-size="24" opacity=".7">{DOMAIN}</text>
</svg>"""


def main():
    for werkzeug in ("qlmanage", "sips"):
        if not shutil.which(werkzeug):
            sys.exit(f"{werkzeug} nicht gefunden — dieses Skript braucht macOS.")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        quelle = tmp / "og.svg"
        quelle.write_text(svg_bauen(), encoding="utf-8")
        # qlmanage rastert in ein Quadrat und polstert oben und unten; der
        # anschliessende mittige Beschnitt holt genau die 1200x630 zurueck.
        subprocess.run(["qlmanage", "-t", "-s", "1200", "-o", str(tmp), str(quelle)],
                       check=True, capture_output=True)
        roh = tmp / "og.svg.png"
        if not roh.exists():
            sys.exit("qlmanage hat kein Bild erzeugt.")
        ZIEL.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["sips", "-c", "630", "1200", str(roh), "--out", str(ZIEL)],
                       check=True, capture_output=True)
    print(f"geschrieben: {ZIEL.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
