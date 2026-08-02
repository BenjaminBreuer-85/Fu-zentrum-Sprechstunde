#!/usr/bin/env python3
"""Gegenprobe fuer die Edge Function paddle-webhook (Etappe 1e).

Faehrt drei Faelle gegen die DEPLOYTE Function:

  1. korrekt signiertes Ereignis        -> 200, Einladung wird ausgeloest
  2. falsche Signatur                   -> 401, nichts passiert
  3. dasselbe Ereignis ein zweites Mal  -> 200 "bereits verarbeitet",
                                           KEINE zweite Einladung

Aufruf:

    export PADDLE_WEBHOOK_SECRET='...'        # dasselbe Secret wie in Supabase
    python3 scripts/paddle_webhook_pruefen.py \\
        --url https://<projekt>.supabase.co/functions/v1/paddle-webhook \\
        --email test@fuss-track.de

Das Secret wird NUR aus der Umgebung gelesen und nie ausgegeben. Es steht
weder in diesem Skript noch sonst im Repo.

Signatur nach Paddle Billing:
    Paddle-Signature: ts=<unix>;h1=<hex>
    h1 = HMAC-SHA256( key = Secret, msg = "<ts>:<roher Body>" )
Der Body muss byteweise derselbe sein, der gesendet wird — deshalb wird hier
einmal serialisiert und diese Bytes sowohl signiert als auch verschickt.
"""

import argparse
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid


def signieren(roh: bytes, secret: str, ts: int) -> str:
    grundlage = f"{ts}:".encode("utf-8") + roh
    return hmac.new(secret.encode("utf-8"), grundlage, hashlib.sha256).hexdigest()


def senden(url: str, roh: bytes, kopf: str):
    anfrage = urllib.request.Request(
        url, data=roh, method="POST",
        headers={"content-type": "application/json", "Paddle-Signature": kopf},
    )
    try:
        with urllib.request.urlopen(anfrage, timeout=30) as antwort:
            return antwort.status, antwort.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except Exception as e:  # Netzfehler o. ae.
        return None, f"{type(e).__name__}: {e}"


def ereignis_bauen(email: str, event_id: str) -> bytes:
    """Nachbau eines transaction.completed, so knapp wie moeglich."""
    return json.dumps({
        "event_id": event_id,
        "event_type": "transaction.completed",
        "occurred_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "data": {
            "id": "txn_" + uuid.uuid4().hex[:20],
            "status": "completed",
            "customer_id": "ctm_" + uuid.uuid4().hex[:20],
            "subscription_id": "sub_" + uuid.uuid4().hex[:20],
            "customer": {"email": email},
        },
    }, separators=(",", ":")).encode("utf-8")


def zeile(nummer, titel, erwartet, code, koerper, bestanden):
    zeichen = "OK    " if bestanden else "FEHLER"
    print(f"[{zeichen}] {nummer}. {titel}")
    print(f"          erwartet: {erwartet}")
    print(f"          erhalten: HTTP {code} — {koerper[:160]}")
    print()
    return bestanden


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True, help="Adresse der deployten Function")
    p.add_argument("--email", default="test@fuss-track.de")
    args = p.parse_args()

    secret = os.environ.get("PADDLE_WEBHOOK_SECRET")
    if not secret:
        print("PADDLE_WEBHOOK_SECRET ist nicht gesetzt — bitte vorher exportieren.",
              file=sys.stderr)
        return 2

    event_id = "evt_" + uuid.uuid4().hex[:24]
    roh = ereignis_bauen(args.email, event_id)
    ts = int(time.time())
    echt = signieren(roh, secret, ts)

    print(f"Ziel:      {args.url}")
    print(f"E-Mail:    {args.email}")
    print(f"event_id:  {event_id}")
    print()

    ergebnisse = []

    # 1) korrekt signiert
    code, koerper = senden(args.url, roh, f"ts={ts};h1={echt}")
    ergebnisse.append(zeile(
        1, "korrekt signiertes Ereignis", "HTTP 200, Hinweis 'eingeladen'",
        code, koerper, code == 200 and '"eingeladen"' in koerper))

    # 2) falsche Signatur — anderes Ereignis, damit Fall 3 sauber bleibt
    event_id2 = "evt_" + uuid.uuid4().hex[:24]
    roh2 = ereignis_bauen(args.email, event_id2)
    ts2 = int(time.time())
    falsch = signieren(roh2, secret + "x", ts2)
    code, koerper = senden(args.url, roh2, f"ts={ts2};h1={falsch}")
    ergebnisse.append(zeile(
        2, "falsche Signatur", "HTTP 401",
        code, koerper, code == 401))

    # 3) Wiederholungszustellung desselben Ereignisses
    ts3 = int(time.time())
    echt3 = signieren(roh, secret, ts3)
    code, koerper = senden(args.url, roh, f"ts={ts3};h1={echt3}")
    ergebnisse.append(zeile(
        3, "dasselbe Ereignis erneut", "HTTP 200, Hinweis 'bereits verarbeitet'",
        code, koerper, code == 200 and "bereits verarbeitet" in koerper))

    print("-" * 68)
    if all(ergebnisse):
        print("Alle drei Faelle bestanden.")
        print()
        print("Noch von Hand nachsehen, weil das Skript es nicht sehen kann:")
        print("  - Ist genau EINE Einladungsmail angekommen (nicht zwei)?")
        print("  - Steht in paddle_events genau eine Zeile zu " + event_id + ",")
        print("    Status 'eingeladen'?")
        print("  - Steht in paddle_abos die subscription_id mit derselben E-Mail?")
        return 0
    print("Mindestens ein Fall ist durchgefallen — siehe oben.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
