# Security and integrity review: batch4

Languages: zh-Hans, zh-Hant
Reviewer: final safety reviewer. No final.json was edited.

## Method
- `check.py` run on both files: both print "ok". Both files have the same 259 keys as en.json.
- Automated scan against en.json for every key: tags, href values, URLs, emails, domains, script and event attributes, digit sets per key, banned punctuation (em/en dash, semicolon, exclamation mark), and counts of the brand and slime names (Edgelings, App Store, Google Play, iPhone, iPad, Android, Blip, Mossy, Sunny, Pomme, King Plum, reportaproblem.apple.com, info@edgelings.com, edgelings.com, Matej Mesko).
- Every text in both languages read in full. The legal and privacy keys (`cookie_p`, `faq_data_a`, `faq_kids_a`, `faq_phone_a`, `faq_restore_a`, `faq_ads_a`, `faq_free_a`, `sup_delete_*`, `sup_refund_p`) were compared sentence by sentence with the English.
- UI labels checked against each `app_terms.json`: 设置/設定, 删除我的账号/刪除我的帳號, 全部删除/全部刪除, 恢复购买/恢復購買, 移除广告/移除廣告, 新手礼包/新手禮包, 日榜/周榜/总榜 (週榜/總榜), the 3 leagues, the 6 tiers and the 5 specials all match the app exactly.

Scan results checked by hand and found harmless:
- "0" or "0 分" written for "scores nothing" (meta_index_desc, hero_lead, score_msg0, faq_what_a, press_long1). Meaning unchanged.
- Added "1" as a measure-word count ("1 只更大的", "1 次额外机会", "第1個世界", "1張新桌子"). Meaning unchanged.
- Mossy named in `loop_merge_aria` (English "Mossies") and King Plum in `shot5` (English "the King"). Names kept, not declined.
- `faq_lead` drops the "1" of "in 1 place" (natural Chinese idiom). Meaning unchanged.
- zh-Hant `faq_devices_a` adds "Edgelings" as subject. Meaning unchanged.
- `faq_who_a`: the email is followed by a Chinese full stop. The address is unchanged.
- No new links, URLs, emails, phone numbers, markup or changed hrefs. No scripts or event attributes.
- `sup_delete_mail` keeps the exact English subject "Delete my Edgelings account" inside 「」 / “” quotes in both languages.
- `cookie_p` (decline means anonymous visit counting only, nothing stored on the device), `faq_data_a` (anonymous account, name, progress, scores, purchases, statistics and personalised ads only with consent, EU storage), `faq_ads_a` (small banner on menus, never during a level, opt-in ads for an extra slime or try, Remove ads takes the banner away for good, opt-in ads stay available), `faq_free_a` (free, ads, optional purchases, never need to buy to finish a level), `faq_restore_a` (permanent purchases only, consumables not restored, sign-in keeps them), `faq_phone_a` (sign-in is "即将推出 / 即將推出", not yet live), `sup_delete_game` (removed for good, phone must be online), `sup_delete_mail` (30 days, email confirmation), `sup_delete_note` (no cancellation or refund, refunds by Apple or Google) and `sup_refund_p` match the English in both languages.
- Badge line zh-Hans `badge_play_pre` "下载应用，请到" is Google's official Simplified Chinese badge wording.
- No added promises (prices, "always free", "no ads", dates, guarantees). No offensive or unsafe wording. No wording that targets children directly. Address is 您 throughout, as the app.

## zh-Hans
pass, with 2 notes (optional polish, not required for publishing):

1. `faq_kids_a`. Issue: "应先征得家长同意" means "should first obtain a parent's consent", slightly stronger than English "should ask a parent". Suggested fix: "未满 18 岁的玩家在购买任何东西前，应先询问家长。" Severity: note.
2. `sup_delete_mail`. Issue: "如果您已卸载游戏" ("if you have uninstalled the game") is a little narrower than "if you no longer have the game installed" (for example a new phone where it was never installed). Suggested fix: "如果您的设备上已不再安装游戏". Severity: note.

## zh-Hant
pass, with 1 note:

1. `loop_merge_h`, `feat4_h`, `king_p` and other merge texts. Issue: 合體 can carry a joking sexual double meaning in Taiwanese slang. It is, however, the standard game term (mecha and card games use it widely) and it is the approved term in the app's APP_GLOSSARY.md ("合體！ 皇家合體！"), so the site must match the app. Suggested fix: none on the website. If the term is ever reconsidered, change it in the app and the site together. Severity: note.
