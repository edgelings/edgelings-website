"""Builds the Edgelings website in every language. Run from the repository root: python _src/build.py

- English lives at the root, every other language in its own folder (/de/, /pt-br/, /zh-hans/ ...).
- Page templates: _src/pages/*.html. A {{key}} is replaced by the text for that key in _src/i18n/<lang>.json.
  English (_src/i18n/en.json) is the source. A missing translation falls back to English and is reported.
- Translated: home, support, press kit, get page. English only (binding): privacy, terms, 404.
- The FAQ order lives in FAQ_IDS. Its texts are the faq_<id>_q and faq_<id>_a keys.
- Translations follow the app's process: translator, 2 native reviewers, merge, safety check.
  Work files, briefs and glossaries: _src/i18n/work/.
GitHub Pages does not publish folders that start with an underscore, so _src never goes live.
"""
import hashlib, html, json, pathlib, re, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / '_src'
SITE = 'https://edgelings.com'
UPDATED = '2026-11-19'
CFG = json.loads((SRC / 'config.json').read_text(encoding='utf-8'))
STORES = CFG['stores']

# code, folder, hreflang and html lang, native name, display font class (same choice as the app)
LANGS = [
    ('en', '', 'en', 'English', ''), ('id', 'id', 'id', 'Bahasa Indonesia', ''), ('de', 'de', 'de', 'Deutsch', ''),
    ('es', 'es', 'es-ES', 'Español (ES)', ''), ('es-419', 'es-419', 'es-419', 'Español (LatAm)', ''), ('fr', 'fr', 'fr', 'Français', ''),
    ('hr', 'hr', 'hr', 'Hrvatski', 'f-baloo'), ('it', 'it', 'it', 'Italiano', ''), ('nl', 'nl', 'nl', 'Nederlands', ''),
    ('pl', 'pl', 'pl', 'Polski', 'f-baloo'), ('pt', 'pt', 'pt-PT', 'Português (PT)', ''), ('pt-BR', 'pt-br', 'pt-BR', 'Português (BR)', ''),
    ('ro', 'ro', 'ro', 'Română', 'f-baloo'), ('sl', 'sl', 'sl', 'Slovenščina', 'f-baloo'), ('vi', 'vi', 'vi', 'Tiếng Việt', 'f-baloo'),
    ('tr', 'tr', 'tr', 'Türkçe', 'f-baloo'), ('ru', 'ru', 'ru', 'Русский', 'f-rubik'), ('uk', 'uk', 'uk', 'Українська', 'f-rubik'),
    ('hi', 'hi', 'hi', 'हिन्दी', 'f-baloo'), ('th', 'th', 'th', 'ไทย', 'f-sys'), ('ja', 'ja', 'ja', '日本語', 'f-sys'),
    ('ko', 'ko', 'ko', '한국어', 'f-sys'), ('zh-Hans', 'zh-hans', 'zh-Hans', '简体中文', 'f-sys'), ('zh-Hant', 'zh-hant', 'zh-Hant', '繁體中文', 'f-sys'),
]
OG_LOCALE = {'en': 'en_GB', 'id': 'id_ID', 'de': 'de_DE', 'es': 'es_ES', 'es-419': 'es_MX', 'fr': 'fr_FR', 'hr': 'hr_HR', 'it': 'it_IT', 'nl': 'nl_NL', 'pl': 'pl_PL',
             'pt': 'pt_PT', 'pt-BR': 'pt_BR', 'ro': 'ro_RO', 'sl': 'sl_SI', 'vi': 'vi_VN', 'tr': 'tr_TR', 'ru': 'ru_RU', 'uk': 'uk_UA', 'hi': 'hi_IN', 'th': 'th_TH',
             'ja': 'ja_JP', 'ko': 'ko_KR', 'zh-Hans': 'zh_CN', 'zh-Hant': 'zh_TW'}
