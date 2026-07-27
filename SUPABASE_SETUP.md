# Supabase-Einrichtung (Stufe 2 — Inhalte hinter Login)

Diese Anleitung führt einmalig durch die Einrichtung. Danach lädt die Toolbox auf GitHub Pages die Inhalte nur noch nach Anmeldung aus einem privaten Supabase-Bucket; lokal (Dev-Server) lädt sie weiterhin aus `./data/`.

## 1. Projekt anlegen (ca. 5 Minuten)

1. Auf https://supabase.com ein Konto anlegen und **New project** klicken.
2. Name z. B. `fusszentrum-toolbox`, Region **Frankfurt (eu-central-1)**, Free-Tier reicht. Das Datenbank-Passwort sicher ablegen (wird für die Toolbox selbst nicht gebraucht).

## 2. Anmeldung konfigurieren (nur eingeladene Nutzer)

1. **Authentication → Sign In / Providers → Email**: aktiviert lassen.
2. Wichtig: **„Allow new users to sign up" AUSSCHALTEN** — sonst könnte sich jeder selbst registrieren.
3. Nutzer anlegen: **Authentication → Users → Add user → Create new user** — E-Mail + Passwort vergeben, **„Auto Confirm User" anhaken**. Für jedes Team-Mitglied wiederholen.

## 3. Privaten Storage-Bucket anlegen und Daten hochladen

1. **Storage → New bucket**: Name exakt `toolbox-data`, **Public bucket: AUS** (privat).
2. Die zehn Dateien aus dem lokalen `data/`-Ordner in den Bucket hochladen (Drag & Drop, Dateinamen unverändert):
   `katalog2026.json, erloes2026.json, diagnosen.json, opmethoden.json, opsteuerung.json, endo.json, preise.json, optexte.json, aufklaerung.json, referenz.json`

## 4. Lese-Policy für eingeloggte Nutzer

**SQL Editor → New query**, folgendes ausführen:

```sql
create policy "Eingeloggte duerfen Toolbox-Daten lesen"
on storage.objects for select
to authenticated
using (bucket_id = 'toolbox-data');
```

Keine weiteren Policies anlegen — ohne insert/update/delete-Policy kann über den anon-Key niemand schreiben.

## 5. Zugangsdaten in index.html eintragen

