-- ===========================================================================
-- Paddle-Webhook: Ereignisprotokoll und Abo-Zuordnung
--
-- Beide Tabellen enthalten Zahlungs- und Kontaktdaten und gehen ausschliesslich
-- die Edge Function etwas an. Deshalb: RLS an, aber KEINE Policies. Ohne Policy
-- kommt niemand durch — weder anon noch ein angemeldeter Nutzer. Die
-- service_role, mit der die Function arbeitet, umgeht RLS ohnehin.
-- ===========================================================================

-- --------------------------------------------------------------------------
-- paddle_events — jedes Ereignis genau einmal
--
-- event_id ist der Primaerschluessel. Die Function beansprucht ein Ereignis per
-- INSERT, bevor sie arbeitet: schlaegt der INSERT wegen Schluesselkonflikt fehl,
-- war das Ereignis schon da und die Zustellung ist ein No-op. Scheitert die
-- anschliessende Arbeit, loescht die Function den Anspruch wieder, damit Paddles
-- Wiederholung greifen kann.
--
-- status:
--   in_arbeit           beansprucht, Arbeit laeuft (bleibt nur kurz stehen)
--   eingeladen          Einladung ist raus
--   bereits_registriert Adresse hatte schon ein Konto — kein Fehler
--   email_fehlt         Kauf ohne Adresse im Ereignis; braucht eine Hand
--   ignoriert           Ereignistyp loest keine Einladung aus
-- --------------------------------------------------------------------------
create table if not exists public.paddle_events (
  event_id     text primary key,
  event_type   text        not null,
  status       text        not null default 'in_arbeit',
  email        text,
  hinweis      text,
  nutzlast     jsonb,
  empfangen_am timestamptz not null default now()
);

comment on table public.paddle_events is
  'Ereignisprotokoll des Paddle-Webhooks. event_id sichert die Einmalverarbeitung.';

create index if not exists paddle_events_empfangen_am_idx
  on public.paddle_events (empfangen_am desc);
create index if not exists paddle_events_status_idx
  on public.paddle_events (status);

alter table public.paddle_events enable row level security;
-- Bewusst keine Policy: nur service_role (umgeht RLS) kommt heran.

-- --------------------------------------------------------------------------
-- paddle_abos — Zuordnung subscription_id <-> E-Mail
--
-- Grundlage fuer die spaetere Kuendigungs-Behandlung. In dieser Etappe wird
-- ausschliesslich GESPEICHERT; es haengt noch keine Logik daran.
-- --------------------------------------------------------------------------
create table if not exists public.paddle_abos (
  subscription_id text primary key,
  email           text        not null,
  customer_id     text,
  status          text,
  angelegt_am     timestamptz not null default now(),
  aktualisiert_am timestamptz not null default now()
);

comment on table public.paddle_abos is
  'Zuordnung Paddle-Abo zu E-Mail. Speichern only — Kuendigungs-Behandlung folgt spaeter.';

create index if not exists paddle_abos_email_idx on public.paddle_abos (email);

alter table public.paddle_abos enable row level security;
-- Bewusst keine Policy: nur service_role (umgeht RLS) kommt heran.
