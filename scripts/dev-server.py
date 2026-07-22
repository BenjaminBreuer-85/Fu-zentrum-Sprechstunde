#!/usr/bin/env python3
"""Lokaler Entwicklungsserver mit Live-Reload für die Fußzentrum-Toolbox.

Start:  python3 scripts/dev-server.py   (aus dem Repo-Root)
Adresse: http://localhost:8000/index.html

Funktionsweise: Serviert das Repo-Verzeichnis wie python3 -m http.server und
injiziert in jede ausgelieferte HTML-Seite ein kleines Skript, das jede Sekunde
/__livereload abfragt. Ein Hintergrund-Thread überwacht die Datei-Änderungszeiten
im Repo (ohne .git); ändert sich etwas, lädt der Browser die Seite neu.
Die Dateien selbst werden dabei nicht verändert.
"""
import http.server
import os
import sys
import threading
import time

PORT = int(os.environ.get("PORT", "8000"))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORE_DIRS = {".git", "__pycache__", ".claude"}

_version = 0
_lock = threading.Lock()

LIVERELOAD_SNIPPET = b"""
<script>
(function(){
  var v=null;
  setInterval(function(){
    fetch('/__livereload').then(function(r){return r.text();}).then(function(t){
      if(v===null){v=t;} else if(t!==v){location.reload();}
    }).catch(function(){});
  },1000);
})();
</script>
"""


def scan_mtimes():
    newest = 0.0
    count = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for f in filenames:
            try:
                m = os.stat(os.path.join(dirpath, f)).st_mtime
            except OSError:
                continue
            count += 1
            if m > newest:
                newest = m
    return (newest, count)


def watcher():
    global _version
    last = scan_mtimes()
    while True:
        time.sleep(0.5)
        cur = scan_mtimes()
        if cur != last:
            last = cur
            with _lock:
                _version += 1


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        if self.path.startswith("/__livereload"):
            with _lock:
                body = str(_version).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path in ("/", ""):
            self.path = "/index.html"
        path = self.translate_path(self.path.split("?")[0])
        if path.endswith(".html") and os.path.isfile(path):
            with open(path, "rb") as f:
                content = f.read()
            if b"</body>" in content:
                content = content.replace(b"</body>", LIVERELOAD_SNIPPET + b"</body>", 1)
            else:
                content += LIVERELOAD_SNIPPET
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        super().do_GET()

    def end_headers(self):
        # Kein Browser-Caching im Dev-Betrieb — Änderungen sollen sofort sichtbar sein
        buf = getattr(self, "_headers_buffer", [])
        if b"Cache-Control" not in b"".join(buf):
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        if "/__livereload" in (args[0] if args else ""):
            return  # Polling nicht loggen
        sys.stderr.write("%s - %s\n" % (self.log_date_time_string(), fmt % args))


def main():
    threading.Thread(target=watcher, daemon=True).start()
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print("Dev-Server läuft: http://localhost:%d/index.html (Live-Reload aktiv, Strg+C beendet)" % PORT)
    server.serve_forever()


if __name__ == "__main__":
    main()