**Project Settings → API** (bzw. „Data API"): dort stehen **Project URL** und der **anon public**-Key. Beide in index.html in den Block `window.TOOLBOX_AUTH` eintragen:

```js
window.TOOLBOX_AUTH = {
  url: "https://xxxxx.supabase.co",
  anonKey: "eyJhbGciOi...",
  bucket: "toolbox-data"
};
```

Der anon-Key ist bewusst öffentlich (er steht in jeder Supabase-Webapp im Quelltext); der Schutz kommt aus der Policy in Schritt 4.

## 6. Testen — erst lokal, dann deployen

1. Dev-Server starten und **http://localhost:8000/index.html?auth=1** öffnen (`?auth=1` erzwingt lokal den Login-Pfad).
2. Mit einem angelegten Nutzer anmelden — die App muss vollständig laden. Der „Abmelden"-Link erscheint unten rechts.
3. Erst wenn das klappt: `index.html` auf GitHub hochladen.

## 7. data/-Ordner aus dem GitHub-Repo entfernen

Nach erfolgreichem Test den Ordner `data/` im GitHub-Repo **löschen** (im Web: Ordner öffnen → jede Datei → Delete file, oder per Commit „data/ entfernt"). Sonst bleiben die Inhalte trotz Login öffentlich abrufbar. Lokal bleibt `data/` erhalten (Dev-Server + Quelle für Supabase-Uploads).

**Ehrlicher Hinweis zur Git-Historie:** Die bisherigen Commits (eingebettete index.html, data/-Ordner) bleiben in der öffentlichen Historie einsehbar. Wer gezielt sucht, findet die 2026er-Daten dort weiterhin. Wenn das stört, gibt es zwei Optionen, beide mit Aufwand: die Historie neu aufsetzen (neues Repo bzw. Orphan-Branch nur mit aktuellem Stand) — dabei ändert sich die GitHub-Pages-URL nicht, wenn Repo-Name gleich bleibt — oder es pragmatisch akzeptieren, weil der Schutz vor allem für künftige Katalog-Jahrgänge greift.

## Nutzer einladen & Passwort vergessen (eingerichtet 07/2026)

Die App enthält einen „Passwort vergessen?"-Link in der Login-Maske und eine Empfangsseite für Einladungs-/Reset-Links („Neues Passwort setzen"). Damit die Mail-Links funktionieren, muss im Dashboard einmalig die URL-Konfiguration stimmen:

**Authentication → URL Configuration** (Stand nach Domain-Umzug 07/2026):
- **Site URL:** `https://fuss-track.de/app.html` — WICHTIG: auf die App-Seite zeigen, nicht auf die Landingpage; Dashboard-Einladungen („Invite user") schicken die Empfänger an genau diese Adresse.
- **Redirect URLs:**
  - `https://fuss-track.de/*`
  - `http://localhost:8000/*` (für lokale Tests)
  - (`https://benjaminbreuer-85.github.io/...` kann als Altlast entfernt werden, sobald alles auf der Domain läuft)

**Neuen Nutzer aufnehmen:** Authentication → Users → **Invite user** → E-Mail eintragen. Die Person bekommt eine Einladungs-Mail, klickt den Link, landet in der Toolbox auf „Neues Passwort setzen" und ist danach drin. Kein Passwort-Handling durch den Admin. Zugang entziehen: Users → Drei-Punkte-Menü → Delete user (wirkt sofort).

**Passwort vergessen:** Nutzer trägt in der Login-Maske seine E-Mail ein, klickt „Passwort vergessen?", bekommt eine Mail und setzt über den Link ein neues Passwort. Ohne Admin-Beteiligung. Hinweis: Der kostenlose eingebaute Mail-Versand von Supabase ist auf wenige Mails pro Stunde begrenzt — für ein kleines Team ausreichend.

## Tabellen für „Meine Implantatpreise" (einmalig)

**SQL Editor → New query**, alles einfügen und **Run**. Danach läuft alles automatisch — die App legt Preise selbst an, aktualisiert und liest sie; pro Nutzer getrennt, ohne weiteres Zutun im Dashboard.

```sql
-- 1) Preisliste je Nutzer (die einzige Preisquelle)
create table if not exists public.implantatpreise (
  user_id          uuid    not null references auth.users(id) on delete cascade,
  implantat_id     text    not null,
  bezeichnung      text    not null,
  hersteller       text,
  artikelnummer    text,
  preis            numeric(10,2),
  eigene_position  boolean not null default false,
  aktualisiert     timestamptz not null default now(),
  primary key (user_id, implantat_id)
);

-- 2) Materialsatz je Nutzer (Abweichungen vom Standard-Vorschlag)
create table if not exists public.materialsatz (
  user_id        uuid    not null references auth.users(id) on delete cascade,
  eingriff_id    text    not null,
  variante       text    not null default 'Standard',
  implantat_id   text    not null,
  anzahl         integer not null default 1,
  eingriff_name  text,
  sortierung     integer not null default 0,
  aktualisiert   timestamptz not null default now(),
  primary key (user_id, eingriff_id, variante, implantat_id)
);

-- 3) Zugriffsschutz: jeder sieht und ändert ausschließlich seine eigenen Zeilen
alter table public.implantatpreise enable row level security;
alter table public.materialsatz    enable row level security;

create policy "nur eigene Preise" on public.implantatpreise
  for all to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id);

create policy "nur eigener Materialsatz" on public.materialsatz
  for all to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id);
```

Erfolgsmeldung ist „Success. No rows returned".

**Kontrolle** (die Anzeige im Table Editor unterscheidet sich je nach Supabase-Version — diese Abfrage ist eindeutig). Neue Query, einfügen, Run:

```sql
select t.tablename,
       t.rowsecurity as rls_aktiv,
       count(p.policyname) as policies
from pg_tables t
left join pg_policies p on p.tablename = t.tablename and p.schemaname = 'public'
where t.schemaname = 'public'
  and t.tablename in ('implantatpreise','materialsatz')
group by t.tablename, t.rowsecurity;
```

Richtig ist: **zwei Zeilen**, bei beiden `rls_aktiv = true` und `policies = 1`. Kommt gar keine Zeile zurück, wurde der Block darüber noch nicht ausgeführt.

## Jahres-Update ab jetzt (z. B. Katalog 2027)

1. Neue JSON lokal in `data/` ablegen (aus den Master-Excel-Dateien, 1:1-Regel!).
2. Lokal testen (`http://localhost:8000/index.html`).
3. Datei im Supabase-Bucket ersetzen (Storage → Datei überschreiben). **Nicht** mehr zu GitHub hochladen.