FAQ_IDS = ['what', 'how', 'free', 'devices', 'release', 'browser', 'offline', 'levels', 'slimes', 'daily', 'leagues', 'ads', 'phone', 'restore', 'kids', 'data', 'delete', 'who']
# file, title key, description key, nav key, translated
PAGES = [
    ('index.html', 'meta_index_title', 'meta_index_desc', 'home', True),
    ('support.html', 'meta_support_title', 'meta_support_desc', 'support', True),
    ('press.html', 'meta_press_title', 'meta_press_desc', 'press', True),
    ('get.html', 'meta_get_title', 'meta_get_desc', 'get', True),
    ('privacy.html', 'Privacy Policy | Edgelings', 'How Edgelings handles your data: anonymous player accounts, rankings, purchases, ads and statistics with your consent, cookies on this website and your GDPR rights.', 'privacy', False),
    ('terms.html', 'Terms and Conditions | Edgelings', 'Terms and Conditions for the Edgelings game, including player names, fair play, coins and in-app purchases.', 'terms', False),
    ('404.html', 'Page not found | Edgelings', 'Page not found on edgelings.com.', '', False),
]
INDEXED = {'index.html', 'support.html', 'press.html', 'privacy.html', 'terms.html'}

EN = json.loads((SRC / 'i18n' / 'en.json').read_text(encoding='utf-8'))
TEXTS = {'en': EN}
for code, *_ in LANGS[1:]:
    p = SRC / 'i18n' / f'{code}.json'
    TEXTS[code] = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
MISSING = {}

css = (ROOT / 'assets' / 'site.css').read_bytes()
js = (ROOT / 'assets' / 'site.js').read_bytes()
V = hashlib.md5(css + js).hexdigest()[:8]

APPLE = '<svg width="26" height="30" viewBox="0 0 24 28" aria-hidden="true"><path fill="#fff" d="M19.6 14.9c0-3 2.5-4.5 2.6-4.6-1.4-2.1-3.6-2.4-4.4-2.4-1.9-.2-3.6 1.1-4.6 1.1-1 0-2.4-1.1-4-1-2 0-3.9 1.2-5 3-2.1 3.7-.5 9.2 1.5 12.2 1 1.5 2.2 3.1 3.8 3 1.5-.1 2.1-1 3.9-1s2.3 1 3.9 1c1.6 0 2.7-1.5 3.7-3 1.2-1.7 1.6-3.3 1.7-3.4-.1 0-3.1-1.2-3.1-4.9zM16.6 5.9c.8-1 1.4-2.4 1.2-3.8-1.2.1-2.6.8-3.5 1.8-.8.9-1.5 2.3-1.3 3.7 1.3.1 2.7-.7 3.6-1.7z"/></svg>'
PLAY = '<svg width="26" height="28" viewBox="0 0 24 26" aria-hidden="true"><path fill="#3BCCFF" d="M1.2.6 13.3 12.7 1.2 24.8c-.4-.2-.7-.7-.7-1.3V1.9c0-.6.3-1.1.7-1.3z"/><path fill="#FFD400" d="m17.4 8.6-4.1 4.1 4.1 4.1 4.6-2.6c1.3-.8 1.3-2.1 0-2.9z"/><path fill="#FF3A44" d="M13.3 12.7 1.2 24.8c.4.2 1 .2 1.6-.2l14.6-8.3z"/><path fill="#48FF48" d="M13.3 12.7 17.4 8.6 2.8.4C2.2 0 1.6 0 1.2.2z"/></svg>'


def base_of(code):
    folder = next(l[1] for l in LANGS if l[0] == code)
    return '/' + folder if folder else ''


def t(code, key):
    """Text for a key. Translated strings may hold {base} for language-relative links."""
    s = TEXTS[code].get(key)
    if not s:
        if code != 'en':
            MISSING.setdefault(code, set()).add(key)
        s = EN[key]
    return s.replace('{base}', base_of(code))


def plain(s):
    return html.unescape(re.sub(r'<[^>]+>', ' ', s)).replace('  ', ' ').strip()


def url_of(code, file):
    b = base_of(code)
    if file == 'index.html':
        return SITE + b + '/'
    if file == 'get.html':
        return SITE + b + '/get'
    return SITE + b + '/' + file


