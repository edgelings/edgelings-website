# Security and integrity review: batch3

Languages: tr, ru, uk, hi, th, ja, ko
Reviewer: final safety reviewer. No final.json was edited.

## Method
- `check.py` run on every file: all 7 print "ok".
- Automated scan against en.json for every key: same key set, tags and href values, URLs, emails, domains, script/event attributes, digit sets per key, counts of brand and slime names (Edgelings, App Store, Google Play, iPhone, iPad, Android, Blip, Mossy, Sunny, Pomme, King Plum, reportaproblem.apple.com, Matej Mesko, info@edgelings.com, edgelings.com), dashes, semicolons, exclamation marks, and hidden or control characters (none found).
- Every text in every language read in full. The legal and privacy keys (`cookie_p`, `faq_data_a`, `faq_kids_a`, `faq_phone_a`, `faq_restore_a`, `faq_ads_a`, `faq_free_a`, `sup_delete_*`, `sup_refund_p`) compared sentence by sentence with the English and with each language's `app_terms.json`.

Scan results checked by hand and found harmless:
- "2 Mossies" written as "2 Mossy" with a counter word (all 7). Name kept, not declined.
- "nothing" written as "0" (th, ja, ko) and "1 place" written as "one place" (ru, th, ja, ko). "3 times" written as a word ("втричі", uk). Meaning unchanged.
- ja and ko add the counter "1" in `faq_ads_a` ("1 slime", "1 try"), which matches "an extra slime or an extra try".
- tr `meta_index_title` says "free mobile game" instead of naming iPhone and Android. No fact lost (the description names all 3 platforms).
- "Edgelings" added as subject in some FAQ answers (tr, hi, th). Meaning unchanged.
- Email address checks in ja/ko flagged only because CJK text touches the address. The address itself is unchanged in all 7. hi, th, ja, ko drop the final full stop after the address in `faq_who_a`, which is harmless.
- No new links, URLs, emails, phone numbers, markup or changed hrefs in any language.
- `sup_delete_mail` keeps the exact English subject "Delete my Edgelings account" in all 7 languages.
- `sup_delete_game` and `faq_delete_a` use the exact app labels for Settings, Delete my account and Delete everything in all 7 languages.
- `sup_delete_note`, `sup_delete_game` (removed for good, phone must be online), `sup_delete_mail` (30 days, email confirmation), `cookie_p` (decline means anonymous counting only, nothing stored), `faq_data_a` (EU storage, statistics and personalised ads only with consent), `faq_ads_a` (banner on menus only, never during a level, Remove ads removes the banner for good, opt-in ads stay available), `faq_restore_a` (consumables not restored, sign-in keeps them), `faq_phone_a` (sign-in is "coming", not yet live), `faq_free_a` (no purchase needed to finish a level) and `faq_kids_a` (13 and over, under 18 should ask a parent) match the English in all 7 languages.
- No added prices, rewards, dates, "always free", "no ads" or guarantees. No offensive, unsafe or double-meaning wording found. Special slime names "Ghost" (ru Призрак, uk Привид, hi भूत, th ผี, ja ゴースト, ko 유령) and "Sparkler" are the approved app terms and are harmless in context.

## tr
pass

## ru
pass

## uk
1 finding.
- key: `faq_kids_a`
  - issue: last sentence switches to direct address of minors: "Якщо вам менше 18 років, запитайте батьків, перш ніж щось купувати." ("If you are under 18, ask your parents before buying anything."). English is 3rd person ("Players under 18 should ask a parent"). The meaning is still protective, but the brief asks to avoid wording that speaks to children directly.
  - suggested fix: "Гравцям, молодшим за 18 років, варто запитати батьків, перш ніж щось купувати."
  - severity: note

## hi
1 finding.
- key: `band_p`
  - issue: "खेलना बिल्कुल मुफ़्त" means "completely free to play". English is "Free to play." The game has ads and optional purchases, so "completely" slightly strengthens the claim. Not a new promise.
  - suggested fix: "जल्द ही iPhone, iPad और Android पर। खेलना मुफ़्त।"
  - severity: note

## th
pass

## ja
1 finding.
- key: `faq_daily_a`
  - issue: "購入したお助けアイテムは使えないので" drops "there" (on the daily table). Read alone it can suggest bought helpers cannot be used at all. The paragraph context is the daily table, so the risk is low.
  - suggested fix: "デイリーテーブルでは購入したお助けアイテムは使えないので、公平な勝負になります。"
  - severity: note

## ko
1 finding.
- key: `faq_levels_a`
  - issue: "앱 업데이트 없이도 서버에서 새 레벨이 계속 추가돼요" means "new levels keep being added from the server". "계속" (continuously) reads as an ongoing content promise. English only says "More levels arrive from the server without an app update."
  - suggested fix: "새 레벨은 앱 업데이트 없이 서버에서 추가돼요."
  - severity: note
