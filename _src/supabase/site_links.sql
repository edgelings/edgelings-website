-- Social links for edgelings.com. Run once in the Supabase SQL editor (project Edgelings).
-- The website shows a link only when active is true and url is filled in.
-- To switch one on: Table editor, site_links, paste the url, tick active. Live at once, no push needed.
create table if not exists public.site_links (
  network text primary key check (network in ('tiktok','instagram','youtube','facebook','x','discord')),
  label   text not null,
  url     text not null default '',
  active  boolean not null default false,
  sort    smallint not null default 0
);
alter table public.site_links enable row level security;
drop policy if exists "site links readable when active" on public.site_links;
create policy "site links readable when active" on public.site_links for select to anon, authenticated using (active and url <> '');
grant select on public.site_links to anon, authenticated;
insert into public.site_links (network, label, sort) values
  ('tiktok','Edgelings on TikTok',1),('instagram','Edgelings on Instagram',2),('youtube','Edgelings on YouTube',3),
  ('facebook','Edgelings on Facebook',4),('x','Edgelings on X',5),('discord','Edgelings on Discord',6)
on conflict (network) do nothing;