def badges(code, place):
    # Official Apple and Google badge artwork, one file per language in img/badges/ (do not redraw or edit it).
    out = []
    for key, img, name in (('ios', f'/img/badges/apple-{code}.svg', 'App Store'), ('android', f'/img/badges/play-{code}.png', 'Google Play')):
        url = STORES.get(key, '')
        cls = 'ios' if key == 'ios' else 'and'
        if url:
            out.append(f'<a class="sbadge" href="{html.escape(url)}" rel="noopener" data-store="{key}" data-place="{place}"><img class="{cls}" src="{img}" alt="{name}" loading="lazy" decoding="async"></a>')
        else:
            aria = html.escape(t(code, 'badge_soon_aria').replace('{store}', name))
            out.append(f'<span class="sbadge soon" role="img" aria-label="{aria}"><small>{t(code, "badge_soon")}</small><img class="{cls}" src="{img}" alt="" loading="lazy" decoding="async"></span>')
    return '<div class="badges">' + ''.join(out) + '</div>'


def qr(code):
    return (f'<div class="qr"><img src="/img/qr-get.svg" alt="{html.escape(t(code, "qr_alt"))}" width="92" height="92" loading="lazy">'
            f'<span>{t(code, "qr_text")}</span></div>')


def faq_html(code):
    return '\n'.join(f'<details id="{i}"><summary>{t(code, f"faq_{i}_q")}</summary><p>{t(code, f"faq_{i}_a")}</p></details>' for i in FAQ_IDS)


def fill(code, tpl):
    tpl = (tpl.replace('{{BADGES_HERO}}', badges(code, 'hero')).replace('{{BADGES_DEMO}}', badges(code, 'demo'))
           .replace('{{BADGES_BAND}}', badges(code, 'band')).replace('{{BADGES}}', badges(code, 'page'))
           .replace('{{QR}}', qr(code)).replace('{{FAQ}}', faq_html(code)).replace('{{STORES_JSON}}', json.dumps(STORES))
           .replace('{{LANG}}', code).replace('{{base}}', base_of(code)))
    tpl = re.sub(r'\{\{PTS:(\d+)\}\}', lambda m: t(code, 'slime_points').replace('{n}', m.group(1)), tpl)
    return re.sub(r'\{\{([a-z0-9_]+)\}\}', lambda m: t(code, m.group(1)), tpl)


def jsonld(code, file, desc):
    hl = next(l[2] for l in LANGS if l[0] == code)
    org = {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'Edgelings', 'url': SITE + '/', 'logo': SITE + '/img/icon-512.png', 'email': 'info@edgelings.com',
           'founder': {'@type': 'Person', 'name': 'Matej Mesko'}, 'address': {'@type': 'PostalAddress', 'addressCountry': 'SI'}}
    graph = [org, {'@type': 'WebSite', '@id': SITE + '/#site', 'name': 'Edgelings', 'url': SITE + '/', 'publisher': {'@id': SITE + '/#org'},
                   'inLanguage': [l[2] for l in LANGS]}]
    if file == 'index.html':
        game = {'@type': ['VideoGame', 'MobileApplication'], '@id': SITE + '/#game', 'name': 'Edgelings', 'url': url_of(code, file), 'description': desc,
                'image': SITE + '/og-image.png', 'screenshot': [SITE + f'/media/{s}.webp' for s in ('shot-edge', 'shot-merge', 'shot-honey', 'shot-ice', 'shot-king')],
                'gamePlatform': ['iOS', 'Android'], 'operatingSystem': 'iOS, Android', 'applicationCategory': 'GameApplication',
                'genre': ['Casual', 'Puzzle', 'Arcade'], 'playMode': 'SinglePlayer', 'inLanguage': hl, 'availableLanguage': [l[2] for l in LANGS],
                'isAccessibleForFree': True, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'},
                'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'},
                'trailer': {'@type': 'VideoObject', 'name': 'Edgelings trailer', 'description': 'Gameplay trailer of Edgelings.', 'thumbnailUrl': SITE + '/media/trailer.webp',
                            'contentUrl': SITE + '/media/trailer.mp4', 'uploadDate': '2026-11-18', 'duration': 'PT38S'}}
        same = [u for u in STORES.values() if u]
        if same:
            game['sameAs'] = same
        graph.append(game)
    if file in ('index.html', 'support.html'):
        graph.append({'@type': 'FAQPage', 'inLanguage': hl, 'mainEntity': [{'@type': 'Question', 'name': plain(t(code, f'faq_{i}_q')),
                      'acceptedAnswer': {'@type': 'Answer', 'text': plain(t(code, f'faq_{i}_a'))}} for i in FAQ_IDS]})
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False) + '</script>'


