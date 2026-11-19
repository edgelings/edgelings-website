# Edgelings website: what the texts are

## The website
edgelings.com is the marketing website of Edgelings, a free casual mobile game for iPhone, iPad and Android (launching soon on the App Store and Google Play).
Visitors should get excited and download the game. The tone is playful, warm, confident and short, like the website of a top mobile game. It must not read like a translation.
The English texts are in `en.json` (key: English text). Pages: home page (hero, playable browser demo, "how scoring works" toy, trailer, screenshots, features, slime cast, FAQ), support page, press kit, a "get the app" page, a cookie banner, the header and footer, and the menu screens of the small browser demo (keys starting with `dm_`).

## The game, in short
The player pulls back a small slime in a sling and lets go. It slides up a wooden table. The closer to the far edge it stops, the more points. Over the edge it falls off and scores 0. 2 slimes of the same kind merge into a bigger one: Blip, Mossy, Sunny, Pomme, King Plum (these 5 names stay in English, never declined). Specials: Magnet, Ghost, Heavy, Sparkler, Mystery (these ARE translated in the app: use the app's word, see `app_terms.json`). 1,200 levels in 6 tiers (Easy, Medium, Hard, Extra Hard, Ultimate, Crazy). A daily table, the same for every player in the world, 3 tries a day. Weekly leagues: Bronze, Silver, Gold. Plays offline.

## Consistency with the app (most important)
- The app is already translated. Your language folder holds `APP_GLOSSARY.md` (the app's approved terms and register rule) and `app_terms.json` (the app's exact translations of button and screen names).
- Use the APP_GLOSSARY terms for every game term (table, daily table, edge, bank, gold zone, merge, slime, league, coins, chest...).
- Where the website names something in the app (a button, a setting, a tab, a tier, a league, a special slime), use the exact text from `app_terms.json`, so players find it. Examples in English: "Settings", "Delete my account", "Delete everything", "Restore purchases", "Remove ads", "Daily", "Weekly", "All time", Bronze, Silver, Gold, the 6 tiers, the special slimes. If your language needs quotes or a particular case around a UI label, do what local apps do.
- Use the register rule from APP_GLOSSARY.md (formal or informal address) exactly as the app does.

## Rules for every text
- Keep every {placeholder} exactly: {n} (a number), {lang} (a language name written in its own language, e.g. "Deutsch"), {store} ("App Store" or "Google Play"), {base} (part of a link address, keep it inside href exactly).
- Keep HTML exactly: same tags, same attributes, same href values, same number of tags. You may move a tag to where it fits your sentence. Only these tags occur: <br>, <b>...</b>, <a href="...">...</a>. Translate the text between tags.
- Keep "Edgelings", "App Store", "Google Play", "iPhone", "iPad", "Android", "info@edgelings.com", "reportaproblem.apple.com", "edgelings.com" unchanged.
- Numbers stay digits. "1,200" is a number: write it as your language writes 1200 (for example 1.200 in German, 1 200 in French, 1200 is fine where usual). "38 seconds", "540 by 960", "30 days", "13 and over", "under 18", "10%", "3 times", "x2": keep the numbers.
- No exclamation mark unless the English has one. No em dash or en dash. No semicolons. No emojis. Use commas and full stops.
- Never guess the reader's gender. Rephrase to stay neutral.
- Do not add facts, links, brand names or advice. Keep every fact.
- Variants: es = Spain, es-419 = neutral Latin American, pt = Portugal, pt-BR = Brazil, fr = France, zh-Hans = Simplified Chinese (mainland), zh-Hant = Traditional Chinese (Taiwan), hi = Hindi in Devanagari, natural everyday Hindi (English loanwords only where Indian games use them).
- Sentence case for headings and buttons, as your language does in interfaces (no English Title Case).

## Space
- Header and button texts must be short: keys `nav_*`, `get_btn`, `bar_demo`, `demo_play_now`, `demo_keep`, `demo_close`, `cookie_yes`, `cookie_no`, `suggest_go`, `suggest_no`, `fact_*`, `badge_*`, `foot_*`, `lang_label`, `dm_*`, `loop_*_h`, `slime_special`, `slime_surprise`, `chain_then`. Aim for the English length. The checker refuses texts much longer than English for these keys.
- `hero_h1` is the big headline with a line break: "Close to the edge.<br>Not over it." Make it punchy and short, a real slogan in your language, keep the <br> between the 2 parts. `foot_tag1` is the same slogan on 1 line, without <br>. `hero_tag` and `foot_tag2` are the second slogan ("One quick game for a short break.").
- `dm_*` are drawn inside the game canvas on a phone-sized screen. Keep them very short. {n} is a number.

## Notes on some keys
- `meta_*_title`, `meta_*_desc`: search engine title and description. Titles up to about 60 characters, descriptions up to about 155. Write them so a person searching in your language would click. Keep "Edgelings" in the title.
- `suggest_text`: shown to a visitor whose browser is in your language while they read another language version. {lang} is your language's own name. Example: "This page is also available in Deutsch." Then buttons `suggest_go` ("Switch") and `suggest_no` ("No thanks").
- `badge_ios_pre` / `badge_play_pre`: the small line above "App Store" / "Google Play" on store badges. Use what Apple and Google use in your language on their official badges if you know it ("Laden im" / "Jetzt bei" in German), otherwise a short natural phrase.
- `badge_soon`: small line above the store name before launch ("Coming soon").
- `cookie_p`: a consent text. It must stay precise and complete: cookies are used to see how visitors use the site (demo plays and store clicks are examples). Declining means only anonymous counting with nothing stored on the device.
- `foot_privacy_en`, `foot_terms_en`: links to the Privacy Policy and Terms, which exist only in English. Say so ("Privacy (in English)").
- `sup_meta`: "We reply in English." stays: support answers in English.
- `faq_*`: the FAQ. Search engines and AI assistants read it, so answers must be complete, natural sentences that answer the question on their own.
- `score_pts` and `slime_points`: "{n} points" shown under a number.
- `press_*`: the press kit for journalists. `press_lang_v`: "24 languages".
- `step1`..`step4`: how to play, very short.

## Decisions after the translation round (reviewers and editors: apply these)
- `sup_delete_mail`: the email subject stays in English, exactly "Delete my Edgelings account", inside your language's quotes. Support works in English and recognises that subject.
- Fixed values: in `dm_more` {n} is always 1195, in `dm_first` {n} is always 5, in `dm_level` {n} is 1 to 5, in `score_pts` {n} is 0, 30, 60 or 90, in `slime_points` {n} is 10, 30, 90, 270 or 810. Forms like "Points: {n}" are fine where plurals would break.
- "tier": use the word the APP_GLOSSARY uses for the 6 difficulty stages (often "world"), so the site matches the app.
- Google Play menu names in `sup_refund_p` ("Payments and subscriptions", "Budget and history"): use the exact wording of Google Play in your language if you know it, otherwise a clear description.
- Store badge lines (`badge_ios_pre`, `badge_play_pre`): Apple's and Google's official badge wording in your language where it fits above the store name.
- A shorter footer label (for example "FAQ") is fine where the full word does not fit.
