# Security and integrity review: batch1

Languages: de, es, es-419, fr, it, nl, pt, pt-BR, pl
Reviewer: final safety reviewer. No final.json was edited.

## Method
- `check.py` run on every file: all 9 print "ok".
- Automated scan against en.json for every key: href values, URLs, emails, domains, phone-like numbers, script/event attributes and tags other than `<b>`, `<a>`, `<br>`, digit sets per key, and counts of the brand and slime names (Edgelings, App Store, Google Play, iPhone, iPad, Android, Blip, Mossy, Sunny, Pomme, King Plum, reportaproblem.apple.com, Matej Mesko).
- Every text in every language read in full. The legal and privacy keys (`cookie_p`, `faq_data_a`, `faq_kids_a`, `faq_phone_a`, `faq_restore_a`, `faq_ads_a`, `faq_free_a`, `sup_delete_*`, `sup_refund_p`) were compared sentence by sentence with the English.

Scan results checked by hand and found harmless:
- "2 Mossies" written as "Mossy" or "Mossy-slijmpjes" (name kept and not declined, as the rules require).
- "3 times" written as "el triple" (es), "0" written for "nothing" (de), "1 groter" (nl), "en un solo lugar" (es, pt, fr). The meaning is unchanged.
- "Edgelings" added as a subject in some FAQ answers (de, fr, nl, pl). The meaning is unchanged.
- de `faq_delete_a`: the address is followed by a full stop that ends the sentence. The address is unchanged.
- No new links, URLs, emails, phone numbers, markup or changed hrefs in any language.
- `sup_delete_mail` keeps the exact English subject "Delete my Edgelings account" in all 9 languages.
- `sup_delete_note`, `sup_delete_game` (removed for good, phone must be online), `sup_delete_mail` (30 days, email confirmation), `cookie_p` (decline means anonymous counting only, nothing stored), `faq_data_a` (EU storage, consent for statistics and personalised ads), `faq_ads_a` (banner on menus only, never during a level, Remove ads takes the banner away for good, opt-in ads stay available), `faq_restore_a` (consumables not restored, sign-in keeps them), `faq_phone_a` (sign-in is "coming", not yet live) and `faq_kids_a` (13 and over, under 18 should ask a parent) match the English in all 9 languages.
- No added promises (prices, "always free", "no ads", dates, guarantees). No offensive or unsafe wording. No wording that targets children directly.

## de
pass

## es
pass

## es-419
pass

## fr
pass

## it
pass

## nl
pass

## pt
pass

## pt-BR
pass

## pl
1 finding.
- key: all slime texts (`nav_slimes`, `slimes_h2`, `meta_*`, `faq_slimes_a` and others) use "glutek" / "glutki"
  - issue: "glut" in colloquial Polish also means snot. It is the established Polish word for toy slime, and it is the approved app term in `pl/APP_GLOSSARY.md` ("slime | glutek"), so it matches the app.
  - suggested fix: none. Keep it for consistency with the app. Change it only if the app term is changed.
  - severity: note