def suggest_map():
    out = {}
    for code, folder, hl, name, _ in LANGS:
        out[code] = {'text': t(code, 'suggest_text').replace('{lang}', name), 'go': t(code, 'suggest_go'), 'no': t(code, 'suggest_no'), 'html': hl}
    return out


SUGGEST = None


def shell(code, file, title, desc, key, body, translated):
    b = base_of(code)
    hl, name, fcls = next((l[2], l[3], l[4]) for l in LANGS if l[0] == code)
    url = url_of(code, file)
    cur = ' aria-current="page"'
    home = file == 'index.html'
    pre = '' if home else b + '/'
    nav = ''.join(f'<a href="{h}"{cur if key == k else ""}>{t(code, n)}</a>' for k, h, n in (
        ('home', b + '/', 'nav_home'), ('play', pre + '#play', 'nav_play'), ('video', pre + '#video', 'nav_video'),
        ('features', pre + '#features', 'nav_features'), ('slimes', pre + '#slimes', 'nav_slimes'), ('support', b + '/support.html', 'nav_support')))
    noindex = file not in INDEXED
    head = '<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'
    if translated and not noindex:
        alts = ''.join(f'\n<link rel="alternate" hreflang="{l[2]}" data-code="{l[0]}" href="{url_of(l[0], file)}">' for l in LANGS)
        head += alts + f'\n<link rel="alternate" hreflang="x-default" href="{url_of("en", file)}">'
    elif translated:
        head += ''.join(f'\n<link rel="alternate" hreflang="{l[2]}" data-code="{l[0]}" href="{url_of(l[0], file)}">' for l in LANGS)
    if home:
        head += '\n<link rel="preload" as="image" href="/media/hero.webp" fetchpriority="high">'
    if fcls == '':
        head += '\n<link rel="preload" href="/fonts/lilita-one-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>'
    app_banner = f'<meta name="apple-itunes-app" content="app-id={CFG["appStoreId"]}">' if CFG.get('appStoreId') and CFG.get('smartBanner') else ''
    edg = json.dumps({'sb': CFG['supabaseUrl'], 'sbKey': CFG['supabaseKey'], 'ph': CFG['posthogKey'], 'phHost': CFG['posthogHost'],
                      'lang': code, 'base': b, 'suggest': SUGGEST if translated else {}}, ensure_ascii=False)
    # Language menu: same page in every language. English-only pages offer the home page of each language.
    target = file if translated else 'index.html'
    menu = ''.join(f'<a href="{url_of(l[0], target).replace(SITE, "")}" hreflang="{l[2]}" lang="{l[2]}" data-setlang="{l[0]}"{cur if l[0] == code else ""}>{l[3]}</a>' for l in LANGS)
    flangs = ''.join(f'<a href="{url_of(l[0], target).replace(SITE, "")}" hreflang="{l[2]}" lang="{l[2]}" data-setlang="{l[0]}"{cur if l[0] == code else ""}>{l[3]}</a>' for l in LANGS)
    legal_p = t(code, 'foot_privacy') if code == 'en' else t(code, 'foot_privacy_en')
    legal_t = t(code, 'foot_terms') if code == 'en' else t(code, 'foot_terms_en')
    globe = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4c2.4 2.4 3.6 5.3 3.6 8.6s-1.2 6.2-3.6 8.6c-2.4-2.4-3.6-5.3-3.6-8.6S9.6 5.8 12 3.4z"/></svg>'
    return f'''<!doctype html><html lang="{hl}"{f' class="{fcls}"' if fcls else ''}><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{head}
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#1B1233">
{app_banner}
<meta property="og:site_name" content="Edgelings">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(t(code, 'meta_og_alt'))}">
<meta property="og:locale" content="{OG_LOCALE[code]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<link rel="stylesheet" href="/assets/site.css?v={V}">
{jsonld(code, file, desc)}
<script>window.EDG={edg}</script>
<script defer src="/assets/site.js?v={V}"></script>
</head><body>
<a class="sr" href="#main">{t(code, 'skip')}</a>
<header class="top"><div class="wrap">
<a class="logo" href="{b}/" aria-label="{html.escape(t(code, 'home_aria'))}"><img src="/img/logo.webp" alt="Edgelings" width="900" height="261"></a>
<nav aria-label="Main">{nav}</nav>
<details class="lang"><summary aria-label="{html.escape(t(code, 'lang_label'))}: {name}">{globe}<span>{name}</span></summary><div class="menu">{menu}</div></details>
<a class="pill small" href="{b}/get" data-place="header">{t(code, 'get_btn')}</a>
</div></header>
<div class="suggest" id="suggest" role="region" aria-live="polite"></div>
<main id="main" class="wrap">
{body}
</main>
<footer><div class="wrap">
<div class="grid">
<div>
<div class="brand"><img src="/img/icon-192.png" alt="" width="52" height="52"><span><b>Edgelings</b>{t(code, 'foot_tag1')}</span></div>
<p style="margin:0">{t(code, 'foot_tag2')}</p>
<div class="social" id="social" hidden aria-label="{html.escape(t(code, 'social_label'))}"></div>
</div>
<div><h4>{t(code, 'foot_game')}</h4><ul>
<li><a href="{b}/">{t(code, 'nav_home')}</a></li><li><a href="{b}/#play">{t(code, 'foot_demo')}</a></li><li><a href="{b}/#video">{t(code, 'foot_trailer')}</a></li><li><a href="{b}/#faq">{t(code, 'foot_faq')}</a></li><li><a href="{b}/press.html">{t(code, 'foot_press')}</a></li><li><a href="{b}/get" data-place="footer">{t(code, 'get_btn')}</a></li>
</ul></div>
<div><h4>{t(code, 'foot_help')}</h4><ul>
<li><a href="{b}/support.html">{t(code, 'nav_support')}</a></li><li><a href="{b}/support.html#delete">{t(code, 'foot_delete')}</a></li><li><a href="/privacy.html">{legal_p}</a></li><li><a href="/terms.html">{legal_t}</a></li>
<li><button class="linkish" type="button" data-cookies>{t(code, 'foot_cookies')}</button></li><li><a href="mailto:info@edgelings.com">info@edgelings.com</a></li>
</ul></div>
</div>
<nav class="langs" aria-label="{html.escape(t(code, 'lang_label'))}">{flangs}</nav>
<p class="op">{t(code, 'foot_operated')}</p>
</div></footer>
<div class="bottombar"><a class="pill purple" href="{b}/#play" data-demo>{t(code, 'bar_demo')}</a><a class="pill" href="{b}/get" data-place="bar">{t(code, 'get_btn')}</a></div>
<div class="consent" id="consent" role="dialog" aria-labelledby="c-h" aria-live="polite">
<h3 id="c-h">{t(code, 'cookie_h')}</h3>
<p>{t(code, 'cookie_p')} <a href="/privacy.html#website">{t(code, 'cookie_more')}</a></p>
<div class="btns"><button class="pill green" id="c-yes" type="button">{t(code, 'cookie_yes')}</button><button class="pill blue" id="c-no" type="button">{t(code, 'cookie_no')}</button></div>
</div>
</body></html>
'''


