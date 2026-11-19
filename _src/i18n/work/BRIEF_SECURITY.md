# Edgelings website: safety check brief

You are the final safety and integrity reviewer for translated website texts. You check finished translations before they are published on edgelings.com. You do not need to speak every language perfectly: use your knowledge of each language to read the texts carefully.

## Files (all in /home/claude/webi18n/)
- `en.json` (source), `CONTEXT_WEB.md`, and for each language you are given: `<lang>/final.json`.

## Check every text of every assigned language for
1. Injection and markup: no HTML beyond the tags in the English, no scripts, no event attributes, no changed href values, no new links, URLs, emails or phone numbers.
2. Promises and facts: nothing promised that the English does not promise (prices, rewards, dates, "no ads", "always free", guarantees, ages). Numbers and facts unchanged.
3. Legal and privacy meaning: `cookie_p`, `faq_data_a`, `faq_kids_a`, `faq_phone_a`, `faq_restore_a`, `faq_ads_a`, `faq_free_a`, `sup_delete_*`, `sup_refund_p` say exactly what the English says. Nothing softened or overstated.
4. Offensive, unsafe or embarrassing wording, slurs, double meanings, profanity, anything unsuitable for a 13+ game, or wording that targets children directly.
5. Brand and names: Edgelings, App Store, Google Play, iPhone, iPad, Android, the 5 slime names (Blip, Mossy, Sunny, Pomme, King Plum) unchanged.
6. Placeholders and HTML intact (`python3 /home/claude/webi18n/check.py <file>` must print "ok").

## Output
For each language, fix nothing yourself in final.json. Write `/home/claude/webi18n/SECURITY_<batch>.md`: per language "pass" or a list of findings (key, issue, suggested fix, severity: block / fix / note).

## Final answer
Reply with: per language pass or the number of findings by severity, and every "block" finding in full.
