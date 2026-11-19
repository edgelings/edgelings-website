# edgelings.com

Static website for the Edgelings game, hosted on GitHub Pages from the main branch.

## Pages

- `index.html` home: hero loop, playable demo, scoring strip, trailer and loops, screenshots, features, slimes, FAQ
- `support.html` support, FAQ and account deletion (store support URL, Google Play deletion URL)
- `press.html` press kit with `media/edgelings-press-kit.zip`
- `privacy.html`, `terms.html`
- `get.html` smart store link: edgelings.com/get sends iPhones to the App Store and Android phones to Google Play
- `demo/` the playable web demo, built from the app (see below)
- `media/` trailer, loops and screenshots
- `sitemap.xml`, `robots.txt`, `llms.txt`, `app-ads.txt`, IndexNow key file, `CNAME`, `404.html`

## Editing

- Page layout: `_src/pages/` (texts are `{{key}}` placeholders)
- All texts, FAQ included: `_src/i18n/en.json` (English source) and `_src/i18n/<lang>.json`
- Store links, App Store ID, public keys: `_src/config.json`
- Shell (head, header, footer): `_src/build.py`

After a change, run from this folder, then commit and push with GitHub Desktop:

```
python _src/build.py
```

After the push is live, tell search engines (Bing and other IndexNow engines):

```
python _src/indexnow.py
```

## Languages

24 languages: English at the root, the other 23 in folders (`/de/`, `/pt-br/`, `/zh-hans/` and so on).
Privacy, terms and 404 stay English only. Visitors are never redirected. A bar suggests their browser language once.
The language list, fonts and locales are at the top of `_src/build.py`.
A missing text falls back to English and the build reports it.

To change a text: edit `en.json`, then the same key in every language file.
New or changed texts go through the same steps as before: translator, 2 native reviewers, merge, safety check.
Briefs, glossaries, review logs and the checker are in `_src/i18n/work/`. Check a file with:

```
python _src/i18n/work/check.py _src/i18n/de.json
```

## Store links

Once the game is live, paste the links into `stores` in `_src/config.json`, set `smartBanner` to true, run the build and push.
The badges switch from Coming soon to real links and /get starts redirecting.

## Social links

Run `_src/supabase/site_links.sql` once in the Supabase SQL editor. Then switch a network on in the table `site_links`:
paste the url and tick `active`. The footer shows it at once, no push needed.

## Demo

Built from the app repository: `npx vite build --config vite.demo.config.ts`, then copy `dist-demo/` here as `demo/`
(rename `demo.html` to `index.html`, leave out `assets/icons`).

## Statistics

The site asks for cookie consent. Accept: PostHog with cookies. Decline: PostHog cookieless counts only.
Events: $pageview, demo_start, demo_level, demo_end, demo_close, get_click, store_click, trailer_play, faq_open, score_strip, social_click.
All carry `site: web` and `lang`.
