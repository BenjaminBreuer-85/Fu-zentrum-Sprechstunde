// ============================================================================
// paddle-webhook — Supabase Edge Function
//
// Nimmt Paddle-Billing-Ereignisse entgegen und loest fuer Kaeufer eine
// Einladung aus. Ab da uebernimmt die bereits bewaehrte Kette: Supabase
// verschickt die Einladungsmail ueber Brevo, der Empfaenger landet auf
// "Neues Passwort setzen" (Site URL zeigt auf /app.html) und ist danach drin.
//
// GRUNDSAETZE
//   - Das Webhook-Secret steht NIE im Code und nie im Repo. Es kommt aus den
//     Supabase-Secrets: supabase secrets set PADDLE_WEBHOOK_SECRET=...
//   - Ohne gueltige Signatur wird nichts verarbeitet — Antwort 401.
//   - Jedes Ereignis wird genau einmal verarbeitet (Tabelle paddle_events).
//     Wiederholungszustellungen von Paddle sind No-ops mit Antwort 200.
//   - Ein bereits registrierter Kaeufer ist KEIN Fehler, nur ein Protokolleintrag.
//
// SIGNATURPRUEFUNG (Paddle Billing)
//   Header:  Paddle-Signature: ts=<unix>;h1=<hex>
//   Grundlage: HMAC-SHA256 ueber "<ts>:<roher Body>", Schluessel = Webhook-Secret.
//   Der Body muss dafuer ROH gelesen werden — erst pruefen, dann JSON parsen.
// ============================================================================

import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.4";

// Aelter als das hier akzeptieren wir nicht (Schutz vor Wiedereinspielung).
const MAX_ALTER_SEKUNDEN = 60 * 5;

// Diese Ereignisse loesen eine Einladung aus.
const EINLADUNGS_EREIGNISSE = new Set([
  "transaction.completed",
  "subscription.activated",
]);

function hexZuBytes(hex: string): Uint8Array {
  const sauber = hex.trim().toLowerCase();
  const out = new Uint8Array(sauber.length / 2);
  for (let i = 0; i < out.length; i++) {
    out[i] = parseInt(sauber.substr(i * 2, 2), 16);
  }
  return out;
}

// Zeitkonstanter Vergleich — verhindert, dass sich das Secret ueber
// Laufzeitunterschiede Byte fuer Byte erraten laesst.
function gleichZeitkonstant(a: Uint8Array, b: Uint8Array): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a[i] ^ b[i];
  return diff === 0;
}

function signaturKopfLesen(kopf: string | null): { ts: string; h1: string } | null {
  if (!kopf) return null;
  let ts = "", h1 = "";
  for (const teil of kopf.split(";")) {
    const i = teil.indexOf("=");
    if (i < 0) continue;
    const schluessel = teil.slice(0, i).trim();
    const wert = teil.slice(i + 1).trim();
    if (schluessel === "ts") ts = wert;
    else if (schluessel === "h1") h1 = wert;
  }
  if (!ts || !h1) return null;
  if (!/^\d+$/.test(ts)) return null;
  if (!/^[0-9a-fA-F]+$/.test(h1) || h1.length % 2 !== 0) return null;
  return { ts, h1 };
}

async function signaturGueltig(
  rohBody: string,
  kopf: string | null,
  secret: string,
): Promise<{ ok: boolean; grund?: string }> {
  const teile = signaturKopfLesen(kopf);
  if (!teile) return { ok: false, grund: "Signatur-Kopfzeile fehlt oder ist unlesbar" };

  const alter = Math.abs(Math.floor(Date.now() / 1000) - Number(teile.ts));
  if (alter > MAX_ALTER_SEKUNDEN) {
    return { ok: false, grund: `Zeitstempel ist ${alter} s alt` };
  }

  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signatur = new Uint8Array(
    await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(`${teile.ts}:${rohBody}`)),
  );

  if (!gleichZeitkonstant(signatur, hexZuBytes(teile.h1))) {
    return { ok: false, grund: "Signatur passt nicht" };
  }
  return { ok: true };
}

// Paddle legt die Kaeufer-Adresse je nach Ereignis an unterschiedliche Stellen.
// Wir sehen der Reihe nach nach und melden ausdruecklich, wenn keine dabei ist —
// ein bezahlter Kauf ohne Adresse darf nicht stillschweigend verfallen.
function emailLesen(daten: Record<string, unknown>): string | null {
  const kandidaten: unknown[] = [
    (daten?.customer as Record<string, unknown> | undefined)?.email,
    daten?.customer_email,
    (daten?.custom_data as Record<string, unknown> | undefined)?.email,
    (daten?.billing_details as Record<string, unknown> | undefined)?.email,
  ];
  for (const k of kandidaten) {
    if (typeof k === "string" && k.includes("@")) return k.trim().toLowerCase();
  }
  return null;
}

function antwort(status: number, koerper: Record<string, unknown>): Response {
  return new Response(JSON.stringify(koerper), {
    status,
    headers: { "content-type": "application/json" },
  });
}

