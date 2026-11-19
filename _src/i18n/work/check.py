"""Checks a website translation against en.json. Usage: python3 check.py <lang>/<file>.json"""
import json, re, sys, pathlib
EN = json.load(open(pathlib.Path(__file__).resolve().parents[1] / "en.json", encoding='utf-8'))
PH = re.compile(r'\{\w+\}')
p = sys.argv[1]
T = json.load(open(p, encoding='utf-8'))
SHORT = re.compile(r'^(nav_|get_btn|bar_demo|demo_play_now|demo_keep|demo_close|cookie_yes|cookie_no|suggest_go|suggest_no|fact_|badge_|foot_|lang_label|dm_|loop_.*_h|slime_special|slime_surprise|chain_then)')
CJK = re.compile(r'[぀-ヿ㐀-鿿가-힯฀-๿]')
errs = []
for k, en in EN.items():
    if k not in T or not isinstance(T[k], str) or not T[k].strip():
        errs.append(f'{k}: missing'); continue
    s = T[k]
    if sorted(re.findall(r'\{\w+\}', en)) != sorted(re.findall(r'\{\w+\}', s)):
        errs.append(f'{k}: placeholders differ {PH.findall(en)} vs {PH.findall(s)}')
    if sorted(re.findall(r'<[^>]+>', en)) != sorted(re.findall(r'<[^>]+>', s)):
        errs.append(f'{k}: HTML tags differ')
    if re.search(r'[–—;]', s): errs.append(f'{k}: dash or semicolon')
    if '!' in s and '!' not in en: errs.append(f'{k}: exclamation mark')
    if '！' in s: errs.append(f'{k}: exclamation mark')
    for keep in ('Edgelings', 'App Store', 'Google Play', 'info@edgelings.com'):
        if keep in en and keep not in s: errs.append(f'{k}: "{keep}" missing')
    if SHORT.match(k):
        n_en, n_s = len(re.sub(r'<[^>]+>', '', en)), len(re.sub(r'<[^>]+>', '', s))
        limit = n_en * (1.0 if CJK.search(s) else 1.6) + 6
        if n_s > limit: errs.append(f'{k}: too long ({n_s} chars, English {n_en})')
for k in T:
    if k not in EN: errs.append(f'{k}: unknown key')
if list(T.keys()) != [k for k in EN if k in T]: errs.append('key order differs from en.json')
print('ok' if not errs else '\n'.join(errs))
