# Thai (th) merge log

Format: key, reviewer, decision, reason.

- faq_leagues_a, A+B, accepted, both identical. ตกลง reads as "agree", เลื่อนชั้น / ตกชั้น is standard league wording.
- sup_delete_game, A+B, adapted, quotes on the 3 labels from both. A was right that "for this" was lost, wrote "ขณะลบบัญชี" instead of A's "ขั้นตอนนี้..." for a smoother sentence.
- sup_delete_note, A, accepted, clearer and more precise for a legal-like text.
- sup_delete_mail, A+B, accepted B, both fix ไม่ได้...ไว้แล้ว. B's word order (ถ้าในเครื่องของคุณไม่ได้ติดตั้งเกมนี้แล้ว) reads more naturally, A rejected in its favour.
- faq_ads_a, A+B, accepted A, both quote ลบโฆษณา. A's การซื้อ "ลบโฆษณา" makes clear it is a purchase, B's bare quoted label at sentence start rejected.
- faq_free_a, A+B, adapted, quote "ลบโฆษณา" from both. Kept the opener ฟรี (Thai answers ฟรีไหม this way) instead of B's ใช่, took B's fix for the triple ฟรี: ดาวน์โหลดและเล่นได้ฟรี.
- faq_restore_q, A+B, adapted, ปุ่ม "กู้คืนการซื้อ" ใช้ทำอะไร. B's ปุ่ม names the button clearly, A's ใช้ทำอะไร is shorter than มีไว้ทำอะไร.
- faq_restore_a, A, accepted, product name quoted so it is not read as "delete ads".
- faq_delete_a, A+B, accepted, both identical, labels quoted.
- sup_p, A+B, accepted, both identical, label quoted.
- sup_refund_p, A+B, accepted, both identical, Google Play menu names quoted.
- faq_levels_a, A, accepted, restores the fact that more levels do arrive (not only "can").
- faq_slimes_a, A, accepted, first sentence now has a verb.
- suggest_text, A+B, accepted B, rejected A. build.py fills {lang} with ไทย (language menu name), so B gives หน้านี้มีฉบับภาษาไทยด้วย with ภาษา once. A's เวอร์ชันไทย is less natural.
- hero_video_aria, A+B, accepted A, both fix the trailer clash and add the colon. A's ภาพการเล่นจริง matches GLOSSARY_WEB for gameplay, B's ภาพการเล่น rejected.
- score_blob_alt, A+B, accepted, both identical. เรา avoids the gendered ฉัน per APP_GLOSSARY.
- feat3_p, A+B, accepted B, rejected A. Both fix the "Silver and Gold at once" reading, B's ขึ้นลีกเงิน สู่ลีกทอง is shorter and has better climbing rhythm.
- hero_tag, B, accepted, สำหรับ read as translated. เกมสั้นๆ ไว้เล่นตอนพักเบรก is natural slogan Thai.
- foot_tag2, B, accepted, same slogan as hero_tag.
- feat_h2, B, accepted, มีดีกว่า is awkward. ไม่ใช่แค่ไล่เล่นทีละด่าน is natural.
- step1, B, accepted, word order no longer calqued.
- faq_how_a, B, accepted, consistent with step1.
- press_long1, B, accepted, consistent with step1.
- faq_phone_a, B, accepted, กำลังจะมา was a calque. เร็วๆ นี้จะรองรับ keeps the "coming" fact.
- faq_devices_a, B, accepted, answer now stands alone with a subject. No fact added.
- faq_data_a, B, accepted, full sentence instead of a bare noun list. Facts unchanged.
- sparkler_p, B, accepted, ระมัดระวัง is the idiomatic form.
- glossary: UI labels in quotes, A+B, accepted, applied to buttons and menu items in running text (ตั้งค่า, ลบบัญชี, ลบทั้งหมด, ลบโฆษณา, กู้คืนการซื้อ, Google Play menus). Tab, league and tier names (รายวัน, ทอง, ยาก...) stay bare since they read as ordinary words in lists and neither reviewer quoted them.
- glossary: move up / move down, A+B, accepted, เลื่อนชั้น / ตกชั้น.
- glossary: One quick game for a short break, B, accepted, เกมสั้นๆ ไว้เล่นตอนพักเบรก.
- glossary: More than a level list, B, accepted, ไม่ใช่แค่ไล่เล่นทีละด่าน.
- glossary: Delete my account note, A, accepted as a flag only. Site keeps ลบบัญชี from app_terms.json. APP_GLOSSARY's mention of ลบบัญชีของฉัน conflicts and should be checked against the live app.

Totals by key: accepted 24, adapted 3, rejected 5 (rejected = the losing version where both reviewers changed the same key: A on sup_delete_mail, suggest_text, feat3_p, B on faq_ads_a, hero_video_aria). No key was left unchanged against both reviewers. Glossary items: 5 accepted.
