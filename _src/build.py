"""Builds the Edgelings website. Run from the repository root: python _src/build.py

Every page shares 1 shell (head, navigation, footer). Page bodies live in _src/pages/*.html.
GitHub Pages does not publish folders that start with an underscore, so _src never goes live.
"""
import hashlib, html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / '_src'
SITE = 'https://edgelings.com'
UPDATED = '2026-11-18'

PAGES = [
    # file, title, description, nav key, in sitemap
    ('index.html', 'Edgelings: close to the edge, not over it',
     'A free casual game for iPhone and Android. Flick glossy slimes across the table. The closer they stop to the edge, the more they score. Over the edge scores nothing.', 'home', True),
    ('support.html', 'Support | Edgelings',
     'Help with Edgelings: player name, lost progress, purchases, ads choices and how to delete your account.', 'support', True),
    ('privacy.html', 'Privacy Policy | Edgelings',
     'How Edgelings handles your data: anonymous player accounts, rankings, purchases, ads and statistics only with your consent, and your GDPR rights.', 'privacy', True),
    ('terms.html', 'Terms and Conditions | Edgelings',
     'Terms and Conditions for the Edgelings game, including player names, fair play, coins and in-app purchases.', 'terms', True),
    ('404.html', 'Page not found | Edgelings', 'Page not found on edgelings.com.', '', False),
]

css = (ROOT / 'assets' / 'site.css').read_bytes()
CSSV = hashlib.md5(css).hexdigest()[:8]

APPLE = '<svg width="26" height="30" viewBox="0 0 24 28" aria-hidden="true"><path fill="#fff" d="M19.6 14.9c0-3 2.5-4.5 2.6-4.6-1.4-2.1-3.6-2.4-4.4-2.4-1.9-.2-3.6 1.1-4.6 1.1-1 0-2.4-1.1-4-1-2 0-3.9 1.2-5 3-2.1 3.7-.5 9.2 1.5 12.2 1 1.5 2.2 3.1 3.8 3 1.5-.1 2.1-1 3.9-1s2.3 1 3.9 1c1.6 0 2.7-1.5 3.7-3 1.2-1.7 1.6-3.3 1.7-3.4-.1 0-3.1-1.2-3.1-4.9zM16.6 5.9c.8-1 1.4-2.4 1.2-3.8-1.2.1-2.6.8-3.5 1.8-.8.9-1.5 2.3-1.3 3.7 1.3.1 2.7-.7 3.6-1.7z"/></svg>'
PLAY = '<svg width="26" height="28" viewBox="0 0 24 26" aria-hidden="true"><path fill="#3BCCFF" d="M1.2.6 13.3 12.7 1.2 24.8c-.4-.2-.7-.7-.7-1.3V1.9c0-.6.3-1.1.7-1.3z"/><path fill="#FFD400" d="m17.4 8.6-4.1 4.1 4.1 4.1 4.6-2.6c1.3-.8 1.3-2.1 0-2.9z"/><path fill="#FF3A44" d="M13.3 12.7 1.2 24.8c.4.2 1 .2 1.6-.2l14.6-8.3z"/><path fill="#48FF48" d="M13.3 12.7 17.4 8.6 2.8.4C2.2 0 1.6 0 1.2.2z"/></svg>'

def badges():
    # Store links go here once the game is live. Until then the badges say "Coming soon".
    links = json.loads((SRC / 'stores.json').read_text(encoding='utf-8'))
    out = []
    for key, icon, name, live_label in (('ios', APPLE, 'App Store', 'Download on the'), ('android', PLAY, 'Google Play', 'Get it on')):
        url = links.get(key, '')
        if url:
            out.append(f'<a class="badge" href="{html.escape(url)}" rel="noopener">{icon}<span><small>{live_label}</small><b>{name}</b></span></a>')
        else:
            out.append(f'<span class="badge soon" aria-label="{name}, coming soon">{icon}<span><small>Coming soon</small><b>{name}</b></span></span>')
    return '<div class="badges">' + ''.join(out) + '</div>'

def shell(file, title, desc, key, body):
    url = SITE + ('/' if file == 'index.html' else '/' + file)
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{h}"{cur if key == k else ""}>{n}</a>'
                  for k, h, n in (('support', '/support.html', 'Support'), ('privacy', '/privacy.html', 'Privacy'), ('terms', '/terms.html', 'Terms')))
    ld = {'@context': 'https://schema.org', '@type': 'VideoGame', 'name': 'Edgelings', 'url': SITE + '/',
          'description': PAGES[0][2], 'gamePlatform': ['iOS', 'Android'], 'applicationCategory': 'GameApplication',
          'operatingSystem': 'iOS, Android', 'image': SITE + '/img/icon-512.png',
          'author': {'@type': 'Person', 'name': 'Matej Mesko'}, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'}}
    extra = '<meta name="robots" content="noindex">' if file == '404.html' else f'<link rel="canonical" href="{url}">'
    head_ld = f'<script type="application/ld+json">{json.dumps(ld)}</script>' if file == 'index.html' else ''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{extra}
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta name="theme-color" content="#1B1233">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/fonts/lilita-one-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={CSSV}">
{head_ld}</head><body>
<nav aria-label="Main"><a class="logo" href="/" aria-label="Edgelings home"><img src="/img/logo.webp" alt="Edgelings" width="900" height="261"></a><span class="links">{nav}</span></nav>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
<div class="brand"><img src="/img/icon-192.png" alt="" width="44" height="44"><span><b>Edgelings</b>Close to the edge. Not over it.</span></div>
<div class="flinks"><a href="/support.html">Support</a><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a><a href="mailto:info@edgelings.com">info@edgelings.com</a></div>
<p class="op">Edgelings is operated by Matej Mesko, Slovenia.</p>
</div></footer>
</body></html>
'''

def build():
    for file, title, desc, key, _ in PAGES:
        body = (SRC / 'pages' / file).read_text(encoding='utf-8').replace('{{BADGES}}', badges())
        (ROOT / file).write_text(shell(file, title, desc, key, body), encoding='utf-8', newline='\n')
    urls = ''.join(f'<url><loc>{SITE}{"/" if f == "index.html" else "/" + f}</loc><lastmod>{UPDATED}</lastmod></url>'
                   for f, *_, s in PAGES if s)
    (ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding='utf-8')
    # Writing checks: no em dashes, no contractions, no exclamation marks in page text.
    for file, *_ in PAGES:
        text = re.sub(r'<[^>]+>', ' ', (ROOT / file).read_text(encoding='utf-8'))
        for bad in ('—', "n't", '!'):
            if bad in text:
                print(f'warning: {file} contains {bad!r}')
    print('built', len(PAGES), 'pages, css', CSSV)

if __name__ == '__main__':
    build()