def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for file, _, _, _, translated in PAGES:
        if file not in INDEXED:
            continue
        codes = [l[0] for l in LANGS] if translated else ['en']
        for code in codes:
            alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l[2]}" href="{url_of(l[0], file)}"/>' for l in LANGS) if translated else ''
            if translated:
                alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url_of("en", file)}"/>'
            out.append(f'<url><loc>{url_of(code, file)}</loc><lastmod>{UPDATED}</lastmod>{alts}</url>')
    out.append('</urlset>')
    return '\n'.join(out) + '\n'


def llms():
    lines = ['# Edgelings', '', f'> {plain(EN["meta_index_desc"])}', '',
             'Edgelings is a casual mobile game for iPhone, iPad and Android, made by Matej Mesko in Slovenia. '
             'Players pull a slime back in a sling and let go. Slimes that stop close to the far edge of the table score the most. A slime that goes over the edge scores nothing. '
             '2 slimes of the same kind merge into a bigger one: Blip, Mossy, Sunny, Pomme and finally King Plum.', '',
             '## Key facts', '',
             '- Price: free, with optional in-app purchases and ads (Remove ads available)',
             '- Platforms: iPhone, iPad, Android phones and tablets',
             '- Levels: 1,200 across 6 tiers (Easy, Medium, Hard, Extra Hard, Ultimate, Crazy)',
             '- Modes: levels, a daily table that is the same for every player, weekly leagues (Bronze, Silver, Gold), rankings',
             '- Offline: all levels play offline',
             '- Languages: ' + ', '.join(l[3] for l in LANGS),
             '- Status: coming soon to the App Store and Google Play',
             '- Developer: Matej Mesko, Slovenia. Contact: info@edgelings.com', '',
             '## Pages', '',
             f'- [Home]({SITE}/): what the game is, playable demo, trailer, screenshots, features, slimes, FAQ',
             f'- [Support and FAQ]({SITE}/support.html): help, progress on a new phone, purchases, account deletion',
             f'- [Press kit]({SITE}/press.html): fact sheet, descriptions, logos, screenshots, trailer',
             f'- [Privacy Policy]({SITE}/privacy.html)',
             f'- [Terms and Conditions]({SITE}/terms.html)', '',
             '## Other languages', '']
    lines += [f'- [{l[3]}]({url_of(l[0], "index.html")})' for l in LANGS[1:]]
    lines += ['', '## FAQ', '']
    for i in FAQ_IDS:
        lines += [f'### {EN[f"faq_{i}_q"]}', '', plain(t("en", f"faq_{i}_a")), '']
    return '\n'.join(lines)


