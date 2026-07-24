#!/usr/bin/env python3
"""Prüfskript Stufe 1: Vergleicht data/*.json Wert für Wert mit den Original-
Datenblöcken aus dem alten index.html (git HEAD vor dem Umbau).

Jede Abweichung (fehlender/zusätzlicher Schlüssel, anderer Wert, anderer Typ,
andere Schlüssel-Reihenfolge) wird einzeln gemeldet. Exit-Code 0 = identisch.

Aufruf:  python3 scripts/verify_extraction.py [<git-ref>]   (Default: HEAD)
Läuft ohne Node.js — nutzt macOS-JavaScriptCore (jsc).
"""
import json, os, re, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSC = "/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc"
REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"

GROUPS = {
    "diagnosen": ["DIAG", "COALITIO_BEFUNDE", "KONSERV", "RISIKEN", "RISIKEN_ENDO", "KONTROLLE_TEXT", "KONTROLLE_LABEL"],
    "opmethoden": ["OPS", "OPS_LABELS", "AUFKLAERUNG_MAP", "PATIENT_EINGRIFF_MAP", "PATIENT_VARIANTEN"],
    "opsteuerung": ["OP_STEUERUNG", "UGVD_ABSCHLAG", "ME_REGIONEN"],
    "endo": ["ENDO_DRG", "ENDO_KONSTELLATIONEN", "ENDO_BEF_HUEFTE", "ENDO_BEF_KNIE", "ENDO_BEF_TEP_SCHMERZ",
             "ENDO_ZE", "ENDO_HTEP_IMPL", "ENDO_DUOKOPF_IMPL", "ENDO_IMPL_KOMPONENTEN", "ENDO_KTEP_IMPL",
             "ENDO_KTEP_MODULAR_IMPL", "ENDO_SCHLITTEN_IMPL", "ENDO_EINGRIFFE"],
    "preise": ["EINZELPREISE", "UC_IMPL_HUMERUS_PROX", "UC_IMPL_RADIUS_DISTAL"],
    "optexte": ["T", "UC_EINGRIFFE", "UC_TEXT_MAP", "WS_EINGRIFFE", "WS_WIRBEL", "WS_SEGMENTE"],
    "aufklaerung": ["AUFKLAERUNG_RISIKEN"],
    "referenz": ["KLASSIFIKATIONEN", "ROENTGEN", "MESSMETHODEN", "MANUALE"],
    "erloes2026": ["GVD"],
}

old = subprocess.run(["git", "-C", REPO, "show", REF + ":index.html"],
                     capture_output=True, text=True, encoding="utf-8")
if old.returncode != 0:
    sys.exit("git show fehlgeschlagen: " + old.stderr.strip())
src = old.stdout

def find_const_block(name):
    matches = list(re.finditer(r'(?m)^([ \t]*)const %s\s*=\s*' % re.escape(name), src))
    if len(matches) != 1:
        sys.exit("Altbestand: %d Fundstellen fuer const %s" % (len(matches), name))
    m = matches[0]
    i = m.end()
    while src[i] not in '{[':
        i += 1
    open_ch = src[i]; close_ch = {'{': '}', '[': ']'}[open_ch]
    depth = 0; j = i; in_str = None; esc = False
    while True:
        c = src[j]
        if in_str:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == in_str: in_str = None
        else:
            if c in ('"', "'", '`'): in_str = c
            elif c == open_ch: depth += 1
            elif c == close_ch:
                depth -= 1
                if depth == 0: break
        j += 1
    return src[m.start():j + 1]

def window_span(first, last_start):
    a = src.index(first)
    b = src.index(last_start, a)
    b = src.index(';', b) + 1
    return src[a:b]

katalog_src = window_span("window._KATALOG_META=", 'window._KX={')
erloes_src = window_span("window._ERLOES_META =", "window._KURZ = {")

js = ['var window={_fx:function(s){return {"__fx":s};}};']
for names in GROUPS.values():
    for n in names:
        js.append(find_const_block(n) + ";")
js.append(katalog_src)
js.append(erloes_src)

js.append("var OLD={};")
for g, names in GROUPS.items():
    js.append('OLD["%s"]={%s};' % (g, ",".join('"%s":%s' % (n, n) for n in names)))
js.append('OLD.erloes2026._ERLOES_META=window._ERLOES_META; OLD.erloes2026._DRG=window._DRG;'
          'OLD.erloes2026._HDRG=window._HDRG; OLD.erloes2026._KURZ=window._KURZ;')
js.append('OLD.katalog2026={_KATALOG_META:window._KATALOG_META,_KX:window._KX,_HD:window._HD};')

js.append("var NEW={};")
for g in list(GROUPS) + ["katalog2026"]:
    p = os.path.join(REPO, "data", g + ".json")
    js.append('NEW["%s"]=JSON.parse(readFile(%s));' % (g, json.dumps(p)))

js.append("""
var diffs=0, leaves=0;
function typ(x){ return x===null?"null":Array.isArray(x)?"array":typeof x; }
function melde(pfad,alt,neu){
  diffs++;
  print("ABWEICHUNG "+pfad+"\\n  alt: "+JSON.stringify(alt)+"\\n  neu: "+JSON.stringify(neu));
}
function cmp(a,b,pfad){
  var ta=typ(a), tb=typ(b);
  if(ta!==tb){ melde(pfad,a,b); return; }
  if(ta==="object"){
    var ka=Object.keys(a), kb=Object.keys(b).filter(function(k){return k!=="_kommentar";});
    if(ka.join("\\u0000")!==kb.join("\\u0000")){
      if(ka.slice().sort().join("\\u0000")===kb.slice().sort().join("\\u0000"))
        melde(pfad+" [SCHLUESSEL-REIHENFOLGE]",ka,kb);
      else {
        ka.forEach(function(k){ if(kb.indexOf(k)<0) melde(pfad+"."+k+" [FEHLT NEU]",a[k],undefined); });
        kb.forEach(function(k){ if(ka.indexOf(k)<0) melde(pfad+"."+k+" [ZUSAETZLICH NEU]",undefined,b[k]); });
      }
    }
    ka.forEach(function(k){ if(k in b) cmp(a[k],b[k],pfad+"."+k); });
  } else if(ta==="array"){
    if(a.length!==b.length) melde(pfad+" [LAENGE]",a.length,b.length);
    var n=Math.min(a.length,b.length);
    for(var i=0;i<n;i++) cmp(a[i],b[i],pfad+"["+i+"]");
  } else {
    leaves++;
    if(a!==b) melde(pfad,a,b);
  }
}
var groups=Object.keys(OLD);
groups.forEach(function(g){
  var before=diffs, lb=leaves;
  cmp(OLD[g],NEW[g],g);
  print((diffs===before?"OK      ":"FEHLER  ")+"data/"+g+".json  ("+(leaves-lb)+" Werte verglichen"+(diffs>before?", "+(diffs-before)+" Abweichungen":"")+")");
});
print("");
print(diffs===0 ? "ERGEBNIS: IDENTISCH — "+leaves+" Einzelwerte verglichen, 0 Abweichungen."
                : "ERGEBNIS: "+diffs+" ABWEICHUNGEN bei "+leaves+" verglichenen Einzelwerten!");
if(diffs>0) throw new Error("Abweichungen gefunden");
""")

with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
    f.write("\n".join(js))
    tmp = f.name
r = subprocess.run([JSC, tmp], capture_output=True, text=True, encoding="utf-8")
os.unlink(tmp)
sys.stdout.write(r.stdout)
if r.returncode != 0:
    sys.stdout.write(r.stderr[-500:])
    sys.exit(1)
