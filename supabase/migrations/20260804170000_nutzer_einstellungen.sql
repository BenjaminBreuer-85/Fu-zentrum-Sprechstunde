-- ===========================================================================
-- nutzer_einstellungen — kontogebundene Rundgang-Merker
--
-- Bisher lag der "schon gesehen"-Zustand nur im localStorage, also an Geraet
-- und Browser. Derselbe Nutzer bekam den Rundgang auf jedem neuen Geraet, in
-- jedem anderen Browser, im privaten Fenster und nach dem Loeschen der
-- Browserdaten erneut. Kuenftig ist der Server die Wahrheit, localStorage nur
-- noch Zwischenspeicher.
--
-- Bewusst NICHT hier abgelegt und weiterhin geraetegebunden:
--   ft-homescreen-gesehen  — auf einem neuen Geraet liegt die App dort noch
--                            nicht auf dem Startbildschirm, der Hinweis muss
--                            also wieder erscheinen.
--   ft-schriftgroesse      — am Telefon eine andere Groesse als am Rechner
--                            ist gewollt.
--
-- rundgaenge ist bewusst jsonb und keine vier Spalten: weitere Rundgaenge
-- kommen dann ohne Migration dazu. Inhalt z. B. {"menue":1,"sb":1}.
-- ===========================================================================
create table if not exists public.nutzer_einstellungen (
  user_id         uuid primary key references auth.users(id) on delete cascade,
  rundgaenge      jsonb       not null default '{}'::jsonb,
  aktualisiert_am timestamptz not null default now()
);

comment on table public.nutzer_einstellungen is
  'Kontogebundene Oberflaechen-Merker. Geraetegebundenes bleibt im localStorage.';

alter table public.nutzer_einstellungen enable row level security;

-- Jeder sieht und aendert ausschliesslich seine eigene Zeile.
drop policy if exists "eigene Einstellungen lesen"     on public.nutzer_einstellungen;
drop policy if exists "eigene Einstellungen schreiben" on public.nutzer_einstellungen;
drop policy if exists "eigene Einstellungen ändern"    on public.nutzer_einstellungen;

create policy "eigene Einstellungen lesen"
  on public.nutzer_einstellungen for select to authenticated
  using (auth.uid() = user_id);

create policy "eigene Einstellungen schreiben"
  on public.nutzer_einstellungen for insert to authenticated
  with check (auth.uid() = user_id);

create policy "eigene Einstellungen ändern"
  on public.nutzer_einstellungen for update to authenticated
  using (auth.uid() = user_id) with check (auth.uid() = user_id);