def build():
    global SUGGEST
    SUGGEST = suggest_map()
    count = 0
    for file, tk, dk, key, translated in PAGES:
        tpl = (SRC / 'pages' / file).read_text(encoding='utf-8')
        for code, folder, *_ in (LANGS if translated else LANGS[:1]):
            title = t(code, tk) if translated else tk
            desc = t(code, dk) if translated else dk
            body = fill(code, tpl)
            out = ROOT / folder / file if folder else ROOT / file
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(shell(code, file, title, desc, key, body, translated), encoding='utf-8', newline='\n')
            count += 1
    (ROOT / 'sitemap.xml').write_text(sitemap(), encoding='utf-8')
    (ROOT / 'llms.txt').write_text(llms(), encoding='utf-8', newline='\n')
    # Texts of the demo's own menu screens, in every language. Read by /demo/ at start.
    demo = {code: {k: t(code, k) for k in EN if k.startswith('dm_')} for code, *_ in LANGS}
    (ROOT / 'demo').mkdir(exist_ok=True)
    (ROOT / 'demo' / 'strings.json').write_text(json.dumps(demo, ensure_ascii=False), encoding='utf-8')
    # Press kit zip: logo, icon, key art, screenshots, trailer and slime renders.
    with zipfile.ZipFile(ROOT / 'media' / 'edgelings-press-kit.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for p in ['img/logo.webp', 'img/icon-512.png', 'og-image.png', 'media/trailer.mp4'] + [f'media/{n}.webp' for n in ('shot-edge', 'shot-merge', 'shot-honey', 'shot-ice', 'shot-king', 'shot-complete', 'shot-demo')] \
                + [f'img/{n}.webp' for n in ('slime1', 'slime2', 'slime3', 'slime4', 'slime5', 'mag', 'ghost', 'heavy', 'boom', 'myst')]:
            if (ROOT / p).exists():
                z.write(ROOT / p, 'edgelings-press-kit/' + p.split('/')[-1])
    # Writing checks on English visible text.
    for file, *_ in PAGES:
        tx = re.sub(r'<script.*?</script>', ' ', (ROOT / file).read_text(encoding='utf-8'), flags=re.S)
        tx = re.sub(r'<[^>]+>', ' ', tx)
        for bad in ('—', "n't", "'re", "'ll", "'ve", '!'):
            if bad in tx:
                print(f'warning: {file} contains {bad!r}')
    for code, keys in MISSING.items():
        print(f'missing {len(keys)} texts in {code}, English shown')
    print('built', count, 'pages in', len(LANGS), 'languages, version', V)


if __name__ == '__main__':
    build()