Deno.serve(async (req: Request): Promise<Response> => {
  if (req.method !== "POST") return antwort(405, { fehler: "nur POST" });

  const secret = Deno.env.get("PADDLE_WEBHOOK_SECRET");
  if (!secret) {
    // Fehlkonfiguration — nicht als "ungueltig" tarnen, sonst sucht man lange.
    console.error("PADDLE_WEBHOOK_SECRET ist nicht gesetzt");
    return antwort(500, { fehler: "Webhook-Secret fehlt in der Konfiguration" });
  }

  // ROH lesen: die Signatur gilt fuer genau diese Bytes.
  const rohBody = await req.text();

  const pruefung = await signaturGueltig(rohBody, req.headers.get("Paddle-Signature"), secret);
  if (!pruefung.ok) {
    console.warn("Signatur abgelehnt:", pruefung.grund);
    return antwort(401, { fehler: "Signatur ungültig" });
  }

  let ereignis: Record<string, unknown>;
  try {
    ereignis = JSON.parse(rohBody);
  } catch {
    return antwort(400, { fehler: "Body ist kein JSON" });
  }

  const eventId = String(ereignis.event_id ?? "");
  const eventType = String(ereignis.event_type ?? "");
  if (!eventId || !eventType) {
    return antwort(400, { fehler: "event_id oder event_type fehlt" });
  }

  const admin = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  // ---- Idempotenz: Ereignis beanspruchen ----------------------------------
  // Der Eintrag wird VOR der Einladung gesetzt. Gelingt der Insert nicht, weil
  // die event_id schon existiert, war das Ereignis bereits da -> No-op.
  const { data: beansprucht, error: insertFehler } = await admin
    .from("paddle_events")
    .insert({ event_id: eventId, event_type: eventType, status: "in_arbeit" })
    .select("event_id")
    .maybeSingle();

  if (insertFehler && insertFehler.code === "23505") {
    console.log("Wiederholungszustellung, nichts zu tun:", eventId);
    return antwort(200, { ok: true, hinweis: "bereits verarbeitet", event_id: eventId });
  }
  if (insertFehler) {
    console.error("paddle_events-Insert fehlgeschlagen:", insertFehler.message);
    return antwort(500, { fehler: "Protokoll konnte nicht geschrieben werden" });
  }
  if (!beansprucht) {
    return antwort(200, { ok: true, hinweis: "bereits verarbeitet", event_id: eventId });
  }

  // Ab hier gilt: wir haben das Ereignis beansprucht. Scheitert die Arbeit,
  // geben wir den Anspruch wieder frei, damit Paddles Wiederholung greift.
  async function anspruchFreigeben() {
    await admin.from("paddle_events").delete().eq("event_id", eventId);
  }

  async function abschliessen(status: string, email: string | null, hinweis: string | null) {
    await admin.from("paddle_events")
      .update({ status, email, hinweis, nutzlast: ereignis })
      .eq("event_id", eventId);
  }

  try {
    if (!EINLADUNGS_EREIGNISSE.has(eventType)) {
      await abschliessen("ignoriert", null, "Ereignistyp loest keine Einladung aus");
      return antwort(200, { ok: true, hinweis: "ignoriert", event_type: eventType });
    }

    const daten = (ereignis.data ?? {}) as Record<string, unknown>;
    const email = emailLesen(daten);
    const subscriptionId = typeof daten.subscription_id === "string"
      ? daten.subscription_id
      : (eventType === "subscription.activated" && typeof daten.id === "string" ? daten.id : null);
    const customerId = typeof daten.customer_id === "string" ? daten.customer_id : null;

    if (!email) {
      // Sichtbar ablegen statt verwerfen. 200, damit Paddle nicht endlos
      // wiederholt — der Fall braucht eine Hand, keine Zustellwiederholung.
      console.error("Kaeufer-E-Mail fehlt im Ereignis", eventId);
      await abschliessen("email_fehlt", null, "Keine E-Mail im Ereignis gefunden — bitte manuell einladen");
      return antwort(200, { ok: true, hinweis: "E-Mail fehlt, Ereignis protokolliert" });
    }

    // ---- Mapping subscription_id <-> E-Mail ------------------------------
    // Nur speichern. Die Behandlung von Kuendigungen ist ausdruecklich NICHT
    // Teil dieser Etappe — diese Tabelle ist deren Grundlage.
    if (subscriptionId) {
      const { error: aboFehler } = await admin.from("paddle_abos").upsert({
        subscription_id: subscriptionId,
        email,
        customer_id: customerId,
        status: eventType === "subscription.activated" ? "aktiv" : null,
        aktualisiert_am: new Date().toISOString(),
      }, { onConflict: "subscription_id" });
      if (aboFehler) console.error("paddle_abos-Upsert fehlgeschlagen:", aboFehler.message);
    }

    // ---- Einladung --------------------------------------------------------
    const { error: einladungsFehler } = await admin.auth.admin.inviteUserByEmail(email);

    if (einladungsFehler) {
      const meldung = String(einladungsFehler.message || "");
      const schonDa = /already been registered|already registered|already exists/i.test(meldung);
      if (schonDa) {
        console.log("Adresse bereits registriert, keine neue Einladung:", email);
        await abschliessen("bereits_registriert", email, meldung);
        return antwort(200, { ok: true, hinweis: "bereits registriert", email });
      }
      // Echter Fehler: Anspruch freigeben, 500 -> Paddle wiederholt.
      console.error("Einladung fehlgeschlagen:", meldung);
      await anspruchFreigeben();
      return antwort(500, { fehler: "Einladung fehlgeschlagen" });
    }

    await abschliessen("eingeladen", email, null);
    console.log("Einladung verschickt an", email);
    return antwort(200, { ok: true, hinweis: "eingeladen", email });

  } catch (e) {
    console.error("Unerwarteter Fehler:", e instanceof Error ? e.message : String(e));
    await anspruchFreigeben();
    return antwort(500, { fehler: "unerwarteter Fehler" });
  }
});
