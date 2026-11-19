"""Tells Bing, Yandex, Seznam and other IndexNow engines that pages changed.
Run after GitHub Pages has published a change: python _src/indexnow.py
The key file 455d51a266738de31276645f39afb55e.txt sits at the site root and proves the site is ours."""
import json, pathlib, re, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEY = '455d51a266738de31276645f39afb55e'
urls = re.findall(r'<loc>([^<]+)</loc>', (ROOT / 'sitemap.xml').read_text(encoding='utf-8'))
body = json.dumps({'host': 'edgelings.com', 'key': KEY, 'keyLocation': f'https://edgelings.com/{KEY}.txt', 'urlList': urls}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
with urllib.request.urlopen(req, timeout=20) as r:
    print('IndexNow answered', r.status, 'for', len(urls), 'pages')
