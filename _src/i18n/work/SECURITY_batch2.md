# Security and integrity review: batch2

Languages: hr, sl, ro, id, vi
Reviewer: final safety reviewer. No final.json was edited.

## Method
- `check.py` run on every file: all 5 print "ok". All keys present, no extra keys.
- Automated scan against en.json for every key: href values, tags, URLs, emails, `www.` strings, phone-like numbers, digit sets, added em dash, en dash, semicolon or exclamation mark, and counts of the brand and slime names (Edgelings, App Store, Google Play, iPhone, iPad, Android, Blip, Mossy, Sunny, Pomme, King Plum, Matej Mesko, reportaproblem.apple.com, info@edgelings.com, edgelings.com). Nothing missing or added.
- App UI labels used in legal keys (Settings, Delete my account, Delete everything, Restore purchases, Remove ads, Starter pack) compared with each `app_terms.json`: all 5 languages match.
- Every text in every language read in full. Legal and privacy keys compared sentence by sentence with the English.

Scan results checked by hand and found harmless:
- Digit differences only from added counting words "1" (id, vi `loop_merge_p`, `feat4_p`, `faq_how_a`, `faq_ads_a`, `press_long2`), a dropped "1" (sl `feat2_p` "Vsak dan nova miza") and "1 place" written as "un singur loc" (ro `faq_lead`). Meaning unchanged.
- `sup_delete_mail` keeps the exact English subject "Delete my Edgelings account" in all 5 languages, with 30 days and email confirmation.
- `cookie_p`, `faq_data_a`, `faq_kids_a` (13 and over, under 18 ask a parent), `faq_phone_a` (sign-in is "coming"), `sup_delete_game`, `sup_delete_note`, `sup_refund_p` match the English in all 5 languages.
- No added promises, prices, dates or guarantees beyond the points below. No offensive, unsafe or double-meaning wording found. No wording that targets children directly. vi "đừng lố" (do not overdo it) is colloquial but harmless.

## hr
pass

## sl
1. `faq_restore_a`
   - Issue: "Kovanci in drugi porabljeni predmeti" means "coins and other used-up items". It mirrors the ambiguity of the English but can read as "items already spent", while the intent is consumables in general (unspent coins are not restored either).
   - Suggested fix: "Kovanci in drugi potrošni predmeti se na ta način ne obnovijo."
   - Severity: note

## ro
pass

## id
1. `faq_restore_a`
   - Issue: "Koin dan item lain yang sudah terpakai" means "coins and other items that have already been used". The English means consumable items (coins and items that get used up). As written, the sentence implies only spent items are not restored, and the next sentence ("Item tersebut tetap aman jika Anda masuk akun") then says used items stay safe with sign-in. The restore scope is misstated.
   - Suggested fix: "Koin dan item habis pakai lainnya tidak dipulihkan dengan cara ini. Item tersebut tetap aman jika Anda masuk akun."
   - Severity: fix

## vi
1. `faq_restore_a`
   - Issue: "Xu và các vật phẩm đã dùng hết" means "coins and items that have already been used up". Same problem as id: it suggests only spent items are not restored, and "Đăng nhập sẽ giữ lại những thứ đó" then says sign-in keeps the used items. The English means consumables.
   - Suggested fix: "Xu và các vật phẩm tiêu hao khác sẽ không được khôi phục theo cách này. Đăng nhập sẽ giữ lại những thứ đó."
   - Severity: fix
2. `faq_free_a`
   - Issue: "được tải về và chơi hoàn toàn miễn phí" adds "hoàn toàn" (completely). The English says only "free to download and free to play". The game has ads and purchases, so "completely free" overstates on a legal key.
   - Suggested fix: "Có. Edgelings được tải về và chơi miễn phí."
   - Severity: fix
3. `faq_ads_a`
   - Issue: "vẫn luôn sẵn có" adds "luôn" (always) to "stay available", a slightly stronger promise than the English.
   - Suggested fix: "Các quảng cáo bạn tự chọn xem vẫn sẵn có."
   - Severity: note
4. `hero_lead`, `meta_index_desc`
   - Issue: "Rơi khỏi mép là mất trắng" (fall off the edge and you lose everything) can be read as losing all points, while the English says only that the slime scores nothing.
   - Suggested fix: "Rơi khỏi mép là không được điểm."
   - Severity: note
